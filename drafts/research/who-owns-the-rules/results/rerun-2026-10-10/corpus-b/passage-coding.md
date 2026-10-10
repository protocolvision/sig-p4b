# Passage coding: agreement and counts (deviation 10)

Codebook `loop-prompts/filing-codes.md` (fixed). Haiku 5.5 on all 2216 passages; Sonnet 5.5 on the 222-passage 10% file. Gate: kappa 0.6 or more per code.

## Agreement (Haiku vs Sonnet, 222 shared passages)

| Code | Kappa | Haiku yes | Sonnet yes | Both yes | Prevalence Haiku (shared) | Prevalence Sonnet | Prevalence Haiku (all) | Gate 0.6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| own_use | 0.765 | 36 | 41 | 31 | 0.162 | 0.185 | 0.196 | pass |
| product | 0.786 | 140 | 142 | 130 | 0.631 | 0.640 | 0.642 | pass |
| reorg | 0.000 | 0 | 2 | 0 | 0.000 | 0.009 | 0.009 | FAIL |
| body | 0.000 | 1 | 0 | 0 | 0.005 | 0.000 | 0.006 | FAIL |
| metric | 0.497 | 3 | 1 | 1 | 0.014 | 0.005 | 0.015 | FAIL |
| controls | 0.674 | 16 | 10 | 9 | 0.072 | 0.045 | 0.093 | pass |
| workforce | 0.396 | 4 | 1 | 1 | 0.018 | 0.005 | 0.017 | FAIL |
| rule_cited | 0.453 | 12 | 5 | 4 | 0.054 | 0.023 | 0.037 | FAIL |

## Verbatim-quote rate (yes-quotes found in the passage, whitespace-normalised, case-insensitive)

| Run | Yes codes | Verbatim | Rate |
| --- | --- | --- | --- |
| Haiku | 2249 | 2135 | 0.9493 |
| Sonnet | 202 | 196 | 0.9703 |

Per code (Haiku): own_use 412/435, product 1354/1423, reorg 17/19, body 13/14, metric 31/33, controls 199/206, workforce 36/38, rule_cited 73/81

## Companies with yes, by year of filing (`filed`)

Distinct companies (cik) with at least one Haiku-yes passage; last row is distinct companies with any passage.

| Code | 2022 | 2023 | 2024 | 2025 | 2026 |
| --- | --- | --- | --- | --- | --- |
| own_use | 1 | 2 | 4 | 41 | 199 |
| product | 2 | 3 | 9 | 90 | 227 |
| reorg | 0 | 1 | 0 | 3 | 9 |
| body | 0 | 0 | 0 | 2 | 9 |
| metric | 0 | 1 | 0 | 2 | 21 |
| controls | 0 | 0 | 4 | 20 | 95 |
| workforce | 0 | 1 | 1 | 4 | 24 |
| rule_cited | 0 | 0 | 0 | 13 | 40 |
| (all passages) | 5 | 5 | 14 | 135 | 439 |

## Companies with yes, by filer type

Distinct companies (cik) with at least one Haiku-yes passage; last row is distinct companies with any passage.

| Code | vendor | adopter |
| --- | --- | --- |
| own_use | 85 | 126 |
| product | 150 | 93 |
| reorg | 6 | 6 |
| body | 4 | 6 |
| metric | 11 | 11 |
| controls | 61 | 39 |
| workforce | 9 | 16 |
| rule_cited | 26 | 20 |
| (all passages) | 177 | 288 |

A company appears in each year or type column where it has a yes; year columns therefore do not sum to the company total.
