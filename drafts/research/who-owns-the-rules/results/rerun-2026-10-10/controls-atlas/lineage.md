# Lineage of control regimes in five domains (Phase 4c)

Collected 2026-10-11. Source: `lineage.csv` (46 milestones, every quote verified verbatim against the stored page, 40 words or fewer). Searches and fetches: `lineage-searchlog.csv`. Pages: `corpus/b-raw/controls-atlas/lineage/`.

## Years from the first sourced stage-1 control to the first control at each stage

Years are measured from the earliest milestone coded stage 1 in the collected set. "First at stage k or above" treats the scale as ordinal; "exactly" requires the stage to match. Dates mark first availability or publication, not adoption. Negative values mean the later stage appears earlier in the sourced record than the stage-1 baseline, which shows the baseline is censored. Year given in brackets.

| Domain | Milestones | First stage 1 | First at stage 3 or above | First at stage 4 or above | First at stage 5 | First legal requirement |
|---|---|---|---|---|---|---|
| apis | 14 | 1999-06 | +3.7 (2003) | +3.7 (2003) | +3.7 (2003) | +16.4 (2015) |
| cloud | 7 | 2010-07-06 | +0.2 (2010) | +0.2 (2010) | +6.6 (2017) | +12.4 (2022) |
| network | 10 | 1989-03 | +13.9 (2003) | +13.9 (2003) | +31.4 (2020) | +13.9 (2003) |
| industrial | 7 | 1989-06-14 | +2.7 (1992) | n/a | n/a | +0.0 (1989) |
| water | 8 | 1974 | +24.6 (1999) | +24.6 (1999) | n/a | +0.0 (1974) |

## Same table, stage must match exactly

| Domain | Exactly stage 3 | Exactly stage 4 | Exactly stage 5 |
|---|---|---|---|
| apis | +13.3 (2012) | +10.8 (2010) | +3.7 (2003) |
| cloud | +12.4 (2022) | +0.2 (2010) | +6.6 (2017) |
| network | +18.3 (2007) | +13.9 (2003) | +31.4 (2020) |
| industrial | +2.7 (1992) | n/a | n/a |
| water | +27.9 (2002) | +24.6 (1999) | n/a |

## First legal requirement, by domain

- apis: 2015-11-25, EU PSD2 Article 97: strong customer authentication required for payment account access (binding on payment providers) (stage 4)
- cloud: 2022-12-14, EU DORA: binding ICT risk-management framework for financial entities (applies from 2025-01-17) (stage 3)
- network: 2003-02-20, HIPAA Security Rule published (effective 2003-04-21): access control and person authentication for health data systems (stage 4)
- industrial: 1989-06-14, EU Machinery Directive 89/392/EEC: essential requirements incl. emergency stop devices (stage 1)
- water: 1974, US Safe Drinking Water Act: national health-based drinking water standards (stage 1)

## Reading the numbers

- Stage 2 (classifier) is thin outside network security. Only IPS guidance and web application firewalls were coded stage 2; the stage-2 column is therefore left out of the timing table.
- Stage assignments are single-coder judgements by this collector. The design calls for two coders and Opus adjudication; that has not been done. Each non-obvious call is flagged in the `notes` column.
- Baselines are censored in cloud, industrial and water. The earliest controls (AWS account keys 2006, IEC 60204-1 1981, EN 418 1992, water SCADA telemetry) had no dated primary page that could be fetched, so the first sourced stage-1 row is later than the true first control.
- Legal rows are not all comparable. Some are sector-specific (HIPAA, PSD2, DORA) or bind only federal agencies (EO 14028, M-22-09). The EPA memo reversal is kept in the CSV and excluded from timing.
- API stage 5 (XACML 2003) appears before the stage-4 and stage-3 rows for OAuth because standards for policy engines were written long before API products adopted them. Product availability for stage 5 is 2018 (OPA) and 2023 (Cedar, Verified Permissions).

## Gaps

- API keys era: no dated primary source found (RFC 2617 Basic authentication stands in at stage 1).
- Apigee launch and AWS Config Rules: pages not retrievable or dated.
- Azure Policy: Microsoft GA post not found; documentation page has no date, so it is not in the CSV.
- Check Point stateful inspection (1994) and Snort (1998): primary vendor pages blocked or undated; stateful inspection is dated by NIST codification (2009) and the application-firewall/IPS rows by NIST 2007 and PCI 2008.
- ISO 13850 (first edition 1996), IEC 60204-1, IEC 62443 IEC publication dates: standards-body pages blocked (403) or showing only current editions.
- Water SCADA adoption: only an undated trade history was found; EPA cybersecurity pages for the 2023 memo were found only through the withdrawal memo.
- FedRAMP (2011) and other cloud legal requirements beyond DORA: FedRAMP pages returned 404.
- Wayback Machine: not used (0 requests).
