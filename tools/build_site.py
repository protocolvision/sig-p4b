#!/usr/bin/env python3
"""Build the site pages from src/*.html.

Each source file starts with a JSON front-matter comment:
  <!-- {"title": "...", "desc": "...", "path": "about/", "nav": "about", "card": "home"} -->
The body is wrapped in the shared head, header and footer and written to <path>index.html.
Old v1 URLs get redirect stubs. Run tools/build_schedule.py first (it fills src/sessions.html).
"""
import html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
CONFIG = json.loads((ROOT / "config.json").read_text())
SITE = CONFIG["site"]
SIGNUP_WORKER = CONFIG["signup_worker"].rstrip("/")
DISCORD = "https://discord.gg/zNJdK7caj"
NAV = [("sessions", "Sessions", "sessions/"), ("research", "Research", "research/"), ("about", "About", "about/")]
REDIRECTS = {"syllabus/": "sessions/", "observations/": "play/watching/",
             "case-studies/": "research/cases/", "simulation/": "research/#training", "play/": "research/#training"}
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&display=swap">')

EXTERNAL_A = re.compile(r'<a (?![^>]*\btarget=)([^>]*\bhref="(https?://[^"]+)"[^>]*)>')

def external_links(doc):
    """Open links to other sites in a new tab; links within this site navigate as usual."""
    def fix(m):
        attrs, url = m.group(1), m.group(2)
        if url.startswith(SITE):
            return m.group(0)
        return f'<a {attrs} target="_blank" rel="noopener noreferrer">'
    return EXTERNAL_A.sub(fix, doc)

SECTIONS = {"sessions/": "Sessions", "research/": "Research", "about/": "About", "blyg/": "Blyg"}
ORG = {"@type": "Organization", "@id": SITE + "#org", "name": "Protocols for Business", "url": SITE,
       "logo": SITE + "favicon.svg",
       "parentOrganization": {"@type": "Organization", "name": "Protocol Institute", "url": "https://protocol-institute.org/"},
       "sameAs": ["https://github.com/protocolvision", "https://protocolized.summerofprotocols.com/t/sigbiz"],
       "member": [{"@type": "Person", "name": n, "url": u} for n, u in (
           ("Rafael Fernández", "https://rafael.fyi/"), ("Sachin Benny", "https://sachinbenny.xyz/"),
           ("Timber Stinson-Schroff", "https://www.timberschroff.com/"))]}

