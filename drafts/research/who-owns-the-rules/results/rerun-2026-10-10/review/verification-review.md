# Review of the phase 2 verification (spot check of 30 verdicts)

Scope: `verification-{loop-analysis,loop-redteam,industry,random150}.csv` and their `.md` summaries.
Sample: 30 verdicts drawn with `random.seed(31)`, stratified 8 / 8 / 8 / 6. Within each stratum, "corrected" and "not found" rows were drawn first (3 / 3 / 4 / 3), so 13 of the 30 are those verdicts, and the rest were drawn from the other rows.
Method: each verdict was re-checked against `corpus/text/`, the round-one files and the loop data. `loop-tools/analyze.py` was rerun on `results/loop-2026-10-10`, and its output is byte-identical to `analysis.md`. The industry means and the 20,000-weighting robustness figure were recomputed from `scores-A/B.json`. The corpus-wide searches used all 1,266 texts. No round-one or verification file was edited.

## 1. Per-verdict agreement

Agree = the verdict and the correct_value both stand. Category = the facts are right, but the claim is a bare list marker or another non-claim that should not be counted as "confirmed".

| # | Slice | Claim | Verifier verdict | Review | Note |
|---|---|---|---|---|---|
| 1 | loop-analysis | CL0094 | corrected | Agree | "HR service representative (tier 2)" and "help desk agent" are not attested as human titles. The only "helpdesk agent" hit (C26c0c603) is an AI agent. |
| 2 | loop-analysis | CL0181 | corrected | Agree | C85ecc82f reads "Review **Fin** conversations weekly…", so the quote in quotation marks is altered. The R8231 PV secondary comes from coder B only, which the claim states correctly. |
| 3 | loop-analysis | CL0182 | corrected | Agree (minor) | Coder A: "tools, not rules"; coder B: "no cross-functional trade-off". "Both noted not cross-functional" is a slight overstatement. |
| 4 | loop-analysis | CL0099 | confirmed | Agree | C7 has 17 records (rerun). "AI Steward" appears 7 times in Cf7d364f5. |
| 5 | loop-analysis | CL0051 | confirmed | Agree | Reproduced by the rerun of analyze.py. |
| 6 | loop-analysis | CL0019 | confirmed | Agree | Reproduced by the rerun. |
| 7 | loop-analysis | CL0088 | confirmed | Agree | Reproduced by the rerun. |
| 8 | loop-analysis | CL0006 | confirmed | Agree | Reproduced by the rerun (RD 0/0/0). |
| 9 | loop-redteam | CL0130 | corrected | **Overturn → confirmed** | See section 2. |
| 10 | loop-redteam | CL0122 | corrected | Agree | All 13 C4 records are S1. 2 come from a Yahoo Finance article (D782) and 1 from a ZipRecruiter results page (D214). |
| 11 | loop-redteam | CL0147 | corrected | Agree | The five postings supply 19 of 29 records (5+5+4+3+2). 20 holds only if the direct Databricks page D638 is added. |
| 12 | loop-redteam | CL0124 | confirmed | Agree | 15 of 17 are S5 vendor docs; 2 come from EY D114. |
| 13 | loop-redteam | CL0162 | confirmed | Category | "1." is a list marker. It should be unverifiable / not a claim, not confirmed. |
| 14 | loop-redteam | CL0165 | confirmed | Category | "2." Same problem as CL0162. |
| 15 | loop-redteam | CL0116 | confirmed | Agree | Recount: 40 records over 8 clusters; C7 has 13 (32.5%). |
| 16 | loop-redteam | CL0117 | confirmed | Agree | All 10 named records are in C7 and come from vendor admin docs. The note correctly says some record quotes are not in the stub texts. |
| 17 | industry | CL0251 | corrected | Agree (low confidence) | UK certification is firm-made under SYSC 27.7 and has no exam, so the correction holds. "Exam machinery" could also be read as supervisory examinations, which would weaken the correction. |
| 18 | industry | CL0204 | corrected | **Overturn → unverifiable (facts confirmed)** | See section 2. |
| 19 | industry | CL0243 | corrected | Agree | Recomputed: trading or grid first in 87.6–87.9% of flat-Dirichlet weightings; trading beats the grid in about 91–92%. The "coin toss" does not come from the weights. |
| 20 | industry | CL0210 | corrected | Agree | C4b3f4f11: "Experience level Director", NAM head reporting to the Global Head of ETRC, MSS COO function (2021). "Mid-level" is wrong. |
| 21 | industry | CL0222 | confirmed | Category | "4." is a list marker; the verifier's own note says "no checkable content". |
| 22 | industry | CL0258 | confirmed | Agree | FIA C6ca2423e dated "27 April 2010". C4f61e392: "Release No. 61379 (January 19, 2010)". |
| 23 | industry | CL0249 | confirmed | Agree | "Partly refuted" matches findings.md, and the ecommerce CSV has MRC 2002 and CCU 2020 with lever none. "If anything harsh" is opinion. |
| 24 | industry | CL0257 | confirmed | Agree | Knight on 1 Aug 2012 (Cb7cdbe95); 34-77551 on 7 Apr 2016; effective 30 Jan 2017 (C6b47f19f). The intervals are 3.7 and 4.5 years. |
| 25 | random150 | CL2502 | not found | **Overturn → confirmed** | See section 2. |
| 26 | random150 | CL2136 | not found | Agree | Not in C91e33f0b or C30b30ff2 (50 items), and C36fc6e16 (34-76188) is a 1.6 kB stub. A corpus-wide search for the 125/22/12/79 breakdown finds nothing. |
| 27 | random150 | CL1850 | corrected | Agree | The C5ba4d90b page title is "Mastering Implementation-Grade GRC Engineering". |
| 28 | random150 | CL0967 | unverifiable | **Overturn → confirmed** | See section 2. |
| 29 | random150 | CL1060 | confirmed | Agree (caveat) | The quote is verbatim in C67a6dd21, but that page is the Jobs for Humanity SmartRecruiters copy. The "YUPRO version" attribution was not checked. |
| 30 | random150 | CL0903 | unverifiable | **Overturn → confirmed (partial)** | See section 2. |

