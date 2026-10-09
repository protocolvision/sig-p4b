// The approval-queue figure for slide 05, from the protocolvision.org tangle study (directions/tangle/tangle.js),
// with larger labels for slides. Only the "scale" figure is used here.
// The tangle study: the landing page's figures redrawn as live canvas drawings.
// Protocols are strands of a knot diagram (real over/under crossings, recomputed every frame from a 3-D curve),
// agents are ooze (metaballs: they merge, pinch off and flow around whatever is in the way), the hard core is
// Bidwell's packing of 17 squares, and unplanned options grow as a slime mould. One frame for reduced motion.
"use strict";
(() => {
const C = { paper: "#f9f8f5", ink: "#2c2c2a", ink2: "#5f5e5a", faint: "#b3b0a8", hair: "#d9d6cf", hard: "#0f6e56" };
const MONO = '"JetBrains Mono", ui-monospace, Menlo, monospace';
const TAU = Math.PI * 2;
const REDUCE = matchMedia("(prefers-reduced-motion: reduce)");
const PHONE = matchMedia("(max-width:560px)");
const rng = (seed) => () => ((seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0) / 4294967296);
const lerp = (a, b, t) => a + (b - a) * t, clamp = (x, a, b) => Math.max(a, Math.min(b, x));
const ease = (t) => (t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
const smooth = (a, b, x) => { const t = clamp((x - a) / (b - a), 0, 1); return t * t * (3 - 2 * t); };
const layer = () => document.createElement("canvas");
const hex = (h) => [1, 3, 5].map((i) => parseInt(h.slice(i, i + 2), 16));

// ---- drawing kit --------------------------------------------------------------------------------
function text(g, x, y, s, size, col = C.ink, align = "left", weight = 400, ls = 0) {
  g.font = `${weight} ${size}px ${MONO}`; g.fillStyle = col; g.textAlign = align; g.textBaseline = "alphabetic";
  if ("letterSpacing" in g) g.letterSpacing = `${ls}px`;
  g.fillText(s, x, y);
  if ("letterSpacing" in g) g.letterSpacing = "0px";
}
function line(g, pts, col, w, dash) {
  g.beginPath(); pts.forEach(([x, y], i) => (i ? g.lineTo(x, y) : g.moveTo(x, y)));
  g.strokeStyle = col; g.lineWidth = w; g.setLineDash(dash || []); g.stroke(); g.setLineDash([]);
}
function box(g, x, y, w, h, label, size) {
  g.fillStyle = C.paper; g.fillRect(x, y, w, h);
  g.strokeStyle = C.faint; g.lineWidth = .5; g.strokeRect(x, y, w, h);
  text(g, x + w / 2, y + h / 2 + 3, label, size, C.ink2, "center");
}
function arrow(g, x, y, ang, len, col, w) {
  line(g, [[x - len * Math.cos(ang - .45), y - len * Math.sin(ang - .45)], [x, y], [x - len * Math.cos(ang + .45), y - len * Math.sin(ang + .45)]], col, w);
}
function numbered(g, x, y, n, col, size) {
  g.beginPath(); g.arc(x, y, size * .95, 0, TAU); g.fillStyle = C.paper; g.fill(); g.strokeStyle = col; g.lineWidth = .8; g.stroke();
  text(g, x, y + size * .36, String(n), size, col, "center", 500);
}
let hatchCache = null;
function hatch(g, col) {   // diagonal hatching in screen space, like the drafting kit's
  if (!hatchCache) {
    const c = layer(); c.width = c.height = 8; const h = c.getContext("2d");
    h.strokeStyle = col; h.lineWidth = .9; h.globalAlpha = .7;
    h.beginPath(); h.moveTo(-2, 10); h.lineTo(10, -2); h.moveTo(-2, 2); h.lineTo(2, -2); h.moveTo(6, 10); h.lineTo(10, 6); h.stroke();
    hatchCache = c;
  }
  return g.createPattern(hatchCache, "repeat");
}

// ---- knot diagrams ------------------------------------------------------------------------------
// A strand is a curve f(u, t) -> [x, y, z], u in [0, 1). Where two pieces cross in the drawing, the one with the
// larger z goes over, so every frame is a valid diagram of a real (moving) link.
let seeds = 1;
function strand(f, n, closed, style) {
  return { f, n, closed, style, pts: new Float32Array(n * 3), len: new Float32Array(n), total: 0, seed: (seeds++ * 2.39996) % TAU };
}
function sample(S, t) {
  for (const s of S) {
    for (let i = 0; i < s.n; i++) {
      const p = s.f(s.closed ? i / s.n : i / (s.n - 1), t);
      s.pts[3 * i] = p[0]; s.pts[3 * i + 1] = p[1]; s.pts[3 * i + 2] = p[2];
    }
    // arc length, so a rope's twist stays put along the strand as it moves
    for (let i = 1; i < s.n; i++) s.len[i] = s.len[i - 1] + Math.hypot(s.pts[3 * i] - s.pts[3 * i - 3], s.pts[3 * i + 1] - s.pts[3 * i - 2]);
    s.total = s.len[s.n - 1] + (s.closed ? Math.hypot(s.pts[0] - s.pts[3 * s.n - 3], s.pts[1] - s.pts[3 * s.n - 2]) : 0);
  }
}
function crossings(S, cell = 22) {
  const cells = new Map(), segs = [], out = [];
  S.forEach((s, si) => {
    const m = s.closed ? s.n : s.n - 1;
    for (let i = 0; i < m; i++) {
      const j = (i + 1) % s.n, ax = s.pts[3 * i], ay = s.pts[3 * i + 1], bx = s.pts[3 * j], by = s.pts[3 * j + 1];
      const id = segs.length; segs.push([si, i, ax, ay, bx, by]);
      for (let gx = Math.floor(Math.min(ax, bx) / cell); gx <= Math.floor(Math.max(ax, bx) / cell); gx++)
        for (let gy = Math.floor(Math.min(ay, by) / cell); gy <= Math.floor(Math.max(ay, by) / cell); gy++) {
          const k = (gx + 500) * 4000 + gy + 500; let l = cells.get(k); if (!l) cells.set(k, (l = [])); l.push(id);
        }
    }
  });
  for (const [k, l] of cells) for (let a = 0; a < l.length; a++) for (let b = a + 1; b < l.length; b++) {
    const A = segs[l[a]], B = segs[l[b]];
    if (A[0] === B[0]) {
      const n = S[A[0]].n, d = Math.abs(A[1] - B[1]);
      if (d <= 1 || (S[A[0]].closed && d >= n - 1)) continue;
    }
    const rx = A[4] - A[2], ry = A[5] - A[3], sx = B[4] - B[2], sy = B[5] - B[3], den = rx * sy - ry * sx;
    if (Math.abs(den) < 1e-9) continue;
    const qx = B[2] - A[2], qy = B[3] - A[3], ta = (qx * sy - qy * sx) / den, tb = (qx * ry - qy * rx) / den;
    if (ta < 0 || ta >= 1 || tb < 0 || tb >= 1) continue;
    const x = A[2] + ta * rx, y = A[3] + ta * ry;
    if ((Math.floor(x / cell) + 500) * 4000 + Math.floor(y / cell) + 500 !== k) continue;   // count each crossing once
    const z = (seg, f) => { const s = S[seg[0]], i = seg[1], j = (i + 1) % s.n; return lerp(s.pts[3 * i + 2], s.pts[3 * j + 2], f); };
    const pa = { si: A[0], i: A[1], f: ta, z: z(A, ta) }, pb = { si: B[0], i: B[1], f: tb, z: z(B, tb) };
    out.push(pa.z > pb.z ? { x, y, o: pa, u: pb } : { x, y, o: pb, u: pa });
  }
  return out;
}
// strokes indices i0..i1 of a strand, split into runs that share a style (a strand can be hard in places)
function runs(g, s, i0, i1, forced) {
  const n = s.n, key = (i) => (forced ? forced : s.style((((i % n) + n) % n) / n));
  let st = key(i0), start = i0;
  const flush = (end) => {
    if (end <= start) return;
    if (st.skip) return;
    if (st.crystal) return crystal(g, s, start, end, st);
    if (st.rope) return rope(g, s, start, end, st);
    g.beginPath();
    for (let i = start; i <= end; i++) { const j = ((i % n) + n) % n; i === start ? g.moveTo(s.pts[3 * j], s.pts[3 * j + 1]) : g.lineTo(s.pts[3 * j], s.pts[3 * j + 1]); }
    g.strokeStyle = st.c; g.lineWidth = st.w; g.globalAlpha = st.a ?? 1; g.setLineDash(st.d || []); g.stroke();
    g.setLineDash([]); g.globalAlpha = 1;
  };
  for (let i = i0 + 1; i <= i1; i++) { const k = key(i); if (k !== st) { flush(i); st = k; start = i; } }
  flush(i1);
}
// a strand drawn as rope: a faint body and a few fibres twisted around the centre line, a little uneven.
// Porous strands get dashed fibres, each broken in different places, so they read as loose thread.
function rope(g, s, i0, i1, st) {
  const n = s.n, P = [];
  const pt = (i) => { const j = ((i % n) + n) % n; return [s.pts[3 * j], s.pts[3 * j + 1], s.len[j] + Math.floor(i / n) * s.total]; };
  const nb = (i) => (s.closed ? i : clamp(i, 0, n - 1));
  for (let i = i0; i < i1; i++) {   // subdivide, so the twist is drawn smoothly
    const a = pt(i), b = pt(i + 1), pa = pt(nb(i - 1)), pb = pt(nb(i + 2));
    const k = Math.max(1, Math.ceil(Math.hypot(b[0] - a[0], b[1] - a[1]) / 1.8));
    for (let q = 0; q < k; q++) {
      const f = q / k, x = lerp(a[0], b[0], f), y = lerp(a[1], b[1], f), L = lerp(a[2], b[2], f);
      let tx = lerp(b[0] - pa[0], pb[0] - a[0], f), ty = lerp(b[1] - pa[1], pb[1] - a[1], f); const tl = Math.hypot(tx, ty) || 1;
      P.push([x, y, L, -ty / tl, tx / tl]);
    }
  }
  { const b = pt(i1), a = pt(nb(i1 - 1)), tl = Math.hypot(b[0] - a[0], b[1] - a[1]) || 1; P.push([b[0], b[1], b[2], -(b[1] - a[1]) / tl, (b[0] - a[0]) / tl]); }
  if (P.length < 2) return;
  const fray = st.fray ?? .5, rw = st.rw, pitch = st.pitch || 9, nf = st.rope, al = st.a ?? 1;
  const off = (L) => fray * (Math.sin(L * .19 + s.seed) + .6 * Math.sin(L * .47 + 2 * s.seed));
  const path = (o) => { g.beginPath(); P.forEach(([x, y, L, nx, ny], i) => { const d = o(L); i ? g.lineTo(x + nx * d, y + ny * d) : g.moveTo(x + nx * d, y + ny * d); }); };
  g.strokeStyle = st.c; g.lineCap = "round"; g.lineJoin = "round";
  path(off); g.lineWidth = 2 * rw + st.w; g.globalAlpha = al * (st.body ?? .12); g.stroke();
  g.globalAlpha = al; g.lineWidth = st.w;
  for (let f = 0; f < nf; f++) {
    path((L) => off(L) + rw * Math.sin(TAU * L / pitch + f * TAU / nf) * (1 + .15 * Math.sin(L * .31 + f)));
    if (st.d) { g.setLineDash(st.d); g.lineDashOffset = f * 3.7 + s.seed * 5; }
    g.stroke(); g.setLineDash([]);
  }
  g.globalAlpha = 1; g.lineCap = "butt"; g.lineJoin = "miter";
}
// Hard protocols are crystal, not rope: a chain of straight faceted rods along the path, each with a lit facet and a ridge.
// Rods sit at fixed arc lengths along the strand, so a redraw over a crossing lands exactly on the same rods.
const crystalSt = (hw = 2.5, L = 11, extra = {}) => ({ c: C.hard, crystal: true, hw, L, w: .8, ...extra });
function posAtLen(s, Lq) {
  const n = s.n, Lm = s.closed ? ((Lq % s.total) + s.total) % s.total : clamp(Lq, 0, s.len[n - 1]);
  let lo = 0, hi = n - 1; while (lo < hi) { const mid = (lo + hi + 1) >> 1; if (s.len[mid] <= Lm) lo = mid; else hi = mid - 1; }
  const i = lo, j = (i + 1) % n, segL = (i === n - 1 ? s.total : s.len[j]) - s.len[i];
  if (!s.closed && i === n - 1) return [s.pts[3 * i], s.pts[3 * i + 1]];
  const f = segL > 0 ? (Lm - s.len[i]) / segL : 0;
  return [lerp(s.pts[3 * i], s.pts[3 * j], f), lerp(s.pts[3 * i + 1], s.pts[3 * j + 1], f)];
}
function crystal(g, s, i0, i1, st) {
  const n = s.n, Lat = (i) => s.len[((i % n) + n) % n] + Math.floor(i / n) * s.total;
  const L0 = Lat(i0), L1 = Lat(i1), L = st.L, gp = .7, [r, gg, b] = hex(st.c), al = st.a ?? 1;
  const end = s.closed ? Infinity : s.len[n - 1];
  for (let k = Math.floor(L0 / L); k * L < L1; k++) {
    const a = Math.max(0, k * L + gp), e = Math.min(end, (k + 1) * L - gp); if (e - a < 1.5) continue;
    const A = posAtLen(s, a), B = posAtLen(s, e), dx = B[0] - A[0], dy = B[1] - A[1], d = Math.hypot(dx, dy) || 1;
    const tx = dx / d, ty = dy / d, nx = -ty, ny = tx, hw = st.hw * (.8 + .4 * (Math.sin(k * 12.9898 + s.seed * 7) * .5 + .5)), tip = Math.min(st.hw * .9, d * .3);
    const P = [A, [A[0] + tx * tip + nx * hw, A[1] + ty * tip + ny * hw], [B[0] - tx * tip + nx * hw, B[1] - ty * tip + ny * hw], B,
      [B[0] - tx * tip - nx * hw, B[1] - ty * tip - ny * hw], [A[0] + tx * tip - nx * hw, A[1] + ty * tip - ny * hw]];
    const poly = (pts) => { g.beginPath(); pts.forEach(([x, y], i) => (i ? g.lineTo(x, y) : g.moveTo(x, y))); g.closePath(); };
    g.globalAlpha = al;
    poly(P); g.fillStyle = `rgba(${r},${gg},${b},.14)`; g.fill();
    poly(P.slice(0, 4)); g.fillStyle = `rgba(${r},${gg},${b},.38)`; g.fill();   // the lit facet
    poly(P); g.strokeStyle = st.c; g.lineWidth = st.w; g.lineJoin = "miter"; g.stroke();
    g.beginPath(); g.moveTo(A[0], A[1]); g.lineTo(B[0], B[1]); g.lineWidth = st.w * .6; g.stroke();   // the ridge
  }
  g.globalAlpha = 1;
}
function pathLine(g, pts, st) {   // a polyline drawn in a strand style (keys, rails, guardrails)
  const L = [0]; for (let i = 1; i < pts.length; i++) L.push(L[i - 1] + Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]));
  const tot = L[L.length - 1] || 1;
  const tmp = strand((u) => { const d = u * tot; let i = 1; while (i < L.length - 1 && L[i] < d) i++; const f = (d - L[i - 1]) / ((L[i] - L[i - 1]) || 1); return [lerp(pts[i - 1][0], pts[i][0], f), lerp(pts[i - 1][1], pts[i][1], f), 0]; },
    Math.max(8, Math.ceil(tot / 2)), false, () => st);
  sample([tmp], 0); runs(g, tmp, 0, tmp.n - 1);
}
function haloText(g, x, y, s, size, col, align, weight) {   // a label that stays legible over lines
  g.font = `${weight || 400} ${size}px ${MONO}`; g.textAlign = align || "left"; g.lineWidth = 3.5; g.strokeStyle = C.paper; g.lineJoin = "round"; g.strokeText(s, x, y);
  text(g, x, y, s, size, col, align, weight);
}
function ropeLine(g, x0, x1, y, st) {   // a short sample of a style, for keys
  const tmp = strand((u) => [lerp(x0, x1, u), y, 0], 24, false, () => st); sample([tmp], 0); runs(g, tmp, 0, 23);
}
// the whole diagram: every strand, then each crossing's over-piece is cut free (a gap in the under strand) and redrawn
function diagram(g, S, X, opt = {}) {
  const gap = opt.gap ?? 3.2, reach = opt.reach ?? 9;
  for (const s of S) runs(g, s, 0, s.closed ? s.n : s.n - 1, opt.forced);
  for (const c of X) {
    const s = S[c.o.si], n = s.n;
    let a = c.o.i, b = c.o.i + 1, la = 0, lb = 0;
    const seg = (i) => { const j = ((i % n) + n) % n, k = (((i + 1) % n) + n) % n; return Math.hypot(s.pts[3 * k] - s.pts[3 * j], s.pts[3 * k + 1] - s.pts[3 * j + 1]); };
    while (la < reach && (s.closed || a > 0)) { a--; la += seg(a); }
    while (lb < reach && (s.closed || b < n - 1)) { lb += seg(b); b++; }
    const st = opt.forced || s.style((((c.o.i % n) + n) % n) / n);
    g.globalCompositeOperation = "destination-out";
    if (!st.skip) runs(g, s, a, b, { c: "#000", w: (st.crystal ? 2 * st.hw : st.rope ? 2 * st.rw + st.w : st.w) + 2 * gap });
    g.globalCompositeOperation = "source-over";
    runs(g, s, a, b, opt.forced);
  }
}
function at(s, u) {   // a point on a sampled strand
  const n = s.n, x = (s.closed ? ((u % 1) + 1) % 1 : clamp(u, 0, 1)) * (s.closed ? n : n - 1);
  const i = Math.floor(x), f = x - i, j = s.closed ? (i + 1) % n : Math.min(i + 1, n - 1), i2 = Math.min(i, n - 1);
  return [lerp(s.pts[3 * i2], s.pts[3 * j], f), lerp(s.pts[3 * i2 + 1], s.pts[3 * j + 1], f)];
}
// a torus knot (p, q) drifting in place: the projection of a curve wound p times around and q times through a ring
function torus(o) {
  return (u, t) => {
    const th = TAU * u, ph = o.q * th + o.ph + t * o.w2, r = o.R + o.A * Math.cos(ph), a = o.p * th + o.rot + t * o.w;
    const ws = o.ws ?? 1, x = r * Math.cos(a) * o.ex + o.wob * Math.sin(3 * th + t * .37 * ws + o.ph), y = r * Math.sin(a) * o.ey + o.wob * Math.cos(2 * th - t * .29 * ws);
    return [o.cx + x, o.cy + y, Math.sin(ph) + (o.zo || 0)];
  };
}
// an open strand through waypoints, coiled: a curl travels along it, so it loops over and under itself
function coil(way, a, f, w, zo) {
  const P = way;
  const spline = (u) => {
    const m = P.length - 1, x = clamp(u, 0, .99999) * m, i = Math.floor(x), t = x - i;
    const p0 = P[Math.max(i - 1, 0)], p1 = P[i], p2 = P[i + 1], p3 = P[Math.min(i + 2, m)];
    const cr = (k) => .5 * (2 * p1[k] + (-p0[k] + p2[k]) * t + (2 * p0[k] - 5 * p1[k] + 4 * p2[k] - p3[k]) * t * t + (-p0[k] + 3 * p1[k] - 3 * p2[k] + p3[k]) * t * t * t);
    return [cr(0), cr(1)];
  };
  return (u, t) => {
    const [x, y] = spline(u), env = Math.pow(Math.sin(Math.PI * u), .8), ph = TAU * f * u - w * t;
    return [x + a * env * Math.cos(ph), y + a * env * Math.sin(ph), Math.sin(ph) + .6 * Math.sin(TAU * 2 * u + zo + t * .2)];
  };
}

// ---- ooze -----------------------------------------------------------------------------------------
// Agents as metaballs: a field sum r²/d², filled softly and outlined where it crosses 1.
const MS = [[], [[3, 2]], [[2, 1]], [[3, 1]], [[0, 1]], [[3, 0], [2, 1]], [[0, 2]], [[3, 0]], [[3, 0]], [[0, 2]], [[0, 1], [3, 2]], [[0, 1]], [[3, 1]], [[2, 1]], [[3, 2]], []];
function goo(g, parts, opt) {
  if (!parts.length) return;
  const cell = opt.cell || 4, pad = 18;
  let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
  for (const p of parts) { x0 = Math.min(x0, p.x - p.r * 3); y0 = Math.min(y0, p.y - p.r * 3); x1 = Math.max(x1, p.x + p.r * 3); y1 = Math.max(y1, p.y + p.r * 3); }
  x0 = Math.floor((x0 - pad) / cell) * cell; y0 = Math.floor((y0 - pad) / cell) * cell;
  const nx = Math.ceil((x1 + pad - x0) / cell) + 1, ny = Math.ceil((y1 + pad - y0) / cell) + 1;
  const F = new Float32Array(nx * ny);
  for (const p of parts) {
    const R = p.r * 3.2, r2 = p.r * p.r * (p.w ?? 1);
    const gx0 = Math.max(0, Math.floor((p.x - R - x0) / cell)), gx1 = Math.min(nx - 1, Math.ceil((p.x + R - x0) / cell));
    const gy0 = Math.max(0, Math.floor((p.y - R - y0) / cell)), gy1 = Math.min(ny - 1, Math.ceil((p.y + R - y0) / cell));
    for (let gy = gy0; gy <= gy1; gy++) { const dy = y0 + gy * cell - p.y; for (let gx = gx0; gx <= gx1; gx++) {
      const dx = x0 + gx * cell - p.x, d2 = dx * dx + dy * dy; if (d2 < R * R) F[gy * nx + gx] += r2 / (d2 + 1) * (1 - d2 / (R * R)); } }
  }
  // soft fill: one pixel per grid node, scaled up with smoothing
  const im = opt.cache || (opt.cache = layer());
  if (im.width !== nx || im.height !== ny) { im.width = nx; im.height = ny; }
  const ic = im.getContext("2d"), data = ic.createImageData(nx, ny), [r, gg, b] = hex(opt.fill || C.ink);
  for (let i = 0; i < nx * ny; i++) { const v = smooth(.55, 1.05, F[i]); data.data[4 * i] = r; data.data[4 * i + 1] = gg; data.data[4 * i + 2] = b; data.data[4 * i + 3] = 255 * v * (opt.fa ?? .16) + 255 * smooth(1.6, 4, F[i]) * (opt.core ?? .1); }
  ic.putImageData(data, 0, 0);
  g.imageSmoothingEnabled = true; g.drawImage(im, x0 - cell / 2, y0 - cell / 2, nx * cell, ny * cell);
  if (opt.lw === 0) return;
  // crisp outline: marching squares at the level 1
  const lv = opt.level ?? 1;
  g.beginPath();
  for (let gy = 0; gy < ny - 1; gy++) for (let gx = 0; gx < nx - 1; gx++) {
    const a = F[gy * nx + gx], bq = F[gy * nx + gx + 1], c = F[(gy + 1) * nx + gx + 1], d = F[(gy + 1) * nx + gx];
    const k = (a >= lv) << 3 | (bq >= lv) << 2 | (c >= lv) << 1 | (d >= lv);
    if (!k || k === 15) continue;
    const X = x0 + gx * cell, Y = y0 + gy * cell;
    const e = (i) => i === 0 ? [X + cell * (lv - a) / (bq - a), Y] : i === 1 ? [X + cell, Y + cell * (lv - bq) / (c - bq)]
      : i === 2 ? [X + cell * (lv - d) / (c - d), Y + cell] : [X, Y + cell * (lv - a) / (d - a)];
    for (const [p, q] of MS[k]) { const P = e(p), Q = e(q); g.moveTo(P[0], P[1]); g.lineTo(Q[0], Q[1]); }
  }
  g.strokeStyle = opt.stroke || C.ink; g.lineWidth = opt.lw || .8; g.stroke();
}
// Work in motion: each agent is a packet (a small card with lines of text on it) leaving a faint trail of ooze.
// A forest corner fold marks constraints the agent carries with it.
function packet(g, x, y, a, s, opt = {}) {
  const w = 2.7 * s, h = 1.85 * s, r = .35 * s;
  const ga = g.globalAlpha; g.save(); g.translate(x, y); g.rotate(a); g.globalAlpha = ga * (opt.alpha ?? 1);
  g.beginPath(); g.roundRect ? g.roundRect(-w / 2, -h / 2, w, h, r) : g.rect(-w / 2, -h / 2, w, h);
  g.fillStyle = C.paper; g.fill(); g.strokeStyle = C.ink; g.lineWidth = Math.max(.5, s * .14); g.stroke();
  g.beginPath(); g.moveTo(-w * .32, -h * .12); g.lineTo(w * .26, -h * .12); g.moveTo(-w * .32, h * .18); g.lineTo(w * .06, h * .18);
  g.lineWidth = Math.max(.35, s * .1); g.globalAlpha *= .75; g.stroke();
  if (opt.mark) { g.globalAlpha = ga * (opt.alpha ?? 1); g.beginPath(); g.moveTo(w / 2 - s * .9, -h / 2); g.lineTo(w / 2, -h / 2); g.lineTo(w / 2, -h / 2 + s * .9); g.closePath(); g.fillStyle = C.hard; g.fill(); }
  g.restore();
}
// What the reader sees of an agent is steadied: the simulation can jostle a packet that's stuck against a wall or
// in a crowd, but the drawn packet eases toward it, turns slowly, never flips end over end (a card reads the same
// either way round), and fades in wherever it jumps (a respawn) instead of popping.
function steady(p, want, ease = .22) {
  const first = p.sx == null;
  if (first || Math.hypot(p.x - p.sx, p.y - p.sy) > 24) { p.sx = p.x; p.sy = p.y; p.svx = p.svy = 0; p.a = want ?? p.a ?? 0; p.fade = first ? 1 : 0; }
  const ox = p.sx, oy = p.sy;
  p.sx += (p.x - p.sx) * ease; p.sy += (p.y - p.sy) * ease;
  p.svx = lerp(p.svx, p.sx - ox, .06); p.svy = lerp(p.svy, p.sy - oy, .06);
  p.fade = Math.min(1, (p.fade ?? 1) + .04);
  if (want == null) { if (Math.hypot(p.svx, p.svy) < .05) return; want = Math.atan2(p.svy, p.svx); }
  let d = Math.atan2(Math.sin(want - p.a), Math.cos(want - p.a));
  if (Math.abs(d) > Math.PI / 2) d -= Math.sign(d) * Math.PI;
  p.a += clamp(d, -.04, .04);
}
function flow(g, trails, opt = {}) {   // trails: head first; the trail oozes, the head is the packet
  goo(g, trails.flat(), { cell: opt.cell || 3, fa: opt.fa ?? .1, core: .04, lw: 0, cache: opt.cache });
  for (const T of trails) {
    const p = T[0], q = T[1] || T[0];
    steady(p, Math.hypot(p.x - q.x, p.y - q.y) > .3 ? Math.atan2(p.y - q.y, p.x - q.x) : null, .5);
    const w = (p.w ?? 1) * p.fade; if (w < .02) continue;
    packet(g, p.sx, p.sy, p.a, opt.s || p.r * .8, { alpha: w, mark: opt.mark });
  }
}
function swarm(g, ps, opt = {}) {   // free agents: a packet each, turned the way it's going, over a faint ooze
  goo(g, ps, { cell: opt.cell || 3, fa: opt.fa ?? .08, core: .03, lw: 0, cache: opt.cache });
  for (const p of ps) {
    steady(p, opt.angle ? opt.angle(p) : null);
    const w = (p.w ?? 1) * p.fade; if (w < .02) continue;
    packet(g, p.sx, p.sy, p.a, opt.s || p.r * .75, { alpha: w, mark: opt.mark });
  }
}
// pairwise soft forces that keep a blob of particles together like a liquid
function liquid(ps, near = 7, far = 15, k = 1) {
  for (let i = 0; i < ps.length; i++) for (let j = i + 1; j < ps.length; j++) {
    const a = ps[i], b = ps[j], dx = b.x - a.x, dy = b.y - a.y, d2 = dx * dx + dy * dy;
    if (d2 > far * far || d2 < 1e-6) continue;
    const d = Math.sqrt(d2), f = (d < near ? -(near - d) * .45 : (d - near) * .03) * k / d;
    a.vx += dx * f; a.vy += dy * f; b.vx -= dx * f; b.vy -= dy * f;
  }
}

// ---- stage ---------------------------------------------------------------------------------------
// Fixed-step simulation, drawn every frame, paused off screen. Reduced motion: run to fig.still, draw once.
function mount(canvas, make, opts = {}) {
  const g = canvas.getContext("2d");
  let fig, t = 0, raf = 0, visible = false, last = 0, acc = 0;
  const DT = 1 / 60;
  const draw = () => {
    if (!canvas.width) return;
    const k = canvas.width / fig.W;
    g.setTransform(1, 0, 0, 1, 0, 0); g.clearRect(0, 0, canvas.width, canvas.height);
    g.setTransform(k, 0, 0, k, 0, 0); fig.draw(g, t + acc, k, canvas);
  };
  const size = () => {
    if (!opts.wide && fig._m !== PHONE.matches) return build();   // the layout changed (resize, rotation): redraw in the right shape
    const w = canvas.getBoundingClientRect().width; if (!w) return;
    const dpr = Math.min(devicePixelRatio || 1, fig.maxDpr || 2);
    canvas.width = Math.round(w * dpr); canvas.height = Math.round(w * dpr * fig.H / fig.W); draw();
  };
  const loop = (now) => {
    raf = requestAnimationFrame(loop);
    const dt = last ? Math.min(.1, (now - last) / 1000) : DT; last = now; acc += dt;
    let n = 0; while (acc >= DT && n < 3) { fig.step?.(DT, t); t += DT; acc -= DT; n++; }
    if (n === 3) acc = 0;
    draw();
  };
  const play = () => { if (!raf && visible && !REDUCE.matches) { last = 0; raf = requestAnimationFrame(loop); } };
  const stop = () => { cancelAnimationFrame(raf); raf = 0; };
  const build = () => {
    stop(); const m = opts.wide ? false : PHONE.matches; fig = make(m); fig._m = m; t = 0;
    canvas.style.setProperty("--ar", fig.W / fig.H); canvas.style.aspectRatio = `${fig.W} / ${fig.H}`;
    if (REDUCE.matches) { const end = fig.still ?? 6; while (t < end) { fig.step?.(DT, t); t += DT; } }
    size(); play();
  };
  const ro = new ResizeObserver(size), io = new IntersectionObserver(([e]) => { visible = e.isIntersecting; visible ? play() : stop(); });
  build(); ro.observe(canvas); io.observe(canvas);
  PHONE.addEventListener("change", build); REDUCE.addEventListener("change", build);
  return { destroy() { stop(); ro.disconnect(); io.disconnect(); PHONE.removeEventListener("change", build); REDUCE.removeEventListener("change", build); } };
}

// ==== hero: the tangle, mostly in the blind ===========================================================
// A field of knots larger than the screen, nearly all of it in fog. Focus drifts slowly; inside it the strands are
// sharp, the hard ones (forest) don't move at all, and agents ooze along the rest.
function hero() {
  const W = 1600, H = 1000, rnd = rng(11);
  const soft = { c: C.ink, w: 0.66, rope: 2, rw: 1.5, pitch: 10, fray: 0.45 }, hardS = crystalSt(2.8, 14);
  const PQ = [[2, 3], [3, 4], [2, 5], [3, 5], [2, 7], [3, 2], [4, 3], [5, 3], [3, 7]];
  const K = [];
  for (let k = 0; k < 400 && K.length < 10; k++) {
    const cx = 420 + rnd() * 1240, cy = 40 + rnd() * 920;
    if (K.some((o) => Math.hypot(o.cx - cx, o.cy - cy) < 230)) continue;
    const [p, q] = PQ[Math.floor(rnd() * 4)], R = 100 + rnd() * 90;
    K.push({ p, q, cx, cy, R, A: R * (.45 + rnd() * .25), ex: .85 + rnd() * .3, ey: .85 + rnd() * .3, rot: rnd() * TAU,
      w: (rnd() - .5) * .014, w2: (rnd() - .5) * .04, ph: rnd() * TAU, wob: 14 + rnd() * 18, ws: .12, zo: (rnd() - .5) * .6, rigid: rnd() < .15 });
  }
  for (let k = 0; k < 1; k++)   // a long loose loop that tie the knots together
    K.push({ p: 1, q: 2 + k, cx: 1050 + k * 60, cy: 500 - k * 40, R: 360 + k * 110, A: 40, ex: 1.15, ey: .75, rot: k, w: .003 * (k - 1), w2: .01, ph: k * 2, wob: 110, ws: .1, zo: 0, rigid: false });
  const S = K.map((o) => { const f = torus(o); return strand(o.rigid ? (u) => f(u, 0) : f, o.p * o.q > 10 || o.p === 1 ? 440 : 300, true, o.rigid ? () => hardS : () => soft); });
  const names = ["approval", "handoff", "spend limit", "data out", "access", "sign-off"];
  const labels = names.map((n, i) => ({ n, si: Math.floor(rnd() * (S.length - 3)), u: rnd() }));
  const slugs = Array.from({ length: 7 }, () => {
    const si = Math.floor(rnd() * S.length);
    return { si, u: rnd(), v: (rnd() < .5 ? -1 : 1) * (.004 + rnd() * .006) * (K[si].p === 1 ? .4 : 1), cool: 0,
      ps: [7, 6, 5, 4.2, 3.4, 2.6].map((r) => ({ x: 0, y: 0, r, init: false })) };
  });
  let X = [];
  const fogL = layer(), sharpL = layer(), maskL = layer(), gc = layer();
  const lens = (t) => [
    [1020 + 240 * Math.sin(t * TAU / 80), 440 + 170 * Math.sin(t * TAU / 40 + 1), 220],
    [1160 + 180 * Math.cos(t * TAU / 61), 470 + 200 * Math.sin(t * TAU / 61 + 2), 140],
  ];
  return {
    W, H, maxDpr: 1.5, still: 20,
    step(dt, t) {
      if (!X.length) { sample(S, t); X = crossings(S, 26); }
      for (const sl of slugs) {
        sl.u += sl.v * dt; sl.cool -= dt;
        if (sl.cool <= 0) for (const c of X) {   // at a crossing, now and then an agent changes protocol
          for (const [me, other] of [[c.o, c.u], [c.u, c.o]]) {
            if (me.si !== sl.si || K[me.si].rigid) continue;
            const uc = (me.i + me.f) / S[me.si].n, du = Math.abs((((sl.u - uc) % 1) + 1.5) % 1 - .5);
            if (du < .003) { sl.cool = 3; if (rnd() < .3 && !K[other.si].rigid) { sl.si = other.si; sl.u = (other.i + other.f) / S[other.si].n; sl.v = (rnd() < .5 ? -1 : 1) * Math.abs(sl.v); } }
          }
          if (sl.cool > 0) break;
        }
        sl.ps.forEach((p, k) => {
          const [x, y] = at(S[sl.si], sl.u - Math.sign(sl.v) * k * .004 * (K[sl.si].p === 1 ? .4 : 1));
          if (!p.init) { p.x = x; p.y = y; p.init = true; }
          const f = 1 - Math.exp(-dt * (9 - k * 1.1)); p.x += (x - p.x) * f; p.y += (y - p.y) * f;   // the tail lags: ooze
        });
      }
    },
    draw(g, t, k) {
      sample(S, t); X = crossings(S, 26);
      const pw = Math.round(W * k), ph = Math.round(H * k);
      for (const L of [fogL, sharpL, maskL]) if (L.width !== pw || L.height !== ph) { L.width = pw; L.height = ph; }
      // the fog: everything, faint and out of focus
      const f = fogL.getContext("2d"); f.setTransform(1, 0, 0, 1, 0, 0); f.clearRect(0, 0, pw, ph); f.setTransform(k, 0, 0, k, 0, 0);
      diagram(f, S, X, { forced: { c: "#aaa69d", w: .8, rope: 2, rw: 1.6, pitch: 9, body: .3, fray: 1 }, gap: 3 });
      // in focus: crossings drawn properly, hard strands in forest, agents, names
      const s = sharpL.getContext("2d"); s.setTransform(1, 0, 0, 1, 0, 0); s.clearRect(0, 0, pw, ph); s.setTransform(k, 0, 0, k, 0, 0);
      diagram(s, S, X, { gap: 3.2 });
      flow(s, slugs.map((sl) => sl.ps), { cell: 4, fa: .12, s: 5.2, cache: gc });
      for (const l of labels) { const [x, y] = at(S[l.si], l.u); text(s, x + 8, y - 8, l.n, 16, C.ink, "left", 400, .4); }
      const m = maskL.getContext("2d"); m.setTransform(1, 0, 0, 1, 0, 0); m.clearRect(0, 0, pw, ph); m.setTransform(k, 0, 0, k, 0, 0);
      for (const [x, y, r] of lens(t)) {
        const gr = m.createRadialGradient(x, y, 0, x, y, r);
        gr.addColorStop(0, "#000"); gr.addColorStop(.5, "rgba(0,0,0,.85)"); gr.addColorStop(1, "rgba(0,0,0,0)");
        m.fillStyle = gr; m.fillRect(x - r, y - r, 2 * r, 2 * r);
      }
      s.setTransform(1, 0, 0, 1, 0, 0); s.globalCompositeOperation = "destination-in"; s.drawImage(maskL, 0, 0); s.globalCompositeOperation = "source-over";
      g.save(); g.setTransform(1, 0, 0, 1, 0, 0);
      g.filter = `blur(${(3.2 * k).toFixed(1)}px)`; g.globalAlpha = .6; g.drawImage(fogL, 0, 0); g.filter = "none"; g.globalAlpha = 1;
      g.drawImage(sharpL, 0, 0); g.restore();
    },
  };
}

// ==== 01 see: the org chart unravels into the tangle it was hiding ==========================================
// Each protocol starts as an org-chart route (up the hierarchy and back down) and peels off into the path the work
// really takes: hard flows set rigid, in forest; soft ones coil, drift and are porous (dashed).
function see(m) {
  const W = m ? 400 : 680, H = m ? 610 : 420, fs = m ? 10.5 : 9, T = 20;
  const G = m ? { lead: [155, 20], depts: [[22, "SALES"], [155, "OPS"], [288, "FINANCE"]], dy: 84, ty: 142, bus1: 62, tx: (x) => [x - 8, x + 53] }
              : { lead: [295, 28], depts: [[70, "SALES"], [295, "OPERATIONS"], [520, "FINANCE"]], dy: 92, ty: 150, bus1: 70, tx: (x) => [x - 10, x + 55] };
  const dc = (d) => G.depts[d][0] + 45, tc = (d, k) => G.tx(G.depts[d][0])[k] + 22.5;
  const busT = G.dy + 40, leadC = G.lead[0] + 45, leadB = G.lead[1] + 22, tb = G.ty + 20;
  const up = (d, k) => [[tc(d, k), G.ty], [tc(d, k), busT], [dc(d), busT], [dc(d), G.dy + 22], [dc(d), G.dy], [dc(d), G.bus1]];
  const route = ([da, ka], to) => to === "lead" ? [...up(da, ka), [leadC, G.bus1], [leadC, leadB]]
    : [...up(da, ka), ...up(to[0], to[1]).reverse()];
  const polyAt = (pts) => {   // a polyline by arc length
    const L = [0]; for (let i = 1; i < pts.length; i++) L.push(L[i - 1] + Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]));
    return (u) => { const d = clamp(u, 0, 1) * L[L.length - 1]; let i = 1; while (i < L.length - 1 && L[i] < d) i++; const f = (d - L[i - 1]) / ((L[i] - L[i - 1]) || 1); return [lerp(pts[i - 1][0], pts[i][0], f), lerp(pts[i - 1][1], pts[i][1], f)]; };
  };
  const P = m ? {
    defs: [
      { from: [0, 0], to: [1, 0], hard: false, way: [[36.5, 162], [26, 250], [120, 310], [175, 230], [169.5, 162]] },
      { from: [1, 1], to: [2, 0], hard: true, way: [[230.5, 162], [236, 250], [296, 250], [302.5, 162]] },
      { from: [2, 1], to: "lead", hard: true, way: [[363.5, 162], [352, 300], [372, 470]] },
    ], edge: [[14, 440], [W - 14, 440]], a: 12,
  } : {
    defs: [
      { from: [0, 0], to: [1, 0], hard: false, way: [[tc(0, 0), tb], [64, 250], [170, 310], [250, 205], [330, 290], [tc(1, 0), tb]] },
      { from: [1, 1], to: [2, 0], hard: true, way: [[tc(1, 1), tb], [395, 250], [480, 262], [tc(2, 0), tb]] },
      { from: [2, 1], to: "lead", hard: true, way: [[tc(2, 1), tb], [606, 262], [640, 292], [676, 296]] },
    ], edge: [[640, 20], [640, 330]], a: 14,
  };
  const morph = (t) => { const ph = t % T; return ease(clamp((ph - 2.5) / 3.5, 0, 1)) * (1 - ease(clamp((ph - 16.5) / 3, 0, 1))); };
  const orgSt = { c: C.faint, w: .6 }, hardSt = crystalSt(2.6, 12), softSt = { c: C.ink, w: 0.66, rope: 2, rw: 1.7, pitch: 10, d: [5, 2.5], fray: 0.45, body: .07 };
  const S = P.defs.map((d, i) => {
    const org = polyAt(route(d.from, d.to)), tang = d.hard ? coil(d.way, 0, 1, 0, i) : coil(d.way, P.a * .8, 6, .25, i * 2.1);
    const st = { cur: orgSt };
    const s = strand((u, t) => { const k = morph(t), [ox, oy] = org(u), [x, y, z] = tang(u, d.hard ? 0 : t); return [lerp(ox, x, k), lerp(oy, y, k), z]; }, 420, false, () => st.cur);
    s.def = d; s.st = st; return s;
  });
  const slugs = []; S.forEach((s, i) => { for (let k = 0; k < 1; k++) slugs.push({ s: i, u0: i * .3, ps: [4, 3.2, 2.6].map((r) => ({ x: 0, y: 0, r, w: 1 })) }); });
  const ink = layer(), gc = layer();
  return {
    W, H, still: 11,
    draw(g, t, k) {
      const mk = morph(t);
      for (const s of S) s.st.cur = mk < .2 ? orgSt : s.def.hard ? hardSt : softSt;
      sample(S, t);
      const X = mk > .3 ? crossings(S, 20) : [];
      const pw = Math.round(W * k), ph = Math.round(H * k);
      if (ink.width !== pw || ink.height !== ph) { ink.width = pw; ink.height = ph; }
      const s = ink.getContext("2d"); s.setTransform(1, 0, 0, 1, 0, 0); s.clearRect(0, 0, pw, ph); s.setTransform(k, 0, 0, k, 0, 0);
      // the org chart's own lines are the protocols, before they come loose
      diagram(s, S, X, { gap: 2.6, reach: 7 });
      for (const sl of slugs) {   // agents ride the protocols once they're visible
        const u = (t / 10 + sl.u0) % 1;
        sl.ps.forEach((p, i) => { const [x, y] = at(S[sl.s], u - i * .008); p.x = x; p.y = y; p.w = smooth(.7, 1, mk) * smooth(0, .08, u) * smooth(1, .9, u); });
      }
      flow(s, slugs.map((sl) => sl.ps), { cell: 3, fa: .14, s: 4.2, cache: gc });
      g.save(); g.setTransform(1, 0, 0, 1, 0, 0); g.drawImage(ink, 0, 0); g.restore();
      // the reporting lines stay as a ghost, and the boxes sit on top, fading as the tangle shows
      g.globalAlpha = .6 * smooth(0, .3, mk);
      for (const d of [0, 1, 2]) { line(g, [[leadC, leadB], [leadC, G.bus1], [dc(d), G.bus1], [dc(d), G.dy]], C.faint, .5);
        for (const k2 of [0, 1]) line(g, [[dc(d), G.dy + 22], [dc(d), busT], [tc(d, k2), busT], [tc(d, k2), G.ty]], C.faint, .5); }
      g.globalAlpha = 1;
      g.globalAlpha = lerp(1, .45, mk);
      box(g, G.lead[0], G.lead[1], 90, 22, "LEAD", fs * .85);
      for (const [x, name] of G.depts) { box(g, x, G.dy, 90, 22, name, fs * .85); G.tx(x).forEach((tx, i) => box(g, tx, G.ty, 45, 20, `TEAM ${i + 1}`, fs * .75)); }
      g.globalAlpha = 1;
      g.globalAlpha = smooth(.4, 1, mk);
      line(g, P.edge, C.ink2, .5, [4, 3]);
      if (m) text(g, 14, 434, "COMPANY EDGE", fs * .8, C.ink2); else text(g, 636, 30, "COMPANY EDGE", fs * .8, C.ink2, "right");
      const e = S[2], [x, y] = at(e, 1), [px, py] = at(e, .985); arrow(g, x, y, Math.atan2(y - py, x - px), 6, C.hard, 1.6);
      [.25, .5, .55].forEach((u, i) => { const [x, y] = at(S[i], u); numbered(g, x, y, i + 1, i ? C.hard : C.ink, fs * .95); });
      g.globalAlpha = 1;
      // key: what the lines are, and which protocols are named
      const lx = m ? 14 : 24, ly = m ? H - 92 : H - 48;
      const row = (dy, st, label, a = 1) => { g.globalAlpha = a; if (st.rope || st.crystal) ropeLine(g, lx, lx + 30, ly + dy - 3, { ...st, a }); else line(g, [[lx, ly + dy - 3], [lx + 30, ly + dy - 3]], st.c, st.w); text(g, lx + 38, ly + dy, label, fs * .9, st === orgSt ? C.ink2 : C.ink); g.globalAlpha = 1; };
      row(0, orgSt, "who reports to whom");
      row(16, hardSt, "hard: enforced, fixed in place", .3 + .7 * mk);
      row(32, softSt, "soft: fluid and porous", .3 + .7 * mk);
      const names = m ? ["handoff", "approval", "data leaves"] : ["order handoff", "payment approval", "data leaves"];
      let kx = m ? 14 : 400; const ky = m ? H - 22 : H - 14;
      g.globalAlpha = .3 + .7 * mk;
      names.forEach((n, i) => { numbered(g, kx + 6, ky - 3, i + 1, i ? C.hard : C.ink, fs * .85); text(g, kx + 16, ky, n, fs * .9); kx += (n.length + 4) * fs * .6 + 4; });
      g.globalAlpha = 1;
    },
  };
}

