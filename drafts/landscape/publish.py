#!/usr/bin/env python3
"""Step 5: publish the explorer to sessions/map/ (served with the site by deploy.sh).

Copies the explorer page, script and styles, the landscape data, and a light readings.json that
people's AI assistants can read (titles, links, citations, areas, themes; no passage text).
"""
import json, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "sessions" / "map" / "3d"
DATA = ROOT / "sessions" / "map"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    L = json.loads((HERE / "data/landscape.json").read_text())
    shutil.copy(HERE / "explorer/explorer.js", OUT / "explorer.js")
    shutil.copy(HERE / "explorer/explorer.css", OUT / "explorer.css")
    shutil.copy(HERE / "data/landscape.json", OUT / "landscape.json")
    page = (HERE / "explorer/index.html").read_text()
    page = page.replace('content="../data/landscape.json"', 'content="landscape.json"')
    page = page.replace('href="../../../sessions/"', 'href="../../"')
    page = page.replace('<p class="draft">Draft · <span id="count">', '<p class="draft"><span id="count">')
    (OUT / "index.html").write_text(page)

    areas = {a["id"]: a["name"] for a in L["areas"]}
    syllabus = L["paths"][0]
    theme_of = {id_: f'{m["n"]}. {m["name"]}' for m in syllabus["movements"] for id_ in m["stops"]}
    readings = sorted(({"title": r["title"], "url": r["url"], "cite": r["cite"], "year": r.get("year"),
                        "area": areas[r["area"]], **({"syllabus_theme": theme_of[r["id"]]} if r["id"] in theme_of else {}),
                        **({"already_read": True} if r.get("read") else {})}
                       for r in L["readings"]), key=lambda r: (r["area"], r["title"].lower()))
    (DATA / "readings.json").write_text(json.dumps(
        {"about": "Readings on the Protocols for Business SIG reading map, grouped by area. Readings in the year's syllabus carry their theme.",
         "map": "https://npc.here.now/protocolvision/sessions/map/",
         "suggest": "https://github.com/protocolvision/sig-p4b/issues/new?template=reading-suggestion.yml",
         "readings": readings}, ensure_ascii=False, indent=1) + "\n")
    print(f"published sessions/map/3d/ and sessions/map/readings.json ({len(readings)} readings)")


if __name__ == "__main__":
    main()
