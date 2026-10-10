# Verification of the random 150 first-round claims

Phase 2 of RERUN.md, random slice. Claims: `results/rerun-2026-10-10/sealed/phase2/slice-random150.csv` (150 claims). Evidence: `corpus/text/<id>.txt` plus the round-one data files. Full record: `verification-random150.csv`. No round-one file was edited.

## Counts by verdict

| Verdict | Claims |
|---|---|
| confirmed | 76 |
| corrected | 4 |
| not found | 15 |
| unverifiable | 55 |
| total | 150 |

## Error rate

Error rate = (corrected + not found) / (confirmed + corrected + not found), excluding unverifiable claims.

- Verifiable claims: 95
- Errors: 19 (4 corrected, 15 not found)
- **Error rate 20.0%, Wilson 95% interval 13.2% to 29.1%**
- 55 of 150 claims (37%) could not be checked, so the rate applies to the checkable part of the sample only.

## Error rate by claim type

| Claim type | Sampled | Confirmed | Corrected | Not found | Unverifiable | Verifiable | Error rate | Wilson 95% |
|---|---|---|---|---|---|---|---|---|
| number | 41 | 18 | 1 | 3 | 19 | 22 | 18.2% | 7.3% to 38.5% |
| date | 53 | 33 | 0 | 10 | 10 | 43 | 23.3% | 13.2% to 37.7% |
| quote | 42 | 23 | 3 | 2 | 14 | 28 | 17.9% | 7.9% to 35.6% |
| characterisation | 14 | 2 | 0 | 0 | 12 | 2 | 0.0% | 0.0% to 65.8% |

## Reading the result

- Of the 150 sampled claims, many were fragments of activity-library tables, bare list numbers, headings or reference-list entries produced by the extraction (for example `7.`, `Main structure today:`, `Accessed October 2026`). Where the surrounding line carried a checkable assertion it was checked; otherwise the verdict is unverifiable.
- Unverifiable claims fall into three groups: own recommendations and syntheses with no source (for example the business-protocol-lead critique, the predicting-roles literature review); negative search results ("not found" statements); and sources that were not acquired (failed, HTTP 404 or needs-browser).
- Two recurring causes of `not found`: (1) the acquirer stored a generic landing page instead of the cited posting (Jointaro, Scale AI careers; see index.csv `final_url`), and (2) Nomura posting pages were stored as 1 kB stubs with no body text. These are acquisition defects as much as round-one errors; the claim may be true but cannot be shown from the corpus.
- Corrections were mainly wording: a paraphrase presented in quotation marks (OpenAI field feedback line), an incomplete title (Art of Service course, USF Health page), and a list of teams that adds three that the posting does not name (OpenAI FDE).
- Dates and figures the corpus could check mostly held (FinCEN SAR counts, Florida blackout loads, Part 504, ESMA dates, Knight penalty, Visa transactions per second). Failures cluster in dates and secondary details not stated in the cited page: the 13 March 2019 grounding date, the 13 October 2026 Nessie trial date, the 2016 Series 57 format, the late 2022 Goodside hire, the 1983 Progressive start.
- Small subsamples by type: the intervals are wide, so differences between types should not be over-read.

## Method notes

- Search: per-claim text lookup in the cited ids first, then a corpus-wide search of all 1,266 texts for names, figures and phrases.
- Rule for `confirmed`: the figure, date or wording appears in an acquired text; trivial title punctuation differences were accepted. Where only part of a compound claim was checkable and the checked part held, the verdict is confirmed and the note says which part was not rechecked.
- Rule for `unverifiable`: no id or URL, the cited ids have no text file, or the claim is a negative or interpretive statement.
