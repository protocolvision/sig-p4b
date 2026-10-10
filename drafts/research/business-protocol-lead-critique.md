# The Business Protocol Lead, critiqued, and the role we expect for 2027–2029

Research draft · 10 October 2026 · Protocols for Business · for review before any post

> **Status.** Working notes. This critiques the job description published on the blyg as "A job
> description for a Business Protocol Lead" (`blyg-src/threads/job-protocol-operations-lead.md`), using
> the tests in [`role-emergence.md`](role-emergence.md). Sources are cited there; markers (S) and (M) mean
> the same thing. The projections in section 5 are judgments, labelled with rough probabilities.

## 1. What the post proposes

An exploratory role, three to five years' experience, reporting to the COO. Its job is to find the rules a
business actually runs on and rethink them as AI agents arrive. In its own words: follow real work end to
end; read agent traces as field notes; keep an open map of protocols; choose questions with the COO each
quarter; run experiments that loosen or harden a rule; prototype interfaces others can build on; review
new agents with security; run blameless incident reviews; write monthly field notes. "Security, finance
and legal decide what the rules say; engineering builds them; you bring back what's true on the ground."

## 2. Scored against the lineage tests

| Test (from `role-emergence.md`) | How the post scores | Why |
| --- | --- | --- |
| A capability makes new work cheap | Pass | Agents make enforced rules cheap to run and expose unwritten ones quickly |
| A cost lands between functions, and someone senior asks | Pass | Approvals, limits and data rules sit across sales, finance, security and legal; the COO asks |
| The trade-off is permanent, not a migration | Partial | The post frames the role around "AI adoption", which is a migration. Revenue against risk is permanent, but the post doesn't claim it |
| Nobody already owns the trade-off | Fail | The post leaves every decision with the incumbents and every build with engineering. The role owns nothing |
| Something outside keeps asking, and the role controls a number | Fail | The first version had cycle time and decisions made without approval; the current version dropped them. No audit, regulator or customer is named |

**Verdict.** As written, it matches the Chief Knowledge Officer and innovation-manager pattern from
section 5 of the research: a discovery role held up by one sponsor, with no number of its own. Roles like
that are the first cut in a budget review, or their work moves to consultants and forward-deployed
engineers. The post describes valuable work, but in the history we traced, a seat with this framing
rarely lasts.

## 3. What it gets right

Keep these. They are the role's method and its edge over an auditor or an engineer:

- **Field work first.** Following real deals and refunds is how protocol vision is trained. Nobody else
  in the company is paid to look before designing.
- **Agents as instruments.** Reading where agents stall, loop or improvise as evidence of unwritten rules
  is new, cheap and specific to this moment.
- **Experiments with written hypotheses.** Loosening or hardening a rule on purpose, and writing up the
  result, is how a rule set improves without a big redesign.
- **The upside reading.** "What becomes possible once a rule holds" is missing from most controls work,
  which only counts what it prevents.
- **Blameless reviews and an open map.** Both come straight from safety-critical practice and keep the
  information honest.

## 4. What it gets wrong

1. **It owns nothing.** Discovery without authority to change rules depends entirely on the COO's
   attention. Every lasting role in the research held something: a brand's profit, reliability, the
   board's risk.
2. **No number.** Without a measure the role controls, it can't show progress or defend its budget. The
   research suggests two: *time to amend* (how long a wrong rule takes to fix) and *wait and override*
   (how long work waits on each approval or limit, and how often each is overridden).
3. **Seniority mismatch.** Three to five years' experience, reporting to the COO, expected to get
   security, engineering and sales to agree and to run experiments on discount limits. The first CISO came
   with a board mandate; Google's first SRE lead was a senior engineer. Either raise the bar to eight or
   more years, or make the role an analyst seat under an owner who holds the rules.
4. **Scope sprawl.** Ethnography, trace reading, experiment design, interface prototyping, security
   reviews, incident reviews and writing. That resembles the 1998 webmaster's list, and that role split.
5. **Who approves the experiments?** Loosening a discount limit for a month is a decision, not research.
   The post doesn't say who signs off, or what happens when an experiment goes wrong.
