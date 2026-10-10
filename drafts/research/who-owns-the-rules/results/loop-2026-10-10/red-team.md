# Red team: loop 2026-10-10

## 1. The activities do not cluster, or cluster only inside existing roles

- **PE fails the pre-registered test.** C7 holds 46% of the 13 agreed PE records (60% needed), and only 1 of 2 eligible iterations reaches 60% (3 needed). The "partly concentrated" verdict in `analysis.md` is not in section 7. Under the design, PE is neither clustered nor dispersed. It is indeterminate.
- **Nothing is stable.** The adjusted Rand index is 0.59 for 3→4 and 0.56 for 2→3, and section 7 says to report unstable results as unstable. PE's top cluster moves every round:
  - iteration 3: split between C6 and C7, 38% each;
  - iteration 4: C5 at 60%;
  - iteration 5: C7 at 46%.

  The 60% held only until regulation (S3) entered. S3 pulled R8958, R4263 and R5100 into C12 and C10.
- **The wider count disperses.** With secondary codes, 40 PE records spread over eight clusters, and the top one holds 32%. That is below the "dispersed" line.
- **The rule-design cluster is mostly existing admin work.** C7's records describe IAM and platform consoles: Okta (R7070, R8529, R1437), Entra (R6638, R9271), Workday (R6186), Gemini (R9237, R1002), Power Platform (R2839) and M365 (R3363).
- **Rule work outside C7 stays with incumbent function owners.** Examples: legal playbooks (R6915), buyers setting negotiation bounds (R9692), engineering access gates (R4556, R3469), supervisory procedures in regulated firms (R8958, R4263), and law-firm AI policy (R5100).
- **PV and PE cannot co-cluster.** With 0 PV records, the co-cluster test cannot be run. Nothing here shows that finding rules and designing rules belong to one role.

## 2. The clusters reflect the question, the definitions and the sources

- **Clusters follow the type of document.**
  - C12 is 24/24 regulation, and 14 of those records come from one document (D219, FINRA *as summarized by SIA Partners*).
  - C4 is 13/13 postings.
  - C13 is 26/29 research.
  - C7 is 15/17 vendor documentation.
  - C10 takes 10 of its 25 records from one ABA opinion (D314), and C11 takes 11 of 28 from the EU AI Act (D274).

  "Same document" counts as bundling evidence. A regulation's duty list, an admin guide or a posting's bullets is therefore role-shaped by construction. C1's own bundling evidence says "Five postings carry most of this bundle".
- **Rule design entered with vendor documentation.** Strata entered in the order S4, S1, S5, S2, S3. Agreed PE records went from 0 (after S4) to 1 (after S1, R9635) to 8 once S5 entered. The "admitting agents" cluster first appears at that point, in iteration 3. Seven of the 13 PE records are from S5. Without vendor docs, the central rule-design cluster would not exist.
- **The vendor share goes beyond S5.** Many S2 "practitioner accounts" are vendor marketing or customer stories:
  - Anthropic: D513, D745, D356
  - OpenAI: D381, D706, D681
  - Microsoft: D552, D574
  - Salesforce: D397
  - Ramp: D192, D161

  A large part of S4 is also vendor research: D711, D869 and D973, plus Microsoft-affiliated D968, D388 and D296.
- **The framing pushes rule work into AO.** Every PE candidate touches an agent, and AO claims anything "about the agent". 27 records got PE only as a secondary code, including escalation and handoff configuration (R5876, R7901, R9416, R9678). The line is inconsistent: R9635 (what the AI must never answer, when it escalates) is primary PE, while R9678 (escalation paths) is primary AO.
- **Postings were selected on the outcome.** S1 searched for postings mentioning agents, so C1's "existing title" (AI Agent Operations Specialist) partly reflects the search terms.
- **A quarter of the pool is not human work.** In 73 of 298 records the performer is an agent or software (for example R7560, R1762, R1324). In 8 records no performer is named (R9045, R7923). These records cannot show how human roles bundle, yet they shape C8, C9 and C14.

## 3. The strongest-looking findings rest on weak records

- **All 298 records are grade S.** No source was opened.
- **None of the 13 agreed PE records observes a person in a firm doing the work.**
  - 7 are vendor statements of what a product assumes (R2839, R9271, R9237, R6186, R1437, R1002, R6915). R6915 is the vendor's own services team.
  - 3 are normative "should" statements: R8958 and R4263 come through a consultancy summary, and R5100 is the ABA opinion.
  - R9635 is one posting found through an aggregator (zapply.jobs).
  - R4556 is a press report of Amazon's statement after an outage.
  - R9692 is a 2023 trade-blog summary of an HBR chatbot case.
