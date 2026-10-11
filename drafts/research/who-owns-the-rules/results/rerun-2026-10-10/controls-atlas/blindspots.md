# Blind spots in agent controls, October 2026

11 October 2026. This file combines three sources:
- the ranked gaps (`gaps.md`, `map-reverse.csv`): controls from other domains with no direct agent equivalent;
- object coverage across 46 products (`coverage.md`);
- growth in the timeline (`timeline-final.csv`, `timeline-analysis.md`).

For each blind spot I also searched the 2,046 inventory controls and the 303 timeline events for related work and for announcements.

Ranking rule, as in `gaps.md`:
1. whether the control is required in its home domain;
2. the consequence if an agent lacks it;
3. as a tie-break, no growth in the timeline and no announced work.

"Announced work" means a dated event in the timeline or a documented control in the inventory. It does not mean vendor intent stated elsewhere. Claims marked "inference" are not documented.

| Rank | Blind spot | Home-domain status | Closest agent controls | Timeline growth | Announced work |
|---|---|---|---|---|---|
| 1 | Kill function that stops all of a firm's agents and their pending actions | Law (RTS 6) | Sign-in disable (EG-173, EG-186), agent containment (AH-066), one-task cancel (AH-427) | Autonomy: no new vendor in 2026 | None |
| 2 | Firm-wide aggregate exposure limit across all agents | Law (RTS 6, 15c3-5) | API spend caps (CD-852, P-107), one mandate's budget (AH-524) | None in any quarter | None |
| 3 | Per-action value cap on tool calls that move value, outside payments | Law (RTS 6) | AP2 and ACP amount caps for payments only (AH-523, AH-532) | Payment protocols announced only (A-041, A-044) | None outside payments; policy engines could express one (inference) |
| 4 | Two-person approval of high-impact agent actions | Practice in trading and payments (design test) | Single-approver confirmations; multi-stage approval only for access requests (EG-181) | None | None |
| 5 | Independence of the guardrail from the agent, and the firm's exclusive control of its controls | Standard (IEC 61511), law (15c3-5) | Server-side gateways (BF-129, EG-021); managed settings documented as "not a security boundary" (CD-411) | Moving: server-side enforcement in 2026 (P-110 beta, P-115 GA) | Partial: Anthropic inference hooks (beta), server-side tool-call evaluation |
| 6 | Post-action checks and reversal | Law (RTS 6) | Audit logs (AH-192); "no undo" for external changes (CD-1042) | None | None |
| 7 | Segregation of duties across an agent's tools | Product feature (SAP, Oracle) | One fixed "lethal trifecta" detector (EG-062) | None | None |
| 8 | Controls on agent-to-agent delegation chains | Design test (no home rule) | A2A per-skill authorisation (AH-485), OAuth on-behalf-of (AH-188), MCP OAuth (A-022, A-033, A-060), Workday's ban on proxy delegation (AH-190) | Protocol-level auth only; A2A announced (A-026), proxies with analytics (G-099) | Protocol auth work; nothing on chain depth or scope |
| 9 | Throttle that disables an agent across runs until a person re-enables it | Law (RTS 6) | Per-run loop caps (AH-279, AH-435, BF-197); per-session spend pause (P-111) | None | None |
| 10 | Accuracy, data-reach and stored-data controls stalled | n/a (low coverage) | Groundedness and automated reasoning (P-030, P-066), content exclusions (A-078) | ACC 0 and STOR 0 events in 2026; DATA 3 vendors at most | None new since 2025 |

## 1. No vendor can stop all of a firm's agents at once, and none plans to in the record

RTS 6 requires a firm to "cancel immediately, as an emergency measure, any or all of its unexecuted orders".

What agents have:
- Entra can disable one risky agent, or block all agents from one blueprint (EG-173, EG-186). This stops sign-ins.
- ServiceNow lets a delegated role deactivate agents (AH-066).
- MCP and A2A cancel one task at a time (AH-427).

None of these cancels actions already queued or under way. A text search of the inventory for "cancel all", "stop all", "kill switch" and "emergency" finds only UiPath's switch for third-party model calls (AH-270).

Autonomy and handover is a mid-coverage object: 19 of 46 products. It gained no new vendor in the timeline in 2026.

No preview, beta or announcement in the timeline addresses this. Forecast 10 gives 0.75 that the gap remains in October 2027.

## 2. No control limits what all of a firm's agents can do in total

RTS 6 and 15c3-5 require pre-set firm-level risk and credit thresholds. `map-reverse.csv` codes this as "none", the only trading law with no partial agent equivalent.

What agents have instead:
- API spend caps at organisation and project level (P-107, CD-852). These meter vendor cost, not the value the agents move.
- Cloudflare's per-user baselines (G-105). These flag a session only when it also exceeds an organisation-level threshold, and they do not block.

Usage and spend limits is a well-covered object (33 products, 10 timeline vendors). The blind spot is what the limits count, not whether limits exist.

## 3. Value caps exist only for agent payments

AP2 amount ranges (AH-523) and ACP allowances (AH-532) cap one payment. In the timeline, both protocols appear only as announcements (A-041, A-044).

