#!/usr/bin/env python3
"""Render a 1200x630 share card for each blyg post into assets/cards/blyg/<id>.jpg, plus the blyg
index card (assets/cards/blyg.jpg). Needs Google Chrome and Pillow, so it runs on a laptop, not in CI;
commit the cards. Posts without a card fall back to the index card. Run after tools/build_blyg.py;
pass --force to re-render cards that already exist (for example after a title change)."""
import json, subprocess, sys, tempfile, urllib.parse
from datetime import datetime
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
TEMPLATE = ROOT / "tools/cards/blyg.html"
OUT = ROOT / "assets/cards/blyg"
sys.path.insert(0, str(ROOT / "tools"))
from build_blyg import title_of

def render(params, dest):
    with tempfile.TemporaryDirectory() as tmp:
        png = Path(tmp) / "card.png"
        url = TEMPLATE.as_uri() + "#" + urllib.parse.urlencode(params)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=5000",
                        "--window-size=1200,630", f"--screenshot={png}", url], check=True, capture_output=True)
        Image.open(png).convert("RGB").save(dest, quality=88, optimize=True)
    print("card ->", dest.relative_to(ROOT))

def main():
    force = "--force" in sys.argv
    OUT.mkdir(parents=True, exist_ok=True)
    index = ROOT / "assets/cards/blyg.jpg"
    if force or not index.exists():
        render({"title": "Blyg", "kind": "Session notes and research log"}, index)
    for f in sorted((ROOT / "blyg/items").glob("*.json")):
        if f.name == "index.json":
            continue
        d = json.loads(f.read_text())
        if d.get("kind") == "withdrawn":
            continue
        dest = OUT / f"{d['id']}.jpg"
        if dest.exists() and not force:
            continue
        kind = "Thread" if d["kind"] == "thread" else "Fragment"
        date = datetime.fromisoformat(d["created"].replace("Z", "+00:00")).strftime("%-d %B %Y")
        render({"title": title_of(d, kind), "kind": "Blyg", "date": date}, dest)

if __name__ == "__main__":
    main()
