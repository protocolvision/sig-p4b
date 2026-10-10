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
