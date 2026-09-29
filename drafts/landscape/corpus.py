#!/usr/bin/env python3
"""Step 1: assemble the reading corpus -> data/corpus.json.

Sources, in priority order (first one wins on duplicates):
  - planned_arc.json: the first syllabus (26 sessions, their "also read" pieces and Protocolized companions)
  - tools/themes.json: the current syllabus, by theme
  - sources/protocol-vision/inventory.md: the BPM source inventory (unpublished items excluded)
  - ~/Documents/rafaelfyi/v4/readings.json: a sample of the Daily NPC finds (prototype) or all (full run)
Session readings carry a seed area from the current syllabus; everything else is unlabelled.
"""
import hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
READINGS = Path.home() / "Documents/rafaelfyi/v4/readings.json"
FULL = "--full" in sys.argv
PROTOTYPE_FINDS = 20

SEED = {1: "swarms", 2: "swarms", 3: "nature", 4: "nature", 5: "records", 6: "records", 7: "records",
        8: "records", 9: "boards", 10: "boards", 11: "boards", 12: "boards", 13: "people", 14: "people",
        15: "people", 16: "people", 17: "people", 18: "people", 19: "firm", 20: "firm", 21: "firm",
        22: "firm", 23: "tending", 24: "tending", 25: "tending", 26: "tending"}
UNPUBLISHED = {29}  # inventory numbers not to be shown publicly
# Readings the SIG has already read: on the map, never in a syllabus path.
ALREADY_READ = [
    {"title": "Atoms, Institutions, Blockchains", "url": "https://paragraph.com/@josh-stark/atoms-institutions-blockchains",
     "cite": "Josh Stark, 2022 (Summer of Protocols edition, 2023)", "year": 2022, "quote": "",
     "local_pdf": str(Path.home() / "Documents/NPC/npcblog/SOP Research Archive/Atoms-Institutes-Blockchains-Josh-Stark.pdf")},
]


def norm_url(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
    return u


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def year_of(text):
    m = re.search(r"\b(1[89]\d\d|20\d\d)\b", text or "")
    return int(m.group(1)) if m else None


def from_sessions():
    out = []
    for i, s in enumerate(json.loads((HERE / "planned_arc.json").read_text()), 1):
        out.append({"title": s["title"], "url": s["url"], "cite": s["cite"], "year": year_of(s["cite"]),
                    "quote": s.get("quote", ""), "source": "session", "session": i, "seed": SEED[i]})
        a = s.get("also_read")
        if a:
            out.append({"title": a["title"], "url": a["url"], "cite": a["cite"], "year": year_of(a["cite"]),
                        "quote": a.get("quote", ""), "source": "session-also", "near_session": i})
        if s.get("pi_url"):
            out.append({"title": s["pi_title"], "url": s["pi_url"], "cite": s["pi_cite"],
                        "year": year_of(s["pi_cite"]), "quote": "", "source": "companion", "near_session": i})
    return out


def from_syllabus():
    """Readings from proposed syllabi that aren't in the corpus yet (they carry their own citation)."""
    out = []
    for t in json.loads((ROOT / "tools/themes.json").read_text())["themes"]:
        for r in t["readings"]:
            out.append({"title": r["title"], "url": r["url"], "cite": r["cite"], "year": year_of(r["cite"]),
                        "quote": r.get("quote", ""), "source": "proposed"})
    return out


def from_inventory():
    text = (ROOT / "sources/protocol-vision/inventory.md").read_text()
    out = []
    for m in re.finditer(r"^(\d+)\. \*\*(.+?)\*\*\n((?:[ \t]+-.*\n?)+)", text, re.M):
        n, title, body = int(m.group(1)), m.group(2), m.group(3)
        if n in UNPUBLISHED:
            continue
        url = re.search(r"https?://[^\s)]+", body)
        if not url:
            continue
        lines = [l.strip()[2:] for l in body.splitlines() if l.strip().startswith("- ")]
        cite = lines[0] if lines and not lines[0].startswith("http") else ""
        q = re.search(r'Quote[^:]*: "(.+?)"', body)
        out.append({"title": title, "url": url.group(0), "cite": cite, "year": year_of(cite),
                    "quote": q.group(1) if q else "", "source": "inventory", "inventory": n})
    return out


def from_readings():
    items = json.loads(READINGS.read_text())
    if not FULL:
        items = [x for x in items if "daily" in str(x.get("via", x.get("source", ""))).lower()][:PROTOTYPE_FINDS]
    out = []
    for x in items:
        out.append({"title": x.get("title", ""), "url": x.get("url", ""),
                    "cite": ", ".join(str(v) for v in (x.get("author"), x.get("publication"), x.get("year")) if v),
                    "year": x.get("year") if isinstance(x.get("year"), int) else year_of(str(x.get("year"))),
                    "quote": "", "excerpt": x.get("excerpt", ""), "source": "readings",
                    "via": x.get("via", x.get("source", ""))})
    return out


def main():
    seen_u, seen_t, corpus = set(), set(), []
    read = [dict(r, source="read", read=True) for r in ALREADY_READ]
    for r in from_sessions() + read + from_syllabus() + from_inventory() + from_readings():
        u, t = norm_url(r["url"]), norm_title(r["title"])
        if not r["url"] or not t or u in seen_u or t in seen_t:
            continue
        seen_u.add(u); seen_t.add(t)
        r["id"] = "r" + hashlib.sha1(u.encode()).hexdigest()[:8]  # stable across runs
        corpus.append(r)
    (HERE / "data").mkdir(exist_ok=True)
    (HERE / "data/corpus.json").write_text(json.dumps(corpus, ensure_ascii=False, indent=1))
    by = {}
    for r in corpus:
        by[r["source"]] = by.get(r["source"], 0) + 1
    print(f"{len(corpus)} readings:", by)


if __name__ == "__main__":
    main()
