# The Business Protocol Lead, critiqued, and the roles we expect for 2027–2029

Research draft, v3 · 10 October 2026 · Protocols for Business · for review before any post

> **Status.** Working notes. This critiques the job description published on the blyg as "A job
> description for a Business Protocol Lead" (`blyg-src/threads/job-protocol-operations-lead.md`), using
> the tests in [`role-emergence.md`](role-emergence.md) (v6). Sources are cited there; (S) and (M) mean the
> same thing. Projections are judgments with rough probabilities.
>
> **What changed from v1.** v1 objected that three to five years' experience was too junior. The
> seniority evidence (role-emergence, section 6) shows most lasting roles started with junior or mid-level
> practitioners, whose authority came from a rule a senior sponsor signed. That objection is withdrawn and
> replaced by the missing agreement. v2 separated protocol work from agent management; v3 applies an
> operations executive's review: the role is for cross-functional rules only, the metric needs a
> threshold and open-case counts, and the autonomy budget is narrowed to workflows with counted losses.

## 1. What the post proposes

An exploratory role, three to five years' experience, reporting to the COO. Its job is to find the rules a
business actually runs on and rethink them as agents arrive: follow real work end to end; read agent traces
as field notes; keep an open map of protocols; choose questions with the COO each quarter; run experiments
that loosen or harden a rule; prototype interfaces others can build on; review new agents with security;
run blameless incident reviews; write monthly field notes. "Security, finance and legal decide what the
rules say; engineering builds them; you bring back what's true on the ground."

## 2. Scored against the lineage tests

| Test | How the post scores | Why |
| --- | --- | --- |
| A capability makes new work cheap | Pass | Agents make enforced rules cheap to run and expose unwritten ones quickly |
| A cost lands between functions, and someone senior asks | Pass | Approvals, limits and data rules sit across sales, finance, security and legal; the COO asks |
| Permanent trade-off, not a migration | Partial | The post frames the role around "AI adoption", a migration. Revenue against risk is permanent, but the post doesn't say so |
| Nobody already owns the trade-off | Fail as framed | The post leaves every decision with the incumbents and every build with engineering, so the role owns nothing |
| Outside renewal, and a number the role controls | Fail | The first version had cycle time and decisions made without approval; the current one dropped them. No audit, regulator or customer is named |
| Practitioner level, with a signed agreement (new) | Half | The level fits the pattern. The agreement that would give it authority is missing |

**Verdict.** The level is right; the mandate is not. As written, the role is a discovery seat held up by
one sponsor, the Chief Knowledge Officer pattern. Give it a signed agreement and a number, and it becomes
the practitioner seat that lasting roles started from.

## 3. What it gets right

- **Field work first.** Following real deals and refunds is how protocol vision is trained.
- **Agents as instruments.** Reading where agents stall, loop or improvise as evidence of unwritten rules is
  cheap, new and specific to this moment.
- **Experiments with written hypotheses.** Loosening or hardening a rule on purpose, and writing up the
  result, improves a rule set without a redesign.
- **The upside reading.** "What becomes possible once a rule holds" is missing from most controls work.
- **Blameless reviews and an open map.** Both keep the information honest.
- **The level.** A practitioner seat is how lasting roles began.

## 4. What it gets wrong

1. **No signed agreement.** The post never says what the COO grants in advance: which rules the role may
   propose changes to, by what process, within what limits. Without it, every change needs the sponsor's
   attention, the pattern that faded. With it, a practitioner can act, as early SREs could stop launches
   under an error budget policy the business had approved.
2. **No number.** It should own time to amend, with wait and override as supporting measures (section 6).
3. **Unclear scope.** Each rule already has a functional owner: the controller's delegation-of-authority
   matrix, the deal desk's approval matrix, revenue operations' pricing and routing rules. The post doesn't
   say which rules are its business. The defensible answer: only rules whose owner and whose pain sit in
   different functions, such as a legal data rule slowing sales, or a finance limit stalling refunds.
