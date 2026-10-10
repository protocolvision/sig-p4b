# Corpus B findings (blind)

Protocols for Business · rerun of 10 October 2026 · triangulation design section 7, step 4 · written by a fresh Opus agent that has not seen round one's conclusions. Not opened: `results/loop-2026-10-10/`, `results/industry-2026-10-10/`, `roles/`, `exploratory/`, `report/`, `README.md`, `recommendation-draft.md`, `results/rerun-2026-10-10/sealed/`. (The agent's write was refused by the harness, so the orchestrator saved the text unchanged.)

Every number carries the file it comes from. Paths are relative to `results/rerun-2026-10-10/` unless they start with a design file name. "Speech" findings are descriptive only, because H-cal was refuted (`calibration.md`; loop v2 section 8.5). Speech counts are lower bounds: extraction recall is about 0.5 (`instruments/I6.md`; deviation 13).

---

## 1. Findings

### F-1. Agent duties sit inside existing jobs about as often as under new AI titles. That is short of the 3-to-1 margin the DevOps pattern predicts.

**Evidence**
- I1 two-phase estimate (`instruments/I1-twophase.md`). Existing postings with at least one confirmed agent duty (final code AO, PE or RD): about 2,529 (S1 189 plus rest-of-crawl 2,340). New-title postings with a confirmed duty: 1,601 (1,384–1,795).
  - Ratio against new-title postings that carry a confirmed duty: **1.58** (1.03–2.45).
  - Ratio against all 2,790 new-title postings (the denominator set in deviation 21): **0.91** (0.66–1.21).
- The pre-registered lexical flag gives 5.32 (sampling-weighted; `instruments/I1.md`). But its precision against the coders is 0.05 and 0.14, so it counts mentions of the terms, not duties (`instruments/I1.md`; deviation 24).
- New AI-type titles are widespread but thin:
  - 161 of 198 employers (81%) have at least one;
  - they are 2.5% of postings, sampling-weighted;
  - venture-backed software firms 6.6% against Fortune 500 firms 2.3% (`instruments/I1.md`).
- Speech points the same way. Of the 11 speakers who describe staffing, 7 gave existing staff new duties, 3 hired and 1 did both (`instruments/I6.md`). M072, 2026-01-01: "she spends 20% of her time managing the agents, orchestrating the agents."
- I3: in a random sample of 30 of today's AI-titled postings, 25 ask for experience in the function where the work sits (`instruments/I3.md`).

**Confidence: medium.** Two kinds of data (postings and speech) point the same way, and the two-phase coding was adjudicated blind. However, the 0.91 interval crosses 1, and phase-2 kappa for AO and PE is only 0.61–0.64 (`instruments/I1-twophase.md`).

**Caveats**
- Two biases push the ratio down, against absorption:
  - the screen's recall is only 0.25–0.43, so existing postings whose agent duties avoid the term list are missed (`instruments/I1.md`);
  - the "new-title" group counts every AI, ML, automation or RPA title, not only agent-work titles (deviation 14).
- The true ratio is therefore probably above the estimate. Nothing here shows it reaching 3 to 1.

### F-2. Rule work is rare in what firms post and what practitioners say. Running agents dominates.

Rule work here means setting what agents may do (PE), finding where actual rules differ from written ones (PV), and deciding rule changes across functions (RD).

**Evidence**
- Postings (`coding/scores.md`):
  - in 300 real posting records, coders found PE 2 and 6, PV 1 and 4, RD 0 and 0, and AO 3 and 5 (coder A and coder B);
  - a blind Opus check found rule work in **3 of 40** records, with 39 of 40 agreement with each coder on whether rule work is present (`review/coding-real-check.md`);
  - seed recall passes for both coders: PV 0.95; PE 1.00; RD 1.00 and 0.94, all with Wilson lower bounds of 0.72 or more (`coding/scores.md`). So the rarity is not a coder blind spot, within the limit that seed recall is an upper bound (deviation 8).
