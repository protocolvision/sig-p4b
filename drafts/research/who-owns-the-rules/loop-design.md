# Loop design: from changing activities to likely roles

Protocols for Business · version 1 · 10 October 2026 · pre-registered: committed before the first run

## 1. The problem this loop addresses

Our exploratory work started from roles (product manager, SRE, data scientist) and from our own idea of
protocol work, then asked whether a role would form around it. That order invites confirmation: we looked
for the role we had already described. This loop reverses the order. It starts from evidence of how
*activities* are changing as AI agents take on operational work, groups the activities that travel
together, infers which roles those groups support, and only then asks where activities like protocol
vision and protocol engineering fall: in one cluster, spread across several, inside existing roles, or
nowhere in particular.

## 2. Question

As AI agents take on operational work in companies, which activities are appearing, growing, moving or
disappearing; which of them bundle together under one accountability; what roles do the bundles support;
and where, if anywhere, do protocol vision and protocol engineering activities cluster?

## 3. Sources of reinforced bias, and the control for each

| Bias | How it would enter | Control |
| --- | --- | --- |
| Anchoring on our vocabulary | Agents search for and find "protocols" because we named them | Collectors and clusterers never see our terms. Banned in their prompts and outputs: protocol, protocol vision, protocol engineering, Business Protocol Management, BPM, hard/soft/free rules, hardness map, time to amend, Business Protocol Lead, amendment rule |
| Anchoring on our conclusions | Agents read our drafts | Agents are told not to open any repository file except their own output paths |
| Starting from roles | Evidence is gathered to fit roles already named | The unit of evidence is an activity, recorded with the titles observed doing it; collectors make no role predictions |
| Narrow search | Evidence comes only from AI governance sources | Five source strata; at most half of each collector's records may concern governance, control or compliance; quotas for shrinking and automated activities |
| Iterations reinforcing each other | Each round reads the last round's conclusions and refines them | Evidence accumulates across rounds; conclusions don't. Each round's clusterer is a fresh agent that sees only the pooled evidence, shuffled, never a previous clustering |
| Coding to fit the clusters | Whoever labels activities as protocol work also sees the clusters | Two coders label every record against the definitions in section 6, independently, without seeing any clustering. Agreement is measured |
| Order effects | Early sources shape all later clusterings | Strata enter in a random order, drawn before the run (seed 20261010): S4, S1, S5, S2, S3. Records are shuffled before each clustering |
| Our own synthesis | The orchestrator, who wrote the exploratory drafts, interprets the results | Interpretation rules are fixed in section 7 before the run. A red-team agent argues the null against the final results |

## 4. Evidence strata

| Stratum | Sources |
| --- | --- |
| S1 | Job postings and hiring data: posting analyses (Indeed Hiring Lab, LinkedIn Economic Graph, Lightcast, Revelio Labs), and postings for new and existing roles that mention agents or automation |
| S2 | Practitioner accounts: engineering and operations blogs, case studies, conference talks, postmortems and incident reports from companies deploying agents |
| S3 | Regulation, standards, audit and control guidance: activities these require of people in companies (EU AI Act, NIST AI RMF, ISO/IEC 42001, audit and internal control bodies, banking model risk guidance, sector regulators) |
| S4 | Research on work and tasks: labour economics, occupational task data, workforce surveys, usage studies, ethnographies of AI at work |
| S5 | Vendor and product documentation: what human tasks agent and enterprise platforms assume (administration, configuration, approvals, monitoring, permissions, identity) |

## 5. The loop

**Collection (once per stratum, five collectors, independent).** Each collector gathers 40 to 60 activity
records from its stratum and writes them to `results/loop-2026-10-10/ledger/<stratum>.jsonl`. Schema:

