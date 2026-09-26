#!/usr/bin/env python3
"""Build the session calendar from tools/sessions.json.

Writes sig-p4b.ics (subscribable, times in UTC) and refreshes the embedded
session list the homepage uses for its "Next session" box.
Sessions are fixed at 15:30-16:30 UTC; calendar apps show local time.
"""
import json, re, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SESSIONS = json.loads((ROOT / "tools/sessions.json").read_text())
START, END = "153000Z", "163000Z"
DISCORD = "https://discord.gg/zNJdK7caj"
SITE = "https://npc.here.now/protocolvision/"

def esc(s):
    return s.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")

def fold(line):
    out, b = [], line.encode()
    while len(b) > 74:
        cut = 74
        while (b[cut] & 0xC0) == 0x80:  # don't split a UTF-8 character
            cut -= 1
        out.append(b[:cut].decode()); b = b" " + b[cut:]
    out.append(b.decode())
    return "\r\n".join(out)

stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Protocol Institute//SIG P4B//EN",
         "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:Protocols for Business SIG",
         "X-WR-CALDESC:Biweekly sessions of the Protocol Institute's Protocols for Business SIG"]
for i, s in enumerate(SESSIONS, 1):
    d = s["date"].replace("-", "")
    desc = (f"Reading: {s['title']} ({s['cite']})\n{s['url']}\n\n"
            f"Alongside: {s['pi_title']} ({s['pi_cite']})\n{s['pi_url']}\n\n"
            f"Feature: {s['feature']}\n\nJoin on the Protocol Institute Discord: {DISCORD}\n"
            f"Syllabus: {SITE}syllabus/\nSessions are recorded.")
    lines += ["BEGIN:VEVENT", f"UID:sig-p4b-{d}@protocol-institute", f"DTSTAMP:{stamp}",
              f"DTSTART:{d}T{START}", f"DTEND:{d}T{END}",
              fold(f"SUMMARY:{esc(f'SIG P4B · {s['title']}')}"),
              fold(f"DESCRIPTION:{esc(desc)}"),
              fold(f"LOCATION:{esc('Protocol Institute Discord · ' + DISCORD)}"),
              f"URL:{SITE}", "END:VEVENT"]
lines.append("END:VCALENDAR")
(ROOT / "sig-p4b.ics").write_text("\r\n".join(lines) + "\r\n")

# Refresh the homepage's embedded session list.
idx = ROOT / "index.html"
page = idx.read_text()
slim = [{k: s[k] for k in ("date", "title", "url", "cite", "feature")} for s in SESSIONS]
blob = json.dumps(slim, ensure_ascii=False)
page = re.sub(r'(<script id="sessions" type="application/json">).*?(</script>)',
              lambda m: m.group(1) + blob + m.group(2), page, flags=re.S)
idx.write_text(page)
print(f"{len(SESSIONS)} sessions -> sig-p4b.ics")