- Speech (`instruments/I6.md`), final codes on 862 spans:
  - AO 170, PE 24, PV 2, **RD 0**, OT 667;
  - no span describes reviewing exceptions or a decision to change a rule across functions.
- The nearest speech cases:
  - M021, 2025-09-19: "We changed the guard rails" (the functions involved are not stated);
  - M065, 2025-10-28: "I had to modify a bit our compliance approval process for new tools".
- The clearest rule-work posting line is R0397, 2026 snapshot: "turn goals into … rules, constraints … that AI systems can execute" (`review/coding-real-check.md`).

**Confidence: high for postings, medium for speech.** The posting coding passed every gate and an independent check. Speech extraction recall is about 0.5, and the kappas before adjudication were PV 0.28 and RD 0.33 (deviation 22).

**Caveat.** Postings say what employers ask for, and speech says what speakers choose to tell. If rule changes are agreed informally, neither source would show them (research-design H8). This finding is about the written and spoken record, not about the work itself.

### F-3. Where rule work shows up in postings, it forms around AI security, inside the security function. It does not form as a cross-functional bundle.

**Evidence**
- I2 found 11 stable clusters, 8 of them work clusters (holdout ARI 0.827; baseline 0.964; `clusters/leaf/stability.md`).
- The one AI cluster among them is 111, "Assess AI systems for security risk" (it/security, technical; 35 discovery tasks; 18 employers; `instruments/I2.md`):
  - coders gave it PE shares of 0.30 (A) and 0.40 (B), with AO at 0.07–0.10;
  - central span: "Review AI systems and integrations for security risk before and after deployment."
- Three AI clusters formed in discovery but did not replicate in the holdout (best Jaccard 0.17–0.33; `instruments/I2.md`):
  - 110, "Govern AI systems for compliance and responsible use" (the only mixed business and technical one);
  - 112, "Build agentic AI workflows";
  - 113, "Identify AI use cases".
- AI-titled postings combine business and technical clusters no more often than other postings (`instruments/I1.md`):
  - found clusters: 0.6% against 0.3%;
  - all clusters: 8.2% against 8.4%.
- I3 examples, all from the 2026 snapshot (`instruments/I3.md`):
  - #12 Merck: "security architecture reviews and risk assessments for AI systems, AI applications, AI agents";
  - #3 IQVIA: "reports to the Security Architecture leader";
  - #19 JLL: reports to the "Regional Business Governance & Compliance Director".

**Confidence: medium.** The clusters are stable, but 65% of tasks are noise. Only 8 of 114 clusters count as found, and found-cluster cross-function counts are tiny (1 and 3 postings; `instruments/I1.md`).

**Caveats**
- Clustering describes English-language postings only (deviation 20).
- "Not found" means unstable, not absent (`instruments/I2.md`).
- The rule for language clusters was set after the fact (deviation 20), and so was the switch to leaf selection (deviation 19).

### F-4. Practitioners most often describe a coordinating body (council, committee, guild or centre of excellence) or a team inside one function. Filings barely mention such bodies.

**Evidence**
- I6 coding of 34 speakers (`instruments/I6.md`):
  - placement: 5 describe a central body between functions, 5 a team within one function, 1 work spread across individuals, 23 not described;
  - framing: 5 describe coordinating existing functions, 3 a new specialist capability, 26 not described.
- Quotes:
  - M010, 2025-07-22: "I'm on the AI Governance Council and we've just had our second meeting.";
  - M024, 2025-06-30: "we have a strat and gov team that sit in the middle";
  - M065, 2025-10-28: "I totally delegated the influence to that guild led by this chief architect that was highly respected".
