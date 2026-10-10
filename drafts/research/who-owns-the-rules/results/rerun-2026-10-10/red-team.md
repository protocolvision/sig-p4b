# Red team: Corpus B findings and report-plan archetypes

Rerun of 10 October 2026. Written by a fresh Opus agent asked to find the strongest reasons each finding could be wrong or overstated. Inputs: `findings-corpus-b.md`, `../../report/report-plan.md`, `deviations.md`, `log.md`, `instruments/*`, `clusters/leaf/*`, `coding/*`, `pattern-match/*`, `review/*`, `corpus-b/*`, `../../triangulation-design.md` and `../../loop-design-v2.md`. Paths are relative to `results/rerun-2026-10-10/` unless stated.

I re-ran several numbers from committed data. Each check names its input file, and the scripts are described inline so they can be repeated: `clusters/leaf/assignments.csv.gz`, `instruments/I1-posting-level.csv.gz`, `coding/phase2-*.csv`, `coding/speech-*.csv`, the speech consensus spans in `corpus/b-raw/extract/speech-*consensus/`, and the k-flagged-tasks rule from `loop-tools/i1_twophase.py`. Nothing was committed.

---

## The five most serious problems

### 1. The only stable AI cluster (111) is stable because of one job posting

- In the holdout half, 24 of the 53 tasks predicted into cluster 111 come from a single posting: Thrivent Financial REQ-47040, "Principal Engineer - AI Security", which has 43 holdout tasks. The same posting supplies 32 of the 66 tasks in the matching independent holdout cluster 80 (`clusters/leaf/assignments.csv.gz`).
- Drop that one posting and cluster 111 fails both found criteria:
  - predicted holdout members fall from 53 to **29**, below the 30 threshold;
  - best Jaccard falls from 0.506 to **0.432**, below 0.5.
- Its discovery side is also thin: 35 tasks from 19 postings. The 300-per-employer cap (deviation 16) does not guard against one long posting, because the split is by posting.
- The only reason anything was found at all is deviation 19 (eom gave 0 found).
- **Affected:** F-3; H-federated's "partly supported"; archetype 1 ("most settled"); the I2 "+" cells in the grid for H3, H-federated and F2.
- **Narrower reading:** no AI task bundle in the posting crawl is robustly stable. AI security review is the closest to stable, and it hangs on one employer's posting.

### 2. H-absorb's pre-registered refutation condition is met at the point estimate, and the new-title group omits 155 "agentic" titles

- **The rule.** Loop v2 §4 says H-absorb is refuted if "new-title postings outnumber existing-occupation postings that carry agent or rule duties". The comparison is with all new-title postings, the denominator deviation 21 fixed.
- **The measured ratio is 0.91.** The 2,790 new-title postings outnumber the roughly 2,529 existing postings with a confirmed duty (`instruments/I1-twophase.md`). F-1 and the hypothesis table instead report "partly supported… not refuted, but the interval crosses 1". That is the wrong way round: the point estimate sits on the refuted side.
- **The ratio depends on assumptions the findings do not show.** I re-ran the `i1_twophase.py` estimator:

  | Assumption | Ratio, existing : all new-title | Ratio, existing : confirmed new-title |
  | --- | --- | --- |
  | As reported (independence, adjudicated codes) | 0.91 | 1.58 |
  | Tasks confirm together within a posting (full correlation) | 0.54 | 2.17 |
  | Coder A's codes only (Sonnet) | 0.69 | 1.45 |
  | Coder B's codes only (Haiku) | 1.27 | 2.05 |

  - Independence matters because new-title postings average 4.3 flagged tasks, against 1.85 in rest20. Assuming independence inflates new-title confirmation most.
  - The adjudicator chose between a coder known to default to OT (A) and one that over-codes (B). It sided with B in 41 of 67 such cases (`coding/phase2-*.csv`).
  - No reading reaches 3:1. Against all new-title postings, the plausible range is roughly 0.5–1.3.
