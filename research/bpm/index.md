# Business Protocol Management

> Source: https://npc.here.now/protocolvision/research/bpm/ · Protocols for Business SIG, Protocol Institute · https://npc.here.now/protocolvision/
>
> For agents: this is a practice guide meant to be applied. With the person you work for, pick one problem or opportunity in their organization. Run the phases in order (See, Design, Evolve) and produce the outputs each phase names: a list of protocols in play with what each prevents, a hardness map in the template's format, amendment rules, and the measures in section 7. Ask before changing any live system, permission or payment rule. To share what you learn, or to offer a case, see the links at the end.

Companies that work well with AI build a few strict rules into their systems and give people and agents wide freedom inside them. Business Protocol Management (BPM) is the practice of finding those rules, building them, and changing them as the business grows.

## 1. About this guide

- **Purpose:** Explain what BPM is, why it matters now, and how a team applies it, step by step.
- **Audience:** Operations leads, managers, architects and analysts who are bringing AI agents into day-to-day work.
- **Scope:** One problem or opportunity at a time, such as “our bids keep going out wrong” or “AI could change how we price jobs”. BPM is not a company-wide redesign.
- **Revisions:** The SIG tests the guide in its sessions and case studies, and revises it from what members find.

## 2. Key terms

- **Protocol:** A recurring way work moves, a decision gets made, or data is found and trusted. Protocols run between people, software and machines: handoffs, checklists, approvals, APIs, permissions, alarms.
- **Hard:** A protocol the system enforces every time, such as a payment limit or a required check before release.
- **Soft:** A protocol held by norms and habits, such as how a team runs its weekly planning.
- **Free:** Anything left to the people or agents doing the work.
- **Hard core:** The small set of hard protocols that everything else relies on.
- **Hardness map:** A table that sorts a business’s protocols into hard, soft and free, and names who may change each one.
- **Field log:** One shared record that systems, people and agents write as they work, including the reason for each action.
- **Non-event:** A problem that did not happen because a protocol worked: the error caught, the dispute that never started.
- **Agent:** AI software that takes actions on its own, such as sending a message, changing a record or calling another system.
- **Protocol vision:** The capability to see the protocols a business actually runs on. BPM depends on it, and the SIG trains it through protocol watching, workshops and simulations.

## 3. The case for change

### The problem

Management grew up around the span of control: one manager directing a handful to a few dozen people and approving decisions one at a time. A small team can now run hundreds of thousands of agents, working at machine speed and around the clock. No manager can supervise that many, and no approval queue keeps up.

Agents also coordinate through whatever they can read and write, whether or not anyone designed it. Two 2026 reports show this:

