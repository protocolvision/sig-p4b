"""Build the public web page of the interactive report for protocolsforbusiness.com/agentcontrolreport2026/.

Same content as the artifact (interactive-src.html with data/map.json inlined), except the meeting box: the website keeps the meeting drawer (posts to the sign-up Worker’s /interest route), the artifact keeps a link to it; wrapped in a full HTML document
with the site's canonical address, description and social tags. Writes <out>/index.html and copies the fonts.
Usage: python3 build_site_page.py <out_dir>
"""
import pathlib, re, shutil, sys

HERE = pathlib.Path(__file__).resolve().parent
URL = "https://protocolsforbusiness.com/agentcontrolreport2026/"
DESC = ("Who owns the rules when AI agents join the business? Desk research on 118,526 job postings, company filings, "
        "practitioner recordings, laws and 31 agent products. Protocols for Business, October 2026.")

def build(out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    body = (HERE / "interactive-src.html").read_text().replace("/*MAP*/", (HERE / "data/map.json").read_text())
    # website version: keep the meeting form, drop the artifact-only link
    body = re.sub(r"<!--ARTIFACT-->.*?<!--/ARTIFACT-->", "", body, flags=re.S).replace("<!--SITE-->", "").replace("<!--/SITE-->", "")
    title_end = body.index("</title>") + len("</title>")
    title, rest = body[:title_end], body[title_end:]
    head = "\n".join([
        "<!doctype html>", '<html lang="en">', "<head>", '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
        title.replace("<title>Who Owns the Rules</title>", "<title>Who Owns the Rules · AI agent control report 2026</title>"),
        f'<meta name="description" content="{DESC}">', f'<link rel="canonical" href="{URL}">',
        '<meta property="og:type" content="article">', '<meta property="og:title" content="Who owns the rules when agents join the business?">',
        f'<meta property="og:description" content="{DESC}">', f'<meta property="og:url" content="{URL}">',
        '<meta name="twitter:card" content="summary">',
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">',
    ])
    # split the source's head material (links, style) from the body: the body starts at the hidden SVG pattern defs
    i = rest.index('<svg width="0"')
    html = head + rest[:i] + "</head>\n<body>\n" + rest[i:] + "\n</body>\n</html>\n"
    (out / "index.html").write_text(html)
    (out / "fonts").mkdir(exist_ok=True)
    for f in ("jetbrains-mono-latin-400.woff2", "jetbrains-mono-latin-500.woff2", "OFL.txt"):
        shutil.copy(HERE / "fonts" / f, out / "fonts" / f)
    print("wrote", out / "index.html")

if __name__ == "__main__":
    build(sys.argv[1])
