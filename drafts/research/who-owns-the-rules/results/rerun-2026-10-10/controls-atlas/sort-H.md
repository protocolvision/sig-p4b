# Card sort H: taxonomy of 662 controls

Independent bottom-up sort of `sort-sample.jsonl` (662 controls, 46 products, groups A to H). Two axes: **object** (what is controlled, 13 categories) and **mechanism** (how, 7 categories). Every control has one object and one mechanism. Assignments are in `sort-H.csv`. Counts are of controls. Products and groups are the number documenting at least one control in the category.

Coding rules used throughout:
- Code the thing the control acts on for **object**, and the effect for **mechanism**.
- An explicit block or deny at runtime is M1. A detector that only scores, flags or alerts is M6, even if its output is later used to block.
- A standing grant, allow-list, feature switch, routing choice or lifecycle state is M2. An action on one request is not M2.
- Rows that document a non-coverage gap ("not covered", "blind spot", "not supported") were coded by the control they would have been (usually M6). There are about ten of these; the reconciler should check them.

## Object axis (13 categories)

**O1. Harmful or off-topic content** (89 controls; 25 products, 6 groups)
- Definition: The meaning of prompts or responses judged against safety categories, topics, toxicity, named subjects or groundedness.
- Inclusion: The control classifies what the text says or is about. Excludes injected instructions (O2) and personal identifiers (O3).
- Examples: BF-021, BF-007, BF-001.

**O2. Prompt attacks and injected instructions** (20; 11 products, 4 groups)
- Definition: Attempts to override instructions, including jailbreaks, prompt injection, injected text in tool results, and escaping of user-supplied template input.
- Inclusion: The control targets adversarial instruction content or how untrusted text is inserted into a prompt.
- Examples: BF-006, BF-065, BF-052.

**O3. Personal and sensitive data in content** (31; 19 products, 7 groups)
- Definition: Personal identifiers, payment, secret and other confidential data appearing in prompts, responses, tool arguments, logs or outbound messages.
- Inclusion: The control detects, masks, redacts or blocks such data (includes DLP rules and PII filters).
- Examples: AH-539, AH-517, BF-011.

**O4. Model choice, routing and parameters** (34; 17 products, 8 groups)
- Definition: Which model or provider serves a request, where inference runs, how requests are routed, retried or fallen back, generation parameters (length, temperature), and model-side response caching.
- Inclusion: The control sets the model call itself, not what the call is used for.
- Examples: CD-075, CD-074, BF-233.

**O5. Agent actions and tool calls** (124; 37 products, 8 groups)
- Definition: What an agent may do: tool, MCP and API calls, commands, orders and payments, computer use, scheduled runs, and the approval or hooks that gate them.
- Inclusion: The thing constrained is an action or tool invocation.
- Examples: AH-485, AH-489, AH-486.

**O6. Data sources and files an agent can reach** (27; 20 products, 8 groups)
- Definition: Knowledge bases, documents, files, folders, retrieval sources and read/write boundaries an agent or model can access.
- Inclusion: The control scopes which data or files are available, rather than what is done with them (O7) or the network path (O8).
- Examples: BF-034, CD-1007, CD-467.

**O7. Stored data: retention, training and encryption** (33; 18 products, 7 groups)
- Definition: How long data is kept, whether it may be used for model training, and how stored data is encrypted or keyed.
- Inclusion: The control applies to data at rest or its afterlife (retention, deletion, training opt-in or opt-out).
- Examples: AH-502, BF-039, BF-035.

**O8. Network destinations and endpoints** (33; 23 products, 8 groups)
- Definition: Outbound hosts, domains, IP ranges, private networking, regional endpoints, webhooks and sandbox network rules.
- Inclusion: The control governs where traffic can go or from where it can arrive.
- Examples: AH-493, AH-481, BF-040.

**O9. Identities, keys and access rights** (71; 32 products, 7 groups)
- Definition: Who or what may use, manage or call an agent, gateway or key: SSO, RBAC roles, API keys, OAuth and token validation, agent identities and sponsors, conditional access, and denial policies on users.
- Inclusion: The control concerns the principal or credential, not the action it performs.
- Examples: AH-509, AH-492, AH-537.

**O10. Agents and AI systems: inventory, versions and status** (70; 25 products, 7 groups)
- Definition: The agent or AI system as a managed asset: registration, discovery, risk rating, versions and aliases, publish and retire states, owners, policy packs and governance registries.
- Inclusion: The control acts on the asset's lifecycle or governance record.
- Examples: AH-491, AH-538, AH-531.