Totals:
- 22 of 30 agree outright.
- 3 are category errors (list markers marked "confirmed").
- 5 are substantively overturned.
- Of the 13 sampled "corrected" or "not found" verdicts, 11 stand. 1 is overturned (CL0130), and the "not found" for CL2502 becomes "confirmed". CL0204 is a "corrected" that should be unverifiable.

By slice: loop-analysis 8/8, loop-redteam 5/8 (1 substantive), industry 6/8 (1 substantive), random150 3/6 (3 substantive).

Correct_value check: all correct_values on the upheld corrections are accurate. Two are not:
- CL0130's correct_value ("the wording is iteration 5 C7") answers a different question.
- CL0204's correct_value substitutes the red team's judgement for the findings' judgement.

## 2. Overturned verdicts

| Claim | Verifier | Right verdict | Evidence |
|---|---|---|---|
| CL0130 (red-team.md 27): "The 'admitting agents' cluster first appears at that point, in iteration 3." | corrected | **confirmed** (wording nit only) | `clusters/iter-3.json` has C6 "Registering agents as identities, naming a human owner and business sponsor…" and C7 "Deciding which agents and agent capabilities the organization allows: approving agents for the shared catalogue…". Iterations 1–2 have no such cluster. Iteration 3 is the first after S5 entered, which is what the sentence claims. The verifier objected only that the literal label "Admitting agents" first appears in iteration 4. The red team itself says iteration 3 was "split between C6 and C7". |
| CL0204 (findings.md 25): H-bridge "Supported, weakly…" | corrected (to "untested") | **unverifiable** (role facts confirmed) | The factual parts hold. Series 57 covers persons "primarily responsible for the design… of an algorithmic trading strategy" (C6b47f19f), and the NERC certified operator appears in C84c34c54. Whether the hypothesis is "supported weakly" or "untested" is an interpretive call against `industry-analogue-design.md` s5. The pre-registered refutation ("general or pure technical roles") is not met. The verifier replaced the findings' judgement with the red team's, which is not something a source can settle. |
| CL2502 (role-emergence.md 230): "late 2022 \| First staff prompt engineer, at Scale AI" | not found | **confirmed** | The verifier searched only the two cited ids. The corpus has two more sources. Cb88035da (pedaily, Dec 2022, URL `/202212/`) says Goodside quit his job on 29 Oct, Scale AI formally hired him as "Prompt Engineer" after ChatGPT went viral, and the CEO called it the first such position in the industry. C3593f1a3 (Interconnects) says he "joined Scale around when ChatGPT came out". "Staff" is attested from 2023 (C325a0a40, Cd13d7a36). |
| CL0967 (timeline-algorithmic-trading.md 51): "Shareable algorithm certificates (2026, FIX; S)." | unverifiable ("No FIX algorithm-certificate source in corpus") | **confirmed** | Cbf0d4d5c (Mondo Visione, 03/06/2026): FIX released Recommended Practices for Algorithm Testing and Certification. They cover "approving an algorithm as being suitable for production usage and communicating that in the form of a certificate" to "counterparties and regulators". The CSV row (line 55) also cites a June 2026 report. |
| CL0903 (timeline-electricity-grid.csv 32): FERC approves a $25m FPL settlement in 2009; FRCC pays $350,000 in 2010 | unverifiable ("Troutman page not acquired") | **confirmed (partial)**, per the verifier's own compound-claim rule | C811f2a93 (FERC, 129 FERC ¶ 61,016, Oct 2009): "FPL has agreed to pay a civil penalty of $25,000,000" over the 26 Feb 2008 Florida Blackout. C04eeec59 confirms a separate FRCC settlement (130 FERC ¶ 61,163, 2010). The $350,000 amount and "largest since 2007" are not in the corpus. |

