# Field-research plan scaffold

Protocols for Business · 10 October 2026 · pre-registered: written and committed before any Corpus B
result, instrument output or feature coding was read · completes into `field-plan.md`
([`../../triangulation-design.md`](../../triangulation-design.md), section 9)

Written from the design files only: `triangulation-design.md` (with addenda A to A.4 and the reading rule),
`research-design.md` sections 3 to 5, `loop-design-v2.md` sections 3, 4, 6 and 8,
`loop-prompts/feature-coding.md`, this folder's `log.md` and `deviations.md`, and section 10 of
`signatures.md` (N20 to N24). No instrument, cluster, pattern-match, loop, industry, role-library,
exploratory, report or corpus file was opened. Nothing below may be changed after the first Corpus B
finding is committed, except by a dated addendum that says why.

## 0. How to use this scaffold

**Decision.** Field work tests the claims in section 1 against the refutation criteria in section 2. It
does not look for new hypotheses to support. Firms are named later, by the rule in section 3.2, from
public signals only.

Reasons:

- The desk design cannot settle these claims by construction (A.4, deviations 5, 10 and 11, research
  design section 11), so the field is the only test, not a confirmation step.
- If the field plan were written after desk results, the choice of firms, questions and thresholds could
  follow the results. Writing it now prevents that.

Order:

1. Commit this scaffold (before any desk result).
2. Commit the Corpus B findings (design section 7, step 4).
3. Run the candidate script (section 3.2) on Corpus B indices. Commit its code, seed and output before any
   firm is approached. Write `field-plan.md` from this scaffold and the candidate list.
4. Field work. Interviewers and field coders do not read Corpus B findings, signatures or this file's
   sections 1 and 2 until field coding is committed (section 6.1).
5. Field results are compared with desk results under section 6.4.

## 1. What field work must answer

**Decision.** Nine claims go to the field. For each, the desk contributes context and, in some cases, a
value to check, but none can be settled from public written sources.

Reasons:

- Postings say what employers want, filings what firms disclose, and speech how people describe their
  work. None is observed work (design section 10).
- Several desk measures failed their gates. Filing codes for reorganisation (kappa 0.52), metrics (0.58)
  and rule citation (0.39) are unreliable. Bodies and workforce passed kappa but are unverified (fewer
  than 5 positives in the clean check). The log concludes that F1 and F3 rest on speech and field work.
- A.4 has 4 to 6% power to call H-DevOps "supported" when it is true, so its expected verdict is
  "Inconclusive" under every truth.

### C1. The pattern verdict under A.4

- **Claim.** The present formation of agent work matches the DevOps pattern rather than the scarcity
  boom pattern, and rather than the other five patterns.
- **Desk will contribute.** The A.4 verdict, the secondary seven-way ranking, and two coders' values for
  all 21 features. Above all, the Stage 2 features: N15, N04a, N20, N21, N22, N23 (four after
  truncation: N15, N20, N21, N22).
- **Desk will not contribute.** A verdict that can be read either way. "Not supported" and
  "Inconclusive" are not evidence against H-DevOps. A.4 cannot tell a single pattern from a mixture.
- **Field evidence needed.** Firm-level values of the Stage 2 features observed inside firms. Who the
  first holders were and where they came from (N20). Where the work sits in the organisation (N21). Why
  people say the role exists (N22). How much of the work is operating a tool (N15). Also the features
  that point to rival patterns: whether a legal text sets the work (N11), whether one firm was copied
  (N09), and whether the work is only configuration in a platform team (N19).

### C2. N10: authority from an owned number

- **Claim.** The person or team that changes what agents may do gets the right to decide from a number it
  owns (an accuracy, error, escalation or containment target). Linked to loop v2's H-number: the agent
  operations bundle lasts only where its holder owns a number.
- **Desk will contribute.** Mentions of measures in posting duties (`duties_text`) and in speech
  (`measure_named`). N10 is coded but not scored (A.2 point 3).
- **Desk will not contribute.** Whether the number decides anything. A posting can list a metric that no
  one uses to allow or refuse a change.
- **Field evidence needed.** Recent changes to agent permissions, and whether a number set in advance was
  the reason a change was made, refused or escalated. Who set the number. Whether the holder can act
  inside it without asking.

### C3. F1: reorganisation around agents

- **Claim.** Firms join business and engineering functions around agents (phase-change claim, design
  section 2).
- **Desk will contribute.** Speech accounts (I6) and the filing code `reorg`, which is unreliable and not
  used for F1.
- **Desk will not contribute.** Whether a reorganisation happened, as opposed to being described, and
  whether it changed reporting lines, budgets or team membership.
- **Field evidence needed.** Organisation charts before and after agent deployment, internal
  announcements, and team rosters showing staff from business and engineering functions in one unit or
  reporting line.

### C4. F3: new operating metrics

- **Claim.** Firms adopt new operating metrics for agent work. Under H-DevOps these come from
  practitioners rather than regulators or vendors (D5, N05).
