# Functional analysis: who does what with AI, by business function

Descriptive, added at the user's request (design in `design.md`). Run on the 25,512 selected postings (`I1-posting-level.csv.gz`), 305,533 extracted duty statements, 600 phase-2 coded tasks, the platform-controls P2 recode and the I6 speech counts. Functions come from one map (`function_map.py`); every figure inherits its error (see Limits). Intervals are 95%.

## Function map and hand spot check

Title keywords (security, legal, support, data/AI, sales, plus short finance, HR, marketing, software and executive lists) are applied first; otherwise the O*NET detailed code of `postings-mapped-v2.csv` is looked up by detailed code, minor group, then major group; otherwise 'other'. The full tables and keyword lists are in `function_map.py`.

Spot check of 60 postings (40 drawn in proportion to sampling weight, 20 from AI-titled postings), judged by me from title, employer and department (not from posting text; not an independent coder). The first version of the map scored 44/60 correct (73%, 6 partly defensible, 10 wrong), mostly because 'Security Consulting Engineer' and similar titles missed the security rule, hardware engineers went to software, 'transformation' pulled AI roles into executive/strategy, and 'Solution Architect' went to sales. I fixed those rules and drew a fresh sample of 60: **54/60 correct (90%, Wilson 80-95%), 5 partly defensible, 1 wrong**; counting partly defensible as correct, 98%. The fixed rules were tuned on the first sample, so only the fresh draw is a fair estimate. This is a check of business function (15 classes), a different target from the 83% major-group check of deviation 18, which scored the O*NET code alone. Verdicts are in `spotcheck-verdicts.csv` and `spotcheck-accuracy.csv`.

## Q1. AI-titled postings are concentrated in data/AI, software, IT and security, with automation titles carrying manufacturing

Share of each function's postings with an AI, ML, automation or agentic term in the title (deviation 14 list, human-agent titles excluded), weighted by the rest20 sampling weight. Function is assigned with the AI term stripped from the title so the term does not define the function. Interval: Wilson on the Kish effective sample size. 'Census check' is the same share over all 110,715 titles of `postings-mapped-v2.csv` (non-excluded boards), with no weighting.

| function | sampled postings | AI-titled (n) | AI-title share | AI/ML terms | automation | agent/agentic | census check | share of all AI-titled |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ALL | 25512 | 2945 | 2.7% (2.5-2.9) | 1.9% | 0.6% | 0.1% | 2.8% |  |
| software engineering | 2625 | 865 | 10.8% (9.5-12.3) | 8.3% | 1.6% | 0.9% | 11.8% | 29% |
| IT and infrastructure | 1464 | 499 | 9.4% (7.9-11.2) | 7.9% | 1.1% | 0.4% | 9.2% | 17% |
| data and AI/ML | 957 | 446 | 16.3% (13.7-19.4) | 15.0% | 0.7% | 0.7% | 17.1% | 15% |
| manufacturing/field | 5038 | 385 | 1.6% (1.3-2.0) | 0.2% | 1.5% | 0.0% | 1.7% | 13% |
| security | 744 | 227 | 8.6% (6.6-11.2) | 7.2% | 0.9% | 0.5% | 8.6% | 8% |
| sales | 4525 | 149 | 0.7% (0.5-1.0) | 0.5% | 0.2% | 0.1% | 0.7% | 5% |
| marketing | 742 | 84 | 2.5% (1.6-4.0) | 2.1% | 0.2% | 0.2% | 2.6% | 3% |
| executive/strategy | 560 | 79 | 3.2% (2.0-5.1) | 2.8% | 0.2% | 0.2% | 3.4% | 3% |
| operations and supply chain | 2754 | 58 | 0.4% (0.3-0.8) | 0.3% | 0.1% | 0.0% | 0.4% | 2% |
| other | 1853 | 57 | 0.6% (0.4-1.1) | 0.5% | 0.1% | 0.0% | 0.6% | 2% |
| finance and accounting | 1514 | 37 | 0.5% (0.3-1.1) | 0.4% | 0.1% | 0.0% | 0.6% | 1% |
| customer service/support | 760 | 25 | 0.7% (0.3-1.7) | 0.5% | 0.1% | 0.1% | 0.8% | 1% |
| legal and compliance | 414 | 15 | 0.9% (0.3-2.6) | 0.8% | 0.1% | 0.0% | 0.9% | 1% |
| HR | 394 | 14 | 0.8% (0.2-2.2) | 0.8% | 0.0% | 0.0% | 0.8% | 0% |
| healthcare/clinical | 1168 | 5 | 0.1% (0.0-0.5) | 0.1% | 0.0% | 0.0% | 0.1% | 0% |

