# Comparison: round one against the blind rerun

Protocols for Business · rerun of 10 October 2026 · triangulation design section 7, step 6, and research
design section 10 · written by a fresh Opus agent after `findings-corpus-b.md` was committed and the phase 2
verification was finished. No round-one file was edited. Paths are relative to `results/rerun-2026-10-10/`
unless they start with `../`, which means the study root `drafts/research/who-owns-the-rules/`.

## The conclusion

**Round one's description of the record holds up. Its interpretation does not.** The core descriptive
finding is that rule work is rare in public evidence about agents, and that finding unwritten rules (PV) and
deciding rule changes across functions (RD) are close to absent. The rerun reproduces it on an independent,
rule-sampled corpus of acquired texts, with coders shown by seeded cases to be able to see PV and RD. Round
one's translation of algorithmic trading to agent-run business shrinks. AI law names people who oversee AI
but nobody who owns changes to its rules. In trading, the named owners outside the binding core sit in
supervisory guidance, not rules. Two of the five gatekeepers checked out. The layered recommendation keeps
its negative advice (don't hire one senior protocol lead; don't let vendors hold your rules). Most of its
positive machinery has no support in either round: the exception review, the COO register, time to amend,
an executive certifying controls, and certified designers.

Of 25 round-one claims compared below:

| Status | Claims |
| --- | --- |
| Replicated | 6 |
| Revised | 13 |
| Contradicted | 1 |
| Round one only | 5 |
| New in rerun (section 2) | 10 findings |

**The three biggest changes**

1. **Rule work has one observed home: AI security review.** Round one placed rule design as a thin duty
   across agent operations, legal engineering, GTM engineering, identity administration and accounting
   operations. That placement came mostly from search summaries and vendor documentation. In the rerun, the
   only stable AI work bundle in 25,512 postings is "Assess AI systems for security risk" (cluster 111). It
   sits in the security function, and coders put its rule-design share at 0.30–0.40. None of round one's
   five function homes appears as a stable bundle.
2. **The trading translation applies to trading, not to agents in general.** Rule texts were read in full
   (I4). Of 15 provisions that name who owns rule changes, 12 are in trading and 3 in AI labs' own
   policies. None is in AI law: the EU AI Act and Colorado name an overseer, not a change owner.
   Verification found that the inventory, the material-change definition, the named senior manager and
   multi-function sign-off are FCA and PRA guidance, not rules. Only the gatekeepers Mastercard and Amazon
   are confirmed. The executive who certifies controls, the change forum and the certified designers are
   therefore evidenced only for regulated trading.
3. **The PV and RD layers now rest on argument, not evidence.** Round one said the silence on PV and RD was
   expected, because the method would have missed past roles built on internal agreements. The rerun
   tested that reasoning (H-cal, H8), and it failed. Practitioner recordings gave no earlier view than
   written sources for DevOps or the CISO. Seeded tests show the coders detect PV and RD when they are
   present. Yet across 300 posting records and 862 speech spans, PV appears in at most a handful of records
   and RD in none. The silence may still mean the work is unrecorded (field work is the test). It can no
   longer be read as support.

---

## 1. Claim by claim

Status key: **replicated** (rerun evidence agrees); **revised** (rerun evidence agrees in part, how is
stated); **contradicted** (rerun evidence goes against it); **round one only** (no rerun evidence either
way; under triangulation design 7.6, a verified round-one claim that no instrument reaches).

Verification codes: LA = `verification-loop-analysis`, LR = `verification-loop-redteam`, IN =
`verification-industry`, R150 = `verification-random150`. Claim ids (CLxxxx) are rows in those CSVs.