- **A classification bug, contrary to deviation 14.** 155 postings whose title contains "agentic" are filed in the `newtitle-agent-human` group (human support or sales agents) and left out of the 2,790. Examples:
  - "Staff Software Engineer, Agentic Systems";
  - "Software Engineer, Forward Deployed Agent Builder";
  - "Senior Director, Agentic Engineering".

  In all, 193 human-group titles from 52 employers look like AI-agent work (`instruments/I1-posting-level.csv.gz`, columns `group`, `term`, `title`). Deviation 14 lists "agentic" as a new-title term, and its human-agent rule applies to the word "agent" only. As a result, the new-title group holds exactly one posting matched on "agent", plus 35 that contain "agentic" but were matched on "AI".
  - Cluster 112 ("Build agentic AI workflows") draws 25 of its 78 discovery tasks from this mis-grouped set.
  - Adding the 155 back moves the ratio further toward new titles.
- **What "existing jobs" means here.** 53% of the estimated existing-posting numerator is in O*NET major groups 15 (computer and mathematical, 910) and 17 (engineering, 320) (major-group accuracy about 83%). So "absorption" is mostly software and engineering staff doing AI work, not business staff running agents. The ten S1 occupations alone (loop v2's own definition of "existing occupations") give 189 against 2,790: a ratio of 0.07.
- **Affected:** F-1; H-absorb; N07 and N19; archetypes 2 and 3; the report-plan sample counts (2,790).

### 3. The phase-change refutation turns on a switch of unit (speakers, not coded speech)

- **The rule.** Triangulation §2 says the phase-change claim is refuted if F1–F3 appear "in under 5% of filers mentioning agents … and in under 5% of coded practitioner speech".
- **How the findings apply it.** They count F2 per speaker (5 of 34, 15%) and conclude the rule is "not met".
- **Coded speech is spans.** That is the unit H-speech uses ("coded activity mentions"). The consensus spans hold about 8 that mention a council, committee, guild, centre of excellence or "team in the middle", out of 862, which is about 1%. Filings give at most about 2% of filers. On the span unit, F2 is under 5% on both sources, so the refutation condition is met for the one feature that was measurable.
- **F2 requires bodies "with decision rights over agent rules".** None of the five bodies is shown to decide agent rules. They are general AI governance councils and CoEs; F-4 itself says "No body's decision rights over agent rules are shown".
- **Filings undercount bodies by construction.** Passages were retrieved only where one of the six agent phrases appears (`corpus-b/filings-inputs.md`). An "AI governance committee" paragraph without the word "agent" is never retrieved. The `body` code also passed only after deviation 11's full recode: kappa was 0.00 on the first overlap and 0.75 on the full set. Its accuracy rests on 3–4 positives (`review/passage-codes-check.md`).
- **Affected:** F-4; F2 "partly supported"; the "phase change at most partly supported" sentence; archetype 4.
- **Required action:** report both units and state that the span-unit reading meets the refutation condition.

### 4. "Running agents dominates" holds for speech, not postings; RD = 0 in speech is the adjudicator's call

- **Postings do not show dominance.** F-2's posting evidence is 300 real records stratified across found clusters and noise. Almost all are generic non-AI tasks, so the rarity of rule work there is a base rate.
  - Among agent-related records, rule work is not dominated: coder A has AO 3 against PE+PV 3, coder B AO 5 against PE+PV 10 (`coding/scores.md`). The blind reviewer found AO-type work in 4 records and rule work in 3 (`review/coding-real-check.md`).
  - The better sample is the 600 phase-2 flagged tasks. There the final codes give **PE 33 and PV 2 against AO 88** (`coding/phase2-*.csv`, final = agreed plus adjudicated). Rule design is about 28% of agent-related codes, and 16 of 46 (35%) in new-title postings.
  - "Running agents dominates" is a speech result (AO 170 against PE 24). In postings the ratio is about 2.5 to 1, and PE is a substantial minority.
- **Speech RD.** Each speech coder coded RD on 3 spans. On M072_c07:1 both coders coded RD ("decision on which leads go to agent, sales view named"), and the Opus adjudicator replaced it with AO (`coding/speech-coderA.csv`, `speech-coderB.csv`, `speech-adjudicated.csv`). Deviation 22 sends only disagreements to adjudication. Here the code sets differed (RD+AO against RD), so the adjudicator overrode a code both coders gave. "RD 0" should read "RD 0 after adjudication; 3 spans per coder before".
  - H-speech still fails its bar under any reading: PV+RD is 4 of 862 for coder A and 9 of 862 for coder B, both under 2%.
- **The "not a coder blind spot" claim is weaker than stated.**
  - 38 of 60 positive seeds are invented scenarios, more specific than real records (deviation 8).
  - Coder A defaulted unflagged records to OT (deviations 22 and 24).
  - Coder A's real-record rule-work recall in the blind check is 2 of 3.
  - The 39-of-40 agreement is mostly agreement on obvious OT records.

### 5. The six archetypes are a post-hoc typology that mixes units, and their ordering is not measured

- **No pre-registered rule produces archetypes.** Each rests on a different unit, so their "recurrence" cannot be compared:
  - a task cluster (1);
  - a speaker count, single-coded (2, 4);
  - AI-titled postings (3);
  - one vendor's permission label (5);
  - legal text (6).
- **"Ordered by how settled they are" has no measure behind it.**
  - Only archetype 1 has a stability test, and it fails without one posting (problem 1).
  - "Fast-growing" (3) has no time series: the crawl is current-only, which is also why H4 is untestable.
  - The report plan calls unstable clusters "forming, not settled" and draws them hatched. Clusters with best Jaccard of 0.007 (cluster 21, ML model monitoring), 0.17 (110, 113) and 0.33 (112) did not reproduce. Nothing shows they are forming.
- **The speech evidence behind archetypes 2 and 4 has three further faults.**
  - **Speaker-level coding is single-coded.** One write-up agent coded staffing, location and framing per speaker, with no second coder, after speech failed calibration (descriptive only).
  - **The same speakers fill several categories.** M010 and M065 are "existing staff" (archetype 2) and also "central body" (archetype 4). M021 runs "our centre of excellence" yet is coded "within one function". M054's "I asked everybody to create their own agent" is tool use, not an operator role.
  - **The untimestamped stratum was pooled despite failing its gate.** `log.md` (speech, 8 untimestamped pages) says this stratum failed the count-ratio gate (0.667) and is "reported apart and not pooled". `instruments/I6.md` pools its 91 records into the 862. M054 and M067 come from it, and M067 supplies one of the two PV spans and the speech "measures".

---

## Other notable problems

- **"Practice leads law" compares unlike dates** (F-6, F-7, H-DevOps grid I4 "+").
  - Practice is dated by first mention in a speech frame that starts on 1 January 2024 by design. Law is dated by when it takes effect.
  - Dated by adoption, binding text came before the first speech record (2024-11-28). The EU AI Act was published in July 2024 and in force from 1 August 2024, with Art 26 in its final wording. Colorado's original AI Act (SB24-205), with deployer duties, was signed in May 2024. These two dates are outside the I4 files and should be checked before use.
  - The pre-registered I4 measure (share of duty postings that cite a rule text) was not computed.
- **Unregistered I5c search.** It departs from A.2 point 6 and is not recorded in `deviations.md` (`instruments/I5c.md`):
  - tooling was searched "by function" (guardrails, observability, authorisation, governance), not with the pre-registered phrases;
  - "build" frameworks were outside the function search;
  - OSI licence status was not checked (Phoenix, Langfuse and NeMo show NOASSERTION);
  - no search log was written.

  The tooling date (2023-08-15) therefore depends on the search. Including build frameworks would probably move it earlier, which would not change the order.
- **F-7's headline contradicts its own timeline.** "Starts with open tools and practice", yet the first certification (IAPP AIGP, 2024-03-05) comes before the first speech record (2024-11-28), and the speech frame is truncated.
- **Inconsistent change-ownership coding in I4.**
  - `review/I4-review.md` notes that generic "define lines of responsibility" provisions are coded `names_role = yes` for PRA 2.3 but `no` for AI Act Art 17(1)(m). Art 17(1)(m) requires an accountability framework covering, among other things, Art 17(1)(a)'s "procedures for the management of modifications". Under the PRA reading, AI law's "0 of 4" change owners could be 1 of 4. The denominator is 4 in any case.
  - Of the 12 trading change-owner provisions, 8 are supervisory guidance or expectations, not binding rules: the FCA reviews (5) and PRA SS5/18 (3), which is coded `binding = no`.
- **Holdout stability against the baseline.** The holdout ARI (0.827) is 0.137 below the noise baseline (0.964). Loop v2 §7's tolerance is 0.1 below baseline (written for accumulation rounds; deviation 16 reports the baseline "beside" without a rule). `clusters/leaf/stability.md` still lists "HDBSCAN … eom" under Parameters while also stating "Selection method: leaf".
- **Coverage of the clustering.** Only 2.8–4.1% of discovery tasks in each posting group fall in a found work cluster, and 63–65% are noise. I2 describes about 3.5% of the task pool.
- **Speech counts.** The consensus speech set was chosen after the variant scores were seen (deviation 13). It favours precision and has recall of about 0.5. This lowers every count, rare codes most, which reinforces "rare" findings.
- **Sources of bias across the posting instruments.**
  - 87.6% of selected postings come from Workday boards.
  - 166 of 198 employers are Fortune 500.
  - Big tech and most large banks are absent (`corpus-b/coverage.md`).
  - Nvidia supplies 262 of 2,790 new-title postings and 6 of the 30 I3 examples.
  - Cluster 111's and cluster 110's employers are dominated by regulated finance (Thrivent, Corebridge, Northern Trust, Fannie Mae, State Street, LPL). Security- and compliance-shaped AI work there may say more about the frame than about where rule work forms.

---

## Findings, one by one

### F-1. Agent duties sit inside existing jobs about as often as under new AI titles

- **Strongest alternative:** the comparison measures where AI-related technical work is posted, not absorption into business functions.
  - 53% of the existing-posting numerator is in software and engineering occupations.
  - The new-title group is mostly AI (1,838) and automation (656) titles, and it leaves out the 155 most agent-specific "agentic" titles.
- **Weakest link:** `instruments/I1-twophase.md`. The rest20 confirmation rate is 29 of 300 tasks, scaled to 2,340 of the 2,529 numerator. The result also rests on the within-posting independence assumption and on adjudication between coders (range 0.54–1.27; problem 2).
- **Biases:**
  - The caveat that "two biases push the ratio down" is one-sided:
    - the independence assumption inflates the new-title count for the confirmed-ratio but deflates the all-titles ratio;
    - the agentic mis-grouping deflates the denominator.
  - Workday and Fortune 500 heavy.
  - I3's "25 of 30 ask for same-function experience" is circular as absorption evidence. These are new-title postings, and for AI engineering roles the "same function" is AI engineering.
- **Confidence:** medium is too high. Low to medium.
- **Verdict: stands with a narrower claim.** "In this Workday-heavy, Fortune 500 crawl, existing-title postings with a confirmed agent or AI duty are about as numerous as AI- or automation-titled postings: 0.5–1.3 to 1 across plausible assumptions. More than half of them are software and engineering jobs. Nothing approaches 3 to 1. H-absorb's refutation condition is met at the point estimate, so H-absorb is inconclusive, not partly supported."

### F-2. Rule work is rare; running agents dominates

- **Strongest alternative:** postings show rule design (PE) at about a quarter of agent-related codes (phase 2: PE 33, PV 2, AO 88). Rarity is a base-rate effect of sampling generic tasks.
- **Weakest link:** `coding/scores.md`. The real-record counts (PE 2 and 6, AO 3 and 5) are drawn mostly from non-AI clusters and noise. Speech RD 0 depends on the adjudicator overriding both coders on M072_c07:1.
- **Biases:**
  - consensus speech extraction (recall about 0.5, chosen after scoring);
  - coder A's OT default;
  - seeds more specific than real records.
- **Confidence:** "high for postings" is too high for "dominates". It is fine for "RD and PV are nearly absent".
- **Verdict: stands with a narrower claim.** "Finding rule gaps (PV) and deciding rule changes across functions (RD) are nearly absent from postings and speech. Rule design (PE) is a minority but not rare share of agent-related posting duties (about a quarter). Running agents dominates in what practitioners say."

### F-3. Where rule work shows up, it forms around AI security, inside the security function

- **Strongest alternative:** leaf HDBSCAN (deviation 19) favours small, homogeneous clusters. Security review is a tightly worded genre. AI governance (110) and AI security (111) sit on one boundary: 110's holdout members go to holdout clusters 79 and 80, and so do 111's. Which side "replicates" is close to chance.
- **Weakest link:** cluster 111's found status rests on one Thrivent posting (problem 1). The I3 examples are partly off-point: JLL #19 reports to a business governance and compliance director in Facilities, not to security. In I3, rule-related wording appears in 20 of 30 AI postings across engineering, content, consulting and security.
- **Biases:**
  - post-hoc deviations 19 and 20;
  - 65% noise, with 3.5% of tasks in found clusters;
  - English only;
  - regulated-finance employers dominate clusters 110 and 111;
  - packet shares are coder estimates from 40 spans (deviation 17).
- **Confidence:** medium is too high for the positive claim. Low.
- **Verdict: stands with a narrower claim.** "No stable posting cluster joins rule work with agent operations across functions. The one AI cluster that passed the stability test, AI security review, did so only because of one posting. Postings place AI rule work in security and governance roles, but they do not show where it settles."

### F-4. Practitioners describe coordinating bodies; filings barely mention them

- **Strongest alternative:** these are general AI governance councils and CoEs, not bodies for agent rules. Filings miss them because retrieval required agent phrases.
- **Weakest link:**
  - `instruments/I6.md`, "Who does the work": single-coded per speaker, with overlapping assignments (M010, M065, M021);
  - the filing `body` code, with 3–4 positives in the accuracy check.
- **Biases:**
  - podcasts favour senior, articulate, governance-minded speakers;
  - the untimestamped stratum was pooled against the log's rule;
  - speech is descriptive only.
- **Confidence:** low to medium. Low is right.
- **Verdict: stands with a narrower claim.** "5 of 34 speakers mention an AI governance council, committee, guild or centre of excellence. None is shown to decide agent rules. Filing passages retrieved by agent phrases rarely mention such bodies, which says little about their existence." At span level, F2 is under 5% in speech too (problem 3).

### F-5. Agent language in 10-Ks rose to about 7% of filers, mostly about products

- **Strongest alternative:** "mostly products" reflects the composition of filers, not adopters' disclosure. Vendors supply 64% of passages. Among adopter filers, more report own use (126) than products (93) (`corpus-b/passage-coding.md`, by filer type; own_use precision 0.76).
- **Weakest link:** content codes are counted per passage, so vendors with many passages dominate.
- **Biases:**
  - 2026 is a partial year;
  - "digital workers" and "digital labor" may catch non-AI usage (not checked);
  - own_use over-includes generic AI use.
- **Confidence:** right for the counts.
- **Verdict: stands with a narrower claim.** "Agent phrases went from almost none to 6.75% of 10-K filers (18% of the frame) by 2026. Passages are mostly product descriptions because vendors supply most of them. Among non-vendor filers, own use is mentioned about as often as products."

### F-6. Binding AI law names an overseer, not a change owner; only trading rules and lab policies name one

- **Strongest alternative:** the contrast is partly built by coding.
  - AI law's change-regulating provisions number 4, so "0 of 4" is fragile.
  - Art 17(1)(a)+(m) is coded inconsistently with PRA 2.3.
  - 8 of the 12 trading change owners come from guidance, not binding rules.
  - Lab policies name their own boards by construction.
- **Weakest link:** `instruments/I4-required-functions.csv`, row Art 17(1)(m) (`names_role = no`), against `review/I4-review.md` point 4. The coding is single-coder.
- **Biases:**
  - a fixed list of texts: no California SB 53, ISO 42001, NYC LL144 or sector AI guidance (for example bank model-risk guidance);
  - EU annexes not read.
- **Confidence:** "high on what the texts say" holds for the quotes. "Practice comes first" rests on unlike dates (adoption against effective dates) and should be dropped or reworded.
- **Verdict: stands with a narrower claim.** "The binding AI texts read (EU AI Act, Colorado) require deployers to assign people to oversee or review AI outputs. None of the 4 AI-law provisions on changes names who decides them. Named change owners appear in trading rules and guidance and in labs' own policies." The timing sentence does not stand as worded.

### F-7. The dated record starts with open tools and practice; certifications, vendor roles and law come later

- **Strongest alternative:** tooling, then certification, then vendor admin roles, then law is the generic order for any enterprise software category. It does not separate DevOps from scarcity or tool-operator patterns.
- **Weakest link:** `instruments/I5c.md`. The search deviates from A.2 and is not recorded in `deviations.md`, the community date is missing, and practice is dated after the first certification.
- **Biases:**
  - the speech frame starts in 2024;
  - vendor pages are dynamic, and many dates are NF;
  - 12 vendors only.
- **Confidence:** low to medium. Low is right.
- **Verdict: stands with a narrower claim.** "Open agent tooling (2023) comes before agent-scoped certifications (2025), vendor role definitions (2025) and binding deployer rules (2027). The first community date is missing and the practice date is truncated by the frame, so the D3 order cannot be tested." Remove "and practice" from the headline.

### F-8. The pattern test cannot say; the head-to-head leans DevOps below any threshold

- **Strongest alternative:** the lean is an artefact of source. N20 and N22 rest on single-coded speaker counts (7 of 11; 5 against 3) from a source rated descriptive only. One coder (Haiku) scored the head-to-head 0. The postings point the other way.
- **Weakest link:** `instruments/I6.md`, "Who does the work", the input to N20 and N22.
- **Biases:**
  - N19 = "no" is driven by 2,790 AI and automation titles, many of which predate agents (ML engineers);
  - deviation 25 had no effect on the verdict.
- **Confidence:** right. The verdict is fixed by rule.
- **Verdict: stands.** Narrow the "leans toward DevOps" sentence: "On the three separating features the two coders sum to +2 and 0. The DevOps-leaning values rest on speech, and postings lean toward the scarcity pattern. Not distinguishable."

---

## Archetypes (report plan, orchestrator synthesis)

1. **AI security reviewer ("most settled").**
   - **Alternative:** an existing security-architecture duty extended to AI (absorption into security), not a new figure.
   - **Weakest link:** cluster 111 rests on one posting (problem 1). Coder A's primary code for it is OT (0.55).
   - **Verdict: stands with a narrower claim.** "Security architects reviewing AI systems is the most visible AI rule-work duty in postings, at about 18 employers, mostly regulated finance. It is not shown to be settled."
2. **Embedded agent operator ("most common in speech").**
   - **Alternative:** "existing staff" is a residual category for speakers describing tool adoption, such as M054.
   - **Weakest link:** single-coded 7 of 11 speakers, with 23 not described. The posting-side absorption is mostly technical occupations.
   - **Verdict: stands with a narrower claim.** "Among the few speakers who describe staffing, most gave agent work to existing staff. Postings for existing jobs carry agent duties about as often as AI titles do, mainly in technical jobs."
3. **AI or agent builder ("fast-growing, unsettled").**
   - **Alternative:** these are AI and ML engineering and solutions roles that predate agents.
   - **Weakest link:** "fast-growing" has no time data. Agent-builder titles (the "agentic" set) were excluded from the new-title group by the grouping bug.
   - **Verdict: stands with a narrower claim.** Drop "fast-growing". "AI, ML and automation titles appear at 81% of employers (2.5% of postings) and ask for AI experience. Agent-specific builder titles exist (about 190 'agentic' titles, mis-grouped) but form no stable task bundle."
4. **Governance council member.**
   - **Alternative:** a committee seat held part-time by existing leaders. It is an organisational form, not a figure, and it is not agent-specific.
   - **Weakest link:** 5 single-coded speakers; no decision rights shown; cluster 110 did not reproduce. Filings rarity is a retrieval artefact.
   - **Verdict: does not stand as an archetype.** Narrower: "Some organisations describe AI governance councils, guilds or centres of excellence (5 of 34 speakers). Whether they own agent rules is not shown."
5. **Business sponsor (vendor-defined).**
   - **Alternative:** a permission label in one identity product.
   - **Weakest link:** 1 of 30 vendor role rows is a "sponsor" (Microsoft Entra). ServiceNow's AI Steward "configure[s] AI Control Tower settings", which is an admin role, not a business sponsor. There is no evidence anyone holds either role, and the vendor-to-posting wording comparison was not run (`instruments/I5.md`).
   - **Verdict: does not stand.** Narrower: "One vendor (Microsoft, 2025-11-05) separates business accountability ('sponsor') from technical ownership of agents. It shows how vendors scaffold the split, not a role observed in firms."
6. **Designated overseer (law-defined, from 2027).**
   - **Alternative:** a narrow compliance duty. EU Art 26(2) covers high-risk Annex III systems only. Colorado's designated individual reviews consequential decisions, not agent rules. Dates have already moved (Omnibus; Colorado's earlier delay).
   - **Weakest link:** not observed in any posting. The I4 citation measure was not computed.
   - **Verdict: stands with a narrower claim.** "From 2027–28, binding law will require deployers of high-risk or consequential-decision AI to name people who oversee or review its outputs. These laws do not make them owners of the rules."