// ==== 02 hard core: a long exposure ==========================================================================
// A snapshot of the tangle shows every protocol alike. Leave the shutter open: the soft protocols move and blur into
// haze, and what stays sharp is the hard core: one rigid ring whose eight stretches most companies share.
const CORE = [["Signing authority", "who can commit the company"], ["Spending limits", "how much, and by whom"], ["Payment approval", "who may move money"],
  ["Access rights", "who and what sees what"], ["Change control", "nothing ships unreviewed"], ["Data out", "what may leave the company"],
  ["Output checks", "tests every result must pass"], ["Audit trail", "every action, with its reason"]];
const mix = (a, b, t) => { const A = hex(a), B = hex(b); return `rgb(${A.map((v, i) => Math.round(lerp(v, B[i], t))).join(",")})`; };
function core(m) {
  const W = m ? 400 : 680, H = m ? 700 : 410, fs = m ? 11 : 10.5, rnd = rng(17), T = 18;
  const cx = 200, cy = m ? 215 : 222, sc = m ? .95 : 1, RO = 170 * sc;
  const softSt = { c: C.ink, w: 0.54, rope: 2, rw: 1.3, pitch: 9, fray: 0.45, body: .07 };
  const coreSt = { c: C.ink, w: 0.54, rope: 2, rw: 1.3, pitch: 9, fray: 0.45, body: .07 };
  const hazeSt = { c: C.faint, w: .9, a: .5 };
  // the exposure: 0 snapshot, 1 shutter open
  const expo = (t) => { const p = t % T; return smooth(3.5, 7, p) * (1 - smooth(15.5, 17.5, p)); };
  let tau = 0;   // the soft protocols' own clock: it runs faster while the shutter is open
  const softClock = (u, t, f) => f(u, tau);
  const S = [];
  [[2, 3, 0, 0, 104], [3, 4, -26, 20, 124], [1, 4, 0, 0, 152]].forEach(([p, q, dx, dy, R], i) => {
    const f = torus({ p, q, cx: cx + dx * sc, cy: cy + dy * sc, R: R * sc, A: R * sc * (p === 1 ? .12 : .5), ex: 1, ey: .92, rot: i * 1.1,
      w: (i % 2 ? -1 : 1) * (.05 + i * .006), w2: ((i % 3) - 1) * .08 || .06, ph: i * 1.3, wob: 9, ws: .5, zo: 0 });
    S.push(strand((u, t) => softClock(u, t, f), 320, true, () => softSt));
  });
  const nSoft = S.length;
  // the hard core: one rigid trefoil, eight stretches
  const R = 92 * sc;
  let coreCur = coreSt; const coreCrystal = crystalSt(3.8, 11);
  const coreS = strand((u) => { const th = TAU * u - Math.PI / 2; return [cx + R * Math.cos(th), cy + R * Math.sin(th), 1.6 * Math.sin(6 * th)]; }, 360, true, () => coreCur);   // weaves over and under the rest
  S.push(coreS);
  sample([coreS], 0);
  const coreSegs = []; for (let i = 0; i < coreS.n; i++) { const j = (i + 1) % coreS.n, p = coreS.pts; coreSegs.push([p[3 * i], p[3 * i + 1], p[3 * j], p[3 * j + 1]]); }
  const coreX = crossings([coreS], 18);
  const spawn = (p) => { const a = rnd() * TAU, r = RO * (.45 + .5 * Math.sqrt(rnd())); p.x = cx + r * Math.cos(a); p.y = cy + r * Math.sin(a); p.vx = p.vy = 0; };
  const A = Array.from({ length: 26 }, () => { const p = { r: 3.4, vx: 0, vy: 0 }; spawn(p); return p; });
  const crisp = layer(), haze = layer(), hard = layer(), gc = layer();
  let frames = 0;
  const fit = (L, pw, ph) => { if (L.width !== pw || L.height !== ph) { L.width = pw; L.height = ph; return true; } return false; };
  return {
    W, H, still: 11,
    step(dt, t) {
      tau += dt * (1 + 9 * expo(t));
      liquid(A, 6, 12, .5);
      for (const p of A) {
        const dx = p.x - cx, dy = p.y - cy, d = Math.hypot(dx, dy) || 1;
        p.vx += (-dy / d) * .05 + (rnd() - .5) * .2 - dx / d * .012; p.vy += (dx / d) * .05 + (rnd() - .5) * .2 - dy / d * .012;
        if (d > RO - 15) { p.vx -= dx / d * .25; p.vy -= dy / d * .25; }
        p.vx *= .9; p.vy *= .9; p.x += p.vx; p.y += p.vy;
        for (const [ax, ay, bx, by] of coreSegs) {   // the core is closed to agents
          const ex = bx - ax, ey = by - ay, l2 = ex * ex + ey * ey || 1, u = clamp(((p.x - ax) * ex + (p.y - ay) * ey) / l2, 0, 1);
          const qx = p.x - (ax + u * ex), qy = p.y - (ay + u * ey), q = Math.hypot(qx, qy), min = 5.5;
          if (q < min && q > 1e-6) { p.x += qx / q * (min - q); p.y += qy / q * (min - q); const vn = (p.vx * qx + p.vy * qy) / q; if (vn < 0) { p.vx -= vn * qx / q; p.vy -= vn * qy / q; } }
        }
        p.w = clamp((RO + 10 - Math.hypot(p.x - cx, p.y - cy)) / 14, 0, 1);
        if (Math.hypot(p.x - cx, p.y - cy) > RO + 10) spawn(p);
      }
    },
    draw(g, t, k) {
      const e = expo(t), pw = Math.round(W * k), ph = Math.round(H * k);
      const soft = S.slice(0, nSoft);
      sample(soft, t);
      if (fit(haze, pw, ph)) frames = 0;
      fit(crisp, pw, ph); fit(hard, pw, ph);
      // the long exposure: each frame fades what came before and adds the soft strands faintly
      const h = haze.getContext("2d"); h.setTransform(1, 0, 0, 1, 0, 0);
      h.globalCompositeOperation = "destination-out"; h.fillStyle = `rgba(0,0,0,${e > .02 ? .09 : .3})`; h.fillRect(0, 0, pw, ph);
      h.globalCompositeOperation = "source-over"; h.setTransform(k, 0, 0, k, 0, 0);
      h.globalAlpha = .05; for (const s of soft) runs(h, s, 0, s.n, hazeSt); h.globalAlpha = 1; frames++;
      // the snapshot: everything crisp, and alike
      const cr = smooth(.35, .8, e); coreCur = coreSt;   // rope in the snapshot; it crystallises as the shutter stays open
      if (e < .999) {
        const c = crisp.getContext("2d"); c.setTransform(1, 0, 0, 1, 0, 0); c.clearRect(0, 0, pw, ph); c.setTransform(k, 0, 0, k, 0, 0);
        diagram(c, S, crossings(S, 18), { gap: 2.8, reach: 7 });
      }
      const hd = hard.getContext("2d"); hd.setTransform(1, 0, 0, 1, 0, 0); hd.clearRect(0, 0, pw, ph); hd.setTransform(k, 0, 0, k, 0, 0);
      if (cr < 1) { coreCur = { ...coreSt, c: mix(C.ink, C.hard, cr), a: 1 - cr }; diagram(hd, [coreS], coreX, { gap: 3.2, reach: 8 }); }
      if (cr > 0) { coreCur = { ...coreCrystal, a: cr }; diagram(hd, [coreS], coreX, { gap: 3.2, reach: 10 }); }
      coreCur = coreSt;
      g.save(); g.setTransform(1, 0, 0, 1, 0, 0);
      if (e > 0) {
        g.globalAlpha = e * .7;
        if (frames > 20) g.drawImage(haze, 0, 0);
        else { g.filter = `blur(${(2.5 * k).toFixed(1)}px)`; g.globalAlpha = e * .35; g.drawImage(crisp, 0, 0); g.filter = "none"; }   // a still frame: fake the blur
      }
      g.restore();
      g.globalAlpha = 1 - .5 * e; swarm(g, A, { cell: 3, fa: .05, s: 3.2, cache: gc }); g.globalAlpha = 1;
      g.save(); g.setTransform(1, 0, 0, 1, 0, 0);
      if (e < 1) { g.globalAlpha = 1 - e; g.drawImage(crisp, 0, 0); }
      g.globalAlpha = smooth(0, .5, e); g.drawImage(hard, 0, 0); g.globalAlpha = 1; g.restore();
      // the core named: a pin between stretches, a number on each
      const held = smooth(.75, 1, e);
      if (held > 0) {
        g.globalAlpha = held;
        for (let i = 0; i < 8; i++) {
          const [px, py] = at(coreS, i / 8); g.fillStyle = C.hard; g.fillRect(px - 2.4, py - 2.4, 4.8, 4.8);
          const [x, y] = at(coreS, (i + .5) / 8), dx = x - cx, dy = y - cy, d = Math.hypot(dx, dy) || 1;
          numbered(g, x + dx / d * 14, y + dy / d * 14, i + 1, C.hard, fs * .9);
        }
        g.globalAlpha = 1;
      }
      // what the reader is looking at, as it changes
      const tx = m ? 14 : 24;
      g.globalAlpha = 1 - smooth(.1, .4, e); text(g, tx, 20, "A SNAPSHOT: EVERY PROTOCOL LOOKS ALIKE", fs * .85, C.ink, "left", 500);
      g.globalAlpha = smooth(.6, .9, e); text(g, tx, 20, "OVER TIME: THE SOFT ONES MOVE, THE HARD CORE HOLDS", fs * .85, C.hard, "left", 500);
      g.globalAlpha = 1;
      const lx = m ? 14 : 410, l0 = m ? 480 : 78, step = m ? 26 : 34;
      if (!m) { g.globalAlpha = .3 + .7 * held; text(g, lx, 50, "THE HARD CORE MOST COMPANIES SHARE", fs * .85, C.hard, "left", 500); g.globalAlpha = 1; }
      CORE.forEach(([name, detail], i) => {
        const y = l0 + i * step; g.globalAlpha = .3 + .7 * held;
        numbered(g, lx + 6, y - 3, i + 1, C.hard, fs * .9);
        text(g, lx + 20, y, name, fs * 1.05, C.ink, "left", 500);
        if (!m) text(g, lx + 20, y + 12, detail, fs * .8, C.ink2); else text(g, lx + 20 + (name.length + 1) * fs * 1.05 * .6, y, detail, fs * .8, C.ink2);
        g.globalAlpha = 1;
      });
      const ky = m ? H - 26 : H - 28, kx = m ? 14 : 410;
      g.globalAlpha = .3 + .7 * held;
      ropeLine(g, kx, kx + 30, ky - 3, crystalSt(3, 10)); text(g, kx + 40, ky, "hard: holds still, closed to agents", fs * .85);
      g.globalAlpha = 1;
    },
  };
}

