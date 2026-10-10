# Report template v2: design notes

File: `template-v2.html` (reviewed 2026-10-10; pre-review copy `template-v2-pre-review.html`, review in `review-template.md`). All values are placeholders; none is a finding. Swap the `report-data` JSON block and the `PROSE SLOT` paragraphs.

## Editorial rule

The report leads with what was found. A lack of evidence gets space only when it changes the narrative, and then briefly. An undecided test is one plain line in Method, with its power, and is never phrased as "no".

## Structure (under seven minutes)

1. **What we found**: 3–5 findings, each with its evidence and a confidence mark. A decisive verdict and a decisive head-to-head join this list.
2. **What each instrument found**: the hypotheses × instruments grid, rows with evidence only. All-`none` rows fold into one line: "Not tested by desk evidence (see What we test next)".
3. **Pattern match**: feature profiles, head-to-head (drawn only when decisive), timeline.
4. **Since round one**.
5. **What we test next**: the field plan, forward-looking.
6. **Method and sources**: undecided tests, then a compact corpus and coverage note, then drawers for deviations, method steps and sources.

Pages 2–5 and each block in page 3 render only if their data has content. Page numbers ("Page n of N") and nav links follow the visible pages. Sticky page nav.

## Tokens

Paper `--bg` #fbfbf8 / dark #121614; ink `--fg` #1d2320 / #e5e9e3; `--muted` #586059 / #9aa49c; `--rule` (hairlines only); `--line` #8a938c / #69736b (axes and guides, 3:1); `--fill`; forest `--accent` #0f6e56 / #46b996 and `--accent-soft`; `--on-accent` #fff / #0b0f0d (text on accent fills); `--warn` #a8481b / #e48a5c for contradicts and caveats only. One typeface: `Lora, Charter, Georgia` (same stack as site style.css, no webfont load). Lining tabular figures. Light, dark (system) and `data-theme` override all defined. Every text and graphic pair passes WCAG AA in both themes (script and table in `review-template.md`).

## Visual language

Hard vs soft: solid = observed or strong; dashed or frayed = early sign, partial, not yet observable. The masthead rope is straight, then frays. Every state has a shape plus a word, never colour alone: strong / high confidence = filled disc; single / moderate = ring with dot; early sign / low = dashed ring; none = dash; contradicts = cross (warn colour). Motion: none (smooth scroll only, off under `prefers-reduced-motion`).

## Data schema (`#report-data`)

- `meta` {series, date, title, subtitle, footer}
- `findings[]` (3–5) {id, statement, evidence_summary, instruments[] (ids from `grid.instruments`), sources (count), confidence: high|moderate|low, quote {text, id (corpus id)}, caveat: string|null}. A caveat that changes how a finding reads goes here, next to the finding, not in Method.
- `verdict` {outcome: supported|family|not-supported|inconclusive, label, statement, hypothesis, power: [lo, hi] (% from simulation; a range, never a single point), falseSupport: number|null, instruments[], confidence}. Any outcome but `inconclusive` becomes the first finding, with "Verdict: label. The test returns this verdict in lo–hi% of simulated runs…; false support at most n%." `inconclusive` becomes one line in Method: "…returns 'Supported' in only lo–hi% of simulated runs, so this result is not evidence against it."
- `grid` {instruments[{id,name}], hypotheses[{id,label,cells[n]: strong|single|none|contradicts}]}
- `profiles` {scale, scoreLabel, caption, features[{id,name}] (any count; the reading rule reports all 21 coded features), patterns[{id,name,values[] of 0|1|2,score|null}], present{name,values,score}}. Collapses if `patterns` or `present.values` is empty. Score column shows only when a score exists.
- `headToHead` {a, b, k, power (string), features[{id,name,value -1|0|1}]}. Sum computed in script; drawn and listed as a finding when |sum| > k; otherwise one line in Method.
- `timeline` {title, historicalLabel, presentLabel, axis{min,max,unit,nowYear}, historical[{year,text}], present[{year,text}], caption}. Collapses if both lists are empty.
- `changes[{status: replicated|revised|round-one-only, text}]`. Collapses if empty.
- `nextTests[{test, why, when|null}]`. `why` names the finding or hypothesis the test sharpens. Collapses if empty.
- `funnel[{stage,count}]` (rendered as one sentence in Method), `coverage` {sectors[{name,status: covered|partial|missing}] (one sentence), caveat[strings] (limits that change no finding)}
- `deviations[]`, `method[]` (strings, in `<details>`), `sources[{id,type,date,use}]`.

## Charts at phone width

The head-to-head and timeline SVGs are drawn at the container's real pixel width and redrawn on resize, so text stays at 12–13px. Below 480px the head-to-head puts each feature label above its row. The dot matrix labels every fifth feature column and draws a faint guide every five. The grid fits 375px without scrolling (six instruments); the sources table scrolls inside its own box.

## Accessibility

Landmarks and one h1; focusable scroll regions with labels; SVGs carry `role="img"` with an aria-label (profiles: per-feature values; head-to-head: a hidden per-feature list follows; timeline: events listed below); the grid has hidden per-cell text and `<abbr>` instrument ids; page nav marks the current section with `aria-current="location"`; visible focus ring; 16px+ side gutter; no body horizontal scroll at 375px (checked headless in an iframe harness).

## Open items

- The page is rendered by script; with JavaScript off it is empty. The site rule is "no JS", so the final report should be pre-rendered at build time (run the same script once and save the DOM) before publishing.
- Head-to-head feature labels are single-line SVG text; keep names under about 40 characters.
