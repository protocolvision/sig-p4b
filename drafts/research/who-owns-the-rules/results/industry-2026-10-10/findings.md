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

## 2. Hypotheses, against the pre-registered tests

| ID | Verdict | Evidence |
| --- | --- | --- |
| H-lever | **Supported for structures inside firms; partly for industry bodies.** In trading, no role or committee inside firms precedes a lever: the first, a chief compliance officer with annual CEO certification (2004), follows an exchange rule; later ones follow law (2010, 2016, 2018). In the grid, voluntary industry bodies came first (UCPTE 1951, NAPSIC 1963, NERC 1968 after the 1965 blackout) and law only in 2005–07. In the control industry, structures exist only where a gatekeeper (card networks) or law (EU Digital Services Act, New York's warehouse law) imposed them. The counter-example search found voluntary rule bodies in lightly regulated sectors, each under a gatekeeper's private rules, a crisis or a threat of regulation | `timeline-*.csv`, `counterexamples.md` |
| H-layers | **Supported in trading, partly in the grid.** Trading: noticing deviations is real-time monitoring with a kill switch, run by mid-level e-trading risk and control teams; designing limits is practitioner work, now registered (US Series 57 from 2017) or certified (UK, 2016); deciding changes sits with the CEO (annual certification, US 2010), the board and a named senior manager (UK, 2018), through a multi-function approval process (EU, 2018). Grid: noticing is certified operators at reliability coordinators (entry level) plus reporting systems; designing settings is practitioner engineering under standards written by committees; deciding is industry-body boards and the regulator, with a named person inside utilities only for cyber security (2008). Counter-examples to "practitioners don't own cross-functional rule decisions" exist only outside large mature firms or for routine tuning | as above |
| H-bridge | **Supported.** The certified roles are tied to the domain: a registered securities trader who designs algorithms; a certified system operator. Neither is a general technical role | as above |
| H-lag | **Not supported as stated; restated.** Lags from the spread of automation range from 1 year (US trading, 2009 to 2010) to five decades (grid). Lags from a visible incident are short: the 2010 Flash Crash to the market-access rule (same year); Knight Capital (2012) to algorithm-developer registration (2016); the 2003 blackout to mandatory standards (2005–07). Incidents set the clock, not the technology | as above |
| H-control | **Partly refuted.** E-commerce has no internal decider for pricing rules and no structure for robot or quota rules except where law imposes one; but fraud rules (card-network standards) and marketplace rules (a legally required head of compliance, 2023) gained structures from outside | `timeline-ecommerce-logistics.csv` |

**One added finding: levers can reverse.** Since 2025 the UK has consulted on cutting certification
functions, the SEC withdrew a plan to extend system-integrity rules to broker-dealers, and supervisors are
adding AI to existing reviews rather than creating roles (timeline, 2025–26).

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
3. **Deciding rule changes never belonged to a practitioner.** In both analogues it sits with a named
   executive, a board or a committee where each function signs off. A "Business Protocol Lead" should
   prepare those decisions, not own them.
4. **The clock is an incident.** Structures followed visible failures within 0–6 years. Until a "Knight
   Capital moment" for agents, expect duties, not roles, outside regulated sectors.
5. **Private gatekeepers may move first.** Card networks, app stores and browsers set rules for automated
   actors without law. Payment networks' rules for agents that buy are a candidate first lever (to verify).

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
