# Predicting the role: six frameworks, where they diverge, and what they agree on

Research draft · 10 October 2026 · Protocols for Business · companion to
[`role-emergence.md`](role-emergence.md), [`business-protocol-lead-critique.md`](business-protocol-lead-critique.md)
and [`bpm-and-ai-safety.md`](bpm-and-ai-safety.md)

> **Status.** Working notes. Sources were found through web search; the pages themselves could not be
> opened from this environment. (S) means a search result supported the point; (M) means from memory;
> [seen] marks a quotation that appeared verbatim in a search result, usually an abstract or a secondary
> source. Check every quotation against the original before publishing.

## Summary

People have predicted new roles in six main ways. Each answers a different question, and each predicts
something different for protocol work:

| Framework | The question it asks | Its prediction for protocol work, 2027–2029 |
| --- | --- | --- |
| 1. Jurisdiction (Abbott, Hughes) | Which occupation can claim the new tasks with its own abstract knowledge? | A contest. Accountants claim rules about money, engineers claim enforcement, lawyers claim data rules. A distinct role only if Business Protocol Management becomes a credible abstraction; otherwise an advisory or subordinate seat |
| 2. Integration (Lawrence and Lorsch, Galbraith, Jaques) | Has cross-unit uncertainty outgrown hierarchy and rules? | Companies climb a ladder: liaison and task forces (AI councils) in 2027, then integrating roles for cross-functional rule changes. Practitioner level, influence from competence |
| 3. Task economics (Autor, Acemoglu and Restrepo, Atalay, Lin) | Which new tasks appear, and inside which jobs? | Mostly absorbed within existing titles, as 88% of task change has been. A new title only in dense, diverse labour markets and AI-heavy firms |
| 4. Decision rights (Agrawal, Gans and Goldfarb) | When prediction gets cheap, where do judgment and decision rights move? | A judgment owner for the payoffs in rule decisions (how much risk for how much speed), plus transition roles for redesigning interdependent decisions |
| 5. Institutional markers (Wilensky; occupation statistics) | Has the work built the institutions that lasting roles build? | Not yet: no body of knowledge, association or certification for protocol work. Adjacent work with institutions (AI governance, GRC engineering) absorbs it first |
| 6. Movements into offices (Dobbin, Edelman, Lounsbury) | Is a movement pushing the work into firms, through which profession and which lever? | An added duty for privacy and legal in most firms; dedicated seats only where a movement organization is present and a lever forces it. If an office forms, it survives on a business case that dilutes the goal |

**Where they converge.** All six put the durable part of the work in the same place: judgment about rules
that cross functions, held by practitioners whose authority comes from structure. And they converge on
knowledge as the deciding asset. A role forms when enough of the tacit knowledge behind Business Protocol
Management is written down to be claimed and taught (a register, an amendment rule, a metric), while the
judgment that resists writing down (weighing revenue against risk across functions) stays with a person.
Too little written down, and the work stays with long-tenured staff who "just know". Too much, and it
becomes policy code and is absorbed by engineering.

## 1. How roles have been predicted and documented

Before the frameworks, the record on prediction itself.

- **Official classifications are reliable but late.** The US Standard Occupational Classification takes
  about five years per revision and adds an occupation only when it is distinct and has enough workers to
  measure (S).[^soc] Data scientist: title coined 2008, occupation code 2018, first stand-alone employment
  estimate May 2021, about 13 years in all. Information security analyst: first certification (CISSP) 1994,
  occupation code 2010, first estimate 2012, about 18 years (S).[^lag]
- **The Census index records titles as they appear in survey answers.** It held about 30,000 titles in
  1990 and over 32,000 by 2022, adding titles reported "numerous times" [seen]. Autor and colleagues date
  new work by the decade a title enters it (S).[^census]
