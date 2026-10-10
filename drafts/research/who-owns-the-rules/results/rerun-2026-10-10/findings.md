# Final findings: who owns the rules when agents join the business

Protocols for Business · rerun of 10 October 2026 · RERUN.md phase 4, step 1. (Written by a fresh Opus agent; the harness refused its write, so the orchestrator saved the text unchanged.)

These findings start from the blind findings (`findings-corpus-b.md`). They take in the red team (`red-team.md`), the comparison with round one (`comparison.md`), the phase 2 verification files and their review, and deviations 19–26. Every verdict is re-derived from the pre-registered refutation conditions:
- research design §5;
- loop v2 §4;
- triangulation design §2 and the A.4 reading rule.

Paths are relative to `results/rerun-2026-10-10/` unless they name a design file.

**Corrected inputs used throughout:**
- **I1 (deviation 26).** 155 "agentic" titles were regrouped as new titles, so there are now 2,945 new-title postings. The two-phase ratio is 0.86 (0.63–1.15) against all new-title postings and 1.49 (0.97–2.30) against new-title postings with a confirmed duty. The red-team sensitivity range against all new titles is 0.54–1.27 (`instruments/I1.md`).
- **I6, timestamped speech only.** 771 spans: OT 600, AO 150, PE 21, PV 1, RD 0. The 91 spans from untimestamped transcript pages (M041, M053, M054, M067) are reported separately, as the log's rule requires (`log.md`; deviation 26).

All speech results are descriptive only, because H-cal was refuted (`calibration.md`). Speech counts are lower bounds, because extraction recall is about 0.5 (`instruments/I6.md`).

---

## 1. Findings

### Finding 1. Finding unwritten rules (PV) and deciding rule changes across functions (RD) are nearly absent from postings and speech. Setting what agents may do (PE) is a real minority of agent duties in postings. Running agents dominates what practitioners say.

**Evidence**
- **Postings, agent-related tasks.** Phase 2 coded 600 flagged tasks. Final codes (agreed codes plus blind adjudication) are AO 88, PE 33, PV 2 and RD 0. PE is therefore about 27% of agent-related codes (`coding/phase2-*.csv`; recounted for this file).
- **Postings, real records.** 300 records were coded:
  - coder A: PE 2, PV 1, RD 0;
  - coder B: PE 6, PV 4, RD 0.

  A blind Opus check found rule work in 3 of 40 records and agreed with each coder on 39 of 40 (`coding/scores.md`; `review/coding-real-check.md`). These records are mostly generic non-AI tasks, so this figure is a base rate, not a share of agent work.
- **Speech (timestamped, 771 spans).** AO 150, PE 21, PV 1, RD 0.
  - The one PV span is about a budget overrun: "I have a couple of associates … that have exceeded their replic budget in only two weeks" (M016, 2026-07-27).
  - Before adjudication, each coder coded RD on 3 spans. On M072_c07:1 the adjudicator replaced an RD that both coders had given. So the RD figure reads "0 after adjudication" (`coding/speech-*.csv`).
- **The coders can see these codes.** Seed recall is PV 0.95, PE 1.00 and RD 0.94–1.00, with Wilson lower bounds of 0.72 or more (`coding/scores.md`). Seeds are cleaner than real text (deviation 8), so this is an upper bound on recall.
- **No speech span describes reviewing exceptions or deciding a rule change across functions.** The nearest cases are:
  - "We changed the guard rails" (M021, 2025-09-19; the functions involved are not stated);
  - "I had to modify a bit our compliance approval process for new tools" (M065, 2025-10-28).
- **Clearest rule-design posting line:** "turn goals into … rules, constraints … that AI systems can execute" (R0397, 2026 snapshot).

**Confidence.** High that PV and RD are near-absent from the public record. Medium for the PE share, because the phase 2 kappa before adjudication was 0.64 for PE. Low to medium for the speech balance: recall is about 0.5, and the consensus extraction set was chosen after scoring (deviation 13).

**What changed since round one: replicated, narrowed.** Round one's "rule work is rare; PV and RD do not appear" holds on an independent corpus whose coders were shown by seeded cases to detect PV and RD (comparison claims 1–2). Two parts are revised:
- "Running agents dominates" holds for speech. In postings, AO outnumbers PE only about 2.5 to 1.
- PV and RD are near-absent, not absent.