- **Desk will contribute.** `measure_named` and `measure_origin` in speech; the filing code `metric`, which
  is unreliable and not used for F3.
- **Desk will not contribute.** Whether the metric is reviewed, by whom, and whether it changes decisions.
- **Field evidence needed.** Dashboards and recurring review agendas showing which agent metrics are
  reviewed, by whom, how often, where the definition came from (own team, vendor default, regulator,
  industry group), and whether a change followed.

### C5. N20, N22 and N23: the interpretive features

- **Claim.** The first holders were mostly existing staff given new or added titles (N20). The stated
  purpose of the work is coordinating existing functions rather than supplying a scarce capability
  (N22). Early accounts frame it as a change in ways of working rather than a new technique (N23). These
  are the features on which DevOps (yes, yes, yes) and the scarcity boom (no, no, partial) differ most.
- **Desk will contribute.** Two coders' values from posting titles, requirements and purpose statements,
  and from speakers' paths and framing quotes. A.1 point 4 fixed their definitions.
- **Desk will not contribute.** A check that the coded wording reflects what happened. A posting may ask
  for outside experience and then be filled by an insider. A purpose statement may be marketing copy.
  N23 is subject to the truncation rule and may be "insufficient".
- **Field evidence needed.** For N20, the actual career paths of the first holders in each firm. For
  N22, why managers say the role was created, and what it would cost to remove it. For N23 (adapted),
  how the work was first presented internally. This is a different construct from early public talks
  and is reported apart (section 6.2).

### C6. H7: time to amend

- **Claim.** Time to amend can be measured from existing records and differs between firms with and
  without an owner (research design H7).
- **Desk will contribute.** Nothing measurable. Published rule-change events (S6) and speakers' accounts
  give anecdotes, not durations with a denominator.
- **Desk will not contribute.** Any duration. The internal records are not public.
- **Field evidence needed.** Change logs for agent permissions, override and escalation reports, and
  decision records, measured under the protocol in section 5.2.

### C7. The RD layer: decisions on rule changes across functions

- **Claim.** Some people decide to change, keep or retire agent rules where two or more functions are
  involved or a trade-off is stated (code RD). This work is present and is not only engineering
  configuration (against rival R1) or no one's work (against R4). Linked to H-speech and H-federated.
- **Desk will contribute.** RD and PV shares in postings and speech, and the clustering of PE and RD
  records.
- **Desk will not contribute.** Decisions that are never written publicly. H8 predicts that desk sources
  miss them. Speech shows how people describe decisions, not how they were taken.
- **Field evidence needed.** Critical-incident accounts of recent rule changes (who raised it, who was
  consulted, who decided, which trade-off was weighed), checked against the change record.

### C8. Who holds rule-change decisions in practice

- **Claim.** In most firms deploying agents, decisions about agent rules sit inside existing roles
  (H3, absorption). Where a firm names an owner in writing, that person takes the decisions in
  practice (H-agreement, extended to practice). The rivals must be tested equally: R1, platform
  engineering decides; R2, privacy or compliance decides; R3, an agent operations team decides; and
  committees (F2) decide rather than only discuss.
- **Desk will contribute.** Titles and duties in postings, published agent policies that name who may
  change them (H-agreement, S6), vendor role definitions (I5: steward, asset owner, agent owner), and the
  filing code `body` (unverified).
- **Desk will not contribute.** Whether the named person or body actually decides. It cannot see the
  difference between the written and the actual decision holder.
- **Field evidence needed.** For each recent change episode, the person or body that decided, compared
  with the one named in policy. The category of decision holder (section 6.2). Whether committees took
  any decision in the window.

### C9. H8: desk sources miss agreement-based authority

- **Claim.** Public written sources detect roles that operate a new tool, and miss roles whose authority
  comes from an internal agreement on a trade-off until the agreement is published.
- **Desk will contribute.** Each visited firm's public written record (postings, filings, published
  policies, vendor case studies) as Corpus B captured it.
- **Desk will not contribute.** What it missed. Only the field can show that.
- **Field evidence needed.** For each firm, whether an internal agreement on who decides agent rule
  changes exists, its date, and whether the same arrangement appears in that firm's public record.

## 2. Refutation criteria

**Decision.** Each claim has a stated result that counts against it, fixed now. Thresholds are counts of
firms in the 16-firm adopter sample (section 3.3), unless stated. "Firm value" means the value both field
coders agree on after reconciliation (section 6.1).

Reasons:

- The sample is chosen by strata, not at random from all firms. Shares in it are not prevalence
  estimates. Thresholds are set as counts so that a result says what happened in these firms, not in the
  population.
- The 60% and 40% cut-offs repeat loop v2 section 9, so desk and field use the same language.
- A claim with no counting-against result cannot be tested; every claim has one below.