| # | Round-one claim (short) | Where it came from | Verification status | Rerun evidence | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Rule work is rare; running agents (AO) dominates. Agreed codes: PE 13, AO 90, OT 188 of 298 | `../results/loop-2026-10-10/analysis.md`; report p.3; recommendation §1 | LA confirmed: `analyze.py` output byte-identical, kappa 0.95 recomputed | Postings: in 300 real records, PE 2/6, PV 1/4, RD 0/0 (coder A/B); seed recall ≥0.94; independent Opus check finds rule work in 3 of 40 (F-2). Speech: AO 170, PE 24, PV 2, RD 0 of 862 spans (I6) | **Replicated**, with stronger evidence: acquired texts, independent corpus, seeded recall |
| 2 | Finding unwritten rules (PV) and deciding cross-function changes (RD) "don't appear in public documents at all" | report summary; recommendation §1; loop red team §4 | LA, LR confirmed. LR adds that PV did appear as a secondary code (R1848, R8231), so "never seen" overstates | PV 1–4 posting records and 2 speech spans; RD 0 everywhere. No span describes reviewing exceptions or a cross-function rule decision. Nearest: M067 (2025), "five different policies … on what constituted a return" (F-2, I6) | **Replicated** (near-absent rather than absent) |
| 3 | Rule design (PE) does not cluster, and the clustering is unstable | loop analysis; loop red team §1 | LR confirmed; stability failure borderline (ARI 0.595 against a 0.6 bar) | With a stable method (holdout ARI 0.83), PE forms one small stable bundle: cluster 111, AI security review (35 tasks, 18 employers, PE share 0.30–0.40). The cross-functional governance cluster 110 did not replicate (I2, F-3) | **Revised**: rule design does bundle, once and narrowly, inside security |
| 4 | Rule design is a duty inside existing roles: agent operations, legal engineers, GTM engineers, identity admins, accounting operations leads | recommendation §1, §3, §5; `../roles/README.md`; report p.5 | R150: role-library details 20% wrong where checkable (Wilson 13–29%). LA: C9's "Senior Manager, Accounting Operations" not found. LR: two of eight "rule work stays with incumbents" examples (R9692, R8958) have no supporting passage | "Duty, not job" holds: no stable cross-function bundle; AI titles are 2.5% of postings (I1). The home differs: Merck and IQVIA AI security architects, JLL under a governance and compliance director (I3). Title count by the comparison agent in `../corpus/b-raw/mapping/selection.csv` (not an instrument): legal engineer 0, AI steward 0, GTM engineer 2, agent owner or manager 1 (the 20% sample undercounts non-AI titles) | **Revised**: still a duty, but its observed home is security and governance, not the five functions |
| 5 | Running agents is the work forming into jobs; agent operations specialist named a likely distinct role in four of five rounds | report summary and p.3; loop cluster C1 | LR corrected: C1 takes 19 (not 20) of 29 records from five aggregator postings | AO is the main agent activity (I6). But in speech it is carried by existing staff (7 of 11 speakers who describe staffing; M072: "she spends 20% of her time managing the agents"). Confirmed duty postings in existing jobs against new titles: 0.91 (0.66–1.21) to 1.58 (1.03–2.45) (I1). 12 AI or agent operations titles at 6 employers (comparison agent's count). Today's AI titles are mostly engineers and consultants (I3: 10 and 8 of 30). The agentic-workflow cluster 112 did not replicate | **Revised**: running agents dominates, but it is not visibly forming into an operator job; it is split between existing staff and AI engineering titles |
| 6 | Agent operations is dispersed and sits inside functions (top cluster 29%) | loop analysis; loop red team "what survives" | LA confirmed | Speech AO by function: sales and RevOps 89, support 26, finance 17, IT 11, engineering 10 (I6). No stable AO cluster; AO share 0.07–0.10 in the one AI packet (I2) | **Replicated** |
| 7 | Vendors attach rule design to admitting and permissioning agents in admin consoles; "business sponsor" and "AI steward" are product roles | loop red team §1–3; exploratory analysis; report p.4 | LA confirmed (ServiceNow AI steward, Cf7d364f5). IN: Microsoft "sponsor for every new Copilot Studio agent" not in the acquired pages | I5: 30 vendor roles at 12 vendors (15 admin, 6 owner, 1 sponsor). Entra (2025-11-05): "Sponsors provide business accountability for agents … without technical administrative access." Vendor "owner" roles are product permissions (H-agreement). Agent owner or manager titles in postings: 1 | **Replicated** (as vendor design, not as observed jobs) |
| 8 | Silence is weak evidence: applied early, the method would have missed brand management, CISO and SRE, whose authority came from internal agreements (H8; calibration) | report summary; recommendation §1; `../exploratory/role-emergence.md` | R150: interpretive and lineage claims mostly unverifiable; the report itself marks the lineages "partly from memory" | H-cal refuted: for DevOps and CISO, recordings came no earlier than written sources (−1.5 and −17.7 years). H8's refutation condition is met, on a weak test because the earliest recordings were missing (`calibration.md`). Signatures tie the CISO to a 1995 bank title and 2002 statute, and date SRE's written error budget to 2016 | **Revised**: keep as a caveat on what desk research can see; drop as evidence for PV and RD |
| 9 | Most firms absorb protocol work into existing roles; distinct roles are a minority, concentrated in AI-native firms (H3; task-economics prediction) | `../research-design.md` H3; `../exploratory/predicting-roles.md` | Predictions; not checkable (R150 unverifiable) | H3 partly supported (current state only). AI titles are 6.6% of postings at VC software firms against 2.3% in the Fortune 500. 81% of employers have at least one AI title (I1). The duty-to-title ratio is about 1 to 1.6, not "most". The share of firms with a distinct protocol-work role was not measured | **Revised**: concentration in software firms replicated; absorption is about even with new titles, not a clear majority |
| 10 | A role lasts when it owns a permanent trade-off, nobody else owns it, and an outside force renews demand with a number the role controls (H1) | `../exploratory/role-emergence.md` §6; research design H1 | Unverifiable (interpretive) | DevOps and data scientist lasted without an owned number (N10 = no, grade P), which meets H1's refutation rule (`signatures.md` §8). Signatures only; conditions (a) and (b) not coded | **Contradicted** (low confidence) |
| 11 | Lasting roles began at entry or mid level, with authority from a written mandate (H2) | role-emergence §6; report p.5 table | Lineage dates partly unverifiable; R150: "late 2022" Scale prompt-engineer hire not found | N12 = no (not senior at first) for DevOps, SRE, data scientist and brand management. A legal text gave authority only to the mandated officer (N11) | **Revised**: the "not senior" half holds; the "written mandate" half does not |
| 12 | Agent-management titles peak and fold by 2028–29, as prompt engineer did (H4) | research design H4; predicting-roles §6 | Forecast | Untestable: the crawl is current-only. Early sign only: vendors relabelled products and certifications within about three years (N24 yes for both coders; Einstein Copilot to Agentforce 2024-09-12) | **Round one only** (forecast open; rerun forecast 5 tests it) |
| 13 | Algorithmic trading and the electricity grid are the nearest analogues, effectively tied | `../results/industry-2026-10-10/findings.md` §1–2; report p.4 | IN: scores reproduce; "88% of weightings" holds only under flat Dirichlet weights; trading beats the grid in about 91% of weightings, so "tied" rests on two cell scores | No instrument re-scored the industries. I4: trading texts regulate rule changes and name owners (12 of 15 named change owners); grid texts name certified operators (7 of 7) but none regulates changes. I3 period postings too few to compare (17 trading, 5 grid) | **Revised**: trading is the closer analogue for who owns rule changes; "tied" is not supported |
| 14 | In trading, rule work settled into three forms: a mid-level risk and control team with the kill switch; registered or certified designers; a CEO or named senior manager who answers for controls | industry findings §3; report p.4–5 | IN corrected (CL0210–0212, CL0216): the team is Director level, under an existing global head. Inventory, material change, named SMF and multi-function sign-off are PRA and FCA guidance or expectations. Binding: 15c3-5 CEO certification, Series 57, RTS 6 | I4 reproduces the binding core from full texts: 15c3-5(e)(2) CEO annual certification; FINRA 16-21 registration of whoever designs or significantly modifies algorithms; RTS 6 Art 5(2), a designated person authorises deployment or substantial update. PRA SS5/18 algorithm owners with Front Office, Risk and control sign-off (guidance) | **Revised**: named persons and registration replicated; "mid-level" and "required" corrected |
| 15 | The grid wrote its rules through industry committees; smaller organisations let individuals own rule changes (Mozilla, Wikipedia, Progressive) | industry findings §2–3; `counterexamples.md`; report p.4 | IN: UCPTE 1951 and NAPSIC 1963 unverifiable; NERC 1968 confirmed. R150: Progressive 1983 start not found | No instrument covers grid committees or the counter-examples | **Round one only** |
| 16 | The kind of outside pressure shapes the structure: law produced named persons and certification; industry bodies produced committees and standards | industry findings §2–3; report summary | IN corrected (CL0223, CL0267): law is coded for 1 of 5 "person" rows; weak for the grid; "moderate" too strong | I4: AI law names an overseer (EU AI Act Art 26(2), Colorado SB26-189) but no change owner (0 of 4 change provisions). Voluntary lab self-policies name change owners and boards (3 of 3) | **Revised**: law produces a named overseer; named change owners come from an industry template (trading) or a firm's own policy (labs) |
| 17 | Structures do not form only after a law (H-lever not supported); practice comes before law | industry findings §2; report summary | IN: H-lever reasoning holds on NERC 1968 alone | Speech about running agents dates from 2024-11-28 and a central governance team from 2025-06-30 and a council from 2025-07-22 (I6). Binding deployer rules start 2027-01-01 (Colorado) and 2027–28 (EU) (F-6, F-7) | **Replicated** |
| 18 | Outside rules are already arriving through chokepoints: Visa, Mastercard, Amazon, Google Play and Microsoft bind agents that pay or act through them | industry §3a; `gatekeepers.md`; report p.4; recommendation §1, §4 | IN: Mastercard and Amazon confirmed (Amazon BSA effective 4 Mar 2026). Visa details unverifiable (paywall). Google Play date and Microsoft sponsor wording not in the acquired pages. "Browsers" unsupported (CL0225–0227) | I4 coded only Amazon's notice: agents identify themselves and stop when asked; no role named. Mastercard guide and California SB 53 not acquired. No instrument tested whether gatekeeper rules create in-firm structures | **Revised**: narrowed to two confirmed gatekeepers; neither requires an in-firm role |
| 19 | Finance regulators will reuse trading's templates for agents: inventory, material change, kill function, named senior owner (high confidence; 0.6 by end 2027) | industry red team §5; findings §4; recommendation §9 | IN corrected (CL0266): "high" applies to direction only; the FINRA 2026 report does not yet require agent inventories | The templates exist in trading texts (I4). No AI-specific finance rule is in Corpus B | **Round one only** (open forecast) |
| 20 | Protocol engineering becomes a certified specialty inside existing desks, like registered algorithm developers | industry §3; report p.5; recommendation §3–4 | IN corrected (CL0204): H-bridge untested; Series 57 adds an exam for people already doing the work. CL0252: NERC certification exists outside finance | Agent certifications exist but are vendor product credentials (Agentforce Specialist 2025-03-03; Microsoft AB-620, 2026), and they are relabelled fast (I5). Governance credentials are separate (IAPP AIGP 2024; ISACA AAIA, AAISM 2025). AI law asks for "competence, training and authority", not registration (I4) | **Revised**: certification is arriving through vendors and governance bodies, not as a register of agent designers |
| 21 | Protocol vision becomes the inventory, then monitoring; one register of agents and rules | industry §3; report p.5; recommendation §2–3 | IN corrected (CL0211, CL0216): the inventory requirement is FCA guidance, not a rule | Vendors ship registries and agent identities: Entra Agent ID; Agent 365 lets IT quarantine unsanctioned agents (2025-11-18); ServiceNow AI Control Tower; Google ownership transfer (I5). JLL runs a "portfolio governance 'system of record'" (I3 #19). PV itself is near-absent (F-2) | **Revised**: the register is arriving as vendor tooling run by IT admins, not as rule-finding work |
| 22 | In large firms, cross-functional rule decisions sit with a named executive or committee; a protocol lead prepares them; councils form before rule roles | industry §3.3; report p.5; recommendation §3, §7; predicting-roles §6 (integration) | IN: CL0221 not found (authors' recommendation) | Councils, guilds and centres of excellence: 5 of 34 speakers (M010 "AI Governance Council"; M065 "AI guild"); IQVIA posting lists a "governance committee seat". Filings: 9 of 2,216 passages. No body's decision rights over agent rules shown; RD 0. Outside trading and labs, no text names a change owner (F-4, F-6) | **Revised**: the council form appears; nothing shows it decides rule changes, and outside trading no named executive owns them |
| 23 | Don't hire one senior "Business Protocol Lead"; distinct roles start at practitioner level | recommendation §7; `../exploratory/business-protocol-lead-critique.md`; report p.5 | Recommendation; not checkable | No posting for a role that owns rules across functions in 25,512 selected postings (F-2, F-3). Lasting roles did not start senior (N12). Titles, teams and measures for AI work do exist (N19 = no), but none for protocol work | **Replicated** |
| 24 | BPM is a managerial translation of AI safety's agent-control strand, not the movement's institutional expression (H5) | `../exploratory/bpm-and-ai-safety.md`; research design H5 | Unverifiable (interpretive) | Untestable: no data on carriers. One related fact: the only AI texts that name change owners are labs' own policies (Anthropic RSP, OpenAI Preparedness, DeepMind FSF) (I4) | **Round one only** |
| 25 | Time to amend can be measured from existing records and is the right number for rule work (H7) | recommendation §3–4; business-protocol-lead critique §6; research design H7 | Unverifiable | Untestable: it needs internal records. No speech span on reviewing exceptions. The measures speakers name are interaction scoring and share handled by the agent ("Toby fixes 60% of those issues itself", M021) (I6) | **Round one only** |

**Against the design's section 7.6 labels.** No round-one claim, and no rerun finding, reaches **strong**
(three or more instruments with different data). Claims 1–2 are supported by two kinds of data (postings and
speech), and claim 17 by two (rule texts and speech). Claims 12, 15, 19, 24 and 25 are **round one only**.

---

## 2. New in the rerun

Round one had none of these. All rest on acquired texts from Corpus B.

1. **Agent language in annual reports went from almost nothing to 6.75% of 10-K filers in 2026** (18% of
   frame filers). It is mostly product talk: 64% of passages come from vendors, and product codes outnumber
   own-use codes 1,342 to 369. No 10-K uses an agent phrase in Item 9A, controls and procedures (F-5).
2. **AI law names an overseer but no change owner.** In the AI law and standards family, 5 of 37 provisions
   name anyone, and 0 of 4 change provisions name an owner. Named change owners sit in trading rules (12)
   and lab self-policies (3) (F-6, I4).
3. **AI security review is the one stable AI work bundle.** Governance (110), agentic workflows (112) and
   use cases (113) are large but did not replicate in the holdout half (F-3, I2).
4. **The ratio of agent duties to new titles is measured, and it is about even.** Postings in existing
   occupations with a confirmed agent duty, against new AI-titled postings, give 0.91–1.58. That is short of
   the 3-to-1 margin the DevOps pattern predicts (F-1).
5. **Postings and speech disagree about who does the work.** Speech says existing staff (7 of 11 speakers),
   coordinating functions. Today's AI postings ask for AI-specific experience (27 of 30) and name AI or ML
   teams (13 of 21). Period DevOps postings asked for both operations and programming backgrounds. On
   postings, AI work looks like a scarce new capability, not a merger of two functions (F-8, I3).
6. **The dated order runs from open tooling to vendor credentials to law.** Open agent tooling dates from
   2023-08-15, AI governance certification from 2024-03-05, agent-scoped certification from 2025-03-03,
   vendor role definitions from 2025, and binding deployer rules from 2027-01-01. The community date is
   missing (F-7, I5, I5c).
7. **Vendors split business accountability from technical control.** Entra defines sponsors (business
   accountability, no admin access) apart from owners (technical administrators). Vendors also rename
   agent products and credentials within about three years (I5; N24).
8. **Practitioner speech is not an earlier signal of roles built on agreements.** H-cal is refuted, so the
   speech findings are descriptive only (`calibration.md`).
9. **The DevOps-pattern test is undecidable by rule.** 10 of 15 scored features are insufficient. Power
   was 4–6% at about three years of evidence. On the three features that separate DevOps from the
   scarcity pattern, the evidence leans toward DevOps, below any threshold (F-8, `pattern-match/result.md`,
   `pattern-power-v4.md`).
10. **Where the evidence cannot reach.** 59% of frame employers have no crawlable board, including Alphabet,
    Apple, Meta, Microsoft, Amazon, Goldman Sachs, JPMorgan and most utilities (15% of utilities are
    covered). The firms that lead adoption are the least visible (`corpus-b/coverage.md`).

---

## 3. What changed and why

| | Round one | Rerun | Effect on conclusions |
| --- | --- | --- | --- |
| Source text | Search-engine summaries only; no page opened; every record grade S | Acquired full texts: 118,526 postings from 218 boards through ATS APIs; EDGAR full text; Whisper transcripts; rule texts read provision by provision | Details round one took from summaries fall away: the C9 accounting title, the R9692 and R8958 passages, Visa's rule terms, the guidance-versus-rule distinction in trading. Random-claim error rate in round one: 20% of checkable claims |
| Selection | Topic searches by people who held the hypotheses; postings found by searching for "agent", many through aggregators; five strata, 60 records each | A frame fixed in advance: 550 employers (Fortune 500 plus 50 software firms); every open posting on each discovered board; no topic search; round-one overlaps kept and counted | Round one's C1 (aggregator postings) and C7 (15 of 17 vendor docs) clusters were artefacts of selection. In a full crawl, rule work surfaces where controls language lives: security |
| Scale | 298 records | 25,512 postings selected, about 305,000 duty statements, 50,675 clustered; 862 speech spans; 2,216 filing passages; 111 provisions | Rates and ratios can be estimated (F-1, F-5). Small categories like PV and RD remain too sparse for anything but "near-absent" |
| Clustering | A fresh LLM clusterer per iteration as strata were added; failed stability | Embeddings with HDBSCAN; discovery and holdout halves; three-seed noise baseline; holdout ARI 0.83 | Stable bundles can be told from unstable ones. The governance and agentic clusters are "forming, not settled" |
| Coding | Two coders from one model; 85 of 298 notes identical; no seeds, so PV and RD sensitivity unknown | Sonnet and Haiku coders; seeded PV, PE and RD cases with recall gates (≥0.94); Opus adjudication and blind checks | PV and RD absence is no longer a possible coder blind spot (within the limit that seeds are cleaner than real text) |
| Blinding | Collectors and clusterers barred from the study vocabulary, but run by the team that held the hypotheses; industry scorers knew the history | Instruments and the findings writer did not open round one, the roles, the exploratory drafts or the report. Feature coders saw no pattern names. Verification ran after the findings were committed | The rerun's agreement with round one on rule-work rarity is independent. Its disagreements are not shaped by round one's framing |
| Instruments | Activity loop; calibration from memory-assisted lineages; industry scoring of 10 sectors | Six instruments: postings (I1), task clusters (I2), period postings (I3), rule texts (I4), vendors (I5), speech (I6); plus filings and blind pattern matching | Claims that rested on one study (industry scoring) now meet a second source (I4), which supports part and corrects part. The industry ranking itself was not re-run |
| Verification | none | 221 of 267 load-bearing claims confirmed; random 150 gives 20% errors (Wilson 13–29%) among the 95 checkable | The loop numbers are exact. The industry slice is the weakest part of round one (38 of 70 confirmed) |

**Rerun limits that matter for this comparison.** There is no historical board crawl (CDX was rate-limited),
so no title trends and no test of H4. The firms that lead adoption are not crawlable. Speech recall is about
0.5 and speech is descriptive only. I4's citation share, I5's comparison of vendor and posting wording and
I3's embedding comparison were not computed. California SB 53, Visa's rules and Mastercard's guide were not
acquired. The industry analogue was not rescored on Corpus B, so claims 13–16 rest on verification plus I4,
not on a rerun of that study.

---

## 4. Implications for the recommendation

`../recommendation-draft.md` was marked provisional: "the rerun keeps only what it supports". Taking its
positions in turn:

### Survive

- **Rule work is a duty, not a job** (§1, first bullet). Supported by I1, I2, I3 and I6. Change the
  evidence line from v1 clusters and the role library to Corpus B.
- **Don't hire one senior Business Protocol Lead to own all three layers** (§7). No posting for such a role
  exists. Lasting roles did not start senior. The council form exists, but it is not a single owner.
- **Don't build the third stage's machinery before its trigger** (§4). Practice runs years ahead of law
  (F-6, F-7). AI law, when it comes, asks for a designated overseer, not a change committee or certified
  designers.
- **Don't let vendor consoles hold your rules** (§7). The rerun strengthens the risk. Vendors define agent
  roles, registries and sponsor or owner splits, and relabel them within about three years (I5).
  Trading's "direct and exclusive control" requirement is binding (IN). The rerun does not test whether
  the alternative works better.

### Need revising

- **§1, "Outside rules are arriving through chokepoints."** Narrow this to Mastercard and Amazon, which are
  confirmed. Mark Visa as unverified. State that neither names an in-firm role. On finance templates, say
  which parts bind: CEO certification under 15c3-5, Series 57 registration, the RTS 6 designated person.
  The inventory, material change, named SMF and multi-function sign-off are guidance.
- **§1, "That silence is weak evidence."** Recast it as a limit of desk research, not as evidence. The
  calibration test failed (H-cal, H8).
- **§2 one-line recommendation and §3 "Designing rules" row.** The observed home of rule design is AI
  security review in the security function, plus governance roles reporting to compliance (I2, I3). It is
  not agent operations specialists, legal engineers, GTM engineers or accounting operations leads. Drop
  v1 clusters C1, C7 and C8 as evidence: they rest on aggregator postings, vendor docs and search
  summaries (LR).
- **§3 "Deciding changes" row and §4.** Councils, guilds and centres of excellence appear in practice (5 of
  34 speakers). Present the forum as an observed form whose decision rights are unknown. Outside trading,
  there is no evidence for "a named executive (usually the COO)" or for one who certifies agent controls
  yearly. Add Colorado SB26-189 (1 January 2027) beside the EU AI Act, and update the EU dates to 2
  December 2027 and 2 August 2028 under the Omnibus. Both require a designated person with authority to
  oversee or override. Neither requires a change owner or certification.
- **§4 "agent risk and control team under the COO, mid-level".** In the trading source this team is
  Director level under an existing global head (IN CL0210, CL0264). No agent-side evidence exists. Keep it
  only as a trading example.
- **§2–3 "one register".** Registries are arriving as vendor products run by IT admins (I5). Recommend
  that the firm own a cross-vendor register. Don't present the register as protocol-vision work that
  surfaces unwritten rules.
- **§5 by function.** Speech supports placing agent running inside functions, with existing staff given
  new duties (I6). Nothing shows those function leads own a hardness map or rule changes. Present this as
  a proposal, not a finding.
- **§9 predictions.** Keep them as open forecasts. Prediction 3 (a non-financial firm publishes an agent
  policy naming who may change agent limits) has no instance so far (H-agreement not supported). Add the
  rerun's five dated forecasts.

### No support in either round

- **A monthly exception review in each function that surfaces unwritten rules** (§3, §4 "Now"). PV is
  near-absent in postings and speech, and no speech span describes reviewing exceptions or overrides.
- **A mid-level analyst in the COO's office who keeps the register** (§3). Not observed. Only two COO
  items were in the speech frame, too few to code.
- **Time to amend as the measure** (§3, §4). Untestable from public records (H7). Speakers name
  interaction scores and agent containment, not amendment times.
- **Certified designers for every agent that touches regulated decisions** (§4). No AI rule requires them.
  Agent credentials are vendor product certifications.
- **A named executive who certifies agent controls each year** (§4). It exists only in US trading law
  (15c3-5).
- **The training path** (§6: watching, workshops, simulations). Not tested by either round.
- **"Don't frame it as AI safety"** and **"don't let the register become ceremony"** (§7). Both are
  reasoning from history, and neither round tested them. One fact cuts slightly the other way on framing:
  the only AI texts that name rule-change owners are AI labs' own safety policies (I4).

### The stake check (research design §10.3)

Does the case for Business Protocol Management rest on primary or read-in-full evidence? Not yet. The
positions that would favour BPM have no support from opened texts: a protocol-vision layer, a rule-decision
layer, time to amend, and the register as rule-finding. The positions that survive are the ones that run
against a single protocol role, and the warning about vendor control. A recommendation built only on what
survives is narrower:

- give rule design for agents an owner inside security and governance review, where it already forms;
- own a cross-vendor agent register rather than relying on vendor consoles;
- give the existing AI council written decision rights over agent rules that cross functions;
- meet the overseer duties of the EU AI Act and Colorado with named, trained people.

Field work (`field-plan-scaffold.md`) is the test of whether exception reviews and cross-function rule
decisions happen out of public view. Until then the recommendation should present PV and RD as hypotheses
to test inside firms, not as layers to build.