- I3 #3 (IQVIA, 2026 snapshot) lists a "governance committee seat" among the duties (`instruments/I3.md`).
- Filings (log entries for 10 October; `corpus-b/passage-coding.md`):
  - a standing body ("body") is coded yes by both models in **9 of 2,216 passages** from 465 filers, at most about 2% of filers;
  - "reorg" (kappa 0.52) and "metric" (kappa 0.58) failed the reliability gate and are not used (deviation 11).

**Confidence: low to medium.** Speech is descriptive only, and two-thirds of speakers do not address the question. The filing code "body" passed kappa (0.75), but its accuracy was checked on fewer than 5 positives.

**Caveat.** Filings describe products far more than internal organisation (F-5). A low filing count says little about whether such bodies exist.

### F-5. Agent language in annual reports went from almost nothing to about 7% of all 10-K filers in four years (18% of the frame's filers). It is mostly about products.

**Evidence**
- `corpus-b/filings-denominator.csv`: share of 10-K filers using one of the six phrases:
  - 0.05% (2022), 0.06% (2023), 0.12% (2024), 1.71% (2025), **6.75%** (2026, filed through 10 October);
  - among frame employers: 0%, 0%, 0.21%, 3.8%, **18.0%** (77 of 428).
- Content (log entries for 10 October; deviations 9–11):
  - vendors (SIC 7370–7374, 3570–3579) supply 64% of passages;
  - consensus codes over 2,216 passages: product 1,342; own use 369; controls 109; workforce 24; rule cited 22; metric 15; reorg 10; body 9;
  - none of 539 10-Ks with a detectable Item 9A uses a search phrase in that item.

**Confidence: high for the counts, medium for the content codes.** The counts are phrase hits on EDGAR full text. Product and controls passed every check. "Own use" passed, but it over-includes generic AI use (precision 0.76; `review/passage-codes-check.md`).

**Caveat.** 2026 is a partial year, but most 10-Ks are filed by March. The rise is in disclosure language, which can run ahead of practice.

### F-6. Binding AI law requires a person to oversee AI but names no one who owns changes to its rules. Only trading rules and the AI labs' own policies name a change owner.

**Evidence**
- I4 read 111 provisions from 19 texts (`instruments/I4.md`):
  - 32 provisions regulate how rules or limits are changed, and 15 of those name an owner: **12 in trading and markets, 3 in lab self-policies, 0 in AI law and standards** (0 of 4 there);
  - in the AI law and standards family, 5 of 37 provisions name anyone.
- Quotes:
  - EU AI Act Art 26(2) (C9b1da45a): "Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority". It applies from 2 Aug 2026 as enacted; the Omnibus moves it to 2 Dec 2027 and 2 Aug 2028;
  - Colorado SB26-189 (CO-SB26-189-act), effective 1 Jan 2027: "individual designated by the deployer who has authority to approve, modify, or override a consequential decision";
  - PRA SS5/18 3.2–3.3, 30 Jun 2018 (Cef3dde3f): "each algorithm to have assigned owners, who are accountable for the algorithm's use and performance".
- Timing: practice comes first. Speech about running agents dates from 2024-11-28 (`instruments/I6.md`). Binding rules that require a designated person at deployers start on 2027-01-01 (Colorado) and 2027–28 (EU) (`instruments/I4.md`).

**Confidence: high on what the texts say.** Every quote was checked by script. The coding has a single coder with an Opus review (`instruments/I4.md`).

**Caveats**
- I4's own pre-registered measure, the share of duty-carrying postings that cite a rule text, was not computed. The filings code "rule cited" failed kappa (0.39).
- "Practice leads law" rests on timing, not on citation counts.
- California SB 53 was not acquired (`instruments/I4.md`).

### F-7. The dated record starts with open tools and practice. Agent certifications, vendor role definitions and binding law come later. The first community date is missing.