The ordering by settledness does not stand. Present the six as heterogeneous signals from different sources, not as a ranked typology.

---

## Did the post-hoc deviations steer results?

| Deviation | What it changed | Direction |
| --- | --- | --- |
| 19 (eom → leaf, after 0 found) | Created every found cluster, including 111 | Leaf favours small, single-genre clusters. That works against finding a broad cross-functional PE+AO bundle, so it leans toward F-3 and H-federated and against the I2 DevOps prediction. Without it, I2 has no result. |
| 20 (language clusters, rule written after seeing cluster 0) | Removed 3 found clusters, none AI | Neutral for AI claims. Confines I2 to English, so non-English AI duties go to noise. |
| 24 (two-phase, after the flag's precision was known) | Replaced the pre-registered measure, which gave 5.32 and met D7's 3:1, with an estimate of 0.91 or 1.58 | Moved I1 from supporting D7 to "short of 3:1" and pushed H-absorb toward refutation. Well justified by 0.05–0.14 precision. But the new measure has unregistered choices (independence, choice of denominator, adjudication between asymmetric coders) that move it from 0.54 to 1.27 (problem 2). |
| 25 (scoring script corrected) | d from 0.20 to 0.40 | No steering. The verdict was already "unreliable" on the more-than-5-dropped trigger. |
| Also worth stating: 11, 13, 22 | 11 rescued `body` (kappa 0.00 to 0.75) by a full recode after the gate failed; 13 picked consensus after seeing the scores; 22's adjudication removed an RD both coders gave | 11 enables F-4's filing count; 13 and 22 lower rare-code counts, which leans toward F-2 and H-speech. |

Net: the post-hoc choices do not all lean one way. Deviation 24 leans against DevOps and absorption, and deviation 19 leans toward "rule work inside one function". None of them plausibly produced F-2's PV/RD absence, F-5's counts or F-8's verdict.

## Places where the findings contradict pre-registered rules

1. **H-absorb verdict.** The refutation condition is met at the point estimate (0.91). The findings report "partly supported".
2. **Phase-change rule.** "Coded speech" is evaluated per speaker, not per coded span (problem 3). F2's "decision rights" condition is not shown.
3. **H-federated.** The positive claim requires PE to cluster *with AO* inside each function. Cluster 111 has AO 0.07–0.10, and F-8 itself says there is "no joint cluster of PE or RD with AO". The refutation test cannot work with 2–6 PE real records. "Not refuted (untestable)" is the defensible verdict, not "partly supported".
4. **I4's pre-registered measure was not computed**, yet the grid scores I4 "+ (timing)" for H-DevOps with a substitute measure. I1's "− (D7)" scores the pre-registered prediction with the post-hoc measure. The pre-registered flag met the prediction (5.32).
5. **Deviation 14's term list.** 155 "agentic" titles are mis-grouped as human agents.
6. **A.2 point 6.** The I5c search terms, OSI check and search log were not followed, and this is not recorded in `deviations.md`.
7. **`log.md`'s own rule for untimestamped speech** ("reported apart and not pooled") is broken in I6.
8. **Loop v2 §7.** Stability within 0.1 of the baseline is not met (0.137 below), although deviation 16 arguably displaced it.
9. **Deviation 22.** Adjudication was to resolve disagreements, but it removed a code both coders gave (M072_c07:1, RD).
10. **H3 "partly supported".** New AI titles at 81% of employers cut against "distinct roles under 20% of firms" unless AI titles are excluded from "distinct roles". Without a measure of protocol-role firms, the defensible verdict is "untestable".

## Suggested corrections before the report

- Fix the `agentic` grouping and re-run I1 and the two-phase estimate. Report the 0.5–1.3 sensitivity range, and change H-absorb to "inconclusive (refutation condition met at point estimate)".
- Report cluster 111's single-posting dependence. Drop "most settled" and "forming".
- Report F2 on both units. Drop the claim that the phase-change refutation is "not met".
- Rewrite F-2's "dominates" for postings, using phase-2 code shares. Restate speech RD as "0 after adjudication".
- Drop "practice leads law" as a timing claim, or date both sides by adoption.
- Record the I5c departures and the pooling of untimestamped speech in `deviations.md`.
- Fix the stale "eom" parameter line in `clusters/leaf/stability.md`.
