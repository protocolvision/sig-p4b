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

### Amendment A.1 (same day, still before any present-day coding)

1. **Calibration.** The rule in A.3(c) gave a margin of 0.01: it simulated only presents that were noisy
   copies of one pattern. It now also requires that no pattern reaches "supported" in more than 5% of runs
   when the truth is a 50/50 blend of any two patterns, or a random profile
   (`loop-tools/pattern_power.py`).
2. **Result on round-2 signatures** (22 features observable now):
   - q = 0.2: margin **0.17**; when DevOps is the truth it is supported in 91% of runs.
   - q = 0.3: margin **0.20**; 62%.
   - With the round-2 features, every pattern's ideal margin is above both thresholds, so there are no
     families.
   - Outputs: `results/rerun-2026-10-10/pattern-power-q0.2.md` and `pattern-power-q0.3.md`.
3. **Which margin applies is fixed now.** The present-day feature coding uses two coders (section 6.2).
   - If their per-feature disagreement rate is 0.25 or less, the margin is 0.17.
   - If it is above 0.25, the margin is 0.20.
   - If it is above 0.35, the pattern verdict is reported as unreliable and only the feature-level results
     are given.
4. **Interpretive features.** N20, N22 and N23 depend on how sources state purpose and framing. Their
   coding definitions are written in the feature-coding prompt before coding starts and are not changed
   afterwards.

### Amendment A.2 (same day, still before any present-day coding)

Answers the collection-pipeline review (`results/rerun-2026-10-10/review/pipeline-review.md`), findings
C4, C6 and C7. No present-day evidence had been coded when this was written. Changed files:
`loop-tools/pattern_power.py`, `loop-tools/leak_check.py`, `loop-prompts/feature-coding.md`. New outputs:
`results/rerun-2026-10-10/pattern-power-v2-q0.2.md` and `pattern-power-v2-q0.3.md`. The A.1 outputs
(`pattern-power-q0.2.md`, `-q0.3.md`) are kept as the record of the superseded rule.

**Scoring (C4)**

1. **Noise.** When a feature is chosen for noise (probability q), a 0 or 1 now always moves inward to 0.5,
   and a 0.5 moves to 0 or 1 at random. Before, the code drew ±0.5 and clipped, so an extreme value moved
   only half the time it was chosen, and the real noise on yes/no cells was about q/2. (C4.1)
2. **NF in truth presents.** When a pattern is the simulated truth, each feature it grades NF takes a
   random value from {0, 0.5, 1}. The same applies to each parent's NF cells in a blend. NF is never
   entered as "no". Before, all NF cells carried `value = no` and became fabricated observations. (C4.2)
3. **Comparable scores.** Every pattern is scored on one common feature set: the observable-now features
   graded (not NF) in at least 5 of the 7 patterns. That gives 15 features: N01, N02, N03, N04a, N06a,
   N08, N09, N12, N13, N15, N19, N20, N21, N22 and N23.
   - Not scored, because they are graded in too few patterns: N05 (4 of 7), N07 (3), N10 (3), N11 (2),
     N14 (3), N16a (3) and N24 (2). They are still coded and reported feature by feature, except N16a
     (point 6).
   - Where a common feature is NF for a pattern, that cell is missing for the pattern. The raw score is
     standardised: 1 − mean |present − profile| over the cells the pattern grades.
   - Missing cells: SRE N04a; Mandated officer N23; Lead-industry N03, N13 and N04a; Engineering
     absorption N12, N13 and N21.
   - Each pattern's raw score is then converted to a mid-rank percentile against that pattern's own
     null: 20,000 uniform random presents over the same features, seed 20261012. Ranks, "supported",
     "partly supported" (section 6.3, as amended by A.3(e)) and margins all use these percentiles. Margins
     are in percentile points.
   - Reason: patterns were scored on 14–20 features of their own. NF worked as a free pass, and random or
     ambiguous evidence favoured patterns with many NF or partial cells. (C4.3)
   - Null check (uniform presents, one coder, no noise; 10,000 draws; 1/7 = 14.3%):

     | Pattern | Top share, A.2 rule | Top share, A.1 rule |
     | --- | --- | --- |
     | DevOps | 13.3% | 10.0% |
     | SRE | 13.3% | 13.2% |
     | Mandated officer | 16.1% | 27.6% |
     | Tool-operator fade | 12.4% | 10.5% |
     | Scarcity boom | 11.1% | 6.9% |
     | Lead-industry | 15.1% | 13.0% |
     | Engineering absorption | 18.6% | 18.8% |

     Under A.2 the range is 11–19%, against 7–28% under A.1. The tilt is smaller but not gone, because
     the 15 features are shared and correlated across profiles. Engineering absorption, not DevOps, is
     now the most favoured pattern under the null.
