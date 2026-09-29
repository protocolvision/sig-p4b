#!/usr/bin/env python3
"""Build everything schedule-related from tools/themes.json and tools/slots.json.

- tools/themes.json: the syllabus as six themes, each with its readings in order of exploration
  (a reading marked "companion" is read alongside the one before it, not in its own session)
- tools/slots.json: the 26 session dates, each with its show-and-tell or guest
- src/sessions.html: a summary of the themes with sample readings (between the schedule markers)
- sessions.json: public per-session data; sig-p4b.ics: the subscribable calendar (15:30-16:30 UTC)

Edit themes.json or slots.json, run this script, then ./deploy.sh.
"""
import html, json, re, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tools/themes.json").read_text())
SLOTS = json.loads((ROOT / "tools/slots.json").read_text())
S = []
for t in T["themes"]:
    for r in t["readings"]:
        if r.get("companion") and S:
            S[-1]["also_read"] = r
            continue
        S.append({"theme": f'{t["n"]}. {t["name"]}', "theme_blurb": t["blurb"], "title": r["title"], "url": r["url"],
                  "cite": r["cite"], "quote": r.get("quote", "")})
assert len(S) == len(SLOTS), f"{len(S)} sessions but {len(SLOTS)} dates in slots.json"
for s, slot in zip(S, SLOTS):
    s.update(slot)
e = lambda s: html.escape(s, quote=False)
ea = lambda s: html.escape(s, quote=True)
label = lambda d: f"{int(d[8:])} {dt.date.fromisoformat(d).strftime('%B %Y')}"
DISCORD = "https://discord.gg/zNJdK7caj"
SITE = json.loads((Path(__file__).resolve().parent.parent / "config.json").read_text())["site"]

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

# --- syllabus summary (src/sessions.html): themes in order of exploration, with sample readings ---
out = [f'<p>{e(T["summary"])}</p>', '<ol class="theme-grid" role="list">']
k = 0
for i, t in enumerate(T["themes"], 1):
    n = sum(1 for r in t["readings"] if not r.get("companion"))
    sessions = S[k:k + n]
    k += n
    guests = [re.match(r"Guest: (.*?) \((.*)\)", s["feature"]) for s in sessions]
    guests = [g for g in guests if g]
    guest = f'<p class="guest"><span class="kind">Guest</span> {e(guests[0].group(1))}</p>' if guests else ""
    readings = "".join(f'<li><a href="{ea(r["url"])}">{e(r["title"])}</a> <span class="muted">{e(r["cite"])}'
                       + (" · read alongside the previous reading" if r.get("companion") else "") + "</span></li>"
                       for r in t["readings"])
    out.append(f'<li class="theme-card" id="theme-{t["n"].lower()}">'
               f'<img src="../assets/themes/theme-{i}.svg" alt="" width="320" height="140" loading="lazy">'
               f'<h3><span class="n">{e(t["n"])}</span> {e(t["name"])}</h3>'
               f'<p>{e(t["blurb"])}</p>{guest}'
               f'<details class="samples"><summary><span class="meta">{n} sessions</span>'
               f'<span class="ic-wrap"><svg class="ic" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5zM4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg><svg class="chev" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span class="visually-hidden">, show the readings</span></summary>'
               f'<ol class="sample">{readings}</ol></details></li>')
out.append("</ol>")
out.append('<p class="map-cta"><a class="btn" href="map/">Explore every reading on the map</a> '
           '<span class="small muted">All 27 syllabus readings among 400 related works, with the full schedule by date.</span></p>')
p = ROOT / "src/sessions.html"
p.write_text(replace_between(p.read_text(), "schedule", "\n".join(out)))

# --- structured data (schema.org) on the sessions page ---
events = [{"@type": "Event", "name": f"SIG P4B · {s['title']}",
           "startDate": f"{s['date']}T15:30:00Z", "endDate": f"{s['date']}T16:30:00Z",
           "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
           "eventStatus": "https://schema.org/EventScheduled",
           "location": {"@type": "VirtualLocation", "url": DISCORD},
           "about": {"@type": "CreativeWork", "name": s["title"], "url": s["url"]},
           "description": f"Theme {s['theme']}. {s['theme_blurb']} Show-and-tell: {s['feature']}.",
           "organizer": {"@type": "Organization", "name": "Protocol Institute", "url": "https://protocol-institute.org/"},
           "isAccessibleForFree": True} for s in S]