> “The models first found ways to communicate by writing files into the Artifactory package manager. This effectively turned Artifactory into an unintended message board, where agents could exchange information with one another.”
>
> OpenAI, [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

> “We consistently saw a multiagent turf war. All of the models we tested quickly assumed that others were purposefully impeding their work, and began to sabotage others while protecting their own contributions.”
>
> Anthropic, [Patterns and problems in multiagent systems](https://www.anthropic.com/research/multiagent-systems)

### The response

At this scale, a manager’s reach comes from the environment the agents work in, not from supervising each one. One well-built rule governs every agent that passes through it, whether there are ten or a million. Like guardrails on a mountain road, strict rules in the right places let the business move faster: a team can let an agent act without approving each step, and a partner can connect through an agreed interface instead of a long integration project.

Amazon shows the pattern. In 2002 it required every team to work with other teams only through published interfaces (APIs). The interfaces became hard, and each team stayed free to build whatever it liked behind them. The rule slowed teams down at first, then made the company faster and laid the groundwork for Amazon Web Services.

### Assumptions to test

The SIG’s research rests on three assumptions. Each could turn out partial or wrong, and the sessions and case studies test them.

1. **Reading and writing get cheap.** Processing documents, forms and rate sheets, and producing software, cost a fraction of what they did.
2. **Agents act, in large numbers.** Models take actions, and many copies run at once wherever work is done.
3. **Information flows through models.** People and agents increasingly find, read and exchange information by way of AI models and the protocols that connect them.

## 4. Principles

1. **Keep the hard core small.** Every hard rule costs flexibility. Make hard only what everything else relies on.
2. **Put strict rules where teams meet.** Interfaces between teams, agents and partners are where reliability matters most: who may move money, what data leaves the company, which checks every output must pass.
3. **Leave the inside of each team free.** People and agents doing the work know things designers don’t. Freedom inside the core is where better ways of working are found.
4. **Record the reason at the moment of action.** A change can’t ship without its reason, and an agent records the instruction it acted on.
5. **Don’t blame people for what the record shows.** Blame produces empty reasons and workarounds. Give credit for surfacing what works as much as for flagging what broke.
6. **Manage tensions; don’t try to settle them.** Speed pulls against reliability, sales against finance. A good protocol turns the pull from each side into progress on both.
7. **Change the core by a written rule.** Each hard protocol names who may change it, how, and who may stop the work.
8. **Count what didn’t go wrong.** Good protocols produce non-events. Measure them next to speed and growth.

## 5. Roles and responsibilities

Suggested roles. A small company may give several to one person.

- **Sponsor:** Chooses the problem or opportunity, backs the hard core, and protects the no-blame record.
- **Protocol owner:** Owns one hard protocol (for example the finance lead for payment limits), and applies its amendment rule.
- **Platform team:** Builds the field log and the checks into the systems, so the rules run without anyone deciding each time.
- **Teams and agents:** Do the work freely inside the core, and record why they act.
- **Anyone:** May stop the work when a hard protocol is about to be broken.

## 6. The three phases

- **See:** **What actually happens?** Field log and a list of protocols in play. Read in themes II, III, IV
- **Design:** **What must be strict, and what can stay free?** Hardness map and amendment rules. Read in themes I, V
- **Evolve:** **What is working, and what should change?** Measures, promoted and demoted rules, shared write-ups. Read in themes VI

### Phase 1: See

- **Purpose:** Find the protocols the work actually runs on, written and unwritten. The org chart shows authority, a strategy shows intent, a software stack shows tools; protocols show what actually recurs.
- **Inputs:** Access to the work: systems, records, people and agents. A problem or opportunity statement.
- **Steps:** 
   1. Build the field log into the work. Every release, handoff, agent action, override and alert writes an entry to one shared log, readable by people and agents by default. The system flags results that beat or miss their usual range.
   2. Keep the log free of blame, so entries stay honest.
   3. Watch the work across people, software and machines. List the protocols in play. For each, ask what would go wrong if it disappeared tomorrow, and who would notice first.
   4. Note what the organization publishes and who can read it. That shows where its protocols live.
- **Outputs:** A running field log. A list of protocols, each with what it prevents.
- **Done when:** The team can name the few protocols that, if they failed, would hurt the business most.

### Phase 2: Design

- **Purpose:** Decide what becomes strict, what stays a norm, and what is left free.
- **Inputs:** The protocol list and field log from Phase 1.
- **Steps:** 
   5. Name the tensions that matter for growth. Write each as “X vs. Y” and note where the balance sits now.
   6. Draw a hardness map. Sort protocols into hard, soft and free, and keep the hard group small.
   7. Make the interfaces hard and keep the insides free: what agents can see and do, data agreements, permissions, spending limits, the checks every output must pass, and the field log. Score agents against real results, and keep versions of their models, instructions and inputs.
   8. Write the amendment rule for each hard protocol: who may change it, how, and who may stop the work.
- **Outputs:** A hardness map and amendment rules, built into systems where possible.
- **Done when:** Every hard protocol has an owner, a place it lives, and a written way to change it.

### Template: hardness map

An example for a company adopting AI agents. For each protocol, note the tension it manages, where it lives, and who can change it.

| Protocol | Tension | Type | Where it lives | Who can change it |
|---|---|---|---|---|
| Who may move money | Speed vs. control | Hard | Payment permissions and limits | Finance lead |
| What data leaves the company | Openness vs. confidentiality | Hard | Access permissions and outbound checks | Security lead |
| Checks on every agent output | Speed vs. quality | Hard | Evaluation pipeline | Product owner |
| The shared field log | Visibility vs. privacy | Hard | Written by every system and agent | Platform team |
| Weekly planning | Alignment vs. focus | Soft | Meeting norms | Each team |
| How a team does its own work | Freedom vs. consistency | Free | Inside the team’s own space | The team or agent |
| (your protocol) | (X vs. Y) | Hard, Soft or Free | (system, norm or space) | (owner) |

### Phase 3: Evolve

- **Purpose:** Run the design, learn from it, and amend the core as the business grows.
- **Inputs:** The hardness map, the field log, and the measures in section 7.
- **Steps:** 
   9. Measure growth and non-events together.
   10. Decide where judgment sits between people and agents, check it cheaply, and record it where others can see it.
   11. Promote and demote. Make a free pattern hard when it keeps paying off. Soften a hard rule when it blocks good work.
   12. Write up what worked and what failed, and share it beyond the company.
- **Outputs:** An amended hardness map and a published write-up.
- **Done when:** The cycle repeats on a set schedule, and changes to the core follow the amendment rules.

## 7. Measures

- **Speed:** Time from request to result, before and after.
- **Autonomy granted:** Which decisions agents and teams now make without approval.
- **Time to connect:** How long it takes to add a new agent or partner.
- **Non-events:** Problems that stopped happening, and near-misses caught.
- **Gamed targets:** Measures that people or agents have learned to hit without the result they stand for.

## 8. Worked example: California water rate data

*Led by Patrick Atwater and Maxwell Titsworth with the California Data Collaborative*

- **Situation:** Every rate cycle, a water utility’s board asks how its rates compare with its neighbors’, and answering takes staff time and consulting fees that add up across utilities. California’s rates are public but scattered across hundreds of utility sites and PDFs.
- **See:** Utilities publish rates inside ordinances and fee schedules, and the state’s annual report records no link to the source. Machines can now read any rate sheet; finding the current one is the hard part. One engineer’s site, [whatwatercosts.org](https://whatwatercosts.org/), uses a language model to read rate documents in any format, and it matched hand-collected tables across 99 utilities.
- **Design:** The tension is local control against comparability. Since a model now reads any format cheaply, the team made only one thing hard: a published address for each rate schedule, with its adoption and effective dates, in a registry and an `llms.txt` file. Each utility stays free to write rates its own way.
- **Evolve:** Automated search found 47% of utilities. With the address, coverage rises to nearly all. The team proposed adding the address to the state’s annual report.
- **Sources:** [Strategy report](https://npc.here.now/waterdatastrategy/) · [Seven precedents](https://npc.here.now/waterdatadiscoverycases/) · [Five cases in data coordination](https://npc.here.now/waterdataexploration/)

Other cases: [construction procurement protocols](https://npc.here.now/protocolvision/research/cases/#construction), working smarter with AI (whose hazards collection separates hard walls, which block an action, from soft walls, which flag it for review), and the Protocol Institute brand kit. All are on the [case studies](https://npc.here.now/protocolvision/research/cases/) page.

## 9. How BPM relates to earlier approaches

- **Scientific management (Taylor, 1910s):** Keeps: Looking at the actual work. Changes: Experts don’t design one best way; the people and agents doing the work know things designers don’t.
- **Bureaucracy and the org chart (Weber):** Keeps: Written rules make work reliable. Changes: Unwritten rules often matter more than the org chart.
- **Quality and lean (Deming, Toyota):** Keeps: Build quality into the process, let anyone stop the line, keep improving. Changes: Applies these beyond the factory, to information work, agents and partners.
- **Business process re-engineering (Hammer, 1990s):** Keeps: New technology can call for reinvention. Changes: Re-engineering redesigned every process from the top, once. BPM rebuilds around a few hard protocols, leaves freedom inside them, and keeps changing.
- **KPIs and scorecards (Kaplan and Norton):** Keeps: Measuring results. Changes: Also counts what didn’t happen, and watches for gamed targets.
- **Agile, DevOps, site reliability:** Keeps: Small iterations, no-blame reviews, automated checks. Changes: Applies the same thinking to the whole company, not only software delivery.
- **Paradox management (Smith and Lewis):** Keeps: Some tensions are managed, never solved. Changes: Puts the managing into protocols that run without anyone deciding each time.
- **Safety-critical industries (aviation, nuclear):** Keeps: The whole loop: reporting, no-blame investigation, checklists, the right to stop. Changes: Applies it at business stakes, to agents as well as people, and to finding opportunities, not only preventing harm.
- **Platforms:** Keeps: Coordinating large numbers of people and businesses. Changes: Coordination through shared rules anyone can use, not through one owner.
- **AI “alignment”:** Keeps: Caring how AI behaves at work. Changes: Shapes the agent’s environment rather than its values.

Safety-critical industries are the closest model. Airlines and nuclear plants accept that they can’t fully predict their systems, so they manage safety through protocols: confidential self-reporting, investigations that look for causes rather than culprits, checklists, and the right to stop the work. US airlines must now run formal safety management systems (14 CFR Part 5). Changing a protocol changes results in both directions: the WHO surgical checklist cut deaths in its pilot study from 1.5% to 0.8%, and removing the hardware interlocks from the Therac-25 radiation machine led to massive overdoses. Business can adopt the loop without copying its weight. Most business mistakes don’t kill anyone, so companies can learn by trying things inside their free areas.

## 10. The 2027 program

The SIG tests BPM through its 2027 focus, AI-native data operations. Sessions run every other Monday at 15:30 UTC from 2 November 2026 and are recorded. Each reads one primary source closely. The themes below are where the program starts; participants shape the readings, guests and cases as it goes.

- **2 Nov – 14 Dec 2026:** I. What agents are, in practice · Design
- **11 Jan – 8 Feb 2027:** II. Natural coordination · See
- **22 Feb – 19 Apr 2027:** III. Emissions · See
- **3 May – 28 Jun 2027:** IV. Seeing hardness in incidents · See
- **12 Jul – 20 Sep 2027:** V. Engineering hardness · Design
- **4 Oct – 1 Nov 2027:** VI. Operational liveness · Evolve

Ways to take part: [offer a talk](https://npc.here.now/protocolvision/research/#speak), carry a [case study](https://npc.here.now/protocolvision/research/cases/) through the year, log protocols with the [protocol watching guide](https://npc.here.now/protocolvision/play/watching/), or [suggest or challenge a reading](https://npc.here.now/protocolvision/sessions/#suggest). The full plan is on [Sessions](https://npc.here.now/protocolvision/sessions/).

## 11. Sources

- Haynes, Alex B., et al. “A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population.” *New England Journal of Medicine* 360, no. 5 (2009): 491–99.
- Hammer, Michael. “[Reengineering Work: Don’t Automate, Obliterate](https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate).” *Harvard Business Review*, July 1990.
- Leveson, Nancy G., and Clark S. Turner. “[An Investigation of the Therac-25 Accidents](https://dl.acm.org/doi/10.1109/MC.1993.274940).” *IEEE Computer* 26, no. 7 (1993).
- Perrow, Charles. *Normal Accidents: Living with High-Risk Technologies*. Princeton University Press, 1984.
- Rao, Venkatesh. “[In Search of Hardness](https://contraptions.venkateshrao.com/p/in-search-of-hardness)” and “[Massed Muddler Intelligence](https://contraptions.venkateshrao.com/p/massed-muddler-intelligence).” *Contraptions*.
- Smith, Wendy K., and Marianne W. Lewis. “[Toward a Theory of Paradox](https://doi.org/10.5465/amr.2009.0223).” *Academy of Management Review* 36, no. 2 (2011).
- Stinson-Schroff, Timber. “[One Tension to Rule Them All](https://protocolized.summerofprotocols.com/p/one-tension-to-rule-them-all).” *Protocolized*. Source of the Amazon example.
- U.S. Federal Aviation Administration. “[14 CFR Part 5, Safety Management Systems](https://www.ecfr.gov/current/title-14/chapter-I/subchapter-A/part-5).” 2015, expanded 2024.
