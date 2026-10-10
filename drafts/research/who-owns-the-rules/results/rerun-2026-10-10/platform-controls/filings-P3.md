# P3. Filings: governance-platform and guardrail terms

Descriptive only. Part P3 of `design.md`. Input: the 2,216 consensus filing passages (`corpus/b-raw/extract/passages-consensus.jsonl` holds flags only; the text, form, section and vendor status come from `filings-input-v3.jsonl`, same 2,216 ids). Vendor = SIC 7370-7374 / 3570-3579 (1,428 passages); non-vendor = all other filers (788). Form type was read from each passage header. Search: case-insensitive substring, nine terms ("permission" also matches permissions, permissioned; "approval" also matches approvals). Scripts: scratchpad `p3a.py`, `build.py`.

**206 of 2,216 passages (9.3%) contain at least one term.** The 206 hit passages come from 99 filers.

## Hit counts by term, form and filer group (passages containing the term)

| term | all | 10-K | 10-Q | vendor | non-vendor | 10-K vendor | 10-K non-vendor | 10-Q vendor | 10-Q non-vendor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| guardrail | 41 | 30 | 11 | 39 | 2 | 28 | 2 | 11 | 0 |
| governance platform | 2 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 0 |
| control tower | 3 | 3 | 0 | 3 | 0 | 3 | 0 | 0 | 0 |
| agent registry | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| permission | 48 | 28 | 20 | 40 | 8 | 22 | 6 | 18 | 2 |
| human oversight | 34 | 21 | 13 | 29 | 5 | 17 | 4 | 12 | 1 |
| access control | 49 | 35 | 14 | 40 | 9 | 30 | 5 | 10 | 4 |
| audit trail | 8 | 8 | 0 | 7 | 1 | 7 | 1 | 0 | 0 |
| approval | 58 | 34 | 24 | 23 | 35 | 15 | 19 | 8 | 16 |
| any term (passages) | 206 | 131 | 75 | 151 | 55 | 98 | 33 | 53 | 22 |

A passage with several terms counts once under each term, so term rows sum to more than the 206 passages. Denominators: 10-K 1,313 and 10-Q 903 passages; vendor 1,428 and non-vendor 788. Hit rate: vendor 151/1,428 (10.6%), non-vendor 55/788 (7.0%); 10-K 131/1,313 (10.0%), 10-Q 75/903 (8.3%).

Total keyword occurrences (not passages): guardrail 46, governance platform 2, control tower 4, agent registry 1, permission 52, human oversight 34, access control 56, audit trail 8, approval 65.

## Coding

Each of the 206 hit passages was coded by one coder (Claude Sonnet 5.5, single pass, no second coder, no seeds) from the text around each hit. `agent_ai_control_context` (y/n) is an added flag: n marks hits unrelated to AI or agent control (regulatory approval, product names such as "Access Control" video, stockholder approval, general cybersecurity). Where a passage describes a vendor's own product controls for its customers, `who_manages` follows the text: customer if the text says customers, users, administrators or teams set or manage the control; vendor_or_product if the product itself is said to enforce it; not_stated otherwise. The quote column is one verbatim quote of at most 40 words supporting both codes. All 206 quotes were checked by script (whitespace-normalised, case-insensitive substring of the passage): 206 of 206 pass.

## who_manages by filer group, all 206 hit passages

| who_manages | vendor | non-vendor | total |
| --- | --- | --- | --- |
| it_or_security | 1 | 1 | 2 |
| business_owner | 0 | 1 | 1 |
| committee_or_board | 5 | 1 | 6 |
| vendor_or_product | 52 | 0 | 52 |
| customer | 33 | 2 | 35 |
| not_stated | 60 | 50 | 110 |
| total | 151 | 55 | 206 |

## who_manages by filer group, 127 passages in AI/agent control context

| who_manages | vendor | non-vendor | total |
| --- | --- | --- | --- |
| it_or_security | 1 | 0 | 1 |
| business_owner | 0 | 1 | 1 |
| committee_or_board | 5 | 0 | 5 |
| vendor_or_product | 45 | 0 | 45 |
| customer | 25 | 2 | 27 |
| not_stated | 36 | 12 | 48 |
| total | 112 | 15 | 127 |

## control_kind by filer group, 127 passages in AI/agent control context

| control_kind | vendor | non-vendor | total |
| --- | --- | --- | --- |
| in_product_setting | 47 | 4 | 51 |
| separate_platform | 18 | 0 | 18 |
| policy_or_process | 15 | 6 | 21 |
| not_stated | 32 | 5 | 37 |
| total | 112 | 15 | 127 |

