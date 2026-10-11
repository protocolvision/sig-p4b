# Editorial review: Who Owns the Rules (interactive)

## Verdict

The argument and visual language are strong. Three things block launch:
- The headline number contradicts the page: "0" vs "rarely named" vs vendor quotes that name a decider.
- The menu button shows on desktop.
- Key figures break on phones: the "0" row is cut off, roadmap and filings text is 5–7px, and the reach table hides its key column.

## 1. Storyboard

What goes wrong:
- **Personal AI breaks the main thread.** It interrupts Tools → Roles, the payoff of Ch1–2, and it answers a separate boundary question.
- **Roles is the synthesis.** Put it straight after Ch2.
- **Law drives "What to do"** (the 2027 deadline) but arrives late. Put it after Roles.
- **The design-vs-runs step at the end of Ch2 is stranded** over an unrelated product grid. It explains move 2 of the roadmap, so it belongs there.
- **Missing: a one-line definition of "an agent's rules".** The page uses rules, limits, guardrails and design interchangeably.
- **Missing: a one-line sources strip under the short version.** Reuse the funnel numbers so "how do you know" is answered early.

Proposed order:
1. Hero
2. Short version, plus the sources strip
3. Ch1 Work
4. Ch2 Tools
5. Roles
6. Law
7. Context: Functions, DevOps, 10-K filings
8. Personal AI
9. What to do, with design-vs-runs inside move 2
10. Try it
11. How we know, with the rests-on and sources drawers


## 2. Readability: rewrites

1. Hero stat. Now: "0 statements or postings describe deciding a rule change across functions". Rewrite: "**0** of 771 practitioner statements and 25,512 job postings describe who decides a rule change across functions."
2. Ch2 h3. Now: "an admin decides what the agent may do". This contradicts the thesis. Rewrite: "an admin **edits** what the agent may do."
3. Ch2 h3. Now: "If no one is named, where do the changes happen?" This is a question, not a finding. Rewrite: "We read 31 products' documentation to see where rule changes happen."
4. Card 1. Now: "For every 100 job ads with an AI title, about 86 ads with an ordinary title … also list agent work." Rewrite: "Agent work is nearly as common in ordinary jobs as in AI jobs: 86 ordinary ads list it for every 100 AI-titled ones."
5. Ch1 step 4. Now: "The coders could see this work: they caught 94–100% of hidden test examples of it." Rewrite: "It is not a blind spot in our method: when we planted examples, the coders found nearly all of them." Put the figure in a bubble.
6. Ch1 step 1. Now: "Two coders from different model families sorted each statement blind." This never says the coders are AI. Rewrite: "Two AI models from different vendors sorted each statement independently."
7. Ch2 note. Now: "Our pre-set test needed two-thirds…mixed rather than conclusive." Rewrite: "15 of 26 products name an editor: a majority, short of the two-thirds we set in advance."
8. Method h2. Now: "Three hundred thousand duties sorted into eight stable bundles of work, and only one involves AI". Rewrite: "Across 300,000 job duties, only one kind of AI work recurs consistently: security review of AI systems."
9. Walk step 04. Now: "114 bundles; eight reappeared in the held-out half". Rewrite: "We grouped similar duties into 114 clusters and rechecked them on unseen postings. Eight held up (green); the big AI clusters (blue) did not."
10. Roles › Reviewers. Now: "the one stable AI bundle of duties … in the held-out half, 24 of the bundle's 53 duties come from one posting". Rewrite: "the only AI role that recurs consistently. Low confidence: much of the confirming data is one posting."
11. Roles › gap. Now: "The edit has an owner, a product permission." Rewrite: "Making the edit is a permission someone holds. Deciding it is not."
12. Law intro. Make the finding come first: "Of 111 provisions in 19 laws and policies, only trading rules and AI labs' own policies name who decides a change. AI law names no one."
13. DevOps figure h3. Now: "AI agents got both within about three". The law is only scheduled. Rewrite: "…AI agents had certification within a year and face binding law within three."
14. Roadmap move 2. It cites "finding 5", but the page has no numbered findings. Rewrite: "Follows from how agent platforms work (chapter 2)." Cut the 120-word detail to about 50 words; the Microsoft example goes in a bubble.
15. Roadmap move 4. Now: "We build Business Protocol Management…" Rewrite: "We sell services in this area, so we treat anything that would favour them as unproven."

Also fix:
- **Undefined terms.** Gloss "10-K" (US annual reports), MCP/A2A/AP2/ACP, "tenant restrictions", "domain capture" and "deployers". Replace the cite "M072" with "Sales leader, podcast, 2026".
- **"Sources quoted" uses internal IDs** (`C9b1da45a`, `Cef3dde3f`, `sf-guard`, `R-251199`). Use readable titles and links; leave the IDs on GitHub.
- **Two units for practitioners.** The hero says "20 of 30 practitioners"; Ch1 says "of the 30 recordings" and "38 recordings". Pick one unit and say why 30 of 38.

## 3. What moves to explainers

Use one pattern throughout: an "i" bubble, a 24px target that opens on hover, focus or tap and closes on Esc. On desktop, use right-gutter margin notes in the scrolly chapters; below 860px they collapse into the same bubble. Show confidence as a small High/Med/Low chip that opens a bubble.

