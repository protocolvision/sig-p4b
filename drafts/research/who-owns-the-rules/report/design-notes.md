# Report template v2: design notes

File: `template-v2.html` (r2 memo; r1 kept as `template-v2-r1.html`; reviewed 2026-10-10; pre-review copy `template-v2-pre-review.html`, review in `review-template.md`). All values are placeholders; none is a finding. Swap the `report-data` JSON block and the `PROSE SLOT` paragraphs.

## Editorial rule

The report leads with what was found. A lack of evidence gets space only when it changes the narrative, and then briefly. An undecided test is one plain line in Method, with its power, and is never phrased as "no".

## Structure (a memo, under seven minutes)

r2 (2026-10-10) turned the page template into a memo. Previous version: `template-v2-r1.html`.

- **No label headings.** Every title, section heading, figure title and drawer summary is the lede of a finding: a full sentence. Placeholders read "PLACEHOLDER: a finding stated as a sentence". The one exception in form is the closing note, whose heading is also a statement ("how much weight these findings bear").
- **Minimal formatting.** Running prose, one 40rem column, no cards, badges, boxes, page numbers or tab chips. Navigation is one quiet inline line, "In this memo: ..." built from the visible sections' headlines. Confidence and evidence are small muted prose under each finding ("High confidence, from A and B; 42 sources."). A caveat is a sentence starting "Read with this in mind". Changes and next tests are plain paragraphs with the status or reason in small text beneath.
- Order: lead (headline, dek, optional ambient rope, contents line), findings, evidence grid, pattern match (profiles, head-to-head, timeline), changes, next tests, closing note (undecided tests, corpus, coverage, then three statement-titled drawers).
- Sections other than findings and the closing note, and each figure in the pattern section, render only if their data has content (the contents line follows). Head-to-head is drawn and listed as a finding only when |sum| > k. Inconclusive is one sentence in the closing note ("... so this result is not evidence against it"), power as a range.

## Tokens

Paper `--bg` #fbfbf8 / dark #121614; ink `--fg` #1d2320 / #e5e9e3; `--muted` #586059 / #9aa49c; `--rule` (faint guides only); `--line` #8a938c / #69736b (axes, 3:1); `--fill`; forest `--accent` #0f6e56 / #46b996; `--on-accent`; `--warn` #a8481b / #e48a5c (contradicts and caveats). `--accent-soft` was dropped with the highlighted row. Values unchanged from r1, so the r1 contrast table in `review-template.md` still holds (AA both themes). One typeface: Lora/Charter/Georgia. Light, dark (system) and `data-theme` override defined.

## Visual language

Hard vs soft: solid = observed or strong; dashed or frayed = early sign, partial, not yet observable. Shapes plus words for every state (filled disc, ring with dot, dashed ring, dash, cross). The ambient figure under the series line is a rigid ruled line with joints that meets three frayed strands and one small packet (tangle study language); decorative, `aria-hidden`, on when `meta.ambient` is true.

## Animation spec

- The script adds `anim` to `<html>` only if IntersectionObserver exists and `prefers-reduced-motion` is not `reduce`. Otherwise no start state applies and every figure shows its final state immediately. Figures are readable without animation (all labels, lists and captions are static).
- Each figure (`[data-anim]`) gets class `in` once, when 20% is in view; then it is unobserved, so it runs once.
- Marks carry one of four classes: `a-grow` (scale 0 to 1, .8s), `a-draw` (stroke-dashoffset with pathLength 1, 1.1s), `a-fade` (.8s), `a-slide` (translateX from `--dx`, 1.1s). All ease-out, per-mark delay in `--d`.
- Per figure, one idea: ambient (hard rule draws, strands draw, packet fades in); grid (icons grow row by row); profiles (dots grow row by row); head-to-head (the sum marker slides from 0 to its value; feature rows are static); timeline (lane lines draw, points grow in date order across both lanes at 130 ms steps, "now" and the projection fade in last).
- Redraws on resize keep the final state if the figure has already played.

## Data schema (`#report-data`)

Every section and every figure has `headline` (the finding as a sentence) and optional `dek` (one supporting sentence). Sections also take `prose[]` (paragraphs).

