# Part 2 summary: written governance documents naming a decider

Quotes checked verbatim by script against stored files; pass count in the final report.

| Domain | Documents | Name a decider | Strongest binding level naming one |
|---|---|---|---|
| AGT AI agents | 8 | 7 | regulator-guidance |
| CRD Credit | 4 | 3 | regulator-guidance |
| PRC Pricing | 4 | 3 | law |
| FRD Fraud/AML | 5 | 4 | law |
| CHG IT change | 3 | 2 | firm-policy |
| ACC Access/identity | 5 | 4 | firm-policy |
| TRD Trading limits | 5 | 3 | regulator-guidance |
| CLN Clinical | 5 | 4 | law |
| PRO Procurement | 5 | 4 | law |

## Notes

- All eight comparison domains have at least one document naming a decider; AGT has seven rows coded yes, but none is agent-rule specific and none is law.
- AGT: no public document found that names who approves changes to an AI agent's own rules or permissions. Named deciders are for AI use or AI risk generally (OMB CAIO and governance board, Oregon EIS, Ohio AI Council, NIST executive leadership). SR 11-7 (AGT-03) concerns models, not agents; counting it as agent-specific would inflate AGT.
- Document-count rule: AGT includes 8 rows (including two reused from corpus/b-raw/platforms/E) because agent-specific sources are thin; other domains have 3-6 rows.
- Coding choices: NIST CM-3 and AC-2 leave the approver as an organization-defined placeholder, coded names_decider=no. 15c3-5 and 17 CFR 1.73 require limits and CEO certification but do not name who approves limit changes (no). 42 CFR 482.12 names the governing body as responsible but not for formulary or protocol rules (no).
- Binding labels: OMB memos are labelled regulator-guidance (binding on federal agencies only). State and university policies are labelled firm-policy (public-body policy). Philippine bank charters (FRD-03, FRD-04) and the Malaysian Tropicana charter (PRC-02) are non-US.
- Weak or partial: PRO-03 quote verified in text, but the schedule's tables were not read. CHG-01 and ACC-01 are CSF Tools mirrors of NIST SP 800-53 Rev 5. ACC-03 shows only an 'approved by' line plus CIO administrative authority; CHG-03 Rowan's CAB is advisory.
- Gaps: no ITIL or ISO 20000 official text (paywalled); SVB and Auckland Airport charters, UCSF P&T charter, FFIEC BSA/AML manual page and the SEC 10-K pages were blocked (captcha, bot checks) and are not used; no Joint Commission text (paywalled/sign-in); no US corporate sales discount-approval policy found (PRC rests on one foreign charter, one hospital, GSAM); SR 11-7 uses the Fed attachment PDF.
- Purposive sample, not a census.

## Review corrections (Opus, review.md)

- Agents: no document names who approves changes to an agent's *rules*. Microsoft Entra Agent ID documentation (vendor, voluntary) names approvers for changes to an agent's *access*: "designated approvers" and sponsors "accountable for making decisions about its lifecycle and access". Only the sponsor role counts as a named decider.
- AGT-07 (Ohio AI Council) is advisory: recoded as not naming a decider of rule changes.
- PRC-05 (GSAM) names contract parties, not who approves pricing-rule changes: recoded no; pricing's strongest level is firm policy.
- FRD-02: the monitoring designee is not a decider; the board-approval line in the same file keeps the yes.
- CLN-01 names who sets up the formulary, not who approves changes: weak.
- Limits added: 48 of 60 agent items come from AI-titled postings; "change management" also matched regulatory and organisational change; clinical matched clinical-trial protocols; trading (7) and clinical (5) are too small to read.
