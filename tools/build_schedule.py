#!/usr/bin/env python3
"""Build everything schedule-related from tools/sessions.json.

- syllabus/index.html: the movements, topics and sessions (between the schedule markers)
- index.html: the homepage schedule list and the "Next session" data
- sig-p4b.ics: subscribable calendar, sessions fixed at 15:30-16:30 UTC

Edit sessions.json, run this script, then ./deploy.sh.
"""
import html, json, re, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
S = json.loads((ROOT / "tools/sessions.json").read_text())
e = lambda s: html.escape(s, quote=False)
ea = lambda s: html.escape(s, quote=True)
label = lambda d: f"{int(d[8:])} {dt.date.fromisoformat(d).strftime('%B %Y')}"
DISCORD = "https://discord.gg/zNJdK7caj"
SITE = "https://npc.here.now/protocolvision/"

def short_feature(f):
    m = re.match(r"Guest: (.*?) \(", f)
    if m: return "Guest: " + m.group(1)
    if f.startswith("Show-and-tell"): return "Show-and-tell"
    if f.startswith("Cognitive Ergonomics"): return "Cognitive Ergonomics project"
    return f.split(":")[0]

def replace_between(text, name, body):
    pat = re.compile(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)", re.S)
    assert pat.search(text), f"missing markers for {name}"
    return pat.sub(lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), text)

# --- syllabus ---
out, movement = [], None
for s in S:
    if s["movement"] != movement:
        if movement: out.append(f'<p class="claim"><span class="kind">What we now see</span><br>{e(prev_claim)}</p>')
        movement = s["movement"]; prev_claim = s["movement_claim"]
        out.append(f'<h3>{e(movement)}</h3>')
    if s["first_in_topic"]:
        if out[-1].endswith("</li>"): out.append("</ul>")
        out.append(f'<p class="topic"><strong>{e(s["topic"])}.</strong> {e(s["topic_line"])} '
                   f'<span class="muted">Alongside: <a href="{ea(s["pi_url"])}">{e(s["pi_title"])}</a> ({e(s["pi_cite"])})</span></p>')
        out.append('<ul class="schedule">')
    extra = ""
    if s.get("also_read"):
        a = s["also_read"]
        extra = (f'<br>\n    <span class="kind">with</span> <a href="{ea(a["url"])}">{e(a["title"])}</a> <span class="muted">{e(a["cite"])}</span>')
    quotes = f'<q>{e(s["quote"])}</q>'
    if s.get("also_read"):
        quotes += f' <q>{e(s["also_read"]["quote"])}</q>'
    out.append(f'  <li><time datetime="{s["date"]}">{label(s["date"])}</time>\n'
               f'    <span class="what"><a href="{ea(s["url"])}">{e(s["title"])}</a> <span class="muted">{e(s["cite"])}</span>{extra}<br>\n'
               f'    <span class="kind">feature</span> <span class="muted">{e(s["feature"])}</span></span>\n'
               f'    <span class="also quote">{quotes}</span></li>')
out.append("</ul>")
out.append(f'<p class="claim"><span class="kind">What we now see</span><br>{e(prev_claim)}</p>')
p = ROOT / "syllabus/index.html"
p.write_text(replace_between(p.read_text(), "schedule", "\n".join(out)))

# --- homepage ---
home = [f'  <li><time datetime="{s["date"]}">{label(s["date"])}</time><span class="what">'
        f'<a href="{ea(s["url"])}">{e(s["title"])}</a> <span class="muted">· {e(short_feature(s["feature"]))}</span></span></li>'
        for s in S]
p = ROOT / "index.html"
t = p.read_text()
if "<!-- schedule:start -->" in t:  # homepage list was removed in v1; kept for older layouts
    t = replace_between(t, "schedule", '<ul class="schedule">\n' + "\n".join(home) + "\n</ul>")
slim = [{k: s[k] for k in ("date", "title", "url", "cite", "feature")} for s in S]
t = re.sub(r'(<script id="sessions" type="application/json">).*?(</script>)',
           lambda m: m.group(1) + json.dumps(slim, ensure_ascii=False) + m.group(2), t, flags=re.S)
p.write_text(t)

# --- calendar ---
def esc(s): return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")
def fold(line):
    out, b = [], line.encode()
    while len(b) > 74:
        cut = 74
        while (b[cut] & 0xC0) == 0x80: cut -= 1
        out.append(b[:cut].decode()); b = b" " + b[cut:]
    out.append(b.decode()); return "\r\n".join(out)
stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Protocol Institute//SIG P4B//EN", "CALSCALE:GREGORIAN",
     "METHOD:PUBLISH", "X-WR-CALNAME:Protocols for Business SIG",
     "X-WR-CALDESC:Biweekly sessions of the Protocol Institute's Protocols for Business SIG"]
for s in S:
    d = s["date"].replace("-", "")
    desc = (f"{s['topic']}: {s['topic_line']}\n\nReading: {s['title']} ({s['cite']})\n{s['url']}\n\u201c{s['quote']}\u201d\n\n"
            f"Alongside: {s['pi_title']} ({s['pi_cite']})\n{s['pi_url']}\n\nFeature: {s['feature']}\n\n"
            f"Join on the Protocol Institute Discord: {DISCORD}\nSyllabus: {SITE}syllabus/\nSessions are recorded.")
    L += ["BEGIN:VEVENT", f"UID:sig-p4b-{d}@protocol-institute", f"DTSTAMP:{stamp}",
          f"DTSTART:{d}T153000Z", f"DTEND:{d}T163000Z",
          fold("SUMMARY:" + esc(f"SIG P4B · {s['title']}")), fold("DESCRIPTION:" + esc(desc)),
          fold("LOCATION:" + esc("Protocol Institute Discord · " + DISCORD)), f"URL:{SITE}", "END:VEVENT"]
L.append("END:VCALENDAR")
(ROOT / "sig-p4b.ics").write_text("\r\n".join(L) + "\r\n")
print(f"{len(S)} sessions -> syllabus, homepage, sig-p4b.ics")
