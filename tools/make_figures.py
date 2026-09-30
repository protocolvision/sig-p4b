#!/usr/bin/env python3
"""Generate the site's line figures into assets/fig/*.svg.

Quiet, static line drawings in the site's ink and cobalt: a murmuration, a protocol network,
emissions, fault lines, a hard core with free edges, a heartbeat, quorum sensing. Each one is
drawn from a fixed seed, so rebuilding gives the same pictures. No scripts, no animation.
"""
import math, random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets/fig"
INK, COBALT, FAINT = "#262624", "#004fcc", "#c9c7c0"


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{label}">'
            f'<g fill="none" stroke-linecap="round" stroke-linejoin="round">{body}</g></svg>\n')


def f(x):
    return f"{x:.1f}"


def murmuration(w, h, seed, n=2400):
    """A flock with a dense, folded core and sharp edges: birds sampled from a density field built along two
    overlapping curved spines, each bird a short stroke aligned with the local heading."""
    r = random.Random(seed)
    ph, ph2 = r.random() * 6, r.random() * 6
    spines = []
    for k, (x0, x1, amp, wid, phase) in enumerate([(.1, .92, .22, .2, ph), (.3, .78, .16, .12, ph2)]):
        pts = []
        for i in range(60):
            t = i / 59
            x = w * (x0 + (x1 - x0) * t); y = h * (.5 + amp * math.sin(2.1 * math.pi * t + phase))
            pts.append((x, y, h * (.03 + wid * math.sin(math.pi * t) ** .8)))
        spines.append(pts)
    def field(x, y):
        best, head = 0.0, 0.0
        for pts in spines:
            for i, (sx, sy, sw) in enumerate(pts):
                d2 = (x - sx) ** 2 + ((y - sy) * 1.3) ** 2
                v = math.exp(-d2 / (2 * sw * sw))
                if v > best:
                    j = min(i + 1, len(pts) - 1); k = max(i - 1, 0)
                    best, head = v, math.atan2(pts[j][1] - pts[k][1], pts[j][0] - pts[k][0])
        return best, head
    out, tries = [], 0
    while len(out) < n and tries < n * 40:
        tries += 1
        x, y = r.random() * w, r.random() * h
        v, head = field(x, y)
        if r.random() > 1 / (1 + math.exp(-(v - .45) * 14)):   # a sigmoid gives the flock a crisp edge
            continue
        a = head + r.gauss(0, .18); L = 2.2 + r.random() * 1.8
        col = COBALT if r.random() < .015 else INK
        out.append(f'<path d="M{f(x)} {f(y)}l{f(math.cos(a) * L)} {f(math.sin(a) * L)}" stroke="{col}" stroke-width="1.25" opacity="{min(1, .45 + v * .6):.2f}"/>')
    return svg(w, h, "".join(out), "A murmuration of starlings, drawn as small aligned strokes")


def network(w, h, seed, n=22):
    r = random.Random(seed)
    pts = [(24 + r.random() * (w - 48), 18 + r.random() * (h - 36)) for _ in range(n)]
    edges = set()
    for i, (x, y) in enumerate(pts):
        near = sorted(range(n), key=lambda j: (pts[j][0] - x) ** 2 + (pts[j][1] - y) ** 2)[1:4]
        for j in near: edges.add(tuple(sorted((i, j))))
    out = []
    for i, j in sorted(edges):
        (x1, y1), (x2, y2) = pts[i], pts[j]
        out.append(f'<path d="M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}" stroke="{FAINT}" stroke-width="1"/>')
    for i, j in r.sample(sorted(edges), min(7, len(edges))):   # messages in flight
        (x1, y1), (x2, y2) = pts[i], pts[j]; u = .3 + r.random() * .4
        out.append(f'<path d="M{f(x1)} {f(y1)}L{f(x1 + (x2 - x1) * u)} {f(y1 + (y2 - y1) * u)}" stroke="{COBALT}" stroke-width="1.6"/>')
        out.append(f'<rect x="{f(x1 + (x2 - x1) * u - 2.5)}" y="{f(y1 + (y2 - y1) * u - 2.5)}" width="5" height="5" fill="{COBALT}" stroke="none"/>')
    for x, y in pts:
        out.append(f'<rect x="{f(x - 4)}" y="{f(y - 4)}" width="8" height="8" stroke="{INK}" stroke-width="1.3" fill="#fff"/>')
    return svg(w, h, "".join(out), "Agents as nodes, with messages moving along the connections between them")


def emissions(w, h, seed):
    r = random.Random(seed)
    out, dots = [], [(r.random() * w, r.random() * h) for _ in range(260)]
    srcs = [(w * (.2 + .6 * r.random()), h * (.25 + .5 * r.random())) for _ in range(3)]
    rings = []
    for sx, sy in srcs:
        for k in range(1, 5):
            rad = k * h * .16
            rings.append((sx, sy, rad))
            out.append(f'<circle cx="{f(sx)}" cy="{f(sy)}" r="{f(rad)}" stroke="{INK}" stroke-width="1" opacity="{1 - k * .2:.2f}"/>')
        out.append(f'<rect x="{f(sx - 4)}" y="{f(sy - 4)}" width="8" height="8" fill="{INK}" stroke="none"/>')
    for x, y in dots:
        hit = any(abs(math.hypot(x - sx, y - sy) - rad) < 3 for sx, sy, rad in rings)
        out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{2.2 if hit else 1.2}" fill="{COBALT if hit else FAINT}" stroke="none"/>')
    return svg(w, h, "".join(out), "Signals spreading in rings from a few sources; the readers they reach light up")


