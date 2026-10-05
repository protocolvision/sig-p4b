"""A small drafting kit for the site's figures: hairline weights, construction and centre lines,
dimension lines with architectural ticks, numbered callouts, section hatching, axonometric
projection and a title block. Every figure in tools/make_figures.py is drawn with these, so the
whole site shares one drawing-sheet language."""
import math

INK, COBALT, MUTED, FAINT, PAPER = "#262624", "#004fcc", "#6b6a66", "#c9c7c0", "#ffffff"
HAIR, FINE, MEDIUM, HEAVY = .5, .75, 1.1, 1.8   # line weights, as on a drawing sheet
MONO = "ui-monospace, 'IBM Plex Mono', Menlo, monospace"


def f(x):
    return f"{x:.1f}"


class Sheet:
    def __init__(self, w, h, label):
        self.w, self.h, self.label, self.out, self.defs = w, h, label, [], []
        self._hatch_ids = {}
        self.ts = 1.0   # text scale, for figures shown small (such as in the blyg's narrow column)

    # --- primitives ---------------------------------------------------------------------------
    def line(self, x1, y1, x2, y2, col=INK, sw=HAIR, dash=None, op=1):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' opacity="{op}"' if op != 1 else ""
        self.out.append(f'<path d="M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}" stroke="{col}" stroke-width="{sw}"{d}{o}/>')

    def path(self, pts, col=INK, sw=HAIR, dash=None, close=False, fill="none", op=1):
        if not pts:
            return
        d = "M" + "L".join(f"{f(x)} {f(y)}" for x, y in pts) + ("Z" if close else "")
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' opacity="{op}"' if op != 1 else ""
        self.out.append(f'<path d="{d}" stroke="{col}" stroke-width="{sw}" fill="{fill}"{ds}{o}/>')

    def circle(self, x, y, r, col=INK, sw=HAIR, fill="none", dash=None, op=1):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' opacity="{op}"' if op != 1 else ""
        self.out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" stroke="{col}" stroke-width="{sw}" fill="{fill}"{ds}{o}/>')

    def dot(self, x, y, r=1.4, col=INK, op=1):
        o = f' opacity="{op}"' if op != 1 else ""
        self.out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{col}" stroke="none"{o}/>')

    def rect(self, x, y, w, h, col=INK, sw=HAIR, fill="none", dash=None):
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.out.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" stroke="{col}" stroke-width="{sw}" fill="{fill}"{ds}/>')

    def text(self, x, y, s, size=9, col=INK, anchor="start", weight=400, spacing=.6):
        if self.ts != 1:
            size = round(size * self.ts, 2)
        self.out.append(f'<text x="{f(x)}" y="{f(y)}" font-family="{MONO}" font-size="{size}" font-weight="{weight}" '
                        f'letter-spacing="{spacing}" fill="{col}" text-anchor="{anchor}" stroke="none">{s}</text>')

    # --- drafting conventions -------------------------------------------------------------------
    def centerline(self, x1, y1, x2, y2, col=MUTED):
        self.line(x1, y1, x2, y2, col, HAIR, "14 3 2 3")

    def construction(self, x1, y1, x2, y2):
        self.line(x1, y1, x2, y2, FAINT, HAIR, "1 3")

    def tick(self, x, y, size=4, col=INK):
        """An architectural slash tick, used at the ends of dimension lines."""
        self.line(x - size, y + size, x + size, y - size, col, FINE)

    def dim(self, x1, y1, x2, y2, label, off=14, col=INK):
        """A dimension line parallel to (x1,y1)-(x2,y2), offset by `off`, with extension lines and ticks."""
        a = math.atan2(y2 - y1, x2 - x1); nx, ny = -math.sin(a) * off, math.cos(a) * off
        ax, ay, bx, by = x1 + nx, y1 + ny, x2 + nx, y2 + ny
        ext = 3 * (1 if off > 0 else -1)
        self.line(x1 + nx * .15, y1 + ny * .15, ax - math.sin(a) * ext, ay + math.cos(a) * ext, col, HAIR)
        self.line(x2 + nx * .15, y2 + ny * .15, bx - math.sin(a) * ext, by + math.cos(a) * ext, col, HAIR)
        self.line(ax, ay, bx, by, col, HAIR)
        self.tick(ax, ay, 3.5, col); self.tick(bx, by, 3.5, col)
        mx, my = (ax + bx) / 2, (ay + by) / 2
        deg = math.degrees(a)
        if 90 < abs(deg):
            deg += 180
        self.out.append(f'<text x="{f(mx)}" y="{f(my - 4)}" font-family="{MONO}" font-size="8.5" letter-spacing=".6" fill="{col}" '
                        f'text-anchor="middle" stroke="none" transform="rotate({deg:.1f} {f(mx)} {f(my)})">{label}</text>')

    def callout(self, x, y, n, bx, by, col=INK, note=None):
        """A numbered bubble at (bx,by) with a leader to the point (x,y), and an optional note beside it."""
        self.line(bx, by, x, y, col, HAIR)
        self.dot(x, y, 1.6, col)
        self.circle(bx, by, 7.5, col, FINE, fill=PAPER)
        self.text(bx, by + 3, str(n), 8.5, col, "middle", 500, 0)
        if note:
            right = bx >= x
            self.text(bx + (11 if right else -11), by + 3, note, 8.5, col, "start" if right else "end")

    def hatch(self, spacing=5, angle=45, col=INK, sw=HAIR):
        key = (spacing, angle, col, sw)
        if key not in self._hatch_ids:
            pid = f"h{len(self._hatch_ids)}"
            self._hatch_ids[key] = pid
            self.defs.append(f'<pattern id="{pid}" width="{spacing}" height="{spacing}" patternUnits="userSpaceOnUse" '
                             f'patternTransform="rotate({angle})"><line x1="0" y1="0" x2="0" y2="{spacing}" stroke="{col}" stroke-width="{sw}"/></pattern>')
        return f"url(#{self._hatch_ids[key]})"

    def arrow(self, x, y, ang, size=6, col=INK, sw=FINE):
        for s in (-1, 1):
            self.line(x, y, x - size * math.cos(ang + s * .45), y - size * math.sin(ang + s * .45), col, sw)

    def frame(self, number, title, scale="NTS"):
        """A hairline border with corner ticks and a small title block, bottom right."""
        w, h, m = self.w, self.h, 6
        self.ts = 1.0
        self.rect(m, m, w - 2 * m, h - 2 * m, FAINT, HAIR)
        for cx, cy, sx, sy in ((m, m, 1, 1), (w - m, m, -1, 1), (m, h - m, 1, -1), (w - m, h - m, -1, -1)):
            self.line(cx, cy, cx + 10 * sx, cy, INK, FINE); self.line(cx, cy, cx, cy + 10 * sy, INK, FINE)
        tw = max(150, 7 * (len(title) + 14))
        x0, y0 = w - m - tw, h - m - 16
        self.rect(x0, y0, tw, 16, INK, HAIR, fill=PAPER)
        self.line(x0 + 54, y0, x0 + 54, y0 + 16, INK, HAIR)
        self.line(x0 + tw - 38, y0, x0 + tw - 38, y0 + 16, INK, HAIR)
        self.text(x0 + 6, y0 + 11, f"FIG {number:02d}", 7.5, INK, weight=500)
        self.text(x0 + 60, y0 + 11, title.upper(), 7.5, INK)
        self.text(x0 + tw - 32, y0 + 11, scale, 7.5, MUTED)

    def svg(self):
        defs = f"<defs>{''.join(self.defs)}</defs>" if self.defs else ""
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
                f'role="img" aria-label="{self.label}">{defs}<g fill="none" stroke-linecap="round" stroke-linejoin="round">'
                + "".join(self.out) + "</g></svg>\n")


def iso(x, y, z, ox, oy, s=1.0):
    """Isometric projection (30°) of a point, scaled by s and placed at (ox, oy)."""
    c, sn = math.cos(math.pi / 6), math.sin(math.pi / 6)
    return ox + (x - y) * c * s, oy + (x + y) * sn * s - z * s
