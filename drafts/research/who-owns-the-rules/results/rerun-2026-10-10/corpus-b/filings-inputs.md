# Filing inputs v3: counts per step

Built by `loop-tools/build_filing_inputs.py` (design 4.2; review item C1). Windows are +/-150 words around each phrase match.

| Step | Filings | Passages |
|---|---|---|
| Old `filings-input.jsonl` (undocumented step, from 5,319 windows) | | 5276 |
| 1. Windows re-cut from fetched filings | 1167 | 5319 |
| 2. Drop amendments with original present (11 of 13 amendments) | 1156 | 5286 |
| 3. Merge overlapping windows within section | 1144 | 2808 |
| 4a. Keep business, risk_factors, mdna, controls (extraction input) | 968 | 2216 |
| 4b. `other` (stored separately, not extracted) | | 592 |
| 6. 10% sample, seed 20261014 | | 222 |

## Passages by section

| Section | Windows (step 1) | Merged (step 3) |
|---|---|---|
| business | 1612 | 695 |
| mdna | 1122 | 623 |
| other | 1092 | 592 |
| risk_factors | 1493 | 898 |

## Vendor / adopter split (SIC 7370-7374 and 3570-3579 = vendor)

| Set | Vendor | Adopter | Vendor share |
|---|---|---|---|
| Passages in v3 input | 1428 | 788 | 64.4% |
| Filers (CIKs) | 177 | 288 | 38.1% |
| 10% sample passages | 142 | 80 | 64.0% |

Filers with no SIC in EDGAR (counted as adopter): 11 of 517.