| Claim | Counts against the claim | Counts for it |
| --- | --- | --- |
| **C1** pattern | **Against DevOps, for scarcity boom:** in 10 or more of 16 firms (60%), first holders were hired from outside for a skill the firm lacked (N20 no), *and* the stated purpose is a new capability (N22 no). **Against DevOps, for another rival:** in 10 or more firms, the work is mainly operating one product (N15 yes; tool-operator), or changes are authorised by citing a legal text (N11 yes or partial; mandated officer), or no person or team is named and agent rules are changed only as configuration by platform engineering (N19 yes; engineering absorption). **Against DevOps on placement:** in 10 or more firms, the work sits in research, analytics or data-science units (N21 no) | N20, N21 and N22 coded yes in 10 or more firms, and N15 coded no in 10 or more |
| **C2** N10 | Among firms with a named holder, in 60% or more, no number set in advance is cited as the reason a change was made or refused, in either the interviews or the change records. Also against: numbers exist but are set and changed by someone other than the holder | In half or more of recorded change episodes, a number set in advance is cited as the reason, and the holder set it or agreed it |
| **C3** F1 | 2 or fewer of 16 firms show, in a document, a reorganisation that put business and engineering staff in one unit or reporting line around agents | 6 or more firms show it in a document. Between 3 and 5 is reported as mixed |
| **C4** F3 | 2 or fewer firms review an agent-specific operating metric in a recurring meeting with power to change something. Also counts against D5 (practitioner origin): in 60% or more of firms with such a metric, it is a vendor default or a regulator's measure | 6 or more firms review one, and in most of them the definition came from the firm's own staff or a practitioner group |
| **C5** N20, N22, N23 | For each feature: the field value differs from the desk consensus value by a full step (yes against no). The desk value for that feature is then reported as not confirmed in the field. Half a step is "partly consistent" | Field value equal to the desk value |
| **C6** H7 | **Measurability:** in fewer than half of the firms that keep a change log for agent permissions, the records yield 5 or more episodes with t0 and t1 both dated (section 5.2). **Difference:** the median time to amend in owner firms is not shorter than in no-owner firms, or the difference is smaller than the coders' dating disagreement. No difference claim is made with fewer than 6 measurable firms per arm | Measurable in half or more of the firms with logs, and the owner arm's median is shorter by more than the dating disagreement, with 6 or more firms per arm |
| **C7** RD | RD records are under 2% of coded activity mentions from the changer, manager and risk roles, *and* in 80% or more of recorded change episodes one function decided without naming another function or a trade-off. Absence is interpretable only if coder recall on RD speech seeds is 0.7 or more with a Wilson 95% lower bound of 0.5 or more (deviation 6) | RD in 5% or more of mentions, and at least one cross-function decision episode in 10 or more firms |
| **C8** who holds | **Against absorption (H3):** a role whose primary duty (more than half its work) is deciding agent rules holds the decisions in half or more of incumbent firms. **Against "the named owner decides":** in 60% or more of firms with a written owner, most recorded episodes were decided by someone else. **Against F2 as decision bodies:** in 60% or more of firms with a standing committee, no episode in the window was decided there. **For each rival R1–R3:** that category holds the decisions in 10 or more firms | Existing roles hold the decisions in most firms; written owners decide most of their episodes |
| **C9** H8 | In 60% or more of firms where the field finds an internal agreement on who decides, the same arrangement was visible in that firm's public record before the visit | Visible in 20% or fewer such firms |

Cases that fit neither column are reported as mixed, with the firm counts.

## 3. Firm selection

### 3.1 Criteria and strata

**Decision.** There are two types of firm: 16 adopters and 4 vendors. Adopters are crossed on two
binary strata (software-native or incumbent; regulated or not) to give four cells of four. Within each
cell, two firms have a public owner signal and two do not. Every adopter must meet the heavy-use bar. All
strata are computed by script from public signals, defined here.

Reasons:

- The adopter strata are those the hypotheses predict will differ. H3 predicts distinct roles in
  software-native firms. D6 and N06a predict diffusion from software-native firms to incumbents to
  regulated sectors. The mandated-officer rival predicts the work forms in regulated firms first.
- Requiring heavy use in every firm means a firm without an owner is a real disconfirming case (use
  without a new role), not a firm that has nothing to own.
- Vendors are a separate type, because they write the role definitions that I5 dates. They are asked
  whether their definitions came from customers' practice or preceded it (D3, N24). Their own internal
  use is recorded, but not pooled with adopters.

Definitions (each from public signals, with the source fixed):