| Field | Content |
| --- | --- |
| `id` | `<stratum>-<nnn>` |
| `doc` | An ID shared by all records drawn from the same source document (one posting, one report), so co-occurrence can be counted |
| `activity` | Verb phrase, 15 words or fewer, in the source's own terms |
| `object` | What the activity acts on |
| `performed_by` | Titles or functions observed doing it, as the source states |
| `change` | `new`, `growing`, `moving` (from whom to whom), `shrinking`, `automated`, or `unclear` |
| `decision` | The decision or trade-off the activity serves, if the source shows one |
| `knowledge` | What the source says the person must know |
| `functions` | Functions the activity connects |
| `driver` | Why it is changing, per the source |
| `quote` | Up to 40 words seen verbatim, or empty |
| `source` | Chicago-style citation with URL |
| `date` | Date of the source |
| `grade` | P (primary, opened), R (reputable secondary, opened), S (search summary only), M (memory: not allowed) |

**Iteration k (k = 1 to 5).** Pool the ledgers of the first k strata in the drawn order, shuffle, strip the
stratum from the IDs (replace with random IDs, keeping a key), and give the pool to a fresh clusterer. The
clusterer groups activities by evidence of bundling (same document, same performer, same decision, same
knowledge, same functions), names each cluster neutrally, and infers the roles that would hold it, whether
they exist today and at what level. It writes `clusters/iter-k.json`.

**Coding (once, on the full pool, two coders, independent).** Each coder labels every record against the
definitions in section 6, without seeing clusters. Disagreements are reported, not resolved by either
coder.

**Analysis (orchestrator, scripted).** For each iteration: cluster stability against the previous iteration
(adjusted Rand index on shared records); where coded records fall across clusters; concentration measures.

**Red team (once).** A fresh agent receives the final clusters, the codes and the analysis, and argues
that protocol work does not cluster, or clusters only inside existing roles, using the ledger.

## 6. Definitions for coding (fixed before the run)

Each record gets one primary code, and optionally one secondary.

| Code | Activities |
| --- | --- |
| PV: protocol vision | Finding the rules, written or unwritten, that actually govern how work is done: observing workarounds, exceptions, overrides, escalations, or where automated agents stall, loop or improvise, in order to infer the rule; telling binding rules from leftovers; mapping rules across functions |
| PE: protocol engineering | Designing, encoding, changing or testing the rules that constrain what people and agents may do in systems: permissions, spending and approval limits, data-access rules, approval gates, interfaces between teams, partners or agents, policy as code, procedures for changing these rules, testing rules against circumvention |
| RD: rule decisions | Deciding whether a rule should change by weighing a trade-off across functions (revenue against risk, speed against control), and owning that decision or its measure |
| AO: agent operations | Building, configuring, prompting, supervising, evaluating or fixing AI agents and their outputs, where the activity is about the agent rather than the rules it acts under |
| OT: other | Anything else |

## 7. Interpretation rules (fixed before the run)

- **Codes used:** a record counts for a code if both coders gave it that primary code. Records where coders
  disagree are reported separately and rerun through the rules as a sensitivity check.
- **Clusters together:** at least 60% of a code's records fall in one cluster, in the final iteration and in
  at least three of the five iterations where the code has ten or more records.
- **Co-cluster:** PV and PE each have at least 40% of their records in the same cluster.
- **Dispersed:** no cluster holds more than 40% of a code's records in the final iteration.
- **Absorbed:** the cluster holding most of a code's records is one the clusterer attributes to an existing
  role or title.
- **Distinct candidate:** that cluster is attributed to a role that does not exist today under a stable title.
- **Stable:** adjusted Rand index of 0.6 or more between iterations 3–4 and 4–5.
- **Unstable results are reported as unstable,** whatever their content.
- **Coder agreement:** Cohen's kappa below 0.6 means the definitions are not reliable enough to support
  conclusions about clustering; the report says so.

## 8. Outputs

`results/loop-2026-10-10/`: `ledger/`, `pool/` (shuffled pools and ID keys), `clusters/`, `codes/`,
`analysis.md` (scripted tables), `red-team.md`, `report.md` (findings against section 7, then
interpretation, then limits).

## 9. Limits

- All agents share one underlying model; independence is of context, not of judgment.
- Most sources will be search summaries; grades show this.
- The banned-terms rule hides our vocabulary but not our framing of the question, which still points
  collectors at operational work around agents.
- Five iterations measure stability, not truth.