- **"Business sponsor of an agent (new)" rests on one Microsoft Entra page.** Both supporting records (R8345, R9271) come from D446, and the role is a product field, not an observed job. The "existing" title AI steward (R4736) is a ServiceNow product persona.
- **C8, "Writing the policy an agent approves against", contains no record of anyone writing policy.**
  - Its secondary-PE records are agents applying policy (R7560, R6656, R2791). The coders' notes say "executing, not designing".
  - The rest are humans deciding cases (R8449, R1491, R1155).
  - Only R9692 sets bounds.

  The clusterer concedes that "no record names who writes the policy the agent reads". C9's "lead who sets matching and tolerance rules" likewise has no supporting record: in R1762 the agent applies the rules.
- **C1, the top "distinct by 2030" candidate, rests on aggregator postings.** It takes 20 of its 29 records from about five postings found through zapply.jobs, ZeroG Talent, a16z Jobs, CareerBuilder (through a staffing firm) and an Indeed search page.
- **The coders were not independent in judgment.** Kappa is 0.95, but 85 of 298 notes are word-for-word identical. Neither coder ever saw a positive PV or RD case, so the kappa says nothing about those codes.

## 4. The opposite case: the design could hardly find PV or RD

- **PV requires a stated purpose** ("in order to infer the rule"), and summaries rarely give one. The nearest record, R1848 (a weekly review for gaps and avoidable escalations), is coded AO.
- **The best PV material was flattened.**
  - D616: a support bot (Cursor) invented a policy, which is the definition's "agents improvise" case. It was recorded as "answer support emails" (R2388, OT).
  - The Replit postmortem (R8231) and "the knowledge manager was born" (R8233) went to AO.
  - Finding shadow agents (R8529) went to AO.
- **The best RD document was flattened too.** Ramp's "It's Time to Rewrite Your Expense Policy for AI: Insights from 10,000 Expense Policies" (D161) yielded one record: agents "review expenses" (R2791). Cross-functional decisions appear only as company actions or reviews coded OT (R2505, R9974, R2799).
- **The design limits made PV and RD unlikely to surface:**
  - activities capped at 15 words in the source's own terms;
  - no stratum has a word for rule-finding;
  - primary-only counting;
  - no interviews, full postmortems or audit findings;
  - only three ethnographic sources (D730, D887, D895).

  "Absent" means absent from summary-grade public text, as section 9 predicted. It does not mean the work doesn't happen.

## What survives, and with what confidence

| Finding | Confidence |
| --- | --- |
| PV and RD are essentially undocumented in public, summary-grade sources about agents | High about the corpus, low about work |
| PE does not meet "clusters together", and the clustering is unstable | High |
| PV–PE co-clustering is untested, not refuted | High |
| Vendors attach rule design to admitting and permissioning agents in existing admin consoles. The inclusive count spreads it across functions | Medium for vendor assumptions, low for staffing |
| AO is dispersed and sits inside functions (top cluster 29%) | Medium |
| A new "business sponsor" or "approval-policy owner" role exists | Low |

## What the next run should change

1. **Sources.** At least half the records graded P or R, from opened documents. Exclude aggregator pages and sources from before 2024. Sample postings at random within occupations, not by searching for "agent".
2. **A rule-change stratum.** Full postmortems, audit findings and enforcement actions, change and policy logs, policy revisions (like D161), and practitioner forums.
3. **Interviews or ethnography for PV and RD.** Even ten operations leads would test whether the absence is real.
4. **Bundling evidence.**
   - Do not treat co-occurrence in the same normative document as bundling.
   - Cap the number of records per document.
   - Cluster within each stratum as well as across strata.
   - Pre-register a stratum-purity threshold above which a cluster is reported as an artefact of the source type.
5. **Separate clustering for agent-performed and empty-performer records.**
6. **Codes.**
   - Pre-register a multi-label rule.
   - Settle the AO/PE boundary for escalation, handoff and guardrails.
   - Replace PV's purpose clause with observable proxies, such as reviewing exceptions or overrides that lead to a rule change.
   - Seed known PV and RD cases to measure coder sensitivity.
   - Use a different model or a human as the second coder.
7. **Stability.** Repeat the clusterer on the same pool to separate clusterer noise from the effect of adding strata. Define "partly concentrated" in advance or drop it.
