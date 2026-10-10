# Triangulation design: is AI a DevOps-like phase change in how firms own their rules?

Protocols for Business · version 1 · 10 October 2026 · pre-registered: committed before any evidence for
it is collected · extends [`research-design.md`](research-design.md) and
[`loop-design-v2.md`](loop-design-v2.md); changes how the end-to-end rerun ([`RERUN.md`](RERUN.md))
organises phases 3 and 4, recorded in `results/rerun-2026-10-10/deviations.md`

## 1. Why this design

The first round and the planned rerun share three weaknesses that a recheck cannot remove.

1. **Selection.** About 1,264 of the corpus's sources were chosen by round one, which already held the
   hypotheses. Splitting them into halves gives two samples with the same bias.
2. **One instrument.** Most evidence passes through one method (activity coding with our codebook). Two
   halves of one instrument agreeing says little; different instruments with different biases agreeing
   says more.
3. **Scale.** About a hundred hand-picked postings per group supports hand coding, not measurement of
   trends, absorption or language change.

This design adds an independent, rule-sampled corpus, runs each established way of forecasting roles on it
as a separate instrument, and tests one general hypothesis against named rivals. Round one is verified
separately (RERUN.md phase 2, unchanged) and compared only at the end.

## 2. The general hypothesis and its rivals

**H-DevOps.** Putting AI agents to work is a phase change in how firms organise, and the work of owning
the rules agents act under will form the way DevOps formed: as a practice before a title, merging work
that two separate functions held, carried by practitioners before vendors and regulators, measured by
shared practitioner metrics, and later renamed or split.

Each historical pattern is reduced to a **signature**: dated features observable in public evidence. The
present-day evidence is coded for those features without reference to which pattern they belong to, and a
script scores the match (section 6). The DevOps signature competes with five rivals.

| Pattern | Origin | Signature features (what the record would show) |
| --- | --- | --- |
| **DevOps** (H-DevOps) | Practitioner movement, about 2008–09 | D1 practice described years before a common title; D2 duties from two previously separate functions in one posting or team; D3 order of first appearance: practitioner community, then open tooling, then vendor certification, then (if ever) regulation; D4 title rises then fragments or is renamed (platform engineering) within about ten years; D5 shared metrics from practitioner research, not regulation; D6 diffusion from software-native firms to enterprises to regulated sectors; D7 more postings carry the practice as a duty or skill than carry the title |
| **SRE** (rival P1) | One firm's internal design, then published | Title and practice appear together; single-firm origin; authority from an owned number (error budget); spreads by imitation of the originating firm |
| **Mandated officer** (P2: CISO, data protection officer, compliance officer) | Law, regulation or board mandate | Title tied to a legal text; senior or executive at first appearance; certification and statute before practitioner community; duties defined by the mandate |
| **Tool-operator fade** (P3: webmaster, prompt engineer) | A new tool or channel | Title boom within two to three years of the tool; duties are operating the tool; folds into many existing jobs; no owned trade-off |
| **Scarcity boom then specialisation** (P4: data scientist) | Talent shortage for a new capability | Title boom with salary premium; later splits into narrower titles (ML engineer, analytics engineer) |
| **Lead-industry diffusion** (P5: brand or product management) | Invented in one industry, carried to others over decades | Mature in one industry long before others; carried by people moving between industries; others copy the leader's structure |
| **Engineering absorption** (P6: rival R1 in loop v2) | No new organisational form | Rule work becomes configuration and policy code in platform teams; no new title, no merged team, no new metric |

**Phase-change claim.** H-DevOps also says the change reaches beyond one role: operating models, team
structure and metrics change. Observable features: F1 firms describe reorganisations that join business
and engineering functions around agents; F2 new standing bodies (councils, committees, a chief AI officer)
with decision rights over agent rules; F3 new operating metrics reported in filings or talks. Refuted as a
phase change if F1–F3 appear in under 5% of filers mentioning agents (section 4.2) and in under 5% of coded
practitioner speech.

## 3. Instruments

Each instrument states its prediction under H-DevOps before it runs, and what would count against it.