4. **It sits close to agent management.** Reading agent traces and reviewing new agents with security are
   also what today's agent manager does. Section 5 separates the two.
5. **Scope sprawl.** Ethnography, trace reading, experiment design, interface prototyping, security reviews,
   incident reviews and writing resembles the 1998 webmaster's list, and that role split. Scope it to one
   value stream, such as quote-to-cash.
6. **Who approves experiments.** Loosening a discount limit for a month is a decision. The agreement should
   say who signs off and what happens when an experiment goes wrong.
7. **The title.** "Business protocol" means etiquette or B2B message formats to most searchers. Hire under
   a title people already search for, and keep "protocol" in the text (section 8).
8. **No outside renewal.** For US-listed companies the strongest is Sarbanes-Oxley: an agent that approves
   discounts or payments is an automated control, so changes to its rules fall under IT change-management
   controls (M). Customers' security reviews (SOC 2) add to it. The EU AI Act's high-risk list rarely
   covers revenue or service agents.
9. **Reporting line taken for granted.** The COO fits if cross-functional rule changes have no owner; where
   the controller or deal desk already owns limits and their delays, the CFO fits.

## 5. Protocol work is not agent management, but it may be the controller's

Today's "AI agent manager" sets agents' tasks, reviews their output, handles the exceptions they can't,
and improves the workflow (*Harvard Business Review*, Srinivasan and Wei; S). It has no standard title and
no senior track. In knowledge work it looks like prompt engineering: a skill likely to become part of every
manager's job. In high-volume customer operations it may persist as supervision, quality and workforce
planning, as contact-centre roles did. The closest precedent is the robotic process automation centre of
excellence of 2017–22, which shrank into automation teams rather than becoming a profession (M).

| | Agent management | Protocol work (cross-functional rule changes) |
| --- | --- | --- |
| Object | The agents | The rules every person and agent acts under, where owner and pain sit in different functions |
| Question | Is this agent doing its task well? | When a policy keeps getting overridden, how many days until it is fixed or confirmed, and by whom? |
| Would it exist without agents? | No | Yes: approval chains and limits existed before agents and will after |
| Kind of work | A supervision skill | A permanent trade-off: revenue against risk, speed against control |
| Who already does it | Each team's manager; agent platforms | Each rule has a functional owner (controller, deal desk, revenue operations); changes that cross functions are often unowned |
| Its numbers | Task success, exceptions handled, cost per task | Time to amend, wait and override, change-versus-keep ratio, reversals |
| Likely fate | Absorbed into managers' jobs and tooling in knowledge work; supervision roles in high-volume operations | Durable work; usually absorbed by the controller or deal desk, sometimes a distinct seat |

**The strongest case that the line collapses.** By 2027 many enforced rules will live in agent
configuration: the discount ceiling in a deal agent's instructions, the refund limit in its tool
permissions. Whoever edits the agent edits the rule. The rest is already owned: the controller reviews the
delegation-of-authority matrix, the deal desk handles discount exceptions, process-mining teams measure
waits from event logs. The real risk isn't being absorbed like agent management. It's being absorbed by
functions that already exist, which is what happened to the work before agents.

**What keeps it distinct.** Only rules whose change crosses functions. For rules inside one function, the
functional owner plus the agent owner is enough.

**The swap test for a job description.** If every agent were replaced by people tomorrow, would this job's
main number and deliverables stay the same, and would its decisions bind teams outside its own reporting
line? Yes to both: protocol work. If its numbers are counted per agent (task success, cost per task): agent
management.

## 6. The question, the metric and the activities

**The question.** Plainer, and measurable from records:

> **When a policy keeps getting overridden or worked around, how many days until someone fixes it or
> confirms it, and who is that?**

A COO asks the cost question first ("where is work waiting on sign-off?"); this is the second question,
and the one that tests ownership. Count open cases, not only fixed ones: sampling rules that were
eventually fixed hides the ones that never were.