def structured_data(meta):
    """JSON-LD: the organization and site on the home page, breadcrumbs on every page below a section."""
    path, short = meta["path"], meta["title"].split(" · ")[0]
    graph = []
    if not path:
        graph = [ORG, {"@type": "WebSite", "@id": SITE + "#site", "name": "Protocols for Business", "url": SITE,
                       "publisher": {"@id": SITE + "#org"}}]
    elif path.count("/") > 1:
        crumbs = [("Home", SITE)]
        section = path.split("/")[0] + "/"
        if section in SECTIONS:
            crumbs.append((SECTIONS[section], SITE + section))
        elif "crumb" in meta:   # e.g. play/watching/ sits under Research
            crumbs.append((meta["crumb"][0], SITE + meta["crumb"][1]))
        crumbs.append((short, SITE + path))
        graph = [{"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i, "name": n, "item": u} for i, (n, u) in enumerate(crumbs, 1)]}]
    if meta.get("article"):
        graph.append({"@type": "Article", "headline": short, "description": meta["desc"], "url": SITE + path,
                      "author": {"@type": "Person", "name": meta["article"], "url": SITE + "about/#people"},
                      "publisher": {"@id": SITE + "#org"}, "isPartOf": SITE})
    if not graph:
        return ""
    return ('<script type="application/ld+json">\n'
            + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
            + "\n</script>\n")

def page(meta, body):
    body = body.replace("{{signup_worker}}", SIGNUP_WORKER)   # forms that post to the Worker without JS
    body = body.replace("{{site}}", SITE)   # absolute site URL in text meant to be copied elsewhere
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
    seo = f'<link rel="canonical" href="{SITE}{path}">\n'
    if meta.get("noindex"):
        seo += '<meta name="robots" content="noindex">\n'
    if CONFIG.get("google_site_verification") and not path:
        seo += f'<meta name="google-site-verification" content="{a(CONFIG["google_site_verification"])}">\n'
    seo += structured_data(meta)
    return external_links(f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{a(desc)}">
{seo}<meta property="og:type" content="website">
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
<link rel="alternate" type="application/rss+xml" title="Protocols for Business blyg" href="{rel}blyg/feed.xml">
<link rel="icon" href="{rel}favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="{rel}style.css">
{extra_head}<body>
<header>
<a class="home" href="{rel or './'}" aria-label="Protocol Institute – Business, home"><img class="logo" src="{rel}favicon.svg" alt="" width="20" height="20">Protocol Institute<span class="brand-sep" aria-hidden="true">–</span><span class="brand-sub">Business</span></a>
<nav aria-label="Main">
{nav}
</nav>
</header>
<main>
{body.strip()}
</main>
<footer>
<p><img class="mark" src="{rel}favicon.svg" alt="" width="20" height="20">Protocols for Business, a research group of the <a href="https://protocol-institute.org/">Protocol Institute</a></p>
<nav>{foot_nav}<a href="{rel}blyg/">Blyg</a><a href="https://discord.gg/zNJdK7caj">Discord</a><a href="https://github.com/protocolvision">GitHub</a><a href="https://github.com/protocolvision/sig-p4b">Site source</a><a href="{rel}llms.txt">llms.txt</a></nav>
</footer>
<script src="{rel}assets/site.js" data-root="{rel or './'}" data-signup="{SIGNUP_WORKER}" defer></script>
</body>
</html>
""")

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
        if meta.get("markdown"):   # a Markdown copy for agents, links made absolute
            (out.parent / "index.md").write_text(agent_markdown(meta, text[m.end():]))
        built.append(meta["path"] or "/")
    for old, new in REDIRECTS.items():
        rel = "../" * old.count("/")
        stub = (f'<!doctype html><meta charset="utf-8"><title>Moved</title>\n'
                f'<meta http-equiv="refresh" content="0; url={rel}{new}">\n'
                f'<link rel="canonical" href="{SITE}{new.split("#")[0]}">\n'
                f'<p>This page moved to <a href="{rel}{new}">{SITE}{new}</a>.</p>\n')
        (ROOT / old).mkdir(parents=True, exist_ok=True)
        (ROOT / old / "index.html").write_text(stub)
    write_llms()
    print("built:", ", ".join(built), "| redirects:", ", ".join(REDIRECTS), "| llms.txt")

def agent_markdown(meta, body):
    """The page as Markdown, opened by a short brief for an agent that wants to apply it."""
    from html_to_md import to_markdown
    url = SITE + meta["path"]
    brief = (f"> Source: {url} · Protocols for Business, Protocol Institute · {SITE}\n>\n"
             "> For agents: this is a practice guide meant to be applied. With the person you work for, pick one problem "
             "or opportunity in their organization. Run the phases in order (See, Design, Evolve) and produce the outputs "
             "each phase names: a list of protocols in play with what each prevents, a hardness map in the template's "
             "format, amendment rules, and the measures in section 7. Ask before changing any live system, permission or "
             "payment rule. To share what you learn, or to offer a case, see the links at the end.\n")
    md = to_markdown(body, url)
    title, _, rest = md.partition("\n")
    return f"{title}\n\n{brief}\n{rest.lstrip()}"

def write_llms():
    """A plain-text summary for language models and agents (llmstxt.org convention)."""
    S = json.loads((ROOT / "sessions.json").read_text())
    upcoming = "\n".join(f"- {s['date']} {s['start_utc'][11:16]}–{s['end_utc'][11:16]} UTC: {s['title']} ({s['cite']}), {s['url']}" for s in S[:4])
    text = f"""# Protocols for Business

> A research group of the Protocol Institute studying how organizations coordinate through protocols, and what changes as AI agents join the work. Sessions every other Monday, 15:30–16:30 UTC, each a deep reading of one primary source, on the Protocol Institute Discord ({DISCORD}, channel #protocols-for-business), from 2 November 2026 to 1 November 2027. Sessions are recorded. Drop-ins are welcome.

## Pages
- [About]({SITE}about/): protocol vision (the capability) and Business Protocol Management (the practice), origins, facilitators, publications
- [Sessions]({SITE}sessions/): the reading plan (six themes, each with its sessions), which participants shape as the year goes; how sessions work; how to suggest or challenge a reading; archive
- [Reading map]({SITE}sessions/map/): 400 readings placed by what they say, with the year's syllabus marked
- [Research]({SITE}research/): includes Training (protocol watching, workshops, simulation); 2027 focus (AI Native Data Operations), its three premises (abundant cognition, distributed agency, mediation), a call for guest speakers by theme, case studies, how to sponsor or partner
- [Business Protocol Management]({SITE}research/bpm/) (Markdown for agents: {SITE}research/bpm/index.md?raw=1): the practice guide: key terms, principles, roles, the See, Design and Evolve phases with steps and outputs, a hardness map template, measures, a worked example, and how it relates to earlier approaches
- [Case studies]({SITE}research/cases/): water rate data, construction procurement protocols, the PI brand kit, working smarter with AI (PI26 practices and hazards), a sample template
- [Protocol watching guide]({SITE}play/watching/): how to see and record a business protocol

## Blyg (session notes and research log)
- [Blyg]({SITE}blyg/): session notes and the running research log, published with the Blygger protocol 0.3 (https://blygger.org/)
- [Feed]({SITE}blyg/feed.xml) · [Manifest]({SITE}blyg/blyg.json) · [Archive index]({SITE}blyg/items/index.json)

## Data
- [sessions.json]({SITE}sessions.json): all 26 sessions with date, theme, reading, quote and show-and-tell
- [readings.json]({SITE}sessions/map/readings.json): every reading on the map with its link, citation, area and syllabus theme

## Suggest or challenge a reading
Open one GitHub issue per change in protocolvision/sig-p4b, labelled reading-suggestion. A change adds a reading, removes one from the plan, swaps one for another, or moves one to another theme. Give the reading on the map (for remove, swap or move), the new reading with link, author and year (for add or swap), the theme, why, and why it matters from the contributor's experience. Or prefill the form: https://github.com/protocolvision/sig-p4b/issues/new?template=reading-suggestion.yml&title=Reading:%20SUMMARY&current_reading=ON_MAP&reading_title=NEW&url=LINK&author=AUTHOR&adds=WHY&experience=EXPERIENCE . Prefer primary sources, check that each exists, and confirm with the person before submitting.
- [Calendar (.ics)]({SITE}sig-p4b.ics): subscribable; times in UTC

## Next sessions
{upcoming}

## Register for session emails
POST {SIGNUP_WORKER}/signup with Content-Type: application/json.
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