## who_manages by control_kind, 127 passages in AI/agent control context

| who_manages | in_product_setting | separate_platform | policy_or_process | not_stated | total |
| --- | --- | --- | --- | --- | --- |
| it_or_security | 0 | 0 | 1 | 0 | 1 |
| business_owner | 0 | 0 | 1 | 0 | 1 |
| committee_or_board | 0 | 0 | 5 | 0 | 5 |
| vendor_or_product | 27 | 11 | 4 | 3 | 45 |
| customer | 20 | 7 | 0 | 0 | 27 |
| not_stated | 4 | 0 | 10 | 34 | 48 |
| total | 51 | 18 | 21 | 37 | 127 |

## who_manages by form, AI/agent control context

| who_manages | 10-K | 10-Q | total |
| --- | --- | --- | --- |
| it_or_security | 1 | 0 | 1 |
| business_owner | 1 | 0 | 1 |
| committee_or_board | 1 | 4 | 5 |
| vendor_or_product | 27 | 18 | 45 |
| customer | 21 | 6 | 27 |
| not_stated | 31 | 17 | 48 |
| total | 82 | 45 | 127 |

## Distinct filers in AI/agent control context, by who_manages (a filer counts once per code)

| who_manages | filers | vendor filers | non-vendor filers |
| --- | --- | --- | --- |
| it_or_security | 1 | 1 | 0 |
| business_owner | 1 | 0 | 1 |
| committee_or_board | 1 | 1 | 0 |
| vendor_or_product | 18 | 18 | 0 |
| customer | 15 | 14 | 1 |
| not_stated | 33 | 22 | 11 |
| any | 59 | 46 | 13 |

## Five representative quotes

- **Salesforce, Inc.  (CRM)**, 10-K, filed 2025-03-05, vendor (`0001108524-25-000006_1`; who_manages = customer; control_kind = in_product_setting): "Our Trust Layer is built into the Salesforce Platform to help customers safely use their data and set guardrails on what AI agents do with that data."
- **SS&C Technologies Holdings Inc  (SSNC)**, 10-K, filed 2026-02-26, vendor (`0001193125-26-076745_2`; who_manages = vendor_or_product; control_kind = separate_platform): "SS&C has also developed AI Gateway, our enterprise-grade governance platform that accelerates the safe integration of AI into complex business processes."
- **Rubrik, Inc.  (RBRK)**, 10-Q, filed 2025-09-10, vendor (`0001943896-25-000042_3`; who_manages = committee_or_board; control_kind = policy_or_process): "our AI governance committee (including leaders from our Engineering, Product, Legal, and Information Security teams) performs an analysis and review of each AI tool for which pre-approval is required"
- **Datavault AI Inc.  (DVLT)**, 10-K, filed 2026-03-18, non-vendor (`0001104659-26-031280_0`; who_manages = business_owner; control_kind = policy_or_process): "These agents operate subordinate to human oversight and governance at all times, with human executives, compliance teams, and domain experts retaining final authority."
- **Samsara Inc.  (IOT)**, 10-K, filed 2026-03-16, vendor (`0001628280-26-018167_0`; who_manages = not_stated; control_kind = not_stated): "Our AI Agents automate complex, data-heavy operational tasks with minimal human oversight."

## Limits

- Passages were selected earlier by phrase match (agentic and related terms, +/-150 words), so this is a search of text near agent mentions, not of whole filings. Terms outside those windows are not counted.
- Repetition inflates counts. The same text recurs across a firm's 10-K and 10-Qs (Rubrik, Box, C3.ai, Extreme Networks, Innodata, Appian, Kaltura, Microsoft, Blackbaud appear many times). The filer-level table counts each firm once.
- Most vendor hits are marketing or business-section descriptions of what a product does; most non-vendor hits are risk-factor language. These describe what firms say, not what they do. The not_stated code is the largest category in both groups.
- Single coder, no agreement check, no seeded items; the vendor-product codes (customer vs vendor_or_product) involve judgement where the text says only that a product "provides" or "enforces" a control. A fresh review of these codes is advisable before use.
- The 79 hits flagged n (outside AI or agent control context) are kept in the CSV and the all-hits table so the keyword counts reconcile; the context tables drop them.
- Only 2 passages contain "governance platform" as an exact string, 3 "control tower" and 1 "agent registry", so these terms carry no weight on their own. Some governance products appear under other words (for example "command center", "governance tools", "AI Gateway").
- Descriptive only; no verdict on H-local, H-decide or H-none is drawn here.
