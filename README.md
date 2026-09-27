# Protocols for Business SIG

The central repository for the Protocol Institute's Special Interest Group in Protocols for Business
(SIG P4B). Everything the group publishes, and the tooling around it, lives here and is built from here.

**Live:** https://npc.here.now/protocolvision/ (a staging domain; a production domain comes later)

## What's in it

| Part | Where | What it does |
|---|---|---|
| Website | `src/`, `tools/build_site.py` | About, Sessions, Research, Play. Built to static pages with `llms.txt` for language models |
| Syllabus and calendar | `tools/sessions.json`, `tools/build_schedule.py` | 26 sessions from 2 November 2026: readings, quotes, companions, show-and-tell; `sessions.json`, schema.org events, and a subscribable `.ics` |
| Blyg | `blyg-src/`, `tools/build_blyg.py` | Session notes and the research log, published with the Blygger protocol 0.2. Git commits are publishes; `tools/blyg_check.py` checks conformance |
| Member sign-ups | `worker/` | Cloudflare Worker storing registrations (member / pi-core roles), CSV export, signed unsubscribe links |
| Case studies, protocol watching | `src/research-cases.html`, `src/play-watching.html`, `case-studies/`, `observations/` | Templates and guides for participants' own cases and observations |
| CI and deploy | `.github/workflows/site.yml`, `deploy.sh` | Build and check on every push and pull request; publish from `main` |

The design is quiet and text-first, after the Personhood Research Group's site, with the
[Protocol Institute brand kit](https://npc.here.now/protocolinstitutebrandkit/) applied lightly and
Apple-style controls (44pt targets, sentence-case buttons).

## Roadmap: building on the central repo

The repo is meant to be the group's single source of truth, with more flows added on top of it:

1. **Email to members.** Send each session's reading and prep notes to registered members from
   `tools/sessions.json`, with each person's unsubscribe link. The member list and roles already live
   in the sign-up worker. Candidates: Cloudflare Email Service from the worker, or an export to a
   newsletter tool.
2. **Meeting recordings.** Connect the Protocol Institute's recording pipeline (c3po's Discord
   ingestion and the recording notes in PI's storage) so each session's recording and notes land
   here automatically: a session-notes thread on the blyg and a link in the Sessions archive.
3. **Production domain.** Move from the npc.here.now staging mount to a permanent domain. The blyg's
   origin URL is its identity, so this should happen before the feed is announced widely.
4. **Auto-publish from GitHub.** Add the here.now key as a repository secret so merges to `main`
   publish without a local deploy.

## Layout

```
index.html               overview, research questions, session list, essays
syllabus/index.html      year-long reading group: 26 sessions, each a core classic + a response (NPC Memo / Archival Time / Protocolized); 7 parts, each ending in a claim
observations/index.html  protocol watching (the reps): how to see a protocol, bigger questions, recording (field-guide notation + Bicorder), sources, inventory
observations/            per observation: Bicorder JSON export + short .md note (copy TEMPLATE.md)
case-studies/index.html  the heavy lifts: every participant carries one case; worked examples; milestones; template
case-studies/<name>/     participant case studies (copy case-studies/TEMPLATE.md)
play/index.html          Protocol Play (top menu): games and simulations; first entry is the Swarm Simulation placeholder (Kestrel Widget Works)
simulation/index.html    redirect stub to play/
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

The homepage Register button opens a dialog (a bottom drawer on phones) that posts to a Cloudflare Worker (`worker/`, deployed as `sig-p4b-signup` on rafaeldf2.workers.dev) that stores sign-ups in KV.

- **Export the list before a session:** `worker/export.sh` writes `signups-YYYY-MM-DD.csv`, which is gitignored. Columns: name, email, affiliation, website, github, discord, role (member or pi-core), signed_up, source, updated, unsubscribe_url. Registering again merges: new non-empty fields update the record, empty ones keep existing values, and the original signup date, source, and role are kept. It reads the secret from `~/.config/sig-p4b/export_secret`.
- **Unsubscribe links:** each row has one. Include it in every session email.
- **Redeploy the worker:** `cd worker && npx wrangler deploy`.

## Sessions and calendar

`tools/sessions.json` is the source of truth for the 26 sessions: date, reading, companion piece, and feature. After editing it, run:

    python3 tools/build_schedule.py

The script rebuilds `sig-p4b.ics`, the subscribable calendar with times in UTC (15:30–16:30), and refreshes the homepage's "Next session" box, which picks the next upcoming session in the reader's browser. Run `./deploy.sh` afterwards.

Recordings go in the homepage's "Past sessions" archive. A commented template entry is in `index.html`.

## v2 layout (branch `v2`)

Pages are built from `src/*.html` bodies:

    python3 tools/build_schedule.py   # sessions.json -> src/sessions.html syllabus, schema.org data, sessions.json, sig-p4b.ics
    python3 tools/build_site.py       # src/*.html -> page files, redirect stubs, llms.txt

| Path | Page |
|---|---|
| `/` | Home: next session, what we do, highlights |
| `about/` | Protocol vision, origins, people, work so far |
| `sessions/` | Joining details, session format, syllabus, archive |
| `research/`, `research/cases/` | 2027 focus, questions, case cards; full case briefs and template |
| `play/`, `play/watching/` | Protocol watching, workshops, simulation; the watching guide |
| `llms.txt`, `sessions.json` | Machine-readable summary and session data |

The next-session card and the register dialog come from `assets/site.js`. Old URLs (`syllabus/`, `observations/`, `case-studies/`, `simulation/`) redirect to the new pages. v1 is tagged `v1`.

## Blyg (session notes and research log)

`blyg-src/` holds the SIG's session notes and research log. `tools/build_blyg.py` publishes them to
`/blyg/` with the [Blygger protocol](https://blygger.org/) 0.2 (Level 1), and `tools/blyg_check.py`
checks conformance. Versions come from git: each commit that changes an item is one published version.
See `blyg-src/README.md` for how to contribute. The first ten session notes were imported from the
Protocol Institute's meeting archive (PI `website` repo, generated by c3po from the session Discord threads
and recordings), with provenance links on each item.

## Continuous integration

`.github/workflows/site.yml` builds everything and runs the blyg check on every push and pull request.
On `main` it also publishes to here.now, if the repo has a `HERENOW_API_KEY` secret.
