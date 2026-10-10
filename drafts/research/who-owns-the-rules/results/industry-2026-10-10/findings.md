# Industry analogue: findings and translation

Run 10 October 2026 under [`../../industry-analogue-design.md`](../../industry-analogue-design.md). All facts
rest on search-result summaries: no source page could be opened. Some timeline rows carry grades P or R
because their agents graded by source type; read every row as grade S until checked.

## 1. Which industry

Two scorers, working independently from ten cited fact sheets, ranked algorithmic and electronic trading
first (59.5 of 64) and electricity grid operation second (57.0); commercial aviation (54.0) and retail
banking (52.5) followed. Hospital clinical care ranked last (39.0): physicians own the decisions and
software rarely acts on its own. Agreement: rank correlation 0.85; identical cell scores 80%; every cell
within one point (`scoring.md`). Seventeen and fifteen of 80 cells were thin, mostly D5 (which functions sign
off a rule change), which no fact sheet could document well.

## 2. Hypotheses, against the pre-registered tests (revised after the red team)

The first draft of this section was more favourable than the pre-registered tests allow; `red-team.md`
shows why. The verdicts below apply the tests as written.

| ID | Verdict | Evidence |
| --- | --- | --- |
| H-lever | **Not supported as stated.** In trading the test could hardly fail (levers are coded from 1987–89), and it leaned on lever types added during coding (exchange rule, industry body, gatekeeper rule). In the grid, voluntary industry bodies (UCPTE 1951, NAPSIC 1963, NERC 1968) preceded any law by decades, which refutes it if the grid is the analogue. Several counter-examples formed without a gatekeeper, crisis or threat (airline revenue management, Google's search-quality process). **What survives (moderate):** the kind of outside pressure shapes the form a structure takes: law produced named persons and certification; industry bodies produced committees and voluntary standards | `timeline-*.csv`, `counterexamples.md`, `red-team.md` |
| H-layers | **Refuted by its own test.** The counter-example search found three moderate-to-strong cases of individuals owning cross-functional rule decisions (Mozilla's root store manager, Progressive's state product managers, Wikipedia's edit-filter managers); the test needed two. The trading rows also disagree with the hypothesis in places (rule design is mostly coded as systems; the US decider is a CEO certifying alone, with no committee). **What survives (moderate):** in large regulated firms, cross-functional rule decisions sit with named executives, boards or committees | as above |
| H-bridge | **Supported, weakly.** The certified roles are domain-tied (a registered securities trader who designs algorithms; a certified system operator); two industries are a small base | as above |
| H-lag | **Not supported; no restatement holds.** Lags depend on the start date chosen (1 year from 2009; 33 or more from 1976; five decades in the grid). "Incidents set the clock" was added after the fact and fails in places: industry controls (FIA, April 2010) preceded the Flash Crash; the 1987 crash produced no role inside firms for 17 years. **Low confidence** | as above |
| H-control | **Partly refuted.** No internal decider for pricing rules; but fraud and marketplace rules gained structures, some under outside rules and some (the Merchant Risk Council, Amazon's counterfeit unit) with no coded lever | `timeline-ecommerce-logistics.csv` |

**Choice of analogue (revised).** Trading and the grid are effectively tied: one of the two ranks first in
88% of 20,000 random weightings, and two defensible score changes put the grid first. Trading alone as
the analogue is low confidence; the pair is high confidence. The weights are not the problem: trading
still leads with equal weights and with any single dimension dropped.

**Levers can reverse (moderate).** Since 2025 the UK has consulted on cutting certification functions,
the SEC withdrew a plan to extend system-integrity rules to broker-dealers, and supervisors are adding AI
to existing reviews rather than creating roles.

## 3. Translation to companies running agents (interpretation, not finding)

How trading organised rule work for automated actors, and the counterpart for agent-run business:

| Layer | Trading today | Counterpart for agents | Exists now? | Likely lever | Estimate |
| --- | --- | --- | --- | --- | --- |
| Noticing deviations | Real-time monitoring and a kill switch per firm; first-line e-trading risk and control team, mid-level, under the markets COO | An agent risk and control team under the COO: monitors agent actions against limits, holds the kill switch, reviews exceptions | Partly: agent operations specialists, observability tools | A costly agent incident; EU AI Act Art. 26 oversight (Dec 2027); insurers | Regulated firms 2027–29; others after an incident |
| Designing limits | Pre-trade controls under the firm's "direct and exclusive control"; an inventory of algorithms; a defined "material change"; designers registered or certified | Action limits (spend, data, actions) enforced at a gateway the firm controls, not the vendor's; an agent inventory naming who may operate each agent; a definition of a material change to an agent; certification of whoever is primarily responsible for an agent's design | Partly: identity and permission consoles, agent registries (our v1 cluster C7) | Sector regulators in finance first; card networks for agents that spend | Finance 2027–28; elsewhere later or never |
| Deciding changes | CEO certifies controls yearly (US); named senior manager and board approval (UK); multi-function approval of deployments and updates (EU) | A named executive accountable for agent controls, certifying them yearly; an agent change committee where business, risk, compliance and technology each sign off their part | No, outside AI labs' scaling policies | Law with personal liability; regulated sectors first | Finance 2028–30; elsewhere only with a statute or insurer demand |
| Industry body | FIA standards (2010) before rules; FIX certification (2026) | A standards body for agent operating controls, formed before law | Forming: open agent standards bodies exist; no operating-controls standard yet | A visible incident; gatekeeper rules | 2026–28 |

**What this says about protocol vision and protocol engineering.**

1. **When stakes rise, unwritten rules get written down.** Trading's regulators required an inventory, a
   definition of material change and named operators. The tacit work of finding the rules a business runs
   on becomes, under a lever, the work of building that inventory. Protocol vision's likely institutional
   form is the inventory and its upkeep, done once well and then maintained by monitoring.
2. **Protocol engineering becomes certified practitioner work tied to a domain.** Trading registered the
   people who design and change algorithms, at mid level, under a supervising principal. The agent
   counterpart is a certified specialty inside existing functions, consistent with v1's finding that rule
   design is a duty, not a job.
3. **In large regulated firms, deciding rule changes sits above practitioners.** In trading it sits with a
   named executive, a board or a committee where each function signs off. Smaller and community
   organisations let individuals own such decisions (Mozilla, Wikipedia). A "Business Protocol Lead" in a
   large firm should prepare those decisions; in a small firm it may own them.
4. **The pressure, not the technology, shapes the structure.** Law produced named persons and
   certification; industry bodies produced committees and standards. Outside regulated finance, agent
   rule work is more likely to follow the control industry: no internal decider until outside rules arrive.
5. **Private gatekeepers may move first.** Card networks, app stores and browsers set rules for automated
   actors without law. Payment networks' rules for agents that buy are a candidate first lever (to verify).

## 3a. The chokepoint test

The red team named one piece of evidence that would most change the forecast: whether a gatekeeper
already imposes binding rules on agent actions, as exchanges do on orders (`gatekeepers.md`, all grade S).

- **Card payments: yes, reportedly.** Visa's agentic transaction rules (April 2026) reportedly bind
  agentic payment providers to cardholder consent, identity checks, instructions with an expiry and record
  keeping; Mastercard admits only registered, verified agents to Agent Pay. The Visa rule text was not seen.
- **Single platforms: yes, by contract.** Amazon requires agents to identify themselves and stop on request
  (seller agreement from March 2026); Google Play bars autonomous agent control through accessibility
  services (January 2026); Microsoft gives every new Copilot Studio agent an identity with a sponsor.
- **Agent actions in general: no.** Model providers prohibit misuse; clouds offer limits, logging and kill
  switches as options. No rule requires customers to limit, log or be able to stop their agents in general.

**Consequence for the forecast.** Trading's path (inventory, limits under the firm's control, named
owners) is likely to carry to agents that spend money or act on large platforms, and to regulated
finance. For other agent work, the control industry is the better guide: no internal decider until
outside rules arrive.

## 4. Predictions to register

| By | Prediction | Probability | Check against |
| --- | --- | --- | --- |
| End 2027 | A bank or broker regulator issues guidance requiring an inventory of AI agents with named owners and kill controls | 0.6 | FINRA, FCA, PRA, ESMA publications |
| End 2028 | A publicly reported agent incident with losses of $100m or more at a named firm | 0.4 | Press, regulator orders |
| Within 3 years of such an incident | A rule requiring certification or registration of people responsible for agent design in the affected sector | 0.5 | Regulator rulebooks |
| End 2028 | A card network publishes rules that require merchants or agent providers to limit and log agent purchases | 0.6 | Visa, Mastercard rule updates |
| End 2029 | A statute outside finance requires a named executive to certify controls on AI agents | 0.2 | Legislation trackers |

## 5. Limits

- Trading's automated actions are uniform and measured in money; business agents act across many kinds of
  work, which may delay inventories and limits.
- The dimensions and weights were ours; healthcare's last place partly reflects D1 and D6 by design.
- Two timelines and one control are a small base; the translation is a forecast.
- Agents know how these industries turned out; the scoring was blind to our hypotheses but not to history.