**Evidence**
- `instruments/I5c.md`, `instruments/I5.md` and `instruments/I4.md`:
  - open agent tooling, third-earliest: **2023-08-15** (2023-01-31 on a lenient reading);
  - AI-governance certification: 2024-03-05 (IAPP AIGP);
  - first speech in this frame about operating agents: 2024-11-28 (`instruments/I6.md`);
  - first agent-scoped certification: 2025-03-03 (the Agentforce Specialist rename);
  - vendor agent roles: ServiceNow's release family on 2025-03-12; Microsoft Entra sponsor and owner wording on 2025-11-05;
  - binding deployer rule: 2027-01-01 (Colorado).
- Vendors relabelled existing products for agents within about three years: Einstein Copilot became Agentforce on 2024-09-12, and Agentspace became Gemini Enterprise on 2025-10-09. Both coders code N24 yes (`pattern-match/result.md`).
- Vendors split business accountability from technical control. Microsoft Entra, 2025-11-05 (ms-entra-owners): "Sponsors provide business accountability for agents, making lifecycle decisions without technical administrative access."

**Confidence: low to medium.** The dates are labelled by type after review (`review/I5-review.md`). However:
- Meetup founding dates could not be read, so the community step is missing, and N03 and N13 are "insufficient";
- the speech frame starts in 2024, so "practice first" is truncated (amendment A.2, point 6);
- the comparison of vendor wording with posting wording was not run (`instruments/I5.md`).

### F-8. The pre-registered pattern test cannot say whether this is DevOps-like. By rule its verdict is unreliable. On the three features that separate DevOps from the scarcity pattern, the evidence leans toward DevOps, below any decision threshold.

**Evidence**
- `pattern-match/result.md`: 11 of 21 features are "insufficient". These include **10 of the 15 scored features** (N01, N03, N04a, N06a, N08, N09, N12, N13, N15, N23).
- By amendment A.2 point 9, more than 5 left out makes the verdict unreliable.
  - `result.md` cites the superseded "more than 8" threshold. The verdict is the same under either rule. (Orchestrator note: `result.md` has since been corrected.)
  - My own count adds a second trigger. On the 5 scored common features that remain (N02, N19, N20, N21, N22), the coders disagree on 2, so d = 0.40, which is above the 0.35 band. `result.md` reports 0.20 because it counts over all 10 coded features. (Corrected; it now reports 0.40.)
- Feature-level results, read without pattern names (`pattern-match/coder-*.csv`):
  - N19 "no new title, team or metric" is **no** for both coders: titles, teams and named measures exist;
  - N24 vendor relabelling is **yes** for both;
  - N02 cross-function merge and N07 duty more common than title are **partial** for both;
  - N05 practitioner metrics, N10 owned number and N11 title tied to law are **partial** for both.
- Head-to-head (section 4): mean sum +1.0 on 3 of 6 features. No threshold was set for 3 features, so the result is not distinguishable.

**Confidence.** The decision itself was set in advance. The power to decide was always low: when DevOps is the truth, it is "supported" in 4–6% of runs (`pattern-power-v4.md`).

**Caveat.** "Unreliable" is not "no". By amendment A.4's reading rule, a failed or unreliable verdict is not evidence against H-DevOps.

---

## 2. Hypotheses

Evidence comes from Corpus B instruments unless marked. "Signatures only" means the dated historical record in `signatures.md`, not a present-day instrument.

### Research design

