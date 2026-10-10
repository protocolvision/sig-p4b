# Is Business Protocol Management the institutional expression of the AI safety movement?

Research draft · 10 October 2026 · Protocols for Business · companion to
[`role-emergence.md`](role-emergence.md), [`business-protocol-lead-critique.md`](business-protocol-lead-critique.md)
and [`predicting-roles.md`](predicting-roles.md)

> **Status.** Exploratory. Sources were found through web search; the pages themselves could not be opened
> from this environment. (S) means a search result supported the point; (M) means from memory; [seen] marks
> a quotation that appeared verbatim in a search result. Check every quotation against the original before
> publishing.

## Summary

**The problem.** The Silicon Valley AI safety movement has built institutions in three places: inside the
frontier labs (scaling policies, safety teams, a Responsible Scaling Officer), in governments (safety
institutes, California's SB 53) and in standards (NIST AI RMF, ISO/IEC 42001). It has built almost nothing
inside the ordinary companies that deploy agents. There, AI governance is mostly an added duty of privacy
and legal teams. Whoever fills that gap will decide what "safe agents" means in day-to-day operations,
because firms, not lawmakers, usually define what compliance means in practice.

**The test.** Social movements have become offices inside firms before: industrial safety, quality,
environment, privacy, civil rights, content moderation. From that record we drew seven conditions and
scored Business Protocol Management (BPM) against each.

| Condition | Result |
| --- | --- |
| 1. Carries the movement's frame | Partly: control and oversight yes; values alignment explicitly no; catastrophic risk absent; upside added |
| 2. Carried by the movement's people and organizations | No |
| 3. A lever from the movement forces adoption | Weak: the one deployer duty (EU AI Act Art. 26) comes from a different lineage |
| 4. A carrier profession with its own body of knowledge | No: privacy professionals hold the claim today |
| 5. Reframes the movement's goal as a business case | Yes, strongly |
| 6. Gives one person or office responsibility | Yes in design (the amendment rule); untested in firms |
| 7. Resists decoupling and cooptation | Unknown; the record says the risk is high |

**Verdict.** As stated, the hypothesis fails: BPM is not the movement's institutional expression. It lacks
the movement's carriers, its lever and its central frame. A narrower claim holds up: BPM is a candidate
*managerial translation* of one strand of AI safety, the work on controlling and governing agents (AI
control "protocols", OpenAI's practices for agentic systems, visibility and IDs for agents, multi-agent
risk). It translates that strand for companies that deploy agents, in the same way personnel professionals
translated civil-rights law into human resources offices. Its ideas come from elsewhere (protocol studies,
safety-critical industries, quality); its timing and evidence increasingly come from the safety strand.

If BPM takes that translating role, the record predicts two things: it survives by making the business case,
and the business case dilutes the original goal. Time to amend and counting non-events are the guards
against that dilution.

## 1. The question and why it matters

An *institutional expression* of a movement is the set of structures (offices, roles, routines, standards)
through which the movement's claims become ordinary organizational practice.[^dobbinsutton] Movements
usually get several, in different arenas. The question here is narrow: inside a company that deploys agents
(not a lab, not a regulator), is BPM, or could it become, the structure through which AI safety claims turn
into practice?

It matters for three reasons:

- **Meaning is set inside firms.** Edelman showed that vague law leaves firms room to construct what
  compliance means, through "symbolic structures" such as officers and rules; later, courts deferred to
  those structures, and "law becomes endogenous to managerialization" [seen, secondary].[^edelman] The
  EU AI Act's deployer duties are vague in exactly this way.
- **Framing decides survival.** Offices tied to a movement's language were cut when the politics turned
  (section 2). If BPM is presented as AI safety, it inherits that exposure.
- **The research group has a choice to make** about whether to place BPM in the safety conversation, in
  operations, or both.

## 2. How movements have become offices

| Movement | Carrier into firms | Lever | Office | Diluted? | Lasted? |
| --- | --- | --- | --- | --- | --- |
| Industrial safety, 1906–1930s | Insurance inspectors, safety engineers (ASSE 1911, National Safety Council 1913) (S) | Workmen's compensation put accident costs on employers (S, M) | Plant safety engineer | Partly: "safety first" ideology also blamed "careless workers" (S, M)[^aldrich] | Yes |
| Quality, 1946–1990s | Quality engineers (ASQC 1946) (S) | Procurement standards, ISO 9000 (1987), Baldrige (1987) (S) | Quality manager | Yes: TQM's symbolic value displaced its technical value (S)[^zbaracki] | Function yes, label no |
| Environment, 1970– | Engineers and lawyers, then EHS managers; activists as recycling coordinators (S, M) | EPA statutes, ISO 14001 (1996) (S) | EHS function; later Chief Sustainability Officer | Yes: means-ends decoupling (S)[^bromley] | EHS yes; CSO count falling from its peak of 216 (S)[^cso] |
| Privacy, 1991– | Privacy lawyers, then CPOs; IAPP 2000 (S) | Ambiguous law plus FTC enforcement; GDPR's DPO, 2018 (S) | Chief Privacy Officer, DPO | Mixed: substantive in the US and Germany (S)[^bamberger] | Yes, strongest case |
| Civil rights, 1961– | Personnel professionals (S)[^dobbin] | Federal contract compliance, Title VII (S) | EEO office, then HR and diversity management | Yes: the clearest managerialization (S)[^edelman] | HR yes; CDO titles cut and renamed from 2023 (S) |
| Harmful content, 2010s– | In-house policy and operations staff; TSPA 2020 (S) | Reputation, advertisers; later the EU DSA (S, M) | Trust and safety | — | Fragile: cuts in 2023 (S) |
| Responsible AI, 2018– | Researchers inside tech firms | None outside the firm | Ethics and responsible AI teams | — | Mostly no: Twitter 2022, Microsoft and Meta 2023, OpenAI Superalignment 2024 (S)[^raicuts] |

**Seven conditions follow from the record.**

1. **Frame continuity.** The office pursues the movement's goal, in managerial terms.
2. **Carriers.** The movement's people or organizations bring it in. Lounsbury found that universities
   with a chapter of the student environmental movement created dedicated, full-time recycling
   coordinators filled by activists; the rest added recycling to existing staff's duties (S).[^lounsbury]
3. **A forcing lever.** A law, liability rule, procurement rule or certification with a vague mandate that
   firms must interpret. Without one, offices are cut in a downturn (the responsible AI, trust and safety,
   sustainability and diversity cases).
4. **A carrier profession** with an association, a certification and a body of knowledge (ASSE, ASQC, IAPP,
   TSPA).
5. **A business case.** Personnel offices survived by recasting themselves in "purely economic terms"
   [seen].[^dobbinsutton] The same move empties out the goal (Edelman).
6. **A responsibility structure.** Kalev, Dobbin and Kelly found that "efforts to establish responsibility
   for diversity lead to the broadest increases" [seen]; training and evaluations did least.[^kalev]
7. **Coupling.** The structure changes outcomes rather than standing as ceremony (Meyer and Rowan) or being
   implemented without affecting results (Bromley and Powell).[^meyer][^bromley] Cooptation shares the
   symbols of power, not the power (Selznick, M).[^selznick]

Two later findings matter for any new office. Activists filled the first sustainability manager roles and
were displaced by degree-holding professionals as the roles formalized (S).[^augustineking] And recycling
coordinators institutionalized recycling while their own occupation declined (S).[^augustine]

## 3. Where AI safety has already been institutionalized

| Arena | Form | Status, October 2026 |
| --- | --- | --- |
| Frontier labs | Anthropic's Responsible Scaling Policy (Sept 2023), with a Responsible Scaling Officer; OpenAI's Preparedness Framework (Dec 2023; v2 Apr 2025); Google DeepMind's Frontier Safety Framework (2024; v3 Sept 2025) (S) | In force, softened: RSP v3.0 (Feb 2026) dropped the 2023 pause commitment and recast some mitigations as "industry-wide recommendations" [seen] |
| Industry commitments | Frontier AI Safety Commitments, Seoul, May 2024: 16 companies to publish thresholds at which risks are "deemed intolerable" [seen] | Frameworks published |
| Evaluators | METR (Dec 2023) (S) | Active |
| Governments | UK AI Safety Institute (2023), renamed AI Security Institute (Feb 2025); US AISI renamed Center for AI Standards and Innovation (June 2025) (S) | Refocused from "safety" to security and "demonstrable risks" |
| State law | California SB 1047 vetoed (2024); SB 53 signed 29 Sept 2025, applying to frontier developers (S) | In force for developers, not deployers |
| Standards | NIST AI RMF (Jan 2023); ISO/IEC 42001 (2023) (S) | Voluntary, certifiable |
| Professions | IAPP AI Governance Professional certification, exam from April 2024 (S) | Privacy is the leading carrier |
| Deployer law | EU AI Act Art. 26(2): "Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support" [seen]; Annex III systems from 2 Dec 2027 after the 2026 Omnibus (S)[^aiact] | Pending; Colorado's broader act was repealed and replaced by a narrower law effective 1 Jan 2027 (S)[^colorado] |

Two observations.

- **The movement's own institution is a business protocol.** The Responsible Scaling Policy is a hard rule
  for a firm (if a model reaches a capability threshold, then certain safeguards apply) with a written
  amendment rule: as remembered from the 2024 text, changes are "proposed by the CEO and the Responsible
  Scaling Officer and approved by the Board of Directors, in consultation with the Long-Term Benefit Trust"
  (M; wording to confirm). Karnofsky's "if-then commitments" generalize the form and note that they "can be
  voluntarily adopted by AI developers; they also, potentially, can be enforced by regulators" [seen].[^karnofsky]
  The 2026 revisions moved parts of the policy from hard to soft. In BPM terms, this is a hardness map
  with an amendment rule, maintained at a lab.
- **Inside deploying firms, privacy and legal hold the work.** Primary responsibility for AI governance:
  privacy 22%, legal and compliance 22%, IT 17%, data governance 10%, ethics and compliance 6%, security 5%
  (IAPP and Credo AI, *AI Governance Profession Report 2025*, S).[^iapp] 68% of privacy professionals have
  taken on AI governance (IAPP, *Salary and Jobs Report 2025–26*, S).

## 4. Scoring BPM against the seven conditions

### 4.1 Frame continuity: partly

The agent strand of AI safety and BPM share mechanisms. OpenAI's *Practices for Governing Agentic AI
Systems* lists seven practices (S, from a secondary summary);[^shavit] most have a BPM counterpart:

| Shavit et al. practice | BPM principle or tool |
| --- | --- |
| Evaluate suitability for the task | Hardness map: which rules an agent may act within |
| Constrain the action space and require approval | Keep the hard core small; put strict rules where teams meet |
| Set default behaviours | Soft rules |
| Legibility of agent activity | Record the reason at the moment of action |
| Automatic monitoring | Count what didn't go wrong; time to amend's threshold rules |
| Attributability | Record the reason; agent IDs (Chan et al.)[^chan] |
| Interruptibility | The right to stop the work, named in the amendment rule |

Greenblatt and colleagues call their pipelines of safety techniques "protocols" (S); a 2025 follow-up tests
"control protocols" on agents doing system administration, cutting attack success from 58% to 7% at a 5%
cost in usefulness (S).[^control] Hammond and colleagues' multi-agent risks (miscoordination, conflict,
collusion) are the risks the BPM guide opens with, citing OpenAI's and Anthropic's 2026 reports on agents
using a package manager as a message board and a "multiagent turf war".[^hammond] Kulveit and colleagues
argue that economic institutions stay aligned with people partly because they depend on human
participation, and that replacing that participation weakens the alignment even if no system is
power-seeking (S).[^kulveit] Business protocols are where that participation is written down.

