# Review of template-v2.html

Date: 2026-10-10. Pre-review copy: `template-v2-pre-review.html`. Scope: design quality, readability at 375px, contrast, data contract, site style. Midway through, a new direction came in: lead with what was found, and give a lack of evidence space only when it changes the narrative. The restructure below follows that direction.

## Fixed

**Restructure (new direction)**
- Page 1 is now **What we found**: 3–5 finding statements. Each has a confidence mark (shape plus word), the instruments, a source count, one evidence line and one representative quote with its corpus id. New `findings[]` schema.
- The four-row verdict card is gone. A decisive verdict (Supported, family, Not supported: X) becomes the first finding, with its power range and false-support rate in the text. "Inconclusive" is one line in Method, with its power: "…returns 'Supported' in only 5–8% of simulated runs, so this result is not evidence against it". It is never phrased as "no".
- The head-to-head is drawn, and listed as a finding, only when it decides (|sum| > k). Otherwise it is one line in Method.
- The grid shows only hypotheses with evidence. All-`none` rows fold into "Not tested by desk evidence (see What we test next)".
- The corpus funnel bars and the coverage panel are now one sentence each in Method. A caveat that changes how a finding reads sits on that finding as "Read with: …".
- New **What we test next** page (`nextTests[]`). Each test says which finding or hypothesis it sharpens.
- Profiles, head-to-head, timeline, changes, next tests, deviations and method each collapse when their data is empty. Page numbers and nav links follow the visible pages.

**Honesty of encodings**
- Power is now a range `[lo, hi]` from simulation, shown as text. The old single-value meter bar implied more precision than the simulations give (they report ranges such as 92–95% and 73–75%).
- False support can be `null` (not applicable) instead of a blanket "up to 5%" on every verdict.
- The funnel's 8% minimum bar width drew small counts out of scale. Now removed (the funnel is a sentence).

**Readability at 375px**
- The head-to-head and timeline SVGs had a fixed 560px viewBox scaled to about 335px, so their 11–13px text rendered at about 7px. Now drawn at real container width (text 12–13px) and redrawn on resize. On phones the head-to-head puts labels above rows, and the centre line no longer runs through them.
- The page scrolled sideways (scrollWidth 420 at 375). Cause: absolutely positioned visually hidden spans inside the scrolling grid. Fixed with `left:0`, `clip-path` and a positioned `.scroll`.
- The grid needed sideways scrolling. It now fits 375px.
- The dot matrix had no column reference. It now labels every fifth feature (F01, F05, F10, F15) and draws faint guides every five.

**Contrast** (WCAG; script below)
- White text on dark-theme accent markers (head-to-head sum, timeline H markers) was 2.43:1. New `--on-accent` token (#0b0f0d in dark) gives 7.94:1.
- `--muted` darkened #5d655f → #586059 (4.76 → 5.14 on the highlighted present row).
- Axis ticks and guides were drawn in `--rule` (1.25:1). New `--line` token: 3.05 light, 3.71 dark.
- Absent dots now use `--muted`. `--line` gave only 2.50:1 on the present row's tint.

**Accessibility**
- The profiles used `role=table/row` with no cells (invalid ARIA). Now a list, and each row's SVG has an aria-label with per-feature values.
- The head-to-head now has a hidden per-feature list.
- Grid instrument ids are now `<abbr>`, and the grid has a visible "Hypothesis" header.
- Nav uses `aria-current="location"`.

**Data contract**
- Hard-coded "Four possible verdicts", "Six separating features" and the timeline lane labels now come from data or are computed (`timeline.historicalLabel` / `presentLabel`, `profiles.caption`).
- The `.replace('PLACEHOLDER ')` hack is removed.
- design-notes.md documents the full schema and the collapse rules.

## Contrast table (after)

| Pair | Light | Dark | Need |
|---|---|---|---|
| fg on bg | 15.42 | 14.86 | 4.5 |
| muted on bg | 6.27 | 7.10 | 4.5 |
| muted on accent-soft | 5.14 | 4.79 | 4.5 |
| muted on fill (band label) | 5.81 | 6.36 | 4.5 |
| accent on bg (links, labels) | 5.98 | 7.51 | 4.5 |
| warn on bg | 5.61 | 7.03 | 4.5 |
| on-accent on accent | 6.20 | 7.94 | 4.5 |
| accent on accent-soft (dots) | 4.91 | 5.07 | 3 |
| line on bg (axes, guides) | 3.05 | 3.71 | 3 |
| rule on bg | 1.25 | 1.40 | decorative hairlines only |

## Remains

- **Script-rendered page vs the site's "no JS" rule.** With JavaScript off the page is empty. Pre-render at build time (headless Chrome `--dump-dom`) before publishing.
- Head-to-head labels are single-line SVG text. Long feature names (over about 40 characters) will clip on phones.
- Profiles tested with 15 features. With the 21 coded features the dots shrink to about 5px radius at 375px: still legible, but check with real data.
- The dataviz palette validator was not run. The palette is one hue plus status shapes, so CVD separation rests on shape, not hue.
- Minor: years print with a hyphen ("Year -3") rather than a minus sign. "PLACEHOLDER" tags and prose slots stay until real content goes in.
- Not tested: a screen reader pass, and keyboard order beyond the visible focus ring.

## Screenshots (375×812 viewport, iframe harness, headless Chrome)

- Before: `review-pre-light-375.png`, `review-pre-dark-375.png` (full page, shows the 7px chart text and the verdict card).
- After, light: `review-post-l-0.png` (findings), `-750` (findings 2–4), `-1500` (grid), `-2250` (profiles), `-3000` (present row and key), `-3750` (head-to-head), `-4500` (timeline), `-5250` (changes, next tests).
- After, dark: `review-post-d-3000.png`, `review-post-d-3750.png`.
- Decisive-verdict variant with collapsed timeline and changes: `review-post-variant-supported-0.png`.