| Stratum | Definition | Source |
| --- | --- | --- |
| **Adopter vs vendor** | Vendor: sells a product whose documentation defines roles for building, running or controlling AI agents (a row in `I5-vendor-roles.csv`), or SIC 7370–7374 with 50% or more of its agent-term filing passages coded `product`. Adopter: everyone else meeting the heavy-use bar | I5 vendor-roles index; `corpus-b/filings-index.csv`; passage codes |
| **Software-native vs incumbent** | Software-native: SIC 3570–3579, 3670–3679 or 7370–7379, or a frame employer of type venture-backed software (the rule in A.2 point 6). Incumbent: all others | `filings-index.csv`, `software_native`; S1 frame |
| **Regulated vs not** | Regulated: primary SIC in banking, credit, securities or insurance (6000–6411), health services or health insurance (8000–8099, 6324), or electric, gas and water utilities (4900–4991). These are sectors with a prudential or sector supervisor whose rules reach automated decisions or operational risk | EDGAR SIC |
| **Heavy agent use** (required of all adopters) | At least two public signals of the firm's own use of agents in production, from two different source types: (a) a filing passage coded `own_use` that names agents (one of the six filing phrases); (b) an I6 speech record with `in_company_agent_work` = yes, by a speaker employed by the firm; (c) a vendor case study naming the firm as a customer running agents; (d) three or more postings with `agent_duty` = yes | Corpus B indices |
| **Functions using agents** | The functions named in the heavy-use signals: customer support, finance and procurement, sales and revenue operations, IT and security operations, HR, software engineering, other. Recorded per firm. The function with the most signals is the primary function | Same signals |
| **Owner signal** | Public evidence that a named role holds agent rules: a posting with `agent_title` = yes, or an AI steward, agent owner or AI governance title; a published policy that names who may change the firm's agent rules (H-agreement); or a filing passage coded `body` naming a body with decision rights over agents. No individual is named or searched | I1 postings; S6 events; filing codes |

Function spread. Across the 16 adopters, at least three functions must be primary in two or more firms
each, and no function may be primary in more than six.

Reasons: the RD claim is about decisions across functions, and H-federated predicts that rule design
stays inside each function. A sample dominated by support desks would test neither.

### 3.2 Rule for naming candidates later

**Decision.** Candidates are drawn by script, at random within cells, from a pool built only from the
stratum signals above. Nothing about a firm's coded features or the desk findings enters the draw.
Disconfirming cells are filled first and cannot be dropped.

1. **Pool.** The 550 frame employers, plus any employer named in an I6 speech row or an I5 customer row,
   with origin recorded. Each firm gets the five stratum values by script.
2. **Inputs the script may read.** Only the columns named in 3.1. It may not read N-codes, `I2`
   clusters, `pattern-match/`, any `findings*.md`, round-one citations, or the group's contact lists.
3. **Exclusions, fixed now.**
   - Current or prospective advisory clients of the group, and employers of group members. They may give
     the two pilot interviews (section 4.4), which are not counted.
   - Firms with fewer than 500 employees, where the four roles in section 4.1 are often one person.
   - Excluded firms are listed with the reason.
4. **Draw.** Within each of the eight subcells (four adopter cells × owner signal yes or no) and the
   vendor list, sort candidates by a random permutation with seed **20261020**. Commit the script, seed
   and ordered list before the first approach.
5. **Approach.** Approach firms in list order. A firm that declines, or cannot provide the changer role,
   is replaced by the next firm in the same subcell. Every approach and outcome is logged in
   `field/approaches.csv` (firm pseudonym, subcell, date, outcome). No reasons are given to firms about
   which subcell they are in.
6. **Gaps.** If a subcell is not filled after 12 approaches, it is reported as a gap. It is not filled
   from another subcell, and no firm is added because it looks promising.
7. **Disconfirming cases, required.**
   - The four no-owner subcells contain firms with heavy agent use and no new title. They are filled
     first.
   - The two regulated cells (eight firms) are required. If either is unfilled, the report says the
     mandated-officer rival was not tested in the field.
8. **Warm introductions.** Allowed only for a firm already on the ordered list, and only when it is next
   in turn. An introduction never moves a firm up the list.
9. **Function spread.** If the spread rule in 3.1 fails after drawing, the last firm drawn in the
   over-represented function is replaced by the next firm in its subcell whose primary function is under-
   represented. This is the only reordering allowed, and it is logged.

Reasons:

- Selection on the outcome is the main risk. Naming firms that are known to have stewards, or are vocal
  about agents, would select for the hypothesis.
- Random order within strata, a fixed seed committed before contact, and a logged replacement rule make
  the selection checkable.
- The owner signal is a stratum, not a preference: half the adopters have none.

### 3.3 Sample size per stratum

**Decision.** 20 firms: 16 adopters (4 per cell, 2 with and 2 without an owner signal) and 4 vendors (2
software-native platform vendors, 2 incumbents selling agent products). Four interviews per firm (section
4.1), 80 interviews in all, plus two pilot interviews that are not counted.

Reasons:

- **H7 needs two arms.** The owner signal splits adopters 8 against 8. Section 2 requires at least 6
  measurable firms per arm before any difference is reported, which leaves room for two firms per arm
  whose records fail.
- **Each cell needs a disconfirming case to be visible.** With four firms per cell, one firm that differs
  can be seen, and a cell-level pattern rests on more than one firm.
- **Thematic saturation.** Interview studies with a fixed guide reach most codes within about 12
  interviews in a fairly uniform group. Each role across 20 firms gives 20 interviews per role, and each
  cell gives 16 interviews.