Across all postings 2.7% (2.5-2.9) carry an AI-capability title (census 2.8%). Data and AI/ML leads at 16.3% (13.7-19.4), then software engineering 10.8% (9.5-12.3), IT and infrastructure 9.4% (7.9-11.2) and security 8.6% (6.6-11.2). Executive/strategy (3.2% (2.0-5.1)) and marketing (2.5% (1.6-4.0)) are next; sales, customer service, finance, HR, legal and healthcare are all below 1%. Software engineering (29% of all AI-titled postings), IT (17%) and data/AI (15%) hold most of them; manufacturing/field holds 13% because its base is large, and its 1.6% rate is almost entirely 'automation' titles (1.5%), not AI or agent terms. Agent or agentic titles are rare everywhere (0.1% overall).

## Q2. Confirmed agent duties in existing-title postings sit mainly in data/AI, software, security and IT

Existing-title postings only (S1 study occupations plus the rest20 sample), sampling-weighted. 'Confirmed' uses the two-phase logic of `i1_twophase.py`: a posting with k lexically flagged tasks has probability 1-(1-p)^k of at least one confirmed (AO, PE or RD) task, with p the phase-2 confirmation rate of its sampling group. The estimate reproduces `I1-twophase.md` (S1 189, rest20 2,340 postings). Interval for the two-phase column: percentile bootstrap (2,000 resamples) over postings within group and over the phase-2 sample (it does not include lexical-recall error). The last column is the direct confirmation rate of the sampled flagged tasks in that function (Wilson intervals in `tables.csv`); it rests on very few tasks outside data/AI, software, security and manufacturing.

| function | existing postings (sampled) | flagged by lexical screen | confirmed agent duty (two-phase est.) | phase-2 tasks confirmed |
| --- | --- | --- | --- | --- |
| sales | 4152 | 5.7% (5.1-6.5) | 0.8% (0.6-1.1) | 5% of 22 |
| customer service/support | 671 | 12.1% (9.8-14.8) | 1.8% (1.2-2.6) | 0% of 2 |
| marketing | 653 | 19.7% (16.8-22.9) | 3.6% (2.3-4.9) | 16% of 19 |
| finance and accounting | 1476 | 12.8% (11.1-14.6) | 1.7% (1.2-2.3) | 9% of 11 |
| HR | 380 | 13.3% (10.3-17.2) | 2.1% (1.3-3.1) | 0% of 5 |
| legal and compliance | 398 | 18.9% (15.0-23.4) | 3.1% (2.1-4.3) | 12% of 8 |
| IT and infrastructure | 960 | 29.8% (27.0-32.8) | 5.1% (3.5-6.9) | 6% of 32 |
| security | 510 | 32.2% (28.2-36.5) | 5.8% (4.0-7.7) | 29% of 24 |
| software engineering | 1700 | 38.8% (36.3-41.3) | 8.1% (6.0-10.3) | 19% of 138 |
| data and AI/ML | 548 | 46.3% (41.9-50.8) | 10.2% (7.6-13.0) | 35% of 80 |
| operations and supply chain | 2651 | 11.5% (10.4-12.8) | 1.5% (1.0-2.1) | 8% of 25 |
| manufacturing/field | 4645 | 11.3% (10.4-12.2) | 1.8% (1.2-2.4) | 3% of 62 |
| healthcare/clinical | 1161 | 1.4% (0.9-2.2) | 0.2% (0.1-0.3) | 0% of 1 |
| executive/strategy | 479 | 19.6% (16.3-23.4) | 3.3% (2.1-4.6) | 12% of 8 |
| other | 1754 | 5.5% (4.5-6.7) | 0.8% (0.5-1.1) | 0% of 13 |
| ALL | 22138 | 13.8% (13.4-14.3) | 2.4% (1.7-3.1) | 16% of 450 |

