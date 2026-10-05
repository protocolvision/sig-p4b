#!/usr/bin/env python3
"""Generate the site's figures into assets/fig/*.svg, as hairline technical drawings.

Every figure uses the drafting kit in tools/drafting.py: hairline weights, centre and construction
lines, dimension lines with architectural ticks, numbered callouts, section hatching, axonometric
projection and a small title block. Ink and cobalt only. Each figure is drawn from a fixed seed, so
rebuilding gives the same pictures. No scripts, no animation.
"""
import math, random
from pathlib import Path
from drafting import Sheet, iso, MONO, INK, COBALT, MUTED, FAINT, PAPER, HAIR, FINE, MEDIUM, HEAVY

OUT = Path(__file__).resolve().parent.parent / "assets/fig"
STRIP = 150   # figures this short are strips: no title block, just corner ticks and a label


def finish(s, n, title, strip_label=None):
    if s.h <= STRIP and strip_label:
        for cx, cy, sx, sy in ((4, 4, 1, 1), (s.w - 4, 4, -1, 1), (4, s.h - 4, 1, -1), (s.w - 4, s.h - 4, -1, -1)):
            s.line(cx, cy, cx + 8 * sx, cy, INK, FINE); s.line(cx, cy, cx, cy + 8 * sy, INK, FINE)
        s.text(12, s.h - 9, strip_label, 7.5, MUTED, spacing=1)
    elif s.h > STRIP:
        s.frame(n, title)
    return s.svg()


# --- murmuration: a flock of hairline ticks, with its spine and one bird's seven neighbours ----------
def murmuration(w, h, seed, n=1500, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "A murmuration of starlings, with one bird's seven nearest neighbours marked")
    ph = r.random() * 6
    spine = []
    for i in range(70):
        t = i / 69
        spine.append((w * (.08 + .84 * t), h * (.48 + .22 * math.sin(2.1 * math.pi * t + ph)), h * (.04 + .17 * math.sin(math.pi * t) ** .8)))
    def field(x, y):
        best, head = 0.0, 0.0
        for i, (sx, sy, sw) in enumerate(spine):
            v = math.exp(-((x - sx) ** 2 + ((y - sy) * 1.3) ** 2) / (2 * sw * sw))
            if v > best:
                j, k = min(i + 1, 69), max(i - 1, 0)
                best, head = v, math.atan2(spine[j][1] - spine[k][1], spine[j][0] - spine[k][0])
        return best, head
    birds, tries = [], 0
    while len(birds) < n and tries < n * 40:
        tries += 1
        x, y = r.random() * w, r.random() * h * .92
        v, head = field(x, y)
        if r.random() < 1 / (1 + math.exp(-(v - .45) * 14)):
            birds.append((x, y, head + r.gauss(0, .16), v))
    for i in range(0, 69, 1):   # the flock's spine as a centre line
        pass
    s.path([(x, y) for x, y, _ in spine[::3]], MUTED, HAIR, "14 3 2 3")
    for x, y, a, v in birds:
        L = 2.2 + v * 2
        s.line(x, y, x + math.cos(a) * L, y + math.sin(a) * L, INK, .7, op=round(.35 + .6 * v, 2))
    if h > STRIP and birds:
        bx, by, _, _ = max(birds, key=lambda b: b[3] - abs(b[0] - w * .45) / w)
        near = sorted(birds, key=lambda b: (b[0] - bx) ** 2 + (b[1] - by) ** 2)[1:8]
        rad = max(math.hypot(b[0] - bx, b[1] - by) for b in near)
        s.circle(bx, by, rad + 3, COBALT, HAIR, dash="2 2")
        for b in near:
            s.line(bx, by, b[0], b[1], COBALT, HAIR)
        s.dot(bx, by, 2.2, COBALT)
        s.callout(bx + rad * .7, by - rad * .7, 1, bx + 60, by - 70, INK, "EACH BIRD TRACKS ~7 NEIGHBOURS")
        s.dim(spine[5][0], h * .9, spine[64][0], h * .9, "ONE FLOCK · NO LEADER", -8)
    return finish(s, 1, "Murmuration", label)


