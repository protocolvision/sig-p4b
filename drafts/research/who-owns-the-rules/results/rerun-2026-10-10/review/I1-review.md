# I1 review (Opus, 10 October 2026)

Scope: `loop-tools/i1_labour.py`, `instruments/I1.md`, `I1-tables.csv` and `I1-lexical-flags.csv`, checked against deviations 14, 18 and 21. The record-pool key and the coder record files were used only to validate the lexical flag.

Outputs:
- the fixed script, `loop-tools/i1_labour.py` (v2), with the old one kept as `loop-tools/i1_labour-v1.py`;
- regenerated `I1.md`, `I1-tables.csv`, `I1-lexical-flags.csv` and `I1-posting-level.csv.gz`, with the old ones kept as `*-v1.*`;
- a new file of sampling strata, `I1-strata.csv`.

`leak_check.py` finds no hits in the I1 files. Hits remain in I3 and clusters files, which are outside this review.

## Verdict

v1 should not be used. Its main pooled figure, absorption ratio (b), was too small by a factor of about 4.5 because rest20 was not weighted. Its lexical flag was never compared with the coders. When compared, precision is 0.05 against coder A and 0.14 against coder B. The flag counts mentions of the listed terms, not agent or AI duties as the coders code them. v2 fixes the arithmetic and states the flag's precision next to every figure that uses it. The flag's low precision is a property of the pre-registered measure; the term list was not changed.

## 1. Sampling weights (critical; fixed)

**Strata.** Deviation 14 stratifies rest20 by O*NET major group × employer type (seed 20261019). I rebuilt the strata from the mapping used at selection time:
- `selection.csv`'s `onet_code` matches `postings-mapped.csv` (v1 mapping) on 100% of rows, and the v2 mapping on only 45%;
- employer type comes from `boards.csv`;
- the universe is the 110,715 titled postings on non-excluded boards. The rest is 106,510 postings in 39 strata (24 Fortune 500, 15 venture-backed software).

All large strata have a sampling fraction of 0.198 to 0.204. A few tiny venture-backed strata (1 to 3 postings) have fractions of 0.33, 0.5 or 1.0. The overall fraction is 0.2000 and the mean weight is 4.999. The near-constant fractions confirm the reconstruction. Untitled postings (695) were not in the sampling frame: the "none" stratum fraction would otherwise be 0.18, not 0.199.

**Weights.**
- **sampling-weighted:** a rest20 posting has weight N_h / n_h; S1 and new-title postings have weight 1.
- **employer-weighted:** each employer has total weight 1, spread over its postings in proportion to their sampling weights. v1 had spread it equally over the selected postings.

**Corrected figures (unweighted → sampling-weighted / employer-weighted):**

| Figure | v1 | v2 unweighted | v2 sampling-weighted | v2 employer-weighted |
|---|---|---|---|---|
| Absorption ratio (b), all non-new-title | 1.179 (unw.), 1.231 (emp.) | 1.179 | **5.316** | **5.079** |
| Flagged existing postings (b) | 3,288 | 3,288 | 14,833 of 107,341 | — |
| Absorption ratio (a), S1 | 0.143 (unw.), 0.177 (emp.) | 0.143 | 0.143 | 0.192 |
| Share of existing with flag (b) | 0.149 | 0.149 | 0.138 | 0.158 |
| Cross-function secondary, other postings | 0.084 | 0.084 | 0.083 | 0.148 |
| Cross-function primary, other postings | 0.003 | 0.003 | 0.003 | 0.005 |
| New-title share of all postings | 0.109 (not shown in v1) | 0.109 | **0.025** | — |
| US / non-US / unknown postings | 14,974 / 8,281 / 2,257 | 15,080 / 8,215 / 2,217 | 66,581 / 34,262 / 9,872 | — |

By employer type, ratio (b) is 5.35 for Fortune 500 and 5.11 for venture-backed software (sampling-weighted). By location it is 5.06 for US and 5.58 for non-US. All slices are in the CSV.

Not affected: S1-only and new-title-only figures, including counts per employer and the share of employers with at least one new-title posting. Two limits remain:
- Employer counts with a flagged existing posting are lower bounds for (b), because rest20 is a sample.
- The clustering pool's cap of 300 tasks per employer is a second sampling stage, which these weights do not correct. Cross-function shares are therefore pool-conditional.

## 2. Lexical flag validation (critical; measured, list unchanged)

Deviation 21 says "the 300 real records of the coding pool". The key has 300 real records in all: 200 postings, 50 filings and 50 speech. The posting records are the 200 used here. I checked that each record's span equals the Haiku span of the task id given in the key (200 of 200). A coder is positive if code1 or code2 is in {AO, PE, RD}.