- **Cost.** About two site days per firm, and artefact extraction on site, are what the group can carry
  across one quarter.
- **Limit, stated now.** Twenty firms cannot estimate prevalence. They test whether the pre-stated
  arrangements exist, where decisions sit, and whether desk codes match practice. Shares are reported as
  counts.

## 4. Interview guide skeleton

### 4.1 Roles to interview

**Decision.** Four roles per firm, interviewed one at a time and in this order, so that later interviews
can check what earlier ones said about the same episodes.

| Code | Role | Why |
| --- | --- | --- |
| **R-A** | The person who changes what an agent is permitted to do: edits its permissions, limits, approval steps or escalation conditions in the system | Closest to the actual changes; source for episodes, H7 triggers, N15, N20 |
| **R-B** | R-A's manager | Why the role exists (N22), how it was created (N20), reporting line (N21, F1), measures (F3), who settles disputes (C8) |
| **R-C** | The risk, compliance, security or legal counterpart consulted on agent changes, if any | Whether they can block, which texts they cite (N11), whether a committee decides (F2) |
| **R-D** | A front-line user who works alongside the agent | Overrides and workarounds as they occur (PV, H7 trigger), whether reporting leads to change |

If a firm has no R-C, record that as data. If R-A and R-B are the same person, record that and interview
the person to whom they report.

Reasons:

- Each claim needs at least two viewpoints. The changer and the manager can disagree about who decides
  (C8), and the front-line user tests whether reported overrides reach anyone (C6, C7).
- R-A is the anchor. Recruiting starts with "the person who changes what the tool is allowed to do", not
  with a title, so firms with no title are not filtered out.

### 4.2 Wording rules

**Decision.** Interviewers use plain words about work, tools and changes. The study's vocabulary and the
feature definitions are never spoken first.

- **Never introduce:** protocol, governance, rule owner or owner, steward, accountability, operating
  model, culture, coordination, scarce, phase change, DevOps, or any pattern or role name from the
  design. If an interviewee uses one of these words, the interviewer may repeat it and ask what they mean.
- **Say instead:** "what the tool is allowed to do", "settings", "limits", "approvals", "when it hands
  over to a person", "a change".
- **Agent**, defined once at the start: "software that takes actions on its own, such as sending,
  approving, changing a record or paying, not only suggesting".
- **Ask for episodes, not opinions:** "the last time", "walk me through", "when was that", "who
  exactly", "is there a record of it".
- **No double-barrelled or yes-no openers.** Probes follow the interviewee's words.

Reasons: the interpretive features (N20, N22, N23) are coded from how people describe their work. If the
interviewer supplies the framing, the coding measures the interviewer.

### 4.3 Questions and probes

Claim tags in brackets are for the analyst. They are removed from the interviewer's copy.

**Opening (all roles)**

1. "Tell me about your job, and how it has changed in the last two years."
2. "In your area, which tasks are now done or started by software that acts on its own?"
   - Probe: "Since when? What did it replace?"

**R-A: the person who makes changes**

3. "Walk me through the last time you changed what one of these tools is allowed to do." [C6, C7, C8]
   - Probes: "What started it? When did you first hear about it? Who else was involved? Who said yes?
     When was it done? Is there a record?"
4. "Tell me about a time a change was asked for and didn't happen." [C7, C8, C6 open cases]
   - Probe: "Who decided not to? Is it still open?"
5. "How do you find out that a setting isn't working: people going around it, the tool being stopped, or
   complaints?" [C6 trigger, PV]
   - Probe: "How many times before you act? Is that written down?"
6. "Which changes can you make without asking anyone? Which need someone else's agreement, and whose?"
   [C8, C2]
7. "Is any of that written down? Could I see it?" [C8, C9, artefacts]
8. "Are there any figures you watch that would make you change a setting, or stop you changing one?"
   [C2, C4]
   - Probes: "Who chose the figure, and the level? Where did the definition come from? Has a figure ever
     settled a disagreement?"
9. "How did you come to do this work? What were you doing before, here or elsewhere? What was your title
   then?" [C5 N20]
10. "Of a normal week, how much is spent inside the tool, and how much with other teams?" [C1 N15]
11. "Has there been a time when two teams wanted different things from the tool? What happened?" [C7]
12. "Did you look at how any other company did this before setting it up here?" [C1 N09]

**R-B: the manager**

13. "Why does [R-A's] job exist? If it disappeared tomorrow, what would happen?" [C5 N22]
14. "How was the job filled at first: someone moved from inside, or hired from outside? What background
    did you look for?" [C5 N20, N12]
15. "Where does this work sit in the organisation, and has that changed since the tool came in? Is there
    a chart from before and after?" [C3 F1, C1 N21]
16. "When the tool was first brought in here, how was it described to staff? What did leaders say it was
    for?" [C5 N23, adapted]
17. "What figures do you review about this work, how often, and with whom? When did a figure last lead to a
    change?" [C4, C2]
