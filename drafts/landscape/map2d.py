#!/usr/bin/env python3
"""Step 6: a light 2D reading map -> src/sessions-map.html (built into sessions/map/ by build_site.py).

Draws the landscape as faint contour lines, every reading as a dot, and the year's syllabus in
cobalt, as one inline SVG. assets/map2d.js adds theme filters and reading details. It works on
phones and without WebGL; the 3D explorer lives at sessions/map/3d/.
"""
import html, json, math
from pathlib import Path
import numpy as np
from skimage.measure import find_contours

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
W, H, PAD = 1000, 760, 24
e = lambda s: html.escape(str(s or ""), quote=True)


def main():
    L = json.loads((HERE / "data/landscape.json").read_text())
    G = L["grid"]
    height = np.array(L["height"]).reshape(G, G)
    sx = lambda x: PAD + x * (W - 2 * PAD)
    sy = lambda y: PAD + y * (H - 2 * PAD)

    contours = []
    for level in (0.1, 0.22, 0.36, 0.5, 0.64, 0.78, 0.9):
        for c in find_contours(height, level):
            pts = c[::5]
            if len(pts) < 6:
                continue
            d = "M" + " ".join(f"{sx((col + .5) / G):.0f},{sy((row + .5) / G):.0f}" for row, col in pts)
            contours.append(f'<path d="{d}" class="c{int(level * 10)}"/>')

    syl = L["paths"][0]
    theme_of, session_of, companion = {}, {}, set()
    k = 0
    for i, m in enumerate(syl["movements"], 1):
        for rid in m["stops"]:
            theme_of[rid] = i
            if rid in m.get("companions", []):
                companion.add(rid); session_of[rid] = k - 1
            else:
                session_of[rid] = k; k += 1
    areas = {a["id"]: a for a in L["areas"]}

    dots, items = [], []
    order = sorted(range(len(L["readings"])), key=lambda i: L["readings"][i]["id"] in theme_of)  # syllabus drawn last, on top
    for idx in order:
        r = L["readings"][idx]
        t = theme_of.get(r["id"])
        cls = f"s t{t}" if t else "o"
        attrs = f' tabindex="0" role="button" aria-label="{e(r["title"])}"' if t else ""
        tip = f'<title>{e(r["title"])}</title>' if t else ""
        dots.append(f'<circle cx="{sx(r["x"]):.0f}" cy="{sy(r["y"]):.0f}" r="{5 if t else 3}" class="{cls}" data-i="{len(items)}"{attrs}>{tip}</circle>')
        items.append({"t": r["title"], "u": r["url"], "c": r["cite"], "a": areas[r["area"]]["name"], "th": t,
                      "s": session_of.get(r["id"]), "co": r["id"] in companion, "rd": bool(r.get("read"))})
    # place area labels, nudging any that would overlap an earlier one
    placed, labels = [], []
    for a in sorted(L["areas"], key=lambda a: a["y"]):
        x, y, w = sx(a["x"]), sy(a["y"]), len(a["name"]) * 9.5
        for _ in range(12):
            if not any(abs(x - px) < (w + pw) / 2 + 8 and abs(y - py) < 26 for px, py, pw in placed):
                break
            y += 26
        placed.append((x, y, w))
        labels.append(f'<text x="{x:.0f}" y="{y:.0f}" class="area">{e(a["name"])}</text>')
    T = json.loads((ROOT / "tools/themes.json").read_text())["themes"]
    by_id = {r["id"]: r for r in L["readings"]}
    # Place each tag at the nearest spot to its theme's centre that covers no syllabus dot, no area name,
    # and no other tag: try points on rings of growing radius around the centre.
    blue = [(sx(r["x"]), sy(r["y"])) for r in L["readings"] if r["id"] in theme_of]
    area_boxes = [(lx - lw / 2, ly - 16, lx + lw / 2, ly + 6) for lx, ly, lw in placed]
    tags, tag_pos = [], []
    for i, m in enumerate(syl["movements"], 1):
        pts = [(sx(by_id[rid]["x"]), sy(by_id[rid]["y"])) for rid in m["stops"]]
        cx, cy = sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts)
        label = f'{m["n"]} · {T[i - 1].get("short", m["name"])}'
        w, h = len(label) * 10 + 22, 30
        # the titles map2d.js draws to the right of this theme's dots (38 characters at most)
        name_boxes = [(bx, by - 12, bx + 12 + min(len(by_id[rid]["title"]), 38) * 7.2, by + 20)
                      for rid, (bx, by) in zip(m["stops"], pts)]

        def clear_at(x, y):
            x0, y0, x1, y1 = x - w / 2 - 6, y - h / 2 - 6, x + w / 2 + 6, y + h / 2 + 6
            if x0 < 4 or x1 > W - 4 or y0 < 4 or y1 > H - 4:
                return False
            if any(x0 <= bx <= x1 and y0 <= by <= y1 for bx, by in blue):
                return False
            if any(not (x1 < ax0 or ax1 < x0 or y1 < ay0 or ay1 < y0) for ax0, ay0, ax1, ay1 in area_boxes + name_boxes):
                return False
            return not any(abs(x - px) < (w + pw) / 2 + 8 and abs(y - py) < h + 8 for px, py, pw in tag_pos)

        best = None
        for radius in range(24, 400, 12):
            for k in range(24):
                ang = -math.pi / 2 + k * math.pi / 12   # start straight above the centre
                x, y = cx + radius * math.cos(ang), cy + radius * math.sin(ang)
                if clear_at(x, y):
                    best = (x, y); break
            if best:
                break
        x, y = best or (cx, cy - 40)
        tag_pos.append((x, y, w))
        tags.append(f'<g class="tag" data-th="{i}" tabindex="0" role="button" aria-label="Theme {e(m["n"])}: {e(m["name"])}" '
                    f'transform="translate({x:.0f},{y:.0f})"><rect x="{-w / 2:.0f}" y="-15" width="{w:.0f}" height="30" rx="15"/>'
                    f'<text y="5">{e(label)}</text></g>')
    svg = (f'<svg viewBox="0 0 {W} {H}" class="map" role="group" aria-labelledby="map-title map-desc" id="map">'
           f'<title id="map-title">Reading map</title><desc id="map-desc">{len(L["readings"])} readings placed by what they say. '
           f'Readings in this year’s plan are marked in blue.</desc>'
           f'<g class="contours" aria-hidden="true">{"".join(contours)}</g>'
           f'<g class="labels" aria-hidden="true">{"".join(labels)}</g><g class="spokes" aria-hidden="true"></g>'
           f'<g class="dots">{"".join(dots)}</g><g class="tags">{"".join(tags)}</g><g class="names" aria-hidden="true"></g></svg>')

    themes = [{"n": m["n"], "name": m["name"], "blurb": m["blurb"], "short": T[i].get("short", m["name"]),
               "x": round(tag_pos[i][0]), "y": round(tag_pos[i][1])} for i, m in enumerate(syl["movements"])]
    chips = '<button type="button" data-th="0" aria-pressed="true">All</button>' + "".join(
        f'<button type="button" data-th="{i}" aria-pressed="false">{e(m["n"])}. {e(m["name"])}</button>'
        for i, m in enumerate(syl["movements"], 1))
    by_area = "".join(
        f'<h3>{e(a["name"])}</h3><ul>' + "".join(
            f'<li><a href="{e(r["url"])}">{e(r["title"])}</a></li>'
            for r in sorted((r for r in L["readings"] if r["area"] == a["id"]), key=lambda r: r["title"].lower())) + "</ul>"
        for a in L["areas"])
    data = json.dumps({"items": items, "themes": themes, "slots": L["slots"]}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    body = f'''<!-- {{"title": "Reading map · Protocols for Business SIG", "desc": "{len(L["readings"])} readings placed by what they say, with this year’s reading plan marked.", "path": "sessions/map/", "nav": "sessions", "card": "syllabus"}} -->
<p class="meta"><a href="../">Sessions</a></p>
<h1>Reading map</h1>
<p class="lede">This map shows {len(L["readings"])} readings. Readings about similar ideas sit close together. The blue dots are this year’s reading plan. Point at a theme to see its readings, and zoom in to read the titles.</p>
<div class="map-wrap"><div class="map-zoom" role="group" aria-label="Zoom"><button type="button" data-z="in" aria-label="Zoom in">+</button><button type="button" data-z="out" aria-label="Zoom out">−</button><button type="button" data-z="reset">Reset</button></div>{svg}<div class="map-tip" hidden></div></div>
<div id="map-info" class="map-info" aria-live="polite"><p class="muted">Select a blue dot, or choose a theme above.</p></div>
<p class="small muted"><a href="3d/">Open the map in 3D</a> (best on a computer) · <a href="readings.json">All readings as data</a> · <a href="../#suggest">Suggest or challenge a reading</a></p>
<details><summary>All readings by area</summary>{by_area}</details>
<script type="application/json" id="map-data">{data}</script>
<script src="../../assets/map2d.js" defer></script>
'''
    (ROOT / "src/sessions-map.html").write_text(body)
    print(f"src/sessions-map.html: {len(contours)} contours, {len(items)} readings")


if __name__ == "__main__":
    main()