Three differences keep this partial:

- **Values.** The BPM guide's comparison table says BPM "shapes the agent's environment rather than its
  values". The movement's founding frame is alignment of values.
- **Stakes.** The movement's defining claim is catastrophic and existential risk (the 2023 CAIS statement,
  M). BPM works at business stakes and says so.
- **Upside.** BPM treats a well-made rule as something others can build on ("risk and opportunity live in
  the same place"). The movement's frame is protective. The nearest match in the wider conversation is
  Buterin's d/acc (defensive, decentralized, differential acceleration), not the safety mainstream (S).[^dacc]

### 4.2 Carriers: no

No AI safety organization or its people carry BPM into firms. BPM's carriers are the Protocol Institute
and Summer of Protocols network, plus practitioners from operations, governance and design. Lounsbury's
finding predicts that, without a movement organization present, the work becomes an added duty.

### 4.3 Lever: weak

The one deployer duty that names people, EU AI Act Art. 26(2), comes from the EU's fundamental-rights
approach more than from the Silicon Valley safety movement, whose legislative work (SB 1047, SB 53)
targets developers. Colorado narrowed its law. Our own candidate lever, auditors bringing agent
permissions into Sarbanes-Oxley IT controls, has no tie to the movement. So the lever that would force a
BPM-like structure in deploying firms is not the movement's.

### 4.4 Carrier profession: no

Privacy professionals have the association (IAPP), the certification (AIGP, 2024) and the plurality of
the work. In Abbott's terms, they are the incumbent claimant. BPM has no association or certification and
a body of knowledge in draft.

### 4.5 Business case: yes

The BPM guide argues that strict rules in the right places let the business move faster, and that a gap
in the hard core is both a risk and a missed opportunity. That is the move Dobbin and Sutton describe:
offices first justified by law come to be justified "in purely economic terms" [seen]. It is also the move
that, per Edelman, Fuller and Mara-Drita, drew diversity programmes away from their civil-rights goals.

### 4.6 Responsibility structure: yes in design

The amendment rule names who may change a hard protocol, how, and who may stop the work. The RSP shows
the form operating at a lab. Kalev and colleagues' finding favours this over training. No deploying firm
has been observed running it.

### 4.7 Coupling: unknown, risk high

Every comparable office without an outside lever was cut or diluted (section 2). The labs' own policies
were softened in 2026. Courts and auditors tend to accept the presence of a structure as evidence of
compliance (Edelman 2011, S).[^edelman] BPM's defence is its measures: time to amend counts open cases,
and counting non-events ties the structure to outcomes rather than to its own existence. Whether that
holds in practice is untested.

## 5. Three readings

| Reading | Claim | Fit with the evidence |
| --- | --- | --- |
| A. Institutional expression | BPM is how the AI safety movement becomes practice inside deploying firms | Poor: fails carriers, lever and profession; partial on frame |
| B. Managerial translation | BPM translates the agent-control strand into operations terms, for deploying firms | Good on mechanisms and framing; untested on adoption |
| C. Separate lineage | BPM descends from protocol studies, safety-critical industries and quality; safety research is an input | Best fit for carriers and history |

Our judgment: B and C together. BPM's ancestry is C. Its role, if it gets one, is B. Presenting it as A
would claim a movement it doesn't belong to and import that movement's political exposure.

## 6. What follows

- **Frame for operations, cite safety as evidence.** Offices framed by a movement were cut when the
  politics turned; offices with a responsibility structure and an outside lever lasted. Keep BPM framed
  as operations and cite the agent-safety literature for mechanisms and incidents.
- **Write the first Article 26 oversight template.** Whoever writes the first templates for a vague
  mandate sets its meaning (Edelman). A hardness map plus an amendment rule plus named overseers is a
  candidate structure for Art. 26(2) in firms deploying high-risk systems from December 2027.
- **Study the RSP as a case.** It is a published business protocol with an amendment rule, a named
  officer and three years of version history, including softening. It is the best available test of time
  to amend at a real firm.
- **Expect carrier turnover.** If protocol work formalizes, early enthusiasts (including this group's
  members) are likely to be displaced by credentialed professionals from privacy, audit or GRC, as
  activists were in sustainability.
- **Expect dedicated seats where safety culture is present.** Lounsbury's mechanism and Lin's location
  finding point the same way: AI-native firms in dense labour markets.

**Predictions to register** (to add to [`predicting-roles.md`](predicting-roles.md), section 6):

| By | Prediction | Check against |
| --- | --- | --- |
| End 2027 | The IAPP or a privacy-led body publishes an agent-oversight or Art. 26 guide before any operations body does | IAPP publications |
| End 2028 | At least one non-lab firm publishes a scaling-policy-style document for its own agents, with an amendment rule | Company publications |
| End 2028 | At least one more frontier lab policy revision moves a hard commitment to a recommendation | Policy changelogs |

## 7. Assumptions to pressure-test

- [ ] **"The movement" is several movements.** Rationalist and effective-altruist x-risk work, lab safety
  teams and AI control research have different carriers. The verdict could differ by strand.
- [ ] **The historical analogues may not transfer.** Civil rights and environmentalism had mass
  movements and statutes; AI safety is small, funded by a few donors and centred on labs.
- [ ] **The Shavit mapping** rests on a secondary summary of the practices.
- [ ] **The RSP amendment wording** is from memory; whether versions after v3.2 exist is unconfirmed.
- [ ] **Art. 26's lineage** (fundamental rights rather than Silicon Valley safety) is our reading.
- [ ] **Our stake.** We build BPM. A verdict that it translates a respected movement flatters it.

## Notes

(S) from a search-result summary, not opened. (M) from memory. [seen] verbatim in a search result.

[^dobbinsutton]: Frank Dobbin and John R. Sutton, "The Strength of a Weak State: The Rights Revolution and the Rise of Human Resources Management Divisions," *American Journal of Sociology* 104, no. 2 (1998): 441–76, https://www.journals.uchicago.edu/doi/10.1086/210044. Abstract [seen]: "These legal changes stimulated organizations to create personnel, antidiscrimination, safety, and benefits departments to manage compliance. Later, middle managers came to disassociate these new offices from policy and to justify them in purely economic terms." (S)
[^dobbin]: Frank Dobbin, *Inventing Equal Opportunity* (Princeton, NJ: Princeton University Press, 2009). (S)
[^edelman]: Lauren B. Edelman, "Legal Ambiguity and Symbolic Structures: Organizational Mediation of Civil Rights Law," *American Journal of Sociology* 97, no. 6 (1992): 1531–76; Lauren B. Edelman, Sally Riggs Fuller and Iona Mara-Drita, "Diversity Rhetoric and the Managerialization of Law," *American Journal of Sociology* 106, no. 6 (2001): 1589–1641; Lauren B. Edelman et al., "When Organizations Rule: Judicial Deference to Institutionalized Employment Structures," *American Journal of Sociology* 117, no. 3 (2011): 888–954; Lauren B. Edelman, *Working Law: Courts, Corporations, and Symbolic Civil Rights* (Chicago: University of Chicago Press, 2016). "Law becomes endogenous to managerialization" quoted in a symposium essay. (S)
[^lounsbury]: Michael Lounsbury, "Institutional Sources of Practice Variation: Staffing College and University Recycling Programs," *Administrative Science Quarterly* 46, no. 1 (2001): 29–56. Finding paraphrased from a search summary of the abstract. (S)
[^augustineking]: Grace Augustine and Brayden G. King, "From Movements to Managers: Crossing Organizational Boundaries in the Field of Sustainability," *Work and Occupations* 51, no. 2 (2024): 207–48. (S)
[^augustine]: Grace Augustine, Leanne Hedberg, Tae-Ung Choi and Michael Lounsbury, "Wasted? The Downstream Effects of Social Movement–Backed Occupations," *Administrative Science Quarterly* 70, no. 1 (2025): 23–68. (S)
[^kalev]: Alexandra Kalev, Frank Dobbin and Erin Kelly, "Best Practices or Best Guesses? Assessing the Efficacy of Corporate Affirmative Action and Diversity Policies," *American Sociological Review* 71, no. 4 (2006): 589–617. (S; issue M)
[^meyer]: John W. Meyer and Brian Rowan, "Institutionalized Organizations: Formal Structure as Myth and Ceremony," *American Journal of Sociology* 83, no. 2 (1977): 340–63. (S)
[^bromley]: Patricia Bromley and Walter W. Powell, "From Smoke and Mirrors to Walking the Talk: Decoupling in the Contemporary World," *Academy of Management Annals* 6, no. 1 (2012): 483–530. (S)
[^selznick]: Philip Selznick, *TVA and the Grass Roots: A Study in the Sociology of Formal Organization* (Berkeley: University of California Press, 1949). Definition of cooptation not verified. (S, M)
[^aldrich]: Mark Aldrich, *Safety First: Technology, Labor, and Business in the Building of American Work Safety, 1870–1939* (Baltimore: Johns Hopkins University Press, 1997). (S)
[^zbaracki]: Mark J. Zbaracki, "The Rhetoric and Reality of Total Quality Management," *Administrative Science Quarterly* 43, no. 3 (1998): 602–36. (S; issue M)
[^cso]: "CSO Headcount Falls," *Trellis*, citing Weinreb Group, https://trellis.net/article/cso-headcount-falls-weinreb-group/. Scopes differ across editions. (S)
[^bamberger]: Kenneth A. Bamberger and Deirdre K. Mulligan, *Privacy on the Ground: Driving Corporate Behavior in the United States and Europe* (Cambridge, MA: MIT Press, 2015). (S)
[^raicuts]: "Microsoft's A.I. Ethics Layoffs Send a Worrying Signal," *Fortune*, 14 March 2023, https://www.fortune.com/2023/03/14/microsofts-a-i-ethics-layoffs-send-a-worrying-signal; "Facebook Parent Meta Breaks Up Its Responsible AI Team," *CNBC*, 18 November 2023, https://www.cnbc.com/amp/2023/11/18/facebook-parent-meta-breaks-up-its-responsible-ai-team.html; "OpenAI Dissolved Its Team Dedicated to Preventing Rogue AI," *Popular Science*, May 2024, https://www.popsci.com/technology/openai-dissolved-its-team-dedicated-to-preventing-rogue-ai/. (S)
[^aiact]: Regulation (EU) 2024/1689, Art. 26, https://artificialintelligenceact.eu/article/26/; White & Case, "EU AI Omnibus Enters into Force, Amending the AI Act," July 2026, https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act. (S)
[^colorado]: Lathrop GPM, "Colorado Enacts New Law Regulating Automated Decision-Making Technology," May 2026, https://www.lathropgpm.com/insights/colorado-enacts-new-law-regulating-automated-decision-making-technology/. (S)
[^karnofsky]: Holden Karnofsky, "If-Then Commitments for AI Risk Reduction," Carnegie Endowment for International Peace, 13 September 2024, https://carnegieendowment.org/research/2024/09/if-then-commitments-for-ai-risk-reduction; Anthropic, "Responsible Scaling Policy Updates," https://www.anthropic.com/rsp-updates; Centre for the Governance of AI, "Anthropic's RSP v3.0: How It Works, What's Changed," 2026, https://governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections. (S)
[^iapp]: IAPP and Credo AI, *AI Governance Profession Report 2025*, 16 April 2025, https://iapp.org/resources/article/ai-governance-profession-report. (S)
[^shavit]: Yonadav Shavit et al., *Practices for Governing Agentic AI Systems* (OpenAI, December 2023), https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf. (S; list of practices from a secondary summary)
[^chan]: Alan Chan et al., "Visibility into AI Agents," *FAccT* 2024, https://arxiv.org/abs/2401.13138; Alan Chan et al., "IDs for AI Systems," arXiv:2406.12137, 2024. (S)
[^control]: Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan and Fabien Roger, "AI Control: Improving Safety Despite Intentional Subversion," *Proceedings of ICML* 2024, PMLR 235, https://proceedings.mlr.press/v235/greenblatt24a.html; Aryan Bhatt et al., "Ctrl-Z: Controlling AI Agents via Resampling," arXiv:2504.10374, 2025. (S)
[^hammond]: Lewis Hammond et al., *Multi-Agent Risks from Advanced AI*, Cooperative AI Foundation Technical Report 1, February 2025, https://arxiv.org/abs/2502.14143. (S)
[^kulveit]: Jan Kulveit et al., "Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development," arXiv:2501.16946, January 2025; ICML 2025, https://proceedings.mlr.press/v267/kulveit25a.html. (S)
[^dacc]: Vitalik Buterin, "My Techno-Optimism," 27 November 2023, as summarized in *The Defiant*, https://thedefiant.io/vitalik-buterin-proposes-d-acc-philosophy-in-post-on-techno-optimism. (S)