Neither source can show rule changes that are agreed informally. This finding describes the written and spoken record, not the work itself.

### Finding 2. In this crawl, existing-title postings with a confirmed agent duty are about as numerous as AI- or automation-titled postings, and most of them are technical jobs. Nothing approaches the 3-to-1 margin the DevOps pattern predicts.

**Evidence** (`instruments/I1.md`, two-phase section; deviations 24 and 26)
- **Estimated postings with a confirmed agent duty:**
  - existing postings: about 2,529 (S1 189, rest20 2,340);
  - new-title postings: 1,701 (1,471–1,906) of 2,945.
- **Ratio against all new-title postings: 0.86 (0.63–1.15).** This is the comparison the refutation rule names.
  - Against new-title postings with a confirmed duty, the ratio is 1.49 (0.97–2.30).
  - Across the red team's assumptions, the ratio against all new titles runs from 0.54 to 1.27. Those assumptions are tasks confirming together within a posting, or coder A's or coder B's codes alone (`red-team.md`, problem 2).
- **The ten study occupations (S1) alone:** 189 against 2,945, a ratio of about 0.06. S1 is one of deviation 21's two definitions of "existing occupations".
- **Who the existing postings are.** About 53% of the existing-posting estimate sits in O*NET major groups 15 (computer and mathematical) and 17 (engineering). The major-group mapping is about 83% accurate (`red-team.md`; deviation 18). So "absorption" here is mostly software and engineering staff doing AI work. It is not business staff running agents.
- **The pre-registered lexical flag gives 5.32.** Its precision against the coders is only 0.05 and 0.14, so that figure counts mentions of the terms, not duties (deviation 24).
- **New AI titles are widespread but thin.**
  - At least 161 of 198 employers (81%) have one.
  - They are about 2.5% of postings, sampling-weighted, before the regrouping of the 155 agentic titles (about 2.7% after).
  - They are 6.6% of postings at venture-backed software firms and 2.3% in the Fortune 500.
- **Speech (single-coded per speaker, timestamped speakers).** Of the 10 speakers who describe staffing, 6 gave existing staff new duties, 3 hired and 1 did both. Example: "she spends 20% of her time managing the agents, orchestrating the agents." (M072, 2026-01-01).

**Confidence: low to medium.** The interval spans parity. The estimate rests on two unregistered choices: confirmation within a posting is treated as independent, and adjudication chose between two coders with opposite biases. The screen's recall is 0.25–0.43, so duties that avoid the term list are missed in both groups.

**What changed since round one: new.** Round one had no ratio. Round one's prediction that "most firms absorb" (comparison claim 9) is revised. In this crawl, absorption and new titles are about even.

### Finding 3. No stable posting cluster joins rule work with agent operations across functions. The one AI cluster that passed the stability test, AI security review (cluster 111), passed only because of one posting.

**Evidence**
- **The clustering found 8 stable work clusters.** Holdout ARI was 0.827 against a noise baseline of 0.964 (`clusters/leaf/stability.md`). This used leaf selection, a post-hoc change made after the pre-registered method found 0 clusters (deviation 19).
- **Cluster 111, "Assess AI systems for security risk," is the only AI cluster among them.**
  - Size: 35 discovery tasks from 19 postings at 18 employers.
  - Coders put its PE share at 0.30 (A) and 0.40 (B), and its AO share at 0.07–0.10 (`instruments/I2.md`).
  - **Cluster 111 rests on one posting.** In the holdout half, 24 of its 53 tasks come from Thrivent Financial REQ-47040, "Principal Engineer - AI Security". Without that posting, the cluster fails both found criteria: 29 members against the 30 needed, and Jaccard 0.432 against the 0.5 needed (`red-team.md`, problem 1).
- **The other AI clusters did not replicate in the holdout half** (best Jaccard 0.17–0.33):
  - 110, AI governance and compliance;
  - 112, agentic workflows;
  - 113, AI use cases.

  "Did not replicate" means unstable. It does not mean these bundles are forming.
- **AI-titled postings combine business and technical clusters no more often than other postings** (`instruments/I1.md`):
  - found clusters: 0.6% against 0.3%;
  - all clusters: 8.2% against 8.4%.