- `meta` {series, date, headline, dek, ambient: bool, footer}
- `findings` {headline, dek, prose[], items[{id, headline, body, instruments[] (ids from `evidence.grid.instruments`), sources (count), confidence: high|moderate|low, quote {text, id}, caveat: string|null}]}. 3-5 items. A caveat that changes how a finding reads sits on that finding.
- `verdict` {outcome: supported|family|not-supported|inconclusive, label, headline, hypothesis, power: [lo, hi] (from simulation; a range), falseSupport: number|null, instruments[], confidence}. Decisive: becomes the first finding with its power range. `inconclusive`: one sentence in the closing note.
- `evidence` {headline, dek, prose[], grid {headline, dek, instruments[{id,name}], hypotheses[{id,label,cells[]: strong|single|none|contradicts}]}}. All-`none` rows fold into one sentence under the grid.
- `patterns` {headline, dek, prose[], profiles {headline, dek, scale, scoreLabel, caption, features[], patterns[{id,name,values,score|null}], present{name,values,score}}, headToHead {headline, dek, a, b, k, power, features[{id,name,value -1|0|1}]}, timeline {headline, dek, historicalLabel, presentLabel, axis{min,max,unit,nowYear}, historical[{year,text}], present[{year,text}], caption}}
- `changes` {headline, dek, prose[], items[{status: replicated|revised|round-one-only, text (a sentence)}]}
- `next` {headline, dek, prose[], items[{test (a sentence), why, when|null}]}
- `closing` {headline (a statement about how much weight the findings bear), dek, prose[], funnel[{stage,count}] (one sentence), coverage {sectors[{name,status}], caveat[]}, deviations {headline, items[]}, method {headline, steps[]}, sources {headline, rows[{id,type,date,use}]}}. The three drawers' summaries are the `headline`s.

## Charts at phone width

The head-to-head and timeline SVGs are drawn at the container's real pixel width and redrawn on resize, so text stays at 12–13px. Below 480px the head-to-head puts each feature label above its row. The dot matrix labels every fifth feature column and draws a faint guide every five. The grid fits 375px without scrolling (six instruments); the sources table scrolls inside its own box.

## Accessibility

r2 screenshots: `r2-375-*.png` (375px, dark, reduced motion = final state), `r2-final-1280.png`, `r2-1280-top.png`, `r2-mid-animation-1280.png` (mid-draw ambient figure), `r2-end-top.png`. Page nav removed; the contents line replaces it.


Landmarks and one h1; focusable scroll regions with labels; SVGs carry `role="img"` with an aria-label (profiles: per-feature values; head-to-head: a hidden per-feature list follows; timeline: events listed below); the grid has hidden per-cell text and `<abbr>` instrument ids; visible focus ring; 16px+ side gutter; no body horizontal scroll at 375px (checked headless in `harness.html`, a 375px iframe).

## Open items

- The page is rendered by script; with JavaScript off it is empty. The site rule is "no JS", so the final report should be pre-rendered at build time (run the same script once and save the DOM) before publishing.
- Head-to-head feature labels are single-line SVG text; keep names under about 40 characters.

## Backlog: method walkthrough figure (user request, 10 October 2026)

An animated, scroll-driven figure showing how the data was transformed, so a reader can grasp the
method intuitively. It is placed in the closing method note, or as a short "how we did it" figure after
the lead findings. Steps:
1. **Corpus and sample:** crawled postings → selected postings (dots grouped by employer type and sector).
2. **Extraction:** postings split into duty statements (counts animate).
3. **Embedding and clusters:** statements move into a 2D map and settle into clusters; discovery and
   holdout halves side by side.
4. **Coding:** clusters coloured by code family, with the hidden seeds shown being caught (or missed).
5. **Analysis:** clusters fold into the headline findings (absorption vs new titles; functions combined).

**Data needed:**
- the funnel counts from log.md;
- 2D UMAP coordinates for a stratified sample of about 3,000 statements, with cluster ids;
- cluster code families;
- seed outcomes.
Use real data only. Respect reduced motion (show the final state).

## r3: protocolvision.org brand (2026-10-10)

`template-v2.html` is restyled to the brand; the previous version is `template-v2-r2.html`. Data schema, script logic, animations, reduced motion and collapse rules are unchanged. Differences from the sections above (Tokens, Structure): they describe r2 and are superseded where listed here.

