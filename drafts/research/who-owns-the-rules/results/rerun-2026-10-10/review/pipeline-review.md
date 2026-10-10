# Pipeline review: Corpus B data collection

Reviewer: Opus, fresh agent, 10 October 2026. Read: `triangulation-design.md` (all), `loop-design-v2.md`
§5–6, `corpus/acquisition-plan.md`, `log.md`, `deviations.md`, and the artefacts below. Not opened:
`results/loop-*`, `results/industry-*`, `roles/*.md`, `exploratory/`, `report/`, `README.md`. For the power
check I read only the `pattern`, `feature_id`, `value` and `grade` columns of `signatures.csv`, and only
to count them, which I needed to judge the NF handling. Numbers below come from scripts run on the
committed or `b-raw` data. Live EDGAR queries were used only to check counts.

Scope: errors that would bias or invalidate later analysis. Polish is left out.

---

## CRITICAL fixes (most severe first)

### C1. Filing passages are counted two or three times: overlapping windows, quarterly boilerplate and a few AI vendors

**Where:** `loop-tools/edgar_fetch.py` `passages_for()` (l. 240–255) and `stage_passages()` (l. 258–280);
`corpus/b-raw/extract/filings-input.jsonl`, built by a script that is not in the repo.

**What I found**
- One ±150-word passage is cut for every phrase match, so passages overlap whenever mentions sit within
  300 words of each other. For example, Salesforce's FY25 10-K gives 40 passages, 33 of them in Item 1.
- Of the 41,868 Haiku spans, only 33,442 are unique within their filing, so 8,426 (20%) are repeats from
  overlapping windows. Only 27,012 are unique across the corpus. 13,717 spans are strings that appear
  three or more times, mostly the same risk-factor or product text repeated in each 10-Q and 10-K. The
  top string appears 47 times.
- A few firms supply most of the spans. 532 companies contribute, but the top 5% supply 44% and the top
  10% supply 59%. C3.ai alone supplies 3,768 spans (9%); C3.ai, Salesforce, UiPath, Global AI and Brand
  Engagement Network together supply 20%. These are sellers of agents describing their products (for
  example "a key-value store model can incorporate Cassandra, HBase…"), not firms describing their own
  work.
- 1,083 passages (20%) come from the `other` section. The design (§4.2) keeps only business, risk
  factors, Item 9A and MD&A.
- 13 amendments (10-K/A, 10-Q/A) duplicate their originals.

**Why it matters**
- I2's cluster rule is: at least 30 members, and adjusted Rand index ≥ 0.6 in the holdout half. One
  firm's repeated text meets both conditions by itself, because identical strings land in both halves
  of the random split and cluster together. Clusters will then reflect C3.ai and Salesforce marketing,
  and they will pass the stability test for the wrong reason.
- Feature N02 ("in a stable cluster") and every count of filing tasks are inflated in an unknown
  direction.

**Fix, before embedding or clustering**
1. Merge overlapping windows within each filing. Union the intervals [i−150, j+150] per section and emit
   one passage per merged interval.
2. Deduplicate spans across a company's filings. Key on (CIK, normalised span), keep the earliest
   filing, and store `n_repeats` and `filed_dates` for the time series.
3. Drop amendments when the original is present.
4. Drop `section == other`, or keep it as a separate stratum that is excluded from I2 by default, as
   §4.2 says.