| ID | Verdict | One line of evidence |
| --- | --- | --- |
| H1 (three conditions for a lasting role) | **not supported** (signatures only; low confidence) | Two lasting patterns lack an owned number, part of condition (c): DevOps and data scientist have N10 = no, graded P (`signatures.md` §8). The signatures were not coded for (a) and (b); this is not a Corpus B test |
| H2 (lasting roles start at entry or mid level, with a written mandate) | **partly supported** (signatures only) | Most lasting patterns did not start senior: N12 is no for DevOps, SRE, data scientist and brand management. Authority came from a legal text only for the mandated officer (N11), so the "written mandate" half fails (`signatures.md` §8). Present-day N12 is insufficient |
| H3 (absorption by 2029; distinct roles under 20% of firms, concentrated in AI-native firms) | **partly supported** (current state only; the 2029 claim is untestable now) | Rule work sits inside security and governance units, and AI titles are 2.5% of postings, more common at VC software firms (6.6%) than in the Fortune 500 (2.3%) (`instruments/I1.md`, `I2.md`). The share of firms with a distinct protocol-work role was not measured |
| H4 (agent-management titles peak and fold by 2028–29) | **untestable with this evidence** | The crawl is current-only, with no titles by year (`instruments/I1.md`; deviation 21) |
| H5 (BPM as the managerial translation of the AI-safety movement) | **untestable with this evidence** | No data on carriers. The only AI texts that name change owners are lab self-policies (3 of 3; `instruments/I4.md`) |
| H6 (middle band of written knowledge) | **untestable with this evidence** | No instrument measures how much rule knowledge is written down |
| H7 (time to amend) | **untestable with this evidence** | It needs internal records. Speech has no span about reviewing exceptions (`instruments/I6.md`) |
| H8 (desk research misses agreement-based roles) | **not supported** (pre-registered test; weak) | Its refutation condition is met. Recordings gave no earlier view of the arrangement than written sources for DevOps (−1.5 years) or CISO (−17.7 years), and SRE gave about 0 (`calibration.md`). The earliest recordings were missing, which biases the test toward refutation |

### Loop v2

| ID | Verdict | One line of evidence |
| --- | --- | --- |
| H-cal | **not supported** (refuted as pre-registered) | 2 of 3 roles fail: DevOps and CISO (`calibration.md`). Speech is therefore descriptive only |
| H-speech | **not supported** (refutation condition met) | PV plus RD = 2 of 862 coded spans (0.2%), under the 2% bar. Seed recall is PV 0.95 and RD 0.94–1.00, with Wilson lower bounds of 0.72 or more (`instruments/I6.md`, `coding/scores.md`). Seed recall is an upper bound, and extraction recall is about 0.5 |
| H-absorb | **partly supported** | Confirmed agent-duty postings in existing occupations against new-title postings: 0.91 (0.66–1.21) against all new titles, 1.58 (1.03–2.45) against confirmed ones (`instruments/I1-twophase.md`). Not refuted, but the interval crosses 1 |
| H-federated | **partly supported** | No stable cross-functional cluster holds PE. The one found cluster with PE (111) is inside security; the cross-functional governance cluster 110 did not replicate (`instruments/I2.md`). The positive evidence is one cluster |
| H-number | **untestable with this evidence** | "Lasts" needs time. Speech names agent figures only inside single firms and gives no error rate or containment figure by name (`instruments/I6.md`) |
| H-agreement | **not supported** | No firm outside the AI labs was found to publish an agent rule that names who may change it. Change owners appear only in trading rules and lab policies (`instruments/I4.md`), and vendor "owner" roles are product permissions (`instruments/I5.md`). Stratum S6 was not among these inputs |

### General hypothesis and phase change

| ID | Verdict | One line of evidence |
| --- | --- | --- |
| H-DevOps | **untestable with this evidence: pattern verdict unreliable by rule** (not "no") | 10 of 15 scored features are insufficient, and coder disagreement on the rest is 0.40 (`pattern-match/result.md`). The head-to-head is not distinguishable (+1.0 on 3 features). Instrument predictions: I1 short of 3:1 (F-1); I2 has no joint cluster of PE or RD with AO (F-3); I4 practice before law in timing (F-6); I5 tooling first (F-7) |
| F1 (reorganisations joining business and engineering around agents) | **untestable with this evidence** | The filings code "reorg" is unreliable (kappa 0.52; deviation 11). Speech has a few reorganisations, none clearly around agents: M040, 2026-04-04, "we actually decided to pull all the FP&A team together under one central organization" |
| F2 (standing bodies with decision rights) | **partly supported** | Speech: 5 of 34 speakers (15%) describe a central body (`instruments/I6.md`). Filings: 9 of 2,216 passages, at most about 2% of filers (log). Not refuted, because speech is above 5%. No body's decision rights over agent rules are shown |
| F3 (new operating metrics) | **untestable with this evidence** | The filings code "metric" is unreliable (kappa 0.58). Speech names agent figures only inside single firms. M021, 2025-09-19: "Toby fixes 60% of those issues itself." |