| ID | Method | Data | Analysis | Prediction under H-DevOps | Counts against |
| --- | --- | --- | --- | --- | --- |
| I1 | Labour-market signals | Corpus B postings (section 4.1), current and archived | New-title emergence by year; share of postings in each existing occupation carrying agent or rule duties; co-occurrence of duty families | D7 and D2: duty-carrying postings in existing occupations outnumber new-title postings by 3:1 or more, and duties from two O*NET job families co-occur more over time | New titles outnumber duty-carrying existing postings; no rise in cross-family co-occurrence |
| I2 | Activity analysis | Task statements extracted from Corpus B postings and filings | Embed and cluster without our codebook (discovery half), confirm on the holdout half; map clusters to O*NET work activities; then apply the v2 codebook and report what does not fit | A stable cluster joining rule-setting duties (PE, RD) with agent operations (AO) across business and engineering vocabularies | PE and RD fall only in compliance or only in engineering clusters (P2 or P6) |
| I3 | Lead-industry analogue | Archived postings and rule texts for trading and the grid; DevOps history; present postings | Compare the order and timing of role features (D1–D7) in each history with the present; embedding similarity of present agent postings to period postings from each history | Present-day order of features matches DevOps more closely than trading or grid (which are mandate-led) | Present order matches the mandate pattern of trading and the grid |
| I4 | Rules that require roles | EU AI Act Articles 4, 14, 26 and Omnibus; Colorado SB 26-189; California SB 53; RTS 6; NERC PER; postings and filings that cite them | Map required functions; count postings and filings that cite a rule text as the reason for the duty | Under 20% of duty-carrying postings cite a rule text (practice leads law) | 40% or more cite a rule text (P2) |
| I5 | Vendor and tooling signals | Platform documentation defining agent roles; certifications and their launch dates | Date the vendor role definitions and certifications; compare their wording with posting language | Vendor role definitions follow practitioner descriptions (D3 order) | Vendor definitions precede practitioner descriptions and postings copy vendor wording (vendor-led) |
| I6 | Practitioner speech | Loop v2 stratum S7 (`sources-v2/media-current.csv`), as pre-registered | Loop v2 sections 5–9, unchanged | Speakers describe joining business and engineering work around agents, and their own metrics (D2, D5, F1, F3) | Speech describes agent work as one function's tool use (P3) |

**Loop v2** runs as pre-registered, with strata S1–S5 drawn from Corpus B and the new rule-sampled sources
rather than from round one's citations. Its hypotheses (H-cal, H-speech, H-absorb, H-federated, H-number,
H-agreement) are reported as written.

## 4. Corpus B: independent, rule-sampled

No source cited in round one is selected by these rules on purpose; overlaps that occur by chance are kept
and counted.

### 4.1 Postings

- **Frame:** the 550 employers in `corpus/staging/s1-employer-frame.csv` (Fortune 500, 2025, plus 50
  venture-backed software firms), as built for loop v2 stratum S1.
- **Board discovery:** for each employer, detect a public job board on Greenhouse, Lever, Ashby,
  SmartRecruiters or Workday by scripted probes of the employer's name and career-site links. Record the
  method and failures. No search for topic words.
- **Current crawl:** every open posting on each discovered board (full text, title, location, date where
  given).
- **Historical crawl:** Internet Archive captures of the same board pages and endpoints, one capture per
  employer per half-year, 2019–2026. Coverage is measured and reported per year; trend claims use only
  years with 30% or more employer coverage.
- **Occupation mapping:** titles mapped to O*NET-SOC codes by a fixed title dictionary, with model
  assignment for unmatched titles and a 200-posting hand check.

### 4.2 Filings

- SEC EDGAR full-text search, 10-K and 10-Q, 2022 to October 2026, for: "AI agent", "AI agents",
  "agentic", "autonomous agents", "digital workers", "digital labor". Denominator: every 10-K filed by the
  same population in each year. Sections kept: business description, risk factors, controls and procedures
  (Item 9A), management's discussion.
- Codes: F1–F3, D2, and whether a rule text is cited (I4).

### 4.3 Historical pattern sources (for signatures)

Primary and dated sources for each pattern in section 2: for DevOps, the first DevOpsDays programme (2009),
the Velocity 2009 talk on ten deploys a day, the annual State of DevOps reports (2013 onwards), the
Accelerate metrics (2018), the CNCF platforms white paper (2023), and archived DevOps engineer postings;
for each rival, the sources in `sources-v2/media-historical.csv` and the role histories in loop v2 section
8, checked against primary texts. Signatures are written and committed **before** any present-day coding.

### 4.4 Also in Corpus B

Rule-change events (`corpus/staging/planned-4.6.csv`), research reports (4.1), rule texts (4.2),
capability models (4.4), IAPP proxies (deviation 2) and the media frames, all chosen by the acquisition
plan's rules rather than by round one.

## 5. Extraction and analytics

- **Task extraction:** one model (Haiku, through the Batch API) extracts task statements from each posting
  and filing passage, verbatim spans only. A second model (Sonnet) extracts from a random 10%; agreement
  (span-level F1) is reported, and extraction is accepted at 0.7 or more. A person checks 50 records by
  hand before analysis.
- **Sampling for extraction:** all postings in the ten S1 occupations and all new-title postings; a
  stratified 20% of the rest, with a fixed seed.
- **Embeddings:** an open sentence-embedding model run locally; model and version recorded.
- **Clustering:** discovery on a random half of task statements (seed 20261011), confirmation on the other
  half; a cluster counts as found only if it reappears in the holdout half with adjusted Rand index of 0.6
  or more against the discovery assignment and at least 30 members. Three repeated runs give the noise
  baseline (as loop v2, section 7).
- **Codebook stage:** only after clusters are fixed, apply the v2 codebook (PV, PE, RD, AO, OT) with two
  coders of different models; report what fraction of each cluster the codebook cannot place.

## 6. Pattern matching

1. **Signatures first.** For each pattern in section 2, a historian agent writes the dated signature from
   section 4.3 sources only. Committed before step 2.
2. **Feature coding, blind to patterns.** Fresh coders, who see only the feature definitions (D1–D7,
   F1–F3, and the rival features rewritten as neutral features with no pattern names), code the present-day
   evidence from I1–I6. They do not see which pattern a feature belongs to.
