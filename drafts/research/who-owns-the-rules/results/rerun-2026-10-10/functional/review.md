# Functional analysis: independent review (11 October 2026)

Fresh reviewer; checks ran as scratch scripts.

## Critical fixes

**1. Q5 service management is mostly not service management.** 9 of 20 weighted matches (seed 20261012) were IT service duties: 45% (Wilson 26-66%). False positives: retail price "ticketing", GMP and contract "change control/request", "on-call" shifts, generic "service levels". "ServiceNow" also matches the employer's name (in sales, as heavy as "service level"). Remove these terms or require IT context; drop "support matches IT".

**2. Q5 security review is about 60% precise and circular.** 12 of 20 matches were real security-review work (60%, 39-78%). Four of the 20 were boilerplate such as "abide by security policies" or "report any suspected information security violation". Boilerplate is most of the matches in marketing (61%) and manufacturing (55%), and 30% in data/AI.

The security function is defined by "security" in the title, and the family contains "cybersecurity", "information security" and "security polic", so the 172 per 1,000 is largely built in. The function also holds about 69 physical or store-security postings (roughly 13% of its weighted base), which match physical "access control". Exclude the boilerplate and physical-security titles; do not report the security-review row as a finding.

**3. The Q2 caveat points the wrong way for IT.** Observed against expected confirmations, using each task's sampling-group rate (S1 30%, rest20 9.7%):

| Function | Observed | Expected | Ratio |
|---|---|---|---|
| Manufacturing | 2 | 6.0 | 0.33 |
| IT | 2 | 3.1 | 0.65 |
| Data/AI | 28 | 18.9 | 1.48 |
| Security | 7 | 4.2 | 1.69 |

The IT gap is noise; manufacturing is plausibly overstated; the bigger bias understates data/AI and security. Function-specific rates shrunk toward the pool give:

| Function | Published | Shrunk rate |
|---|---|---|
| Data/AI | 10.2% | about 23% |
| Security | 5.8% | about 12% |
| Software | 8.1% | 12.6% |
| IT | 5.1% | 5.4% |

The ordering holds; call the top cells conservative.

**4. In Q4, "no function named" is mostly classifier misses.** I checked 30 first reports-to phrases:
- **Named a department (21):** 20 were right, a precision of 95% (77-99%).
- **No department (9):** in 7 the department was recoverable. The causes were cuts at an en dash ("Manager – Automation and Controls"), a cut at "U.S-based" (the ABBR rule needs a trailing period), and missed terms SEO, QE and AIT.
- **Not a reporting line (1):** "experience ... reporting to senior leaders".

So the 18% "none" share and the department split lean toward what the keywords catch, mainly data/AI. Phrases also cluster: one employer's template gives 34 of 230, the top three employers 30%, and only 209 sentences are distinct, yet the Wilson intervals assume independence. Fix the cuts, dedupe, and cluster intervals by employer.

**5. The function map is less accurate than the self-score.** I drew 60 postings weighted (seed 20261012) and labelled them blind:
- **Strictly correct:** 49/60, 82% (Wilson 70-89%).
- **Including defensible alternatives:** 57/60, 95% (86-98%).
- **Wrong (3):** "Chief Engineer" sent to executive by the word "chief"; a BMC firmware engineer sent to IT; a non-English logistics title sent to other.

A supplementary 40 from data/AI, software, IT, security and other (seed 20261013) scored 29/40 strictly (72%) and 38/40 with alternatives. The confusions that matter:
- **"Security" in a title wins over everything else.** A software lead with "Security Protocols", a sales consultant for security products and plain "Security" guard titles all land in the security function.
- **The data/AI and software boundary is soft.** "Software Engineer, Data Platform" goes to data/AI; "AI Evaluation Infrastructure Engineer" goes to software.
- **Firmware, BIOS and BMC roles split between software and IT.**

Report 82% next to the author-scored 90%.

**6. Q1 strip-and-remap removes only keyword circularity.** 172 of data/AI's 446 AI-titled postings get there via an O*NET code (mostly 15-2051) assigned from the AI-bearing title. Ordering is safe; the 16.3% level is partly built in. Add to limits.

## Reproduction

All 563 Q1-Q3 rows of `tables.csv` equal `tables-q1q3.csv` and match results.md. The Q2 total (2,528.5) reproduces I1-twophase (189 + 2,340). Weighting is correct (censuses at weight 1, rest20 at about 5); the weighted 2.7% matches the census 2.8%.

## Q5 precision (20 weighted matches per family)

| Family | Precise | Wilson |
|---|---|---|
| AI governance | 17/20 | 64-95% |
| Guardrail/permission | 13/20 | 43-82% |
| Security review | 12/20 | 39-78% |
| Service management | 9/20 | 26-66% |

Guardrail false positives were physical access control, real-estate "entitlement", film-shoot "permissions", "guardrail metrics" in experiments, and construction approvals. AI-governance false positives were mostly "human-in-the-loop" used as a build pattern.

## What can headline

1. **AI titles sit in technology functions (solid).** Data/AI 16.3% (13.7-19.4), software 10.8%, IT 9.4%, security 8.6%; 2.7% overall; under 1% in sales, support, finance, HR, legal, healthcare.
2. **Software, IT and data/AI hold 61% of AI-titled postings (solid).** Manufacturing's 13% is industrial "automation"; agentic titles are 0.1%.
3. **About 2.4% (1.7-3.1) of existing-title postings carry a confirmed agent duty.** Data/AI 10.2% and software 8.1% lead. Call these conservative (fix 3); give only the ordering for security and IT.
4. **Few AI-titled postings state a reporting line: 7.8% (6.9-8.8).** Hold the department split until fix 4.
5. **AI-governance duties concentrate in data/AI.** 10.5 per 1,000 against 1.0 overall, 85% precise; usable with caveats. The guardrail peak in security needs fix 2 first.

Drop the service-management and security-review findings; keep Q3 and speech as illustrations.

## Suggested figure

One shared row per function (technology block first, shaded), with three aligned dot-and-whisker columns, each on its own scale:

1. **Asked for:** AI-title share (Q1).
2. **Agent duties:** confirmed agent-duty share (Q2). Put a right-pointing lower-bound tick on data/AI and security.
3. **Controls:** AI-governance plus guardrail duties per 1,000 (Q5, after the fixes).

Animate the columns in sequence so the same four rows light up three times while business functions stay near zero.