Phase-change refutation rule: F1–F3 must be under 5% of agent-mentioning filers **and** under 5% of coded speech. It is **not met**, because F2 appears for 15% of speakers. With F1 and F3 unmeasurable, the phase-change claim is at most partly supported, through F2.

---

## 3. Comparison grid

Each cell gives one instrument's direction: + supports, − counts against, ± mixed, · no usable evidence. The last column applies section 7.6:
- **strong**: 3 or more instruments with different data support;
- **single**: one supports;
- **two**: two instruments with different data support (the design has no label for this case);
- **none**: no instrument supports.

I1 and I3 (today's sample) draw on the same posting crawl. I2 clusters the same postings' tasks. They count as one kind of data. Filings (design section 4.2) are shown as an extra column.

| Hypothesis | I1 postings | I2 tasks | I3 history | I4 rules | I5 vendors | I6 speech | Filings | Strength |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | · | · | · | · | · | · | · | none |
| H2 | · | · | · | · | · | · | · | none |
| H3 (now) | ± | + | ± | · | · | + | · | two |
| H4 | · | · | · | · | ± | · | · | none |
| H5 | · | · | · | ± | · | · | · | none |
| H6 | · | · | · | · | · | · | · | none |
| H7 | · | · | · | · | · | · | · | none |
| H8 | · | · | · | · | · | − (calibration) | · | none (single, against) |
| H-cal | · | · | · | · | · | − | · | none (single, against) |
| H-speech | · | − (postings: rule work rare) | · | · | · | − | · | none (against) |
| H-absorb | ± | · | + | · | · | + | · | two |
| H-federated | · | + | + | · | · | ± | · | single (posting data) |
| H-number | · | · | · | · | · | ± | · | none |
| H-agreement | · | · | · | − | − | · | · | none (against) |
| H-DevOps | − (D7) | − | ± | + (timing) | ± | ± | · | single |
| F1 | · | · | · | · | · | ± | · (unreliable) | none |
| F2 | · | · | + | ± | · | + | − | two |
| F3 | · | · | · | · | · | ± | · (unreliable) | none |

No hypothesis reaches **strong**.

---

## 4. The head-to-head (amendment A.3, Stage 2, reported conditionally)

The features that separate DevOps from the scarcity pattern (`signatures.md` §10) are N15, N04a, N20, N21, N22 and N23. N04a and N23 fell to the truncation rule, and N15 was insufficient for one coder. **Three remained** (`pattern-match/result.md`). In the signatures, DevOps is yes on all three and the scarcity pattern is no.

| Feature | Sonnet | Haiku | Score (+1 toward DevOps, −1 toward scarcity, 0 tie) |
| --- | --- | --- | --- |
| N20: first holders mostly existing staff given the work | yes | partial | +1 / 0 |
| N21: first agent-work roles or teams sit in operations or IT, not research | partial | partial | 0 / 0 |
| N22: stated purpose is coordinating existing functions, not a scarce new capability | yes | partial | +1 / 0 |
| Sum | +2 | 0 | mean **+1.0** |

- **Direction.** Every non-zero score points toward DevOps, and none toward the scarcity pattern.
  - N20 rests on speech: 7 of the 11 described speakers gave existing staff the work.
  - N22 rests on speech framing: 5 coordinating against 3 new capability, with 26 not described.
  - N21 is mixed. Speech places the work in sales, IT, finance, procurement and central bodies, and vendor roles are mostly IT admin or owner roles (`instruments/I6.md`, `I5.md`).
- **No decision.** Thresholds were fixed only for 6 features (k = 4) and 4 features (k = 3). With 3 there is no k, so under the reading rule the result is "not distinguishable". Even with the 4-feature k, +1.0 is far below 3.
- **Evidence the coders did not weigh** (my reading, not coded as a feature):
  - I3's today sample asks for AI-specific experience in 27 of 30 postings and names AI or ML teams in 13 of 21;
  - period DevOps postings asked for both operations experience (41 of 60) and programming experience (57 of 60) (`instruments/I3.md`);
  - so on postings, today's AI roles look more like a new scarce capability than a merger of two backgrounds;
  - speech and postings point different ways on N22.

---

## 5. What would change these conclusions

1. **A historical board crawl.** Internet Archive captures of the same boards, 2019–2026, were planned but not built because CDX was rate-limited (log; `instruments/I1.md`). With titles by year:
   - N01, N04a, N08, N12 and N14 could be coded;
   - the D2 trend could be measured;
   - the pattern verdict might leave "unreliable".
2. **A recall-corrected absorption estimate.** Fully coding a random sample of unflagged tasks in existing postings would capture duties the term list misses. If that lifts the ratio from about 1–1.6 to 3 or more, F-1 and D7 flip toward the DevOps prediction.
3. **The missing first-community date** (Meetup founding dates, earlier conferences). This would settle N03 and N13 and the practitioner-versus-vendor order in F-7.
4. **Coverage of the firms that lead adoption.** Alphabet, Apple, Meta, Microsoft, Oracle, Amazon, Goldman Sachs, JPMorgan and most utilities have no crawlable board (`corpus-b/coverage.md`). Their postings, or field interviews there, could show rule-ownership roles absent from the Workday-heavy crawl.
5. **Field evidence of unwritten rule changes.** If interviews show cross-function rule-change decisions being made without being posted or spoken about publicly, F-2 becomes a finding about the record, not the work.

---

## 6. Forecasts

| # | Check date | Forecast | Probability | Public source |
| --- | --- | --- | --- | --- |
| 1 | 2028-03-31 | At least 15% of 10-K filers filing in calendar 2027 use one of the six phrases ("AI agent", "AI agents", "agentic", "autonomous agents", "digital workers", "digital labor"). The 2026 figure is 6.75% (`corpus-b/filings-denominator.csv`) | 0.60 | SEC EDGAR full-text search, same query and denominator |
| 2 | 2027-12-31 | Colorado SB26-189 takes effect on 1 January 2027 as signed, with its "individual designated by the deployer" review duty, and is not postponed again | 0.70 | leg.colorado.gov, session laws and bill history |
| 3 | 2028-01-31 | The EU AI Act's Chapter III high-risk obligations (Annex III systems) apply from 2 December 2027, as set by the Omnibus (Reg. 2026/1744), with no further postponement published in the Official Journal | 0.60 | EUR-Lex, consolidated AI Act text and Official Journal |
| 4 | 2030-06-30 | The final 2028 Standard Occupational Classification contains no detailed occupation whose title names AI agents, agent management or AI governance. The work stays a duty, not an occupation | 0.70 | U.S. Bureau of Labor Statistics, SOC revision pages (bls.gov/soc) |
| 5 | 2029-12-31 | At least one of the agent-scoped vendor certifications dated in I5 is retired or renamed: Microsoft AB-620 or AB-900, Salesforce Agentforce Specialist, or AWS AIP-C01 | 0.75 | Microsoft Learn credential retirement pages; Salesforce Trailhead credential pages; AWS Certification pages |

Forecast 5 tests the early fade and renaming signs (N24 now, D4 later). Forecasts 1 and 4 test absorption against a new occupation. Forecasts 2 and 3 test whether binding law, once in force, names a person for deployers.
