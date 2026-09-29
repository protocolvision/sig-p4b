#!/usr/bin/env python3
"""Draw the six theme illustrations for the reading plan -> assets/themes/theme-1.svg ... theme-6.svg.

Line and dot drawings in the site's cobalt, generated from fixed seeds so they're reproducible:
  1 agents: a murmuration        2 natural coordination: cells signalling
  3 emissions: a log emitting     4 incidents: a crack through a lattice
  5 hard core: a bow-tie          6 keeping the core alive: pace layers
"""
import math, random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "themes"
W, H = 320, 140
INK = "#004fcc"


def svg(body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">'
            f'<rect width="{W}" height="{H}" rx="10" fill="#f2f6fd"/>{body}</svg>\n')


def dot(x, y, r, o):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}" fill="{INK}" fill-opacity="{o:.2f}"/>'


def murmuration():
    rng = random.Random(1)
    out = []
    for _ in range(900):
        t = rng.random()
        # a flock stretched along a curving ribbon that thickens in the middle
        cx = 30 + t * 260
        cy = 72 + 26 * math.sin(t * math.pi * 1.6 + 0.4) - 10 * math.cos(t * 5)
        spread = 6 + 30 * math.sin(math.pi * t) ** 1.5
        x = cx + rng.gauss(0, 5)
        y = cy + rng.gauss(0, spread * 0.45)
        out.append(dot(x, y, rng.uniform(0.7, 1.4), rng.uniform(0.35, 0.85)))
    return svg("".join(out), "A murmuration of starlings, drawn as dots")


def cells():
    rng = random.Random(2)
    out, pts = [], []
    while len(pts) < 16:
        x, y = rng.uniform(30, 290), rng.uniform(25, 115)
        if all(math.hypot(x - a, y - b) > 34 for a, b in pts):
            pts.append((x, y))
    for (x, y) in pts:
        a = rng.uniform(0, 180)
        out.append(f'<rect x="{x - 13:.1f}" y="{y - 5.5:.1f}" width="26" height="11" rx="5.5" fill="none" stroke="{INK}" '
                   f'stroke-opacity="0.7" stroke-width="1.4" transform="rotate({a:.0f} {x:.1f} {y:.1f})"/>')
    for _ in range(220):  # signalling molecules, denser where cells crowd
        x, y = rng.choice(pts)
        r, t = abs(rng.gauss(0, 16)) + 9, rng.uniform(0, 2 * math.pi)
        out.append(dot(x + r * math.cos(t), y + r * math.sin(t), 0.9, rng.uniform(0.25, 0.6)))
    return svg("".join(out), "Bacteria signalling to each other with small molecules")


def log():
    rng = random.Random(3)
    out = []
    for i in range(9):  # log entries, appended top to bottom
        y = 22 + i * 12
        w = rng.uniform(60, 120)
        out.append(f'<line x1="28" y1="{y}" x2="{28 + w:.1f}" y2="{y}" stroke="{INK}" stroke-opacity="{0.35 + i * 0.06:.2f}" '
                   f'stroke-width="3" stroke-linecap="round"/>')
        out.append(dot(22, y, 1.8, 0.8))
    for _ in range(140):  # entries travel out to readers on the right
        i = rng.randrange(9)
        y0 = 22 + i * 12
        t = rng.random()
        x = 160 + t * 140
        y = y0 + (70 - y0) * t * 0.35 + rng.gauss(0, 3 + 20 * t)
        out.append(dot(x, y, 1.1, 0.75 - 0.45 * t))
    return svg("".join(out), "A log of entries being published to many readers")


def crack():
    rng = random.Random(4)
    out = []
    # a jagged fracture running top to bottom, with short branches
    pts, x, y = [], 158, 6
    while y < 136:
        pts.append((x, y)); y += rng.uniform(6, 11); x += rng.uniform(-9, 9)
    pts.append((x, 136))
    branches = []
    for k in (4, 8, 12):
        if k < len(pts):
            bx, by = pts[k]; d = rng.choice((-1, 1)); seg = [(bx, by)]
            for _ in range(3):
                bx += d * rng.uniform(7, 12); by += rng.uniform(2, 8); seg.append((bx, by))
            branches.append(seg)
    def near(px, py):
        return min(abs(px - a) + abs(py - b) * 0.2 for a, b in pts)
    step = 18
    for gx in range(16, 305, step):
        for gy in range(16, 125, step):
            shift = 3 if gx > 158 else 0   # the right side has slipped
            o = 0.08 if near(gx, gy) < 14 else 0.2
            if gx + step <= 304:
                out.append(f'<line x1="{gx}" y1="{gy + shift}" x2="{gx + step}" y2="{gy + shift}" stroke="{INK}" stroke-opacity="{o}"/>')
            if gy + step <= 124:
                out.append(f'<line x1="{gx}" y1="{gy + shift}" x2="{gx}" y2="{gy + step + shift}" stroke="{INK}" stroke-opacity="{o}"/>')
            out.append(dot(gx, gy + shift, 1.5, 0.12 if near(gx, gy) < 14 else 0.3))
    for seg, w in [(pts, 2.4)] + [(b, 1.3) for b in branches]:
        d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in seg)
        out.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"/>')
    return svg("".join(out), "A regular lattice split by a crack")


def bowtie():
    rng = random.Random(5)
    out = []
    cx, cy = 160, 70
    for i in range(24):
        y1 = 12 + i * (116 / 23)
        out.append(f'<path d="M20,{y1:.1f} C95,{y1:.1f} 110,{cy} {cx - 16},{cy}" fill="none" stroke="{INK}" stroke-opacity="{rng.uniform(0.2, 0.5):.2f}" stroke-width="1.1"/>')
        y2 = 12 + ((i * 7) % 24) * (116 / 23)
        out.append(f'<path d="M{cx + 16},{cy} C210,{cy} 225,{y2:.1f} 300,{y2:.1f}" fill="none" stroke="{INK}" stroke-opacity="{rng.uniform(0.2, 0.5):.2f}" stroke-width="1.1"/>')
    out.append(f'<rect x="{cx - 17}" y="{cy - 17}" width="34" height="34" rx="6" fill="{INK}"/>')
    out.append(f'<rect x="{cx - 9}" y="{cy - 9}" width="18" height="18" rx="3" fill="#f2f6fd" fill-opacity="0.35"/>')
    return svg("".join(out), "Many inputs converging on a small hard core and fanning out again")


def layers():
    rng = random.Random(6)
    out = []
    cx, cy = 160, 150
    for i, r in enumerate([128, 104, 82, 62, 44, 28]):
        pts = []
        for k in range(61):
            t = math.pi * (1 + k / 60)
            rr = r + (6 - i) * 0.9 * math.sin(t * (3 + i) + i)
            pts.append((cx + rr * math.cos(t) * 1.25, cy + rr * math.sin(t)))
        d = "M" + " L".join(f"{a:.1f},{b:.1f}" for a, b in pts)
        out.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-opacity="{0.25 + i * 0.12:.2f}" stroke-width="{1 + i * 0.35:.2f}"/>')
    out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="22" ry="18" fill="{INK}"/>')
    return svg("".join(out), "Nested layers that change at different speeds around a slow core")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for i, f in enumerate([murmuration, cells, log, crack, bowtie, layers], 1):
        (OUT / f"theme-{i}.svg").write_text(f())
    print("wrote", ", ".join(f"theme-{i}.svg" for i in range(1, 7)))


if __name__ == "__main__":
    main()