- **O*NET ran a formal programme for emerging occupations.** Its definition: occupations that "involve
  significantly different work from that performed by incumbents of other occupations and… are not
  adequately reflected by the existing O*NET system" [seen]. Size was tested by employment, projected
  growth and association membership; 153 such occupations were added in 2009 (S).[^onet]
- **Job-ad and profile data detect roles early but can't separate lasting roles from fads.** LinkedIn's
  "Emerging Jobs" lists flagged data scientist and machine learning engineer years before official codes,
  and flagged blockchain developer (#1 in 2018) just as loudly (S).[^linkedinej] Postings with "metaverse"
  in the title fell 81% between April and June 2022 (S).[^metaverse]
- **Forecast lists are rarely scored.** The World Economic Forum's surveys and Cognizant's "21 Jobs of the
  Future" publish no title-by-title check of what materialised (S). The one rigorously scored forecast,
  the Bureau of Labor Statistics' growth projections, gets direction right most of the time but beats a
  naive trend only modestly (S).[^forecast]
- **Most change happens inside titles.** In 8.3 million newspaper job ads from 1940 to 2000, "88 percent of
  the [economywide] task changes have occurred within job titles" [seen].[^atalay]

**Lesson for us.** A prediction is a hypothesis to be scored. The best leading indicator in the cases we
have is institutional: lasting roles built an association, a body of knowledge, a certification or degree
programmes before they got an official code. Titles with none of these (prompt engineer, Chief Metaverse
Officer) faded. That is our inference from a few cases, not an established finding.

## 2. Six frameworks applied to protocol work

### 2.1 Jurisdiction: who can claim the tasks?

**The claim.** Professions form a system in which each competes for jurisdiction over tasks. New
technology creates or destroys tasks; the group that can redefine the new problem in its own abstract
knowledge wins it, before three audiences (the public, the law and the workplace), with workplace
settlements coming first and messiest (S, M).[^abbott] Settlements range from full jurisdiction to
subordination, a division of labour, an advisory role, or a split by client (S, M). Hughes adds the
distinction between a *license* to do the work and a *mandate* to define how it should be done (S, M).[^hughes]

**Applied.** The tasks are deciding and changing rules that agents and people act under. Claimants, each
with an abstraction:

| Claimant | Its abstraction | Likely claim |
| --- | --- | --- |
| Accountants, controllers, internal audit | Internal control frameworks (COSO), Sarbanes-Oxley | Rules about money and reporting |
| Engineers | Policy as code, access control, the release pipeline | Enforcement, and by default the rule text |
| Lawyers and privacy professionals | Regulation, contracts, data protection | Data and customer rules |
| Process and operations professionals | Lean, process management, value streams | Workflow and approval design |
| Security | Risk frameworks, identity and access | What agents may see, do and spend |

**Prediction.** A contest settled workplace by workplace. Protocol work becomes a distinct jurisdiction
only if Business Protocol Management becomes an abstraction others accept: one that redefines "controls",
"processes" and "permissions" as one problem (hard, soft and free rules; the amendment rule; time to
amend). Otherwise the likely settlement is an advisory or subordinate seat inside the controller's or
engineering's jurisdiction.

### 2.2 Integration: has coordination outgrown hierarchy?

**The claim.** As units differentiate (different goals, time horizons, formality), integration gets
harder; organizations add integrating mechanisms in rising order as uncertainty grows (S).[^lorsch] Lawrence
and Lorsch called the integrator a new kind of management job, and found that in high performers
integrators drew influence from competence rather than position (S, M). Galbraith's ladder runs from direct
contact to liaison roles, task forces, teams, integrating roles, managerial linking roles and the matrix
(S for the categories; the full ladder M).[^galbraith] Jaques sets a role's level by its time span of
discretion: how long its holder works before review (S).[^jaques]

**Applied.** Agents raise interdependence: one rule change (a discount limit in the deal agent's
permissions) now touches sales, finance, legal and security at once, at machine speed.

**Prediction.** Companies climb the ladder. 2027: direct contact, liaison roles and task forces (AI
councils). 2028–29, where cross-functional rule changes stay frequent: an integrating role for those
changes. Level: amendment decisions run over weeks to a quarter, which points to a practitioner level, not
an executive one. Influence from competence and a signed agreement, not rank. This framework predicts the
role the critique proposes most directly.

### 2.3 Task economics: which tasks, inside which jobs?

**The claim.** Jobs are bundles of tasks. Computers substitute for tasks that follow "explicit rules" and
complement "nonroutine problem-solving and complex communications tasks" [seen].[^alm] Automation displaces
labour from tasks; new tasks reinstate it [seen: "a reinstatement effect"].[^ar] New work appears where
innovation complements an occupation's outputs, and first in dense, educated, diverse cities (S).[^autor][^lin]

**Applied.** Agents automate rule-following and create new tasks around rules: finding unwritten ones,
deciding changes, propagating them into agent configuration, checking the result.

**Prediction.** Most of these tasks are absorbed within existing titles: controllers, deal desks,
revenue operations, GRC and platform engineers. A new title appears first in AI-heavy firms in dense labour
markets (San Francisco, New York, London). This framework gives the lowest odds of a distinct role, and it
is the one with the best empirical record.

### 2.4 Decision rights: where does judgment move?

**The claim.** A decision combines prediction and judgment (valuing the payoffs). AI makes prediction
cheap, so judgment, data and action become more valuable; the large gains need system-level redesign of
interdependent decisions, which shifts power (S).[^agg] "Decision rights will flow to where judgment is
still needed" [seen, secondary].[^agg]

**Applied.** Agents take over predictions inside rules (is this discount likely to close the deal? is
this refund fraud?). What remains is judgment about payoffs: how much risk to accept for how much speed,
across functions.

**Prediction.** Two kinds of role. A transition role for redesigning interdependent decisions (forward-
deployed engineers, Chief AI Officers), which ends when redesign does. And a durable judgment owner for
the payoffs written into rules: who sets the limit, and who changes it when losses or delays say it is
wrong. That is the autonomy budget's owner in the critique's terms.

### 2.5 Institutional markers: has the work built institutions?

**The claim.** Occupations professionalize through a typical sequence: full-time work, a training school,
a university specialty, an association, licensing, a code of ethics (S, secondary).[^wilensky] Barley and
Bechky add that the same technology produces different role structures in different workplaces,
negotiated around the objects people work with (S).[^barley][^bechky]

**Applied.** Protocol work has a research group (ours), a practice guide and a training programme
(watching, workshops). It has no association, no body of knowledge others cite, no certification and no
degree programme. Adjacent fields are further along: AI governance has a professional certification (M:
IAPP's AI governance credential, 2024), and GRC engineering has a manifesto and a community (S).

**Prediction.** Near term, the adjacent fields with institutions absorb the work. A distinct role becomes
likely only if protocol work builds its own markers: a body of knowledge that practitioners in other
titles adopt, then training, then an association. Barley's point adds that, even then, the role will look
different in each company.

### 2.6 Movements into offices: who carries the work in, and what forces it?

**The claim.** Social movements have repeatedly become offices inside firms: civil-rights law became
personnel and then human resources departments, environmentalism became EHS functions, privacy advocacy
became the Chief Privacy Officer. Professionals inside firms define what a vague mandate means in practice,
and later justify the new office "in purely economic terms" [seen].[^dobbinsutton] Courts then defer to the
structures firms built (Edelman, S).[^edelmanmov] A movement organization's local presence decides whether
the work gets a dedicated, full-time role or becomes an added duty (Lounsbury, S).[^lounsburymov] Offices
without an outside lever were cut when the politics turned: responsible AI teams (2022–24), trust and safety
(2023), chief diversity and sustainability officers (from 2023) (S).

**Applied.** The nearest movement is AI safety. It has built institutions in labs, governments and
standards, but not in deploying firms, where privacy and legal hold most AI governance work (IAPP and
Credo AI, *AI Governance Profession Report 2025*: privacy 22%, legal and compliance 22%, S). The full test
is in [`bpm-and-ai-safety.md`](bpm-and-ai-safety.md).

**Prediction.** Mostly an added duty, held by privacy, legal or GRC. Dedicated seats where a movement is
present (AI-native firms) and where a lever forces one (EU AI Act Art. 26 oversight from December 2027).
An office that forms will survive by making the business case and will be diluted by it; its early
holders will be displaced by credentialed professionals as it formalizes (Augustine and King, S).

## 3. Where the predictions diverge

| | Jurisdiction | Integration | Task economics | Decision rights | Institutional markers | Movements into offices |
| --- | --- | --- | --- | --- | --- | --- |
| Distinct role by 2029? | Only if the abstraction wins | Yes, where cross-functional change is frequent | Rarely | Yes, as judgment owner | Not unless institutions form | Only with a movement present and a lever |
| Who holds it | The winning profession | An integrator, competence-based | Existing titles | Whoever owns the payoffs | Adjacent fields first | Privacy and legal; enthusiasts first, then professionals |
| Level | Depends on the settlement | Practitioner | Unchanged | Delegated by the CFO or COO | — | Officer title, practitioner work |
| What decides it | Contest of abstractions | Interdependence and uncertainty | Complementarity, location | Where judgment remains | Body of knowledge, training, association | Carriers, lever, business case |
| Its blind spot | Says little about employers | Ignores power | Thin on bundling and politics | Assumes rights move efficiently | Slow, after the fact | Assumes a movement; AI safety is small and lab-centred |

The sharpest disagreement is between task economics (absorbed in existing titles) and integration
(a new integrating role). Both can be right: integration describes the companies where cross-functional
rule changes are frequent; task economics describes the rest. That matches the critique's odds: most
companies absorb the duties; a minority create a seat.

## 4. Where they converge: the tacit knowledge of Business Protocol Management

The frameworks agree on three things.

1. **The durable work is judgment about rules that cross functions.** Integration calls it integration,
   decision rights calls it judgment over payoffs, jurisdiction calls it the contested task. All exclude
   the parts that are skills tied to the technology (agent supervision, prompting).
2. **It sits at practitioner level with authority from structure.** Integrators influence by competence;
   time spans of weeks to a quarter point to practitioners; workplace jurisdiction is settled before legal
   jurisdiction.
3. **Knowledge decides who gets it.** This is where tacit knowledge comes in.

Polanyi: "we can know more than we can tell" [seen].[^polanyi] Nonaka and Takeuchi describe externalization,
turning tacit knowledge into explicit knowledge others can use (S).[^nonaka] Collins separates relational
tacit knowledge (could be told, but isn't), somatic (embodied) and collective (held in a group's practice,
the hardest to write down) (S).[^collins]

The tacit knowledge behind Business Protocol Management, sorted that way:

| Knowledge | Kind of tacit knowledge | Today it lives with | Can it be written down? |
| --- | --- | --- | --- |
| Which rules actually bind, and which are leftovers | Relational | Long-tenured operations staff, deal desk veterans | Yes: the rule register |
| Seeing protocols and their non-events at all (protocol vision) | Somatic, trained by practice | Few people; trained by watching | Partly: the watching guide trains it, it can't replace it |
| How rules interact across functions | Collective | Spread across functions; no one holds it whole | Partly: the map, the amendment history |
| Reading overrides, workarounds and agent stalls as signals | Relational, newly explicit | Agent logs, approval histories | Yes: threshold rules for time to amend |
| Weighing revenue against risk when a rule should change | Collective judgment | Senior managers, informally | Only its process: the amendment rule and the autonomy budget |

**The convergent prediction.** Abbott's framework needs an *abstraction* to claim jurisdiction. Autor's
needs tasks that don't follow "explicit rules" to resist automation. Lawrence and Lorsch's integrators
need collective knowledge of more than one unit. Together they place a durable protocol role in a narrow
band:

- **Too little written down:** the knowledge stays with veterans who "just know". No role forms; the work
  leaves when they do.
- **Too much written down:** rules become policy code and checks. Engineering absorbs it, as with prompting.
- **In between:** enough externalized to be claimable and teachable (the register, the amendment rule, the
  metric), with collective judgment about cross-functional trade-offs still held by a person. That is the
  durable role.

**What this means for the research group.** The group's practical lever is building the abstraction:
Business Protocol Management as a body of knowledge practitioners in other titles adopt. That is Abbott's
precondition for jurisdiction and Wilensky's first institutional marker. The training track (watching,
workshops, simulations) builds the somatic part that writing can't. If both take hold, the likeliest
outcome is a recognised specialty inside existing titles (a controller or revenue operations analyst
"who does protocols"), which may later become a role of its own.

## 5. Why bundling happens: a test we can use

None of the frameworks fully explains why particular activities bundle under one accountability. Combining
them suggests a test: activities bundle into one role when they share

1. **one decision**: the same trade-off judged repeatedly (Agrawal, Gans and Goldfarb);
2. **one body of knowledge**: an abstraction that makes them one problem (Abbott);
3. **one interdependence**: they connect the same differentiated units (Lawrence and Lorsch); and
4. **one renewal**: the same outside pressure and number keeps asking about them (role-emergence,
   section 6).

Applied to the critique's loop (register, find, cost, decide, propagate, check, retire, report): all eight share
the decision (whether a rule should change), the interdependence (functions on both sides of the rule) and
the renewal (time to amend, audit). They lack a shared, accepted body of knowledge. That is the missing
piece, and the one the research group can supply.

## 6. Predictions to register and score

Following the lesson that forecasts should be scored, these are stated so they can be checked:

| By | Prediction | Framework | Check against |
| --- | --- | --- | --- |
| End 2027 | Most companies running agents form an AI council or task force; few create a rules role | Integration | Job postings; council announcements |
| End 2027 | "AI agent manager" postings peak and flatten, as "prompt engineer" did | Task economics | Indeed and Lightcast title counts |
| End 2028 | Agent rules about money appear in audit findings or IT change-control scope in US-listed firms | Jurisdiction (accountants' claim) | Audit and SOX guidance; practitioner surveys |
| End 2028 | At least one AI-native firm in a dense labour market posts a role owning cross-functional rule changes | Task economics (Lin), integration | Postings, under any title |
| End 2029 | No association or certification for protocol work exists unless the research group or a peer builds one | Institutional markers | Association and certification launches |
| End 2027 | A privacy-led body publishes an agent-oversight or Art. 26 guide before any operations body does | Movements into offices | IAPP publications |
| End 2028 | At least one non-lab firm publishes a scaling-policy-style document for its own agents, with an amendment rule | Movements into offices | Company publications |

## 7. Assumptions to pressure-test

- [ ] **The convergence is ours.** The frameworks don't address protocol work directly; the mapping in
  sections 2 and 4 is our interpretation.
- [ ] **Institutional markers as a leading indicator** rest on a few cases (information security, data
  science, prompt engineering, the metaverse).
- [ ] **The tacit-knowledge band** (too little, too much, in between) is a hypothesis built from Abbott,
  Autor and Collins, not a finding.
- [ ] **The AI governance certification** date is from memory.
- [ ] **Our position.** We are the research group building the abstraction. That gives us a stake in
  predicting the role exists.

## Notes

(S) from a search-result summary, not opened. (M) from memory. [seen] verbatim in a search result.

[^soc]: U.S. Bureau of Labor Statistics, "2018 SOC: What's New," https://stats.bls.gov/soc/2018/soc_2018_whats_new.pdf; "2010 SOC: What's New," https://www.bls.gov/soc/soc_2010_whats_new.pdf; Office of Management and Budget, final notice, *Federal Register*, 28 November 2017, https://www.govinfo.gov/content/pkg/FR-2017-11-28/html/2017-25622.htm. (S)
[^lag]: U.S. Bureau of Labor Statistics, "Employment and Wages for Newly Defined Occupations, May 2021," https://www.bls.gov/opub/ted/2022/employment-and-wages-for-newly-defined-occupations-may-2021.htm; "The Origins of the Job Title 'Data Scientist'," *Quartz*, https://qz.com/work/1435689/the-origins-of-the-job-title-data-scientist; "ISC2," *Wikipedia*, https://en.wikipedia.org/wiki/ISC2. (S)
[^census]: U.S. Census Bureau, "Industry and Occupation Indexes," https://www.census.gov/topics/employment/industry-occupation/guidance/indexes.html; "Most Work Is New Work, US Census Data Shows," *MIT News*, 1 April 2024, https://news.mit.edu/2024/most-work-is-new-work-us-census-data-shows-0401. (S)
[^onet]: National Center for O*NET Development, "Updating the O*NET-SOC Taxonomy," 2009, https://www.onetcenter.org/reports/UpdatingTaxonomy2009.html; "New and Emerging Occupations," https://www.onetcenter.org/dl_files/NewEmerging.pdf; National Research Council, *A Database for a Changing Economy: Review of the Occupational Information Network (O*NET)* (Washington, DC: National Academies Press, 2010), ch. 6, https://www.nationalacademies.org/read/12814/chapter/6. (S)
[^linkedinej]: LinkedIn, "The Fastest-Growing Jobs in the U.S. Based on LinkedIn Data," 7 December 2017, https://blog.linkedin.com/2017/december/7/the-fastest-growing-jobs-in-the-u-s-based-on-linkedin-data; "LinkedIn 2018 Emerging Jobs Report," https://economicgraph.linkedin.com/en-us/research/linkedin-2018-emerging-jobs-report. (S)
[^metaverse]: "Chief Metaverse Officers," *Axios*, 29 November 2022, https://www.axios.com/2022/11/29/chief-metaverse-officers (citing Revelio Labs). (S)
[^forecast]: World Economic Forum, *The Future of Jobs Report 2018*, https://www3.weforum.org/docs/WEF_Future_of_Jobs_2018.pdf; Cognizant, "Jobs of the Future," 8 November 2018, https://news.cognizant.com/2018-11-08-Cognizants-Center-for-the-Future-of-Work-Takes-a-Deep-Dive-into-its-Latest-Look-at-the-Jobs-of-the-Future2; U.S. Bureau of Labor Statistics, "Evaluating the 2014–24 Occupational Employment Projections," https://www.bls.gov/emp/evaluations/2014-2024-occupational.htm. (S)
[^atalay]: Enghin Atalay, Phai Phongthiengtham, Sebastian Sotelo and Daniel Tannenbaum, "The Evolution of Work in the United States," *American Economic Journal: Applied Economics* 12, no. 2 (2020): 1–34; quotation as reported in *Monthly Labor Review*, 2021, https://www.bls.gov/opub/mlr/2021/beyond-bls/work-has-transformed-in-the-united-states-just-not-how-you-think-it-has.htm. (S)
[^abbott]: Andrew Abbott, *The System of Professions: An Essay on the Division of Expert Labor* (Chicago: University of Chicago Press, 1988), esp. ch. 3, "The Claim of Jurisdiction," and ch. 4. (S, M)
[^hughes]: Everett C. Hughes, "License and Mandate," in *Men and Their Work* (Glencoe, IL: Free Press, 1958), 78–87. (S; definitions M)
[^lorsch]: Paul R. Lawrence and Jay W. Lorsch, *Organization and Environment: Managing Differentiation and Integration* (Boston: Harvard Business School, Division of Research, 1967); "New Management Job: The Integrator," *Harvard Business Review* 45, no. 6 (November–December 1967): 142–51. (S; volume M)
[^galbraith]: Jay R. Galbraith, *Designing Complex Organizations* (Reading, MA: Addison-Wesley, 1973); "Organization Design: An Information Processing View," *Interfaces* 4, no. 3 (1974): 28–36. (S)
[^jaques]: Elliott Jaques, *Requisite Organization* (Arlington, VA: Cason Hall, 1989; 2nd ed. 1996). (S for 1996; 1989 M)
[^alm]: David H. Autor, Frank Levy and Richard J. Murnane, "The Skill Content of Recent Technological Change: An Empirical Exploration," *Quarterly Journal of Economics* 118, no. 4 (2003): 1279–1333. (S)
[^ar]: Daron Acemoglu and Pascual Restrepo, "Automation and New Tasks: How Technology Displaces and Reinstates Labor," *Journal of Economic Perspectives* 33, no. 2 (2019): 3–30. (S)
[^autor]: David Autor, Caroline Chin, Anna Salomons and Bryan Seegmiller, "New Frontiers: The Origins and Content of New Work, 1940–2018," *Quarterly Journal of Economics* 139, no. 3 (2024); NBER Working Paper 30389 (2022). (S; issue M)
[^lin]: Jeffrey Lin, "Technological Adaptation, Cities, and New Work," *Review of Economics and Statistics* 93, no. 2 (2011): 554–74. (S)
[^agg]: Ajay Agrawal, Joshua Gans and Avi Goldfarb, *Power and Prediction: The Disruptive Economics of Artificial Intelligence* (Boston: Harvard Business Review Press, 2022); *Prediction Machines: The Simple Economics of Artificial Intelligence* (Boston: Harvard Business Review Press, 2018). Quotation from an HBR summary. (S; 2018 publisher M)
[^wilensky]: Harold L. Wilensky, "The Professionalization of Everyone?," *American Journal of Sociology* 70, no. 2 (1964): 137–58. (S; issue M)
[^barley]: Stephen R. Barley, "Technology as an Occasion for Structuring: Evidence from Observations of CT Scanners and the Social Order of Radiology Departments," *Administrative Science Quarterly* 31, no. 1 (1986): 78–108; Stephen R. Barley and Julian E. Orr, eds., *Between Craft and Science: Technical Work in the United States* (Ithaca, NY: ILR Press, 1997). (S)
[^bechky]: Beth A. Bechky, "Object Lessons: Workplace Artifacts as Representations of Occupational Jurisdiction," *American Journal of Sociology* 109, no. 3 (2003): 720–52. (S)
[^dobbinsutton]: Frank Dobbin and John R. Sutton, "The Strength of a Weak State: The Rights Revolution and the Rise of Human Resources Management Divisions," *American Journal of Sociology* 104, no. 2 (1998): 441–76. (S)
[^edelmanmov]: Lauren B. Edelman et al., "When Organizations Rule: Judicial Deference to Institutionalized Employment Structures," *American Journal of Sociology* 117, no. 3 (2011): 888–954. (S)
[^lounsburymov]: Michael Lounsbury, "Institutional Sources of Practice Variation: Staffing College and University Recycling Programs," *Administrative Science Quarterly* 46, no. 1 (2001): 29–56. (S)
[^polanyi]: Michael Polanyi, *The Tacit Dimension* (Garden City, NY: Doubleday, 1966), 4. (S)
[^nonaka]: Ikujiro Nonaka and Hirotaka Takeuchi, *The Knowledge-Creating Company* (New York: Oxford University Press, 1995). (S; publisher M)
[^collins]: Harry Collins, *Tacit and Explicit Knowledge* (Chicago: University of Chicago Press, 2010). (S)
