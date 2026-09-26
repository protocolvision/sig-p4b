#!/usr/bin/env python3
"""Build the site pages from src/*.html.

Each source file starts with a JSON front-matter comment:
  <!-- {"title": "...", "desc": "...", "path": "about/", "nav": "about", "card": "home"} -->
The body is wrapped in the shared head, header and footer and written to <path>index.html.
Old v1 URLs get redirect stubs. Run tools/build_schedule.py first (it fills src/sessions.html).
"""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://npc.here.now/protocolvision/"
DISCORD = "https://discord.gg/zNJdK7caj"
NAV = [("about", "About", "about/"), ("sessions", "Sessions", "sessions/"),
       ("research", "Research", "research/"), ("play", "Play", "play/")]
REDIRECTS = {"syllabus/": "sessions/", "observations/": "play/watching/",
             "case-studies/": "research/cases/", "simulation/": "play/"}
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Lora:ital,wght@0,400;0,600;1,400&family=Outfit:wght@400;500&display=swap">')

def page(meta, body):
    path = meta["path"]
    rel = "../" * path.count("/")
    a = lambda s: html.escape(s, quote=True)
    title, desc = meta["title"], meta["desc"]
    card = f'{SITE}assets/cards/{meta.get("card", "home")}.jpg'
    nav = "\n".join(
        f'<a href="{rel}{p}"' + (' aria-current="page"' if meta.get("nav") == k else "") + f'>{label}</a>'
        for k, label, p in NAV)
    foot_nav = "".join(f'<a href="{rel}{p}">{label}</a>' for k, label, p in NAV)
    extra_head = meta.get("head", "")
    return f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{a(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Protocol Institute">
<meta property="og:title" content="{a(title)}">
<meta property="og:description" content="{a(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{card}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{a(title)}">
<meta name="twitter:description" content="{a(desc)}">
<meta name="twitter:image" content="{card}">
<link rel="alternate" type="text/plain" title="Summary for language models" href="{rel}llms.txt">
<link rel="icon" href="{rel}favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="{rel}style.css">
{extra_head}<body>
<header>
<a class="home" href="{rel or './'}"><img class="logo" src="{rel}favicon.svg" alt="">Protocol Institute</a>
<nav aria-label="Main">
{nav}
</nav>
</header>
<main>
{body.strip()}
</main>
<footer>
<p><img class="mark" src="{rel}favicon.svg" alt="">Protocols for Business SIG, a research group of the <a href="https://protocol-institute.org/">Protocol Institute</a></p>
<nav>{foot_nav}<a href="https://discord.gg/zNJdK7caj">Discord</a><a href="https://github.com/protocolvision/sig-p4b">Source</a><a href="{rel}llms.txt">llms.txt</a></nav>
</footer>
<script src="{rel}assets/site.js" data-root="{rel or './'}" defer></script>
</body>
</html>
"""

def main():
    built = []
    for src in sorted((ROOT / "src").glob("*.html")):
        text = src.read_text()
        m = re.match(r"\s*<!--\s*(\{.*?\})\s*-->\s*", text, re.S)
        assert m, f"{src.name}: missing front matter"
        meta = json.loads(m.group(1))
        out = ROOT / meta["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(meta, text[m.end():]))
        built.append(meta["path"] or "/")
    for old, new in REDIRECTS.items():
        rel = "../" * old.count("/")
        stub = (f'<!doctype html><meta charset="utf-8"><title>Moved</title>\n'
                f'<meta http-equiv="refresh" content="0; url={rel}{new}">\n'
                f'<link rel="canonical" href="{SITE}{new}">\n'
                f'<p>This page moved to <a href="{rel}{new}">{SITE}{new}</a>.</p>\n')
        (ROOT / old).mkdir(parents=True, exist_ok=True)
        (ROOT / old / "index.html").write_text(stub)
    write_llms()
    print("built:", ", ".join(built), "| redirects:", ", ".join(REDIRECTS), "| llms.txt")

def write_llms():
    """A plain-text summary for language models and agents (llmstxt.org convention)."""
    S = json.loads((ROOT / "sessions.json").read_text())
    upcoming = "\n".join(f"- {s['date']} 15:30–16:30 UTC: {s['title']} ({s['cite']}), {s['url']}" for s in S[:4])
    text = f"""# Protocols for Business SIG

> A research group of the Protocol Institute studying how organizations coordinate through protocols, and what changes as AI agents join the work. Sessions every other Monday, 15:30–16:30 UTC, on the Protocol Institute Discord ({DISCORD}, channel #protocols-for-business), from 2 November 2026 to 1 November 2027. Sessions are recorded. Drop-ins are welcome.

## Pages
- [About]({SITE}about/): method (protocol vision), origins, facilitators, publications
- [Sessions]({SITE}sessions/): joining details, session format, full syllabus with a quote from each reading, archive
- [Research]({SITE}research/): 2027 focus (AI Native Data Operations), research questions, case studies, how to sponsor or partner
- [Case studies]({SITE}research/cases/): water rate data, construction bids from PDFs, the PI brand kit, the case template
- [Protocol Play]({SITE}play/): protocol watching, workshops, simulation
- [Protocol watching guide]({SITE}play/watching/): how to see and record a business protocol

## Data
- [sessions.json]({SITE}sessions.json): all 26 sessions with date, reading, quote, companion essay, and show-and-tell
- [Calendar (.ics)]({SITE}sig-p4b.ics): subscribable; times in UTC

## Next sessions
{upcoming}

## Register for session emails
POST https://sig-p4b-signup.rafaeldf2.workers.dev/signup with Content-Type: application/json.
Body fields: email (required), name, website, github, discord, affiliation. Returns {{"ok": true}}.
Only register a person with their consent. Every email includes an unsubscribe link.

## Contact
- Facilitator: Rafael Fernández, @rafa_0x on Discord
- Sponsorship and research partnerships: https://protocol-institute.org/support and https://protocol-institute.org/contact
- Source: https://github.com/protocolvision/sig-p4b
"""
    (ROOT / "llms.txt").write_text(text)

if __name__ == "__main__":
    main()