18. "When teams disagree about what the tool should be allowed to do, who settles it?" [C8, C7]
19. "Is there a group or regular meeting where these questions go? What does it decide, and what does it
    only discuss?" [C8 F2]

**R-C: the risk, compliance, security or legal counterpart**

20. "When are you brought in on changes to what the tool may do? Can you stop a change?" [C8]
21. "Walk me through the last change you reviewed." [C6, C7]
    - Probe: "What did you weigh up? Who decided in the end?"
22. "Is any of this required by a law, a regulator or a contract? Which text?" [C1 N11]
23. "What do you receive about the tool's errors, overrides or incidents, and what happens to it?" [C6]

**R-D: the front-line user**

24. "Tell me about the last time the tool did something you had to undo or stop." [C6 trigger, PV]
    - Probes: "What did you do? Whom did you tell? Did anything change afterwards, and when?"
25. "Are there things you do to get around what the tool will or won't do?" [C6, PV]
26. "If you think the tool should be allowed to do more, or less, whom would you ask?" [C8]

**Closing (all roles)**

27. "Is there anything about how these decisions are made here that I should have asked about?"
28. "Who else should I talk to?" Snowball within the firm only. It is not used to add firms.

### 4.4 Pilot and conduct

- Two pilot interviews in excluded firms (3.2, point 3) test timing (60 minutes per interview) and
  wording. Changes after the pilot are logged in `field/guide-changes.md` before the first counted
  interview. No changes are made afterwards.
- Interviews are recorded only with consent. Otherwise the interviewer takes notes, which are typed up
  within 24 hours.
- Interviewers record every date the interviewee gives, because most features need dates.

## 5. Artefacts to request

### 5.1 The request

**Decision.** Each adopter firm is asked for five kinds of record, covering the 12 months before the visit
(or since agents were first deployed, if that is shorter). The researcher extracts the fields below on
site, or the firm extracts them using the study's template. No raw document leaves the firm unless the
firm chooses to share a redacted copy.

| Artefact | Fields extracted | Claims |
| --- | --- | --- |
| Change log for agent permissions, limits, approval steps and escalation conditions (system audit log, ticket queue or configuration history) | Rule category, function, date requested, date decided, date deployed, decision (change, keep, retire), role of requester and decider (role, not name), functions named | C6, C7, C8 |
| Approval policy or written description of who may change what | Date, roles named, whether a role is named as decider, whether a figure is set | C2, C8, C9 |
| Incident reviews involving an agent | Date, rule involved, decision taken, functions involved, time from incident to decision | C6, C7 |
| Override, escalation and exception reports | Counts per rule per week or month, threshold if any, who receives the report | C6, C4 |
| Organisation charts or announcements, before and after agent deployment | Units, reporting lines, team composition by function | C3, C1 N21 |
| Metric definitions and review agendas (if they exist) | Metric, owner role, origin of definition, review cadence, decisions recorded | C4, C2 |

Reasons:

- Interviews give accounts. Records give dates and counts that can be checked across firms.
- Extracting fields rather than taking documents keeps personal and confidential data out of the study
  (section 7).

### 5.2 Time-to-amend measurement protocol (H7)

**Decision.** Time to amend is measured per rule episode, in calendar days, from a study-defined trigger
to a recorded decision. Open episodes are counted as censored, not dropped.

Definitions:

- **Rule.** A setting that limits what an agent may do and that people other than the setter rely on: a
  permission, a spending or approval limit, an approval step, an escalation or hand-over condition, a list
  of things the agent must not answer, or data the agent may use (the PE scope in loop v2 section 6).
  Prompts, content and tests are not rules (boundary rule, loop v2 section 6).
- **Signal.** A dated record that the rule was in the way or failed: (a) an *override*, where a person
  reversed, blocked or stopped an agent action; (b) an *escalation*, where the agent or a person passed a
  case up because the rule did not allow it; (c) an *exception*, an approved one-off departure from the
  rule; (d) a *workaround*, a recorded action outside the rule to get the work done (from tickets or
  reports, not recollection); (e) an *incident* tied to the rule. Each signal is linked to one rule.
- **Threshold, study definition (primary).** The rule crosses the threshold on the date of its third
  signal within any rolling 30-day window. This is **t0**. One definition for all firms keeps episodes
  comparable.
- **Threshold, firm definition (secondary).** If the firm has its own written threshold for review, t0
  under that definition is also recorded and reported separately.
- **Decision, t1.** The date of the first recorded decision to change, keep or retire the rule, after t0:
  a dated ticket resolution stating the decision, a change-log entry, minutes, or an approval record. A
  decision to keep counts as a decision.
- **Inferred decision.** A change deployed with no separate decision record takes its deployment date as
  t1 and is flagged "inferred". Results are reported with and without inferred decisions.
- **Time to amend.** t1 − t0 in calendar days.
- **Open episodes.** An episode with t0 and no t1 by the extraction date is censored at that date.
- **Exclusions, recorded separately.** Changes made because of a vendor release with no prior signal.
  Emergency stops, which have their own time from first signal to stop. Rules created during the window,
  until 30 days after creation.