3. **Scoring by script.** Each pattern's match score is the share of its features observed in the
   present-day coding, weighted equally. H-DevOps is **supported** if DevOps scores highest and at least
   0.15 above the next pattern; **partly supported** if it ties (within 0.15) with one rival; **not
   supported** otherwise. Ties are reported with the features that separate them.
4. **Time.** Agent-era evidence is about three years old. Features that need a decade (D4, fade) are scored
   as early signs only and flagged; the verdict is re-scored at each forecast check date.

## 7. Order and blinding

1. Commit this design (done before any Corpus B collection).
2. Build Corpus B; write signatures (section 6.1); commit.
3. Run I1–I6, extraction, clustering and feature coding. Agents receive only corpus text, this design's
   definitions and their prompt. They do not open `results/loop-2026-10-10/`, `results/industry-2026-10-10/`,
   `roles/*.md`, `exploratory/`, the published report or the README status table.
4. A fresh agent writes the Corpus B findings. Committed.
5. Only then: RERUN.md phase 2 verification of round one, and the comparison.
6. Comparison grid: hypotheses (research-design H1–H8, loop v2, H-DevOps and F1–F3) against instruments
   I1–I6. A finding is **strong** if three or more instruments with different data support it, **single-
   instrument** if one does, and **round one only** if it appears in the verified round-one findings and in
   no instrument.

The orchestrating session has read round one's README status table; it does not draft findings or
verdicts.

## 8. Models

Collection, crawling scripts and extraction: Haiku and Sonnet. Feature coding: two different models
(Sonnet and Haiku). Signatures, red team, findings and the comparison: Opus, in fresh agents.

## 9. Outputs

In `results/rerun-2026-10-10/`:

- `corpus-b/`: frame, board discovery log, crawl index, filings index, coverage tables (no posting text or
  filing text committed beyond quotes of 40 words or fewer)
- `signatures.md`: dated signatures per pattern, before present-day coding
- `instruments/I1.md` … `I6.md`: each instrument's method, result and prediction check
- `clusters/`: discovery, holdout, stability, codebook overlay
- `pattern-match.md`: feature coding and scores
- `findings-corpus-b.md`, then `comparison.md`, `findings.md`, `exec-summary.md`, `recommendation.md`
- `field-plan.md`: hypotheses that need field evidence, types of firm to visit and named candidate firms
  (from public signals only; no individuals named), interview guide, and what an interview would have to
  show to refute each hypothesis

## 10. Limits

- The frame is US-listed and large firms plus a few software firms; small firms and non-US firms are
  under-represented.
- Public job boards on Greenhouse, Lever and Ashby lean to software firms; Workday and SmartRecruiters
  coverage is measured and reported.
- Postings describe what employers say they want; filings describe what firms disclose. Neither is
  observed work. Field visits are the test.
- Archive coverage of job boards before 2022 is uneven, so long trends are weak.
- DevOps is itself ongoing; its later features (D4) are judged from about fifteen years of history.
- Coders and historians share model knowledge of how DevOps turned out; feature coding is blind to pattern
  names to limit this, not to remove it.

## Addendum A (10 October 2026, before any present-day coding)

Added after the round-1 signatures (`results/rerun-2026-10-10/signatures.csv`, 133 cells: 88 P, 6 R, 39 NF)
and before any Corpus B evidence was coded. No present-day evidence had been coded or read for features
when this was written.

1. **Signatures supersede section 2's wording.** The DevOps features in section 2 were written before the
   historian's work. The evidence contradicts two of them: open tooling came before the first community
   (D3), and the rename came about 14 years after 2009, not about 10 (D4). The scored profiles are the
   historian's, not section 2's.
2. **Power check.** On the 14 features observable within about three years, a present identical to the
   DevOps profile beats the next pattern (scarcity boom, P4) by 0.05, against the 0.15 margin in section
   6.3. With simulated coding noise, H-DevOps could come top but could never be "supported". The test as
   written could not support the hypothesis.
3. **Fixes.**
   - (a) Round 2 of the signatures splits the late features into early and late halves and adds early
     discriminators (N20–N24), with the same source rules.
   - (b) **Scoring.** score = 1 − mean |present − pattern| over the features that are graded (not NF) in
     the pattern and observable now. yes = 1, partial = 0.5, no = 0.
   - (c) **Margin.** The margin is set by simulation on the final signatures, before coding. Each pattern
     is taken in turn as the truth. Coding noise is q = 0.2: each feature moves one step with probability
     0.2. The margin is the smallest value at which a pattern that is not the truth reaches "supported" in
     no more than 5% of 2,000 runs, across all truths.
   - (d) **Families.** Any patterns whose ideal profiles are still within that margin on observable
     features form a family. The verdict is first given for the family, then within it as "not yet
     distinguishable", with the features that would separate them and a date to check them.
   - (e) Section 6.3's fixed 0.15 is replaced by (c). Section 6.4 still applies.
4. The simulation script and its output are committed with the round-2 signatures, before step 2 of
   section 6.
