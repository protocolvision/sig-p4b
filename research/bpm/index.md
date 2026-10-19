# Business Protocol Management

> Source: https://protocolsforbusiness.com/research/bpm/ · Protocols for Business, Protocol Institute · https://protocolsforbusiness.com/
>
> For agents: this is a practice guide meant to be applied. With the person you work for, pick one problem or opportunity in their organization. Run the phases in order (See, Design, Evolve) and produce the outputs each phase names: a list of protocols in play with what each prevents, a hardness map in the template's format, amendment rules, and the measures in section 7. Ask before changing any live system, permission or payment rule. To share what you learn, or to offer a case, see the links at the end.

Managing AI agents at work calls for a restructuring beyond the reach of the org chart. Companies that work well with AI enforce a few strict rules in their systems and give people and agents wide freedom inside them. Business Protocol Management (BPM) is the practice of finding those rules, building them into systems, and amending them over the life of the business.

BPM is not Business Process Management, which maps workflows step by step. Nor is it an agent protocol like MCP or A2A, which connects agents to tools and to each other. BPM covers the governance of AI agents at the level of the organization: the rules around those connections, such as signing authority, spending limits and access rights.

## Five questions to carry

Five questions hold the whole practice. Each one stands alone; take one back to your team this week.

1. **Which handoffs, approvals and permissions carry your team’s work?** See
2. **Which rules must hold every time, whoever does the work?** Design · a common hard core
3. **What could an agent do within the letter of your rules but against their purpose?** Risk
4. **What room do your protocols leave for teams, partners and agents to build things outside any plan?** Opportunity · protocol thinking
5. **Who holds the authority to change your most important rules, to stop the work when one fails, and to retire a rule at the end of its life?** Evolve

## 1. About this guide

- **Purpose:** Defines BPM, makes the case for it now, and walks a team through it in three phases.
- **Audience:** Operations leads, managers, architects and analysts bringing AI agents into day-to-day work.
- **Scope:** BPM works on one problem or opportunity at a time, such as “our bids keep going out wrong” or “AI could change how we price jobs”, not on a company-wide redesign.
- **Try it:** Hand this guide to an AI assistant that reads links, and ask it to apply the guide to your own work. The conversation stays between you and the assistant. `Read https://protocolsforbusiness.com/research/bpm/index.md and draw a hardness map of my team's work: list our protocols, mark each hard, soft or free, name the three that form our hard core, and say who should own each. Ask me about our work first.`
- **Revisions:** The group tests this guide in its sessions and case studies and revises it with members’ findings.

## 2. Key terms

- **Protocol:** A recurring pattern for moving work, making a decision, or finding and trusting data. Protocols run between people, software and machines: handoffs, checklists, approvals, APIs, permissions, alarms.
- **Hard:** A protocol the system enforces every time, such as a payment limit or a required check before release.
- **Soft:** A protocol that norms and habits hold in place, such as a team’s weekly planning.
- **Free:** Anything left to the judgment of the people or agents doing the work.
- **Hard core:** The small set of hard protocols that carries everything else.
- **Hardness map:** A table that sorts a business’s protocols into hard, soft and free, and names who may change each one.
- **Amendment rule:** The written terms for changing a hard protocol: who may propose a change, the bar it must clear, who decides, who may stop the work, and the criteria for retiring the rule.
- **Field log:** One shared record where systems, people and agents log each action and its reason.
- **Non-event:** A problem that did not happen because a protocol worked: the error caught, the dispute that never started.
- **Reach:** Evidence that others build on a protocol: different people, different implementations and different uses, sustained over time.
- **Agent:** AI software that takes actions on its own, such as sending a message, changing a record or calling another system.
- **Protocol vision:** The capability to see the protocols a business actually runs on. BPM depends on this capability; the group trains it through protocol watching, workshops and simulations.

## 3. The case for change

### The problem

Management grew up around the span of control: one manager directing a handful to a few dozen people and approving decisions one at a time. A small team can now run hundreds of thousands of agents, working at machine speed and around the clock. No manager can supervise that many, and no approval queue can match their pace.