| | Flag yes, coder yes | Flag yes, coder no | Flag no, coder yes | Flag no, coder no | Precision | Recall |
|---|---|---|---|---|---|---|
| Coder A (4 positive) | 1 | 20 | 3 | 176 | **0.048** (Wilson 95% CI 0.008–0.227) | 0.25 |
| Coder B (7 positive) | 3 | 18 | 4 | 175 | **0.143** (0.050–0.346) | 0.43 |
| Both coders positive | 1 | 20 | 3 | 176 | 0.048 | 0.25 |
| Either coder positive | 3 | 18 | 4 | 175 | 0.143 | 0.43 |

The coders agree with each other on 197 of 200 records (0.985).

**What drives the false positives.** Of the 18 records flagged that neither coder called an agent or AI duty:
- 13 contain "AI". These are mostly AI as a subject of security or strategy work: "security architecture reviews of new AI services", "evaluate emerging AI technologies", "AI security requirements".
- 5 contain "automation". These are generic: "test coverage and automation maturity", "application development, automation, cloud", "automation scope for capital projects" (plant control systems).
- 1 each contains "Machine Learning" (a team name in "partner with … Machine Learning, and platform teams"), "generative AI" (threat models) and "agentic" (research topics).

**False negatives** (either coder positive, flag off):
- R0178, "agent infrastructure … agent runtime": "agent" is not next to a listed neighbour.
- R0342, "multi-agent systems": same reason.
- R0393, "LLMs": the list has no plural for LLM.
- R0399, a compliance-guidelines task that coder B alone coded.

**Scale in the whole data.** Over all tasks, the flag is carried by "AI" in 11,302 tasks, "automation" in 4,311 and "prompt" in 703; the other terms are far less frequent. Among flagged existing postings (sampling-weighted 14,833):
- 4,231 are flagged only by "automation";
- 1,251 are flagged only by "prompt", often in the sense "prompt and courteous service";
- 4,329 are flagged only by "AI".

In S1, 147 of the 400 flagged postings rest on "automation" and/or "prompt" alone.

**Matching detail.** Case-insensitive whole-word matching of "AI" also catches the Italian preposition "ai" ("dettagli accurati ai clienti"): 30 tasks, which is small. I did not change the matching. The pre-registration does not fix the case, and deviation 14 says case-insensitive for titles.

**Action.** The term list is unchanged. v2 adds a `flag_precision` column to the CSV ("task-level precision 0.05 vs coder A, 0.14 vs coder B"), filled on every row that uses the flag. I1.md states the precision in the flag section, the absorption heading, the major-group note and the limits. `I1-lexical-flags.csv` now carries the matched terms and both coders' codes. Precision is measured per task. A posting is flagged when any one of its tasks is flagged, so posting-level precision is unlikely to be higher.

**Implication for use.** The absorption ratio cannot be read as "existing jobs absorbing agent duties". It measures how often existing postings mention AI or automation terms, relative to the count of new-title postings. With recall also low (0.25 to 0.43, from 4 to 7 positives), the flag is not a usable estimator of coded agent or AI duty prevalence. Its error rates are measured on very few positives, so any correction factor would be unreliable. None is applied.

## 3. US vs non-US rule (checked; fixed)

**Random checks.** I read the location text of two random samples of 50 selected postings (seeds 20261010 and 20261011):

| | Sample 1 | Sample 2 | Total |
|---|---|---|---|
| v1: classified, correct | 47 of 47 | 45 of 46 (1 unverifiable: "Metro North (0233)" called US via "North") | 92 of 93 |
| v1: unknown | 3 (Türkiye, Jordan; "Remote") | 4 | 7 |
| v2: classified, correct | 49 of 49 | 45 of 45 | 94 of 94 (95% CI 0.96–1.00) |
| v2: unknown | 1 ("Remote") | 5 (3 are US places the rule does not list) | 6 |

The two Sample 1 unknowns (Türkiye, Jordan) led to two entries being added to the non-US list. Sample 2 was drawn after the fixes, so it is an untouched check.

