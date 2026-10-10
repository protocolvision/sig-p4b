# Mapper test, 10 October 2026 (pipeline-review C5)

Mapper: `loop-tools/map_occupations.py` after the six C5 fixes. Old mapper = the version before the fixes.

## Scope note on the 40 problem titles
The review (C5) says it ran 40 made-up titles but lists only the problem ones. The 40-title list is not in the repo. This test therefore uses the 23 titles that can be recovered from the review text: the 14 in its table (the three architect/SRE/DevOps titles counted separately), the four `controller` over-match titles, Staff Accountant, Lead Generation, Identity and Access Management Engineer, and four head-level operations variants I added (Head of Revenue Operations, VP Support Operations, Lead Legal Operations, Staff Software Engineer). A mapping counts as correct if its code starts with one of the 'acceptable' prefixes (taken from the review's 'should be about' column), or, where marked, if it is routed to `model`. Where the review gave no target code (Project/Production Controller), correct means only 'not forced into the study occupation controller'.

## Result

- Old mapper: **16 of 23 wrong** (70%).
- New mapper: **6 of 23 wrong** (26%).

| Title | Acceptable | Old (code, method) | Old ok | New (code, method) | New ok |
|---|---|---|---|---|---|
| Product Manager, Payments | 11-2021, 15-1299 | 27-1021.00 fallback | **NO** | 27-1021.00 fallback | **NO** |
| Account Executive, Mid-Market | 41-4011, 41-3091 | 11-2011.00 fallback | **NO** | - model | **NO** |
| Customer Success Manager | 11-2022, 13-1199 | 43-1011.00 alternate | **NO** | 43-1011.00 alternate | **NO** |
| Network Engineer | 15-1241, 15-1244 | 15-1299.05 alternate | **NO** | 15-1299.05 alternate | **NO** |
| Director, Legal Operations | 11-1021 | 11-3071.00 fallback | **NO** | 11-1021.00 override (legal operations manager) | yes |
| Data Scientist II | 15-2051 | - unmatched | **NO** | 15-2051.00 exact | yes |
| Pharmacist | 29-1051 | - unmatched | **NO** | 29-1051.00 exact | yes |
| AI Governance Lead | model / none | - unmatched | yes | - model | yes |
| Solutions Architect | 15-12 | 15-1252.00 alternate | yes | 15-1252.00 alternate | yes |
| Site Reliability Engineer | 15-12 | 15-1252.00 alternate | yes | 15-1252.00 alternate | yes |
| DevOps Engineer | 15-12 | 15-1252.00 alternate | yes | 15-1252.00 alternate | yes |
| Field Service Technician | 49-9 | 49-2022.00 alternate | **NO** | 49-2022.00 alternate | **NO** |
| Air Traffic Controller | 53-2021 | 11-3031.01 override | **NO** | 53-2021.00 exact | yes |
| Project Controller | model / none | 11-3031.01 override | **NO** | 11-3031.01 alternate | yes |
| Production Controller | model / none | 11-3031.01 override | **NO** | 43-5061.00 alternate | yes |
| Firmware Engineer, Motor Controller | 15-12, 17-2 | 11-3031.01 override | **NO** | - model | yes |
| Staff Accountant | 13-2011 | 13-2011.00 alternate | yes | 13-2011.00 alternate | yes |
| Lead Generation Manager | 11-2021, 13-1161, 41- | 11-3051.06 alternate | **NO** | 11-3051.06 fallback | **NO** |
| Identity and Access Management Engineer | 15-1244, 15-1212, 15-1299 | - unmatched | yes | - model | yes |
| Head of Revenue Operations | 11-2022 | - unmatched | **NO** | 11-2022.00 override (revenue operations manager) | yes |
| VP, Support Operations | 11-1021 | - unmatched | **NO** | 11-1021.00 override (support operations manager) | yes |
| Lead, Legal Operations | 11-1021 | - unmatched | **NO** | 11-1021.00 override (legal operations manager) | yes |
| Staff Software Engineer | 15-1252 | 15-1252.00 alternate | yes | 15-1252.00 alternate | yes |

Notes
- Fixed: unmatched singulars (Pharmacist, Data Scientist II), the three controller false positives (Air Traffic, Firmware/Motor routed to model/O*NET, Project/Production no longer study-occupation controller; Project Controller still lands on 11-3031.01 only because O*NET itself lists it as an alternate title), director/head/VP/lead variants of the three operations roles, Legal Operations, Account Executive (now routed to `model`).
- Still wrong (6): Product Manager Payments and Lead Generation Manager (fallback hits that cover 2 of 3 tokens, 67%, so they pass the 60% rule); Customer Success Manager, Network Engineer and Field Service Technician (these are exact hits on O*NET *alternate* titles that point to the wrong code, which none of the six fixes touches). Lowering the error further needs either a threshold above 67% for 3-token titles or demoting `alternate` matches for ambiguous titles to `model`; I did not change that, as it is outside C5's six fixes.
- The 'Project Controller' pass is a judgement: it is correct as an O*NET alternate, but is not a study occupation (study_occupation is empty).
- Unmatched titles now get method `model` (was `unmatched`); `unmatched` is kept only for empty titles. A new column `candidate_code` keeps the rejected fallback guess.

## The 59 S1 titles (planned-4.3.csv rows starting `S1 `)

| Old method | New method | n |
|---|---|---|
| override | override | 59 |

- Study occupation assigned equals the occupation the walk searched for: old 59/59, new 59/59. No disagreements, no title newly routed to `model`.
- All 59 are caught by the override table (the walk searched by those ten titles), so this check confirms the fixes did not break the target roles; it says nothing about the general path. The override change only widens the matches for support, legal and revenue operations.
- The S1 walk's `sel.py` regex was not found in the repo (`corpus/staging` holds only logs), so the controller exclusion list is the reviewer's.
- Not done: the 200-title stratified hand check (C5 fix 6); it needs the crawled titles and a human labeller.