4. **Coders.** The simulation and the scoring rule now use two coders. Each coder's values get their own
   noise and are scored separately (raw score, then percentile). A pattern's score is the mean of the two
   coders' percentiles. Values are never averaged into "partial". Before, averaging pulled every
   disagreement toward 0.5, which fed the tilt in point 3. (C4.3)
5. **Blends.** The margin must satisfy four conditions, each at the 5% false-support bound:
   - when any pattern is the truth, no other pattern is supported;
   - under the feature-wise average blend of any two patterns, no pattern is supported (off-grid values
     0.25 and 0.75 move 0.5 toward the middle when chosen for noise);
   - under the 50/50 random mixture of any two patterns (each feature taken from one parent at random),
     no pattern is supported;
   - under the uniform null, no pattern is supported.

   There are 2,000 runs per truth, per pair and blend type, and for the null. The margin is the smallest
   value, in steps of 0.01, that meets all four. The mixture blend is the binding condition at both
   values of q (Engineering absorption at 5.0%). Before, only the average blend was tested, with 500 runs
   per pair. (C4.4)

**Feature sources (C7)**

6. **Every feature now names its source.** The prompt's new table "Where each feature is answered" names
   the file and column for each feature. These instrument outputs must carry the named columns before
   coding starts:
   - `I1-postings.csv`: `posting_id`, `employer`, `sector`, `firm_type`, `posted_date`, `title`,
     `onet_code`, `onet_family`, `agent_duty`, `agent_title`, `duty_families`, `duties_text`,
     `requirements_text`, `purpose_statement`, `seniority`.
   - `I1-titles-by-year.csv`: `year`, `title`, `agent_title`, `postings`, `employers`,
     `share_agent_duty_postings`.
   - `I1-coverage.csv`: `half_year`, `employers_covered`, `share`.
   - `I2-tasks.csv`: `task`, `source_type`, `doc_date`, `performer`, `org_unit`, `cluster_id`.
   - `I2-clusters.csv`: `cluster_id`, `label`, `stable`, `n`, `onet_families`.
   - `I6-speech.csv`: `item_id`, `date`, `employer`, `employer_software_native`, `speaker_seniority`,
     `speaker_org_unit`, `speaker_path`, `in_company_agent_work`, `firm_cited_as_model`, `measure_named`,
     `measure_origin`, `team_named`, `role_purpose_quote`, `framing_quote`, `quote`. Loop v2 S7 outputs are
     mapped to these names before coding.
   - `corpus-b/filings-index.csv` gains `sic` and `software_native`: SIC 3570–3579, 3670–3679 or
     7370–7379 from EDGAR, or a frame employer of type venture-backed software.
   - I4 and I5 use their existing columns.

   The three features without a source are decided as follows.
   - **N03 and N13: a collection step is added (I5c, an extension of I5).** Both are in the scored set,
     and their sources are public.
     - Output: `instruments/I5-community-tooling.csv`, with columns `record_id`, `record_type`
       (community | open_tooling), `name`, `url`, `event_date`, `date_basis`, `owner_type` (independent |
       vendor | foundation | university), `size`, `licence`, `inclusion_note` and `collected_at`. Every
       query goes to `I5-search-log.csv`.
     - Query terms, and no others: the six filing phrases of section 4.2, plus "LLM agents".
     - Communities, from two sources. (a) Meetup.com group search on each term: dated by the group's
       earliest listed past event; included if the group has 3 or more past events and 50 or more
       members. (b) Conference listings in the open `tech-conferences/conference-data` repository
       (confs.tech): events whose name or topic contains a term, dated by their first edition, confirmed
       by the earliest Internet Archive capture of the event page.
     - Open tooling: GitHub search (repository topics and descriptions) on each term, dated by the
       repository's `created_at`. Included if it has an OSI-approved licence, 1,000 or more stars at
       collection, and a README describing a tool to build, run, monitor or govern AI agents.
     - Exclusions, for both: academic multi-agent research groups, game agents, and trading or crypto
       bots.
     - The date of each type is the **third-earliest** record, so that one outlier cannot set the order.
       The vendor certification date is the earliest `launch_date` in `I5-certifications.csv`. The
       regulation date is the earliest `effective_date` of a binding text in `I4-required-functions.csv`
       whose required function is agent work.
     - Collected by Sonnet and checked by a fresh Opus reviewer, under the standing rule of 10 October.
   - **N16a: dropped.** It is graded in only 3 of 7 patterns, so it is outside the common set (point 3).
     Pay extraction would change no score, so none is added. It is removed from the prompt, which now has
     21 coded features.
   - **Truncation rule (N01, N08, N04a, N12, N23).** If the first practice description falls within 12
     months of the corpus start for its source type, coders mark all five "insufficient" ("truncated").
     Corpus starts: postings, the first half-year with 30% or more employer coverage; speech, 1 January
     2024; filings, 1 January 2022; vendor documents, the earliest I5 capture. Reason: the corpus window,
     not history, would otherwise set these answers. (C7)