series = {"@context": "https://schema.org", "@type": "EventSeries",
          "name": "Protocols for Business SIG sessions", "url": SITE + "sessions/",
          "startDate": S[0]["date"], "endDate": S[-1]["date"], "subEvent": events}
p = ROOT / "src/sessions.html"
p.write_text(replace_between(p.read_text(), "jsonld",
    '<script type="application/ld+json">\n' + json.dumps(series, ensure_ascii=False, indent=1) + "\n</script>"))

# --- public session data ---
public = [{"date": s["date"], "start_utc": f"{s['date']}T15:30:00Z", "end_utc": f"{s['date']}T16:30:00Z",
           "theme": s["theme"], "title": s["title"], "url": s["url"], "cite": s["cite"], "quote": s["quote"],
           **({"also_read": {k: s["also_read"][k] for k in ("title", "url", "cite")}} if s.get("also_read") else {}),
           "feature": s["feature"], "feature_short": short_feature(s["feature"])} for s in S]
(ROOT / "sessions.json").write_text(json.dumps(public, ensure_ascii=False, indent=1) + "\n")

# --- homepage (v1 layouts only) ---
p = ROOT / "index.html"
t = p.read_text()
if "<!-- schedule:start -->" in t:
    home = [f'  <li><time datetime="{s["date"]}">{label(s["date"])}</time><span class="what">'
            f'<a href="{ea(s["url"])}">{e(s["title"])}</a> <span class="muted">· {e(short_feature(s["feature"]))}</span></span></li>' for s in S]
    p.write_text(replace_between(t, "schedule", '<ul class="schedule">\n' + "\n".join(home) + "\n</ul>"))

# --- calendar ---
def esc(s): return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")
def fold(line):
    out, b = [], line.encode()
    while len(b) > 74:
        cut = 74
        while (b[cut] & 0xC0) == 0x80: cut -= 1
        out.append(b[:cut].decode()); b = b" " + b[cut:]
    out.append(b.decode()); return "\r\n".join(out)
# DTSTAMP: last change to the schedule data, so rebuilding doesn't churn the calendar file.
import subprocess
_iso = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%cI", "--", "tools/sessions.json"],
                      capture_output=True, text=True).stdout.strip()
_iso = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%cI", "--", "tools/themes.json", "tools/slots.json"],
                      capture_output=True, text=True).stdout.strip() or _iso
stamp = (dt.datetime.fromisoformat(_iso).astimezone(dt.timezone.utc) if _iso else dt.datetime(2026, 9, 27, tzinfo=dt.timezone.utc)).strftime("%Y%m%dT%H%M%SZ")
L = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Protocol Institute//SIG P4B//EN", "CALSCALE:GREGORIAN",
     "METHOD:PUBLISH", "X-WR-CALNAME:Protocols for Business SIG",
     "X-WR-CALDESC:Biweekly sessions of the Protocol Institute's Protocols for Business SIG"]
for s in S:
    d = s["date"].replace("-", "")
    desc = (f"Theme {s['theme']}\n\nReading: {s['title']} ({s['cite']})\n{s['url']}\n"
            + (f"\u201c{s['quote']}\u201d\n" if s["quote"] else "")
            + (f"\nAlongside: {s['also_read']['title']} ({s['also_read']['cite']})\n{s['also_read']['url']}\n" if s.get("also_read") else "")
            + f"\nFeature: {s['feature']}\n\nJoin on the Protocol Institute Discord: {DISCORD}\n"
            f"Syllabus: {SITE}sessions/\nReading map: {SITE}sessions/map/\nSessions are recorded.")
    L += ["BEGIN:VEVENT", f"UID:sig-p4b-{d}@protocol-institute", f"DTSTAMP:{stamp}",
          f"DTSTART:{d}T153000Z", f"DTEND:{d}T163000Z",
          fold("SUMMARY:" + esc(f"SIG P4B · {s['title']}")), fold("DESCRIPTION:" + esc(desc)),
          fold("LOCATION:" + esc("Protocol Institute Discord · " + DISCORD)), f"URL:{SITE}", "END:VEVENT"]
L.append("END:VCALENDAR")
(ROOT / "sig-p4b.ics").write_text("\r\n".join(L) + "\r\n")
print(f"{len(T['themes'])} themes, {len(S)} sessions -> src/sessions.html, sessions.json, sig-p4b.ics")