About 2.4% (1.7-3.1) of existing-title postings carry a confirmed agent duty. By function the estimate is highest in data and AI/ML (10.2% (7.6-13.0)), software engineering (8.1% (6.0-10.3)), security (5.8% (4.0-7.7)) and IT (5.1% (3.5-6.9)), then marketing (3.6% (2.3-4.9)), executive/strategy and legal; it is under 1% in sales, healthcare and 'other'. These figures apply each sampling group's confirmation rate to every function in it; the direct function-level rates in the last column show the assumption is loose (IT and manufacturing/field confirm less often than the group rate, data/AI and security more), so the IT and manufacturing/field estimates are probably too high. Functions with fewer than 15 sampled tasks (HR, support, finance, healthcare, legal, executive, 'other') should be read as 'not distinguishable from zero or from the average'.

## Q3. Running agents (AO) is the common activity; setting limits (PE) is rarer and sits in data/AI, security, IT and software

Counts of phase-2 coded tasks by the function of the posting they come from. Final code = coders' agreed code, else the blind adjudication; a task with two codes counts under each. The 600 tasks are a stratified sample of lexically flagged tasks (150 S1, 300 rest20, 150 new-title), so counts are unweighted sample counts, not population rates. No task has a final RD code.

| function | tasks sampled | AO | PE | PV | RD | AO existing / new-title | PE existing / new-title |
| --- | --- | --- | --- | --- | --- | --- | --- |
| sales | 27 | 2 | 1 | 0 | 0 | 0 / 2 | 1 / 0 |
| customer service/support | 2 | 0 | 0 | 0 | 0 | 0 / 0 | 0 / 0 |
| marketing | 27 | 3 | 0 | 0 | 0 | 3 / 0 | 0 / 0 |
| finance and accounting | 13 | 1 | 0 | 0 | 0 | 1 / 0 | 0 / 0 |
| HR | 5 | 0 | 0 | 0 | 0 | 0 / 0 | 0 / 0 |
| legal and compliance | 9 | 1 | 0 | 0 | 0 | 1 / 0 | 0 / 0 |
| IT and infrastructure | 52 | 4 | 5 | 0 | 0 | 1 / 3 | 1 / 4 |
| security | 30 | 5 | 6 | 1 | 0 | 5 / 0 | 3 / 3 |
| software engineering | 166 | 31 | 6 | 0 | 0 | 22 / 9 | 5 / 1 |
| data and AI/ML | 137 | 36 | 11 | 1 | 0 | 21 / 15 | 7 / 4 |
| operations and supply chain | 27 | 2 | 3 | 0 | 0 | 1 / 1 | 1 / 2 |
| manufacturing/field | 76 | 2 | 1 | 0 | 0 | 2 / 0 | 0 / 1 |
| healthcare/clinical | 1 | 0 | 0 | 0 | 0 | 0 / 0 | 0 / 0 |
| executive/strategy | 15 | 1 | 0 | 0 | 0 | 1 / 0 | 0 / 0 |
| other | 13 | 0 | 0 | 0 | 0 | 0 / 0 | 0 / 0 |
| ALL | 600 | 88 | 33 | 2 | 0 | 58 / 30 | 18 / 15 |

Platform-controls P2 recode (`p2-final.csv`), posting items only (117 of the 288 items; the rest are speech spans): whether the text is about changing a setting in a tool (tool_change), deciding or approving what an agent may do (decision), or neither.

| function | tool_change | decision | neither |
| --- | --- | --- | --- |
| sales | 0 | 0 | 3 |
| marketing | 0 | 0 | 3 |
| finance and accounting | 0 | 0 | 1 |
| legal and compliance | 0 | 0 | 1 |
| IT and infrastructure | 0 | 2 | 7 |
| security | 0 | 2 | 8 |
| software engineering | 0 | 1 | 35 |
| data and AI/ML | 1 | 5 | 40 |
| operations and supply chain | 0 | 0 | 4 |
| manufacturing/field | 0 | 0 | 3 |
| executive/strategy | 0 | 0 | 1 |
| ALL | 1 | 10 | 106 |

