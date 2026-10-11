# Timeline of agent and model controls, 2021–2026 (Phase 2b analysis)

11 October 2026. Opus adjudicator and analyst. Inputs: `timeline-all.csv` (303 events), `timeline-coded-S.csv` and `timeline-coded-H.csv`, `timeline-disagreements.csv`, `taxonomy.md`. Outputs: `timeline-final.csv` (all 303 events with final codes, both coders' codes and a note on each adjudication) and `timeline-quarterly.csv` (the series below, in two variants, for charting).

Abbreviations for the 14 objects: HARM harmful content, PI prompt attacks, SENS sensitive data, ACC answer accuracy, TOOL agent tools and actions, AUTO autonomy and handover, DATA data the AI can reach, ID identity and access, NET network destinations, MODEL model choice and routing, USE usage and spend limits, LOG logs and audit, STOR stored data, INV inventory, lifecycle and policy management.

## Adjudication: 111 events were in dispute, mostly on sophistication; most disputes were between levels 3 and 4

111 events differed between the two coders on at least one field (the brief said 110; the file has 111). Of these, 80 differed on sophistication, 44 on object and 3 on availability.

How the disputes were settled:

| Field | Disputed | Final = S | Final = H | Neither |
|---|---|---|---|---|
| Object | 44 | 20 | 23 | 1 |
| Sophistication | 80 | 46 | 25 | 9 |
| Availability | 3 | 1 | 2 | 0 |

The rules applied:
- **Level.** Code the highest level whose defining feature the event itself shows.
- **Level 4.** A rule keyed to an agent's tool calls, actions, delegation, session, runtime or identity is level 4. This covers MCP server allowlists, per-tool permissions, OAuth for MCP (delegation) and egress rules for agent runtimes.
- **Level 5.** Level 5 needs a central, declarative policy that is evaluated across agents or tools at runtime. Examples are Cedar policies at the AgentCore gateway and Databricks service policies before MCP calls.
  - Managed settings for a single agent product were held to level 4. These are Claude Code managed settings, the Codex requirements file and the Claude Code managed MCP allowlist (A-047, A-048, A-061, A-063 to A-065). This explains 6 of the 9 "neither" codes: S had coded them 5 and H 3.
  - The Copilot Studio Defender tool-call check (A-062) was held to 4. It is driven by detection, not by policy the customer declares.
- **Object.** The object follows the taxonomy's "not this" rules:
  - Domain lists on browsing and web tools go to TOOL (P-084, P-112).
  - Screening of MCP traffic by Model Armor goes to PI (P-083, P-091, P-092), consistent with the agreed P-052.
  - Sharing guardrails across an organisation goes to INV (P-081, G-060).
  - Run modes such as auto-review go to AUTO (A-066, A-071).
- **Availability.** Future-tense or "announcing" sources are not availability: P-003, P-039, G-026, A-007, plus the protocol announcements. A dated documentation article for a preview feature is availability (P-109).

The single object code that matches neither coder is P-092 (Model Armor with Agent Gateway): S coded HARM and H TOOL. I coded PI so that it matches the other Model Armor rows. Agreement before adjudication was object kappa 0.83, sophistication 0.66 (linear-weighted 0.69) and availability 0.89 (`timeline-agreement.md`).

The final file has 289 availability events and 14 non-availability events. The 14 are announcements, usage policies, protocol announcements and a principles-only MCP revision.

Stages after normalisation:
- 76 GA;
- 44 preview;
- 16 beta;
- 153 with no stage stated.

## Scope grew from 1 control type in 2021 to 146 by Q3 2026; growth peaked in Q2 2025 and new types have slowed since

The unit is a control type: one vendor × one object × one sophistication level, counted at its first availability event. I kept the pre-registered unit. A coarser unit gives the same shape:
- vendor × object: 106 pairs by Q3 2026;
- object × level, ignoring vendor: 40 of 70 possible cells.

Dates are first availability. Archive dates are upper bounds, so the all-evidence series can only move earlier, never later. The sensitivity column drops archive and press events: 16 and 5 among availability events (19 and 7 among all 303), leaving 268.

| Quarter | New events | New types | Cumulative types | Cumulative, primary only | Objects covered (of 14) | Vendors | Highest level, new | Median level, new | Share of new at 4–5 | Share at 4–5, primary only |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021Q1 | 0 | 0 | 0 | 0 | 0 | 0 | – | – | – | – |
| 2021Q2 | 0 | 0 | 0 | 0 | 0 | 0 | – | – | – | – |
| 2021Q3 | 1 | 1 | 1 | 0 | 1 | 1 | 3 | 3 | 0% | – |
| 2021Q4 | 0 | 0 | 1 | 0 | 1 | 1 | – | – | – | – |
| 2022Q1 | 0 | 0 | 1 | 0 | 1 | 1 | – | – | – | – |
| 2022Q2 | 0 | 0 | 1 | 0 | 1 | 1 | – | – | – | – |
| 2022Q3 | 3 | 3 | 4 | 1 | 3 | 3 | 2 | 1 | 0% | 0% |
| 2022Q4 | 2 | 2 | 6 | 2 | 3 | 4 | 3 | 2 | 0% | 0% |
| 2023Q1 | 2 | 2 | 8 | 3 | 4 | 5 | 2 | 1.5 | 0% | 0% |
| 2023Q2 | 7 | 5 | 13 | 7 | 6 | 7 | 3 | 2 | 0% | 0% |
| 2023Q3 | 4 | 4 | 17 | 11 | 7 | 9 | 3 | 2 | 0% | 0% |
| 2023Q4 | 11 | 8 | 25 | 19 | 10 | 13 | 3 | 2 | 0% | 0% |
| 2024Q1 | 20 | 15 | 40 | 32 | 12 | 17 | 3 | 2 | 0% | 0% |
| 2024Q2 | 23 | 15 | 55 | 43 | 13 | 20 | 4 | 2 | 4% | 6% |
| 2024Q3 | 24 | 12 | 67 | 55 | 13 | 22 | 4 | 2 | 4% | 4% |
| 2024Q4 | 15 | 5 | 72 | 60 | 14 | 23 | 4 | 3 | 13% | 8% |
| 2025Q1 | 19 | 12 | 84 | 72 | 14 | 24 | 4 | 2 | 16% | 16% |
| 2025Q2 | 27 | 17 | 101 | 88 | 14 | 25 | 4 | 4 | 52% | 48% |
| 2025Q3 | 27 | 13 | 114 | 101 | 14 | 26 | 4 | 4 | 59% | 60% |
| 2025Q4 | 38 | 13 | 127 | 115 | 14 | 26 | 5 | 4 | 71% | 71% |
| 2026Q1 | 13 | 5 | 132 | 120 | 14 | 26 | 5 | 4 | 69% | 69% |
| 2026Q2 | 28 | 7 | 139 | 127 | 14 | 26 | 5 | 4 | 61% | 61% |
| 2026Q3 | 23 | 7 | 146 | 134 | 14 | 26 | 5 | 4 | 52% | 52% |

Two more events fall in Q4 2026, after the series ends: Databricks G-107 (HARM 3, beta) and G-108 (TOOL 5, beta).

What the numbers say:
- **Scope.** Cumulative types roughly doubled each year to 2025: 6 at end 2022, 25 at end 2023, 72 at end 2024 and 127 at end 2025. Only 19 were added in the first three quarters of 2026 (5, 7 and 7 a quarter, against 12 to 17 a quarter in 2025).
  - New events did not slow in the same way: 64 in 2026 Q1–Q3. 2026 events mostly add controls to vendor × object × level cells a vendor already had. This is an inference.
  - Reading the 2026 slowdown as saturation of the cells our 26 vendors can fill, rather than a slowdown in vendor work, is also an inference. It would need a wider vendor set to test.
- **Breadth.** All 14 objects had at least one available control by Q4 2024. The median object went from 1 vendor at end 2023 to 3 at end 2024, 6.5 at end 2025 and 7 at Q3 2026.
- **Sophistication.** The highest new level rose one step about every year:
  - level 3 from 2021 (archive) or 2022 (primary);
  - level 4 from Q2 2024 (Bedrock guardrails on agents, P-027);
  - level 5 from Q4 2025 (GitHub Agent HQ preview, A-050; AWS AgentCore Policy preview, P-082).
  
  The median new event moved from 2 to 4 in Q2 2025 and has stayed at 4. The share of new events at levels 4–5 rose from under 5% in 2024 to 71% in Q4 2025. It has fallen each quarter since, to 52% in Q3 2026: new identity, spend and model-choice controls at levels 1–3 came back.
- **Level 5.** Seven availability events are at level 5, from five vendors: AWS, Anthropic, GitHub, Microsoft and Databricks (beta, Q4). Only two are GA: AWS AgentCore Policy (March 2026) and Anthropic's server-side tool-call evaluation (September 2026). The other four in the series are preview (A-050, A-058, P-082) or have no stated stage (P-102). P-082, P-085 and P-102 are all AWS AgentCore Policy, so the seven events cover five products.

The sensitivity version tells the same story. Excluding archive and press removes 12 types by Q3 2026 (146 to 134) and 5 vendors (26 to 21). It moves no turning point by more than a quarter. The only change of note is that the first level-3 event moves from 2021 (Credo AI, archive) to December 2022 (GitHub Copilot org policy, primary).

## Vendors per object: tools, identity and inventory grew fastest from 2024; content and injection controls stopped adding vendors after 2025

Vendors with at least one available control on each object (all evidence; last column primary only):

| Object | end 2022 | end 2023 | end 2024 | end 2025 | Q3 2026 | Q3 2026 primary only |
|---|---|---|---|---|---|---|
| HARM | 2 | 8 | 14 | 16 | 16 | 15 |
| PI | 0 | 2 | 6 | 8 | 8 | 7 |
| SENS | 0 | 2 | 5 | 8 | 8 | 8 |
| ACC | 0 | 1 | 3 | 3 | 3 | 3 |
| TOOL | 0 | 2 | 4 | 12 | 15 | 14 |
| AUTO | 0 | 0 | 1 | 5 | 5 | 5 |
| DATA | 0 | 1 | 2 | 2 | 3 | 2 |
| ID | 0 | 1 | 3 | 9 | 10 | 10 |
| NET | 0 | 0 | 1 | 4 | 4 | 4 |
| MODEL | 0 | 0 | 1 | 4 | 6 | 6 |
| USE | 2 | 3 | 8 | 9 | 10 | 8 |
| LOG | 0 | 0 | 3 | 4 | 5 | 4 |
| STOR | 0 | 1 | 2 | 3 | 3 | 2 |
| INV | 1 | 1 | 3 | 10 | 10 | 9 |

Availability events by object and year (counts of events, not types):

| Object | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 (to Oct 10) |
|---|---|---|---|---|---|---|
| HARM | 0 | 3 | 12 | 27 | 17 | 6 |
| PI | 0 | 0 | 2 | 8 | 8 | 2 |
| SENS | 0 | 0 | 2 | 5 | 5 | 1 |
| ACC | 0 | 0 | 2 | 4 | 1 | 0 |
| TOOL | 0 | 0 | 2 | 2 | 31 | 21 |
| AUTO | 0 | 0 | 0 | 1 | 5 | 4 |
| DATA | 0 | 0 | 1 | 2 | 0 | 2 |
| ID | 0 | 0 | 1 | 5 | 16 | 11 |
| NET | 0 | 0 | 0 | 1 | 5 | 1 |
| MODEL | 0 | 0 | 0 | 1 | 3 | 4 |
| USE | 0 | 2 | 1 | 17 | 6 | 8 |
| LOG | 0 | 0 | 0 | 4 | 1 | 2 |
| STOR | 0 | 0 | 1 | 1 | 2 | 0 |
| INV | 1 | 0 | 0 | 4 | 11 | 4 |

Sophistication by year (availability events):

| Year | Events | L1 | L2 | L3 | L4 | L5 | Median | Share 4–5 |
|---|---|---|---|---|---|---|---|---|
| 2021 | 1 | 0 | 0 | 1 | 0 | 0 | 3 | 0% |
| 2022 | 5 | 3 | 1 | 1 | 0 | 0 | 1 | 0% |
| 2023 | 24 | 4 | 15 | 5 | 0 | 0 | 2 | 0% |
| 2024 | 82 | 24 | 33 | 21 | 4 | 0 | 2 | 5% |
| 2025 | 111 | 11 | 25 | 15 | 57 | 3 | 4 | 54% |
| 2026 (to Oct 10) | 66 | 7 | 4 | 16 | 35 | 4 | 4 | 59% |

The shift is from content to action:
- 2023–24 was the classifier era: level 2, HARM and PI.
- 2025–26 is the agent era: level 4, TOOL and ID.

No vendor was added in 2026 for HARM, PI, SENS, ACC, AUTO, NET, STOR or INV. ACC and STOR had no new availability events at all in 2026, and DATA has had 3 vendors at most throughout.

## Limits that shape these numbers

- **Collection.** The events come from three collectors with fixed vendor lists:
  - P: providers and cloud platforms (117 events);
  - G: gateways and guardrails (108);
  - A: agent apps and protocols (78).
  
  Vendors outside the atlas sample are absent. Vendors with dense changelogs (Anthropic, Microsoft, LiteLLM) contribute more events. This is why the type count, not the event count, is the headline measure.
- **2021–2022 is thin.** Many 2020–22 controls predate the changelogs that could be fetched, for example the OpenAI API content filter and rate limits from the 2020 beta. The early series is therefore censored. Early growth rates overstate true growth.
- **153 events have no stated stage.** They are counted as availability when the source describes a usable feature. "GA" counts are therefore a floor.
- **First availability is not adoption.** Previews are counted as availability, as the design specifies, and announcements are not.
- **Sophistication levels are judgements.** Level 4 is broad. It covers both a static egress allowlist on an agent sandbox and per-tool approval rules. The 4–5 share therefore measures agent-scoping more than technical depth.