7. **Coverage (C6).** N06a, N21, and any statement about the order in which kinds of firm took up agent
   work (D6), are coded only from sources that cover big tech: filings, practitioner speech and vendor
   documents. The board crawl (`I1*`) is not used for them, and the prompt says so (its "Coverage rule").
   N21's question now reads "first agent-work roles or teams" rather than "postings", to match. Reason:
   the board crawl misses Amazon, Apple, Alphabet, Microsoft, Meta, Oracle and most utilities. N20, N22
   and N23 keep their wording and definitions. Only their source rows were added, and N23 falls under the
   truncation rule.
8. **Leak check (C7).** `leak_check.py` was rewritten.
   - Labels are matched only in prose. In `.csv` files, every column except those whose header contains
     "title" or "occupation" is checked. In `.md` files, every line is checked, except table cells under
     such headers.
   - `product manag`, `data scientist` and `brand manag` are replaced with the label phrases "product
     management pattern", "data scientist pattern" and "brand management pattern". "Boom then
     specialisation" and "lead industry diffusion" are added. Common occupation names are no longer
     matched.
   - The check scans every file coders receive: all `.md` and `.csv` files of I1–I6 (including all I3, I5
     and I6 files), `clusters/` and `corpus-b/filings-*.csv`. Superseded `-v1` copies are skipped, and
     coders do not receive them.
   - I3's raw period-posting text moves to `history/I3-period-postings.csv`, which coders do not receive.
   - A hit in an agent's prose is rewritten neutrally. A label inside a quoted source passage is replaced
     by "[label removed]".
   - The check was tested on synthetic files. It flags labels in prose and passes titles, occupation
     columns and occupation names. On the current inputs (I4, I5, filings) it reports clean.

**Result (`pattern_power.py`, q = 0.2 and 0.3, 15 features, two coders)**