**Systematic errors.** The random checks hide systematic errors that a scan of all locations shows. v1 bugs:
1. **State-name list bug.** `US_STATE_NAMES` was split on whitespace, so the "state names" included "New", "York", "North", "South", "West", "Island", "Carolina", "Mexico" and "of". Any location with these words and no non-US keyword became US: "Isle of Man", "North Holland", "West Bengal", "BMW of Towson", store names such as "South Tomball (0552)". "Mexico City" was rescued only because "Mexico" is also in the non-US list. "Albuquerque, New Mexico" became non-US.
2. **US places with non-US namesakes.** These became non-US: "Florence, KY" (80 postings), "USA - Pennsylvania - North Wales" (13; "Wales"), Vancouver WA, Melbourne FL, Dublin OH/CA, Vienna VA, Lima OH, Rome NY, Amsterdam NY, Lake Wales FL.
3. **Site codes read as countries.** Carrier's US site codes ("CAN05: …, Charlotte, NC, 28269 USA") were read as ISO3 Canada.
4. **"U.S." at the end of a string.** `\b` after the final "." never matched, so "Remote - U.S." was unknown.
5. **Unhandled formats.** Country-region prefixes ("DE-BY-NORDLINGEN", "GB-AC-ABERDEEN", "AU-WA-…") and US state-dash prefixes ("TX-GRAND PRAIRIE", "FL-Pensacola") were left unknown.
6. **Canadian province codes** ("Richmond, BC", "Laval, QC") were sometimes US through the city list.

**Effect of the v2 fixes.** v2 changes:
- 175 postings non-US → US;
- 96 unknown → non-US and 39 unknown → US;
- 13 US → non-US;
- 95 US → unknown, the v1 "North/West/of" cases.

I read every distinct location string that moved into a class and found no errors among them. Known residual weaknesses:
- Only the first listed location is used. "Remote-Friendly … | San Francisco, CA" stays unknown.
- Bare US town names not on the city list stay unknown ("Clifton Park", "Tempe", "Lehi").

The effect on I1 figures is small (US new-title postings 1,519 → 1,526; non-US 1,188 → 1,184). The v1 classes are kept in the posting-level file (`us_v1`) and the CSV (`us_class_postings_v1_rule`).

## 4. Other correctness issues

1. **Employer misattribution (fixed).** `boards.csv` lists board `workday/abbott` twice: under Abbott Laboratories (workday probe) and under Ross Stores (careers-page link). `selection.csv` took the Ross Stores row, so all 436 Abbott postings (26 new-title) were attributed to Ross Stores. `review/crawl-identity-check.md` confirms the board is Abbott ("Abbott is a global healthcare leader"). In v2:
   - The script maps the board to Abbott Laboratories.
   - Sector counts change: manufacturing 44 → 45 employers and 696 → 722 new-title postings; retail 33 → 32 employers and 179 → 153.
   - Employer weights change for both firms. Ross Stores now has no postings. Its real board was never crawled; this should be noted in the coverage file.
   - The same duplicate exists for `workday/williams` (Williams and Williams-Sonoma). That board is excluded, so it has no effect.
   - Recommend fixing `selection.csv` or `boards.csv` upstream, for the other instruments that read them.
2. **Duplicate rows in v1 CSV.** `new_title_postings` was written twice per slice, once inside each numerator loop. Fixed.
3. **Primary cluster set was hard-coded.** It is now derived as "found and not artefact" from the labels, with an assertion that it equals {2, 19, 43, 67, 69, 76, 83, 111}. The set is unchanged.
4. **v1 validation identified real records by span text, not by the key.** It gave the right 200 records, confirmed against the key.
5. **No other arithmetic errors found.** The absorption numerators and denominators, the cross-function rule (two or more families, at least one business and one technical cluster; "mixed" counts as a family only), the artefact rule and the spread statistics were re-derived and match.
   - "Other postings" in the cross-function comparison includes the 584 human-agent-title postings. This is consistent with "new-title vs other postings" in deviation 21, but it is worth knowing. S1 and rest20 are also reported separately.
6. **Minor.** pandas `fillna` downcasting warnings removed.

## Corrected headline numbers

- **Absorption ratio (b), all non-new-title:** 1.18 unweighted → **5.32 sampling-weighted** (5.08 employer-weighted). Estimated 14,833 existing postings with a flagged task against 2,790 new-title postings. Flag precision 0.05 (A) / 0.14 (B).
- **Absorption ratio (a), S1:** 0.143 (unweighted = sampling-weighted); employer-weighted 0.192. Flag precision 0.05 / 0.14.
- **Share of existing postings with a flagged task:** S1 0.481; all non-new-title 0.138 sampling-weighted. Flag precision 0.05 / 0.14.
- **New-title share of all postings:** 0.025 sampling-weighted (0.109 unweighted). 161 of 198 employers (0.813) have at least one new-title posting.
- **Cross-function, secondary:** new-title 0.082 vs other postings 0.083 sampling-weighted. Primary: 0.006 vs 0.003, on 1 and 3 postings.
- **US rule:** 94 of 94 classified postings correct in random checks; systematic v1 errors (about 300 postings) fixed.
