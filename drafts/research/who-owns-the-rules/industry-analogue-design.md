# Industry analogue: which industry shows software's near future, and how its rule work was organised

Protocols for Business · version 1 · 10 October 2026 · pre-registered: committed before any evidence for
this study is collected · stratum S8 of [`loop-design-v2.md`](loop-design-v2.md)

## 1. The problem

Our software evidence can't show what happens to rule work when the stakes rise: the agreements that give
someone authority over rules stay internal, and no forcing lever (law, liability, insurance) applies yet to
most business agents. As agents gain reach, software may become regulated, controlled and insured the way
some industries already are. Those industries made their rule work public: they had to name who decides,
how deviations are reported and how rules change. If one of them resembles where agent-run business is
heading, its history is a forecast of the org design to expect.

## 2. Questions

1. Which industry most resembles the near future of software run by agents?
2. In that industry (and the runner-up), how did the organisation of rule work evolve: who noticed
   deviations, who designed and changed rules, who decided across functions, at what seniority, and what
   forced each change?
3. What does that evolution predict for companies running agents, and on what timeline?

## 3. Choosing the industry (pre-registered)

**Candidates (fixed before scoring):** hospital clinical care; pharmaceutical manufacturing; commercial
aviation; nuclear power; electricity grid operation; algorithmic and electronic trading; retail banking
(credit, payments, anti-money-laundering); insurance underwriting and claims; automotive driver assistance
and automated driving; e-commerce and retail logistics (a control: heavy automation, light rule regulation).

**Dimensions, each scored 0–4 with cited evidence, weights fixed:**

| Dimension | Weight | 4 means |
| --- | --- | --- |
| D1 Software acts on its own at machine speed | 3 | Most consequential actions are taken by software without a person approving each one |
| D2 Actions have direct financial or legal effect on others | 2 | A single automated action can move money, bind a contract or harm a third party |
| D3 Rules are encoded in software that constrain automated actors | 3 | Limits, permissions and checks are enforced in the systems the automation runs through |
| D4 Rules apply to the software's behaviour, not only the firm | 2 | Regulators, accreditors or insurers set requirements for how the automated system behaves and changes |
| D5 One rule change affects several functions | 2 | Changing a limit or check routinely involves three or more functions |
| D6 No licensed profession already owns the decision | 1 | Decisions are not reserved to a licensed professional (reverse of a physician's or pilot's authority) |
| D7 Deviations are recorded as data | 1 | Overrides, exceptions and near misses are logged and reviewable |
| D8 Fifteen or more years of history with the automation | 2 | The automation has run long enough for organisational responses to be visible |

**Procedure.** Two evidence collectors split the candidates and write a cited fact sheet per industry, one
paragraph per dimension, without scores. Two scorers, working independently and without web access, score
every industry from the fact sheets. The orchestrator computes weighted totals (maximum 64) and agreement
between scorers. The industry with the highest mean total is the primary analogue and the second is the
runner-up, unless scorers disagree on the top industry by more than 6 points, in which case both are
studied as co-primary. The control (e-commerce and retail logistics) is always studied briefly.

## 4. Coding the org-design evolution (pre-registered)

For the primary analogue and the runner-up, a researcher builds a dated timeline of events that changed how
rule work is organised. Each event:

| Field | Content |
| --- | --- |
| `year` | Year of the event |
| `event_type` | technology, incident, regulation, standard, accreditation, insurance, role created, committee created, certification, enforcement |
| `event` | What happened, one sentence |
| `structure` | The organisational structure created or changed (role, committee, office, reporting system, procedure), or empty |
| `layer` | PV (noticing deviations), PE (designing and changing rules), RD (deciding rule changes across functions), or several |
| `form` | person (named individual), practitioner role (an occupation), committee, system (reporting or monitoring system), external body |
| `seniority` | At first creation: entry, mid, senior, executive, board, n/a |
| `lever` | What forced it: law, regulator guidance, accreditation, insurance, liability, incident, customer, none |
| `source`, `grade` | Chicago-style citation; P, R or S |

A separate researcher searches for counter-examples: cases in any industry where an individual practitioner,
not a committee or named executive, owns rule decisions across functions; and industries that automated
heavily without creating rule roles.

## 5. Hypotheses and what would refute them

| ID | Hypothesis | Refuted if |
| --- | --- | --- |
| H-lever | Rule work became distinct roles or bodies only after a forcing lever (law, accreditation tied to payment, personal liability, insurance) | In the primary analogue, two or more role or committee creations precede any lever by three or more years |
| H-layers | The three layers take different forms: noticing deviations becomes a reporting or monitoring system; designing rules becomes a practitioner role; deciding rule changes goes to a committee with a named accountable person | In the primary analogue, any layer's main form differs from this, or the counter-example search finds two or more cases of an individual practitioner owning cross-functional rule decisions |
| H-bridge | The lasting new occupation is a bridge role combining domain standing and system skill, tied to one domain | The new occupations in the analogue are general (not domain-tied) or pure technical roles |
| H-lag | From the automation's spread to a named role or body took ten years or more | The lag is under five years for most structures |
| H-control | The control industry automated without creating comparable rule roles | It shows the same structures as the primary analogue |

## 6. Translation to companies running agents

Map each structure in the analogue's current state to its counterpart for agent-run business, stating for
each: the counterpart (existing or missing), the lever that would create it, and an estimated year range.
Predictions are written as dated, checkable statements with probabilities and added to the prediction
register. The translation is labelled as interpretation, not finding.

## 7. Controls for bias

- Candidates, dimensions, weights and the decision rule are fixed here before any evidence is collected.
- Collectors write facts, not scores; scorers never search, and score independently.
- The control industry and a counter-example search are mandatory.
- Our vocabulary (protocol, protocol vision, BPM) is banned from collector and scorer prompts.
- A red-team agent reviews the choice of industry and the translation.

## 8. Outputs

`results/industry-2026-10-10/`: `factsheets/`, `scores-A.json`, `scores-B.json`, `scoring.md` (totals and
agreement), `timeline-<industry>.csv`, `counterexamples.md`, `translation.md`, `red-team.md`.

## 9. Limits

- Fact sheets rest on search summaries unless pages can be opened.
- All agents share one model and its knowledge of how these industries turned out.
- Similarity on eight dimensions doesn't guarantee the same path; the translation is a forecast, not a
  finding.
