#!/usr/bin/env python3
"""Build the group's blyg (Blygger protocol 0.3, Level 1) from blyg-src/.

Sources
  blyg-src/fragments/*.md   short items (SHOULD stay under 2,000 characters)
  blyg-src/threads/*.md     long items; a line holding only ![[<id>]] transcludes a fragment

Each source file starts with front matter:
  ---
  id: <26-char Crockford base32>     # permanent; create files with tools/blyg_new.py
  author: Name                       # optional per-item byline
  withdrawn: true                    # optional; publishes a withdrawal endcap
  pin: [1]                           # optional; versions promised forever (items/{id}/v{n}.json)
  generated_model: c3po              # optional; model for ::: generated blocks
  stub_of: {"origin": ..., "id": ..., "version": n, "cited": {...}}   # optional, threads only (0.3 §10.6):
                                     # one-line JSON naming what this thread responds to; or {"url": ...} for a plain web page
  ---

Images: put the file in blyg-src/media/ and write ![alt text](media/name.svg). Each version uses the
file as committed with it, published once at blyg/media/{sha256-prefix}.{ext} so a media URL always
serves the same bytes (0.3 §5.4). The link becomes absolute in content_md and content_html (§5.2), and
the item's media array lists it with its alt text.

Versions come from git: every commit that changes an item's content is one publish event,
dated by the commit and noted with the commit subject. Uncommitted edits are drafts and
are not published. Machine-generated passages are fenced as
  ::: generated
  ...
  :::
The fences never reach the wire: content_md drops them, and the rendered HTML of each
block is wrapped in <div class="blyg-tk-gen"> with a matching `generated` entry (spec §5.7).

Members: blyg-src/members.json lists members' blygs or blogs (title, author, site, feed: a blyg's
feed.xml or any RSS/Atom feed). It becomes
blogroll.opml (0.3 §11) and a list on the blyg page. Adding someone is a publishing act: ask first.

Responses: verified Webmentions from other blygs (site/mentions.js) are listed among the Updates on
the blyg page, linking to the source. They never enter feed.xml or the item files (§13.5, §15.5).
The build reads them from the live endpoint, and fetches each source item for its title at build
time (§15.4: pointers are stored, content is fetched when displayed). BLYG_MENTIONS=0 skips this
(offline builds). Members' recent posts are read from their feeds the same way and shown as links to
them. The site workflow rebuilds hourly when any of this changes (--outside-hash).

Output: blyg/ — blyg.json, feed.xml, items/index.json, items/{id}.json, pinned
items/{id}/v{n}.json, blogroll.opml, and human-readable pages (index, f/{id}/, t/{id}/).
"""
import email.utils, hashlib, html, json, os, re, shutil, subprocess, sys, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "blyg-src"
OUT = ROOT / "blyg"
# BLYG_SITE=http://localhost:8011/ previews absolute links (such as images) against a local server
SITE = os.environ.get("BLYG_SITE") or json.loads((Path(__file__).resolve().parent.parent / "config.json").read_text())["site"]
ORIGIN = SITE + "blyg/"
BLYG = "0.3"
GENERATOR_URL = "https://github.com/protocolvision/sig-p4b"
GENERATOR = "sig-p4b-blyg/0.1 (static, git-versioned)"
TITLE = "Protocols for Business"
DESCRIPTION = ("Session notes and the running research log of the Protocol Institute's "
               "Protocols for Business.")
FEED_WINDOW = 50
LEVEL = 2   # informative (0.3 §3.2): L1 plus the page field and stubs, both emitted per §5.8 and §10.6
ID_RE = re.compile(r"^[0-9abcdefghjkmnpqrstvwxyz]{26}$")
TRANSCLUDE_RE = re.compile(r"^\s*!\[\[([0-9a-z]{26})\]\]\s*$")
MEDIA_RE = re.compile(r"!\[([^\]]*)\]\(media/([A-Za-z0-9._-]+)\)")
MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".gif": "image/gif"}
MEDIA = {}   # published path -> bytes, collected while building every version
GEN_OPEN, GEN_CLOSE = re.compile(r"^\s*:::\s*generated\s*$"), re.compile(r"^\s*:::\s*$")

def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, capture_output=True, text=True).stdout

def utc(iso):
    return datetime.fromisoformat(iso).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def rfc822(iso):
    return email.utils.format_datetime(datetime.fromisoformat(iso.replace("Z", "+00:00")), usegmt=True)

