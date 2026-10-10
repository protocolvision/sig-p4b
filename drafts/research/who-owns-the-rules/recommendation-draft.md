# Recommendation (provisional): how protocol vision and Business Protocol Management spread through an organisation

Protocols for Business · draft · 10 October 2026 · **provisional**: built on first-round evidence, which
rests on search-engine summaries; the end-to-end rerun ([`RERUN.md`](RERUN.md)) keeps only what it
supports.

## 1. The problem

Agents already act under rules about what they may spend, see and say, and when a person must step in.
When a rule needs to change, nobody owns the change. The first round found:

- **Rule work is a duty, not a job.** Designing rules for agents shows up inside agent operations, legal,
  sales, identity and risk roles; finding unwritten rules and deciding changes across functions don't
  appear in public documents at all (`results/loop-2026-10-10/`, `roles/`).
- **That silence is weak evidence.** The method would have missed past roles whose authority came from
  internal agreements (calibration in `exploratory/` and the report).
- **Outside rules are arriving through chokepoints.** Card networks and large platforms already bind agents
  that pay or act through them; finance regulators have templates from algorithmic trading: an inventory, a
  defined material change, monitoring with a kill function, certified designers and a named senior owner
  (`results/industry-2026-10-10/`).

So the question is not whether to hire a protocol lead. It is how to place each layer of rule work where it
already lives, and give it an owner, an artefact and a measure before an outside rule decides for you.

## 2. The recommendation in one line

Make protocol vision a shared capability in every function, protocol engineering a named specialty inside
existing roles, and rule decisions an executive's accountability with a cross-functional forum, all
working from one register of agents and rules.

## 3. By layer

| Layer | Who holds it | Seniority | Artefact | Measure | Evidence |
| --- | --- | --- | --- | --- | --- |
| **Finding the rules** (protocol vision) | Everyone who runs agents or approvals, in a monthly exception review per function; a mid-level analyst in the COO's office keeps the register | Practitioner; register owner mid-level | The agent and rule register: every agent, its limits, its named operator, and the unwritten rules found in reviews | Share of agents and rules in the register with a named owner; findings per review | Trading's inventory requirement (RTS 6, PRA SS5/18); the BPM guide's See phase |
| **Designing rules** (protocol engineering) | Agent operations specialists, legal engineers, GTM engineers, identity and access administrators, accounting operations leads | Mid-level, inside each function | A hardness map per function; limits enforced at a gateway the company controls; a written definition of a material change | Rules changed without an incident; overrides per rule | v1 clusters C1, C7, C8, C10; role library; trading's registered designers |
| **Deciding changes across functions** | A named executive (usually the COO), with a monthly change forum where business, risk, compliance and technology each sign off their part | Executive; practitioners prepare the cases | The amendment rule: who may change each hard rule, how, and who may stop the work | Time to amend: days from a rule crossing its override threshold to a recorded decision, counting open cases | Trading (CEO certification, named senior manager); counter-examples show small firms can give this to one person |

## 4. By stage

| Stage | What triggers it | What to put in place |
| --- | --- | --- |
| **Now** | Agents in production, no outside rule | The register; a monthly exception review in each function that runs agents; one or two people per function trained in protocol vision; a baseline for time to amend |
| **Outside rules apply** | Agents that spend money (card network rules) or act on large platforms (platform terms) | Limits, logging and a stop switch enforced at a gateway the company controls, not only in vendor consoles; an agent risk and control team under the COO, mid-level |
| **Sector rules apply** | Regulated finance first; EU AI Act oversight duties for high-risk uses | A named executive who certifies agent controls each year; a formal change forum; named, trained designers for every agent that touches regulated decisions |

Start at the stage you are in; don't build the third stage's machinery before its trigger. Offices built
without a lever were the first to be cut in earlier cycles (responsible AI teams, chief diversity and
sustainability officers).

## 5. By function

Each function that runs agents names one person who owns its hardness map and its exception review, inside
an existing role: the support operations lead for service agents, the deal desk or revenue operations lead
for sales agents, the accounting operations lead for finance agents, the legal operations lead or legal
engineer for contract agents, the identity and access lead for permissions across all agents. The COO's
register joins these up; the change forum decides anything that crosses two functions.

## 6. Training path

The group's three training formats map onto the three layers:

- **Watching** (observations) trains protocol vision: seeing the rules work actually runs on, and reading
  overrides, workarounds and agent stalls as evidence. For everyone in the exception reviews.
- **Workshops** (hardness maps) train protocol engineering: which rules to make hard, which to keep soft,
  where interfaces need strict rules. For the named specialists in each function.
- **Simulations** (amendment decisions under trade-offs) train rule decisions: weighing revenue against risk
  across functions, with time pressure. For executives and the change forum.

## 7. What not to do

- **Don't hire one senior "Business Protocol Lead" to own all three layers.** In the nearest industry,
  practitioners design rules and executives decide changes; a single owner sits in neither place.
- **Don't frame it as AI safety.** Safety-framed offices were cut when the politics turned; frame it as
  operations and cite safety research for mechanisms and incidents.
- **Don't let the register become ceremony.** A register without the exception review and time to amend is
  a structure that changes nothing; courts and auditors accept structures, which makes ceremony tempting.
- **Don't let vendor consoles hold your rules.** Trading required limits under the firm's "direct and
  exclusive control"; agents' limits should live where the company can see and change them across vendors.

## 8. Assumptions to test in the rerun

- Exception reviews surface unwritten rules at a useful rate (needs practitioner speech and rule-change
  events from the corpus).
- Trading's pattern carries to agents that pay or act on platforms; for other agent work the retail control
  case (no internal decider) may hold instead.
- Time to amend can be measured from existing records (approval logs, override logs, tickets).
- Function-level owners exist and have time; the role library suggests the duty sits with mid-level staff
  who already run agents.
- We build Business Protocol Management, so a recommendation that uses its artefacts suits us; the rerun's
  red team should test each artefact against a simpler alternative.

## 9. Predictions to register

| By | Prediction | Check against |
| --- | --- | --- |
| End 2027 | A bank or broker regulator requires an inventory of AI agents with named owners and stop controls | FINRA, FCA, PRA, ESMA publications |
| End 2028 | Card network rules for agent purchases require merchants or agent providers to log and limit agent actions | Visa and Mastercard rule updates |
| End 2028 | At least one large non-financial firm publishes an agent policy naming who may change agent limits | Company publications |
