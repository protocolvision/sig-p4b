# I4 review: required-functions coding

Reviewed 10 October 2026. Inputs: `triangulation-design.md` (section 3, I4 row; sections 4.4, 7, 10),
`instruments/I4-required-functions.csv` (103 rows), `instruments/I4-coverage.md`, `corpus/manifest.csv`,
`corpus/index.csv` and the corpus texts named below. Row numbers are CSV line numbers (header = line 1).

Baseline counts (current file):

| rule type | rows | names_role = yes | owns_rule_changes = yes |
| --- | --- | --- | --- |
| Lab self-policy (Anthropic 31, OpenAI 4, DeepMind 6) | 41 | 36 | 20 |
| Law or supervisory rule (RTS 6 24, AI Act 15, Omnibus 3, NERC 4, Colorado summary 2) | 48 | 3 | 17 |
| Voluntary framework (NIST 13) | 13 | 0 | 1 |
| Platform terms (Amazon) | 1 | 0 | 0 |

So 36 of the 39 "names a role" rows are lab self-policies, and 27 of those 36 are Anthropic RSP versions.
As the file stands, any finding that "rules name roles" is mostly a finding about Anthropic's RSP.

## Critical fixes

1. **Merge policy versions into one provision with a change history (confirmed, and the problem is larger than the row count).**
   Rows 63-93 (Anthropic RSP v1.0-v3.4, 31 rows, 30% of the file) code the same four provisions up to nine times. Rows 74-93
   (v3.0-v3.4) have identical `required_function` text across five versions. Within each version, ownership is also
   counted twice: the RSO row ("proposes policy updates", rows 68, 71, 74, 78, 82, 86, 90) and the "policy changes" row
   (rows 67, 70, 73, 77, 81, 85, 89, 93) both code `owns_rule_changes = yes` for the same CEO/RSO/Board change process.
   The same issue applies to DeepMind FSF (rows 98-103, four versions) and, within one version, OpenAI rows 94 and 97
   (both code SAG as owning framework changes).
   Fix: one row per provision per policy (`policy_family` + `provision`), with `first_version`, `last_version`,
   `versions_present` and a `change_history` cell (e.g. "v1.0 Board approves after LTBT consultation; v2.0 adds CEO+RSO
   as proposers; v3.0 adds independent noncompliance channel"). Expected result: Anthropic about 4-5 rows, DeepMind
   about 3, OpenAI 3. Keep ownership in one row per policy (the change-process row), not in the officer row too.

2. **Add `rule_type` and `addressee` columns, and restrict the I4 primary analysis to binding rules that address deploying or operating firms (confirmed, plus an addressee problem inside the laws).**
   Beyond the type mix in the table above, `applies_to` is free text and hides who is bound. All five AI Act rows
   coded `owns_rule_changes = yes` (rows 27, 28, 32, 34, 38) bind **providers** (Arts 9, 11, 17, 43) or describe a
   deployer turning into a provider (Art 25). The number of AI Act rows where a **deployer** owns rule changes is zero.
   NIST (rows 48-60) is voluntary; NERC binds grid operators, not AI deployers; labs bind themselves as developers.
   Fix: `rule_type` in {statute/regulation, supervisory rule or standard, voluntary framework, lab self-policy,
   platform terms, legislative summary}; `binding` in {yes, no}; `addressee` in {deploying/operating firm,
   provider/developer, both, platform user}. Report I4 on binding x deploying/operating rows; report labs, NIST and
   platform rows as a separate comparison set, never pooled.

3. **Split `owns_rule_changes`; it currently mixes "the provision regulates change" with "someone owns the change", and is over-coded.**
   The coder's definition counts "approving, reviewing, **recording** or proposing changes to the system's rules,
   limits, parameters" and also changes to documents. Of the 17 law/supervisory "yes" rows, 13 name no owner at all
   (`role_title` empty): rows 2, 8, 9, 10, 19, 24, 25, 27, 28, 32, 34, 38 and NIST row 55.
   Over-coded (should be "no" or moved to the new `regulates_changes` field only):
   - row 28 (AI Act Art 11: technical documentation kept up to date; a document, not rules);
   - row 34 (Art 25(1)(b): a legal reclassification of whoever modifies a system, no owner);
   - row 38 (Art 43(4): new conformity assessment after modification; regulator procedure);
   - row 27 (Art 9: risk management system "reviewed and updated"; provider-side, no owner);
   - row 55 (NIST MANAGE 4.1: "change management" is one word in a list);
   - row 25 (RTS 6 Art 21(5): recording modifications is recordkeeping, not ownership);
   - row 99 (DeepMind v2.0: council "reviews implementation", which does not approve changes).
   Under-coded:
   - row 95 (OpenAI Leadership: SAG recommendations on framework changes are "processed according to the standard decision-making process", where Leadership makes "all final decisions"; Leadership is the approver, so code yes, at least as strong as SAG in row 97);
   - row 11 (RTS 6 Art 8: the firm sets predefined limits before deployment, coded "unclear" while the parallel Art 15 row 19 is "yes");
   - row 3 ("unclear" for a separation-of-duties provision should be "no").
   Fix: replace with two fields. `regulates_changes` (yes/no: the provision governs changes to the system's rules,
   limits or parameters). `change_owner` (named title / designated individual / function or body / firm in general /
   none). Drop "recording" and "document kept up to date" from the definition. Normalise the compound labels
   ("yes (proposes policy updates)" and five others) into the enum, with the comment in a `note` column.

4. **`names_role` is applied inconsistently, and this flips the trading vs AI comparison.**
   The rule is "yes where the text names a title or a designated body or person, including 'person designated by senior
   management'". RTS 6 rows 7, 14 and 18 (designated person or individual) are coded yes. But AI Act Art 26(2), row 35
   ("Deployers shall assign human oversight to natural persons who have the necessary competence, training and
   authority", line 1497 of C9b1da45a) is a designation of individuals and is coded "no", as is row 30. NERC row 44
   codes "System Operator", which is a defined NERC Glossary title, as "no". RTS 6 row 20 ("trader in charge of the
   algorithm") is "no". With these errors, laws on trading appear to name roles and the AI Act appears not to.
   Fix: replace the binary with a four-level `role_specificity`: titled role (RSO, CEO, System Operator, SAG) /
   designated individual without a title (RTS 6 Arts 5(2), 11, 15; AI Act Art 26(2), 14(5)) / function or staff group
   (compliance function, risk management function) / none. Recode rows 7, 14, 18, 20, 30, 31, 35, 44 and all lab rows
   on this scale.

5. **Core rule texts are missing or uncoded (confirmed, with two corrections).**
   - Uncoded, wrong manifest category (confirmed): FINRA RN 15-09 (C07e09d04), RN 16-21 (C6b47f19f), PRA SS5/18
     (Cef3dde3f PDF; Ce06358c0 web), NERC PER-003-2 (C84c34c54; -1 and -0 are HTTP 404), FCA SYSC 27 (C060d8f5f),
     FCA algorithmic trading review (Ceb232737, C3db6f9c1). Recategorise as `rule-text` (or code by a list of rule
     ids, not by category) and code them.
   - **SEC Rule 15c3-5 (C9e5e0522)** is full regulation text (LII copy, 7.5 KB, paras (a)-(f)) and is uncoded; the
     coverage file still says it is "not found". Code at least: (b) documented controls and supervisory procedures;
     (c)(1)(i)-(ii) pre-set credit, capital, price and size thresholds; (c)(2)(iii) access restricted to pre-approved
     persons; (c)(2)(iv) "appropriate surveillance personnel" receive post-trade reports; (d) controls "under the direct
     and exclusive control" of the broker-dealer (`regulates_changes` yes, parallel to RTS 6 Art 20(2), row 24);
     (e)(1) annual written review; (e)(2) annual CEO certification (titled role). Date in text: 75 FR 69825, 15 Nov 2010.
   - **Colorado SB26-189: the "new" source C1b071d1a is not new.** It is the same bill page as C5343d573 (URL differs
     only in case; same 123,414 bytes; the text files differ only in the SOURCE line). It still holds only the staff
     bill summary and history, not the act. Fetch the "Recent Bill (PDF)" or signed act linked from the page; drop
     C1b071d1a as a duplicate. Rows 61-62 stay marked as summary-only until then.
   - California SB 53: still absent (confirmed).
   - DeepMind web page C9ae49a11: confirmed binary (compressed bytes after the header). Low impact for I4 because all
     four FSF PDFs (C25f47316, Cf018b703, Cd899a8f2, Ce9065d39) are readable and coded; exclude the web page.

6. **Deployer-side provisions missing from texts that were coded.**
   The I4 question is about deploying firms, yet the deploying-firm rows in the AI Act are only rows 26, 35, 36, 37
   (and 30/31 in part). Not coded: Art 27 fundamental rights impact assessment (deployers including banking and
   insurance under Annex III 5(b)-(c); the deployer must set governance and human-oversight arrangements; see recital
   at line 612 of C9b1da45a); Art 26(1) (technical and organisational measures to use per instructions); Art 26(7)
   (inform workers' representatives). NERC PER-005-2 R2 (Transmission Owner) and R5 (verification) were skipped.
   Colorado summary: "Developers must notify deployers of material updates or modifications" (a change-control duty)
   was not coded. Fix: code these before any deploying-firm count is taken.

## Minor issues

- Rows 32 and 33 both code AI Act Art 17(1)(m); delete the row 33 duplicate or fold it into row 32.
- Row 31 `applies_to` says "deployers"; Art 14(5) is a provider design measure that constrains deployers (row 30 states this correctly).
- Row 59 (NIST MS-4.2-005) paraphrases as "deployment approval go/no-go decisions"; the action is to document how public feedback is used in those decisions.
- In several multi-paragraph rows the quote supports only one part of `required_function` (row 12 quotes approval only; row 23 quotes Art 18(3), not the access restriction in 18(5); row 8 quotes retesting only). Add a second quote or split the rows.
- Effective dates missing where public: NERC PER-005-2 (text gives only a formula); Omnibus (OJ publication date). Fill in from the OJ or NERC effective-date pages, marked as external.
- Colorado rows 61-62 rest on a legislative staff summary; mark `rule_type = legislative summary` and exclude from binding counts until the act is fetched.
- 26 rows (25%) are "unclear" for ownership; after fix 3 most should resolve, and any that remain need a one-line reason.
- `I4-coverage.md` is stale: it lists SEC 15c3-5 as not found and does not mention C1b071d1a.
- Ten NIST quotes (rows 48-51, 55-60) fail a plain string match because the PDF text interleaves table columns. I checked rows 50, 55, 58 and 59 by hand and they are present. Fine, but record the line numbers so others can verify.

## Sample check

Random sample of 15 rows (Python `random.seed(20261010)`): rows 7, 23, 24, 31, 34, 43, 44, 46, 47, 52, 53, 82, 86, 95, 104.
All 103 quotes were also checked by script (whitespace, case and punctuation ignored): 93 match directly and 10 NIST
rows match only after joining across interleaved columns (see minor issues).

| field | correct | errors |
| --- | --- | --- |
| quote exists in source | 15/15 | none |
| required_function fair, neutral paraphrase | 15/15 | none in the sample (row 59, outside the sample, is skewed) |
| applies_to | 14/15 | row 31 (provider measure coded as deployer duty) |
| names_role | 14/15 | row 44 ("System Operator" is a NERC Glossary title; should be yes under the coder's own rule) |
| owns_rule_changes | 12/15 | row 34 over-coded (yes, should be no); row 95 under-coded (unclear, should be yes); row 43 unclear, should be no |

Systematic pattern. The random sample is about 80% accurate on ownership, but a targeted pass over all 17
law/supervisory "yes" rows finds 5-6 over-codings (rows 25, 27, 28, 34, 38, plus NIST row 55). The causes are the
broad definition (recording, documentation, regulator procedures) and missing addressee information. Errors go
both ways (rows 11 and 95 are under-coded), so the net count is wrong in a way that cannot be predicted. On
`names_role` the error is directional: designated individuals are counted in trading rules but not in the AI Act.
