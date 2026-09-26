# Protocols for Business SIG

Site for the Protocol Institute's Special Interest Group in Protocols for Business (SIG P4B):
the group's relation to Summer of Protocols and PI, the 2027 **AI Native Data Operations** project,
the two pilot case studies (California water rates; construction bids from PDF solicitations),
and the October 2026 – October 2027 syllabus.

**Live:** https://npc.here.now/protocolvision/

Modeled on the Personhood Research Group site (personhoodresearchgroup.isthisa.com): plain HTML,
one stylesheet, no build step. The Protocol Institute brand kit
(https://npc.here.now/protocolinstitutebrandkit/) is applied lightly: paper and ink colors, Lora for
body text, Instrument Serif for the page title, cobalt links.

## Layout

```
index.html               overview, research questions, session list, essays
syllabus/index.html      year-long reading group: 26 sessions, each a core classic + a response (NPC Memo / Archival Time / Protocolized); 7 parts, each ending in a claim
observations/index.html  protocol watching (the reps): how to see a protocol, bigger questions, recording (field-guide notation + Bicorder), sources, inventory
observations/            per observation: Bicorder JSON export + short .md note (copy TEMPLATE.md)
case-studies/index.html  the heavy lifts: every participant carries one case; worked examples; milestones; template
case-studies/<name>/     participant case studies (copy case-studies/TEMPLATE.md)
simulation/index.html    Swarm Simulation — placeholder for a guardrails game (Kestrel Widget Works); linked from homepage + footer, not top menu
sources/                 local reference copies (field guide, Reader EPUB) — gitignored, never deployed; link out instead
assets/                  cube linework watermark + link-preview image (from PI brand kit art 6)
style.css                the only stylesheet
favicon.svg              PI P-mark
deploy.sh                publish to here.now and mount at npc.here.now/protocolvision
```

## Contributing

Open a pull request. To add a session's notes, create `meetings/YYYY-MM-DD-slug/index.html` and link it
from the session's line in `index.html` and `syllabus/index.html`. Keep relative links; the site is
served under `/protocolvision/`.

Keep construction client details anonymized. The client is not named anywhere in this repo.

## Deploy

`./deploy.sh` (needs a here.now API key in `~/.herenow/credentials`).

## Session sign-ups

The homepage form posts to a Cloudflare Worker (`worker/`, deployed as `sig-p4b-signup` on rafaeldf2.workers.dev) that stores sign-ups in KV.

- **Export the list before a session:** `worker/export.sh` writes `signups-YYYY-MM-DD.csv`, which is gitignored. It reads the secret from `~/.config/sig-p4b/export_secret`.
- **Unsubscribe links:** each row has one. Include it in every session email.
- **Redeploy the worker:** `cd worker && npx wrangler deploy`.

## Sessions and calendar

`tools/sessions.json` is the source of truth for the 26 sessions: date, reading, companion piece, and feature. After editing it, run:

    python3 tools/build_schedule.py

The script rebuilds `sig-p4b.ics`, the subscribable calendar with times in UTC (15:30–16:30), and refreshes the homepage's "Next session" box, which picks the next upcoming session in the reader's browser. Run `./deploy.sh` afterwards.

Recordings go in the homepage's "Past sessions" archive. A commented template entry is in `index.html`.
