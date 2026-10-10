# Report content plan (rerun, 10 October 2026)

This plan feeds the final report (memo template `template-v2.html`, protocolvision.org style: light, Lora,
hairline figures, finding-lede headings). The user asked that the items below go in. Every item must trace to
committed files. Items marked **synthesis** are the orchestrator's reading across instruments: the red team
challenges them, and they go in only if they survive.

## Lead findings
From `results/rerun-2026-10-10/findings-corpus-b.md` (F-1 to F-8), updated by the comparison and red team.

## The sample (method walkthrough figure plus one short paragraph)
- Crawl: 118,526 postings from 218 boards. Coverage is 37% of the Fortune 500 and 72% of the VC software
  firms; big tech and most utilities are not reachable (`corpus-b/coverage.md`).
- Selection: 25,512 postings (831 study occupations, 2,790 AI-type titles, a 20% sample of the rest).
  Extraction: about 305,000 duty statements (precision 0.97, recall 0.89).
- Filings: 1,167 filings and 2,216 passages, 64% from vendors.
- Speech: 38 recordings and 862 coded statements (descriptive; minimum counts).
- Rule texts: 111 provisions from 19 texts. Vendors: 30 roles and 21 certifications.
- The funnel and walkthrough animation use these real counts (design-notes backlog).

## Clustering outputs (figure: stable vs unstable bundles)
- 50,675 statements clustered (300 per employer); 114 clusters; 11 stable, of which 3 are language
  artefacts, leaving 8 stable work bundles (`clusters/leaf/clusters.csv` and `labels.csv`).
- Table of the 8 stable bundles with function and employer counts. "Assess AI systems for security risk" is
  the only stable AI bundle; coders put its rule-design share at 0.30–0.40.
- Table of the large but unstable AI bundles: use cases (207 statements, 73 employers), agentic workflows
  (78, 43), AI governance (75, 38), ML model monitoring (43, 28). The figure shows them as dashed or hatched
  ("forming, not settled").

## Archetypes (synthesis; for red-team challenge)
Six recurring figures around AI agents, ordered by how settled they are. Each needs evidence lines and
corpus ids in the report:
1. **AI security reviewer** (most settled): stable cluster 111, rule design 30–40%, in the security
   function (I2, I3 examples: Merck, IQVIA).
2. **Embedded agent operator** (most common in speech): existing staff who take on agent running inside
   their function (I6: 7 of 11 staffing speakers; M072 quote).
3. **AI or agent builder** (fast-growing, unsettled): AI and automation engineer titles. Asks for AI
   experience in 27 of 30; named AI teams (I1, I3; unstable cluster 112).
4. **Governance council member** (in speech, rare in filings): councils, guilds, central teams (I6: 5 of 34;
   filings 9 of 2,216 passages).
5. **Business sponsor** (vendor-defined): Microsoft Entra sponsors and owners (2025-11-05), the ServiceNow
   AI Steward (I5).
6. **Designated overseer** (law-defined, from 2027): EU AI Act Art 26(2), Colorado SB26-189. No change owner
   is named (I4).

## What held from round one (one compact section; collapses to a line if nothing changed)
From the phase 2 verification files:
- Loop analysis: 122 of 127 claims confirmed; the analysis script reproduces round one's numbers exactly.
  Kappa recomputes at 0.95.
- Loop red team: 61 of 70 confirmed; 9 small corrections.
- Industry findings and red team: 38 of 70 confirmed, 19 corrected, 10 not found, 3 unverifiable. The
  weakest part of round one: trading-rule bindingness overstated (guidance shown as rules); robustness
  mis-stated (trading in fact beats the grid in about 91% of weightings); the Citi role misread. The analogue
  conclusion (trading nearest) survives, with weaker 'binding rule' support.
- Random 150 across all files: pending (error rate with interval).
- Then the comparison: replicated, revised, round one only.

## DevOps question (one honest paragraph, not a headline)
The pattern verdict is unreliable by rule (power about 5%). The head-to-head leans DevOps on speech
(existing staff, coordination) while postings lean the other way (scarce AI skill, AI teams). This tension
becomes the lead question of the field plan.