def faults(w, h, seed):
    """An orderly grid of blocks, and a crack that runs across it, tapering and branching as it goes."""
    r = random.Random(seed)
    out = []
    for gx in range(0, int(w), 28):
        for gy in range(0, int(h), 28):
            out.append(f'<rect x="{gx + 4}" y="{gy + 4}" width="20" height="20" stroke="{FAINT}" stroke-width="1"/>')
    y0 = h * (.35 + .3 * r.random())
    tips, segs, branches = [(0.0, y0, 0.0, 2.8, 10 ** 6)], [], 0   # (x, y, heading, width, steps left)
    while tips:
        x, y, a, sw, life = tips.pop()
        main = life > 10 ** 5
        while life > 0 and 0 <= x < w and 0 < y < h:
            a2 = a + r.gauss(0, .42); x2, y2 = x + math.cos(a2) * 6, y + math.sin(a2) * 6
            segs.append((x, y, x2, y2, sw)); x, y, life = x2, y2, life - 1
            pull = (h / 2 - y) / h * .8 if main else 0   # the main crack drifts right and stays in frame
            a = a2 * .8 + pull
            if not main: sw *= .97
            if main and r.random() < .025 and branches < 7:
                branches += 1; tips.append((x, y, a + r.choice([-1.0, 1.0]) * (.6 + r.random() * .5), sw * .5, r.randint(8, 22)))
    for x, y, x2, y2, sw in segs:
        out.append(f'<path d="M{f(x)} {f(y)}L{f(x2)} {f(y2)}" stroke="{INK}" stroke-width="{sw:.2f}"/>')
    out.append(f'<circle cx="6" cy="{f(y0)}" r="5" fill="{COBALT}" stroke="none"/>')
    return svg(w, h, "".join(out), "A crack running across an orderly grid of blocks and branching as it goes")


def hardcore(w, h, seed):
    r = random.Random(seed)
    cx, cy, R = w / 2, h / 2, min(w, h) * .27
    hexp = lambda rad, rot=0: "M" + "L".join(f"{f(cx + rad * math.cos(i * math.pi / 3 + rot))} {f(cy + rad * math.sin(i * math.pi / 3 + rot))}" for i in range(6)) + "Z"
    out = [f'<path d="{hexp(R)}" stroke="{INK}" stroke-width="2.6"/>', f'<path d="{hexp(R * .78)}" stroke="{INK}" stroke-width="1"/>',
           f'<path d="{hexp(R * .56)}" stroke="{COBALT}" stroke-width="1.4"/>']
    for _ in range(70):   # free agents outside, some bouncing off the core
        a = r.random() * math.tau; d = R * 1.12 + r.random() * max(w, h) * .45
        x, y = cx + math.cos(a) * d, cy + math.sin(a) * d * .7
        if not (6 < x < w - 6 and 6 < y < h - 6): continue
        if r.random() < .3:
            bx, by = cx + math.cos(a) * R * 1.02, cy + math.sin(a) * R * 1.02
            out.append(f'<path d="M{f(x)} {f(y)}L{f(bx)} {f(by)}L{f(bx + math.cos(a + 1.1) * 30)} {f(by + math.sin(a + 1.1) * 30)}" stroke="{FAINT}" stroke-width="1" stroke-dasharray="2 3"/>')
        out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="2.4" fill="{INK}" stroke="none"/>')
    return svg(w, h, "".join(out), "A hexagonal hard core, with free agents moving around it and bouncing off its edge")


def heartbeat(w, h, seed):
    r = random.Random(seed)
    out = []
    for gx in range(0, int(w), 16): out.append(f'<path d="M{gx} 0V{h}" stroke="{FAINT}" stroke-width="{.8 if gx % 80 else 1.2}" opacity=".6"/>')
    for gy in range(0, int(h), 16): out.append(f'<path d="M0 {gy}H{w}" stroke="{FAINT}" stroke-width="{.8 if gy % 80 else 1.2}" opacity=".6"/>')
    mid, x, d = h * .58, 0.0, [f"M0 {f(h * .58)}"]
    while x < w:
        period = 110 + r.random() * 30
        d.append(f"L{f(x + period * .45)} {f(mid + r.gauss(0, 1))}")
        d.append(f"L{f(x + period * .5)} {f(mid - h * .38)}L{f(x + period * .55)} {f(mid + h * .22)}L{f(x + period * .6)} {f(mid - h * .06)}L{f(x + period * .65)} {f(mid)}")
        x += period
    out.append(f'<path d="{"".join(d)}" stroke="{INK}" stroke-width="1.8"/>')
    out.append(f'<circle cx="{f(w - 10)}" cy="{f(mid)}" r="4" fill="{COBALT}" stroke="none"/>')
    return svg(w, h, "".join(out), "A heartbeat trace running across graph paper")