No stored page documents a cap on a refund, order or transfer made through an ordinary tool call. The nearest thing in the corpus is a prompt instruction in a UiPath example: escalate refunds "over $100" (`ui-prompts.txt`). That rule is written in natural language and depends on the model to follow it.

Two GA or beta policy engines evaluate each tool request: AWS AgentCore Policy (BF-027, P-085) and Databricks service policies (G-108). They could express a numeric cap. That is an inference; neither documents one. Forecast 11 puts a documented example at 0.50.

## 4. Approval is always one person

The inventory has 145 "Require a human" controls across 26 products. A text search for two-person, dual, four-eyes and multi-stage approval finds only Entra's multi-stage approval. That control applies to requests for agent access (EG-181), not to an agent's action.

Every action-level approval in the corpus is a single confirmation, usually by the user who started the run, for example CD-813, P-035 and P-048. A person approving their own agent's high-impact action is the arrangement two-person rules exist to prevent.

No vendor announcement in the timeline addresses this. The reverse map did not include a two-person row. This gap therefore rests on the inventory search, not on adjudicated mapping.

## 5. Guardrails often run where the agent runs, though 2026 brought server-side enforcement

`gaps.md` ranks guardrail independence (IEC 61511) tenth and the firm's exclusive control of its controls (15c3-5) seventh.

Client-side managed settings are documented as "a client-side control, not a security boundary" (CD-411). A local administrator can edit them (CD-682).

This is the one blind spot with announced movement:
- Anthropic's inference hooks (P-110, beta, August 2026) hold every governed prompt for an external server's verdict.
- Its server-side tool-call evaluation (P-115, GA, September 2026) runs outside the client.
- Gateway-enforced policies are GA at AWS (P-085) and beta at Databricks (G-107, G-108).

None of these documents the independence requirement itself, that the check shares no model, host or runtime with the agent. Server-side enforcement is necessary for independence but not sufficient, so this remains a blind spot. It ranks fifth because work is under way.

## 6. Nothing checks an agent's actions after the fact and stops it

RTS 6 post-trade controls must be able to shut an algorithm down. Agents have audit logs (Logs is the best-covered object, 39 products). They have runtime monitors that can stop a conversation (P-114, OpenAI asynchronous checks).

No vendor documents a check that reviews completed actions and then disables the agent. Gemini Code Assist says plainly that there is no undo for changes made outside the IDE (CD-1042). The only rollback controls roll back agent versions (AH-235, BF-142), not the agent's effects. No announcement.

## 7. Toxic combinations of tools are detected only in one fixed form

SAP and Oracle let firms define conflicting permissions and block or mitigate them. They also offer conflict simulation and "firefighter" emergency access. The reverse map codes five SoD rows as having no agent equivalent.

The only agent analogue is Lakera's detection of one fixed combination: reading confidential data, taking in untrusted content and communicating externally at once (EG-062). No vendor offers a rule such as "no agent may hold both create-vendor and approve-payment". No announcement.

## 8. Delegation between agents is authenticated, not bounded

The design asked us to test controls on agent-to-agent delegation. What exists is authentication and per-hop authorisation:
- A2A per-skill scopes (AH-485);
- OAuth on-behalf-of exchange (AH-188);
- MCP's OAuth framework and resource indicators (A-022, A-033, A-060);
- Salesforce's "fence" of declared subagents (AH-036);
- one platform that forbids agent proxy delegation outright (Workday, AH-190).

What is absent:
- limits on delegation depth;
- narrowing of scope as a task passes from agent to agent;
- a record that ties a downstream action to the original human principal across more than one hop.

Workday's audit log does record "By User / On Behalf Of" for one hop (AH-192).

The timeline's A2A entries are an announcement (A-026, not counted as availability), a gateway proxy with analytics (G-099) and an agent registry (G-090). The announced work is protocol-level authentication only.

## 9. Loop limits reset with every run

RTS 6 requires an algorithm to be "automatically disabled until re-enabled by a designated staff member" after repeated executions. Agent iteration and loop caps (AH-279, AH-435, BF-197) and Anthropic's session spend pause (P-111) end or pause one run. The next run starts clean. No vendor documents a cross-run counter that locks the agent until a person re-enables it. No announcement.

## 10. Accuracy, data-reach and stored-data controls have stopped spreading

These objects rank low on consequence in the comparison, but they are the coverage blind spots:
- **Answer accuracy and presentation** has the lowest product coverage (14 of 46, and none in groups C or G). It has had 3 timeline vendors since 2024 and no new event in 2026.
- **Stored data** had no new event in 2026.
- **Data and files the AI can reach** has never had more than 3 timeline vendors, though 23 inventory products document it.

The low timeline counts may partly reflect the collectors' focus on security and agent changelogs (inference). The most recent accuracy control of note is AWS Automated Reasoning checks (P-066, GA August 2025). No preview or beta in the record addresses these objects.

## Considered and not ranked

- **Stress and load testing** (RTS 6, gap 9). The consequence is medium. It is required, but load is not the main failure mode of agents.
- **Accountable executive certification** (15c3-5, gap 8). This is a governance duty. The main report covers it under named owners.
- **Emergency change and guarded rollout** (product features). They overlap with blind spots 1 and 6.