def split_front(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, v = line.split(":", 1)
            v = v.strip() if v.strip().startswith("{") else v.split(" #")[0].strip()
            if v.startswith("{") and v.endswith("}"):
                v = json.loads(v)   # an inline JSON object, e.g. stub_of
            elif v.startswith("[") and v.endswith("]"):
                v = [int(x) for x in re.findall(r"\d+", v)]
            elif v.lower() in ("true", "false"):
                v = v.lower() == "true"
            meta[k.strip()] = v
    return meta, text[m.end():]

def md_to_html(md_text):
    return markdown.markdown(md_text, extensions=["extra", "sane_lists"], output_format="html")

def render(body):
    """Return (content_md, content_html, n_generated_blocks) for an item body without transclusions."""
    md_lines, parts, block, in_gen, n_gen = [], [], [], False, 0
    def flush(gen):
        text = "\n".join(block).strip("\n")
        if text:
            h = md_to_html(text)
            parts.append(f'<div class="blyg-tk-gen">{h}</div>' if gen else h)
        block.clear()
    for line in body.strip("\n").splitlines():
        if not in_gen and GEN_OPEN.match(line):
            flush(False); in_gen = True; n_gen += 1; continue
        if in_gen and GEN_CLOSE.match(line):
            flush(True); in_gen = False; continue
        md_lines.append(line); block.append(line)
    flush(in_gen)
    content_md = "\n".join(md_lines).strip() + "\n"
    return content_md, "\n".join(parts), n_gen

def versions_of(path):
    """Committed content versions of one source file, oldest first."""
    rel = path.relative_to(ROOT).as_posix()
    log = git("log", "--format=%H%x09%cI%x09%s", "--", rel).strip().splitlines()
    out, last_body, last_withdrawn, last_stub = [], None, False, "null"
    for line in reversed(log):
        sha, when, subject = line.split("\t", 2)
        try:
            text = git("show", f"{sha}:{rel}")
        except subprocess.CalledProcessError:
            continue
        meta, body = split_front(text)
        withdrawn = bool(meta.get("withdrawn"))
        stub = json.dumps(meta.get("stub_of"), sort_keys=True)
        if body == last_body and withdrawn == last_withdrawn and stub == last_stub:
            continue  # front-matter-only change (other than stub_of): not a publish event
        out.append({"sha": sha, "at": utc(when), "note": subject[:140], "meta": meta, "body": body,
                    "withdrawn": withdrawn})
        last_body, last_withdrawn, last_stub = body, withdrawn, stub
    return out

def load_items():
    items = {}
    for kind, folder in (("fragment", "fragments"), ("thread", "threads")):
        for path in sorted((SRC / folder).glob("*.md")):
            meta, _ = split_front(path.read_text())
            iid = str(meta.get("id", ""))
            if not ID_RE.match(iid):
                sys.exit(f"{path}: id must be 26 characters of lowercase Crockford base32 (use tools/blyg_new.py)")
            if iid in items:
                sys.exit(f"{path}: duplicate id {iid}")
            vs = versions_of(path)
            if vs:  # never-committed files are drafts
                items[iid] = {"id": iid, "kind": kind, "path": path, "versions": vs}
    return items

def fragment_version_at(frag, when):
    """Latest published, non-withdrawn version of a fragment at a given time."""
    best = None
    for n, v in enumerate(frag["versions"], 1):
        if v["at"] <= when:
            best = None if v["withdrawn"] else (n, v)
    return best

def build_item(item, items):
    vs, iid, kind = item["versions"], item["id"], item["kind"]
    latest = vs[-1]
    doc = {"blyg": BLYG, "id": iid, "kind": "withdrawn" if latest["withdrawn"] else kind, "origin": ORIGIN,
           "page": f'{"f" if kind == "fragment" else "t"}/{iid}/'}  # 0.3 §5.8: the item's permalink, origin-relative
    author = latest["meta"].get("author")
    if author:
        doc["author"] = {"name": author}
    doc["created"], doc["updated"], doc["version"] = vs[0]["at"], latest["at"], len(vs)
    pins = set(latest["meta"].get("pin") or [])
    snapshots = {}
    for n, v in enumerate(vs, 1):
        snapshots[n] = snapshot(item, v, items)
    doc.update({k: snapshots[len(vs)][k] for k in ("content_md", "content_html", "content_hash")})
    doc["media"] = snapshots[len(vs)]["media"]
    if kind == "thread":
        doc["transclusions"] = snapshots[len(vs)]["transclusions"]
        if isinstance(latest["meta"].get("stub_of"), dict) and not latest["withdrawn"]:
            doc["stub_of"] = latest["meta"]["stub_of"]   # 0.3 §10.6: the one thing this thread responds to
    if snapshots[len(vs)]["generated"]:
        doc["generated"] = snapshots[len(vs)]["generated"]
    doc["changelog"] = []
    for n, v in enumerate(vs, 1):
        entry = {"version": n, "at": v["at"], "note": v["note"]}
        if n in pins:
            entry["pinned"] = True
        doc["changelog"].append(entry)
    return doc, snapshots, pins

def snapshot(item, v, items):
    if v["withdrawn"]:
        s = {"content_md": "", "content_html": "", "generated": None, "transclusions": [], "media": []}
    else:
        body, media = with_media(item, v, v["body"])
        trans, html_parts, md_parts = [], [], []
        if item["kind"] == "thread":
            chunk = []
            for line in body.splitlines():
                m = TRANSCLUDE_RE.match(line)
                if not m:
                    chunk.append(line); continue
                target = items.get(m.group(1))
                if not target or target["kind"] != "fragment":
                    sys.exit(f"{item['path']}: ![[{m.group(1)}]] is not a published fragment of this blyg")
                hit = fragment_version_at(target, v["at"])
                if not hit:
                    sys.exit(f"{item['path']}: ![[{m.group(1)}]] had no published version at {v['at']}")
                n, fv = hit
                cm, ch, _ = render("\n".join(chunk)); chunk = []
                md_parts.append(cm); html_parts.append(ch)
                fmd, fhtml, _ = render(fv["body"])
                md_parts.append(line.strip() + "\n")
                html_parts.append(f'<blockquote class="blyg-transclusion" data-blyg-id="{target["id"]}" '
                                  f'data-blyg-version="{n}">{fhtml}</blockquote>')
                trans.append({"id": target["id"], "version": n})
            cm, ch, _ = render("\n".join(chunk))
            md_parts.append(cm); html_parts.append(ch)
            content_md = "\n".join(p.strip("\n") for p in md_parts if p.strip()) + "\n"
            content_html = "\n".join(h for h in html_parts if h)
            n_gen = len(re.findall(r"^\s*:::\s*generated\s*$", body, re.M))
        else:
            content_md, content_html, n_gen = render(body)
        gen = None
        if n_gen:
            model = str(v["meta"].get("generated_model") or "unspecified")
            gen = [{"sources": [], "model": model, "at": v["at"]} for _ in range(n_gen)]
        s = {"content_md": content_md, "content_html": content_html, "generated": gen, "transclusions": trans,
             "media": media}
    s["content_hash"] = "sha256:" + hashlib.sha256(s["content_md"].encode("utf-8")).hexdigest()
    return s

def with_media(item, v, body):
    """Point ![alt](media/name) at the immutable, content-addressed copy of the file committed with this version."""
    found = []
    def sub(m):
        alt, name = m.group(1), m.group(2)
        ext = Path(name).suffix.lower()
        if ext not in MIME:
            sys.exit(f"{item['path']}: media/{name} is not a supported image type")
        try:
            data = subprocess.run(["git", "-C", str(ROOT), "show", f"{v['sha']}:blyg-src/media/{name}"],
                                  check=True, capture_output=True).stdout
        except subprocess.CalledProcessError:
            sys.exit(f"{item['path']}: media/{name} was not committed with version at {v['at']}")
        rel = f"media/{hashlib.sha256(data).hexdigest()[:16]}{ext}"
        MEDIA[rel] = data
        if rel not in [f["url"] for f in found]:
            found.append({"url": rel, "mime": MIME[ext], "alt": alt})
        return f"![{alt}]({ORIGIN}{rel})"
    return MEDIA_RE.sub(sub, body), found

def permalink(doc_kind, iid):
    return f"{ORIGIN}{'t' if doc_kind == 'thread' else 'f'}/{iid}/"

def absolutize(h):
    return re.sub(r'(src|href)="(?!https?:|#|mailto:)([^"]+)"', lambda m: f'{m.group(1)}="{ORIGIN}{m.group(2)}"', h)

def title_of(doc, fallback_kind):
    md = doc.get("content_md") or ""
    m = re.search(r"^#\s+(.+)$", md, re.M)
    if m:
        return m.group(1).strip()
    words = re.sub(r"[#*_>`\[\]!()]", "", md).split()
    return " ".join(words[:10]) + ("…" if len(words) > 10 else "") or fallback_kind

def main():
    items = load_items()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "items").mkdir(parents=True)
    docs, events = {}, []
    for iid, item in items.items():
        doc, snaps, pins = build_item(item, items)
        docs[iid] = (doc, item)
        (OUT / "items" / f"{iid}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
        for n in sorted(pins):
            if n > len(item["versions"]):
                sys.exit(f"{item['path']}: pin {n} names an unpublished version")
            s = snaps[n]
            pv = {"blyg": BLYG, "id": iid, "kind": item["kind"], "origin": ORIGIN, "version": n,
                  "at": item["versions"][n - 1]["at"], "content_md": s["content_md"],
                  "content_html": s["content_html"], "content_hash": s["content_hash"], "media": []}
            if item["kind"] == "thread":
                pv["transclusions"] = s["transclusions"]
            if s["generated"]:
                pv["generated"] = s["generated"]
            (OUT / "items" / iid).mkdir(exist_ok=True)
            (OUT / "items" / iid / f"v{n}.json").write_text(json.dumps(pv, ensure_ascii=False, indent=1) + "\n")
        if doc["kind"] == "withdrawn":
            events.append((doc["updated"], doc, len(item["versions"]), item["versions"][-1]["note"]))
        else:
            for n, v in enumerate(item["versions"], 1):
                events.append((v["at"], doc, n, v["note"]))
    ordered = sorted((d for d, _ in docs.values()), key=lambda d: d["updated"], reverse=True)
    updated = ordered[0]["updated"] if ordered else datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    index = {"updated": updated, "items": [{"id": d["id"], "kind": d["kind"], "created": d["created"],
                                             "updated": d["updated"], "version": d["version"]} for d in ordered]}
    (OUT / "items" / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n")
    for rel, data in MEDIA.items():   # every version's media, so older and pinned versions keep working
        (OUT / rel).parent.mkdir(exist_ok=True)
        (OUT / rel).write_bytes(data)
    members = load_members()
    manifest = {"blyg": BLYG, "level": LEVEL, "generator": GENERATOR, "generator_url": GENERATOR_URL, "site": ORIGIN, "title": TITLE,
                "author": {"name": TITLE, "bio": DESCRIPTION,
                           "links": [{"label": "Home", "url": SITE}, {"label": "Protocol Institute", "url": "https://protocol-institute.org/"}]},
                "feed": "feed.xml", "items": "items/index.json", "webmention": "webmention", "updated": updated}   # §15.1: served by site/worker.js
    if members:
        manifest["blogroll"] = "blogroll.opml"   # §6.1: only when the blogroll is non-empty
        write_blogroll(members)
    (OUT / "blyg.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n")
    write_feed(sorted(events, key=lambda e: e[0], reverse=True)[:FEED_WINDOW], updated)
    raw, posts = recent_mentions(), member_posts(members)
    mentions, community = with_titles(raw), community_of(members)
    write_pages(ordered, {iid: it["path"].stem for iid, (_, it) in docs.items()}, community, mentions, posts,
                outside_hash(raw, posts))
    print(f"blyg: {len(docs)} items, {len(events)} publish events, {len(members)} members ({len(posts)} of their posts), "
          f"{len(mentions)} responses from other blygs -> {OUT.relative_to(ROOT)}/")

def load_members():
    path = SRC / "members.json"
    members = json.loads(path.read_text()) if path.exists() else []
    for m in members:
        for k in ("title", "site", "feed"):
            if not str(m.get(k, "")).strip():
                sys.exit(f"{path}: every member needs {k}")
        if not all(str(m[k]).startswith("https://") for k in ("site", "feed")):
            sys.exit(f"{path}: {m['title']}: site and feed must be https URLs")
    return members

def write_blogroll(members):
    """0.3 §11: plain OPML 2.0, one rss outline per member blyg, no extensions."""
    a = lambda s: html.escape(str(s), quote=True)
    rows = "\n".join(f'    <outline type="rss" text="{a(m["title"])}" title="{a(m["title"])}" '
                     f'xmlUrl="{a(m["feed"])}" htmlUrl="{a(m["site"])}"/>' for m in members)
    (OUT / "blogroll.opml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
  <head>
    <title>{a(TITLE)} — members' blygs and blogs</title>
  </head>
  <body>
{rows}
  </body>
</opml>
""")

def fetch(url, timeout=8, limit=2_000_000, accept="*/*"):
    req = urllib.request.Request(url, headers={"User-Agent": "sig-p4b-blyg", "Accept": accept})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read(limit + 1)
        if len(data) > limit:
            raise ValueError("too large")
        return data, r.headers.get("Content-Type", ""), r.geturl()

def get_json(url, timeout=5):
    return json.loads(fetch(url, timeout, 1_000_000, "application/json")[0])

def recent_mentions():
    """Verified mentions from the live endpoint, or [] when offline or switched off (BLYG_MENTIONS=0)."""
    if os.environ.get("BLYG_MENTIONS") == "0":
        return []
    try:
        got = get_json(ORIGIN + "webmention/recent", timeout=10)
        return got if isinstance(got, list) else []
    except Exception as ex:
        print(f"blyg: responses from other blygs not loaded ({ex.__class__.__name__}); building without them", file=sys.stderr)
        return []

def with_titles(raw):
    """Each verified mention, with the source item's title fetched now from its origin (nothing is stored)."""
    out = []
    for m in raw[:30]:
        page, origin, sid = str(m.get("page") or ""), str(m.get("origin") or ""), str(m.get("source_id") or "")
        if not page.startswith(("https://", "http://")) or not ID_RE.match(str(m.get("target_id") or "")):
            continue
        title = ""
        if origin.startswith(("https://", "http://")) and ID_RE.match(sid):
            try:
                doc = get_json(origin.rstrip("/") + f"/items/{sid}.json")
                if doc.get("kind") == "withdrawn":
                    continue
                title = title_of(doc, "")
            except Exception:
                pass
        out.append({**m, "title": title})
    return out

def text_of(fragment, limit=220):
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<(script|style)\b.*?</\1>|<[^>]+>", " ", fragment or "", flags=re.S))).strip()
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0].rstrip(",;:·") + "…"

FEED_SHOWN = 50   # posts in the Feed's default view
PER_MEMBER = 3   # newest posts shown from each member's feed

def member_posts(members):
    """Recent posts from members' feeds (a blyg's feed.xml, or any blog's RSS or Atom), shown on the blyg
    page as links to their sites (0.3 §13.5: displayed with attribution, never re-emitted).
    BLYG_MENTIONS=0 skips this too."""
    if os.environ.get("BLYG_MENTIONS") == "0":
        return []
    import xml.etree.ElementTree as ET
    NS, A = "{https://blygger.org/ns/0.1}", "{http://www.w3.org/2005/Atom}"
    def when(text, rfc):
        try:
            d = email.utils.parsedate_to_datetime(text) if rfc else datetime.fromisoformat(text.strip().replace("Z", "+00:00"))
            return d.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        except Exception:
            return None
    out = []
    for m in members:
        try:
            root = ET.fromstring(fetch(m["feed"], accept="application/rss+xml, application/atom+xml, application/xml")[0])
        except Exception as ex:
            print(f"blyg: {m['feed']} not loaded ({ex.__class__.__name__})", file=sys.stderr)
            continue
        rows = []
        if root.tag == A + "feed":   # Atom
            for e in root.iter(A + "entry"):
                links = e.findall(A + "link")
                link = next((l.get("href", "") for l in links if l.get("rel", "alternate") == "alternate"), "")
                rows.append((link, e.findtext(A + "id") or link, "", when(e.findtext(A + "published") or e.findtext(A + "updated") or "", False),
                             e.findtext(A + "title") or "", e.findtext(A + "summary") or e.findtext(A + "content") or ""))
        else:                        # RSS 2.0, including every blyg's feed.xml
            for it in root.iter("item"):
                link = (it.findtext("link") or "").strip()
                rows.append((link, it.findtext(NS + "id") or link, it.findtext(NS + "kind") or "", when(it.findtext("pubDate") or "", True),
                             it.findtext("title") or "", it.findtext("description") or ""))
        seen, n = set(), 0
        for link, key, kind, at, title, desc in rows:   # newest first; a blyg lists one entry per version
            if key in seen or not link.startswith(("https://", "http://")) or not at:
                continue
            seen.add(key)
            if kind == "withdrawn":
                continue
            preview = text_of(desc)
            out.append({"member": m["site"], "link": link, "at": at,
                        "title": text_of(title, 120) or preview[:80] or "A post", "preview": preview})
            n += 1
            if n >= PER_MEMBER:
                break
    return out

def outside_hash(mentions, posts):
    """What the blyg page shows from other blygs; the hourly workflow rebuilds when it changes."""
    state = [mentions, [[p["link"], p["at"], p["title"]] for p in posts]]
    return hashlib.sha256(json.dumps(state, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]

def vehicle_svg(seed, small=False, hue=None):
    """A Braitenberg vehicle for one member, drawn in the site's line style: a body, two wheels, two
    sensors and the wires between them, straight or crossed, excitatory (+, solid) or inhibitory
    (-, dashed), sometimes with the light it turns toward or away from. Seeded by the blyg's address,
    so a member keeps the same vehicle on every build."""
    import math, random
    r = random.Random(hashlib.sha256(seed.encode()).hexdigest())
    f = lambda x: f"{x:.1f}".rstrip("0").rstrip(".")
    crossed, inhibit = r.random() < .5, r.random() < .4
    w, h = r.uniform(12, 16), r.uniform(14, 18)            # body
    x0, y0 = 20 - w / 2, 21 - h / 2 + 2
    shape = r.choice(["box", "box", "round", "nose"])
    if shape == "box":
        body = f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(w)}" height="{f(h)}" rx="{f(r.uniform(1, 3))}"/>'
    elif shape == "round":
        body = f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(w)}" height="{f(h)}" rx="{f(w / 2)}"/>'
    else:
        body = (f'<path d="M{f(x0)} {f(y0 + 4)} L20 {f(y0 - 1)} L{f(x0 + w)} {f(y0 + 4)} V{f(y0 + h)} H{f(x0)} Z"/>')
    wy, wh = y0 + h - r.uniform(5, 7), r.uniform(4.5, 6)   # wheels, at the back
    wheels = (f'<rect x="{f(x0 - 2.6)}" y="{f(wy)}" width="2.6" height="{f(wh)}" rx=".8"/>'
              f'<rect x="{f(x0 + w)}" y="{f(wy)}" width="2.6" height="{f(wh)}" rx=".8"/>')
    spread, sy = r.uniform(.25, .42) * w, y0 + (2 if shape != "nose" else 4)
    sx = (20 - spread, 20 + spread)
    kind = r.choice(["eye", "cup", "antenna"])
    sensors = ""
    for x in sx:
        if kind == "eye":
            sensors += f'<circle cx="{f(x)}" cy="{f(sy - 1.6)}" r="1.6"/>'
        elif kind == "cup":
            sensors += f'<path d="M{f(x - 1.9)} {f(sy - 3)} A1.9 1.9 0 0 0 {f(x + 1.9)} {f(sy - 3)}"/>'
        else:
            tip = (x + (x - 20) * .5, sy - 5)
            sensors += f'<path d="M{f(x)} {f(sy)} L{f(tip[0])} {f(tip[1])}"/><circle cx="{f(tip[0])}" cy="{f(tip[1])}" r=".9"/>'
    motors = (x0 + 1.2, x0 + w - 1.2)
    my = wy + wh / 2
    wires = ""
    for i, x in enumerate(sx):
        mx = motors[1 - i] if crossed else motors[i]
        cy = (sy + my) / 2
        wires += (f'<path class="w" d="M{f(x)} {f(sy + .4)} C{f(x)} {f(cy)} {f(mx)} {f(cy)} {f(mx)} {f(my)}"'
                  + (' stroke-dasharray="1.6 1.3"' if inhibit else "") + '/>')
    sign = (f'<path class="w" d="M{f(20 - 1.3)} {f(y0 + h - 2.2)} h2.6"/>' if inhibit else
            f'<path class="w" d="M{f(20 - 1.3)} {f(y0 + h - 2.2)} h2.6 M20 {f(y0 + h - 3.5)} v2.6"/>')
    tilt = r.uniform(-28, 28)
    light = ""
    if not small and r.random() < .55:   # the light it reacts to, off to one side ahead
        lx, ly = 20 + r.choice([-1, 1]) * r.uniform(9, 12), r.uniform(5, 7)
        rays = "".join(f'M{f(lx + 2.4 * math.cos(t))} {f(ly + 2.4 * math.sin(t))} L{f(lx + 3.6 * math.cos(t))} {f(ly + 3.6 * math.sin(t))} '
                       for t in [k * math.pi / 4 for k in range(8)])
        light = f'<g class="l"><circle cx="{f(lx)}" cy="{f(ly)}" r="1.4"/><path d="{rays.strip()}"/></g>'
    detail = "" if small else wires + sign
    if hue is None:
        hue = preferred_hue(seed)
    return (f'<svg class="bv c{hue}" viewBox="{"5 4 30 32" if small else "3 1 34 36"}" aria-hidden="true">{light}'
            f'<g transform="rotate({f(tilt)} 20 22)">{wheels}{body}{sensors}{detail}</g></svg>')

HUES = 6   # .bv.c0–.c5 in style.css

def preferred_hue(seed):
    return int(hashlib.sha256(("colour:" + seed).encode()).hexdigest(), 16) % HUES   # its own seed: shapes stay as they were

def community_of(members):
    """Members with display names and a vehicle colour: each keeps its seeded colour unless an earlier
    member has it, then takes the next free one, so colours spread out until all are in use."""
    out, used = [], []
    for m in members:
        name = m.get("author") or m["title"]
        hue = preferred_hue(m["site"])
        free = [h for h in range(HUES) if h not in used[-(HUES - 1):]] if len(used) else list(range(HUES))
        if hue not in free:
            hue = min(free, key=lambda h: (h - hue) % HUES)
        used.append(hue)
        out.append({**m, "name": name, "short": m.get("short") or name.split()[0], "hue": hue})
    return out

def write_feed(events, updated):
    e = lambda s: html.escape(s, quote=False)
    rows = []
    for at, doc, n, note in events:
        k = doc["kind"]
        withdrawn = k == "withdrawn"
        title = "withdrawn" if withdrawn else title_of(doc, k)
        if note and not withdrawn and n > 1:
            title = f"{note} — {title}"
        desc = "" if withdrawn else absolutize(doc["content_html"])
        creator = f'\n      <dc:creator>{e(doc["author"]["name"])}</dc:creator>' if doc.get("author", {}).get("name") else ""
        rows.append(f"""    <item>
      <guid isPermaLink="false">blyg:{doc['id']}:v{n}</guid>
      <link>{permalink(k, doc['id'])}</link>
      <title>{e(title)}</title>
      <description><![CDATA[{desc}]]></description>
      <pubDate>{rfc822(at)}</pubDate>{creator}
      <blyg:id>{doc['id']}</blyg:id>
      <blyg:kind>{k}</blyg:kind>
      <blyg:version>{n}</blyg:version>
      <blyg:created>{doc['created']}</blyg:created>
      <blyg:item>{ORIGIN}items/{doc['id']}.json</blyg:item>
    </item>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:blyg="https://blygger.org/ns/0.1" xmlns:dc="http://purl.org/dc/elements/1.1/">
  <channel>
    <title>{e(TITLE)}</title>
    <link>{ORIGIN}</link>
    <description>{e(DESCRIPTION)}</description>
    <lastBuildDate>{rfc822(updated)}</lastBuildDate>
    <blyg:level>{LEVEL}</blyg:level>
    <blyg:manifest>{ORIGIN}blyg.json</blyg:manifest>
{chr(10).join(rows)}
  </channel>
</rss>
"""
    (OUT / "feed.xml").write_text(xml)

def summary(content_html, limit=155):
    """A page's own meta description: its first lines of text, cut at a word."""
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<h1.*?</h1>|<p>(?:(?!</p>).)*?Participants:.*?</p>|<[^>]+>", " ", content_html, flags=re.S))).strip()
    if len(text) <= limit:
        return text or DESCRIPTION
    return text[:limit].rsplit(" ", 1)[0].rstrip(",;:·") + "…"

RETURN_ICON = ('<svg class="stub-icon" viewBox="0 0 16 16" width="14" height="14" aria-hidden="true">'
               '<path d="M6 3 2 7l4 4M2.5 7H10a4 4 0 0 1 0 8H8" fill="none" stroke="currentColor" stroke-width="1.4" '
               'stroke-linecap="round" stroke-linejoin="round"/></svg>')

def stub_line(d):
    """For a stub, a small line above the post linking back to what it responds to (from stub_of.cited)."""
    st = d.get("stub_of")
    if not st:
        return ""
    c = st.get("cited", {})
    url = c.get("url") or st.get("url") or (st.get("origin", "") + "items/" + st.get("id", "") + ".json")
    who = c.get("author")
    label = f"a note by {html.escape(who)}" if who else html.escape(c.get("source") or url)
    where = ""   # the author's name already says whose it is
    return f'<p class="stub-of">{RETURN_ICON} In response to <a href="{html.escape(url, quote=True)}">{label}</a>{where}</p>\n'

VERB = {"stub": "responded", "transclusion": "quoted this", "fork": "forked this"}

def responses_here(ms):
    """An icon after one of our posts on the blyg page, opening the list of responses on other blygs (§15.5)."""
    if not ms:
        return ""
    rows = []
    for m in ms:
        host = re.sub(r"^https?://([^/]+).*$", r"\1", m["page"])
        who = m.get("author") or host
        rows.append(f'<li><a href="{html.escape(m["page"], quote=True)}">{html.escape(m["title"] or "A post by " + who)}</a> '
                    f'<span class="muted">· {html.escape(who)} {VERB.get(m.get("relation"), "mentioned this")}'
                    f'{" · " + html.escape(host) if m.get("author") else ""}</span></li>')
    n = len(ms)
    label = f"{n} response{'s' if n != 1 else ''} on other blygs"
    return (f'<details class="blyg-responses"><summary title="{label}" aria-label="{label}">{RETURN_ICON}{n}</summary>'
            f'<ul>{"".join(rows)}</ul></details>')

def write_pages(ordered, stems, community, mentions, posts, ohash):
    sys.path.insert(0, str(ROOT / "tools"))
    from build_site import page
    alt = ('<link rel="alternate" type="application/rss+xml" title="Protocols for Business blyg" href="{rel}blyg/feed.xml">\n'
           f'<link rel="webmention" href="{ORIGIN}webmention">\n')
    def date(iso): return datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%-d %B %Y")
    def day(iso): return datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%-d %b %Y")
    by_target = {}
    for m in mentions:
        by_target.setdefault(m["target_id"], []).append(m)
    who = {c["site"]: c for c in community}
    entries = []   # (date shown, classes, html): our posts and members' posts in one dated list
    for d in ordered:
        if d["kind"] == "withdrawn":
            continue
        stem = stems.get(d["id"], "")
        m = re.match(r"session-(\d{4}-\d{2}-\d{2})", stem)
        shown = m.group(1) + "T00:00:00Z" if m else d["updated"]
        label = ("session notes" if m else "research log" if stem == "research-log"
                 else "update" if d["kind"] == "thread" else "fragment")
        if d.get("stub_of"):
            label += " · response"
        if d["version"] > 1:
            label += f' · v{d["version"]}'
        href = f'{"t" if d["kind"] == "thread" else "f"}/{d["id"]}/'
        entries.append((shown, "ours", f'<div class="feed-meta">{OUR_MARK}<time datetime="{shown[:10]}">{day(shown)}</time> · {label}'
            f'{responses_here(by_target.get(d["id"], []))}</div>\n'
            f'<p class="feed-title"><a href="{href}">{html.escape(title_of(d, d["kind"]))}</a></p>\n'
            f'<p class="feed-preview">{html.escape(summary(d["content_html"], 200))}</p>'))
    for p in posts:
        c = who.get(p["member"])
        if not c:
            continue
        host = re.sub(r"^https?://([^/]+).*$", r"\1", p["link"])
        entries.append((p["at"], "from-member", f'<div class="feed-meta">{avatar_html(c, "sm")}'
            f'<a href="{html.escape(c["site"], quote=True)}">{html.escape(c["name"])}</a> · '
            f'<time datetime="{p["at"][:10]}">{day(p["at"])}</time><span class="host"> · on {html.escape(host)}</span></div>\n'
            f'<p class="feed-title"><a href="{html.escape(p["link"], quote=True)}">{html.escape(p["title"])}</a></p>\n'
            + (f'<p class="feed-preview">{html.escape(p["preview"])}</p>' if p["preview"] and p["preview"] != p["title"] else "")))
    for d in ordered:
        if d["kind"] == "withdrawn":
            continue
        kind = "Thread" if d["kind"] == "thread" else "Fragment"
        content = d["content_html"]
        if "<h1" not in content:   # one H1 per page: fragments often open without a heading
            content = f'<h1>{html.escape(title_of(d, kind))}</h1>\n' + content
        body = (f'<p class="meta"><a href="../../">Feed</a> · {kind.lower()} · version {d["version"]} · '
                f'updated {date(d["updated"])}</p>\n{stub_line(d)}<article class="blyg-item">\n{content}\n</article>\n'
                f'<section class="responses" data-responses="{d["id"]}" hidden><h2>Responses</h2><ul></ul></section>\n'
                f'<p class="small muted">Machine-readable: <a href="../../items/{d["id"]}.json">item JSON</a> · '
                f'changelog {len(d["changelog"])} version{"s" if len(d["changelog"]) != 1 else ""}</p>')
        folder = OUT / ("t" if d["kind"] == "thread" else "f") / d["id"]
        folder.mkdir(parents=True, exist_ok=True)
        path = f'blyg/{"t" if d["kind"] == "thread" else "f"}/{d["id"]}/'
        card = ROOT / "assets/cards/blyg" / f'{d["id"]}.jpg'   # tools/cards/render_blyg.py; else the blyg card
        card_url = f'{SITE}assets/cards/blyg/{d["id"]}.jpg' if card.exists() else f"{SITE}assets/cards/blyg.jpg"
        author = (d.get("author") or {}).get("name") or "Protocols for Business"
        folder.joinpath("index.html").write_text(page(
            {"title": f"{title_of(d, kind)} · Protocols for Business blyg", "desc": summary(d["content_html"]), "path": path, "nav": "feed",
             "card_url": card_url, "og_type": "article",
             "og_extra": [("article:published_time", d["created"]), ("article:modified_time", d["updated"]), ("article:author", author)],
             "posting": {"datePublished": d["created"], "dateModified": d["updated"], "image": card_url,
                         "author": {"@type": "Organization" if author == "Protocols for Business" else "Person", "name": author}},
             "head": alt.format(rel="../../../") + f'<link rel="alternate" type="application/json" href="../../items/{d["id"]}.json">\n'}, body))
    intro = (f'<h1>Feed</h1>\n<p class="lede">Session notes, the research log and updates from Protocols for Business, '
             f'with new posts from members\' own blygs and blogs. Our posts are versioned: edits show up as new versions, not new posts.</p>\n'
             f'<p class="feed-cta"><button type="button" class="btn" data-listing>Add your blyg or blog</button> '
             f'<span class="small muted">Write a <a href="https://blygger.org/">blyg</a>, or a blog with an RSS feed? Ask to join the community below.</span></p>\n')
    if community:
        intro += ('<h2 class="feed-h">Community</h2>\n<ul class="community">\n'
                  '  <li><label for="show-ours" title="Show only Protocols for Business posts"><span class="avatar lg logo">'
                  '<img class="mark" src="../favicon.svg" alt="" width="24" height="24"></span><span>This group</span></label></li>\n' + "\n".join(
            f'  <li><a href="{html.escape(c["site"], quote=True)}" title="{html.escape(c["title"], quote=True)}">'
            f'{avatar_html(c, "lg")}<span>{html.escape(c["short"])}</span></a></li>' for c in community) + "\n</ul>\n")
    # Everyone: the latest FEED_SHOWN posts. Ours only: every post of ours. A CSS-only toggle (style.css, :has()).
    ordered_entries = sorted(entries, key=lambda e: e[0], reverse=True)
    n_ours = sum(1 for e in entries if e[1] == "ours")
    rows = "\n".join(f'<li class="{cls}{" top" if i < FEED_SHOWN else ""}">{h}</li>' for i, (_, cls, h) in enumerate(ordered_entries))
    intro += ('<div class="feed-wrap">\n<div class="feed-head"><h2 class="feed-h">Latest</h2>\n'
              '<fieldset class="feed-filter"><legend class="visually-hidden">Show</legend>'
              f'<input type="radio" name="feed-show" id="show-all" checked><label for="show-all" title="The latest {FEED_SHOWN} posts">Everyone</label>'
              f'<input type="radio" name="feed-show" id="show-ours"><label for="show-ours" title="All {n_ours} of our posts">Protocols for Business only</label>'
              f'</fieldset></div>\n<ol class="feed">\n{rows}\n</ol>\n</div>\n')
    intro += (f'<p class="small muted">Members\' posts link to their own blygs and blogs. {RETURN_ICON} marks one of ours that someone '
              'answered on their blyg. Follow with any RSS reader: <a href="feed.xml">our feed</a> · '
              '<a href="blogroll.opml">all members (OPML)</a> · built on the <a href="https://blygger.org/">Blygger protocol</a> 0.3 · '
              '<a href="blyg.json">manifest</a> · <a href="items/index.json">archive index</a></p>\n')
    intro += f"<!-- outside:{ohash} -->\n"   # the hourly workflow rebuilds when this changes (--outside-hash)
    head = alt.format(rel="../") + ('<link rel="blogroll" href="blogroll.opml">\n' if community else "")
    (OUT / "index.html").write_text(page(
        {"title": "Feed · Protocols for Business", "desc": "Session notes, the research log and updates from Protocols for Business, "
         "with new posts from members' own blygs and blogs.", "path": "blyg/", "nav": "feed", "card": "blyg", "head": head}, intro))

OUR_MARK = ('<span class="avatar sm logo"><img class="mark" src="../favicon.svg" alt="Protocols for Business" '
            'title="Protocols for Business" width="16" height="16"></span>')   # class "mark": the image viewer skips it

def avatar_html(c, size):
    return f'<span class="avatar {size}">{vehicle_svg(c["site"], small=size == "sm", hue=c.get("hue"))}</span>'

if __name__ == "__main__":
    if sys.argv[1:] == ["--outside-hash"]:   # for the hourly check in .github/workflows/site.yml
        members = load_members()
        print(outside_hash(recent_mentions(), member_posts(members)))
    else:
        main()
