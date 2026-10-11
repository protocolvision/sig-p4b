# Decision rights across rule systems: design (pre-registered)

11 October 2026. Added at the user's request; written before any data are pulled.

## Question

Is the missing owner of agent rule changes specific to agents, or do job ads never say who decides rule changes in any domain? We compare agent rules with eight rule systems that firms already run.

## Domains

| Code | Rule system | Lexical seed terms (duty statements must also contain a rule word) |
| --- | --- | --- |
| AGT | AI agents | agent, agentic, copilot, chatbot, virtual assistant, AI assistant |
| CRD | Credit and underwriting policy | credit policy, underwriting, credit risk, lending criteria |
| PRC | Pricing and discount approvals | pricing, discount, deal desk, price exception |
| FRD | Fraud rules | fraud, AML, transaction monitoring, sanctions screening |
| CHG | IT change management | change advisory board, CAB, change management, release approval |
| ACC | Access and identity policy | access policy, entitlement, identity governance, role-based access, privileged access |
| TRD | Trading limits | trading limit, risk limit, position limit, kill switch, pre-trade |
| CLN | Clinical protocols and formularies | clinical protocol, formulary, order set, clinical guideline, care pathway |
| PRO | Procurement approval thresholds | approval threshold, delegation of authority, procurement policy, spend approval |

The rule words are: rule, policy, policies, limit, threshold, criteria, guideline, protocol, guardrail, standard, control, approval, exception, parameter, configuration.

## Part 1: job-ad duties

**Source.** The 305,533 extracted duty statements, joined to postings. The 20% sample of other postings carries a weight of 5.

**Sample.** Statements match by script: a domain term plus a rule word.
- We draw a seeded random sample of up to 60 statements per domain (seed 20261012), 540 at most, after removing duplicates within each employer.
- We add 30 hidden seeded statements: 10 apply, 10 edit and 10 decide, spread across domains. Their key is stored apart from the pool.

**Code per statement (exactly one):**
- **apply:** follows, enforces, monitors or checks against the rules.
- **edit:** writes, configures, tunes, maintains or updates the rules or their settings.
- **decide:** approves, owns, sets policy on, chairs or signs off changes to the rules, including exceptions above a threshold.
- **none:** not about this domain's rules.

**Coding.**
- Two coders from different model families (Haiku and Sonnet) code blind.
- Seed recall must reach 0.7 for each code.
- Disagreements go to blind Opus adjudication.

**Measures.**
- **Decision share:** decide ÷ (apply + edit + decide) per domain, with a Wilson interval.
- **Edit share** per domain, computed the same way.
- The most common job titles holding decide duties in each domain.

## Part 2: written governance documents

For each domain, collect 3 to 6 public documents that set who decides rule changes:
- policies;
- committee charters;
- regulator rules or guidance;
- published frameworks.

Agent-specific sources include public AI or agent governance policies from firms and vendor or standards guidance.

Code each document:
- **names_decider:** yes or no. Does it name a person, role or body that approves changes to the rules?
- **binding:** law, regulator guidance, firm policy or voluntary framework.

Every claim needs a verbatim quote of 40 words or fewer, checked by script. No sign-ins.

## Reading rule (fixed now)

- **Agents are an exception** if both hold:
  - AGT's decision share is below half the median decision share of the eight comparison domains, and its Wilson upper bound is below that median;
  - in Part 2, at least five of the eight comparison domains have a document naming a decider, while AGT has none, or only voluntary ones.
- **Genre effect** if every domain's decision share is below 5% while Part 2 shows named deciders in most comparison domains. Job ads don't show decision rights; written policies do.
- **Mixed:** any other pattern, reported as such.

## Limits stated in advance

- Lexical matching undercounts domains whose duties avoid the seed terms.
- Domains differ in how many postings there are; small domains get wide intervals.
- Part 2 is a purposive sample, not a census.