- **Where AI rule work appears in postings, it sits in security and governance roles** (`instruments/I3.md`, 2026 snapshot):
  - "Support security architecture reviews and risk assessments for AI systems, AI applications, AI agents, and AI-enabled platforms across the enterprise." (#12, Merck);
  - IQVIA's AI Security Architect "reports to the Security Architecture leader" (#3);
  - JLL's role reports to a "Regional Business Governance & Compliance Director" (#19), outside security.

**Confidence: low.** About 65% of tasks are noise, and found clusters cover about 3.5% of the task pool. The data is English-only (deviation 20) and dominated by regulated-finance employers. The holdout ARI sits 0.137 below the noise baseline.

**What changed since round one: revised.** The comparison called this a revision: rule design "bundles once, inside security". With cluster 111 resting on one posting, the rerun comes closer to round one's own result, that PE does not cluster stably. What is new is where AI rule work shows up in postings: security and governance review. Round one's five function homes do not appear (comparison claims 3–4).

### Finding 4. The binding AI texts read require deployers to assign people who oversee AI, but none of their 4 provisions on changes names who decides them. Named change owners appear in trading texts and in AI labs' own policies.

**Evidence** (`instruments/I4.md`; `review/I4-review.md`)
- **111 provisions from 19 texts.** 32 provisions regulate how rules or limits change, and 15 of those name an owner:
  - 12 in trading and markets;
  - 3 in lab self-policies;
  - 0 of 4 in AI law and standards.
- **Two qualifications:**
  - 8 of the 12 trading change owners come from supervisory guidance or expectations, not binding rules: 5 from FCA reviews and 3 from PRA SS5/18.
  - AI Act Art 17(1)(m) was coded "no" while a similar PRA provision was coded "yes". Under the PRA reading, AI law would be 1 of 4.
- **EU AI Act Art 26(2)** (C9b1da45a): "Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority". The Omnibus (Reg. 2026/1744) moves Annex III high-risk obligations to 2 December 2027, and Annex I systems to 2 August 2028.
- **Colorado SB26-189** (CO-SB26-189-act), effective 1 January 2027: "individual designated by the deployer who has authority to approve, modify, or override a consequential decision".
- **PRA SS5/18** (Cef3dde3f, guidance): "each algorithm to have assigned owners, who are accountable for the algorithm's use and performance".

**Confidence.** High on what the texts say: every quote was checked by script. Medium on the contrast, because the AI-law denominator is 4, one coder did the coding, and the text list is fixed. California SB 53, ISO 42001 and bank model-risk guidance were not read.

**What changed since round one: revised.** Round one carried trading's change-control template across to agents. Verification and I4 narrow this:
- AI law produces a designated overseer, not a change owner.
- In trading, only 15c3-5 CEO certification, Series 57 registration and the RTS 6 designated person bind (comparison claims 14, 16).

The blind findings' "practice leads law" timing claim is dropped. It compared the first speech record, in a frame that starts in 2024, with laws' effective dates. Dated by adoption, the binding texts are not shown to come later.

### Finding 5. Agent language in 10-Ks went from almost none to 6.75% of filers in 2026 (18% of the frame's filers). Passages are mostly product descriptions because vendors supply most of them.

**Evidence**
- **Share of 10-K filers using one of the six agent phrases** (`corpus-b/filings-denominator.csv`):
  - all filers: 0.05% (2022), 0.06% (2023), 0.12% (2024), 1.71% (2025), 6.75% (2026, through 10 October);
  - frame employers: 0%, 0%, 0.21%, 3.8%, 18.0% (77 of 428).
- **Content of 2,216 passages** (consensus codes):
  - product 1,342, own use 369, controls 109;
  - vendors supply 64% of passages (10-K and 10-Q; 60% in 10-Ks alone).
- **Non-vendor filers mention their own use about as often as products.** Counted by company, adopters have own use 126 and product 93 (`corpus-b/passage-coding.md`, Haiku codes by filer type; own-use precision 0.76).
- **No 10-K in Item 9A.** None of 539 10-Ks with a detectable Item 9A uses an agent phrase in that item.

**Confidence.** High for the counts, which are phrase hits on EDGAR full text. Medium for the content codes. 2026 is a partial year, though most 10-Ks are filed by March. "Digital workers" and "digital labor" were not checked for non-AI uses.

**What changed since round one: new.**

### Finding 6. Governance and agent-scoped certifications (2024–25) and vendor agent roles (2025) come before binding deployer rules (2027). Vendors split business accountability from technical control and relabel their agent products within about three years.

**Evidence** (`instruments/I5.md`, `I5c.md`, `I4.md`)
- **Dated order:**
  - open agent tooling, third-earliest: 2023-08-15 (does not resolve to a stored source; the counted repos are monitoring tools, and two lack an OSI licence);
  - AI-governance certification: 2024 (IAPP AIGP; the stored source gives the year only);
  - first agent-scoped certification: 2025-03-03 (Agentforce Specialist);
  - vendor agent roles: Microsoft Entra, November 2025 (listed as new at Ignite 2025);
  - binding deployer rule: 2027-01-01 (Colorado).
- **Vendors split business accountability from technical control.** "Sponsors provide business accountability for agents, making lifecycle decisions without technical administrative access." (ms-entra-owners; new at Microsoft Ignite, November 2025).
- **Vendors relabel.** Einstein Copilot became Agentforce in September 2024, and Agentspace became Gemini Enterprise on 2025-10-09. Both feature coders code N24 (vendor relabelling) yes (`pattern-match/result.md`).

**Confidence: low to medium.**
- The tooling search departed from A.2: it searched by function, did not check licences and kept no search log. This is now recorded in deviation 26.
- The first community date is missing.
- The first speech record (2024-11-28) falls after the first governance certification, and the speech frame starts in 2024. So the place of practice in the order, and with it the D3 order, cannot be tested.
- This order (tooling, then certification, then vendor roles, then law) is common to enterprise software. It does not tell DevOps apart from other patterns.

**What changed since round one: new**, with one revision. Round one's "business sponsor" and "AI steward" stand as vendor product roles, not as observed jobs (comparison claim 7).

### Finding 7. Some speakers describe AI governance councils, guilds or centres of excellence. No such body is shown to decide agent rules, and these bodies are rare in coded speech spans and in filings.

**Evidence**
- **Speakers (single-coded).** 5 of 34 describe a central body between functions, and 5 describe a team within one function (`instruments/I6.md`). None of the 5 central-body speakers comes from the untimestamped pages. Examples:
  - "I'm on the AI Governance Council and we've just had our second meeting." (M010, 2025-07-22);
  - "we have a strat and gov team that sit in the middle" (M024, 2025-06-30; a general IT strategy-and-governance team, not an AI body);
  - "we decided to create like an AI guild" (M065, 2025-10-28; an engineering best-practice guild).
- **Spans.** About 8 of 862 coded spans mention such a body, about 1%. All of them are in timestamped speech, so the figure is at most 8 of 771 (`red-team.md`, problem 3; checked for this file).
- **Filings.** The "body" code is yes in 9 of 2,216 passages, from 5 of 465 filers (1.1%; one vendor, Rubrik, supplies 5 of the 9).
  - Filings undercount by construction: passages were retrieved only where an agent phrase appears.
  - The code passed its kappa gate only after a full recode (deviation 11), and its accuracy check had 3–4 positives.
- **Posting.** IQVIA asks its AI security architect to "Represent Security Architecture in IQVIA's existing AI governance committees and taskforces", among an AI security architect's duties (`instruments/I3.md` #3).

**Confidence: low.**

**What changed since round one: revised.** Round one said councils form and decide cross-function rules (comparison claim 22). The council form appears. Nothing shows that it decides rule changes.

### The DevOps question

The pre-registered pattern verdict is unreliable by rule. Ten of the 15 scored features are "insufficient", above the limit of 5. On the 5 that remain, coder disagreement is 0.40, above the 0.35 limit (`pattern-match/result.md`; deviation 25). Even a clean run would have said "supported" in only about 5% of runs when DevOps is the truth (4–6%, `pattern-power-v4.md`). Under the A.4 reading rule the result is therefore **inconclusive**, and it is not evidence against H-DevOps.

The head-to-head with the scarcity pattern had 3 of its 6 separating features available, and no threshold was set for 3. The coders summed to +2 (Sonnet) and 0 (Haiku), a mean of +1.0, so the result is **undecided**.

The DevOps-leaning values rest on speech, coded single per speaker:
- N20: 6 of the 10 timestamped speakers who describe staffing gave the work to existing staff;
- N22: 5 speakers describe coordinating existing functions, against 3 who describe a new capability.

The postings point the other way (`instruments/I3.md`):
- 27 of 30 of today's AI-titled postings ask for or prefer AI-specific experience (23 require it);
- 13 of 21 name AI or ML teams;
- period operations and systems-engineering postings (2011–16; 26 of 60 with a DevOps-style title) asked for both operations experience (41 of 60) and programming experience (57 of 60).

On postings, today's AI roles look more like a scarce new capability than a merger of two functions. Finding 2's ratio (0.86, against D7's 3 to 1) points the same way, on a measure that was itself chosen after the fact.

---

## 2. Surviving archetypes, narrowed

These are signals from different sources and units. They are not a ranked typology, and no measure of how settled they are exists. The red team's "most settled", "most common" and "fast-growing" labels are dropped.

1. **AI security reviewer.** Security architects reviewing AI systems and agents before and after deployment is the most visible AI rule-work duty in postings: cluster 111, 18 employers, mostly regulated finance, PE share 0.30–0.40.
   - Cluster 111's stability rests on one posting (Thrivent REQ-47040). Without it, the cluster fails both found criteria.
   - The work may be an existing security duty extended to AI rather than a new figure. It is not shown to be settled.
2. **Embedded agent operator.** Among the few timestamped speakers who describe staffing, 6 of 10 gave agent running to existing staff inside a function (M072, M021, M073). The posting-side counterpart is Finding 2's existing-job duties, which are mostly technical occupations. The speaker coding has one coder.
3. **AI or agent builder.** AI, ML and automation titles appear at 81% of employers (about 2.5–2.7% of postings) and ask for or prefer AI-specific experience (27 of 30; 23 require it). Agent-specific builder titles exist: 155 "agentic" titles, now regrouped (deviation 26). They form no stable task bundle (cluster 112 did not replicate). No time series exists, so growth is not shown.
4. **Designated overseer (law-defined, from 2027–28).** Binding law will require deployers of high-risk AI to assign trained people with authority to oversee it (EU AI Act Art 26(2)), and Colorado deployers to offer, on request after an adverse decision and where commercially reasonable, review by a designated individual with authority to override it (SB26-189). These laws do not make those people owners of the rules. No posting for this figure was observed.

**Did not stand as roles:**
- **Governance council.** It is an organisational form held part-time by existing leaders. 5 of 34 speakers describe one, but none is shown to decide agent rules and none is agent-specific. It is not a figure anyone is hired as.
- **Business sponsor.** It is a permission label in one vendor's identity product (Microsoft Entra, November 2025). It shows how vendors scaffold the split between business and technical control. It is not a role observed in firms. ServiceNow's AI Steward is an admin role, not a sponsor.

---

## 3. Hypothesis verdicts, by the pre-registered rules

| ID | Refutation condition (short) | Verdict | Evidence |
| --- | --- | --- | --- |
| H1 (three conditions for a lasting role) | Two or more lasting roles lacked one of (a)–(c) | **Refutation condition met** (signatures only; low confidence) | DevOps and data scientist lasted without an owned number (N10 = no; `signatures.md` §8). (a) and (b) were not coded |
| H2 (lasting roles start at entry or mid level, with a written mandate) | Most lasting roles first appeared senior | **Not refuted** on seniority (signatures only). The written-mandate half is not supported | N12 = no for DevOps, SRE, data scientist and brand management. Only the mandated officer drew authority from a legal text (N11) |
| H3 (absorption by 2029; distinct roles under 20%, in AI-native firms) | Distinct protocol-role postings common outside AI-native firms by 2029, or none at all | **Untestable** | The 2029 claim lies in the future, and the share of firms with a distinct protocol-work role was not measured. AI titles (81% of employers) are not protocol roles |
| H4 (agent-management titles fold by 2028–29) | Titles keep growing through 2029 | **Untestable** | The crawl is current-only (deviation 21). Forecast 5 tracks it |
| H5 (BPM as managerial translation of AI safety) | Movement carriers found in firms, or weak mechanism overlap | **Untestable** | No data on carriers |
| H6 (middle band of written knowledge) | — | **Untestable** | No instrument measures it |
| H7 (time to amend) | Needs internal records | **Untestable** | No span about reviewing exceptions |
| H8 (desk research misses agreement-based roles) | Recordings give no earlier view than written sources for SRE, DevOps and CISO | **Refutation condition met** (weak test) | DevOps −1.5 years, CISO −17.7 years, SRE about 0 (`calibration.md`). The earliest recordings were missing |
| H-cal | Two or more of SRE, DevOps and CISO show no earlier description in speech | **Refuted** | DevOps and CISO fail (`calibration.md`) |
| H-speech | PV+RD below 2% of coded mentions, with seed recall ≥0.7 | **Refuted** | 1 of 771 timestamped spans (0.1%). The pooled figure is 2 of 862. Before adjudication it is 4 (A) and 9 (B) of 862. Seed recall is ≥0.94 |
| H-absorb | New-title postings outnumber existing-occupation postings with agent or rule duties | **Refutation condition met at the point estimate. The interval spans parity** | 0.86 (0.63–1.15). Red-team range 0.54–1.27. On the S1 definition it is about 0.06, which is decisively met |
| H-federated | ≥60% of PE in one stable cross-functional cluster | **Untestable** | No such cluster exists, so the condition is not met. But real PE records are too few to place 60% of them anywhere, and the positive claim (PE clustering with AO inside each function) has no support: cluster 111 has AO 0.07–0.10 and rests on one posting |
| H-number | Bundle persists with no owned number | **Untestable** | "Lasts" needs time. No speaker names an error rate or containment figure |
| H-agreement | No such document found in S6 | **Not tested as specified** (S6 was not searched). No instance found in the texts read | Change owners appear only in trading texts and lab policies (I4). Vendor "owner" roles are product permissions (I5) |
| H-DevOps | A.4 two-stage test | **Inconclusive** (pattern verdict unreliable by rule; power about 5%). Head-to-head undecided | See "The DevOps question" |
| Phase change (F1–F3) | Under 5% of agent-mentioning filers **and** under 5% of coded speech spans | **Refutation condition met for F2, the only feature measurable on both sources.** F1 and F3 are untestable. The claim as a whole is not fully tested | F2: about 1% of spans, 1.1% of filers (5 of 465). F1 and F3 filing codes failed kappa (0.52, 0.58), and speech for them was not counted by span. Filings undercount bodies by construction |

---

## 4. Round one, in one paragraph

Round one's description of the record held. Rule work is rare in public evidence about agents. PV and RD are close to absent. Agent running sits inside functions. And there is no case for hiring one senior protocol lead. Each of these replicated on an independent corpus of texts read in full (6 of 25 claims replicated, 13 revised). Its interpretation did not hold:
- The five function homes for rule design came mostly from search summaries and vendor documents.
- The trading template rests partly on guidance presented as rules.
- The calibration that excused the silence on PV and RD (H8, H-cal) was tested and failed.
- H1 met its refutation condition on the signatures (the 1 contradicted claim).
- "Practice before law" (claim 17, marked replicated in the comparison) is withdrawn here as a timing claim.

Five claims could not be reached by the rerun. On verification:
- the loop analysis reproduces exactly (122 of 127 claims confirmed);
- the loop red team holds 61 of 70;
- the industry slice is the weakest (38 of 70 confirmed; its counts include forecasts as "not found");
- across load-bearing claims, 221 of 267 were confirmed.

The error rate on a random 150 of the remaining claims is **20% (upper bound, recheck pending)** (Wilson 13–29%), because the verifier searched only the cited page (`review/verification-review.md`).

---

## 5. Limits that change how to read the findings

- **The firms that lead adoption are not visible.** 59% of frame employers have no crawlable board, including Alphabet, Apple, Meta, Microsoft, Amazon, Goldman Sachs and JPMorgan. 87.6% of postings come from Workday boards, and Nvidia supplies 262 of the original 2,790 new-title postings (`corpus-b/coverage.md`). Findings 2 and 3 describe large, mostly Fortune 500 employers, not AI leaders.
- **No time series.** The historical board crawl was not built. Title growth, H4 and most of the DevOps features cannot be assessed.
- **Speech is descriptive, partial and single-coded at speaker level.** Extraction recall is about 0.5, and every per-speaker category (staffing, placement, framing) comes from one coder. Rare codes are undercounted most.
- **Several results rest on post-hoc choices:**
  - leaf clustering (deviation 19);
  - the two-phase estimate and its independence assumption (deviation 24);
  - the consensus speech set (deviation 13);
  - the filing "body" recode (deviation 11).

  These do not all lean one way (`red-team.md`, deviation table).
- **Pre-registered measures not computed:** I4's share of duty postings citing a rule text, I5's comparison of vendor wording with posting wording, and I3's embedding comparison.
- **Public record only.** Informal rule changes inside firms would not appear in any of these sources. Field work (`field-plan-scaffold.md`) is the test.

**Where this file departs from the red team:**
- **The 5.32 flag ratio.** The red team notes that the pre-registered flag "met" D7 (5.32). That figure is not used, because a precision of 0.05–0.14 means it counts term mentions, not duties.
- **The holdout ARI.** It falls 0.137 short of the noise baseline. This is reported as a caveat, not a failure, because loop v2 §7's 0.1 tolerance was written for accumulation rounds, which deviation 16 replaced.
- **Archetype 3's wording.** The red team says about 190 agentic titles were mis-grouped. The regroup fixed 155, as deviation 26 states. The remaining roughly 38 human-group titles that look agent-related are not regrouped, and they are a residual undercount of new titles.

---

## 6. Forecasts

The blind findings' five forecasts are kept unchanged. None of the corrections bears on them.

| # | Check date | Forecast | Probability | Public source |
| --- | --- | --- | --- | --- |
| 1 | 2028-03-31 | At least 15% of 10-K filers filing in calendar 2027 use one of the six phrases ("AI agent", "AI agents", "agentic", "autonomous agents", "digital workers", "digital labor"). The 2026 figure is 6.75% | 0.60 | SEC EDGAR full-text search, same query and denominator |
| 2 | 2027-12-31 | Colorado SB26-189 takes effect on 1 January 2027 as signed, with its "individual designated by the deployer" review duty, and is not postponed again | 0.70 | leg.colorado.gov, session laws and bill history |
| 3 | 2028-01-31 | The EU AI Act's Annex III high-risk obligations apply from 2 December 2027, as set by the Omnibus (Reg. 2026/1744), with no further postponement in the Official Journal | 0.60 | EUR-Lex, consolidated AI Act and Official Journal |
| 4 | 2030-06-30 | The final 2028 Standard Occupational Classification has no detailed occupation whose title names AI agents, agent management or AI governance. The work stays a duty, not an occupation | 0.70 | U.S. Bureau of Labor Statistics, SOC revision pages |
| 5 | 2029-12-31 | At least one agent-scoped vendor certification dated in I5 is retired or renamed: Microsoft AB-620 or AB-900, Salesforce Agentforce Specialist, or AWS AIP-C01 | 0.75 | Microsoft Learn, Salesforce Trailhead and AWS Certification credential pages |

Forecasts 1 and 4 test absorption against a new occupation. Forecasts 2 and 3 test whether binding law, once in force, names a person at deployers. Forecast 5 tests the early fade and renaming signs (N24 now; H4 later).

---

## Addendum: round one verification after the corpus-wide recheck (10 October 2026)

Section 4's "20% (upper bound, recheck pending)" is superseded. After a corpus-wide recheck and an Opus review of it (`verification-random150.md`, `review/verification-recheck-review.md`), the random 150 split two ways: 5 of 131 checkable claims (3.8%, Wilson 1.6–8.6%) were contradicted by an acquired source, and 38 (29.0%, 21.9–37.3%) had no supporting passage in the corpus, 16 of them because the cited page was never acquired. "No passage" is not evidence that a claim is false. The industry slice is the weak part: 20 of 55 checkable claims (36.4%) were contradicted by a source, mostly bindingness and robustness. The loop analysis is unchanged (122 of 127), and the loop red team stands at 52 confirmed, 9 corrected and 9 not checkable.

## Addendum: citation audit (phase 5)

`review/citation-audit.md` checked all 33 corpus citations in this file: 26 pass. The corrections above were applied in place (vendor dates reduced to what stored sources support; filer count for bodies 5 of 465; AI-experience counts; Colorado's review duty stated as on-request; IQVIA and M024 relabelled; the 2023 open-tooling date marked as not resolving to a stored source, so the dated order holds from 2024 on at year level).