9. Margins and power:

   | Truth | Supported when true, q = 0.2 | Supported when true, q = 0.3 | Ideal gap | Nearest |
   | --- | --- | --- | --- | --- |
   | DevOps | **0%** | **2%** | 0.05 | Scarcity boom |
   | SRE | 5% | 11% | 0.09 | Scarcity boom |
   | Mandated officer | 29% | 34% | 0.21 | Tool-operator / Lead-industry |
   | Tool-operator fade | 1% | 2% | 0.09 | Scarcity boom |
   | Scarcity boom | 0% | 0% | 0.04 | DevOps |
   | Lead-industry | 12% | 14% | 0.16 | Scarcity boom |
   | Engineering absorption | 24% | 28% | 0.21 | Tool-operator fade |

   - Margins: **0.29** at q = 0.2 and **0.27** at q = 0.3, in percentile points.
   - False support at these margins, worst case per pattern: other truths 0.0%; average blend ≤ 1.3%;
     mixture blend ≤ 5.0%; null ≤ 2.6%. The per-pattern figures are in the two output files.
   - Every pattern comes top in 100% of runs when it is the truth, at both values of q.
   - Every pattern's ideal (noiseless) gap is below the margin, so under A.3(d) every pattern is in a
     family. DevOps and Scarcity boom form one family. Within it, the features that separate them are
     N20, N21 and N22 (yes against no), and N04a, N15 and N23 (half a step).
   - Simulated coder disagreement is 0.33 at q = 0.2 and 0.43 at q = 0.3.

   **Margin selection, restating A.1 point 3.** Let d be the coders' per-feature disagreement on the
   scored features.
   - d ≤ 0.25: margin **0.29**.
   - 0.25 < d ≤ 0.35: margin **0.29**, the larger of the two calibrated margins. The q = 0.3 margin
     (0.27) is not used here. One-coder noise of q = 0.2 already gives a disagreement of about 0.33, which
     falls inside this band, and at q = 0.2 a margin of 0.27 lets false support exceed 5%.
   - d > 0.35: the pattern verdict is reported as unreliable, and only feature-level results are given.
   - If any scored features are "insufficient", both margins are recalculated with `pattern_power.py q
     --drop …` on the remaining features. The same bands apply: m(0.2) for d ≤ 0.25, and the larger of
     m(0.2) and m(0.3) for the middle band.
   - The verdict is unreliable if more than 5 of the 15 scored features are left out. This replaces "8 of
     22", keeping about the same one-third share.
   - Sensitivity, not pre-registered: if the truncation rule removes all five exposed features, 10
     remain. The margins are then 0.30 at q = 0.2 and 0.27 at q = 0.3, and DevOps power is 1% and 3%.

10. **DevOps power is below 60% after the fixes: 0% at q = 0.2 and 2% at q = 0.3.** Nothing was tuned to
    raise it.

    The cause is the percentile step. A present identical to the DevOps profile puts DevOps near the
    100th percentile. It also puts Scarcity boom near the 95th, because the two profiles agree on 9 of
    the 15 features, so the ideal gap is only 0.05. Meanwhile the null and the mixture blends need a gap
    of 0.27–0.29.

    Diagnostic only, not adopted: ranking the same 15-feature, two-coder raw scores without the
    percentile step gives a margin of 0.23 and DevOps power of about 51% at q = 0.2. Any return to raw
    scores would need its own amendment before coding.

    **What the verdict can show.**
    - Which pattern comes top. When a pattern is the truth it comes top in 100% of runs. Under the null,
      DevOps comes top in about 13% of runs.
    - "Supported" for Mandated officer, Engineering absorption and Lead-industry, at a 5% false-support
      bound.
    - Feature by feature, whether the present matches DevOps or Scarcity boom on N20, N21 and N22.

    **What the verdict cannot show.**
    - It cannot declare H-DevOps "supported". A result of "not supported" for H-DevOps is therefore not
      evidence against it.
    - It cannot separate DevOps from Scarcity boom by score.
    - It cannot tell a single pattern from a 50/50 mixture of two.
    - Any claim that the present is DevOps-like must rest on top rank, the family-level verdict and the
      separating features, reported as "not yet distinguishable" under A.3(d), with a date to re-check.

## Addendum A.3 (10 October 2026, still before any present-day coding)

A two-stage test replaces the single seven-way ranking as the primary test of H-DevOps. A.2's fixes all
stay: the common 15 features, missing NF cells, per-pattern null percentiles, the noise fix, NF
randomisation, two coders scored separately, and both blends plus the null. The seven-way ranking and its
margins (A.2 point 9) are reported as a secondary result.

- Code: `python3 loop-tools/pattern_power.py stages`.
- Output: `results/rerun-2026-10-10/pattern-power-v3.md` (q = 0.2 and 0.3, 2,000 runs per condition,
  seed 20261011).