# --- network: agents as numbered nodes, messages as arrows on the edges -------------------------------
def network(w, h, seed, n=20, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "Agents as numbered nodes, with messages moving along the connections between them")
    pad = 30
    pts = []
    while len(pts) < n:
        p = (pad + r.random() * (w - 2 * pad), pad * .7 + r.random() * (h - 2.4 * pad))
        if all(math.hypot(p[0] - q[0], p[1] - q[1]) > 46 for q in pts):
            pts.append(p)
    edges = set()
    for i, (x, y) in enumerate(pts):
        for j in sorted(range(n), key=lambda j: (pts[j][0] - x) ** 2 + (pts[j][1] - y) ** 2)[1:4]:
            edges.add(tuple(sorted((i, j))))
    edges = sorted(edges)
    for i, j in edges:
        s.line(*pts[i], *pts[j], INK, HAIR)
    for i, j in r.sample(edges, min(8, len(edges))):
        (x1, y1), (x2, y2) = pts[i], pts[j]
        u = .35 + r.random() * .3; mx, my = x1 + (x2 - x1) * u, y1 + (y2 - y1) * u
        s.line(x1, y1, mx, my, COBALT, FINE); s.arrow(mx, my, math.atan2(y2 - y1, x2 - x1), 6, COBALT)
    for k, (x, y) in enumerate(pts):
        s.rect(x - 4.5, y - 4.5, 9, 9, INK, FINE, fill=PAPER)
        if h > STRIP:
            s.text(x + 8, y - 6, f"A{k + 1:02d}", 7, MUTED, spacing=.4)
    if h > STRIP:
        a, b = edges[0]
        s.callout(*pts[a], 1, pts[a][0] + 30, pts[a][1] + 40, INK, "AGENT")
        i, j = edges[len(edges) // 2]
        mx, my = (pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2
        s.callout(mx, my, 2, mx + 40, my + 34, INK, "CONNECTION · WHAT THEY CAN READ AND WRITE")
    return finish(s, 2, "Agent network", label)


# --- emissions: sources, rings dimensioned by time, the readers they reach ----------------------------
def emissions(w, h, seed, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "Signals spreading in rings from a few sources; the readers they reach are marked")
    srcs = [(w * (.18 + .64 * k / 2 + r.uniform(-.04, .04)), h * (.42 + r.uniform(-.08, .08))) for k in range(3)]
    rings = []
    for k, (sx, sy) in enumerate(srcs):
        s.centerline(sx - h * .55, sy, sx + h * .55, sy) if h > STRIP else None
        for t in range(1, 5):
            rad = t * h * .14
            rings.append((sx, sy, rad))
            s.circle(sx, sy, rad, INK, HAIR, dash=None if t % 2 else "3 3", op=round(1 - t * .16, 2))
        s.rect(sx - 4, sy - 4, 8, 8, INK, FINE, fill=INK)
    for _ in range(220):
        x, y = r.random() * w, r.random() * h * .9
        hit = any(abs(math.hypot(x - sx, y - sy) - rad) < 2.5 for sx, sy, rad in rings)
        if hit:
            s.circle(x, y, 2.6, COBALT, FINE); s.dot(x, y, 1, COBALT)
        else:
            s.dot(x, y, .9, MUTED, .7)
    if h > STRIP:
        sx, sy = srcs[0]
        s.dim(sx, sy, sx + 3 * h * .14, sy, "t = 3", -h * .3)
        s.callout(sx, sy, 1, sx - 50, sy - 70, INK, "SOURCE")
        s.callout(*srcs[1], 2, srcs[1][0] + 60, srcs[1][1] - 74, INK, "WHAT IT EMITS")
    return finish(s, 3, "Emissions", label)


# --- faults: an orderly grid, a crack through it, a section line A-A ----------------------------------
def faults(w, h, seed, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "A crack running across an orderly grid of blocks, with a section line through it")
    step = 26
    for gx in range(14, int(w) - 10, step):
        for gy in range(14, int(h) - 26, step):
            s.rect(gx, gy, step - 6, step - 6, FAINT, HAIR)
    y0 = h * (.35 + .25 * r.random())
    tips, segs, branches = [(14.0, y0, 0.0, 2.2, 10 ** 6)], [], 0
    while tips:
        x, y, a, sw, life = tips.pop()
        main = life > 10 ** 5
        while life > 0 and 0 <= x < w - 14 and 12 < y < h - 28:
            a2 = a + r.gauss(0, .42); x2, y2 = x + math.cos(a2) * 5, y + math.sin(a2) * 5
            segs.append((x, y, x2, y2, sw)); x, y, life = x2, y2, life - 1
            a = a2 * .8 + ((h / 2 - y) / h * .8 if main else 0)
            if not main: sw *= .96
            if main and r.random() < .025 and branches < 7:
                branches += 1; tips.append((x, y, a + r.choice([-1.0, 1.0]) * (.6 + r.random() * .5), sw * .5, r.randint(8, 22)))
    for x, y, x2, y2, sw in segs:
        s.line(x, y, x2, y2, INK, round(sw * .7, 2))
    if h > STRIP:
        # the blocks the crack passes through are cut: hatch them like a section
        cut = set()
        for x, y, *_ in segs[::3]:
            cut.add((int((x - 14) // step), int((y - 14) // step)))
        hatch = s.hatch(4, 45, INK, .4)
        for cx, cy in cut:
            gx, gy = 14 + cx * step, 14 + cy * step
            if gx < w - 20 and gy < h - 30:
                s.rect(gx, gy, step - 6, step - 6, INK, HAIR, fill=hatch)
        sxl = w * .62
        s.centerline(sxl, 10, sxl, h - 30, INK)
        for yy, lab in ((16, "A"), (h - 36, "A")):
            s.arrow(sxl - 10, yy, math.pi, 6, INK); s.line(sxl, yy, sxl - 10, yy, INK, FINE)
            s.text(sxl + 6, yy + 3, lab, 9, INK, weight=500)
        s.callout(segs[0][0] + 4, segs[0][1], 1, 60, y0 - 40 if y0 > 60 else y0 + 40, COBALT, "ORIGIN")
    else:
        s.dot(segs[0][0] + 2, segs[0][1], 3, COBALT)
    return finish(s, 4, "Fault line", label)


# --- hard core: an axonometric building, a hatched core and free floor plates around it ----------------
def hardcore(w, h, seed, label=None, survey=False):
    r = random.Random(seed)
    s = Sheet(w, h, "An axonometric drawing: a hatched hard core rising through free floor plates")
    sc = min(w / 760, h / 470) * (1.15 if survey else 1)   # sized so the whole building fits its frame
    ox, oy = w * (.46 if not survey else .62), h * (.64 if not survey else .66)
    core, plate, levels = 34, 120, 4
    hatch = s.hatch(3.5, 60, INK, .45)
    for lv in range(levels):   # floor plates: thin slabs at each level
        z = lv * 40
        top = [iso(-plate, -plate, z, ox, oy, sc), iso(plate, -plate, z, ox, oy, sc), iso(plate, plate, z, ox, oy, sc), iso(-plate, plate, z, ox, oy, sc)]
        s.path(top, INK, HAIR, close=True, fill=PAPER if lv else "none")
        edge = [iso(plate, -plate, z, ox, oy, sc), iso(plate, plate, z, ox, oy, sc), iso(plate, plate, z - 4, ox, oy, sc), iso(plate, -plate, z - 4, ox, oy, sc)]
        s.path(edge, INK, HAIR, close=True)
        edge2 = [iso(-plate, plate, z, ox, oy, sc), iso(plate, plate, z, ox, oy, sc), iso(plate, plate, z - 4, ox, oy, sc), iso(-plate, plate, z - 4, ox, oy, sc)]
        s.path(edge2, INK, HAIR, close=True)
        for _ in range(10 if not survey else 7):   # people and agents, free on each floor
            px, py = r.uniform(-plate + 10, plate - 10), r.uniform(-plate + 10, plate - 10)
            if abs(px) < core + 14 and abs(py) < core + 14:
                continue
            x, y = iso(px, py, z, ox, oy, sc)
            s.dot(x, y, 1.6 * sc, INK, .8)
    ztop = levels * 40 + 18
    for face in ([(core, -core), (core, core)], [(-core, core), (core, core)]):   # the core: two hatched faces
        (ax, ay), (bx, by) = face
        quad = [iso(ax, ay, -6, ox, oy, sc), iso(bx, by, -6, ox, oy, sc), iso(bx, by, ztop, ox, oy, sc), iso(ax, ay, ztop, ox, oy, sc)]
        s.path(quad, INK, MEDIUM, close=True, fill=hatch)
    roof = [iso(-core, -core, ztop, ox, oy, sc), iso(core, -core, ztop, ox, oy, sc), iso(core, core, ztop, ox, oy, sc), iso(-core, core, ztop, ox, oy, sc)]
    s.path(roof, COBALT, MEDIUM, close=True, fill=PAPER)
    # centre line of the core
    x1, y1 = iso(0, 0, -20, ox, oy, sc); x2, y2 = iso(0, 0, ztop + 30, ox, oy, sc)
    s.centerline(x1, y1, x2, y2, MUTED)
    if h > STRIP and not survey:   # the advisory version is the plain drawing, no words
        a, b = iso(core, core, -6, ox, oy, sc), iso(core, core, ztop, ox, oy, sc)
        s.dim(a[0], a[1], b[0], b[1], "HARD CORE", -18 * sc)
        pa = iso(plate, -plate, 120, ox, oy, sc)
        rx = iso(-plate, plate, 40, ox, oy, sc)
        if survey:
            pass   # the box beside it carries the words; the drawing stays clean
        else:
            s.callout(*iso(0, 0, ztop, ox, oy, sc), 1, w * .74, h * .14, INK, "HARD CORE · ENFORCED EVERY TIME")
            s.callout(*pa, 2, w * .74, h * .36, INK, "FLOOR PLATE · SOFT NORMS")
            s.callout(*rx, 3, w * .2, h * .78, INK, "FREE EDGES · PEOPLE AND AGENTS")
    return s.svg() if survey else finish(s, 5, "Hard core, free edges", label)


def advisory(w, h, seed):
    """The hard core drawing for a small box: same geometry, heavier pen, so it reads at a glance."""
    svg = hardcore(w, h, seed, survey=True)
    for a, b in (('stroke-width="0.5"', 'stroke-width="1.1"'), ('stroke-width="0.75"', 'stroke-width="1.5"'),
                 ('stroke-width="1.1"', 'stroke-width="1.6"'), ('stroke-width="0.45"', 'stroke-width="0.8"')):
        svg = svg.replace(a, b)
    return svg


# --- heartbeat: an ECG trace on graph paper, with axes ---------------------------------------------
def heartbeat(w, h, seed, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "A heartbeat trace on graph paper")
    for gx in range(0, int(w), 10):
        s.line(gx, 0, gx, h, FAINT, .25 if gx % 50 else .5)
    for gy in range(0, int(h), 10):
        s.line(0, gy, w, gy, FAINT, .25 if gy % 50 else .5)
    mid = h * .58
    s.centerline(0, mid, w, mid, MUTED)
    x, pts, beats = 0.0, [(0, mid)], []
    while x < w:
        p = 110 + r.random() * 25
        pts += [(x + p * .45, mid + r.gauss(0, .6)), (x + p * .5, mid - h * .4), (x + p * .55, mid + h * .2), (x + p * .6, mid - h * .06), (x + p * .66, mid)]
        beats.append(x + p * .5); x += p
    s.path(pts, INK, FINE)
    s.dot(w - 10, mid, 3, COBALT)
    if h > STRIP:
        s.dim(beats[2], h - 26, beats[3], h - 26, "1 BEAT", 0)
    return finish(s, 6, "Liveness", label)


# --- ledger: an append-only field log, columns ruled ------------------------------------------------
def ledger(w, h, seed, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "An append-only field log: numbered entries with the reason for each, one highlighted")
    cols = [("#", 16), ("TIME", 60), ("WHO", 140), ("ACTION", 260), ("WHY", 560)]
    top = 20
    for name, x in cols:
        s.text(x, top, name, 7.5, MUTED, spacing=1)
        s.line(x - 6, top - 10, x - 6, h - 28, FAINT, HAIR)
    s.line(10, top + 6, w - 10, top + 6, INK, FINE)
    y, i = top + 20, 0
    while y < h - 32:
        hot = i == 4
        col = COBALT if hot else INK
        s.text(16, y + 3, f"{i:03d}", 7.5, col, spacing=.4)
        s.text(60, y + 3, f"{9 + i // 3:02d}:{(i * 17) % 60:02d}", 7.5, MUTED, spacing=.4)
        s.line(140, y, 140 + 40 + r.random() * 50, y, col, FINE if hot else HAIR)
        s.line(260, y, 260 + 80 + r.random() * 160, y, col, FINE if hot else HAIR)
        s.line(560, y, 560 + 120 + r.random() * (w - 720), y, col, FINE if hot else HAIR)
        s.line(10, y + 8, w - 10, y + 8, FAINT, .3)
        y += 16; i += 1
    if h > STRIP:
        s.callout(560, top + 20 + 4 * 16, 1, w - 120, top + 2, COBALT, "THE REASON")
    return finish(s, 7, "Field log", label)


# --- quorum: cells and a threshold where they switch on together -----------------------------------
def quorum(w, h, seed, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "Bacteria along a gradient of signal; past the quorum threshold they switch on together")
    th = w * .58
    hatch = s.hatch(3, 45, COBALT, .5)
    for _ in range(150):
        x, y = 20 + r.random() * (w - 40), 16 + r.random() * (h - 54)
        dens = x / w
        if r.random() > .2 + dens * .9:
            continue
        on = x > th
        a = r.randint(0, 179)
        rx, ry = 8, 3.6
        s.out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rx}" ry="{ry}" transform="rotate({a} {x:.1f} {y:.1f})" '
                     f'stroke="{COBALT if on else INK}" stroke-width="{FINE if on else HAIR}" fill="{hatch if on else "none"}"/>')
        for _ in range(3 if on else 1):
            s.dot(x + r.gauss(0, 9), y + r.gauss(0, 9), .8, COBALT if on else MUTED)
    s.centerline(th, 8, th, h - 30, INK)
    s.text(th + 6, 18, "QUORUM", 8, INK, weight=500, spacing=1)
    s.dim(30, h - 22, th - 10, h - 22, "SIGNAL RISES WITH DENSITY", 0)
    return finish(s, 8, "Quorum sensing", label)


# --- gather: flow lines converging on one session -------------------------------------------------------
def gather(w, h, seed, n=46):
    r = random.Random(seed)
    s = Sheet(w, h, "Lines converging from all sides on a single point")
    tx, ty = w * .86, h * .74
    for _ in range(n):
        side = r.random()
        sx, sy = (r.random() * w * .55, -10) if side < .3 else (r.random() * w * .55, h + 10) if side < .6 else (-10, r.random() * h)
        cx, cy = sx + (tx - sx) * .5 + r.gauss(0, h * .16), sy + (ty - sy) * .5 + r.gauss(0, h * .16)
        pts = []
        for k in range(28):
            t = k / 27 * .93
            pts.append(((1 - t) ** 2 * sx + 2 * (1 - t) * t * cx + t * t * tx, (1 - t) ** 2 * sy + 2 * (1 - t) * t * cy + t * t * ty))
        s.path(pts, INK, HAIR, op=.75)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        s.arrow(x2, y2, math.atan2(y2 - y1, x2 - x1), 4, INK, HAIR)
    for k in (1, 2, 3):
        s.circle(tx, ty, 6 + k * 9, COBALT, HAIR, dash=None if k == 1 else "2 2")
    s.rect(tx - 4, ty - 4, 8, 8, COBALT, FINE, fill=COBALT)
    return s.svg()


# --- braitenberg vehicles: wiring alone produces fear, aggression and love ----------------------------
def vehicle(s, x, y, a, scale, crossed, inhibitory, col=INK):
    """A Braitenberg vehicle in plan view: body, two wheels (motors), two sensors, and the wires between."""
    c, sn = math.cos(a), math.sin(a)
    P = lambda u, v: (x + (u * c - v * sn) * scale, y + (u * sn + v * c) * scale)
    body = [P(-12, -9), P(10, -9), P(10, 9), P(-12, 9)]
    s.path(body, col, FINE, close=True, fill=PAPER)
    for v in (-11, 11):   # wheels
        s.path([P(-12, v - 2), P(-4, v - 2), P(-4, v + 2), P(-12, v + 2)], col, FINE, close=True, fill=col)
    for v in (-6, 6):   # sensors
        s.circle(*P(13, v), 2.4 * scale, col, FINE, fill=PAPER)
    for v in (-6, 6):   # wires: sensor to the motor on the same side, or crossed
        tv = -v if crossed else v
        s.path([P(11, v), P(-8, tv * 1.4)], COBALT if inhibitory else col, HAIR, dash="2 1.5" if inhibitory else None)


def simulate(x, y, a, kind, lx, ly, steps=420):
    pts = []
    for _ in range(steps):
        def light(px, py):
            return 1 / (1 + ((px - lx) ** 2 + (py - ly) ** 2) / 9000)
        sl = light(x + math.cos(a - .5) * 12, y + math.sin(a - .5) * 12)
        sr = light(x + math.cos(a + .5) * 12, y + math.sin(a + .5) * 12)
        if kind == "2a":
            vl, vr = sl, sr
        elif kind == "2b":
            vl, vr = sr, sl
        else:   # 3a: inhibitory, uncrossed
            vl, vr = max(0, 1 - 1.4 * sl), max(0, 1 - 1.4 * sr)
        v = (vl + vr) / 2 * 3.2 + (0 if kind == "3a" else .5)
        a += (vl - vr) * .9
        x += math.cos(a) * v; y += math.sin(a) * v
        pts.append((x, y))
        if kind == "3a" and v < .08:
            break
    return pts, a


def braitenberg(w, h, seed, label=None):
    s = Sheet(w, h, "Three Braitenberg vehicles around a light: one turns away, one charges it, one comes to rest facing it")
    lx, ly = w * .5, h * .46
    for k in range(10):   # the light
        ang = k / 10 * math.tau
        s.line(lx + math.cos(ang) * 10, ly + math.sin(ang) * 10, lx + math.cos(ang) * 17, ly + math.sin(ang) * 17, INK, HAIR)
    s.circle(lx, ly, 7, INK, FINE, fill=PAPER); s.dot(lx, ly, 2.5, COBALT)
    for k in (1, 2, 3):
        s.circle(lx, ly, k * h * .14, FAINT, HAIR, dash="1 3")
    small = h <= STRIP
    sc = .9 if small else 1.5
    specs = [("2a", w * .2, h * .3, .25, False, False, "2a · FEAR", "same-side wires, excitatory"),
             ("2b", w * .28, h * .8, -.55, True, False, "2b · AGGRESSION", "crossed wires, excitatory"),
             ("3a", w * .82, h * .2, 2.6, False, True, "3a · LOVE", "same-side wires, inhibitory")]
    if small:
        specs = specs[:2] + [("3a", w * .8, h * .3, 2.7, False, True, "3a · LOVE", "")]
    for kind, x, y, a, crossed, inhib, name, wiring in specs:
        pts, a_end = simulate(x, y, a, kind, lx, ly, 260 if small else 420)
        pts = [(px, py) for px, py in pts if 8 < px < w - 8 and 8 < py < h - 24]
        s.path([(x, y)] + pts, COBALT if kind == "2b" else INK, HAIR, dash="4 3")
        vehicle(s, x, y, a, sc, crossed, inhib)
        if pts:
            ex, ey = pts[-1]
            s.dot(ex, ey, 1.6, INK)
        if not small:
            s.text(x - 46, y - 36, name, 8.5, INK, weight=500, spacing=1)
            s.text(x - 46, y - 26, wiring.upper(), 7, MUTED, spacing=.6)
    if not small:
        s.callout(lx, ly, 1, lx + 70, ly - 60, INK, "LIGHT SOURCE")
    return finish(s, 9, "Braitenberg vehicles", label)


# --- activities: what we do, in three panels ----------------------------------------------------------
def activities(w, h, seed, labels=True):
    r = random.Random(seed)
    s = Sheet(w, h, "Three panels: readers around one document; a path through blocks of data; a lens over a flock")
    pw = w / 3
    # 1. sessions: one document, readers around it with lines of sight
    cx, cy = pw * .5, h * .45
    s.rect(cx - 30, cy - 40, 60, 80, INK, FINE, fill=PAPER)
    s.path([(cx + 18, cy - 40), (cx + 30, cy - 28)], INK, HAIR)
    for k in range(7):
        s.line(cx - 20, cy - 26 + k * 10, cx + 20 - (14 if k == 6 else r.random() * 8), cy - 26 + k * 10, COBALT if k == 2 else FAINT, FINE if k == 2 else HAIR)
    for k in range(9):
        ang = -math.pi * .9 + k / 8 * math.pi * 1.8 + math.pi / 2 * 0
        rx, ry = cx + math.cos(ang) * 92, cy + math.sin(ang) * 66
        s.construction(rx, ry, cx + math.cos(ang) * 32, cy + math.sin(ang) * 40)
        s.circle(rx, ry, 5, INK, FINE, fill=PAPER); s.dot(rx, ry, 1.3, INK)
    # 2. research: blocks of data and the path an agent takes through them
    x0 = pw
    hatch = s.hatch(3, 45, COBALT, .45)
    py = lambda x: h * .45 + math.sin((x - x0) / pw * math.tau * 1.1 + 1) * h * .18
    for i in range(int((pw - 60) / 24)):
        for j in range(int((h - 80) / 24)):
            bx, by = x0 + 30 + i * 24, 34 + j * 24
            hit = abs(by + 8 - py(bx + 8)) < 16
            s.rect(bx, by, 16, 16, COBALT if hit else FAINT, FINE if hit else HAIR, fill=hatch if hit else "none")
    s.path([(x0 + 24 + k * 4, py(x0 + 24 + k * 4)) for k in range(int((pw - 48) / 4))], INK, FINE)
    s.arrow(x0 + pw - 26, py(x0 + pw - 26), 0, 6, INK)
    # 3. training: a lens over a flock, and inside it the pattern is clear
    x0 = 2 * pw; lx, ly, lr = x0 + pw * .55, h * .44, 54
    for _ in range(520):
        t = r.random(); x = x0 + 24 + t * (pw - 48); y = h * .45 + math.sin(t * 5 + 2) * h * .15 + r.gauss(0, 16 * (1 + math.sin(t * math.pi)))
        head = math.atan2(math.cos(t * 5 + 2) * h * .15 * 5 / (pw - 48), 1) + r.gauss(0, .2)
        inside = math.hypot(x - lx, y - ly) < lr - 3
        L = 3.4 if inside else 2.4
        s.line(x, y, x + math.cos(head) * L, y + math.sin(head) * L, COBALT if inside else INK, .8 if inside else .6, op=1 if inside else .55)
    s.circle(lx, ly, lr, INK, MEDIUM); s.circle(lx, ly, lr + 4, INK, HAIR)
    s.line(lx + lr * .72, ly + lr * .72, lx + lr * .72 + 30, ly + lr * .72 + 30, INK, 4)
    s.centerline(lx - lr - 10, ly, lx + lr + 10, ly); s.centerline(lx, ly - lr - 10, lx, ly + lr + 10)
    if labels:
        for i, t in enumerate(("SESSIONS", "RESEARCH", "TRAINING")):
            s.text(pw * i + pw / 2, h - 10, t, 9, INK, "middle", 500, 1.5)
        for i in (1, 2):
            s.line(pw * i, 16, pw * i, h - 30, FAINT, HAIR, "2 4")
    return s.svg()


def activity_panels(seed):
    full = activities(1200, 300, seed, labels=False)
    head, body = full[:full.index(">") + 1], full[full.index(">") + 1:]
    names = [("sessions", "Readers around one document"), ("research", "A path through blocks of data"), ("training", "A lens over a flock, making its pattern clear")]
    defs = body[:body.index("</defs>") + 7] if body.startswith("<defs>") else ""
    rest = body[len(defs):]
    for i, (name, label) in enumerate(names):
        (OUT / f"act-{name}.svg").write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{i * 400 + 20} 10 360 270" width="360" height="270" role="img" aria-label="{label}">{defs}{rest}\n')


# --- cycle: See, Design, Evolve ----------------------------------------------------------------------
def cycle(w, h, seed, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "A loop of three phases: See, then Design, then Evolve, and back to See")
    cx, cy, R = w / 2, h / 2 + 4, min(w, h) * .3
    angs = [-math.pi / 2, math.pi / 6, 5 * math.pi / 6]
    pts = [(cx + R * math.cos(a), cy + R * math.sin(a)) for a in angs]
    s.circle(cx, cy, R, FAINT, HAIR, dash="1 3")
    s.centerline(cx - R - 30, cy, cx + R + 30, cy); s.centerline(cx, cy - R - 30, cx, cy + R + 30)
    for i in range(3):
        a0, a1 = angs[i] + .4, angs[(i + 1) % 3] - .4 + (math.tau if i == 2 else 0)
        arc = [(cx + R * math.cos(a0 + (a1 - a0) * k / 30), cy + R * math.sin(a0 + (a1 - a0) * k / 30)) for k in range(31)]
        s.path(arc, INK, FINE)
        (x1, y1), (x2, y2) = arc[-2], arc[-1]
        s.arrow(x2, y2, math.atan2(y2 - y1, x2 - x1), 7, INK)
    (sx, sy), (dx, dy), (vx, vy) = pts
    for k in (1, 2, 3):
        s.circle(sx, sy, 7 + k * 8, COBALT if k == 1 else INK, HAIR, dash=None if k < 3 else "2 2")
    s.rect(sx - 3.5, sy - 3.5, 7, 7, INK, FINE, fill=INK)
    hatch = s.hatch(3, 45, INK, .45)
    hexp = lambda rad: [(dx + rad * math.cos(i * math.pi / 3), dy + rad * math.sin(i * math.pi / 3)) for i in range(6)]
    s.path(hexp(26), INK, MEDIUM, close=True); s.path(hexp(15), INK, HAIR, close=True, fill=hatch)
    pulse = [(vx - 40, vy), (vx - 12, vy), (vx - 7, vy - 22), (vx, vy + 15), (vx + 5, vy - 5), (vx + 10, vy), (vx + 40, vy)]
    s.path(pulse, INK, FINE); s.dot(vx + 40, vy, 2.5, COBALT)
    for (x, y), name, q, dyy in (((sx, sy), "SEE", "WHAT ACTUALLY HAPPENS", -46), ((dx, dy), "DESIGN", "WHAT MUST BE STRICT", 52), ((vx, vy), "EVOLVE", "WHAT SHOULD CHANGE", 52)):
        s.text(x, y + dyy, name, 12, INK, "middle", 600, 2)
        s.text(x, y + dyy + 14, q, 7.5, MUTED, "middle", spacing=1)
    return finish(s, 10, "See · Design · Evolve", label)


# --- rings: the hardness map in plan, the core cut and hatched ---------------------------------------
def rings(w, h, seed, label=None):
    r = random.Random(seed)
    s = Sheet(w, h, "The hardness map in plan: a hatched hard core, a ring of soft norms, free work outside")
    cx, cy = w / 2, h / 2 - 6
    hatch = s.hatch(4, 45, INK, .35)
    bands = ((h * .44, h * .44 * 2.1, FAINT, HAIR, "2 4", "none"), (h * .33, h * .33 * 1.95, INK, FINE, None, "none"), (h * .2, h * .2 * 2.5, INK, HEAVY, None, PAPER))
    for ry, rx, col, sw, dash, fill in bands:
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        s.out.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" stroke="{col}" stroke-width="{sw}" fill="{fill}"{ds}/>')
    s.out.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{h * .2 * 2.5 - 6:.1f}" ry="{h * .2 - 6:.1f}" stroke="none" fill="{hatch}" opacity=".35"/>')
    s.centerline(cx - h * .44 * 2.1 - 16, cy, cx + h * .44 * 2.1 + 16, cy)
    s.centerline(cx, cy - h * .44 - 10, cx, cy + h * .44 + 10)
    for _ in range(80):
        a = r.random() * math.tau; k = .37 + r.random() * .06
        s.dot(cx + math.cos(a) * h * k * 2.05, cy + math.sin(a) * h * k, 1.3, INK, .6)
    s.text(cx, cy - h * .09, "HARD CORE", 10, COBALT, "middle", 600, 2)
    for (x, y, t) in ((-h * .27, -h * .005, "WHO MAY MOVE MONEY"), (h * .27, -h * .005, "WHAT DATA LEAVES"),
                      (-h * .27, h * .06, "CHECKS ON EVERY OUTPUT"), (h * .27, h * .06, "THE SHARED FIELD LOG")):
        s.text(cx + x, cy + y, t, 7.5, INK, "middle", spacing=.8)
    s.text(cx, cy - h * .265, "SOFT · WEEKLY PLANNING", 8, MUTED, "middle", 500, 1)
    s.text(cx, cy + h * .4, "FREE · HOW EACH TEAM OR AGENT DOES ITS OWN WORK", 8, MUTED, "middle", 500, 1)
    s.dim(cx + h * .2 * 2.5, cy, cx + h * .33 * 1.95, cy, "SOFT", -h * .14)
    s.dim(cx + h * .33 * 1.95, cy, cx + h * .44 * 2.1, cy, "FREE", -h * .14)
    return finish(s, 11, "Hardness map", label)


# --- blyg figures: process vs protocol --------------------------------------------------------------
def process_protocol(w, h, seed, label=None):
    """Left: a swimlane, every step and handoff drawn. Right: three free areas joined by hard interfaces."""
    r = random.Random(seed)
    s = Sheet(w, h, "Left, a process swimlane where every step and handoff is specified. Right, three teams "
                    "working freely inside their own areas, joined by three hard interfaces.")
    mid = w / 2
    s.centerline(mid, 18, mid, h - 30)
    # left: the process
    s.text(24, 32, "PROCESS", 10, INK, weight=600, spacing=1.6)
    s.text(24, 46, "every step and handoff specified", 9, MUTED, spacing=.2)
    top, lane = 60, 80
    for i in range(4):
        s.line(24, top + i * lane, mid - 14, top + i * lane, INK if i in (0, 3) else FAINT, HAIR)
    for i, name in enumerate(("SALES", "OPS", "FINANCE")):
        s.text(28, top + i * lane + 14, name, 7.5, MUTED, spacing=1)
    bw, bh = 34, 22
    steps = [(98, 0), (142, 1), (188, 1, "d"), (234, 2), (280, 1), (322, 0)]
    pts = []
    for n, st in enumerate(steps, 1):
        x, ln = st[0], st[1]
        y = top + ln * lane + lane / 2 + 6
        if len(st) == 3:
            s.path([(x, y - 15), (x + 17, y), (x, y + 15), (x - 17, y)], INK, FINE, close=True, fill=PAPER)
            s.text(x, y + 3, "?", 9, INK, "middle", 600, 0)
            pts.append((x, y, 17))
        else:
            s.rect(x - bw / 2, y - bh / 2, bw, bh, INK, FINE, fill=PAPER)
            s.text(x, y + 3, f"{n:02d}", 8, INK, "middle", 500, .4)
            pts.append((x, y, bw / 2))
    for (x1, y1, r1), (x2, y2, r2) in zip(pts, pts[1:]):   # orthogonal connectors with arrowheads
        xm = (x1 + r1 + x2 - r2) / 2
        s.path([(x1 + r1, y1), (xm, y1), (xm, y2), (x2 - r2, y2)], INK, HAIR)
        s.arrow(x2 - r2, y2, 0, 4.5, INK, HAIR)
    (dx, dy, dr), (bx2, by2, _) = pts[2], pts[1]   # rework loop from the decision back to step 02
    s.path([(dx, dy - 15), (dx, dy - 28), (bx2, dy - 28), (bx2, by2 - bh / 2)], MUTED, HAIR, dash="3 3")
    s.arrow(bx2, by2 - bh / 2, math.pi / 2, 4.5, MUTED, HAIR)
    s.text((dx + bx2) / 2, dy - 32, "REWORK", 6.5, MUTED, "middle", spacing=1)
    s.dim(pts[0][0] - bw / 2, top + 3 * lane, pts[-1][0] + bw / 2, top + 3 * lane, "6 STEPS · 5 HANDOFFS · 1 LOOP", 16)
    # right: the protocol
    x0 = mid + 16
    s.text(x0, 32, "PROTOCOL", 10, COBALT, weight=600, spacing=1.6)
    s.text(x0, 46, "hard at the seams, free inside", 9, MUTED, spacing=.2)
    areas = [(x0 + 4, 64, 132, 100, "TEAM A"), (w - 28 - 132, 64, 132, 100, "TEAM B"), ((x0 + w - 28) / 2 - 66, 206, 132, 96, "AGENTS")]
    for ax, ay, aw, ah, name in areas:
        s.rect(ax, ay, aw, ah, FAINT, HAIR, dash="2 3")
        s.text(ax + 6, ay + 12, name, 7, MUTED, spacing=1)
        for _ in range(4):   # free work: wandering hairlines, each ending at a person or agent
            px, py = r.uniform(ax + 16, ax + aw - 16), r.uniform(ay + 22, ay + ah - 12)
            path = [(px, py)]
            a = r.random() * math.tau
            for _ in range(9):
                a += r.uniform(-1, 1)
                px = min(max(px + math.cos(a) * 9, ax + 8), ax + aw - 8)
                py = min(max(py + math.sin(a) * 9, ay + 18), ay + ah - 6)
                path.append((px, py))
            s.path(path, INK, HAIR, op=.55)
            s.dot(px, py, 1.6, INK)
    (a1x, a1y, a1w, a1h, _), (b1x, b1y, b1w, b1h, _), (c1x, c1y, c1w, c1h, _) = areas
    hatch = s.hatch(3, 45, INK, .5)
    seams = [((a1x + a1w + b1x) / 2, a1y + a1h / 2, 1), ((a1x + a1w / 2 + c1x + 20) / 2, (a1y + a1h + c1y) / 2, 2),
             ((b1x + b1w / 2 + c1x + c1w - 20) / 2, (b1y + b1h + c1y) / 2, 3)]
    joins = [((a1x + a1w, a1y + a1h / 2), (b1x, b1y + b1h / 2)), ((a1x + a1w / 2, a1y + a1h), (c1x + 20, c1y)),
             ((b1x + b1w / 2, b1y + b1h), (c1x + c1w - 20, c1y))]
    for (sx, sy, n), (pa, pb) in zip(seams, joins):
        s.line(pa[0], pa[1], pb[0], pb[1], INK, FINE)
        s.rect(sx - 9, sy - 9, 18, 18, INK, HEAVY, fill=hatch)
        s.callout(sx + 9, sy - 9, n, sx + 22, sy - 20, COBALT)
    for i, t in enumerate(("WHO MAY MOVE MONEY", "WHAT DATA LEAVES", "CHECKS ON EVERY OUTPUT")):
        y = 334 + i * 14
        s.circle(x0 + 8, y - 3, 5.5, COBALT, FINE, fill=PAPER)
        s.text(x0 + 8, y, str(i + 1), 7, COBALT, "middle", 500, 0)
        s.text(x0 + 20, y, t, 7.5, INK, spacing=.8)
    s.text(24, 352, "Owners approve each step.", 9, MUTED, spacing=.2)
    s.text(24, 366, "Change means redrawing the map.", 9, MUTED, spacing=.2)
    return finish(s, 31, "Process and protocol", label)


def steps_rules(w, h, seed, label=None):
    """What you have to specify as the number of agents grows: steps climb, hard rules stay flat."""
    s = Sheet(w, h, "A chart sketch: as agents grow from one to a hundred thousand, the steps a process must "
                    "specify climb past what any manager can approve, while the protocol's hard rules stay flat.")
    x0, x1, y0, y1 = 86, w - 40, h - 62, 40
    s.line(x0, y0, x1, y0, INK, FINE); s.line(x0, y0, x0, y1, INK, FINE)
    s.arrow(x1, y0, 0, 6, INK, FINE); s.arrow(x0, y1, -math.pi / 2, 6, INK, FINE)
    for i, t in enumerate(("1", "10", "100", "1K", "10K", "100K")):
        x = x0 + 20 + i * (x1 - x0 - 50) / 5
        s.line(x, y0, x, y0 + 5, INK, HAIR)
        s.construction(x, y0, x, y1 + 10)
        s.text(x, y0 + 17, t, 8, MUTED, "middle")
    s.text((x0 + x1) / 2, y0 + 34, "AGENTS AT WORK", 8, INK, "middle", 500, 1.2)
    s.out.append(f'<text x="34" y="{(y0 + y1) / 2:.1f}" font-family="{MONO}" font-size="8" font-weight="500" letter-spacing="1.2" '
                 f'fill="{INK}" text-anchor="middle" stroke="none" transform="rotate(-90 34 {(y0 + y1) / 2:.1f})">TO SPECIFY</text>')
    span = x1 - x0 - 50
    steps = [(x0 + 20 + t * span, y0 - 14 - (y0 - y1 - 20) * (math.exp(3.2 * t) - 1) / (math.exp(3.2) - 1)) for t in [i / 60 for i in range(61)]]
    s.path(steps, INK, MEDIUM)
    rules = [(x0 + 20 + t * span, y0 - 30 - 6 * t) for t in [i / 10 for i in range(11)]]
    s.path(rules, COBALT, MEDIUM)
    cap = y0 - (y0 - y1) * .42
    s.line(x0, cap, x1 - 10, cap, MUTED, HAIR, "6 4")
    s.text(x0 + 8, cap - 6, "WHAT ANY MANAGER CAN APPROVE", 7.5, MUTED, spacing=1)
    cross = min(steps, key=lambda p: abs(p[1] - cap))
    s.circle(cross[0], cross[1], 5, INK, FINE)
    s.callout(cross[0], cross[1], 1, cross[0] - 70, cross[1] - 44, INK, "THE APPROVAL QUEUE BREAKS")
    end = steps[-1]
    s.text(end[0] - 8, end[1] + 4, "PROCESS · STEPS", 8, INK, "end", 600, 1)
    s.text(rules[-1][0], rules[-1][1] - 9, "PROTOCOL · HARD RULES", 8, COBALT, "end", 600, 1)
    return finish(s, 32, "Steps and rules", label)


BLYG_FIGS = {   # drawn into blyg-src/media/ (committed with the post that uses them)
    "process-protocol": (process_protocol, 720, 400, 31),
    "steps-rules": (steps_rules, 720, 300, 32),
}


FIGS = {
    "murmuration": (murmuration, 1200, 300, 7),
    "network": (network, 1200, 260, 11),
    "faults": (faults, 1200, 260, 5),
    "hardcore": (hardcore, 1200, 320, 3),
    "emissions": (emissions, 1200, 280, 2),
    "heartbeat": (heartbeat, 1200, 200, 4),
    "ledger": (ledger, 1200, 210, 9),
    "quorum": (quorum, 1200, 240, 8),
    "gather": (gather, 480, 200, 12),
    "activities": (activities, 1200, 300, 13),
    "cycle": (cycle, 900, 360, 14),
    "rings": (rings, 1000, 360, 15),
    "braitenberg": (braitenberg, 1200, 320, 16),
    "advisory": (advisory, 560, 260, 17),
}
STRIPS = {   # one strip per theme, in the order of the year
    "theme-1": (braitenberg, 21, "THEME I · AGENTS"), "theme-2": (murmuration, 22, "THEME II · NATURE"),
    "theme-3": (emissions, 23, "THEME III · EMISSIONS"), "theme-4": (faults, 24, "THEME IV · INCIDENTS"),
    "theme-5": (hardcore, 25, "THEME V · HARDNESS"), "theme-6": (heartbeat, 26, "THEME VI · LIVENESS"),
}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (fn, w, h, seed) in FIGS.items():
        (OUT / f"{name}.svg").write_text(fn(w, h, seed))
    for name, (fn, seed, lab) in STRIPS.items():
        (OUT / f"{name}.svg").write_text(fn(640, 120, seed, label=lab))
    activity_panels(13)
    media = OUT.parent.parent / "blyg-src/media"
    media.mkdir(exist_ok=True)
    for name, (fn, w, h, seed) in BLYG_FIGS.items():
        (media / f"{name}.svg").write_text(fn(w, h, seed))
    print(f"{len(FIGS) + len(STRIPS) + 3} figures in {OUT}")