6. **The title.** "Business protocol" means etiquette or B2B message formats to most searchers (see the
   group's search strategy), and candidates won't look for it. In every lineage the work came before the
   title. Hire under a title people already search for, and keep "protocol" in the description.
7. **No outside renewal.** The post doesn't mention audit, the EU AI Act's oversight duties (from
   December 2027 for high-risk uses), or customers' security reviews: the forces most likely to keep the
   question alive.
8. **Reporting line taken for granted.** The COO is right if no one owns how rules change together. Where
   the controller or deal desk already owns limits and their delays, the role belongs with the CFO. The
   research's ownership question (question 4 in its summary) should decide this, not the template.

## 5. Projection, 2027–2029

Judgments, not forecasts from data. The probabilities are rough and are there to be argued with.

| Period | What we expect | Signals to watch |
| --- | --- | --- |
| 2027 | Discovery work happens in projects, not seats: vendors' forward-deployed engineers, consultants and advisory, internal AI enablement leads. Chief AI Officer appointments peak. Many companies form AI councils, some of which become change advisory boards. | Job postings for "AI operations", "agent operations", "AI controls"; the rate of new CAIO appointments, not the stock |
| Late 2027–2028 | Outside renewal arrives. EU AI Act duties for stand-alone high-risk systems apply from 2 December 2027. Auditors and customers' security questionnaires start asking about agents (assumption). The question shifts from "deploy agents" to "who owns the rules agents act under". Agent permissions move into security and identity teams; rules about money move to controllers and GRC engineering. | Audit findings about agents; agent sections in security questionnaires; agent identity products |
| 2029 | In companies where rules change often and across functions (marketplaces, insurers, lenders, high-volume B2B sales), a named owner of how rules change appears, with a number to defend. It usually has an existing title: business controls engineering, operations engineering, revenue systems. | Titles that pair "controls" or "operations" with "engineering"; time-to-amend or approval-wait figures in board or audit reporting |

Rough odds for 2029 in companies running agents at scale:

- **About 60%:** the duties sit in an existing structure (controller and GRC engineering, revenue
  operations, security) with an explicit metric attached.
- **About 20%:** a distinct role with its own title and mandate, of the kind described in section 6.
- **About 20%:** it stays inside engineering, with no business owner, until an incident forces the
  question.

## 6. The role we'd propose instead

Two stages, so the role carries the post's strengths without its weaknesses.

**Stage A, now to late 2027: a protocol discovery engagement.** The current post, trimmed and made
explicitly temporary: six to twelve months, attached to the person who will own the rules (the COO or the
controller). It delivers the map, a baseline for time to amend and for wait and override on the ten
most-used approvals and limits, and a recommendation on where ownership should sit. It can be a contractor,
an internal analyst or an advisory engagement. Success is measured by whether Stage B is decided with
evidence.

**Stage B, 2028 onward: an owner of how rules change.** Working title *Head of Business Controls
Engineering* (or an existing title from the incumbency answer).

| Element | Proposal |
| --- | --- |
| Mandate | Owns how the company's enforced business rules change: approvals, limits, data permissions, agent scopes. Decides with the rule's functional owner; builds with engineering |
| The number | Time to amend, with wait and override on the most-used approvals and limits as supporting measures |
| Authority | Runs the published amendment rule: criteria for a change, who must agree, and who may stop the work. Can run time-limited experiments within limits agreed with finance and security |
| The autonomy budget | The agent equivalent of SRE's error budget. Each team's agents get a set amount of discretion (actions without approval). It grows while incidents traced to rules stay under an agreed rate, and shrinks when they don't. This turns revenue against risk into a number, as the error budget did for speed against stability |
| Duties | Keep the open map of rules; publish the amendment rule; run the autonomy budget; review rule-related incidents without blame; publish interfaces others can build on (approval, pricing, data requests); report time to amend to the COO and the audit committee |
| Reports to | The COO, unless the controller already owns most limits, in which case the CFO |
| Background | Eight or more years in internal controls, revenue operations, SRE or platform engineering; has turned policy into enforced systems and led incident reviews |
| First 90 days | Day 30: confirm the baseline from Stage A. Day 60: publish the amendment rule and the first autonomy budget for one team. Day 90: one rule amended under the new process, with time to amend measured |

What it avoids: it owns a number and a process, so it doesn't depend on one sponsor; it controls a
budget, not each approval, so it doesn't become a change advisory board; and its renewal comes from audit,
regulation and incidents, not from AI adoption.

## 7. Suggested changes to the published post

Not made yet; for discussion.

- Say plainly that the post describes Stage A, a temporary discovery role, and link to a Stage B
  description.
- Add the two measures (time to amend; wait and override) and a sentence on who approves experiments.
- Raise experience to five to eight years, or describe it as an analyst role under an owner.
- Mention audit, customers' security reviews and the EU AI Act as reasons the work will last.
- Keep the field-work, agent-trace and upside sections; they are the strongest part.

## 8. Assumptions to pressure-test

- [ ] **The autonomy budget works in practice.** It borrows SRE's error budget, which works because
  outages are counted automatically. Incidents "traced to rules" need a reliable way to count them.
- [ ] **Auditors and customers will ask about agents by 2028.** This is the main renewal assumption, and
  it is not yet evidenced.
- [ ] **EU scope.** The AI Act's deployer duties cover listed high-risk uses (such as hiring and credit),
  not all agents. Many companies will be outside it.
- [ ] **The odds in section 5** are our judgment, calibrated against the research's counter-cases, not
  estimated from data.
- [ ] **Stage A as a contract.** Treating discovery as temporary may lose the people best at it. Some
  companies may keep it as a standing research seat, as a few kept data science labs.