5. In I2, cap each firm's contribution: at most k spans per CIK (suggest 50), or weight each span by
   1/(firm's span count). Report every cluster's firm count, and require a cluster to have ≥ 30 members
   **and ≥ 10 distinct firms**.
6. Tag filers by SIC (7370–7374 and 3570–3579 are AI or software vendors) and report vendors separately
   from adopters. A vendor describing its product is S5-type evidence ("assumed work"), not practice.
7. Commit the script that builds `filings-input.jsonl` and the 10% sample (with its seed). Today, 5,319
   passages become 5,276 inputs by an undocumented step.

### C2. The filing extraction prompt pulls product features and corporate activity, not tasks

**Where:** `loop-tools/extract_tasks.py` l. 35–40 (`PROMPTS["filing"]`); `filings-haiku/report.json`.

**What I found**
- The prompt asks for "every activity the passage says the company, its people **or its systems**
  perform". The result is 8 spans per passage on average (median 8, max 33).
- 17,113 spans (41%) are labelled `software or agent`. Most of these are descriptions of what a product
  does.
- Many other spans are corporate actions, such as "identifying, acquiring, integrating … AI-based
  technology companies" (47 copies).
- Haiku extracts 30% more spans than Sonnet on the same 511 documents (4,217 against 3,255). Even under
  a lenient match (token F1 ≥ 0.5), Haiku's precision against Sonnet is 0.65.

**Why it matters:** I2 is meant to find work activities ("task statements"). Most filing spans describe
software capability or corporate strategy. They will form clusters that look like "agent operations"
(AO) and push rule-work clusters below the 30-member line, or into a residual.

**Fix**
- Rewrite the filing prompt so it keeps only activities performed by the company's **people, teams or
  functions**, including when they direct agents. It should leave out descriptions of what a product or
  system does for customers, M&A, financing and forecasts.
- Keep the `performer` field, but split the current `software or agent` value into "product
  capability" (drop) and "agent acting in the firm's own operations" (keep).
- Re-extract with both models.
- Because the prompt changes after a run, record this as a deviation before any clustering.

### C3. The extraction agreement gate is uninterpretable as written: exact match gives 0.35, a lenient match 0.73

**Where:** `extract_tasks.py` `agree()` l. 151–168; design §5 ("span-level F1 … accepted at 0.7").

**What I found** (511 documents extracted by both models)

| Matching rule | P (Haiku vs Sonnet) | R | F1 |
| --- | --- | --- | --- |
| Exact normalised string | 0.31 | 0.40 | **0.35** |
| Token F1 = 1.0 | 0.35 | 0.45 | 0.39 |
| Token F1 ≥ 0.8 | 0.50 | 0.65 | 0.57 |
| Token F1 ≥ 0.6 | 0.61 | 0.79 | 0.69 |
| Token F1 ≥ 0.5 | 0.65 | 0.84 | **0.73** |

- 85% of Sonnet's spans contain, or are contained in, a Haiku span. Most of the disagreement is about
  where a span starts and stops, not about which task it is.
- `agree()` also ignores documents where either model returned no tasks (12 for Sonnet, 10 for Haiku).
  An empty result against a non-empty one is a disagreement, so leaving these out inflates F1.

**Why it matters**
- Under exact match the extraction fails the pre-registered gate.
- Under the loosest reasonable match it passes. The choice is therefore open to post-hoc selection,
  which is exactly the degree of freedom pre-registration is meant to close.
- Segmentation also matters downstream. If Haiku splits one duty into three spans, that duty counts
  three times in cluster sizes.

**Fix, before computing the gate on the final extraction**
1. Fix the matching rule now and record it in `deviations.md`. Use one-to-one greedy matching on token
   F1 ≥ 0.5 (character-offset overlap ≥ 50% is an equivalent alternative). Count unmatched spans in
   both directions, and count empty-against-non-empty documents as misses.
2. Report exact F1 alongside as a segmentation diagnostic.
3. Add a second gate: the per-document task count ratio between the two models stays within
   [0.8, 1.25] at the median. This catches over-segmentation.
4. Rerun the gate after the C2 prompt fix.

### C4. The scoring rule and power check are tilted between patterns, and the noise model is wrong

**Where:** `loop-tools/pattern_power.py` l. 38–48, 55–61; `pattern-power-q0.2.md`; addendum A.3(b) and
A.1.

1. **Noise bug (l. 48).**
   - The design says "each feature moves one step with probability q". The code picks ±0.5 at random
     and then clips at the ends. A yes or no feature therefore moves only half the time it is chosen, so
     the effective q is about 0.1 for the 116 of 151 graded cells that are yes or no.
   - With the noise fixed (an extreme feature always moves inward), DevOps "supported when true" falls
     from **91% to 74%** at q = 0.2. At q = 0.3 with the NF fix it falls to **48%** (reported: 62%).
   - The margin itself barely moves (0.17 → 0.17 or 0.14–0.16).
2. **NF cells enter the simulated truth as "no" (l. 31).**
   - All 37 NF cells carry `value = no`. When pattern t is the truth, its NF features enter the
     simulated present as 0. That is a fabricated observation, and it is scored against every rival
     that grades the feature.
   - Fix: when a feature is NF in the truth pattern, draw its present value at random from
     {0, 0.5, 1}, or drop it from that run.
3. **The patterns are scored on different feature sets of different sizes, so scores are not
   comparable.**
   - Graded feature counts are: DevOps 20, Tool-operator 18, Scarcity 18, SRE 16, Engineering absorption
     16, Mandated officer 15, Lead-industry 14.
   - Each pattern's score is a mean over its own graded features. NF works as a free pass, and a
     "partial" grade can never be more than 0.5 wrong.
   - So patterns with many partial or NF cells score higher on random or ambiguous evidence. Under the
     uniform null, the expected score is DevOps 0.533 against Mandated officer 0.589. Mandated officer
     comes top in 25% of null runs, DevOps in 9%.
   - A present coded entirely "partial" scores Mandated officer 0.77, Tool-operator 0.69 … DevOps 0.60.
   - Averaging the two coders (feature-coding prompt, scoring rules) pulls every disagreement toward
     0.5, which feeds this tilt directly.
   - The "partly supported" (tie) verdict and every rank statement inherit the tilt. Its direction is
     against DevOps and toward the mandate and tool-fade patterns.
4. **Blend sensitivity.**
   - The blend is a feature-wise average, which creates off-grid presents (0.25, 0.75).
   - A 50/50 *mixture* (each feature taken from one of the two patterns at random) is an equally
     literal reading of "50/50 blend". Under it the q = 0.2 margin rises to **0.24**, and DevOps power
     falls to 31% (or 49% without the noise and NF fixes).
   - The margin depends on which reading is used, and only one was tested.

**Fix, before feature coding (addendum A.2, a new amendment)**
- Correct the noise so an extreme feature always moves inward with probability q.
- Randomise NF cells in the truth presents.
- Score every pattern on a **common** feature set: the features graded (not NF) for both patterns in
  each pairwise comparison, or for all patterns. Alternatively, convert each pattern's raw score to a
  percentile against its own null distribution before ranking.
- Calibrate the margin on both blend definitions and take the larger.
- Rerun `pattern_power.py` at q = 0.2 and q = 0.3 and commit before any coding.
- Keep the two coders' values separate in the score (score each coder, then average the scores) rather
  than averaging values into "partial".

### C5. Occupation mapper: the general path is wrong on about a quarter of common titles, and the overrides catch non-target jobs

**Where:** `loop-tools/map_occupations.py`.

**General path.** I ran 40 made-up titles across functions; at least 10 map wrongly:

| Title | Mapped to | Should be about |
| --- | --- | --- |
| Product Manager, Payments | 27-1021 Commercial and Industrial Designers | 11-2021 / 15-1299 |
| Account Executive, Mid-Market | 11-2011 Advertising and Promotions Managers | 41-4011 / 41-3091 |
| Customer Success Manager | 43-1011 First-Line Supervisors, Office | 11-2022 / 13-1199 |
| Network Engineer | 15-1299.05 Information Security Engineers | 15-1241 / 15-1244 |
| Director, Legal Operations | 11-3071 Transportation, Storage and Distribution Managers | legal ops (study occupation) |
| Data Scientist II | unmatched | 15-2051 |
| Pharmacist | unmatched | 29-1051 |
| AI Governance Lead | unmatched ("lead" is stripped as seniority) | — |
| Solutions Architect, Site Reliability Engineer, DevOps Engineer | all 15-1252 Software Developers | defensible, but this merges distinct roles |
| Field Service Technician | 49-2022 Telecom Equipment Installers | 49-9xxx (sector dependent) |

- The "exact" level almost never fires. O*NET occupation titles are plural ("Pharmacists", "Data
  Scientists") and posting titles are singular.
- Stripping "lead", "head of" and "staff" changes meaning: "staff accountant" and "lead generation" are
  not seniority.

**Overrides**
- `controller` catches Air Traffic Controller, Project Controller, Production Controller and "Firmware
  Engineer, Motor Controller". All of these go to 11-3031.01 *as the study occupation*.
- The overrides require the word "manager". Director, Head or VP of Legal Operations or Revenue
  Operations therefore fall through to the general path, which gets them wrong.
- "Identity and Access Management Engineer" is unmatched.

**Why it matters**
- I1's D7 ratio (existing occupations against new titles) and D2 cross-family co-occurrence depend on
  the code and O*NET family of every crawled title.
- The wrong mappings go both ways: across families (sales to advertising, product to design) and into
  or out of the ten study occupations. That biases cross-family co-occurrence (N02) and the absorption
  ratio (N07) in unknown directions.

**Fix**
1. Singularise both sides before lookup (a plain rule-based singulariser: Pharmacists → pharmacist).
2. Stop stripping `lead`, `staff` and `head of` inside titles. Strip them only as leading tokens
   followed by a function noun.
3. Add exclusions to the `controller` override (air traffic, project, production, motor, firmware,
   PLC, network, domain, cost, credit, quality, inventory). The `sel.py` regex from the S1 walk already
   has this list, so reuse it.
4. Accept director, head, VP and lead as well as manager for support, legal and revenue operations.
5. Make `fallback` matches go to model assignment unless the matched dictionary title covers at least
   60% of the posting's tokens.
6. Run the planned 200-title hand check on a **stratified** random sample: 50 override, 50
   exact/alternate, 50 fallback, 50 model. Report error by method. Do not start I1 until fallback error
   is 10% or less.

### C6. Employer coverage is skewed against big tech and regulated sectors, and the S1 sample is mostly offshore Workday enterprise postings

**Where:** `corpus/staging/s1-employer-frame.csv`, `s1-walk-log.csv`, `planned-4.3.csv`,
`corpus-b/boards.csv`.

**Board coverage by sector** (SIC from EDGAR for the 477 mapped CIKs; "crawlable" = board found in
`boards.csv`):

| Sector | Frame | Crawlable | Share | S1 employers |
| --- | --- | --- | --- | --- |
| Manufacturing | 137 | 50 | 36% | 13 |
| Retail and wholesale | 88 | 37 | 42% | 3 |
| Finance, insurance, real estate | 79 | 32 | 41% | 7 |
| VC software (not SEC filers) | 48 | 35 | **73%** | 2 |
| Tech (SIC 357x, 367x, 737x) | 42 | 22 | 52% | 8 |
| Utilities | 33 | 5 | **15%** | 0 |
| Transport and telecom | 31 | 7 | **23%** | 4 |
| Mutuals and private | 25 | 9 | 36% | 1 |

- Amazon, Apple, Alphabet, Microsoft, Meta, Oracle, JPMorgan and Goldman Sachs are all uncrawlable.
  These are the firms most likely to be the earliest enterprise adopters.
- In S1, 53 of 59 postings come from Workday tenants. Only 3 of 44 sampled employers are VC software
  firms.
- Many S1 postings are for offshore shared-service centres: accounts payable in Malaysia, Philippines,
  Poland and Istanbul; HR operations in Sofia, Budapest, Bucharest and Manama. No location filter was
  applied. `log.md` records this, but `deviations.md` does not.

**Why it matters**
- *Absorption (N07, H-absorb).* Duty-in-existing-occupation rates come mostly from transactional
  offshore roles at Workday enterprises, while new agent-work titles cluster at AI-native firms on
  Greenhouse and Ashby, which are over-represented in the board crawl (73% crawlable). The 3:1 ratio is
  then a comparison between different kinds of firm, not a measure of absorption.
- *DevOps-like features.* N06a (first adopters software-native), N21 (first postings in ops or IT) and
  D6 diffusion all depend on which firms are visible. With big tech missing and regulated utilities and
  transport near-absent, the earliest enterprise adopters and the latest regulated adopters both drop
  out. The diffusion sequence cannot be observed.

**Fix**
- Report every I1 rate by sector and firm type, weighted by employer (each employer weight 1), not by
  posting.
- Publish the coverage table above in `corpus-b/`.
- For N06a, N21 and D6, code only from the sources that cover big tech (filings, which do cover them)
  and say so.
- For S1, either filter to US locations (the plan's "location") and redraw, or stratify US against
  non-US and report both. Add the deviation to `deviations.md`.
- Within an employer, `sel.py` takes `ms[0]`, the first result in the ATS's relevance order. Replace
  this with a seeded random draw among all matching postings, and log the number of candidates.
- Commit the walker (`scratchpad/tools/sel.py` and `walk*.py`) to `loop-tools/`. Today the S1 sample
  cannot be reproduced from the repo.

### C7. Several of the 22 features cannot be answered from the planned instrument outputs, and the leak check will block legitimate evidence

**Where:** `loop-prompts/feature-coding.md`, `loop-tools/leak_check.py`.

**Features with no data source**
- **N03 and N13.** These need dated practitioner communities (meetups, conferences, open groups) and
  open tooling. No instrument I1–I6 collects either. I5 covers vendor certifications and I4 covers
  statutes only.
- **N16a.** This needs posted pay. I1's planned analysis (§3) extracts none, and many Greenhouse and
  Workday postings carry no pay field.

**Left-truncated features: N01, N08, N04a, N12, N23**
- These depend on the "first practice description". The speech frame starts in January 2024 (earlier
  items were dropped in cleaning), S1 postings are 2025–26 only, filings start in 2022 (4 filers that
  year), and the archived crawl is usable only in years with 30% coverage.
- The first practice date is therefore bounded by the corpus window, not by history. This pushes N01
  ("gap ≥ 2 years") toward partial or no, and N08 ("same year") toward yes.

**Consequence**
- Coders will mark three to eight features "insufficient". More than 8 makes the verdict unreliable.
- Alternatively, coders will answer from their own knowledge, which the prompt forbids and cannot
  detect.

**Leak check**
- `TERMS` includes `product manag` and `data scientist`. Both are common occupations and will appear in
  I1 title tables and O*NET mappings. Any hit blocks coding until an agent "rewrites the file
  neutrally", which means editing evidence.
- The check also does not scan `I5*.md`, and it does not scan the `.csv` files that coders are given
  for I1, I3 and I6. The globs `I1*` and `I6*` catch them, but `I3*.md` does not cover I3's `.csv`.

**Fix, before coding**
- For each of the 22 features, name the instrument output (file and column) that answers it.
- For N03, N13 and N16a, either add the collection step now (dated community and tooling events in
  I5; pay extraction in I1) or pre-declare the feature unobservable and drop it from every pattern's
  score. Rerun the power check on the reduced set.
- For truncated features, add a rule: if the first practice description is within 12 months of the
  corpus start for its source type, code "insufficient".
- In `leak_check.py`, match pattern names only as role or pattern labels in prose, never inside title
  columns. Exempt I1 title and occupation columns, and replace `product manag` and `data scientist`
  with checks for the pattern labels ("scarcity boom", "brand management pattern").

### C8. The seeds cannot test what the design uses them for

**Where:** `results/rerun-2026-10-10/seeds/seeds.csv`; loop v2 §6.

1. **Recall only.** All 20 seeds are positives. With no AO or OT near-misses (agent prompt-writing,
   applying an existing approval rule), coder *precision* on PV, RD and PE is never tested.
   Over-coding of rule work is the error that would favour the hypothesis.
2. **The gate is too small to mean anything.** "RD recall < 0.7 ⇒ absence uninterpretable" is applied
   to 5 seeds. 4 of 5 passes, with a 95% interval of 0.28–0.99. The gate cannot fail a coder whose
   true recall is 0.5 with any reliability (P(≥4/5 | 0.5) = 0.19).
3. **Detectable as seeds.**
   - The seeds are written to the codebook's own proxies: "where the written definition differs",
     "decide with product and reliability leads", "trading … for fewer breaches".
   - They come from fields absent from the corpus (hospital CPOE, crew scheduling, pre-trade limits,
     SRE error budgets).
   - They carry none of the fields real records have (source id, employer, date, performer,
     timestamp, `speaker_relation`).
   - There are no filing-type seeds, although filings are now about 5,000 of the inputs.
4. **Location.** The seeds sit in `results/rerun-2026-10-10/seeds/`, next to coder inputs. Nothing
   blocks a coding agent from globbing them.

**Fix**
- Write 20 more seeds as negatives and boundary cases: AO, OT, and "applies an existing rule".
- Raise RD and PE to at least 10 each.
- Write the seeds in the vocabulary of the corpus (agent-era business functions), with full record
  fields matching their source type, including filing passages.
- Report precision and recall per code with Wilson intervals.
- Move the seeds outside `results/` (for example `corpus/b-raw/seeds/`, which git ignores) and pass
  coders a merged pool with neutral ids.

---

## Minor issues

1. **Phrase variants.** EDGAR full-text search does not stem. The design lists "autonomous agents" and
   "digital workers" but not the singulars. In 2026 there are 5 and 3 extra 10-K or 10-Q hits. Record
   this as a known gap; do not change the pre-registered list.
2. **Frame–CIK picks.**
   - Spot-checked 10 of the 20 prefix matches: JPMorgan, Wells Fargo (67 candidates, correct main CIK
     72971), Lowe's, Merck, Deere, KKR, Synchrony, GE HealthCare, Interpublic and Wabtec. All are correct.
     The other 10 also look right.
   - Errors are elsewhere:
     - United Airlines Holdings is matched to 319687 (United Airlines, Inc., the subsidiary) and American
       Airlines Group to 4515 (American Airlines, Inc.). Both file joint 10-Ks, and the hits use
       `ciks[0]`, so frame matches can be missed.
     - QVC Group is matched to QVC Inc (a subsidiary).
     - The J.M. Smucker override ("Smucker J M") still resolves to none.
   - Fix: match on any CIK in the hit's `ciks` list, and correct these four by hand.
3. **Denominator window.** 2026 10-K filers come from form.idx Q1–Q3 (to 30 September), but the
   numerator runs to 10 October. Add 2026-QTR4 from the daily index, or cap the numerator at 30
   September. The effect is tiny.
4. **Denominator population.** `tenk_filers` includes asset-backed trusts and shell companies, which file
   10-Ks but never discuss operations. Report the share with and without them (SIC 6189 and blank SIC),
   because the F1–F3 5% threshold uses this population.
5. **Section parser.** Table-of-contents lines also set section marks. These are harmless because body
   headings override them, but `Item 1A` cross-references at the start of a line can mislabel a
   passage. A spot check is enough.
6. **Verbatim check.** Matching is substring-on-normalised-text and includes the injected header
   ("Company: … Section: …"). 1,536 spans (3.7%) are not verbatim. Exclude them from I2, not just flag
   them.
7. **Board identity.**
   - The S1 walk resolved CMS Energy to the Greenhouse board "Campbell Ewald" and Fox to "Fox Creek
     Veterinary Hospital". `okboard` dropped these in S1, but the whole-board crawl must not ingest them.
   - In `boards.csv`, Flock Safety is mapped to `demo.flocksafety-sandbox.com` (a sandbox).
   - Several SmartRecruiters "found" boards hold a single posting (Uber, Caterpillar, Kimberly-Clark,
     Wayfair, News Corp, Omnicom, UHS, Glean) and are probably stub or wrong-entity pages.
   - Walmart shows 79 postings, which is a fragment of its hiring.
   - Fix: set a minimum posting count per board, check identity on 5 sampled postings, and record
     board completeness, because "every open posting" is false for partial boards.
8. **Asymmetric title rules in `sel.py`.** The controller pattern excludes titles containing "ai " but
   platform engineer does not, so 4 of 8 S1 platform-engineer postings carry AI or agent in the title.
   Platform engineer excludes manager, director and head, while controller accepts "Director,
   Controller". Use the same seniority and topic rules across occupations.
9. **Power-check margin search.** It stops at 0.40 and uses 500 runs per blend. After fixing C4, raise
   blend runs to 2,000 so the 5% boundary is not set by Monte Carlo noise (standard error about 1% at
   500 runs).
10. **Feature thresholds.** N01 "titles common" (≥ 1% of agent-duty postings or ≥ 10 employers), N16a
    (15% premium) and N02 (10% of postings) have no stated source. None clearly favours one pattern on
    its own. But N07's 3:1 is copied from H-DevOps's own I1 prediction, and N02's "stable cluster" route
    is vulnerable to C1. Pre-register the threshold sources.

---

## Checked and sound

- **EDGAR search coverage.**
  - All six phrases × five windows were run and fully paged: hits stored equal EFTS totals for all 30
    cells.
  - A live re-query matches: "agentic" 2025 is 191 and "digital workers" 2025 is 2.
  - Known filers are present (Salesforce, Microsoft, Workday).
  - Exhibits are correctly dropped. The 10,000-hit split logic is never triggered.
- **Denominator logic.** Distinct CIKs filing 10-K or 10-KT by filing year from form.idx; the numerator
  is distinct CIKs with a matched 10-K; amendments are excluded on both sides. This is consistent. The
  shares (0.05% in 2022 to 6.75% in 2026) follow from the counts.
- **Prefix CIK matches.** 10 of 10 spot-checked are correct (minor 2 covers the errors found elsewhere).
- **Phrase regex.** "AI agent" does not double-match inside "AI agents" (lookahead), and both are
  searched, so the union is right.
- **S1 walk order.** It reproduces exactly from `random.Random(20261010).shuffle(frame)`.
  It covers all 550 employers and logs failures, as §4.1 asks.
- **Extraction mechanics.** Batch submission, schema-constrained output, no failed requests, and a
  verbatim rate of 96.3% (Haiku) and 99.8% (Sonnet). The posting prompt is well scoped. Neither prompt
  names codes or hypothesis terms. The 10% Sonnet sample is a random (unordered) subset, though its seed
  is not recorded.
- **Media frame cleaning.** 10 changes spot-checked: M005, M010, M012, M022, M027, M028, M035, M053,
  M055 and M080.
  - All fit README rules 1–4.
  - Episode URLs resolved to the episode named in the original row. Each new page contains the
    expected guest, confirmed by fetch for M010, M012, M027, M041, M053 and M055.
  - Function and organisation changes (M035, M080) are corrections under rule 3, and the vendor flags
    follow from them.
  - Pre-2024 drops (M008, M009, M049) apply rule 2.
  - No row was changed for topic.
- **Power check overall.** Seeding, the scoring formula (it matches A.3(b)), the late-feature exclusion
  and the per-truth false-positive rule are implemented as written. The reported 0.17 and 91%
  reproduce exactly. The problems are the ones in C4.
- **Feature-coding prompt.**
  - "No needs positive evidence of absence" and "insufficient drops the feature for all patterns" are
    the right symmetric rules.
  - The N20, N22 and N23 definitions are concrete enough to apply.