def quorum(w, h, seed):
    r = random.Random(seed)
    out, cells = [], []
    for _ in range(90):
        x, y = r.random() * w, r.random() * h
        dens = math.exp(-((x - w * .65) ** 2) / (2 * (w * .18) ** 2))
        if r.random() > .25 + dens: continue
        cells.append((x, y, dens))
    for x, y, dens in cells:
        on = dens > .55
        out.append(f'<rect x="{f(x - 7)}" y="{f(y - 3.5)}" width="14" height="7" rx="3.5" stroke="{COBALT if on else INK}" stroke-width="1.2" transform="rotate({r.randint(0, 179)} {f(x)} {f(y)})"/>')
        for _ in range(3 if on else 1):
            out.append(f'<circle cx="{f(x + r.gauss(0, 10))}" cy="{f(y + r.gauss(0, 10))}" r="1.1" fill="{COBALT if on else FAINT}" stroke="none"/>')
    return svg(w, h, "".join(out), "Bacteria releasing signal molecules; where they are dense enough, they switch on together")


def ledger(w, h, seed):
    r = random.Random(seed)
    out = []
    for i, y in enumerate(range(14, int(h) - 6, 14)):
        L = w * (.35 + .6 * r.random())
        out.append(f'<text x="0" y="{y + 4}" font-family="ui-monospace, Menlo, monospace" font-size="9" fill="{FAINT}">{i:04d}</text>')
        out.append(f'<path d="M34 {y}H{f(34 + L * .8)}" stroke="{INK if i != 7 else COBALT}" stroke-width="{1.2 if i != 7 else 2}"/>')
        if r.random() < .3: out.append(f'<path d="M{f(40 + L * .8)} {y}h{f(r.random() * 60)}" stroke="{FAINT}" stroke-width="1"/>')
    return svg(w, h, "".join(out), "An append-only log: numbered lines, one of them highlighted")


def gather(w, h, seed, n=70):
    """People converging on one meeting: strokes streaming along curves into a single cobalt point."""
    r = random.Random(seed)
    tx, ty = w * .86, h * .74   # low and right: the empty corner beside the Register button
    out = []
    for _ in range(n):
        side = r.random()
        sx, sy = (r.random() * w * .5, -10) if side < .3 else (r.random() * w * .5, h + 10) if side < .6 else (-10, r.random() * h)
        cx, cy = sx + (tx - sx) * .5 + r.gauss(0, h * .35), sy + (ty - sy) * .5 + r.gauss(0, h * .35)
        for k in range(12):
            t = (k + r.random() * .6) / 12
            if t > .96: break
            x = (1 - t) ** 2 * sx + 2 * (1 - t) * t * cx + t * t * tx; y = (1 - t) ** 2 * sy + 2 * (1 - t) * t * cy + t * t * ty
            dx = 2 * (1 - t) * (cx - sx) + 2 * t * (tx - cx); dy = 2 * (1 - t) * (cy - sy) + 2 * t * (ty - cy)
            a = math.atan2(dy, dx); L = 2.5 + t * 2
            out.append(f'<path d="M{f(x)} {f(y)}l{f(math.cos(a) * L)} {f(math.sin(a) * L)}" stroke="{INK}" stroke-width="1.2" opacity="{.2 + t * .7:.2f}"/>')
    for k in (1, 2, 3):
        out.append(f'<circle cx="{f(tx)}" cy="{f(ty)}" r="{6 + k * 9}" stroke="{COBALT}" stroke-width="1" opacity="{.6 - k * .15:.2f}"/>')
    out.append(f'<rect x="{f(tx - 5)}" y="{f(ty - 5)}" width="10" height="10" fill="{COBALT}" stroke="none"/>')
    return svg(w, h, "".join(out), "Strokes converging from all sides on a single point")


FIGS = {
    "murmuration": (murmuration, 1200, 300, 7),
    "network": (network, 1200, 260, 11),
    "faults": (faults, 1200, 240, 5),
    "hardcore": (hardcore, 1200, 300, 3),
    "emissions": (emissions, 1200, 260, 2),
    "heartbeat": (heartbeat, 1200, 180, 4),
    "ledger": (ledger, 1200, 180, 9),
    # one small strip per theme, in the order of the year
    "theme-1": (network, 640, 120, 21), "theme-2": (murmuration, 640, 120, 22), "theme-3": (emissions, 640, 120, 23),
    "theme-4": (faults, 640, 120, 24), "theme-5": (hardcore, 640, 120, 25), "theme-6": (heartbeat, 640, 120, 26),
    "quorum": (quorum, 1200, 220, 8),
    "gather": (gather, 480, 200, 12),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (fn, w, h, seed) in FIGS.items():
        (OUT / f"{name}.svg").write_text(fn(w, h, seed))
    print(f"{len(FIGS)} figures in {OUT}")