- **Unit and summary.** Rule episodes, grouped by firm. Per firm: number of episodes, Kaplan–Meier median
  time to amend counting open episodes, and share of episodes still open at 30 and 90 days. Between arms:
  the median of firm medians, so that one firm with many episodes does not dominate.
- **Arms.** "Owner" is decided from field evidence, not the desk signal: a named person or body whose
  written duties include deciding changes to agent rules, *and* who decided most of the firm's recorded
  episodes. "Written owner only" (named on paper, decided few episodes) is reported as a third group.
- **Measurability.** A firm is measurable if it yields 5 or more episodes with dated t0 and t1, or with t0
  and censoring.
- **Reliability.** For 20% of firms (at least four, one per adopter cell), a second researcher identifies
  episodes and dates from the same extracted records, without seeing the first. Report agreement on
  episode identification (kappa) and the median absolute difference in t0 and t1. That difference is the
  dating error used in section 2.
- **Direction stated now.** Owner firms have the shorter median. No significance test is confirmatory at
  this sample size. The result is reported as firm-level medians, with the dating error.

Reasons:

- H7 names overrides or workarounds crossing a threshold, and asks that open cases count. Without a
  common threshold, firms with no threshold could not be measured at all, and firms with lax thresholds
  would look fast.
- Firm-level summaries stop a firm with many episodes from setting the result.
- Defining the arms from field evidence avoids circularity with the desk owner signal used for selection.

## 6. Analysis plan

### 6.1 Coding, coders and blinding

**Decision.** Two human coders code every interview. Each works independently from pseudonymised
transcripts, using the loop v2 codebook for activity records and the feature definitions in
`feature-coding.md` for firm-level features. Neither has seen this file's sections 1 and 2, the
signatures, the pattern names, or any desk result before field coding is committed.

1. **Records.** Each transcript is cut into records, one per activity the speaker says they or their team
   do, with a timestamp, `speaker_relation` (self, own team, other team, general claim) and
   `performer_type` (person, agent, both), as in loop v2 section 5. General claims are kept but not counted
   as evidence of practice.
2. **Activity codes.** PV, PE, RD, AO and OT, as loop v2 section 6, with its boundary rule. Up to two codes
   per record.
3. **Calibration.** Before field coding, each coder codes the speech seeds from seeds v3 (held outside
   git, key hash in `log.md`). Recall and the Wilson lower bound are reported per code. An absence of PV
   or RD is interpretable only under deviation 6 (recall 0.7 or more, Wilson lower bound 0.5 or more).
4. **Agreement.** Cohen's kappa per code on all records. The gate is 0.6, as for the filing codes. A code
   below the gate is reported as unreliable and not used for refutation. Disagreements are then resolved
   by discussion. Raw and resolved codes are both kept.
5. **Firm-level features.** Each coder reads the firm's records and extracted artefacts, and codes each
   field-applicable feature yes, partial, no or insufficient, with evidence (record or artefact row,
   date, quote of 40 words or fewer). The disagreement rate is reported per feature.
6. **Model coder.** A model may code the same records as a third coder, for comparison only. It does not
   enter field values. It shows how far the desk's model coders differ from people on the same text
   (deviation 5: field work is the human check).

Reasons:

- Using the same definitions as the desk is what makes the field a test of the desk codes, rather than
  a separate study.
- Two human coders give the human check that the desk replaced with model checks.
- Blinding the coders to pattern names repeats the protection in design section 6.2.

### 6.2 Features in the field

| Answerable from the field (per firm) | Not answerable (market-level timing or counts; desk only) |
| --- | --- |
| N02 merged duties; N05 measure origin; N09 copied from another firm; N10 owned number; N11 legal text; N12 seniority of first holders; N15 tool operation; N19 absorption with no title, team or measure; N20 first holders; N21 organisational home; N22 stated purpose; N23f (adapted: how the work was first presented inside the firm) | N01, N03, N04a, N06a, N07, N08, N13, N14, N24 |

Additional firm-level codes, each defined in 5.2 or section 2:

- **Decision-holder category** for each episode: distinct role (primary duty), existing role, platform or
  engineering team (R1), privacy, compliance or legal (R2), agent operations team (R3), committee (F2), or
  not identifiable.
- **F1** (documented reorganisation), **F3** (reviewed agent metric) and its origin.
- **Public visibility** (C9): whether the firm's internal arrangement appears in its public record.
  Coded last, by one coder who then opens that firm's Corpus B rows only.

N23f is a different construct from N23 (early public talks). It is reported beside N23 and never
substituted for it.

### 6.3 Aggregating across firms

- A feature is **yes** for a stratum or the sample if 60% or more of its firms are yes, **no** if 60% or
  more are no, and **mixed** otherwise. Firms coded insufficient are excluded from the denominator, and
  their number is reported.
