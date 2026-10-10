# Coding check on 40 real records (rerun 2026-10-10)

Sources read: `loop-design-v2.md` §6 only; `corpus/b-raw/review/coding-real-sample.jsonl` (40 records).
I coded all 40 records, applying §6 strictly, before I opened `coderA-records.csv` and `coderB-records.csv`
(only the 40 sample ids). No key files were opened.

## 1. My codes (written before seeing the coders)

Rule work (PV, PE, RD) appears in only **3 of 40** real records.

| id | my codes | note |
| --- | --- | --- |
| R0054 | PE, PV | "Assess AI-related controls … find gaps, and drive root-cause remediation": names a gap in controls (PV) and changes them (PE) |
| R0342 | PE, AO | "human-in-the-loop escalation": sets an agent's escalation conditions (PE under the boundary rule); building the multi-agent system is AO |
| R0397 | PE, AO | "turn goals into … rules, constraints … that AI systems can execute": a policy an agent reads (PE); specification work on the agent (AO) |
| R0088 | AO | IDP + orchestration with human exception handling; no hand-off condition or rule is stated, so this is building an agent pipeline, not PE |
| R0135 | AO | "implementing bots into … finance" |
| all other 35 | OT | hours, recruiting, sales, testing, audits executed, revenue statements, remarks |

Borderline OT records I kept as OT: R0024 (a security review before deployment applies an existing gate, so OT under
the boundary rule); R0220 (Heineken "made curiosity training mandatory": a rule reported as a fact, with no rule work by the
speaker); R0180 and R0057 (carrying out audits and filings); R0290 (keeping classification data up to date).

## 2. Agreement

| measure | me vs A | me vs B | A vs B |
| --- | --- | --- | --- |
| exact code-set match | 36/40 | 37/40 | 35/40 |
| PV present/absent | 39/40 | 40/40 | 39/40 |
| PE present/absent | 39/40 | 38/40 | 38/40 |
| RD present/absent | 40/40 | 40/40 | 40/40 |
| AO present/absent | 37/40 | 38/40 | 37/40 |
| any rule work (PV/PE/RD) | 39/40 | 39/40 | 38/40 |

## 3. Disagreements: who is right and why

| id | me | A | B | verdict |
| --- | --- | --- | --- | --- |
| R0054 | PE, PV | OT | PV | **B is right; A under-codes.** Finding gaps in controls and fixing the root cause is PV: it names a gap between the written and the actual rule and a change that followed. PE as a second code is defensible. A's generic "no rule work" reason misses this. |
| R0088 | AO | OT | PE | **Neither is fully right; A is closer on rule work.** No escalation condition is set, only a human exception step in a pipeline, so B's PE is an over-read. A misses the agent work (AO). |
| R0135 | AO | AO | OT | **A is right.** Implementing bots is AO; B treats it as a remark. |
| R0342 | PE, AO | PE | PE, AO | **B is right.** Both coders agree on PE; A drops the AO second code. |
| R0397 | PE, AO | PE | PE, AO | **B is right.** Same pattern: A drops the AO second code. |

## 4. Verdict: under- or over-coding of rule work?

**No systematic under-coding of rule work by the coders.** The real sample simply has little rule work: 3/40 (7.5%).

- **Coder A:** codes 2 of my 3 rule-work records. It has **1 under-code** (R0054, a real gap-finding/remediation statement)
  and 0 over-codes. Rule-work recall is 2/3. A also uses only one code per record on these real records: it never
  gives a second code and drops AO on 3 records (R0088, R0342, R0397). A's boilerplate reason for every OT suggests
  a quick default to OT.
- **Coder B:** codes all 3 of my rule-work records (recall 3/3). It has **0 under-codes** and **1 arguable over-code**
  (R0088 coded PE for a human-exception step with no stated condition). B misses one AO record (R0135).
- **Records any coder might have missed:** I re-checked all 35 OT records for approval limits, escalation conditions,
  permissions or rule changes. None show rule work under strict §6. The closest are R0024 (a gate applied, not set)
  and R0220 (a mandatory policy reported, not designed).

Counts: under-codes of rule work are A = 1, B = 0; over-codes are A = 0, B = 1 (arguable). The disagreement is
at the margins of one or two records, not a bias. With so few positives, though, coder A's single miss already
puts its rule-work recall at 0.67, below the 0.7 bar in §6. On this sample, the seeded-case recall should decide
whether an absence of PV is interpretable. A low PV/PE/RD count on real records is not, by itself, evidence that
the coders missed rule work.