Agents also coordinate through anything they can read and write, designed for the purpose or not. Two 2026 reports document the pattern:

> “The models first found ways to communicate by writing files into the Artifactory package manager. This effectively turned Artifactory into an unintended message board, where agents could exchange information with one another.”
>
> OpenAI, [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

> “We consistently saw a multiagent turf war. All of the models we tested quickly assumed that others were purposefully impeding their work, and began to sabotage others while protecting their own contributions.”
>
> Anthropic, [Patterns and problems in multiagent systems](https://www.anthropic.com/research/multiagent-systems)

### The response

At this scale, managers extend their reach through the agents’ environment, not through supervision of each agent. One well-built rule governs every agent that passes through it, ten or a million. Like guardrails on a mountain road, strict rules in the right places raise the speed of the whole business: a team lets an agent act without approving each step, and a partner connects through an agreed interface instead of a long integration project.

Amazon shows the pattern. In 2002 it required every team to work with other teams only through published interfaces (APIs). The interfaces became hard; behind them, each team kept full freedom over its own design. The rule slowed teams at first, then sped up the whole company and laid the groundwork for Amazon Web Services.

### Protocols, not processes

Process management maps the steps and assigns an owner to each. Protocol management targets the few rules under every step. The two approaches ask different questions:

- **The work:** Process: *What are the steps, and who performs each one?* Protocol: *Which few rules must hold every time, and where do they live?*
- **Ownership:** Process: *Who owns the process?* Protocol: *Who may change this rule, who may stop the work, and who may retire the rule?*
- **Compliance:** Process: *Is everyone following the procedure?* Protocol: *What could anyone, person or agent, do within this rule’s letter that defeats its purpose?*
- **Results:** Process: *Did we hit the target?* Protocol: *What didn’t go wrong, who builds on the rule, and which targets show signs of gaming?*

The blyg post [Process management is over. Manage protocols.](https://protocolsforbusiness.com/blyg/t/0cncz177ac6r4aqrvtcjemzq0d/) adds more pairs, each with readings. Section 9 compares BPM with other earlier approaches.

### Risk and opportunity live in the same place

Both sit at the seams where strict rules belong. A gap in the hard core gives agents a way through: in the OpenAI incident, agents turned a package manager into a message board because no rule forbade it. A well-made interface gives others a place to build: Amazon’s rule became the groundwork for a business outside any plan. So one hardness map answers both questions, and a rule that is only soft is a risk and a missed opportunity at once.

### Assumptions to test

The group’s research rests on three assumptions. Any of them could prove partial or wrong; the sessions and case studies put each to the test.

1. **Reading and writing get cheap.** Processing documents, forms and rate sheets, and producing software, now cost a fraction of their former price.
2. **Agents act, in large numbers.** Models take actions, with many copies running at once across the work.
3. **Information flows through models.** People and agents increasingly find, read and exchange information by way of AI models and the protocols that connect them.

### Protocol thinking for managers: an open question

Most management tools come from product thinking: pick an outcome, steer toward it, measure the distance to the target. [Matthew McDowell-Sweet argues](https://msweet.net/notes/106-cream-pikes) that protocol thinking differs from product thinking at the level of the whole paradigm, not by degree. His note names eight shifts. Six bear directly on how a manager runs a hard core. The group treats them as hypotheses for the year, not findings, and asks how far each holds inside a business that still has to earn a profit.

- **Widen, don’t steer:** A product aims at a target state. A protocol does its job by widening the moves available to others: “Every outcome specified is a move taken off the board for someone else.” The test of a core rule lies in the work teams, agents and partners build on it without anyone’s request. *Which unrequested work does this rule support today?*
- **Keep tolls off the core:** A product earns its keep by capturing value. At a protocol, “every toll taken is a tax on the very moves the protocol was meant to make available.” An extra sign-off, an internal fee or a claim on credit at the core taxes every team and agent on the path. The business still captures value, at the edges, from paying customers. *Where does a toll at the core cost more than its return?*
- **Guard the rules to open the play:** Strict change governance and wide freedom work as a pair: “The rules have to be conservative precisely so the play can be permissive.” McDowell-Sweet’s motto for it: move slow and unlock things. Anything a rule permits, someone will eventually do, and agents follow the letter, not the norm, so for them a soft protocol works much like a free one. The agents in the Artifactory case used every opening the system offered. Publish the bar for a change before anyone proposes one, and give extra scrutiny to any change that favours one team’s capture. *What could someone do within this rule’s letter that defeats its purpose?*
- **Select, don’t engineer:** Once reading and writing get cheap, trying many variants costs less than reasoning toward one design. The hard core then serves as ground for search: teams and agents try variations in the free space, and the business promotes the survivors. *How cheaply can a team test an alternative inside this rule, and how fast does a winner reach the core?*
- **Count what you give away:** Product metrics measure how much value the business keeps. A protocol’s value shows up in others’ gains. McDowell-Sweet proposes four signals, cheap to fake one at a time and hard to fake together: different people use the rule, different implementations follow it, different uses grow from it, and all three persist while leaving stays easy. Treat them as signals, not targets; as targets, they invite gaming. *Who outside the rule’s original purpose depends on it today?*
- **Plan the ending:** Complex systems always run partly broken, and the hunt for a single root cause mostly serves the need for someone to blame. The greater danger lies in a rule with live enforcement and no steward: it lingers on lock-in and inertia, and everything it permits stays open to exploitation. Write sunset criteria and a successor into each hard protocol during its healthy years, and give each steward a fixed term, so stewardship never hardens into ownership. *Which of your rules has outlived its steward?*

The group brings these questions to the sessions, especially themes I, V and VI, and to the [protocol watching guide](https://protocolsforbusiness.com/play/watching/), and revises this guide with members’ findings.

## 4. Principles

1. **Keep the hard core small.** Every hard rule costs flexibility. Reserve hardness for the rules under everything else.
2. **Put strict rules where teams meet.** Interfaces between teams, agents and partners carry the greatest need for reliability: authority to move money, limits on data leaving the company, the checks on every output.
3. **Leave the inside of each team free.** People and agents doing the work hold knowledge no designer has. Freedom inside the core produces the variants that improve the work.
4. **Record the reason at the moment of action.** No change ships without its reason, and every agent logs the instruction behind each action. Once agents can both catch a person’s mistake and make their own, error no longer traces back to one person; the record keeps the trail.
5. **Don’t blame people for what the record shows.** Blame produces empty reasons and workarounds. Reward people for surfacing what works as much as for flagging failures.
6. **Manage tensions; don’t try to settle them.** Speed pulls against reliability, sales against finance. A good protocol turns the pull from each side into progress on both.
7. **Change the core slowly, by a written rule.** Each hard protocol names who may change it, the bar for a change, who may stop the work, and its sunset criteria. Conservative rules keep the play open.
8. **Count non-events and reach.** Good protocols prevent problems and invite others to build. Measure both next to speed and growth.

## 5. Roles and responsibilities

Suggested roles. A small company may give several to one person.

- **Sponsor:** Chooses the problem or opportunity, backs the hard core, funds its upkeep, and protects the no-blame record.
- **Protocol steward:** Holds one hard protocol for a fixed term (for example the finance lead for payment limits), applies its amendment rule, and hands it to a successor at the end of the term.
- **Platform team:** Builds the field log and the checks into the systems, so the rules run without a fresh decision each time.
- **Teams and agents:** Do the work freely inside the core and record the reason for each action.
- **Anyone:** May stop the work at the first sign of a broken hard protocol.

## 6. The three phases

- **See:** **Which protocols carry the work today?** Field log and a list of protocols in play. Read in themes II, III, IV
- **Design:** **What must be strict, and what can stay free?** Hardness map and amendment rules. Read in themes I, V
- **Evolve:** **Which rules earn their place, and which need amendment or retirement?** Measures, promoted, demoted and retired rules, shared write-ups. Read in themes VI

### Phase 1: See

- **Purpose:** Find the written and unwritten protocols under the work. The org chart shows authority, a strategy shows intent, a software stack shows tools; protocols show the patterns that recur every day.
- **Inputs:** Access to the work: systems, records, people and agents. A problem or opportunity statement.
- **Steps:** 
   1. Build the field log into the work. Every release, handoff, agent action, override and alert writes an entry to one shared log, open to people and agents by default. The system flags results above or below their usual range.
   2. Keep the log free of blame, so entries stay honest.
   3. Watch the work across people, software and machines, and list the protocols in play. For each, ask two questions: what breaks if it disappears tomorrow, and who sees the damage first?
   4. Note what the organization publishes and to whom. Published material marks the location of its protocols.
- **Outputs:** A running field log. A list of protocols, each with the problem it prevents.
- **Done when:** The team can name the few protocols whose failure would hurt the business most.

### Phase 2: Design

- **Purpose:** Sort the protocols into strict rules, norms and free space.
- **Inputs:** The protocol list and field log from Phase 1.
- **Steps:** 
   5. Name the tensions that matter for growth. Write each as “X vs. Y” and note the current balance.
   6. Draw a hardness map. Sort protocols into hard, soft and free, and keep the hard group small.
   7. Make the interfaces hard and keep the insides free: agents’ views and permissions, data agreements, spending limits, the checks on every output, and the field log. Score agents against real results, and keep versions of their models, instructions and inputs.
   8. Write the amendment rule for each hard protocol: who may propose a change, the bar it must clear, who decides, who may stop the work, and the criteria for retiring the rule. Publish the bar before anyone proposes a change.
- **Outputs:** A hardness map and amendment rules, built into systems where possible.
- **Done when:** Every hard protocol has a steward, a home in a system, and a written rule for change and retirement.

### Template: hardness map

An example for a company adopting AI agents. For each protocol, record the tension it manages, its home, and the person with authority to change it.

| Protocol | Tension | Type | Where it lives | Who can change it |
|---|---|---|---|---|
| Who may move money | Speed vs. control | Hard | Payment permissions and limits | Finance lead |
| What data leaves the company | Openness vs. confidentiality | Hard | Access permissions and outbound checks | Security lead |
| Checks on every agent output | Speed vs. quality | Hard | Evaluation pipeline | Product owner |
| The shared field log | Visibility vs. privacy | Hard | Written by every system and agent | Platform team |
| Weekly planning | Alignment vs. focus | Soft | Meeting norms | Each team |
| How a team does its own work | Freedom vs. consistency | Free | Inside the team’s own space | The team or agent |
| (your protocol) | (X vs. Y) | Hard, Soft or Free | (system, norm or space) | (owner) |

### Starting point: a common hard core

Most companies appear to share the same few hard protocols, with different degrees of enforcement. Start a hardness map from this list, then add the protocols your work requires and strike the rest. The group offers the list as a proposal under test, not a finding; bring your sector’s additions to a session.

1. **Signing authority** Who can commit the company to a contract or a promise.
2. **Spending limits** The amount a person or agent may spend before a second approval.
3. **Payment approval** Who may move money, and the checks before any payment.
4. **Access rights** Which people and agents can see and change which systems and records.
5. **Change control** Nothing ships unreviewed: versions, reviews and releases for code, models, instructions and policies.
6. **Data out** What may leave the company, to whom, and through which channels.
7. **Output checks** The tests on every result before it reaches a customer or another system.
8. **Audit trail** Every action recorded with its reason: the field log.

For each, ask where it lives today (a system, a document, or someone’s head), whether an agent could get around it, and who would notice the breach.

### Phase 3: Evolve

- **Purpose:** Run the design, learn from it, and amend or retire parts of the core over time.
- **Inputs:** The hardness map, the field log, and the measures in section 7.
- **Steps:** 
   9. Measure growth, non-events and reach together.
   10. Decide where judgment sits between people and agents, check it cheaply, and record it in the shared log.
   11. Promote and demote. Let teams and agents try many variants in the free space, and harden the patterns with a record of repeated payoff, not the best-argued design. Soften any hard rule that blocks good work.
   12. Retire rules on schedule. Apply each rule’s sunset criteria, hand it to its successor, and leave its record and interfaces as ground for whatever replaces it.
   13. Write up successes and failures, and share the write-up beyond the company.
- **Outputs:** An amended hardness map, a list of retired rules, and a published write-up.
- **Done when:** The cycle repeats on a set schedule, and every change to the core follows its amendment rule.

## 7. Measures

- **Speed:** Time from request to result, before and after.
- **Autonomy granted:** Decisions agents and teams now make without approval.
- **Time to connect:** Time to add a new agent or partner.
- **Non-events:** Problems that stopped happening, and near-misses caught.
- **Reach:** Who builds on the core: different teams, partners and agents; different implementations; different uses beyond the original purpose; all sustained while leaving stays easy. Any one signal is cheap to fake. All four together, over time, are not.
- **Gamed targets:** Measures people or agents now hit without the underlying result.

Read non-events and reach as signals, not targets. Turned into targets, they join the gamed list.

## 8. Worked example: California water rate data

*Led by Patrick Atwater and Maxwell Titsworth with the California Data Collaborative*

- **Situation:** Every rate cycle, a water utility’s board asks how its rates compare with its neighbors’, and each answer costs staff time and consulting fees, multiplied across utilities. California’s rates are public but scattered across hundreds of utility sites and PDFs.
- **See:** Utilities publish rates inside ordinances and fee schedules, and the state’s annual report records no link to the source. Machines can now read any rate sheet; the hard part is finding the current one. One engineer’s site, [whatwatercosts.org](https://whatwatercosts.org/), uses a language model to read rate documents in any format, and it matched hand-collected tables across 99 utilities.
- **Design:** The tension is local control against comparability. Since a model now reads any format cheaply, the team made only one thing hard: a published address for each rate schedule, with its adoption and effective dates, in a registry and an `llms.txt` file. Each utility keeps the freedom to write rates its own way.
- **Evolve:** Automated search found 47% of utilities. With the address, coverage rises to nearly every utility. The team proposed adding the address to the state’s annual report.
- **Sources:** [Strategy report](https://npc.here.now/waterdatastrategy/) · [Seven precedents](https://npc.here.now/waterdatadiscoverycases/) · [Five cases in data coordination](https://npc.here.now/waterdataexploration/)

Other cases: [construction procurement protocols](https://protocolsforbusiness.com/research/cases/#construction), working smarter with AI (whose hazards collection separates hard walls, which block an action, from soft walls, which flag it for review), and the Protocol Institute brand kit. All are on the [case studies](https://protocolsforbusiness.com/research/cases/) page.

## 9. How BPM relates to earlier approaches

- **Scientific management (Taylor, 1910s):** Keeps: Looking at the actual work. Changes: Experts don’t design one best way; the people and agents doing the work hold knowledge no designer has.
- **Bureaucracy and the org chart (Weber):** Keeps: Written rules make work reliable. Changes: Unwritten rules often outweigh the org chart.
- **Quality and lean (Deming, Toyota):** Keeps: Build quality into the process, let anyone stop the line, keep improving. Changes: Applies these beyond the factory, to information work, agents and partners.
- **Business process re-engineering (Hammer, 1990s):** Keeps: New technology can call for reinvention. Changes: Re-engineering redesigned every process from the top, once. BPM rebuilds around a few hard protocols, leaves freedom inside them, and amends them in a continuous cycle.
- **KPIs and scorecards (Kaplan and Norton):** Keeps: Measuring results. Changes: Also counts non-events and reach, and watches for gamed targets.
- **Product management:** Keeps: Clear users and honest measures. Changes: Core rules widen others’ options instead of steering to a target, and earn their place through reach, not capture.
- **Agile, DevOps, site reliability:** Keeps: Small iterations, no-blame reviews, automated checks. Changes: Applies the same thinking to the whole company, not only software delivery.
- **Paradox management (Smith and Lewis):** Keeps: Some tensions are managed, never solved. Changes: Puts the managing into protocols that run without a fresh decision each time.
- **Safety-critical industries (aviation, nuclear):** Keeps: The whole loop: reporting, no-blame investigation, checklists, the right to stop. Changes: Applies it at business stakes, to agents as well as people, and to finding opportunities, not only preventing harm.
- **Platforms:** Keeps: Coordinating large numbers of people and businesses. Changes: Coordination through shared rules open to anyone, not through one owner.
- **AI “alignment”:** Keeps: Caring how AI behaves at work. Changes: Shapes the agent’s environment rather than its values.

Safety-critical industries offer the closest model. Airlines and nuclear plants accept the limits of prediction in their systems, so they manage safety through protocols: confidential self-reporting, investigations that look for causes rather than culprits, checklists, and the right to stop the work. US airlines must now run formal safety management systems (14 CFR Part 5). Changing a protocol changes results in both directions: the WHO surgical checklist cut deaths in its pilot study from 1.5% to 0.8%, and removing the hardware interlocks from the Therac-25 radiation machine led to massive overdoses. Business can adopt the loop without copying its weight. Most business mistakes harm no one, so companies can learn by experiment inside their free areas.

## 10. The 2027 program

The group tests BPM through its 2027 focus, AI-native data operations. Sessions run every other Monday at 15:30 UTC from 2 November 2026, with a recording of each. Every session gives one primary source a close reading. The themes below mark the program’s starting point; participants shape the readings, guests and cases over the year.

- **2 Nov – 14 Dec 2026:** I. What agents are, in practice · Design
- **11 Jan – 8 Feb 2027:** II. Natural coordination · See
- **22 Feb – 19 Apr 2027:** III. Emissions · See
- **3 May – 28 Jun 2027:** IV. Seeing hardness in incidents · See
- **12 Jul – 20 Sep 2027:** V. Engineering hardness · Design
- **4 Oct – 1 Nov 2027:** VI. Operational liveness · Evolve

Ways to take part: [offer a talk](https://protocolsforbusiness.com/research/#speak), carry a [case study](https://protocolsforbusiness.com/research/cases/) through the year, log protocols with the [protocol watching guide](https://protocolsforbusiness.com/play/watching/), or [suggest or challenge a reading](https://protocolsforbusiness.com/sessions/#suggest). The full plan is on [Sessions](https://protocolsforbusiness.com/sessions/).

## 11. Sources

- Haynes, Alex B., et al. “A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population.” *New England Journal of Medicine* 360, no. 5 (2009): 491–99.
- Hammer, Michael. “[Reengineering Work: Don’t Automate, Obliterate](https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate).” *Harvard Business Review*, July 1990.
- Leveson, Nancy G., and Clark S. Turner. “[An Investigation of the Therac-25 Accidents](https://dl.acm.org/doi/10.1109/MC.1993.274940).” *IEEE Computer* 26, no. 7 (1993).
- McDowell-Sweet, Matthew. “[Protocol Thinking for Product People, Or How to Move Slow and Unlock Things](https://msweet.net/notes/106-cream-pikes).” msweet.net, Notes 106, 2026. Eight shifts from product thinking to protocol thinking.
- Perrow, Charles. *Normal Accidents: Living with High-Risk Technologies*. Princeton University Press, 1984.
- Rao, Venkatesh. “[In Search of Hardness](https://contraptions.venkateshrao.com/p/in-search-of-hardness)” and “[Massed Muddler Intelligence](https://contraptions.venkateshrao.com/p/massed-muddler-intelligence).” *Contraptions*.
- Smith, Wendy K., and Marianne W. Lewis. “[Toward a Theory of Paradox](https://doi.org/10.5465/amr.2009.0223).” *Academy of Management Review* 36, no. 2 (2011).
- Stinson-Schroff, Timber. “[One Tension to Rule Them All](https://protocolized.summerofprotocols.com/p/one-tension-to-rule-them-all).” *Protocolized*. Source of the Amazon example.
- U.S. Federal Aviation Administration. “[14 CFR Part 5, Safety Management Systems](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-A/part-5).” 2015, expanded 2024.