Of 600 tasks, 88 carry AO, 33 PE, 2 PV and none RD. Data and AI/ML (36) and software engineering (31) hold 76% of the AO tasks. PE is spread over data/AI (11), security (6), software (6), IT (5) and operations (3); PE tasks split almost evenly between existing-title (18) and new-title (15) postings although new-title tasks are a quarter of the sample, and AO tasks are 58 existing to 30 new-title. The two PV tasks are one security and one data/AI posting. In the P2 recode, 10 of 117 posting items describe a decision and 1 a tool change; the decisions sit in data/AI (5), IT (2), security (2) and software (1). Business functions outside technology and security contribute almost no confirmed AO or PE tasks in this sample.

## Q4. Few AI-titled postings state who the role reports to; where they do, it is mostly the data/AI or engineering line

Population: the 2,945 AI-titled (new-title, non-human-agent) postings; raw text joined to the analysis table by doc_id = P + ats + _ + board_id + _ + id (all 2,945 joined). Patterns: 'reports/reporting (directly/functionally) to/into ...' and 'part of / join the ... team|group|organization|department'. The phrase after the cue (up to 9 words, cut at clause breaks) is classified by keyword to the department whose keyword appears earliest; title words (manager, director, VP) do not name a department. One phrase per posting (the first). Keyword rules are in `q4.py`. Posting-level classes are in `q4-phrase-classes.csv` (no phrase text).

7.8% (6.9-8.8) of AI-titled postings name a reporting line (230 postings); 30.0% (28.4-31.7) use a 'part of the ... team' phrase.

| reports to (department of the named manager or leader) | postings | share of postings with a reporting phrase |
| --- | --- | --- |
| data and AI/ML | 64 | 27.8% (22.4-33.9) |
| no function named | 42 | 18.3% (13.8-23.8) |
| software engineering | 36 | 15.7% (11.5-20.9) |
| manufacturing/field | 17 | 7.4% (4.7-11.5) |
| sales | 11 | 4.8% (2.7-8.4) |
| IT and infrastructure | 10 | 4.3% (2.4-7.8) |
| finance and accounting | 8 | 3.5% (1.8-6.7) |
| security | 8 | 3.5% (1.8-6.7) |
| operations and supply chain | 7 | 3.0% (1.5-6.1) |
| product/design | 7 | 3.0% (1.5-6.1) |
| marketing | 5 | 2.2% (0.9-5.0) |
| executive/strategy | 5 | 2.2% (0.9-5.0) |
| legal and compliance | 5 | 2.2% (0.9-5.0) |
| customer service/support | 2 | 0.9% (0.2-3.1) |
| healthcare/clinical | 2 | 0.9% (0.2-3.1) |
| HR | 1 | 0.4% (0.1-2.4) |

By the function of the posting itself (function from the title as written, so counts differ from Q1, which strips the AI term):

| posting function | AI-titled postings | with a reports-to phrase | reports to own function |
| --- | --- | --- | --- |
| data and AI/ML | 994 | 7% (5-8) | 53% of 66 |
| software engineering | 588 | 5% (4-7) | 42% of 31 |
| IT and infrastructure | 378 | 9% (7-12) | 15% of 34 |
| manufacturing/field | 377 | 8% (6-11) | 26% of 31 |
| security | 152 | 11% (7-16) | 38% of 16 |
| sales | 126 | 6% (3-11) | 57% of 7 |
| marketing | 78 | 12% (6-20) | 56% of 9 |
| executive/strategy | 62 | 6% (3-15) | 0% of 4 |
| operations and supply chain | 53 | 15% (8-27) | 38% of 8 |
| other | 53 | 4% (1-13) | 0% of 2 |
| finance and accounting | 27 | 41% (25-59) | 27% of 11 |
| customer service/support | 25 | 12% (4-30) | 33% of 3 |
| legal and compliance | 15 | 13% (4-38) | 50% of 2 |
| HR | 13 | 31% (13-58) | 0% of 4 |
| healthcare/clinical | 4 | 50% (15-85) | 50% of 2 |

