# Agent notes

- Quiet, text-first site in the style of personhoodresearchgroup.isthisa.com. Don't add hero sections, cards, JS, or heavy branding.
- PI brand kit is applied *lightly* through the tokens in `style.css`. Change the tokens rather than adding colors inline.
- All links must be relative (served at npc.here.now/protocolvision/).
- Never name the construction client or give its bid figures. Water case links point to public reports only.
- After editing, run `./deploy.sh`, then commit and push.
- Three tracks: readings (perspectives), observations (reps, ~100/yr), case studies (heavy lifts, encouraged for every member). Keep all three pages in sync when changing dates or parts.
- `deploy.sh` stamps `style.css?v=` on each deploy to bust the CDN cache.
- Syllabus: `tools/themes.json` (six themes, readings in order of exploration, sample readings, companions) and `tools/slots.json` (26 dates with show-and-tell/guest) are the source of truth. Run `python3 tools/build_schedule.py`; it writes the themes summary into `src/sessions.html`, the public `sessions.json` and the calendar.
- Reading map: pipeline in `drafts/landscape/` (see its README); `drafts/landscape/.venv/bin/python drafts/landscape/publish.py` copies it to `sessions/map/`. Re-run `paths.py` then `publish.py` after editing themes.json.
- Sessions are fixed at 15:30 UTC (Berlin local time moves with DST). Sessions are recorded; say so wherever meeting details appear.
- v2: edit `src/*.html` (never the generated page files), then run `tools/build_schedule.py` and `tools/build_site.py`. `src/sessions.html` contains generated regions between markers.
- Blyg (Blygger 0.3): sources in `blyg-src/` (commit = publish; never rename files). `./deploy.sh` builds and runs `tools/blyg_check.py` before publishing. Mark model-written text with `::: generated` fences.
- Sign-up Worker URL and site URL live in `config.json` (read by the builders and `worker/export.sh`); the Worker's own `SITE`/`ALLOWED_ORIGINS` are `vars` in `worker/wrangler.jsonc`. Redeploy-on-another-account steps: `worker/README.md`. Never write sign-up exports into the repo.
- Vocabulary: protocol vision is the *capability* (seeing the protocols a business runs on); Business Protocol Management is the *practice* (See, Design, Evolve). Don't call either one "the method". Watching, workshops and simulations are *training* for the capability.
- `hype/` is a generated parody snapshot (noindex), exported from the local `hype` branch/worktree with `tools/export_hype.sh` there. Never edit it by hand; re-export, then `./deploy.sh`.
- Speakers and rescheduling: `tools/slots.json` is the only place to edit. Each date has a `feature` (`Guest: Name (talk title)` for a guest, `Open guest slot: offer a talk`, `Tooling demo: …`, `Case study catch-up: …`) and optional `links` (`{"Name": url, "first word of title": url}`). To schedule a speaker, replace an open slot; to reschedule, swap two features. Readings stay on their dates (they follow themes.json order). Then run `tools/build_schedule.py` and `./deploy.sh`: the theme drop-downs, guest lines, next-session box (sessions.json), calendar, JSON-LD and the open-slot count on Research all update together. `hype/` is a separate snapshot and only changes when re-exported.
