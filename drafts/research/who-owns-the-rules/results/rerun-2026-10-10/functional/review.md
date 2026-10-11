# Functional analysis: independent review (11 October 2026)

Fresh reviewer. I re-ran nothing that writes to this folder; all checks are scratch scripts.

## Critical fixes

**1. Q5 service management is mostly not service management, so drop "support matches IT."** In 20 matches drawn with sampling weights (seed 20261012), only 9 were IT/service-management duties (45%, Wilson 26-66%). The false positives were retail price "ticketing", GMP and contract "change control/change request", "on-call" shifts, and generic "service levels" in retail and logistics. "ServiceNow" also picks up the employer's name: in sales it carries about as much weighted mass as "service level". Remove ServiceNow, change control, change request, ticketing and on-call, or require an IT context word.

**2. Q5 security review is about 60% precise and circular.** 12 of 20 matches were real security-review work (60%, 39-78%). Four of the 20 were boilerplate ("abide by security policies", "report any suspected information security violation"). In marketing (61%) and manufacturing (55%) most matches are boilerplate; in data/AI it is 30%. The security function is defined by "security" in the title, and the family includes "cybersecurity", "information security" and "security polic", so 172 per 1,000 is largely built in. The function also contains physical and store security: about 69 postings and roughly 13% of its weighted base (store security specialists, "Security Associate"). These match "access control" and "security control" in the physical sense. Exclude the boilerplate pattern, add physical-security titles to the guard exclusion, and do not use the security-review row as a finding.

**3. The Q2 caveat points the wrong way for IT.** Here is observed against expected confirmations under each task's own sampling-group rate (S1 30%, rest20 9.7%):

| Function | Confirmed | Expected | Ratio |
| --- | --- | --- | --- |
| Manufacturing | 2 | 6.0 | 0.33 |
| IT | 2 | 3.1 | 0.65 |
| Data/AI | 28 | 18.9 | 1.48 |
| Security | 7 | 4.2 | 1.69 |

The IT shortfall is a single task, so it is noise. Manufacturing is plausibly overstated. The larger bias is that data/AI and security are understated. Function-specific rates, shrunk toward the pooled rate, give about 23% for data/AI, about 12% for security and 12.6% for software, against the published 10.2%, 5.8% and 8.1%. IT is unchanged (5.4%). Rewrite the caveat: the ordering holds, and the two top cells are conservative.

**4. In Q4, "no function named" is mostly classifier misses.** In 30 sampled first reports-to phrases:
- The classifier named a department in 21. 20 of those were right (precision 95%, 77-99%).
- It returned "no function named" in 9. In 7 of those a department was recoverable from the sentence: the phrase was cut at an en dash ("Manager – Automation and Controls"), at "U.S-based" (the ABBR rule needs a trailing period), or it missed "SEO", "QE" or "AIT".
- One phrase was not a reporting line ("experience ... reporting to senior leaders").

The 18% "none" share and the department split are therefore biased toward whatever the keywords catch, which is data/AI. The phrases are also clustered by employer: one employer's template gives 34 of 230 (15%), the top three give 30%, and only 209 of the 230 sentences are distinct. The Wilson intervals treat these as independent. Fix the cut rules, dedupe sentences, and use an interval clustered by employer.

**5. The function map is less accurate than the self-score.** I labelled 60 postings blind, drawn by sampling weight from the 25,512 (seed 20261012), and then compared them with the map:
- 49/60 strictly correct (82%, Wilson 70-89%).
- 57/60 counting defensible alternatives (95%, 86-98%).
- 3 wrong: "Chief Engineer" going to executive via "chief", a BMC firmware engineer going to IT, and a non-English logistics title going to "other".