- **Field head-to-head (C1).** Apply A.3's Stage 2 statistic to the field values of N15, N20, N21 and N22
  (the truncated set), aggregated over the 16 adopters as above: +1 per feature closer to DevOps, −1 per
  feature closer to the scarcity pattern, 0 if tied, per coder, then averaged. Use k = 3 from A.3.
  Reported as a conditional, small-sample field result. It is never merged into the A.4 score.
- Every result is reported by stratum (software-native or incumbent, regulated or not, owner signal or
  not) as counts. Vendors are reported apart.

### 6.4 How field evidence updates each desk verdict

**Decision.** The pre-registered desk verdicts are never re-scored. Field results are reported next to
them, with one of four labels, under rules fixed now.

| Label | When |
| --- | --- |
| **Confirmed in field** | The field value or verdict matches the desk's, under section 2 |
| **Contradicted in field** | Section 2's counting-against result holds where the desk said otherwise |
| **Field only** | The desk value is "insufficient", unreliable or absent (F1, F3, N10 when not stated, H7, internal RD) |
| **Not tested in field** | Market-level features (6.2), or a stratum left as a gap (3.2) |

Rules by claim:

- **C1 pattern.** The A.4 verdict stands as published. The field head-to-head is reported beside the
  desk Stage 2 head-to-head. If both favour the same pattern, the report may say "desk and field favour
  …", with both powers stated. If they disagree, the claim is reported as contested.
- **C2, C3, C4, C6.** The desk cannot settle these, so the field result is the result, labelled "field
  only" and limited to the visited firms.
- **C5.** The desk value is reported with its field check. A full-step contradiction marks the desk
  coding of that feature as not confirmed. The A.4 score is not recomputed, but the report says the
  feature that drove it was contradicted.
- **C7, C8.** For what firms do internally, the field governs. For what firms say publicly, the desk
  governs. Where they differ, both are reported, and the difference counts as evidence for H8 (C9).
- **Comparison grid** (design section 7.6). Field work enters as one instrument with its own data. A
  finding supported by three or more instruments, field included, is "strong". A finding supported only
  in the field is "field only", not "single-instrument desk".

Reasons:

- Re-scoring the desk verdict with field data would break the pre-registration and mix two samples.
- Fixing in advance which source governs which kind of claim stops the analyst choosing the more
  convenient source afterwards.

## 7. Ethics and data handling

**Decision.** Written informed consent from every interviewee and from the firm. No personal data and no
raw firm documents in the repository. Firms and people are pseudonymised, and the key is kept outside
git.

- **Review.** Before the first approach, the protocol, consent form and data plan are reviewed by a
  research ethics board at a member's institution. If none can host the review, an independent reviewer
  outside the group does it. The review is recorded in `field/ethics.md`, which contains no names.
- **Consent.** The form states:
  - who runs the study, and that the group also offers advisory services and develops a management
    practice in this area (the stake);
  - that taking part is voluntary, and refusing has no effect on any dealings with the group;
  - what is recorded and how it is used;
  - that the firm will not be named without its written agreement;
  - that a participant can withdraw until the analysis lock date stated on the form.
  The hypotheses are not described before the interview. A plain-language debrief is given afterwards.
- **Firm consent** covers access to the artefacts. Each interviewee consents separately. A manager's
  consent never stands in for an employee's.
- **No sales contact.** The group makes no commercial approach to a participating firm for 12 months
  after its last interview. Field staff are not involved in advisory work with these firms.
- **Pseudonyms.** Firms are F01–F20 and people F01-RA, F01-RB, and so on. The key linking pseudonyms to
  firms and people is held by one designated researcher, in encrypted storage outside the repository, and
  never committed.
- **Not in the repository:** recordings, full transcripts, interviewee names or contact details, firm
  names, raw artefacts, and any approach list that names firms. `field/raw/` is git-ignored, as
  `sources-v2/transcripts/` is.
- **In the repository:** pseudonymised coded records, with quotes of 40 words or fewer edited to remove
  names, products and places that identify the firm; firm-level feature codes; and the H7 episode table,
  with durations and month of t0 only, not exact dates.
- **Personal data in artefacts.** Change logs and incident reviews name staff and sometimes customers.
  Only roles are extracted (5.1). Customer data is never extracted.
- **Storage and retention.** Recordings are deleted once the transcript is checked, within 30 days.
  Pseudonymised transcripts are kept in encrypted storage until 24 months after the report, then deleted.
  Interviewees in the EU or UK are handled on the basis of consent under the GDPR, with the right of
  access and erasure until the lock date.
- **Re-identification.** Published tables show no combination of strata with fewer than three firms.
  Vendors, which are few and visible, are described only as a group.
- **Candidate list.** The ordered candidate list (3.2) names firms, because they come from public
  signals. It is committed before contact, as the design requires. Approach outcomes against it are
  committed only as pseudonyms and subcell counts, so that the public record does not show which named
  firm took part.

Reasons:

- The group has a commercial stake. Participants must know it, and the study must not become a sales
  channel.
- Change records and interviews about errors can expose individuals. Extracting roles and dates, not
  documents, keeps that risk out of the study.