**Stage 1: families**

1. **Family rule.** It was set before the distances were looked at.
   - The ideal distance between two patterns is the mean |difference| over the common features both
     grade.
   - Two patterns are linked when their distance is at most half the median of the 21 pairwise distances.
   - Families are the connected groups of linked patterns.
2. **What the rule gives.** The median distance is 0.429, so the threshold is 0.214. The closest pair is
   DevOps and Scarcity boom, at 0.300. The next are Tool-operator and Scarcity boom, and Tool-operator and
   Engineering absorption, both at 0.333. No pair is linked, so **all seven families are single
   patterns**; the expected DevOps and Scarcity boom family does not form. The rule is not changed to
   produce it.
3. **Scoring and margin.** A family's score is its best member's two-coder percentile. A family is
   supported when it is top by at least the margin. Support counts as false when the truth is outside the
   family, when it is a blend whose two parents are not both in the family, or when it is the null; each
   is bounded at 5%. Because every family is a single pattern, Stage 1 is the A.2 ranking:
   - margins 0.29 at q = 0.2 and 0.27 at q = 0.3;
   - DevOps family supported when DevOps is true: **0% at q = 0.2, 2% at q = 0.3**;
   - DevOps family supported when Scarcity boom is true: 0.0% at both.

**Stage 2: DevOps against Scarcity boom**

4. **Features.** Stage 2 uses the features graded in both patterns whose values differ by 0.5 or more:
   N15, N04a, N20, N21, N22 and N23. With the truncation rule applied, N04a and N23 drop out, leaving N15,
   N20, N21 and N22.
5. **Statistic.** For each feature, +1 if a coder's value is closer to DevOps, −1 if closer to Scarcity
   boom, and 0 if tied. The sum is taken for each coder, and the two sums are averaged.
6. **Decision rule.** "DevOps over Scarcity" if the mean sum is at least k; "Scarcity over DevOps" if it
   is at most −k; otherwise "not distinguishable".
   - k is the smallest value, in steps of 0.5, at which each wrong call has 5% probability or less. The
     conditions tested are DevOps true, Scarcity boom true, and the average and mixture blends of the two.
   - **k = 4** with all six features, and **k = 3** with the truncation rule applied, at both values of q.
     The mixture blend binds.
7. **Power.**

   | Features | q | DevOps over Scarcity, DevOps true | Scarcity over DevOps, Scarcity true |
   | --- | --- | --- | --- |
   | All six | 0.2 | 73% | 82% |
   | All six | 0.3 | **47%** | 60% |
   | Truncated (four) | 0.2 | 75% | 67% |
   | Truncated (four) | 0.3 | **55%** | 44% |

   In every row, the wrong call has 0% probability when the truth is the other pattern.

**Verdicts**

8. **H-DevOps verdicts under A.3.**
   - **supported**: Stage 1 picks the DevOps family and Stage 2 says DevOps over Scarcity;
   - **family only**: Stage 1 picks the family and Stage 2 is not distinguishable;
   - **not supported**: Stage 1 picks another family, or Stage 2 says Scarcity.

   When no family is supported at the Stage 1 margin, the verdict is "not supported" and is reported as
   uninformative.
9. **What this gives, stated plainly.**
   - **Stage 2 power is below 60% at q = 0.3**: 47%, or 55% with truncation. It is 73–75% at q = 0.2.
   - The combined test cannot support H-DevOps. With the family rule as fixed, Stage 1 never picks a
     DevOps family that includes Scarcity boom. When DevOps is the truth, the A.3 verdict "supported" has
     probability **0% at q = 0.2 and 2% at q = 0.3**, and "family only" has 0%.
   - False "supported" stays below 2.4% under every other truth, blend and the null.
   - Stage 2 on its own would separate DevOps from Scarcity boom at q = 0.2. Under this addendum it is
     reached only through Stage 1, so it does not change the verdict.
   - A "not supported" verdict for H-DevOps is not evidence against it.
   - Nothing was tuned. A different family rule would be a new amendment, and must be fixed before
     coding.
