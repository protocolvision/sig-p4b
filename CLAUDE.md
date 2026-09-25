# Agent notes

- Quiet, text-first site in the style of personhoodresearchgroup.isthisa.com. Don't add hero sections, cards, JS, or heavy branding.
- PI brand kit is applied *lightly* through the tokens in `style.css`. Change the tokens rather than adding colors inline.
- All links must be relative (served at npc.here.now/protocolvision/).
- Never name the construction client or give its bid figures. Water case links point to public reports only.
- After editing, run `./deploy.sh`, then commit and push.
- Three tracks: readings (perspectives), observations (reps, ~100/yr), case studies (heavy lifts, one per participant). Keep all three pages in sync when changing dates or parts.
- `deploy.sh` stamps `style.css?v=` on each deploy to bust the CDN cache.
