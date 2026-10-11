# Decision rights Part 1: sample

Script: results/rerun-2026-10-10/decision-rights/build_sample.py. Statements scanned: 305533; matched but not joinable to selection.csv: 0.

## Matching

A statement matches a domain if it contains one of the domain terms and one rule word (word-boundary, case-insensitive; CAB and AML case-sensitive). Domain assignment: the domain whose term appears earliest in the statement. Plurals allowed.

Rule word regex: `\b(?:rules?|polic(?:y|ies)|limits?|thresholds?|criteria|guidelines?|protocols?|guardrails?|standards?|controls?|approvals?|exceptions?|parameters?|configurations?)\b`

AGT: bare "agent(s)" counts only if the statement also matches `\b(?:AI|LLMs?|models?|co-?pilots?|chat-?bots?|automation|agentic)\b`. The other AGT terms need no context word.

Domain term regexes (each wrapped in `\b(?:...)\b`):

- AGT: `agents?`; `agentic`; `co-?pilots?`; `chat-?bots?`; `virtual assistants?`; `AI assistants?`
- CRD: `credit polic(?:y|ies)`; `underwriting`; `credit risk`; `lending criteria`
- PRC: `pricing`; `discounts?|discounting`; `deal desk`; `price exceptions?`
- FRD: `fraud`; `AML`; `transaction monitoring`; `sanctions? screening`
- CHG: `change advisory boards?`; `CAB`; `change management`; `release approvals?`
- ACC: `access polic(?:y|ies)`; `entitlements?`; `identity governance`; `role-based access`; `privileged access`
- TRD: `trading limits?`; `risk limits?`; `position limits?`; `kill[\s-]?switch(?:es)?`; `pre-?trade`
- CLN: `clinical protocols?`; `formular(?:y|ies)`; `order sets?`; `clinical guidelines?`; `care pathways?`
- PRO: `approval thresholds?`; `delegations? of authority`; `procurement polic(?:y|ies)`; `spend approvals?`

## Counts

Raw = matched statements assigned to domain; weighted = rest20 statements x5. Dedupe = identical normalized text within the same employer removed (first kept by task_id order). Postings are distinct postings in the raw match.

| Domain | Raw | Weighted | Postings | Employers | After dedupe (raw) | After dedupe (weighted) | Postings after dedupe | Sample n | Multi-domain matches in raw |
|---|---|---|---|---|---|---|---|---|---|
| AGT | 430 | 738 | 354 | 89 | 371 | 655 | 304 | 60 | 1 |
| CRD | 160 | 548 | 136 | 28 | 95 | 459 | 71 | 60 | 6 |
| PRC | 225 | 1061 | 193 | 55 | 144 | 664 | 114 | 60 | 9 |
| FRD | 47 | 195 | 36 | 23 | 46 | 190 | 36 | 46 | 0 |
| CHG | 102 | 398 | 99 | 47 | 92 | 364 | 89 | 60 | 0 |
| ACC | 94 | 302 | 90 | 47 | 87 | 291 | 83 | 60 | 0 |
| TRD | 7 | 27 | 6 | 6 | 7 | 27 | 6 | 7 | 1 |
| CLN | 21 | 105 | 21 | 10 | 13 | 65 | 13 | 13 | 0 |
| PRO | 38 | 138 | 35 | 27 | 35 | 127 | 32 | 35 | 0 |

## Multi-domain matches (all statements, by domain set)

- CRD+PRC: 8
- PRC+PRO: 4
- CRD+FRD: 1
- ACC+AGT: 1
- ACC+TRD: 1
- CRD+FRD+PRC: 1
- AGT+PRC: 1

## Sampling notes

- random.Random(20261012); per domain, pool sorted by task_id, then rng.sample of up to 60; domains processed in table order.
- Sample is unweighted within the deduped pool; weight field is carried for later estimates.
- Employer, title, group come from selection.csv (group falls back to postings-input if blank).
- No coding done; no seed items created. Seed statements (30) still to be added separately.