**The metric: time to amend.**

- **Start:** when a rule crosses a threshold, not at the first exception (one approved exception is the
  exception process working). For example, more than N overrides in 30 days, a formal request to change
  the rule, or repeated agent escalations at the same rule. Date the case from the first override that
  counted.
- **Stop:** a recorded decision: the rule changed everywhere it lives, or kept, with a reason.
- **Report:** in year one, list the cases and how long open ones have waited; add the median and 90th
  percentile once there are more than about 30 closed cases. Split by whether the rule sits in one
  function or several.
- **Guard against gaming:** report the change-versus-keep ratio; if a rule is flagged again within 90 days,
  reopen the same case so its clock keeps running; watch overrides after each decision (if they continue
  after a "keep", the decision didn't hold); spot-check with field work.
- **Collecting it:** override and approval history mostly exists (pricing and ERP approvals, tickets, agent
  platforms' escalation logs). Decisions live in email and meetings, so the seat needs a register: a new
  process, not a new tool.
- **Pairs:** an amendment reversal rate (changes undone or causing an incident within 90 days), and wait
  and override on the ten most-used approvals and limits.

**The autonomy budget, narrowed.** As an analogue of SRE's error budget it is a stretch: error budgets work
because requests are counted automatically and continuously, while incidents traced to rules are rare,
late and disputed. A closer analogue is the delegated credit limit reviewed against losses. Minimal first
version: in one workflow where losses are counted automatically (refunds, credits, discounts), agents may
approve up to an agreed amount. If the monthly write-off or complaint rate stays under an agreed threshold
for two months, raise the limit by a quarter; after a breach, halve it. The CFO signs this once.

**The activities.** A loop, scoped to one value stream.

| Step | Activity |
| --- | --- |
| 0. Register | List the ten most-used approvals and limits in the value stream, each with an ID, where it lives and a named owner |
| 1. Find | Follow real cases; collect overrides, escalations, workarounds and repeated agent stalls; tag them to rules |
| 2. Cost | For each candidate change, estimate the wait time saved and the risk added |
| 3. Decide | Run the signed amendment rule with each rule's owner; record change or keep, with a reason |
| 4. Propagate | Update every place the rule lives: policy, pricing system, agent instructions and permissions, training |
| 5. Check | Track reversals, overrides and incidents after each change; contribute to blameless reviews |
| 6. Retire | Give rules review dates; delete the ones nobody needs |
| Report | Monthly to the COO; supply data for the COO's or CFO's yearly report to the audit committee |

Moved out: publishing approval, pricing and data-request interfaces (platform or engineering, with this
seat specifying them); leading incident reviews (incident or risk teams); reviewing each new agent before
launch (security and agent owners); day-to-day agent supervision (agent managers).

## 7. Near-term and mid-term roles

Judgments, informed by the lineage patterns: senior-first roles signal transitions; practitioner roles
make capabilities routine; skills tied to a technology are absorbed.

| Period | Role | Level | Likely fate |
| --- | --- | --- | --- |
| Near term, 2027 | AI agent manager, agent supervisor | Junior to mid | Absorbed into managers' jobs and tooling in knowledge work by 2028–29; persists as supervision and quality roles in high-volume operations |
| | Forward-deployed engineer | Junior to mid | Grows, then settles as a standard implementation role on the vendor side |
| | Chief AI Officer | Senior | Transition role; appointments peak, then many merge into data, digital or CIO roles |
| | AI council | Committee | Useful briefly; risks becoming a slow approval board |
| | AI governance manager; AI or model risk analyst | Mid | Grows in regulated firms, where second-line risk teams extend model validation to agents |
| | Deal desk analyst; process owner and process-mining team | Junior to mid | The closest incumbents; likely to take on agent rules in their value streams |
| | Protocol discovery (this post, under existing titles) | Junior to mid | The seed. Lasts if it gets a signed agreement, a number and cross-functional scope |
| Mid term, 2028–29 | Business rules analyst or engineer: a small practitioner team owning cross-functional rule changes, with time to amend | Mid | Our candidate for a distinct role, where cross-functional rule changes are frequent |
| | GRC engineer | Junior to mid | Durable; absorbs rules about money and reporting, and audit evidence |
| | Policy-as-code or authorization engineer; agent identity and access engineer | Mid | Durable in engineering and security; absorbs what agents may see, do and spend |
| | Head of the function | Senior | Once a team exists, around 2029–30, or earlier if an agent incident reaches the board |

Rough odds for 2029 in companies running agents at scale (judgment, not data):

- **About 35%:** the duties sit in existing structures (controller, deal desk, revenue operations,
  security) without an explicit metric.
- **About 25%:** the same structures, with time to amend or a similar metric attached.
- **About 15%:** a distinct practitioner seat or team, as below. Lower than v2, given how GDPR's
  data-protection duty mostly went to existing staff and how change advisory boards fared.
- **About 25%:** left inside engineering with no business owner, until an incident forces the question.

## 8. The role we'd propose instead

**A practitioner seat now, a small team later, a head last.**

**Now to 2027: a business rules analyst for one value stream.** "Business rules analyst" is an existing,
searchable title from the era of business-rules engines (M); "business controls engineer" collides with
industrial control engineering in job search, as "business protocol" collides with etiquette. Two to five
years in operations, revenue operations, internal controls, deal desk, business systems or reliability.
Scoped to one value stream, such as quote-to-cash. The current post, trimmed to section 6's loop, plus:

- **A signed agreement.** The COO or CFO signs an amendment rule: which cross-functional rules the analyst
  may propose changes to, who must agree, how experiments are approved, and who may stop the work.
- **A number.** A register and a baseline for time to amend, wait and override by day 60.
- **Renewal.** Data for the yearly audit-committee report; in US-listed companies, alignment with IT
  change-management controls for agents that approve money.

**2028–29: a small team**, if the first value stream shows long, recurring, cross-functional amendment
times. It runs the amendment rule across value streams and the narrowed autonomy budget where losses are
counted automatically.

**Later: a head of the function**, once a team exists, unless an incident creates the role from the top
first, as the Citicorp loss created the CISO.

**What this avoids.** It passes the swap test, so it shouldn't be absorbed with agent management. Its scope
is the cross-functional gap, so it doesn't compete head-on with the controller or deal desk. Its authority
comes from a signed rule, not a sponsor's attention. It owns a number. And its renewal comes from audit,
customers and incidents, not from AI adoption.

## 9. Suggested changes to the published post

Not made yet; for discussion.

- Keep the level (three to five years). Add the signed agreement and scope it to cross-functional rules in
  one value stream.
- Add the measures and the register.
- Add the swap test's spirit: the job's number is about rules, not agents. Cut or move the
  agent-management duties; keep reading traces, framed as finding rule signals.
- Name the renewal: audit and IT change controls, customers' security reviews, the EU AI Act where it
  applies.
- Consider "business rules analyst" or a revenue operations or controls title, with "protocols" in the text.

## 10. Assumptions to pressure-test

- [ ] **Agent management will be absorbed in knowledge work.** If agent fleets grow large enough to need
  dedicated operators, as call centres needed supervisors, it could last as its own role.
- [ ] **Cross-functional rule changes are frequent enough to fill a seat.** A mid-size company may make
  15–30 amendments a year in total. One value stream may not justify a full-time analyst.
- [ ] **The narrowed autonomy budget works** in at least one workflow with counted losses.
- [ ] **Sarbanes-Oxley IT controls will treat agent rules as automated controls.** Plausible, from memory;
  check with an auditor.
- [ ] **"Business rules analyst"** is still a recognised title; check current postings.
- [ ] **Seniority evidence** is partly from memory, and faded junior roles leave few traces.
- [ ] **The odds in section 7** are our judgment, not estimates from data.
