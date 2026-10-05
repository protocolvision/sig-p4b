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

Versions come from git: every commit that changes an item's content is one publish event,
dated by the commit and noted with the commit subject. Uncommitted edits are drafts and
are not published. Machine-generated passages are fenced as
  ::: generated
  ...
  :::
The fences never reach the wire: content_md drops them, and the rendered HTML of each
block is wrapped in <div class="blyg-tk-gen"> with a matching `generated` entry (spec §5.7).

Output: blyg/ — blyg.json, feed.xml, items/index.json, items/{id}.json, pinned
items/{id}/v{n}.json, and human-readable pages (index, f/{id}/, t/{id}/).
"""
import email.utils, hashlib, html, json, re, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "blyg-src"
OUT = ROOT / "blyg"
SITE = json.loads((Path(__file__).resolve().parent.parent / "config.json").read_text())["site"]
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
    doc["media"] = []
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
        s = {"content_md": "", "content_html": "", "generated": None, "transclusions": []}
    else:
        body, trans, html_parts, md_parts = v["body"], [], [], []
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
        s = {"content_md": content_md, "content_html": content_html, "generated": gen, "transclusions": trans}
    s["content_hash"] = "sha256:" + hashlib.sha256(s["content_md"].encode("utf-8")).hexdigest()
    return s

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
    manifest = {"blyg": BLYG, "level": LEVEL, "generator": GENERATOR, "generator_url": GENERATOR_URL, "site": ORIGIN, "title": TITLE,
                "author": {"name": TITLE, "bio": DESCRIPTION,
                           "links": [{"label": "Home", "url": SITE}, {"label": "Protocol Institute", "url": "https://protocol-institute.org/"}]},
                "feed": "feed.xml", "items": "items/index.json", "updated": updated}
    (OUT / "blyg.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n")
    write_feed(sorted(events, key=lambda e: e[0], reverse=True)[:FEED_WINDOW], updated)
    write_pages(ordered, {iid: it["path"].stem for iid, (_, it) in docs.items()})
    print(f"blyg: {len(docs)} items, {len(events)} publish events -> {OUT.relative_to(ROOT)}/")

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

def write_pages(ordered, stems):
    sys.path.insert(0, str(ROOT / "tools"))
    from build_site import page
    alt = '<link rel="alternate" type="application/rss+xml" title="Protocols for Business blyg" href="{rel}blyg/feed.xml">\n'
    def date(iso): return datetime.fromisoformat(iso.replace("Z", "+00:00")).strftime("%-d %B %Y")
    groups = {"log": [], "updates": [], "sessions": [], "notes": []}
    for d in ordered:
        if d["kind"] == "withdrawn":
            continue
        stem = stems.get(d["id"], "")
        m = re.match(r"session-(\d{4}-\d{2}-\d{2})", stem)
        shown = m.group(1) + "T00:00:00Z" if m else d["updated"]
        key = "sessions" if m else ("log" if stem == "research-log" else "updates" if d["kind"] == "thread" else "notes")
        kind_label = "session notes" if m else ("update" if key == "updates" else d["kind"])
        if d.get("stub_of"):
            kind_label += " · response"
        groups[key].append((shown, f'  <li><time datetime="{shown[:10]}">{date(shown)}</time><span class="what">'
            f'<a href="{"t" if d["kind"] == "thread" else "f"}/{d["id"]}/">{html.escape(title_of(d, d["kind"]))}</a> '
            f'<span class="muted">· {kind_label} · v{d["version"]}</span></span></li>'))
    for d in ordered:
        if d["kind"] == "withdrawn":
            continue
        kind = "Thread" if d["kind"] == "thread" else "Fragment"
        content = d["content_html"]
        if "<h1" not in content:   # one H1 per page: fragments often open without a heading
            content = f'<h1>{html.escape(title_of(d, kind))}</h1>\n' + content
        body = (f'<p class="meta"><a href="../../">Blyg</a> · {kind.lower()} · version {d["version"]} · '
                f'updated {date(d["updated"])}</p>\n{stub_line(d)}<article class="blyg-item">\n{content}\n</article>\n'
                f'<p class="small muted">Machine-readable: <a href="../../items/{d["id"]}.json">item JSON</a> · '
                f'changelog {len(d["changelog"])} version{"s" if len(d["changelog"]) != 1 else ""}</p>')
        folder = OUT / ("t" if d["kind"] == "thread" else "f") / d["id"]
        folder.mkdir(parents=True, exist_ok=True)
        path = f'blyg/{"t" if d["kind"] == "thread" else "f"}/{d["id"]}/'
        folder.joinpath("index.html").write_text(page(
            {"title": f"{title_of(d, kind)} · Protocols for Business blyg", "desc": summary(d["content_html"]), "path": path, "nav": "sessions",
             "card": "syllabus", "head": alt.format(rel="../../../")}, body))
    intro = (f'<h1>Blyg</h1>\n<p class="lede">{html.escape(DESCRIPTION)} Items are versioned: edits show up as new '
             f'versions rather than new posts.</p>\n<p class="small muted">Follow with any RSS reader: '
             f'<a href="feed.xml">feed.xml</a> · Built on the <a href="https://blygger.org/">Blygger protocol</a> (0.3) · '
             f'<a href="blyg.json">manifest</a> · <a href="items/index.json">archive index</a></p>\n'
             + "".join(f'<h2>{label}</h2>\n<ul class="schedule">\n' + "\n".join(r for _, r in sorted(groups[k], reverse=True)) + "\n</ul>\n"
                       for k, label in (("log", "Research log"), ("updates", "Updates"), ("sessions", "Session notes"), ("notes", "Fragments")) if groups[k]))
    (OUT / "index.html").write_text(page(
        {"title": "Blyg · Protocols for Business", "desc": DESCRIPTION, "path": "blyg/", "nav": "sessions",
         "card": "syllabus", "head": alt.format(rel="../")}, intro))

if __name__ == "__main__":
    main()
