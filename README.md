# Protocols for Business SIG

Site for the Protocol Institute's Special Interest Group in Protocols for Business (SIG P4B):
the group's relation to Summer of Protocols and PI, the 2027 **AI Native Data Operations** project,
the two pilot case studies (California water rates; construction bids from PDF solicitations),
and the October 2026 – March 2027 syllabus.

**Live:** https://npc.here.now/protocolvision/

Modeled on the Personhood Research Group site (personhoodresearchgroup.isthisa.com): plain HTML,
one stylesheet, no build step. The Protocol Institute brand kit
(https://npc.here.now/protocolinstitutebrandkit/) is applied lightly: paper and ink colors, Lora for
body text, Instrument Serif for the page title, cobalt links.

## Layout

```
index.html               overview, research questions, session list, essays
syllabus/index.html      12 sessions with readings and monthly deliverables, plus the case-study template
case-studies/index.html  water + construction briefs
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