Because a weighted draw holds few technical postings, I added 40 drawn from data/AI, software, IT, security and "other" (seed 20261013). That draw scored 29/40 strictly (72%) and 38/40 with alternatives. The confusions that matter:
- Security in the title wins over everything. A software lead's "Security Protocols" title and a sales "Solution Consultant – Security" both go to security, and bare "Security" guard titles land there too.
- The data/AI versus software boundary is soft. "Software Engineer, Data Platform" goes to data/AI, while "AI Evaluation Infrastructure Engineer" goes to software via O*NET.
- Firmware, BIOS and BMC work splits between software and IT.
- Talent-pool and non-English titles fall to "other".

Report 82% strict (95% lenient) alongside the 90%, which was scored by the map's author.

**6. Q1 strip-and-remap removes keyword circularity only.** 172 of the 446 AI-titled postings in data/AI reach that class through an O*NET code (mostly 15-2051) that the model assigned from a title that still contained "AI". Say so in the Q1 limits. The ordering is safe, but the 16.3% level is partly built in.

## Reproduction

All 563 Q1-Q3 rows in `tables.csv` equal `tables-q1q3.csv`. Every Q1 and Q2 figure in results.md matches the table. The Q2 weighted total is 2,528.5, which reproduces I1-twophase (189 + 2,340). The weighting is correct. AI-titled and human-agent postings are censuses with weight 1, rest20 has weight about 5, and the weighted 2.7% agrees with the unweighted 110,715-title census (2.8%). The Q1 Wilson-on-Kish intervals are appropriate.

## Q5 precision summary (20 weighted matches each)

| Family | Precise | Share (Wilson) | Main false positives |
| --- | --- | --- | --- |
| AI governance | 17/20 | 85% (64-95) | "human-in-the-loop patterns" as build steps; a sales talking point |
| Guardrail/permission | 13/20 | 65% (43-82) | Physical access control; real-estate "entitlement"; film-shoot "permissions"; experiment "guardrail metrics"; construction approval workflows |
| Security review | 12/20 | 60% (39-78) | See fix 2 |
| Service management | 9/20 | 45% (26-66) | See fix 1 |

## What can headline

1. **Demand for AI titles is a technology-function phenomenon.** Data/AI 16.3% (13.7-19.4), software 10.8%, IT 9.4% and security 8.6%, against 2.7% overall and under 1% in sales, support, finance, HR, legal and healthcare. The census agrees within a point. This is solid.
2. **Software, IT and data/AI hold 61% of AI-titled postings.** Manufacturing's 13% is industrial "automation" (1.5 of its 1.6 points), not AI. Agent or agentic titles are 0.1%. This is solid.
3. **About 2.4% (1.7-3.1) of existing-title postings carry a confirmed agent duty.** Data/AI is highest at 10.2% and software is at 8.1%. Present these as conservative, per fix 3, and give the ordering rather than the levels for security and IT. This can headline with that caveat.
4. **AI-titled postings rarely say who the role reports to.** 7.8% (6.9-8.8) name a reporting line; extraction misses are few in this direction. Say only that the data/AI and engineering lines lead among named departments. Do not headline the department split until fix 4 is done.
5. **AI-governance duties concentrate in data/AI.** The rate is 10.5 per 1,000 duties against 1.0 overall, and the family is 85% precise. It can headline with caveats. The guardrail peak in security needs the physical-access fix first.

Caveat or drop:
- Drop "service management sits in support and IT".
- Drop the security-review row as a finding.
- Keep the Q3 counts and the speech contrast as illustrations, not rates.

## Suggested figure

Use three aligned dot-and-whisker columns with one shared row per function, in the same order in each column, technology block first:
- **Asked for:** AI-title share (Q1).
- **Agent duties:** confirmed agent-duty share in existing-title postings (Q2). Draw a right-pointing tick on data/AI and security to mark them as lower bounds.
- **Controls:** AI-governance and guardrail duties per 1,000 (Q5), once the guardrail list is fixed.

Each column gets its own scale, with a light band behind the technology rows. Animate the columns in sequence (asked, then duties, then controls), so the reader sees the same four rows light up three times while the business functions stay near zero. Add a small footnote glyph on any cell built on fewer than 15 phase-2 tasks.