'Part of the ... team' phrases, by team named (generic phrases such as 'winning team' or an employer's name carry no function):

| team named | postings |
| --- | --- |
| no function named | 515 |
| data and AI/ML | 133 |
| software engineering | 83 |
| manufacturing/field | 22 |
| sales | 22 |
| product/design | 21 |
| IT and infrastructure | 17 |
| operations and supply chain | 16 |
| customer service/support | 15 |
| finance and accounting | 13 |
| marketing | 9 |
| security | 8 |
| HR | 4 |
| legal and compliance | 3 |
| executive/strategy | 2 |
| healthcare/clinical | 1 |

Of postings with a reporting line, 28% (22-34) report to a data/AI leader and 16% (12-21) to engineering; security (8), legal and compliance (5), HR (1) and finance (8) together account for about 10%. Postings in data/AI report to their own function about half the time; IT-, manufacturing- and finance-function postings report outside it more often than inside (small n; the function of the posting is itself a title-based label, and AI terms in the reporting phrase pull the classifier toward data/AI). The 'manufacturing/field' reporting lines include phrases such as 'Field AI Strategy', i.e. keyword noise in a small cell. Part-of-team phrases mostly name no function (58%) or a data/AI or engineering team.

Verbatim examples (one sentence, at most 40 words, names, emails and links removed; screened for personal names by a capitalised-bigram rule and read by me):

- (reports to; classified data and AI/ML; posting `Pworkday_analogdevices_R265809`) "Reporting to the Head of Enterprise AI , this leader will build and develop a high-performing team of product managers and establish a consistently high standard for product thinking, written requirements, prioritization, and partnership with science and engineering."
- (reports to; classified software engineering; posting `Pgreenhouse_databricks_8716720002`) "Reporting to the Head of Developer Relations, you'll collaborate with fellow Developer Advocates and program managers to create and execute a cohesive and impactful developer relations strategy."
- (reports to; classified security; posting `Pworkday_micron_JR108743`) "About Our Team The AI Security team is a newly established organization within Micron's Cyber Defense & Resilience (CDR) group, reporting directly to the Deputy CSO."
- (reports to; classified executive/strategy; posting `Pworkday_geaerospace_R5041026`) "Reporting to the CDIO of GE Aerospace and the GM of the Dowty, you won’t just build models—you’ll be a leader in a high-performing team to embed AI directly into our business."
- (reports to; classified sales; posting `Pgreenhouse_stripe_8212325`) "Reporting to the Chief Revenue Officer of AI, you will lead a team of Account Executives responsible for expanding Stripe's relationship with some of the most important AI companies in the world—across payments, billing, and beyond."
- (reports to; classified finance and accounting; posting `Pgreenhouse_databricks_8604577002`) "You will report to the Senior Director, Finance Data, AI & Strategy, and serve as the domain and technical anchor for a team that turns financial operations into trusted, well-governed data and reporting."
- (reports to; classified legal and compliance; posting `Pworkday_homedepot_Req194977`) "Direct Manager/Direct Reports: - Typically reports to Associate General Counsel or Assistant General Counsel - May be accountable for direct supervision of the work activities of others."
- (reports to; classified IT and infrastructure; posting `Pworkday_gilead_R0054109`) "This position reports to the Director, Commercial IT and is based in Tokyo, Japan."
- (reports to; classified marketing; posting `Pgreenhouse_databricks_8735590002`) "Reporting to the AVP of Marketing Technology, Data, and Growth, you will build and lead a net-new team, establishing this function from the ground up."
- (reports to; classified operations and supply chain; posting `Pworkday_henryschein_R134977`) "The Senior AI Transformation & Process Excellence Manager is a strategic business transformation leader will report to the Sr Director, Process Excellence."
- (reports to; classified HR; posting `Pworkday_masco_REQ54239`) "Reporting to the VP, Human Resources, this role partners with business leaders, sales, marketing, supply chain, and analytics functions to simplify manual processes, improve productivity, and support secure, scalable technology adoption."
- (part of team; classified data and AI/ML; posting `Pworkday_nvidia_JR2016032`) "Are you passionate about pushing the boundaries of AI at the intersection of the digital and physical worlds? Join our groundbreaking research team as we revolutionize the future of physical AI through groundbreaking generative models."
- (part of team; classified security; posting `Pworkday_danaher_R1317447`) "This position is within the Danaher Corporate Information Security team, reporting to the Sr Manager, Cyber Threat Engineering."
- (part of team; classified software engineering; posting `Pworkday_amgen_R-251304`) "Senior Business Analyst, AI Studio This Job offers a unique opportunity to join a fun, innovative engineering team within the AI & Data Science (AI&D) - organization."

## Q5. Security review sits in security and IT, AI governance in data/AI, guardrail and permission work in security, and service management in support and IT

Rate per 1,000 duty statements (305,533 statements from 25,220 postings), weighted by the posting's sampling weight; interval = percentile bootstrap over postings within sampling group (duties cluster in postings, so Wilson on statements would be too narrow). Function is the posting's function from the map, so the 'security' row is partly defined by 'security' in the title: its high security-review rate is partly built in.

Keyword families (case-insensitive, whole-word start, stems match; short acronyms matched in capitals only):

- **security review**: security review; security assessment; security audit; security testing; security risk; security posture; security architecture; security requirement; security control; security vulnerabilit; security incident; security standard; security polic; threat model; threat assessment; penetration test; pen test; vulnerabilit; secure code; secure design; code review for security; red team; incident response; AI security; AI red team; cybersecurity; information security; infosec; SOC 2; ISO 27001; NIST; data protection impact
- **ai governance**: AI governance; responsible AI; AI ethics; ethical AI; AI risk; model risk; AI polic; AI safety; AI compliance; EU AI Act; trustworthy AI; model governance; AI oversight; human oversight; human-in-the-loop; human in the loop; algorithmic bias; algorithmic fairness; bias testing; bias mitigation; model validation; AI standards; AI regulation; AI guideline; AI usage polic; AI audit; AI controls
- **guardrail permission**: guardrail; guard rail; permission; access control; role-based access; RBAC; least privilege; entitlement; approval workflow; policy enforcement; allowlist; allow list; access management; privileged access; access authorization; authorization polic; authorization model; authorization framework; access rights; access request; segregation of duties; identity and access; IAM; approval limit; approval authority; delegation of authority; usage polic
- **service management**: ITIL; service management; incident management; change control; change advisory; change request; service desk; ServiceNow; problem management; service level; SLA; service catalog; ticketing; CMDB; on-call; runbook; service request; release management; help desk; helpdesk; ITSM; problem ticket

All postings, weighted:

| function | duty statements | security review | ai governance | guardrail permission | service management |
| --- | --- | --- | --- | --- | --- |
| sales | 54912 | 2.8 (2.2-3.4) | 0.2 (0.0-0.6) | 0.5 (0.3-0.8) | 6.0 (5.0-7.1) |
| customer service/support | 8755 | 4.1 (2.6-5.9) | 0.3 (0.0-0.8) | 2.3 (1.3-3.3) | 30.0 (24.6-35.5) |
| marketing | 9031 | 5.0 (3.3-6.9) | 0.6 (0.2-1.1) | 2.7 (1.5-4.1) | 3.1 (1.8-4.5) |
| finance and accounting | 18222 | 1.8 (0.9-2.9) | 1.2 (0.4-2.1) | 1.1 (0.6-1.7) | 6.3 (5.1-7.6) |
| HR | 4987 | 2.6 (0.9-4.7) | 0.6 (0.1-1.2) | 2.8 (1.3-4.7) | 7.0 (4.2-10.1) |
| legal and compliance | 5048 | 4.7 (2.6-7.4) | 2.4 (1.1-4.1) | 3.6 (1.7-5.9) | 5.0 (3.1-7.1) |
| IT and infrastructure | 16631 | 20.3 (17.0-23.9) | 2.9 (2.0-3.9) | 10.8 (8.6-13.2) | 29.6 (25.0-34.4) |
| security | 8612 | 172.4 (155.6-190.1) | 3.8 (2.6-5.3) | 40.5 (31.3-50.5) | 16.5 (12.5-21.3) |
| software engineering | 24048 | 16.0 (13.9-18.2) | 2.0 (1.5-2.7) | 7.9 (6.5-9.4) | 19.4 (16.5-22.2) |
| data and AI/ML | 16726 | 9.8 (7.8-12.0) | 10.5 (8.3-12.9) | 10.8 (8.7-12.9) | 7.0 (5.1-9.1) |
| operations and supply chain | 36139 | 3.1 (2.4-3.9) | 0.5 (0.3-0.8) | 1.2 (0.8-1.7) | 6.2 (5.3-7.2) |
| manufacturing/field | 57697 | 2.9 (2.4-3.5) | 0.2 (0.1-0.3) | 0.6 (0.4-0.9) | 5.2 (4.5-6.0) |
| healthcare/clinical | 14002 | 0.1 (0.0-0.4) | 0.0 (0.0-0.0) | 0.9 (0.4-1.4) | 4.1 (3.1-5.3) |
| executive/strategy | 6836 | 6.5 (3.5-9.9) | 2.2 (1.2-3.5) | 2.9 (1.7-4.3) | 7.2 (4.7-10.1) |
| other | 22509 | 3.2 (2.2-4.5) | 0.1 (0.0-0.2) | 1.3 (0.7-1.9) | 4.7 (3.6-5.9) |
| ALL | 304155 | 9.0 (8.4-9.7) | 1.0 (0.9-1.1) | 3.2 (2.9-3.6) | 8.6 (8.1-9.1) |

AI-titled postings only (unweighted; small cells are wide):

| function | duty statements | security review | ai governance | guardrail permission | service management |
| --- | --- | --- | --- | --- | --- |
| sales | 1231 | 4.1 (0.0-9.4) | 0.0 (0.0-0.0) | 5.7 (1.8-10.3) | 4.1 (0.0-13.2) |
| customer service/support | 257 | 3.9 (0.0-13.2) | 11.7 (0.0-30.1) | 7.8 (0.0-25.8) | 50.6 (19.2-84.2) |
| marketing | 849 | 5.9 (1.1-13.0) | 9.4 (2.8-17.0) | 9.4 (1.1-21.0) | 2.4 (0.0-6.2) |
| finance and accounting | 341 | 8.8 (0.0-20.9) | 64.5 (19.4-115.1) | 5.9 (0.0-14.6) | 5.9 (0.0-17.3) |
| HR | 185 | 0.0 (0.0-0.0) | 16.2 (0.0-31.2) | 5.4 (0.0-20.6) | 5.4 (0.0-18.5) |
| legal and compliance | 177 | 84.7 (6.4-183.7) | 90.4 (17.5-207.4) | 11.3 (0.0-29.4) | 11.3 (0.0-28.8) |
| IT and infrastructure | 4486 | 18.7 (14.1-23.3) | 18.3 (13.6-23.1) | 14.0 (10.3-18.2) | 14.5 (10.5-18.7) |
| security | 1934 | 265.8 (223.5-306.6) | 40.3 (27.3-56.0) | 69.3 (50.6-90.3) | 12.9 (7.7-18.7) |
| software engineering | 6098 | 15.1 (11.7-18.7) | 12.1 (8.9-15.6) | 16.9 (13.2-20.8) | 20.8 (16.3-26.0) |
| data and AI/ML | 10468 | 14.5 (11.7-17.3) | 22.3 (18.7-26.1) | 17.7 (14.8-20.6) | 10.2 (7.9-12.9) |
| operations and supply chain | 666 | 15.0 (1.9-33.1) | 58.6 (17.3-103.8) | 13.5 (3.7-25.8) | 9.0 (1.3-19.2) |
| manufacturing/field | 4530 | 7.7 (5.2-10.4) | 0.2 (0.0-0.7) | 1.1 (0.2-2.4) | 11.5 (8.3-15.0) |
| healthcare/clinical | 64 | 0.0 (0.0-0.0) | 15.6 (0.0-71.4) | 0.0 (0.0-0.0) | 15.6 (0.0-64.5) |
| executive/strategy | 886 | 10.2 (2.7-20.2) | 36.1 (19.9-51.7) | 11.3 (4.4-20.3) | 4.5 (0.0-11.3) |
| other | 604 | 0.0 (0.0-0.0) | 0.0 (0.0-0.0) | 0.0 (0.0-0.0) | 0.0 (0.0-0.0) |
| ALL | 32776 | 28.2 (24.3-32.2) | 18.1 (15.9-20.3) | 16.2 (14.3-18.2) | 12.6 (11.0-14.1) |

Security review: 172 per 1,000 duties in security postings against 9 overall; IT (20), software (16) and data/AI (10) follow. AI governance is the clearest data/AI signal (10.5 per 1,000, against 1.0 overall), with security (3.8) and IT (2.9) next; in AI-titled postings the rate is 18 per 1,000 and the legal, finance and operations cells are high but rest on 15 to 53 postings. Guardrail and permission duties peak in security (41), with IT (11) and data/AI (11) at about a quarter of that. Service management is the one family that leaves technology: customer service/support (30) matches IT (30), then software (19) and security (17); business functions are 3 to 7 per 1,000. The rates for governance, guardrail and permission duties outside technology and security are close to zero in the whole posting set.

## Speech cross-check (I6, pooled spans)

From `I6-tables.csv` (code by function). These are pooled spans from 34 transcripts, one to seven transcripts per function, extraction recall about 0.5; the function is the speaker's, not a posting's, and the I6 function list differs from the posting map. Totals reflect how many and how long the transcripts are; they are not rates.

| function | AO | PE | PV | OT | AO+PE share of spans |
| --- | --- | --- | --- | --- | --- |
| HR and people ops | 5 | 3 | 0 | 32 | 20% |
| IT, identity and security | 11 | 5 | 0 | 83 | 16% |
| customer support/CX | 26 | 1 | 1 | 54 | 33% |
| engineering and platform | 10 | 4 | 0 | 79 | 15% |
| finance | 17 | 2 | 0 | 103 | 16% |
| general operations leadership (COO) | 4 | 2 | 0 | 11 | 35% |
| legal and legal ops | 1 | 0 | 0 | 28 | 3% |
| procurement | 3 | 2 | 1 | 110 | 4% |
| risk and compliance | 4 | 4 | 0 | 41 | 16% |
| sales, RevOps and go-to-market | 89 | 1 | 0 | 126 | 42% |

Agent-operations spans are dense in sales/RevOps/go-to-market (89 of 170) and customer support/CX (26), finance (17) and IT/identity/security (11); setting-limits spans are few everywhere (24 in all: IT/security 5, engineering 4, risk and compliance 4, HR 3). Postings put running and limit-setting duties mainly in data/AI, software and security, while speakers describing their own work report running agents mostly in go-to-market and support. The two sources do not measure the same thing (posting duties versus self-described practice), so the difference is a contrast, not a contradiction.

## Limits

- Function comes from title keywords and model-assigned O*NET codes; the O*NET major group is about 83% right (deviation 18) and my 60-posting check of the final 15-class map found 90% fully right. Small functions (HR, legal, support, healthcare, finance) have few postings or tasks in the AI and agent subsets, so their cells are wide or empty.
- Q1 and Q4 define 'AI-titled' by title terms, so they measure titles, not work; 'automation' titles in manufacturing/field are mostly industrial automation. Strip-and-remap removes the circularity for Q1 but not for Q2 to Q5, where function is assigned from the title as written.
- Q2 applies group-level confirmation rates to all functions and treats tasks within a posting as independent; the lexical screen misses postings that describe agent duties without the listed terms. Function-level confirmation rates are shown but rest on small counts.
- Q3 counts a stratified task sample; the sample was drawn before function was known, so function counts are not controlled. RD never occurs in the final codes.
- Q4 finds a reporting line in under 10% of AI-titled postings; those are not a random subset (named leaders appear mostly in senior or new-team roles). Department classification is keyword-based and uses the earliest keyword, so AI words in a leader's title pull the class toward data/AI; no precision check against hand coding was run.
- Q5 keyword families are lexical: 'permission', 'entitlement' and 'on-call' have non-IT senses, and 'service level' and 'SLA' occur in commercial contracts. No precision check was run beyond reading the most frequent matches, which led me to drop bare 'authorization', 'escalation', 'root cause analysis', 'change management' and 'risk assessment'.
- Sampling: employers are Fortune 500 and VC-software boards, US and non-US pooled; weights correct for the rest20 sampling only, not for employer selection.
- No personal data is stored: Q4 tables hold department classes only, and the quoted examples were scrubbed of emails, links and phone numbers and screened for names.
