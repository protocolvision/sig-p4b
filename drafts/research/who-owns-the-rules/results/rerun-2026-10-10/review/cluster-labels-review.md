# Cluster label review (leaf clusters, rerun 2026-10-10)

Inputs read: `clusters/leaf/labels.csv`, `clusters/leaf/clusters.csv` (`cluster_id`, `found`, `top20_central_spans`). No other files were consulted.

Checked: 28 of 114 clusters, all 20 central spans each.
- Fixed set (8): 2, 19, 43, 67, 69, 76, 83, 111
- Random spot-check (20; Python `random.seed(5)`, `random.sample` over the remaining 106 ids sorted numerically): 4, 7, 14, 15, 22, 33, 34, 48, 50, 51, 62, 63, 72, 74, 86, 90, 95, 101, 106, 108

## Per-field agreement (existing label vs. reviewer)

| Field | Fixed 8 | Random 20 | All 28 |
|---|---|---|---|
| label (substantive match) | 6/8 | 18/20 | 24/28 (86%) |
| function_family | 7/8 | 20/20 | 27/28 (96%) |
| business_or_technical | 7/8 | 20/20 | 27/28 (96%) |
| all three fields | 6/8 | 18/20 | 24/28 (86%) |

Label disagreements were mostly about scope (too narrow). Only one cluster (19) had a wrong family and wrong business/technical value.

## Changes made to `labels.csv`

| id | field | before | after | why |
|---|---|---|---|---|
| 19 | label | Participate in on-call rotations and 24/7 support | Work on-call rotations, shifts, and off-hours | About 10 of 20 spans are IT on-call; the rest are general shift/weekend/overtime availability (retail, operations leadership) |
| 19 | function_family | it/security | operations | Same: not mainly IT |
| 19 | business_or_technical | technical | mixed | Same |
| 69 | label | Support internal and external audits | Plan, perform, and support internal and external audits | Several spans are about performing audits (audit plans, internal/quality audits, IIA standards), not just supporting them. Family `finance` kept (SOX/statutory spans dominate) |
| 62 | label | Maintain technical documentation and records | Maintain accurate documentation and records | Many spans are general records (DOT logs, audit-ready files, work-performed logs, control/risk docs) |
| 90 | label | Design and support electrical substation engineering | Design, maintain, and troubleshoot electrical power systems | Only about 6 spans are about substations; others cover data-center power, wiring, circuits, and field electrical work |

`notes` was rewritten for the four changed rows (each starts with "Review:"). A `reviewed` column was added (yes for the 28 checked, no for the other 86). The original file is kept at `clusters/leaf/labels-pre-review.csv`.

## Agreed, with minor caveats (no change made)

- 2 SAP: `it/security` is acceptable for enterprise-application work. No better category exists in the list.
- 15 pharma patient/commercial strategy: `marketing` kept. Some spans are medical affairs, so `healthcare/clinical` could also be argued.
- 22 risk: `other` kept. The spans read as enterprise or firm risk management, spread across finance, legal and safety.
- 63 lab testing: `manufacturing/field` fits the pharma QC spans. About 5 spans are clinical specimen handling.
- 83 mentoring: `technical` kept. It is technical leadership, but people development could make it `mixed`.
- 86 forklifts and vehicle moving: `manufacturing/field` kept. Warehouse logistics could also be `operations`.
- 106 cloud/Kubernetes: `it/security` kept. It is close to the border with `software engineering` (DevOps/platform).
