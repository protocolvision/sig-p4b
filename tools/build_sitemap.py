#!/usr/bin/env python3
"""Write sitemap.xml and robots.txt for every indexable page (run after build_site.py and build_blyg.py).

Skips redirect stubs, noindex pages (hype/, unsubscribe/) and the draft 3D map. URLs come from config.json,
so moving to a new domain only needs the "site" value changed.
"""
import json, re, subprocess
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
SITE = json.loads((ROOT / "config.json").read_text())["site"]
SKIP_DIRS = {".git", "drafts", "src", "tools", "worker", "site", "dist", "sources", "ops", "blyg-src", "hype", "node_modules"}

def indexable(f):
    head = f.read_text(errors="ignore")[:6000]
    return not re.search(r'http-equiv="refresh"|name="robots" content="[^"]*noindex', head)

def lastmod(f):
    m = re.search(r'property="article:modified_time" content="([^"]+)"', f.read_text(errors="ignore")[:8000])
    if m:
        return m.group(1)
    return subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%cs", "--", str(f)],
                          capture_output=True, text=True).stdout.strip()

def main():
    urls = []
    for f in sorted(ROOT.rglob("index.html")):
        rel = f.relative_to(ROOT)
        if set(rel.parts) & SKIP_DIRS or rel.parts[:3] == ("sessions", "map", "3d") or not indexable(f):
            continue
        path = "" if rel.parent == Path(".") else rel.parent.as_posix() + "/"
        urls.append((SITE + path, lastmod(f)))
    urls.sort(key=lambda u: (u[0].count("/"), u[0]))
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{escape(u)}</loc>" + (f"<lastmod>{d}</lastmod>" if d else "") + "</url>\n" for u, d in urls)
        + "</urlset>\n")
    # robots.txt only counts at a host's root, so it takes effect once the site has its own domain.
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n")
    print(f"sitemap.xml: {len(urls)} URLs | robots.txt")

if __name__ == "__main__":
    main()