- **Font:** one typeface, JetBrains Mono, self-hosted. `@font-face` for weights 400, 500, 700 points at `fonts/jetbrains-mono-latin-{400,500,700}.woff2` (relative; licence in `fonts/OFL.txt`). Stack: `"JetBrains Mono", ui-monospace, Menlo, Consolas, monospace`. No third-party font. Body 15px/1.75 (14px under 560px, as on the site); h1 `clamp(1.5rem,4.4vw,2.15rem)` weight 400, -.025em; h2 `clamp(1.35rem,3.4vw,1.7rem)` weight 700, -.015em. Column 46rem, side padding 1.25rem. Mono is wide, so head-to-head feature labels are 12px with a 220px label column (stacked above the row below 560px); keep names under about 28 characters.
- **Light tokens:** paper `--bg` #f9f8f5, ink `--fg` #2c2c2a, ink-2 `--muted` #5f5e5a, hair `--rule` #d9d6cf, `--fill` #f1efe9, cobalt `--action` #004fcc (hover #003a96), forest `--accent` #0f6e56 (the brand's `--hard`), `--line` #8a8780 for chart axes, `--warn` #a8481b (contradicts and caveats only; not a brand colour).
- **Dark tokens:** `--bg` #161614, `--fg` #ebe9e3, `--muted` #a9a7a0, `--rule` #3a3935, `--fill` #201f1c, `--action` #7ba6ff (hover #a8c4ff), `--accent` #4fb897, `--line` #77756e, `--warn` #e48a5c, `--on-accent` #10100e. Applied under `prefers-color-scheme: dark` and `data-theme="dark"`.
- **Contrast (checked by script):** light: ink 13.2, ink-2 6.1, cobalt 6.6, forest 5.8, warn 5.5, white on forest 6.2, white on cobalt 7.0, axes 3.4 (on fill 3.1). Dark: ink 14.9, ink-2 7.5, cobalt 7.5, forest 7.5, warn 7.0, dark text on forest 7.8, on cobalt 7.9, axes 3.9. All text at least 4.5:1, graphics at least 3:1.
- **Masthead:** the logo (inline `mark.svg`, recoloured through tokens so it works in dark) at 22px plus "Protocol Vision" in bold, left; the report date, right, in ink-2. The series name sits in small spaced text above the headline.
- **Findings:** each carries a small running label ("01", "02", ...) in the site's `.n` style (12px, .1em, ink-2, top hairline) above its heading. The finding's `body` (or the verdict sentence) renders as `.ask`: forest left border, weight 500.
- **Figure colour:** ink marks and ink-2 secondary marks, hair guides, cobalt for the current state and highlights (present row of profiles, present-day timeline events and "now", the head-to-head sum marker, the ambient packet), forest for hard or confirmed (grid strong, single and early rings, observed profile dots, historical timeline events). Ambient figure: forest rigid rule and joints, ink-2 frayed strands.
- **Screenshots:** `r3-1280-light.png` (full page), `r3-1280-dark.png` (top, 2400px), `r3-375-dark.png` (375px iframe), all in reduced motion (final state).

## r4: lighter, light only, hairline (2026-10-10)

`template-v2.html` is rewritten; the previous version is `template-v2-r3.html`. Data schema, collapse rules, finding-lede headings, 375px layout, scroll-in animation and reduced motion are kept. The r3 section's dark tokens, mono body and `--warn` colour are superseded.

- **Light only.** `<html data-theme="light">`; paper #f9f8f5. The two dark blocks stay as a minimal token redefinition (artifact contract), guarded `:root:not([data-theme="light"])` and `[data-theme="dark"]`, so they never apply. `--warn`, `--rule`, `--line` and `--fill` are gone; `--hair` #c9c7c0 is the one guide colour.
- **Fonts.** Body, captions, figure labels, evidence lines, h2/h3 (weight 600) in Lora (Google Fonts, 400/500/600; fallback Charter, Georgia, serif), 17px/1.65 (16px under 560px), column 40rem. JetBrains Mono (self-hosted 400/500) only for the masthead line, the h1 and the "01" finding labels.
- **Stroke spec.** Axes, gridlines, table rules: 0.5px `--hair`. Marks and lines: 0.75 to 1.2px (ink-2 lines 0.75 to 1, cobalt and forest rings 1 to 1.2). Dots r 2 to 3 (r 4.5 for hatched circles so the hatch reads). Hatch: 45 degree lines, 0.5px, 2.4px pitch, forest (`#hx-f`) or cobalt (`#hx-c`), defined once in a zero-size SVG; no solid fills, shadows or gradients. Dashed `6 2 1 2` for projections, bands and the year-0 guide; `2 2` ring for an early sign.
- **Colour use.** Ink-2 for most marks and lines. Cobalt for the present or current state (present multiple, present events, "now", the head-to-head sum marker, the ambient dot) and links. Forest and forest hatch for confirmed or hard (strong cells, observed dots, historical events, the last funnel and method stage). "Contradicts" is an ink cross, no warning colour.
- **Figures.** Hypothesis grid: a plain table, hairline rules, small hairline glyphs. Pattern profile: small multiples, one 5-column dot grid per pattern (read left to right, top to bottom, in the order of the numbered feature key). Head-to-head, timeline: hairline rows and lanes, dots, dashed band and projection. Funnel: one hairline per stage to scale, end dot, count. Method walkthrough: steps as dots on one hairline inside the drawer, redrawn when it opens. Ambient: one quiet hairline (a rule that frays into a dashed one, one cobalt dot), on when `meta.ambient` is true.
- **Motion.** Lines draw (stroke-dashoffset, 1.6s), dots and dashed pieces fade in order (1s, 120 to 350ms steps), the sum marker slides (1.6s). Nothing scales or bounces. `.anim` is only added when motion is allowed.
- **Contrast (script).** On paper: ink 13.2, ink-2 6.1, cobalt 6.6, forest 5.8 (all text at least 4.5, marks at least 3). `--hair` is 1.6 and is decorative only: no meaning rests on a guide alone.
- **Screenshots.** `r4-1280.png` (full page, final state), `r4-375.png` (375px iframe, full page), `r4-375-top.png`.
