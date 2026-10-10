# Verification of the random 150 first-round claims (v2)

Phase 2 of RERUN.md, random slice. Claims: `results/rerun-2026-10-10/sealed/phase2/slice-random150.csv` (150 claims). Full record: `verification-random150.csv`. The first-pass file is kept as `verification-random150-v1.csv`; the old verdict is in the column `verdict_v1`. No round-one file was edited.

## What changed from v1

The v1 verifier searched the cited source ids only, although its method note said it searched the whole corpus (see `review/verification-review.md`). In v2, every row that v1 marked "not found" or "unverifiable" (70 rows) was searched across `corpus/text/` and the text folders of `corpus/b-raw/` (signatures, vendor, history, filings, postings; the derived `extract`, `review`, `calibration` and `coding` folders were excluded). Each search used 2 to 4 distinctive terms from the claim (names, figures, dates, unusual words), and the hits were read. The search terms for every "not found" are in the `note` column. Rows that are list markers, headings, forecasts, opinions, own recommendations, or statements about the author's own search are `not checkable`. Every v1 "confirmed" list marker was also relabelled `not checkable`.

Verdict meanings:
- confirmed: a passage was found anywhere in the corpus (file and passage are in `evidence_source` and `passage`). Where only the main assertion was found and a secondary detail was not, the verdict is confirmed and the note says "Partial" and names the missing detail (CL0530, CL0815, CL0903, CL1817).
- corrected: the corpus gives a different value (4 rows, unchanged from v1).
- not found: searched everywhere, no passage.
- not checkable: not a factual claim a source could settle.

## Counts by verdict

| Verdict | v2 | v1 |
|---|---|---|
| confirmed | 87 | 76 |
| corrected | 4 | 4 |
| not found | 39 | 15 |
| not checkable | 20 | 0 |
| unverifiable | 0 | 55 |
| total | 150 | 150 |

Movements from v1: 55 unverifiable became 30 not found, 17 not checkable and 8 confirmed; 15 not found became 4 confirmed, 2 not checkable and 9 stayed not found; 1 confirmed list marker (CL1159) became not checkable.
- Not found, now confirmed (4): CL2502 (Goodside hired by Scale AI, Cb88035da), CL0530 (Drive Pilot 2022, Waymo rides), CL0815 (Nasdaq kill switch 2014, Ceb639178; partial), CL1161 (AWS AIP-C01, C39df85f9).
- Unverifiable, now confirmed (8): CL0967 (FIX algorithm certificates, Cbf0d4d5c), CL2504 (M-24-10 Chief AI Officers, C3ea5c448), CL0903 (FPL $25m, C811f2a93; partial), CL2151, CL1966, CL1971, CL1645, CL1817.

## Error rate

Error rate = (corrected + not found) / (confirmed + corrected + not found); not checkable rows are excluded.

- Verifiable claims: 130
- Errors: 43 (4 corrected, 39 not found)
- **Error rate 33.1%, Wilson 95% interval 25.6% to 41.5%** (v1: 20.0%, 13.2% to 29.1%, on 95 claims)
- 20 of 150 claims (13%) are not checkable.

Read this number with care: it is not a rate of false statements. Of the 39 not-found rows, 16 cite a page that was never acquired (HTTP failure, needs-browser, 404) and 10 carry no URL or id, mostly posting details (titles, dates, salaries, requirements) that the corpus cannot show. These are gaps in the corpus as much as errors in the drafts. Excluding the 16 not-acquired rows gives 27/114 = 23.7% (Wilson 16.8% to 32.3%). The v1 rate (20.0%) was lower because v1 put such rows under "unverifiable", not "not found".

## Error rate by claim type

| Claim type | Sampled | Confirmed | Corrected | Not found | Not checkable | Verifiable | Error rate | Wilson 95% |
|---|---|---|---|---|---|---|---|---|
| number | 41 | 22 | 1 | 14 | 4 | 37 | 40.5% | 26.3% to 56.5% |
| date | 53 | 40 | 0 | 9 | 4 | 49 | 18.4% | 10.0% to 31.4% |
| quote | 42 | 23 | 3 | 15 | 1 | 41 | 43.9% | 29.9% to 59.0% |
| characterisation | 14 | 2 | 0 | 1 | 11 | 3 | 33.3% | 6.1% to 79.2% |

Small subsamples (3 verifiable characterisations): the intervals are wide, so differences between types should not be over-read. Numbers and quotes show higher rates than dates mainly because of unacquired posting details (salary bands, requirement clauses).

## Reading the result

- Dates held best (about 82% of verifiable dates confirmed). Failures include the 13 March 2019 grounding day, the 13 October 2026 Nessie trial date, the 6 February 2014 PER-005-2 adoption date, 11 May 2026 for the Talkdesk ad, and the 2011 end date of the El Camino system.
- The earlier finding stands that the previous "not found" and "unverifiable" verdicts were unreliable: 12 of 70 flipped to confirmed, and 19 more were headings, markers or interpretive text.
- Citation-only rows (reference-list entries and posting titles) are `not found` when the exact page is absent even if a similar page exists (for example CL1578, where the corpus has a New York Citi ad with a similar title).
- Activity-library table rows were checked against the named employer postings where the corpus has them; paraphrase was accepted when the posting passage said the same thing.

## Method notes

- Tools: ripgrep (fixed-string, case-insensitive) over `corpus/text` and `corpus/b-raw/{signatures,vendor,history,filings,postings,audio,onet}`; hits were opened and read.
- Rule for `confirmed`: the figure, date or wording appears in an acquired text; trivial punctuation differences were accepted.
- Rule for `not checkable`: list ordinals, headings, forecasts and opinions, the authors' own recommendations or syntheses, and negative statements about the authors' own searches.