// ==== 03 risk: approval steps get flowed around; constraints built in, and guardrails laid down ======================================================================
function scale(m) {
  const W = m ? 400 : 680, H = m ? 690 : 340, fs = m ? 10.5 : 12, rnd = rng(7);
  const gx = 238, gy = 170;
  const A = Array.from({ length: 34 }, () => ({ x: 20 + rnd() * 300, y: gy + (rnd() - .5) * 120, vx: 0, vy: 0, r: 3.6 }));
  // B: no box. Each agent carries its own constraints (micro), and the ground has guides (macro), with new guardrails
  // laid wherever agents start to stray toward what's off limits.
  const T = 24, bx0 = 366, bx1 = 672, by0 = 66, by1 = 322;
  const zones = [{ r: [528, 266, 672, 322], at: 1 }, { r: [586, 70, 672, 110], at: 10 }];   // new risks keep appearing
  const rail = (x0, x1, y, amp, ph) => Array.from({ length: 24 }, (_, i) => { const x = lerp(x0, x1, i / 23); return [x, y + amp * Math.sin(x * .03 + ph)]; });
  const rails = [rail(430, 640, 176, 12, 1)];
  const segsOf = (pts) => pts.slice(1).map((q, i) => [pts[i][0], pts[i][1], q[0], q[1]]);
  const railSegs = rails.flatMap(segsOf);
  let guards = [], lastPh = 0;
  const respawnB = (p) => { p.x = bx0 + 2 + rnd() * 14; p.y = by0 + 20 + rnd() * (by1 - by0 - 50); p.vx = p.vy = 0; };
  const B = Array.from({ length: 22 }, () => { const p = { x: bx0 + rnd() * 300, y: by0 + 20 + rnd() * 200, vx: 0, vy: 0, r: 3.6, ph: rnd() * TAU }; return p; });
  const push = (p, segs, min) => {
    for (const [ax, ay, bx, by] of segs) {
      const ex = bx - ax, ey = by - ay, l2 = ex * ex + ey * ey || 1, u = clamp(((p.x - ax) * ex + (p.y - ay) * ey) / l2, 0, 1);
      const qx = p.x - (ax + u * ex), qy = p.y - (ay + u * ey), q = Math.hypot(qx, qy);
      if (q < min && q > 1e-6) { p.x += qx / q * (min - q); p.y += qy / q * (min - q); const vn = (p.vx * qx + p.vy * qy) / q; if (vn < 0) { p.vx -= vn * qx / q; p.vy -= vn * qy / q; } }
    }
  };
  const guardLen = (gd, t) => 24 * ease(clamp((t - gd.born) / .8, 0, 1));
  const guardSeg = (gd, t) => { const l = guardLen(gd, t); return [gd.x - gd.dx * l, gd.y - gd.dy * l, gd.x + gd.dx * l, gd.y + gd.dy * l]; };
  const near = (z, p) => { const [x0, y0, x1, y1] = z.r, qx = clamp(p.x, x0, x1), qy = clamp(p.y, y0, y1); return [qx, qy, Math.hypot(p.x - qx, p.y - qy)]; };
  const gcA = layer(), gcB = layer();
  let approved = 0;
  return {
    W, H, still: 20,
    step(dt, t) {
      // A: a stream pushed toward one approval step. It can't pass, so it goes around, over and under
      liquid(A, 9, 15, .3);
      for (const p of A) {
        p.vx += .13 + (p.x < gx ? 0 : .06); p.vy += (gy - p.y) * (p.x < gx - 30 ? .0025 : -.0006) + (rnd() - .5) * .25;
        if (p.x > gx - 34 && p.x < gx + 12 && Math.abs(p.y - gy) < 34) { p.vy += Math.tanh((p.y - gy) / 8) * .55 + (p.y === gy ? .01 : 0); p.vx -= .1; }   // the step itself
        p.vx *= .88; p.vy *= .88; p.x += p.vx * .45; p.y += p.vy * .45;   // slowed, so it reads
        p.w = clamp((330 - p.x) / 22, 0, 1) * clamp((p.y - 60) / 12, 0, 1) * clamp((330 - p.y) / 12, 0, 1);
        if (p.x > 328 || p.y < 60 || p.y > 330) { p.x = 16 + rnd() * 30; p.y = gy + (rnd() - .5) * 110; p.vx = p.vy = 0; }
      }
      approved = (t % 10) / 10;
      // B: agents move freely; guides shape the flow; guardrails appear where agents stray
      const ph = t % T; if (ph < lastPh) guards = []; lastPh = ph;
      liquid(B, 9, 15, .35);
      const gSegs = guards.map((gd) => guardSeg(gd, t));
      for (const p of B) {
        p.vx += .045 + Math.cos(t * .4 + p.ph) * .05 + (rnd() - .5) * .14; p.vy += Math.sin(t * .31 + p.ph * 1.3) * .05 + (p.x > 460 ? .055 : .01) + (rnd() - .5) * .14;
        p.vx *= .92; p.vy *= .92; p.x += p.vx * .45; p.y += p.vy * .45;
        push(p, railSegs, 5); push(p, gSegs, 5);
        if (p.y < by0 + 4) { p.y = by0 + 4; p.vy = Math.abs(p.vy); }
        for (const z of zones) {
          if (ph < z.at + .8) continue;
          const [qx, qy, d] = near(z, p);
          if (d === 0) { respawnB(p); break; }
          if (d < 9 && !guards.some((gd) => gd.z === z && Math.hypot(gd.x - qx, gd.y - qy) < 30)) {   // a new guardrail where an agent strayed
            const [x0, y0, x1, y1] = z.r, vert = (qx === x0 || qx === x1) && qy > y0 && qy < y1, nx = (p.x - qx) / d, ny = (p.y - qy) / d;
            const cx = vert ? qx : clamp(qx, x0 + 18, x1 - 18), cy = vert ? clamp(qy, y0 + 18, y1 - 18) : qy;
            guards.push({ z, x: cx + nx * 6, y: cy + ny * 6, dx: vert ? 0 : 1, dy: vert ? 1 : 0, born: t });
          }
        }
        p.w = clamp((bx1 - p.x) / 18, 0, 1) * clamp((by1 - p.y) / 12, 0, 1) * zones.reduce((w, z) => (ph < z.at + .8 ? w : Math.min(w, clamp(near(z, p)[2] / 6, 0, 1))), 1);
        if (p.x > bx1 || p.y > by1) respawnB(p);
      }
    },
    draw(g, t) {
      const panelA = () => {
        text(g, 24, 32, "APPROVAL QUEUE", fs * 1.05, C.ink, "left", 500);
        text(g, 24, 46, "agents don't wait: they flow around it", fs * .85, C.ink2);
        swarm(g, A, { cell: 3.5, fa: .08, s: 3.3, cache: gcA });
        g.fillStyle = C.paper; g.fillRect(gx - 8, gy - 22, 16, 44); g.strokeStyle = C.ink; g.lineWidth = .9; g.strokeRect(gx - 8, gy - 22, 16, 44);
        text(g, gx, gy + 38, "APPROVE", fs * .8, C.ink, "center");
        line(g, [[gx + 9, gy], [322, gy]], C.ink, .5); arrow(g, 322, gy, 0, 6, C.ink, .8);
        const ax = lerp(gx + 10, 320, approved); g.globalAlpha = smooth(0, .1, approved) * smooth(1, .9, approved);
        g.beginPath(); g.arc(ax, gy, 2.2, 0, TAU); g.fillStyle = C.ink; g.fill(); g.globalAlpha = 1;
        text(g, gx + 52, gy - 9, "one at a time", fs * .75, C.ink2, "center");
        text(g, gx, 70, "AROUND IT", fs * .8, C.ink2, "center");
      };
      const panelB = () => {
        text(g, 364, 32, "HARD PROTOCOLS", fs * 1.05, C.hard, "left", 500);
        text(g, 364, 46, "built into every agent, and into the ground", fs * .85, C.ink2);
        // what's off limits, and the guardrails laid in front of it
        const ph = t % T;
        for (const z of zones) {
          const [hx0, hy0, hx1, hy1] = z.r, a = smooth(z.at, z.at + .8, ph);
          if (!a) continue;
          g.save(); g.globalAlpha = .5 * a; g.fillStyle = hatch(g, C.hard); g.fillRect(hx0, hy0, hx1 - hx0, hy1 - hy0); g.restore();
          g.globalAlpha = a; text(g, hx1 - 4, hy1 > 300 ? hy0 + fs * .95 : hy1 - 6, "OFF LIMITS", fs * .72, C.ink2, "right"); g.globalAlpha = 1;
        }
        swarm(g, B, { cell: 3.5, fa: .06, s: 3.3, mark: true, cache: gcB });
        for (const r of rails) pathLine(g, r, crystalSt(2.6, 11));
        const re = rails[0][rails[0].length - 1]; text(g, re[0] + 8, re[1] + 3, "GUIDES", fs * .75, C.hard);
        let newest = null;
        for (const gd of guards) {
          const [ax, ay, bx, by] = guardSeg(gd, t); if (guardLen(gd, t) > 2) pathLine(g, [[ax, ay], [bx, by]], crystalSt(2.6, 10));
          if (!newest || gd.born > newest.born) newest = gd;
        }
        if (newest) { const a = 1 - smooth(2.5, 4, t - newest.born); if (a > 0) { g.globalAlpha = a; text(g, newest.dy ? newest.x - 8 : newest.x, newest.dy ? newest.y : newest.y - 8, "NEW GUARDRAIL", fs * .72, C.hard, newest.dy ? "right" : "center", 500); g.globalAlpha = 1; } }
      };
      if (m) {
        g.save(); g.translate(30, 0); panelA(); g.restore();
        line(g, [[14, 345], [W - 14, 345]], C.ink2, .5, [14, 3, 2, 3]);
        g.save(); g.translate(-310, 340); panelB(); g.restore();
      } else { panelA(); line(g, [[340, 14], [340, 326]], C.ink2, .5, [14, 3, 2, 3]); panelB(); }
    },
  };
}