**O11. Usage volume, spend and compute limits** (45; 27 products, 6 groups)
- Definition: Rate limits, quotas, spend and budget caps, token limits, concurrency, run durations and per-tool resource limits.
- Inclusion: The control caps how much is used, not what is used.
- Examples: AH-496, AH-533, AH-532.

**O12. Logs, traces and audit records** (60; 38 products, 8 groups)
- Definition: What is logged, traced or kept as evidence, including log redaction, log retention, telemetry and receipts.
- Inclusion: The control concerns the record of activity rather than the activity itself.
- Examples: AH-498, AH-530, AH-529.

**O13. Conversations, tasks and handover** (25; 13 products, 5 groups)
- Definition: The flow of a conversation or task: message validation, task states, cancellation, escalation to a person, takeover, dialogue scripts and hooks that run at task completion.
- Inclusion: The control shapes the sequence or handover of an interaction.
- Examples: AH-504, AH-497, AH-505.

## Mechanism axis (7 categories)

**M1. Block or stop** (92 controls; 35 products, 8 groups)
- Definition: Refuses or halts a specific request, output, action, message or session at runtime, or disables a resource in response to a rule.
- Inclusion: The item does not proceed. Includes kill switches and fail-closed behaviour.
- Examples: AH-504, AH-493, AH-497.

**M2. Permit or set state** (264; 45 products, 8 groups)
- Definition: Decides in advance what is allowed or which option applies: allow-lists, grants and scopes, feature enable or disable, identity requirements, routing choices, versions and lifecycle state, and data-use settings.
- Inclusion: A standing setting or grant, not an action on one request.
- Examples: AH-485, AH-491, AH-481.

**M3. Limit volume, amount or time** (73; 34 products, 8 groups)
- Definition: Caps counts, rates, amounts, lengths or durations, and sets expiry, timeouts and retention periods.
- Inclusion: A numeric or time bound on something that would otherwise be unbounded.
- Examples: AH-496, AH-502, AH-509.

**M4. Require human approval or review** (54; 27 products, 6 groups)
- Definition: Holds an action or change until a person confirms, approves, reviews, or takes over.
- Inclusion: A human is in the loop before the item proceeds, including sponsor and reviewer assignments.
- Examples: AH-489, AH-488, AH-541.

**M5. Transform or redact** (31; 18 products, 7 groups)
- Definition: Changes content rather than refusing it: masking, redaction, sanitising, minimising disclosure, placeholder substitution, or returning a stored copy in place of a fresh one.
- Inclusion: The output of the control is modified content.
- Examples: AH-539, AH-517, BF-011.

**M6. Detect, score or flag** (102; 36 products, 8 groups)
- Definition: Classifies, scores or alerts on content or behaviour, with or without blocking; includes detect-only modes, risk scores, discovery, drift detection and evaluation.
- Inclusion: The control produces a verdict, score or alert. An explicit block action is M1.
- Examples: AH-535, BF-044, BF-012.

**M7. Record or report** (46; 33 products, 8 groups)
- Definition: Writes logs, traces, receipts, audit trails, evidence or reports, and exports them.
- Inclusion: The control's effect is a durable record or a report.
- Examples: AH-498, AH-530, AH-529.

## Coverage

- Every object and mechanism category is documented by at least 11 products, so none is flagged as single-product.
- Lowest object coverage: O2 (11 products, 4 groups) and O13 (13 products, 5 groups).
- All 46 products and all 8 groups appear in the sort.

## Known weak points for the reconciler

1. **M2 is overloaded.** It holds 264 of 662 controls (40%). It merges two different things: access grants and allow-lists (identity and scope), and configuration or lifecycle settings (routing, versions, feature switches). Splitting it would give eight mechanisms, one over the 4 to 7 limit, so the reconciler would need to merge another pair (M5 into M1 is the least damaging).
2. **M1 and M6 boundary.** Many guardrail controls both score and block. The rule used is that an explicit block action is M1 and a score, flag or alert is M6. Some assignments may split differently by a second coder.
3. **Object O4 mixes model calls with caching.** Response caches are coded as O4 with M5, which is a judgement.
4. **O9 includes denial policies on users** (for example SCP and adaptive protection), which a coder could place under O5 or O10.