Bubbles:
- 94–100% detection (Ch1 step 4)
- How the statements were coded (Ch1 step 1)
- The two-thirds test (Ch2)
- Protocol acronyms (Ch2 grid header)
- Dashed-edge legend and fetch date (reach table header)
- "Read with care" 82/95/85/7.8% (Functions, beside the h2)
- The agent start-date caveat (DevOps figcaption)

Margin notes:
- "Three sales managers = 89 statements" (Ch1)
- "No law asks firms to register agents" (Ch2)

Confidence chips: every "Low/Moderate/High confidence" line in the role panels and roadmap moves.

Footnote drawer ("Checks"): precision/recall, pre-registration, red team, script-checked quotes (Method), and the Gartner/Netskope sourcing (Personal AI).

## 4. Visuals and animation

- **Hero dots.** They use green for running agents, while Ch1 uses grey for running and green for limits. Pick one mapping. The drift never stops; halt it after about 8s or when the hero scrolls offscreen (WCAG 2.2.2, battery).
- **Ch1 sort.** The fixed ratio leaves 40% of the desktop panel empty and clips the "0" row on phones. Compute the height from the rows. Labels at 45% alpha are faint.
- **Ch2 grid.** Clear, and it needs the legend. Dimming to .28 makes tiles unreadable; use .45.
- **Functions.** `preserveAspectRatio="none"` stretches dots into ellipses and widens text. The columns have no scale, so 16.3% and 10.5 per 1,000 look alike; add a max tick under each header. Delete the injected note about practitioner recordings (there is no such column). The hidden caption says four measures; there are three.
- **DevOps bars.** Good, but the AI values imply different start dates: 0.3 years to certification means about Dec 2024, while 2.6 years to law means mid-2024. Use one start date. The default `figure` margin indents the block by 40px.
- **Filings.** The fixed 520 viewBox shrinks text to about 6px on phones. Define "employers studied".
- **Roadmap.** The weakest figure. The text is in viewBox units, so it renders at 22px on desktop and about 5px on phones, and moves 1–3 all show the same bar. Rebuild it in HTML: four rows, one per move, each a bar from today to its deadline, crossed by the Colorado and EU lines.
- **Method map.** Strong, but it opens on step 04 so readers miss 01–03. Start at 01. The "AI use cases" and "AI governance" labels overlap.
- **Faux bold.** `<b>` (700) is synthesised from Lora 600, which gives the odd spacing in "What firms can do", the Try-it titles and the move titles. Fix with `b, strong { font-weight: 600 }`.

## 5. Accessibility

- **Broken `:root` block (lines 11–40).** The `.menu-btn` and `@media` rules are pasted inside `:root` before `--band-fg`, `--serif` and `--mono`. Browsers without CSS nesting drop those tokens. Move lines 21–32 out of the block.
- **`.menu-btn { display:none; all:unset }`.** `all:unset` cancels `display:none`, so the button shows on desktop. Reorder the two.
- **Faded steps.** Inactive steps at opacity .35 give about 2:1 contrast. Use .55 or more.
- **`#prod` uses `role="img"`.** This hides all 31 product names from screen readers. Use one `<ul>` per group, with hidden status text for each product.
- **Reach table.** Add hidden "(inferred)" text to the dashed cells.
- **Functions cells.** Add hidden "16.3%, range 13.7–19.4".
- **Filings `<rect role="button">`.** Use a radiogroup with arrow keys, or a native `<select>`, and check that the focus ring shows.
- **Panels.** The roles and move panels need `aria-labelledby`, and the roles panel needs an `h3` in place of `p.kick`. The Try-it items are `<p><b>`; make them `h3`.
- **Menu.** Esc closes it but doesn't return focus to the button.
- **Touch targets** under 44px: tabs (about 28px), method steps (about 30px, labels hidden under 520px), filings years.

## 6. Mobile (390px)

The phone-specific problems are already listed above: the clipped "0" row, the reach table, the squashed Functions table, unreadable roadmap and filings text, and step labels reduced to "01–05". One more: the pin plus the sticky bar take about 45% of the screen, so cap the pin at 40vh.

## 7. Prioritized fixes

**P1 (before launch)**
1. CSS: move lines 21–32 out of `:root`.
2. `.menu-btn`: put `display:none` after `all:unset`.
3. Reconcile 0 / rarely / no visible owner. Use rewrite 1, and change the gap button to "named only in a few vendor designs".
4. Ch2: change "an admin decides" to "an admin edits".
5. Ch1 canvas: set the height from the rows, so the "0" row shows on phones and the desktop panel isn't empty.
6. Roadmap: rebuild responsively and drop "finding 5".
7. Filings chart: make it responsive (measure width as `cmpbars` does).
8. Reach table: cards under 640px.
9. DevOps figure: fix the start date, and change "got both" to "face binding law".
10. Hero: "31 agent products and protocols", and one unit for practitioners.

**P2 (should)**
1. Reorder the sections as in §1 and update the nav.
2. Apply rewrites 5–15, and replace the source IDs.
3. Add the bubbles, margin notes and confidence chips from §3.
4. Everything else in §4 and §5 not listed under P1.

**P3 (nice)**
1. Start the method walkthrough at step 01, and fix its overlapping labels.
2. Use "Explore" kickers only on interactive sections.
3. Personal AI examples lean on Anthropic and Claude; add one Microsoft or Google example per layer.
4. Recheck the counts against `report-plan.md`, which lists 862 statements and "7 of 11" staffing speakers. The page says 771 and "6 of 10".