// ==== 04 opportunity: a net woven out from one hard interface, toward futures nobody planned =====================
// Threads leave the interface and get tied off into a net. It sags like rope, reaches toward possible futures
// (dashed), and builds each one it arrives at. Agents ooze out along it.
function upside(m) {
  const W = m ? 400 : 680, H = m ? 690 : 340, fs = m ? 11 : 10.5, rnd = rng(21);
  const rx0 = 400, ry0 = 74, rx1 = 664, ry1 = 300, ix = 392, T = 26;
  const threadSt = { c: C.ink, w: .45, rope: 2, rw: 1.1, pitch: 7, fray: .35, body: .12 };
  const ports = Array.from({ length: 6 }, (_, k) => ry0 + 10 + k * (ry1 - ry0 - 20) / 5);
  const NAMES = ["partner app", "agent tool", "new market", "data product", "marketplace", "open API"];
  const futures = []; for (let k = 0; k < 800 && futures.length < NAMES.length; k++) {
    const x = rx0 + 60 + rnd() * (rx1 - rx0 - 120), y = ry0 + 12 + rnd() * (ry1 - ry0 - 24);
    if (futures.every((f) => Math.hypot(f.x - x, f.y - y) > 70 && Math.abs(f.y - y) > 22)) futures.push({ x, y, name: NAMES[futures.length], built: 0 });
  }
  let nodes, edges, slugs, lastPh = 0, clock = 0, spawn = 0;
  const reset = () => { nodes = ports.map((y) => ({ x: ix + 8, y, p: -1, born: -9 })); edges = []; slugs = []; futures.forEach((f) => (f.built = 0)); };
  reset();
  const tie = (a, b, t) => {   // a thread between two knots, sagging a little
    const A = nodes[a], B = nodes[b], mx = (A.x + B.x) / 2, my = (A.y + B.y) / 2 + 3 + Math.hypot(B.x - A.x, B.y - A.y) * .08;
    const s = strand((u) => [lerp(lerp(A.x, mx, u), lerp(mx, B.x, u), u), lerp(lerp(A.y, my, u), lerp(my, B.y, u), u), 0], 20, false, () => threadSt);
    sample([s], 0); edges.push({ a, b, born: t, s });
  };
  const grow = (t) => {
    let best = null, bs = -1e9;
    for (let k = 0; k < 28; k++) {
      const i = Math.floor(Math.pow(rnd(), .6) * nodes.length), n = nodes[nodes.length - 1 - i] || nodes[0];
      const a = (rnd() - .5) * 2.2, d = 32 + rnd() * 18, x = n.x + Math.cos(a) * d, y = n.y + Math.sin(a) * d;
      if (x < ix + 20 || x > rx1 || y < ry0 || y > ry1 || nodes.some((o) => Math.hypot(o.x - x, o.y - y) < 32)) continue;
      const open = futures.filter((f) => !f.built), near = open.length ? Math.min(...open.map((f) => Math.hypot(f.x - x, f.y - y))) : 0;
      const sc = -near + rnd() * 26;
      if (sc > bs) { bs = sc; best = { x, y, p: nodes.indexOf(n) }; }
    }
    if (!best) return;
    nodes.push({ ...best, born: t }); const j = nodes.length - 1;
    tie(best.p, j, t);
    let o = -1, od = 46; nodes.forEach((n, i) => { if (i !== j && i !== best.p && n.x > ix + 10) { const d = Math.hypot(n.x - best.x, n.y - best.y); if (d < od) { od = d; o = i; } } });
    if (o >= 0) tie(o, j, t + .3);   // a second thread makes it a net, not a branch
    for (const f of futures) if (!f.built && Math.hypot(f.x - best.x, f.y - best.y) < 17) f.built = t;
  };
  const prog = (e, t) => ease(clamp((t - e.born) / .9, 0, 1));
  return {
    W, H, still: 21,
    step(dt, t) {
      const ph = t % T; if (ph < lastPh) reset(); lastPh = ph;
      clock += dt; if (ph < 20 && clock > .6) { clock = 0; grow(t); }
      spawn -= dt;
      if (spawn <= 0 && ph < 22 && nodes.length > 10) {   // an agent heads out along the net
        spawn = .9; let i = nodes.length - 1 - Math.floor(rnd() * Math.min(nodes.length - 6, 60)); const path = [];
        while (i >= 0) { path.push(i); i = nodes[i].p; } path.reverse();
        slugs.push({ path, u: 0, v: 1.6 + rnd(), ps: [3.4, 2.8, 2.2].map((r) => ({ x: 0, y: 0, r, w: 1 })) });
      }
      for (const b of slugs) b.u += b.v * dt;
      slugs = slugs.filter((b) => b.u < b.path.length + 2);
    },
    draw(g, t) {
      const ph = t % T, fade = 1 - smooth(T - 2.5, T - .2, ph);
      const panelA = () => {
        text(g, 24, 32, "PRODUCT", fs * 1.05, C.ink, "left", 500);
        text(g, 24, 46, "steer to one planned target", fs * .85, C.ink2);
        const tx = 280, ty = 180, r2 = rng(3);
        for (const r of [24, 15, 6]) { g.beginPath(); g.arc(tx, ty, r, 0, TAU); g.strokeStyle = C.ink; g.lineWidth = .7; g.stroke(); }
        ropeLine(g, 40, tx - 30, ty, { c: C.ink, w: 0.72, rope: 2, rw: 1.4, pitch: 10, fray: 0.20, body: .15 }); arrow(g, tx - 26, ty, 0, 6, C.ink, 1.1);
        g.beginPath(); g.arc(40, ty, 3, 0, TAU); g.fillStyle = C.ink; g.fill();
        [[80, -1], [115, 1], [150, -1], [185, 1], [215, -1]].forEach(([bx, side]) => {
          const ex = bx + 34, ey = ty + side * (46 + r2() * 30);
          line(g, [[bx, ty], [ex, ey]], C.ink2, .5, [3, 3]); line(g, [[ex - 4, ey - 4], [ex + 4, ey + 4]], C.ink2, .7); line(g, [[ex - 4, ey + 4], [ex + 4, ey - 4]], C.ink2, .7);
        });
        text(g, 150, ty + 112, "other moves taken off the board", fs * .8, C.ink2, "center");
        const u = (t % 3.5) / 3.5; g.globalAlpha = smooth(0, .1, u) * smooth(1, .9, u);
        g.beginPath(); g.arc(lerp(40, tx - 28, u), ty, 2.4, 0, TAU); g.fillStyle = C.ink; g.fill(); g.globalAlpha = 1;
      };
      const panelB = () => {
        text(g, 364, 32, "PROTOCOL", fs * 1.05, C.hard, "left", 500);
        text(g, 364, 46, "widen what others can build", fs * .85, C.ink2);
        // possible futures: outlines until the net reaches them, then built
        let built = 0;
        for (const f of futures) {
          const on = f.built ? smooth(f.built, f.built + 1, t) * fade : 0; if (f.built) built++;
          const s = 5 + 3 * on;
          g.globalAlpha = 1; g.fillStyle = C.paper; g.fillRect(f.x - s, f.y - s, 2 * s, 2 * s);
          if (on) { g.globalAlpha = on; g.fillStyle = hatch(g, C.hard); g.fillRect(f.x - s, f.y - s, 2 * s, 2 * s); g.globalAlpha = 1; }
          g.strokeStyle = on ? C.ink : C.faint; g.lineWidth = on ? .9 : .7; g.setLineDash(on ? [] : [2, 2]); g.strokeRect(f.x - s, f.y - s, 2 * s, 2 * s); g.setLineDash([]);
          
        }
        g.globalAlpha = fade * .85;
        for (const e of edges) { const p = prog(e, t); if (p > 0) runs(g, e.s, 0, Math.max(1, Math.round(p * (e.s.n - 1)))); }
        for (const n of nodes) if (n.p >= 0 && t - n.born > .6) { g.beginPath(); g.arc(n.x, n.y, 1.9, 0, TAU); g.fillStyle = C.paper; g.fill(); g.strokeStyle = C.ink; g.lineWidth = .9; g.stroke(); }   // the knots
        for (const b of slugs) b.ps.forEach((p, k) => {
          const x = clamp(b.u - k * .25, 0, b.path.length - 1.001), i = Math.floor(x), f = x - i, A = nodes[b.path[i]], B = nodes[b.path[i + 1]] || A;
          p.x = lerp(A.x, B.x, f); p.y = lerp(A.y, B.y, f) + Math.sin(f * Math.PI) * 3; p.w = smooth(0, .6, b.u) * (1 - smooth(b.path.length - 1, b.path.length + 1, b.u));
        });
        flow(g, slugs.map((b) => b.ps), { cell: 3, fa: .1, s: 3.4, cache: this.gc || (this.gc = layer()) });
        g.globalAlpha = 1;
        for (const f of futures) if (f.built) { const on = smooth(f.built, f.built + 1, t) * fade; g.globalAlpha = on; haloText(g, f.x + 12, f.y + 3, f.name, fs * .85, C.ink, "left", 500); g.globalAlpha = 1; }
        pathLine(g, [[ix, ry0 - 8], [ix, ry1 + 8]], crystalSt(3, 14));
        for (const p of ports) { g.fillStyle = C.hard; g.fillRect(ix + 4, p - 2, 6, 4); }
        text(g, ix - 8, ry1 + 24, "HARD INTERFACE", fs * .8, C.hard);
        text(g, 664, ry1 + 24, `${built} of ${futures.length} futures built, none planned`, fs * .8, C.ink2, "right");
      };
      if (m) {
        g.save(); g.translate(30, 0); panelA(); g.restore();
        line(g, [[14, 345], [W - 14, 345]], C.ink2, .5, [14, 3, 2, 3]);
        g.save(); g.translate(-310, 340); panelB(); g.restore();
      } else { panelA(); line(g, [[340, 14], [340, 326]], C.ink2, .5, [14, 3, 2, 3]); panelB(); }
    },
  };
}

