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

## Re-review

Re-reviewed 10 October 2026 against the revised `instruments/I4-required-functions.csv` (111 rows, 18 columns),
`instruments/I4-coverage.md` (revision 2) and the corpus texts. Row numbers are CSV line numbers in the revised file
(header = line 1); they do not match the row numbers above. Quotes were re-checked by script for all 111 rows: 101 match
directly, and the 10 NIST rows (86-89, 93-98) match only across interleaved table columns, as the note column says.

**Verdict: pass, with one small remaining fix (OpenAI ownership, below).** No new critical problems.

### Fix-by-fix status

1. **Versions merged: applied, one cell left.** Anthropic is down to 6 rows, DeepMind to 3 and OpenAI to 4, with
   `versions` and `change_history` filled (checked: row 101 is correctly marked absent in v1.0 and present from v2.0).
   Anthropic ownership now sits only in the change-process row (102); the RSO row (100) is `regulates_changes = no`.
   **Not done for OpenAI:** rows 107 (Leadership) and 109 (Updates to the framework) both code
   `regulates_changes = yes` with Leadership as `change_owner`, so OpenAI's change ownership is counted twice. This breaks
   the coverage file's own rule ("one row per policy"). Row 107's quote is about deployment go/no-go and residual risk,
   which the definition excludes. Fix: row 107 `regulates_changes = no`, `change_owner = none named`.
2. **`rule_type`, `binding`, `addressee`: applied.** The enums differ from the ones proposed (`investment firm`,
   `grid entity`, `lab itself` instead of one "deploying/operating firm" value), but they carry the same information and
   the AI Act provider rows (56, 57, 61, 62, 70) are now separate from the deployer rows (64-69). Two gaps, neither
   critical: (a) PRA SS5/18 is coded `binding = comply-or-explain`, which the text does not support (it says "The PRA
   expects"; no comply-or-explain wording); code it `no` like the FCA and FINRA guidance, or add a "supervisory
   expectation" value; (b) the coverage file does not yet state that the I4 primary count is binding rows addressed to
   operating firms, with labs, NIST and Amazon as a separate set.
3. **`owns_rule_changes` split: applied.** `regulates_changes` and `change_owner` replace it; the compound labels are
   gone. Over-coded rows fixed: Art 9 (56), Art 11 (57), Art 25 (63), RTS 6 Art 21(5) (26), DeepMind council (110) are
   now `no`; Art 43(4) (70) and NIST MANAGE 4.1 (93) stay `regulates_changes = yes` with no owner, which is what the
   fix allowed. Under-coded rows fixed: Art 8 (11) yes, Art 1(c) (3) no, OpenAI Leadership now an owner (but see fix 1).
   Left as is: `change_owner` is free text, not the proposed type enum. It is countable ("none named" against everything
   else: 16 rows have a named owner), so this is not blocking. Row 9 (RTS 6 Art 5(7) change log) stays `yes` under the
   new definition's "a change log that records the approver"; that is a stated choice, but it sits close to the dropped
   "recording" criterion.
4. **`names_role`: applied as one binary rule instead of the four-level scale.** The rule is now the same in all sources:
   AI Act Art 26(2) (65) and 14 (59, 60), NERC System Operators (79, 85), RTS 6 "trader in charge" (21) and Colorado's
   "individual designated by the deployer" (76) are all `yes`. The directional bias found earlier is gone. Two
   remaining inconsistencies, not critical: PRA 2.3 (43, "define lines of responsibility") is `yes`, while the same kind
   of provision is `no` in RTS 6 Art 1(a) (2), AI Act Art 17(1)(m) (62) and NIST GOVERN 2.1 (86); and NIST GV-4.1-003
   (95) is `yes` although the functions are only examples ("e.g."). The coverage file says an empty `role_title` with
   `yes` marks an untitled designation, but no row is coded that way (untitled designations such as rows 7, 14, 65 and
   76 have their wording in `role_title`); so titled and untitled roles cannot be told apart. Correct the sentence.
5. **Missing texts: applied.** SEC 15c3-5 is coded at every paragraph listed ((b), (c)(1), (c)(2)(iii)-(iv), (d), (e)(1)-(2);
   rows 27-33). FINRA RN 15-09 and 16-21, PRA SS5/18, NERC PER-003-2, FCA SYSC 27.7 and both FCA reviews are coded
   (rows 34-54, 85). Colorado is now coded from the signed act (`CO-SB26-189-act`, Ch. 131; header and three quotes
   checked against the text), and C1b071d1a is recorded as a duplicate. Outstanding, already listed in the coverage
   file: add the act to `index.csv`/`manifest.csv`; California SB 53 is still absent.
6. **Deployer-side provisions: applied.** AI Act Art 26(1) (64), 26(7) (68), Art 27 (69), NERC PER-005-2 R2 (80) and R5 (83),
   and the Colorado developer notice of material updates (77) are coded.

Earlier minor issues: the Art 17(1)(m) duplicate is gone; the NIST MS-4.2-005 paraphrase (97) is corrected; the
coverage file is current (lists SEC 15c3-5 and C1b071d1a correctly).

### Sample check

Random sample of 15 rows, stratified so that 6 come from newly coded texts (Python `random.seed(20261011)`):
rows 3, 6, 7, 18, 28 (SEC), 35, 37, 38 (FINRA 15-09), 42 (PRA), 57, 74, 75, 85 (NERC PER-003-2), 95, 101. Because the
draw included no FCA or Colorado row, rows 48 (FCA 2018 review 5.7), 76 and 77 (Colorado act) were also checked by
hand; they are outside the accuracy counts.

| field | correct | errors |
| --- | --- | --- |
| quote exists in source | 15/15 | none |
| rule_type | 15/15 | none |
| binding | 14/15 | row 42 (PRA SS5/18 coded comply-or-explain; text says "expects") |
| addressee | 15/15 | none |
| names_role (one rule) | 14/15 | row 95 (NIST GV-4.1-003: oversight functions given only as "e.g.") |
| regulates_changes | 15/15 | none (rows 28 and 37, limit-setting and parameter changes, are consistent with RTS 6 Art 8) |
| change_owner | 15/15 | none |

Extra rows: 48 and 76 are correct on all fields. Row 77 (Colorado developer notice of material updates,
`regulates_changes = yes`) can be argued either way: it is a notice after the change, not approval of it, but "material
update" is defined to include model parameters and default settings (6-1-1701(14)). Keep it, with the note.

### Remaining fixes

Critical: none that would change the primary (binding, operating-firm) counts.

Required before I4 is used (small):
- Row 107: set `regulates_changes = no` and `change_owner = none named`, so that OpenAI change ownership is counted once (row 109). This finishes fix 1.

Recommended:
- PRA SS5/18 rows 42-47: change `binding` from comply-or-explain to `no` (or a "supervisory expectation" value).
- Align `names_role` for generic "define lines of responsibility" provisions (row 43 against rows 2, 62 and 86), and row 95.
- Correct the `role_title` sentence in `I4-coverage.md`, and state the primary-analysis restriction there.
- Add `CO-SB26-189-act` to `index.csv` and `manifest.csv`.
