# Operations

How the group runs, in plain steps. This folder is in the public repository but never on the website.
Nothing private goes here: no sign-up exports, no secrets, no client names.

## Email drafts

Drafts live in [`emails/`](emails/), one file per email, named `YYYY-MM-DD-topic.md`. Each ends with
"Notes before sending", which are not part of the email.

**Sending a session email**
1. Export the list outside the repo: `worker/export.sh ~/Documents/sig-p4b-signups-$(date +%F).csv`
2. In Gmail, put your own address in To and paste the email column into **BCC**.
3. Paste the draft. Its footer links the unsubscribe page: https://protocolsforbusiness.com/unsubscribe/
4. After sending, add `Sent: YYYY-MM-DD` under the title of the draft and commit it.

## Scheduling a speaker or moving a session

Edit `tools/slots.json` only. Each date has a `feature`:

- a guest: `Guest: Name (talk title)`, with optional `links`, e.g. `{"Name": "https://…"}`
- `Open guest slot: offer a talk`, `Tooling demo: …`, `Case study catch-up: …`
- a different time: add `"start"` / `"end"` (HH:MM, UTC)

To schedule a speaker, replace an open slot; to move one, swap two features. Readings stay on their dates.
Commit and push: Sessions, the next-session box, the calendar and the open-slot count on Research update together.
A short blyg post about schedule changes is welcome (see below); confirm guests are happy to be named.

## Publishing

- **Site:** commit and push to `main`. GitHub builds, checks and publishes to https://protocolsforbusiness.com in a minute or two.
- **Blyg post:** `python3 tools/blyg_new.py thread some-name --author "Your Name"`, write it, commit, push.
  Open a pull request instead if you want someone to review it first: merging publishes it.
- **Responding to another post:** add `stub_of` to the front matter (see `blyg-src/README.md`).

## What runs on its own

- **Fridays 16:00 UTC:** one Discord message with the week's blyg posts, responses from other blygs, and the next session.
- **New sign-ups:** a short note in Discord with the new total, no names.
- **Talk offers and advisory requests:** posted to Discord from the site's forms.

## Where things are

| What | Where |
|---|---|
| Site | https://protocolsforbusiness.com (old address redirects: npc.here.now/protocolvision) |
| Source | https://github.com/protocolvision/sig-p4b |
| Sign-ups, forms, digest | `worker/` (Cloudflare Worker `sig-p4b-signup`; deploy with `npx wrangler deploy`) |
| Site hosting, Webmentions | `site/` (Cloudflare Worker `protocolsforbusiness`; deployed by GitHub) |
| Protocol Institute calendar | the "Add the calendar" link in the site footer (update it there separately) |