// ==== 05 evolve: the same ring, three versions =================================================================
// All soft: work goes anywhere. Too hard: everything queues at one gate. Then softened where it slowed good work:
// hard where it matters, porous elsewhere.
function evolve(m) {
  const W = m ? 400 : 680, H = m ? 600 : 270, fs = m ? 10.5 : 9, rnd = rng(5), R = m ? 52 : 50;
  const centres = m ? [[130, 100], [130, 300], [130, 500]] : [[110, 126], [340, 126], [570, 126]];
  const soft = { c: C.ink, w: .65, rope: 2, rw: 1.5, pitch: 9, d: [5, 2.5], fray: .4, body: .05 };
  const hardS = crystalSt(3, 10), gap = { skip: true };
  const GATE = [-.16, .16];   // V2's one way through, at the right
  const seg = (a) => { const s = ((a % TAU) + TAU) % TAU; return Math.floor(s / (TAU / 8)); };
  const inGate = (a) => { const s = Math.atan2(Math.sin(a), Math.cos(a)); return s > GATE[0] && s < GATE[1]; };
  const MIXED = [1, 0, 1, 1, 0, 0, 1, 0];
  const hardAt = [() => false, (a) => !inGate(a), (a) => !!MIXED[seg(a)]];
  const styleAt = [() => soft, (a) => (inGate(a) ? gap : hardS), (a) => (MIXED[seg(a)] ? hardS : soft)];
  const P = centres.map(([cx, cy], k) => {
    const ring = strand((u) => [cx + R * Math.cos(TAU * u), cy + R * Math.sin(TAU * u), 0], 200, true, (u) => styleAt[k](TAU * u));
    sample([ring], 0);
    const A = Array.from({ length: 16 }, (_, i) => {
      const inside = i % 2 === 0, a = rnd() * TAU, r = inside ? R * .5 * Math.sqrt(rnd()) : R + 14 + rnd() * 30;
      return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a), vx: 0, vy: 0, r: 3, want: !inside, tx: 0, ty: 0, stuck: 0 };
    });
    return { ring, A, cx, cy };
  });
  const pick = (p, cx, cy) => {   // somewhere on the other side of the ring
    const a = rnd() * TAU, r = p.want ? R * .55 * Math.sqrt(rnd()) : R + 16 + rnd() * 34;
    p.tx = cx + r * Math.cos(a); p.ty = cy + r * Math.sin(a);
  };
  P.forEach(({ A, cx, cy }) => A.forEach((p) => { p.want = !p.want; pick(p, cx, cy); }));
  return {
    W, H, still: 9,
    step(dt, t) {
      P.forEach(({ A, cx, cy }, k) => {
        liquid(A, 8, 12, .2);
        for (const p of A) {
          const dx = p.tx - p.x, dy = p.ty - p.y, d = Math.hypot(dx, dy) || 1;
          if (d < 8) { p.want = !p.want; pick(p, cx, cy); }
          p.vx += dx / d * .05 + (rnd() - .5) * .1; p.vy += dy / d * .05 + (rnd() - .5) * .1;
          if (p.stuck > 0 && k === 1) {   // blocked by a wall: slide along it toward the gate
            const a = Math.atan2(p.y - cy, p.x - cx), dir = Math.sin(a) > 0 ? -1 : 1;
            p.vx += -Math.sin(a) * dir * .08; p.vy += Math.cos(a) * dir * .08; p.stuck -= dt;
          }
          p.vx *= .9; p.vy *= .9;
          const r0 = Math.hypot(p.x - cx, p.y - cy), nx = p.x + p.vx * .5, ny = p.y + p.vy * .5, r1 = Math.hypot(nx - cx, ny - cy);
          const crossing = (r0 - R) * (r1 - R) <= 0 || Math.abs(r1 - R) < 4;
          const a = Math.atan2(ny - cy, nx - cx);
          if (crossing && hardAt[k](a)) {   // hard: it doesn't let work through
            const side = r0 < R ? -1 : 1, rr = R + side * 4.5, ux = (p.x - cx) / (r0 || 1), uy = (p.y - cy) / (r0 || 1);
            p.x = cx + ux * rr; p.y = cy + uy * rr; const vr = p.vx * ux + p.vy * uy; if (vr * side < 0) { p.vx -= vr * ux; p.vy -= vr * uy; } p.stuck = .6;
          } else { p.x = nx; p.y = ny; }
          if (k === 1 && inGate(a) && Math.abs(r1 - R) < 6) { p.vx *= .5; p.vy *= .5; }   // the gate takes one at a time
        }
      });
    },
    draw(g, t) {
      P.forEach(({ ring, A, cx, cy }, k) => {
        runs(g, ring, 0, ring.n);
        if (k === 1) { const [x, y] = [cx + R, cy]; line(g, [[x - 5, y - 10], [x + 5, y - 10]], C.hard, 1.2); line(g, [[x - 5, y + 10], [x + 5, y + 10]], C.hard, 1.2); }
        swarm(g, A, { cell: 2.5, fa: .06, s: 2.9, cache: this['c' + k] || (this['c' + k] = layer()) });
        const labels = [["V1", "all soft: work goes anywhere"], ["V2", "too hard: everything waits at one gate"], ["V3", "hard where it matters, soft elsewhere"]][k];
        if (m) { text(g, 225, cy - 6, labels[0], fs * 1.1, C.ink, "left", 500); labels[1].match(/.{1,22}(\s|$)/g).forEach((l, i) => text(g, 225, cy + 10 + i * 13, l.trim(), fs * .85, C.ink2)); }
        else { text(g, cx, 240, labels[0], fs * 1.05, C.ink, "center", 500); text(g, cx, 255, labels[1], fs * .8, C.ink2, "center"); }
      });
      const moves = m
        ? [[[[215, 150], [250, 200], [215, 250]], "HARDEN", [256, 203]], [[[215, 350], [250, 400], [215, 450]], "SOFTEN", [256, 403]]]
        : [[[[180, 40], [225, 16], [270, 40]], "HARDEN", [225, 10]], [[[410, 40], [455, 16], [500, 40]], "SOFTEN", [455, 10]]];
      moves.forEach(([pts, label, [lx, ly]]) => {
        line(g, pts, C.ink, .6, [3, 3]);
        const [p, q] = pts.slice(-2); arrow(g, q[0], q[1], Math.atan2(q[1] - p[1], q[0] - p[0]), 5, C.ink, .8);
        text(g, lx, ly, label, fs * .85, C.ink, m ? "left" : "center", 500);
      });
    },
  };
}

// ---- wire up ---------------------------------------------------------------------------------------
const FIGS = { hero, see, core, scale, upside, evolve };
window.Tangle = { FIGS, mount };
document.querySelectorAll("canvas[data-fig]").forEach((c) => mount(c, FIGS[c.dataset.fig], { wide: c.dataset.fig === "hero" }));
})();
