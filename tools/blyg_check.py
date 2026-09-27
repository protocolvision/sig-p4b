#!/usr/bin/env python3
"""Check blyg/ (or a live origin) against the Blygger 0.2 Level 1 publish-side rules.

  python3 tools/blyg_check.py                      # the local build in blyg/
  python3 tools/blyg_check.py https://…/blyg/      # a deployed origin

Exits non-zero on any failure. Checks the rules a reader relies on: ids, hashes,
versions/changelogs, the archive index, per-version feed GUIDs, the manifest hook,
transclusion baking, and generation disclosure.
"""
import hashlib, json, re, sys, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ID_RE = re.compile(r"^[0-9abcdefghjkmnpqrstvwxyz]{26}$")
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
NS = "https://blygger.org/ns/0.1"
errors = []

def fail(msg):
    errors.append(msg)

def loader(base):
    if base.startswith("http"):
        base = base if base.endswith("/") else base + "/"
        def get(rel):
            req = urllib.request.Request(base + rel, headers={"User-Agent": "sig-p4b-blyg-check"})
            with urllib.request.urlopen(req) as r:
                return r.read().decode("utf-8"), dict(r.headers)
        return get
    root = Path(base)
    return lambda rel: ((root / rel).read_text(), {})

def main():
    base = sys.argv[1] if len(sys.argv) > 1 else str(Path(__file__).resolve().parent.parent / "blyg")
    get = loader(base)
    manifest = json.loads(get("blyg.json")[0])
    for k in ("blyg", "level", "site", "title", "feed", "items", "updated"):
        if k not in manifest:
            fail(f"blyg.json: missing {k}")
    if not str(manifest.get("blyg", "")).startswith("0."):
        fail("blyg.json: blyg key must be a 0.x version")
    index = json.loads(get(manifest.get("items", "items/index.json"))[0])
    entries = index.get("items", [])
    if [e["updated"] for e in entries] != sorted([e["updated"] for e in entries], reverse=True):
        fail("items/index.json: not ordered by updated descending")
    docs = {}
    for e in entries:
        iid = e["id"]
        if not ID_RE.match(iid):
            fail(f"index: bad id {iid}")
        doc = json.loads(get(f"items/{iid}.json")[0])
        docs[iid] = doc
        where = f"items/{iid}.json"
        for k in ("blyg", "id", "kind", "origin", "created", "updated", "version", "content_md",
                  "content_html", "content_hash", "media", "changelog"):
            if k not in doc:
                fail(f"{where}: missing {k}")
        if doc["kind"] not in ("fragment", "thread", "withdrawn"):
            fail(f"{where}: unexpected kind {doc['kind']}")
        for k in ("created", "updated"):
            if not TS_RE.match(doc[k]):
                fail(f"{where}: {k} is not ISO 8601 UTC")
        cl = doc["changelog"]
        if [c["version"] for c in cl] != list(range(1, len(cl) + 1)) or doc["version"] != len(cl):
            fail(f"{where}: versions must run 1..N and match the changelog")
        if cl and doc["updated"] != cl[-1]["at"]:
            fail(f"{where}: updated must equal the latest changelog entry")
        want = "sha256:" + hashlib.sha256(doc["content_md"].encode("utf-8")).hexdigest()
        if doc["content_hash"] != want:
            fail(f"{where}: content_hash does not match content_md")
        if re.search(r"^\s*:::", doc["content_md"], re.M):
            fail(f"{where}: authoring fence leaked into content_md")
        if e["version"] != doc["version"] or e["updated"] != doc["updated"] or e["kind"] != doc["kind"]:
            fail(f"index entry for {iid} disagrees with its item document")
        if doc["kind"] == "fragment" and "transclusions" in doc:
            fail(f"{where}: fragments must omit transclusions")
        if doc["kind"] == "thread":
            if "transclusions" not in doc:
                fail(f"{where}: threads must carry transclusions")
            baked = re.findall(r'<blockquote class="blyg-transclusion" data-blyg-id="([0-9a-z]{26})" data-blyg-version="(\d+)">', doc["content_html"])
            if [(t["id"], t["version"]) for t in doc.get("transclusions", [])] != [(i, int(v)) for i, v in baked]:
                fail(f"{where}: transclusions do not match the baked blockquotes")
            directives = re.findall(r"^\s*!\[\[([0-9a-z]{26})\]\]\s*$", doc["content_md"], re.M)
            if directives != [t["id"] for t in doc.get("transclusions", [])]:
                fail(f"{where}: transclusion directives in content_md do not match transclusions")
        gens = doc.get("generated")
        own_html = re.sub(r'<blockquote class="blyg-transclusion".*?</blockquote>', "", doc["content_html"], flags=re.S)
        wrapped = len(re.findall(r'class="blyg-tk-gen"', own_html))  # transcluded fragments carry their own
        if (gens or []) and len(gens) != wrapped:
            fail(f"{where}: generated has {len(gens)} entries but content_html wraps {wrapped} spans")
        if wrapped and not gens:
            fail(f"{where}: blyg-tk-gen spans without a generated array")
        if doc["kind"] == "withdrawn" and (doc["content_md"] or gens):
            fail(f"{where}: withdrawal endcap must be empty and carry no generated array")
        for c in cl:
            if c.get("pinned"):
                try:
                    pv = json.loads(get(f"items/{iid}/v{c['version']}.json")[0])
                    if pv.get("version") != c["version"]:
                        fail(f"items/{iid}/v{c['version']}.json: wrong version")
                except Exception as ex:
                    fail(f"pinned items/{iid}/v{c['version']}.json not served: {ex}")
    for d in docs.values():
        for t in d.get("transclusions", []):
            if t["id"] not in docs:
                fail(f"items/{d['id']}.json: transcludes unknown item {t['id']}")
    feed_text, headers = get(manifest.get("feed", "feed.xml"))
    rss = ET.fromstring(feed_text)
    ch = rss.find("channel")
    if rss.tag != "rss" or rss.get("version") != "2.0" or ch is None:
        fail("feed.xml: not RSS 2.0")
    else:
        if ch.find(f"{{{NS}}}manifest") is None:
            fail("feed.xml: missing <blyg:manifest>")
        items = ch.findall("item")
        if len(items) > 50:
            fail("feed.xml: window larger than 50")
        for it in items:
            iid = it.findtext(f"{{{NS}}}id")
            ver = it.findtext(f"{{{NS}}}version")
            guid = it.find("guid")
            if guid is None or guid.text != f"blyg:{iid}:v{ver}" or guid.get("isPermaLink") != "false":
                fail(f"feed.xml: bad guid for {iid} v{ver}")
            if iid not in docs:
                fail(f"feed.xml: entry for {iid} not in the archive index")
            desc = it.findtext("description") or ""
            if re.search(r'(src|href)="(?!https?:|#|mailto:)', desc):
                fail(f"feed.xml: relative URL in description for {iid}")
    if headers and base.startswith("http"):
        if headers.get("Access-Control-Allow-Origin") != "*":
            print("note: feed.xml is not served with Access-Control-Allow-Origin: * (SHOULD, §4)")
    if errors:
        print("\n".join("FAIL " + e for e in errors))
        sys.exit(1)
    print(f"blyg OK: {len(docs)} items, {len(items)} feed entries, level {manifest.get('level')}, protocol {manifest.get('blyg')}")

if __name__ == "__main__":
    main()