## 3. Systematic problems

1. **random150 does not search the corpus beyond the cited ids, although its method note says it did.** 3 of the 5 non-confirmed random150 verdicts in the sample are wrong. In each case the passage is in the corpus under a different id: a Chinese-language article, a trade-news page and the FERC order itself. One out-of-sample probe found the same failure:
   - CL2504 ("2024: US agencies required to name Chief AI Officers") is marked unverifiable with "M-24-10 itself not in corpus".
   - But C3ea5c448 (Crowell, 2024) states that M-24-10 (28 March 2024) requires all agencies to designate a CAIO.

   The pattern is consistent: the verdict follows the acquisition status of the cited id ("not acquired", "acquisition failed"), not a search of the corpus.

   Consequences:
   - The 37% unverifiable share is overstated.
   - The headline error rate is biased upward. With the four cases above reclassified, it is 18.4% (18/98), down from 20.0%.
   - How many more random150 rows would move is unknown.
2. **"not found" is used for forecasts and opinions in the industry slice.** Eight of the 10 industry "not found" verdicts are forecasts or interpretation, not missing evidence: CL0221, CL0229, CL0230–0234 and CL0256. These should be unverifiable. The `.md` summary says this for CL0230–0234 but still counts them as not found, which inflates the industry error count. CL0252 is really a "corrected" (counter-fact found: NERC certification).
3. **List markers count as "confirmed" in two slices.** Bare ordinals are marked "confirmed" in loop-redteam (7) and industry (5), and unverifiable in random150. Industry also has 4 more "confirmed" rows whose notes say the claim is not checkable. This inflates confirmed counts by about 12 in loop-redteam and industry. It does not hide any error.
4. **Judgement calls are relabelled as corrections.** One sampled case does this (CL0204), and the industry `.md` describes a similar approach to the H-verdicts. Where findings.md and red-team.md disagree on an interpretation, the verifier sides with the red team and calls it a correction.
5. **No evidence of rubber-stamping.** None of the 17 sampled "confirmed" verdicts was wrong on substance. Every one either reproduced from the data (the loop rerun is byte-identical) or had the passage verbatim in the cited text. The verifiers often flagged partial support in the note (CL0117, CL1060).

## 4. Overall judgement

- **Loop slices (analysis and red team): reliable.** Every computed figure reproduces. The corrections are real and correctly valued. The only faults are one over-literal correction (CL0130) and the list-marker bookkeeping.
- **Industry slice: largely reliable on facts.** Dates, recomputed scores and corrections all held. Its verdict counts are not usable as an error rate: "not found" includes forecasts and opinions, and some "corrections" are disagreements of interpretation.
- **random150: "confirmed" and "corrected" can be relied on; "not found" and "unverifiable" cannot.** 3 of 5 sampled non-confirmed verdicts were overturned by a plain corpus-wide search. Before the 20% (13–29%) error rate or the 37% unverifiable share is quoted, every random150 "not found" and "unverifiable" row whose claim names a figure, date or quote should get a corpus-wide search (roughly 40 rows). Until then the error rate should be presented as an upper bound.

In short: a verdict of "confirmed" or "corrected" can be trusted as stated. A verdict of "not found" or "unverifiable" in random150 cannot, and that is where the published error rate comes from.
