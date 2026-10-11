# Controls atlas: final taxonomy (Phase 2, step 4)

11 October 2026. Reconciler (Opus). Inputs: `sort-S`, `sort-H`, `sort-agreement.md`, `embed-clusters.md`, `sort-sample.jsonl` (662 controls, 46 products, 8 groups). The hold-out file was not read. Assignments are in `taxonomy-sample.csv`.

Three axes. Each control gets one object, one mechanism and one enforcement point. Counts below are controls in the 662-row sample, followed by the number of products and groups that document at least one.

## The two sorts agreed on twelve objects; the reconciliation mainly sharpened boundaries and rebuilt the mechanism axis

On objects, the two sorts already agreed on 516 of 662 controls (78%), and 12 of their categories paired off one to one. The final object axis keeps those 12, merges S's "Autonomy and human oversight" with H's "Conversations, tasks and handover", and keeps S's small "Output quality" category, which H had folded into harmful content. That gives 14 objects.

On mechanisms, the two sorts disagreed on 190 controls. Most of these came from two catch-alls: H's "Permit or set state" (264 controls) and S's "Transform, redact or steer" (117). Both have been split up. "Permit or set state" now divides into Allow-list or grant (151), Transform or steer (78), Block or switch off (23) and a few others.

Agreement of the final taxonomy with each input (adjusted Rand index):
- objects: 0.78 with S and 0.73 with H; the two sorts scored 0.59 with each other;
- mechanisms: 0.73 with S and 0.52 with H; the two sorts scored 0.45 with each other.

Against the 36 embedding clusters (459 non-noise controls), the final objects score NMI 0.60 (S 0.59, H 0.55) and ARI 0.39 (S 0.38, H 0.29). The final object axis is therefore at least as close to the data-driven structure as either sort.

## Object axis: what is controlled (14 categories)

Code the thing the rule acts on, not the place where it acts and not what it does. When two objects seem to fit, apply the "not this" rule of the more specific category first.

**1. Harmful and off-limits content** (83; 25 products, 6 groups)
- Definition: what a prompt or response says or is about, judged against safety, topic, brand or acceptable-use policy.
- Include: toxicity and hazard categories, denied topics, word and substring blocklists, competitor mentions, bias, sentiment, banned languages or code, use-case prohibitions (such as clinical use), and generic guardrail settings (thresholds, fail-open or fail-closed, guardrail provider choice).
- Not this: attempts to subvert the model are Prompt attacks (2). Personal or confidential data is Sensitive data (3). Correctness, format and disclosure are Answer accuracy (4).
- Examples: BF-007 Denied topics; BF-001 Content filters by category and strength; EG-141 Hazard category S1: Violent Crimes.

**2. Prompt attacks and untrusted input** (29; 14 products, 6 groups)
- Definition: input that tries to override instructions or exploit the system, and the handling of untrusted text before it reaches the model.
- Include: jailbreak and injection detection, screening of tool results and retrieved text as untrusted, hidden-text removal, template escaping, input validation on protocol messages, malicious URLs, code or SQL injection payloads in output, and trust rules for tool metadata.
- Not this: content that is offensive but not adversarial is Harmful content (1). Numeric size caps are Usage limits (11).
- Examples: BF-082 Prompt injection and jailbreak detection; EG-038 Prompt attack screening of tool responses; BF-153 Template input escaping against injection.

**3. Sensitive data in prompts and outputs** (31; 18 products, 7 groups)
- Definition: personal, payment, secret or confidential data appearing in live AI traffic, including prompts, responses, tool arguments, retrieved content and outbound messages.
- Include: PII, PCI and secrets detectors, DLP rules, masking and de-identification, system-prompt leakage, and any rule triggered by the presence of sensitive data, whatever it then blocks.
- Not this: settings that decide what goes into logs are Logs (12). Data at rest, retention and training use are Stored data (13). Which files or sources the AI can open is Data access (7). Credentials as identities are Identity (8).
- Examples: BF-010 Sensitive information (PII) filter: block or mask; EG-194 DLP: block processing of sensitive prompts; BF-226 Interception of tool requests containing secrets.

**4. Answer accuracy and presentation** (12; 7 products, 4 groups)
- Definition: whether a response is correct, grounded, well-formed and properly presented, as distinct from whether it is harmful.
- Include: groundedness and fact-checking, relevance, schema and format validation, gibberish, URL reachability, low-confidence clarification, AI disclosure and persona branding.
- Not this: harmful or off-policy meaning is Harmful content (1). Length caps are Usage limits (11).
- Examples: BF-056 Groundedness detection; BF-173 JSON Schema check on output; AH-024 AI disclosure.

**5. Agent tools and actions** (101; 32 products, 8 groups)
- Definition: what an agent may do in the world. That covers tools, MCP servers, apps, API calls, commands, file edits, purchases and payments, pull requests, and the execution sandbox those actions run in.
- Include: tool and server allow-lists and deny-lists, per-tool or per-action approval, action policy engines, mandates and buyer approvals for a specific transaction, idempotency, and compute isolation for tool execution.
- Not this: the agent's overall operating mode, escalation or takeover is Autonomy (6). Who the caller is, and admin rights, is Identity (8). Numeric caps on tool calls (timeouts, output tokens, iterations) are Usage limits (11). Network destination lists enforced at egress are Network (9).
- Examples: BF-068 MCP tool allow-list (allowed_tools); BF-069 MCP tool approval (require_approval); EG-269 Agent Governor action: Block.

**6. Autonomy and human handover** (28; 17 products, 7 groups)
- Definition: the agent's run or conversation as a whole. That covers how autonomously it operates, when a person reviews it or takes over, and the state of the task or dialogue.
- Include: run and permission modes (supervised, auto-review, accept-edits, workspace trust prompts), escalation to a human, live takeover, plan review, scheduled autonomous runs, task cancellation and terminal states, dialogue scripts and rails, and instruction files that steer the whole agent.
- Not this: approval of one named tool, action, command or transaction is Tools and actions (5), with mechanism Require a human.
- Examples: AH-020 Escalation flows (frustration or complexity); AH-330 Human takeover of AI agent conversation; CD-869 Org Run Mode policy Auto-review.

**7. Data and files the AI can reach** (24; 19 products, 6 groups)
- Definition: which knowledge sources, documents, files, folders and data stores an agent or model can read or write.
- Include: knowledge-base scoping, content exclusions and ignore lists, filesystem read/write boundaries and protected paths, tenant data isolation, grounding-source steering, and sensitivity labels that stop AI processing.
- Not this: rules triggered by sensitive content in traffic are Sensitive data (3). Access decided by who the user is (roles, project membership) is Identity (8). Approval of a file edit is Tools and actions (5).
- Examples: AH-246 Knowledge base scoping; CD-914 Content exclusion: code review; CD-467 Default write boundary.

**8. Identity, credentials and access rights** (85; 34 products, 7 groups)
- Definition: who or what the caller is, how it proves that, and what it is entitled to use or manage.
- Include: SSO and federation, RBAC roles and permission sets, API keys and their restrictions, OAuth and token validation, agent identities, sponsors and owners in identity systems, conditional access, access requests and certifications, signed requests and mandates bound to keys, credential lifetimes, service control policies on use of the AI service, and admin rights over AI settings (who may change limits, logging or lifecycle status).
- Not this: permissions that name specific tools, apps or actions an agent may invoke are Tools and actions (5). Which data sources are attached is Data access (7).
- Examples: CD-079 Require SSO; EG-164 Conditional Access for agent user accounts; CD-161 API key permission levels.

**9. Network destinations** (22; 16 products, 7 groups)
- Definition: where traffic may go or come from: hosts, domains, IP ranges, private endpoints and transport security.
- Include: egress allow-lists and firewalls, sandbox network modes, private networking, IP allow-lists, TLS mandates, SSRF and DNS-rebinding protection, and switching off web access.
- Not this: where inference runs (region, residency) is Model choice (10). URL lists attached to one tool (for example WebFetch or computer use) are Tools and actions (5). IP restrictions attached to an API key are Identity (8).
- Examples: BF-067 Hosted agent network egress controls; AH-468 SSRF mitigations for server-side clients; BF-071 Private networking with no public egress.

**10. Model choice, routing and caching** (34; 17 products, 7 groups)
- Definition: which model or provider serves a call, where it runs, and how the call is routed, retried, cached or parameterised.
- Include: model allow-lists, kill switches for third-party models, routing, load balancing, fallback and retry, inference region and geography, generation parameters (except numeric caps), and response caching including cache lifetimes.
- Not this: token and output-length caps are Usage limits (11). Whether the provider retains or trains on data is Stored data (13).
- Examples: CD-162 Project model usage allow-list; BF-132 Model or provider fallbacks; AH-270 Enable calls to third-party AI models (global kill switch).

**11. Usage, spend and rate limits** (58; 32 products, 7 groups)
- Definition: how much is used or spent: requests, tokens, money, compute, time, iterations, size and count.
- Include: rate limits, token caps, budgets and spend caps (including hard stops at the cap), quotas, timeouts, concurrency, loop and iteration limits, output and context size caps, per-transaction value caps and cumulative budgets on agent payments, and email frequency limits.
- Not this: how long data or credentials last is Stored data (13), Logs (12) or Identity (8). Cache lifetimes are Model choice (10).
- Examples: CD-030 Input and output tokens per minute limits; CD-852 Spend limits; AH-523 Constraint: amount range.

**12. Logs, traces and audit records** (60; 36 products, 8 groups)
- Definition: the record of activity kept for the customer's oversight, and what that record contains.
- Include: invocation and audit logs, traces, telemetry and metrics, SIEM export, receipts and evidence chains, attribution headers and signed commits, log content settings and log redaction, log retention, activity reports, and operational alerts on runtime events.
- Not this: the AI system as a managed asset (discovery, inventory, risk rating, evaluation) is Lifecycle (14). Customer content held by the vendor (retention, training, abuse-monitoring storage) is Stored data (13). Identity risk detections are Identity (8).
- Examples: BF-025 Model invocation logging; CD-850 Audit logs and SIEM; AH-192 Audit log of agent actions (By User / On Behalf Of).

**13. Stored data: retention, training use and encryption** (34; 17 products, 6 groups)
- Definition: customer content held at rest by the AI system or its vendor, including how long it is kept, whether it may be used for training, how it is encrypted, and who may export it.
- Include: retention windows and deletion, zero data retention, training opt-outs and defaults, telemetry and content-sharing opt-outs, exclusion from abuse-monitoring storage, customer-managed keys, memory persistence and transcript storage.
- Not this: audit and operational logs are Logs (12). Data the agent can read is Data access (7).
- Examples: CD-049 Standard API 30-day deletion; CD-136 No training on workspace content by default; AH-106 Customer-managed encryption keys (CMEK).

**14. AI inventory, lifecycle and policy management** (61; 24 products, 7 groups)
- Definition: the AI system or agent as a managed asset, and the management of the control policies themselves.
- Include: registration and inventory, shadow-AI discovery, risk rating and impact assessment, testing and evaluation before release, publish and promotion gates, versions, aliases and rollback, release channels, enabling or disabling an agent or AI feature for the organisation, offboarding and containment, policy packs, and settings hierarchy and precedence.
- Not this: who may use an agent is Identity (8). The records an agent's activity produces are Logs (12). Evaluations of single answers at runtime are Answer accuracy (4).
- Examples: EG-215 Agent discovery (ISPM); AH-234 Approval gates for promotions (CI/CD); BF-023 Agent alias required to deploy.

## Mechanism axis: how the rule works (7 categories)

The mechanisms form an outcome ladder: what happens to the governed item when the rule applies.

**A. Allow-list or grant** (160; 41 products, 8 groups). The item proceeds only if named, granted or within a boundary.
- Default-closed rules: allow-lists, roles, scopes, permission sets, ACLs, registries of approved items, isolation boundaries, and required conditions such as SSO, TLS, signatures or a version match.
- Not this: a list of what is refused is Block. A setting that chooses among permitted options is Transform or steer.
- Examples: BF-068 MCP tool allow-list; AH-028 Permission sets for agent access; BF-219 IP address allow-list.

**B. Block or switch off** (113; 37 products, 8 groups). The item does not proceed.
- Default-open rules that name what is refused (deny-lists, exclusions, protected paths), runtime refusals on a verdict, kill switches, off switches and opt-outs, fail-closed behaviour, and cancellation.
- Not this: a cap that stops use once a number is reached is Cap a quantity.
- Examples: BF-007 Denied topics; CD-510 disabledMcpjsonServers; AH-270 Enable calls to third-party AI models (global kill switch).

**C. Cap a quantity** (66; 33 products, 8 groups). The item proceeds up to a number.
- Rate, token, money, count, size, duration and expiry limits, including hard stops at the cap and retention periods for stored content.
- Not this: a threshold that only alerts is Detect and flag.
- Examples: CD-030 Input and output tokens per minute limits; CD-852 Spend limits; AH-421 Tool call timeouts.

**D. Require a human** (49; 25 products, 6 groups). The item waits for, or is handed to, a person.
- Approval, confirmation, review gates, multi-stage approval, escalation and takeover, and settings that decide when approval is needed.
- Not this: an automated check before a step is Detect and flag or Block. Authentication steps are Allow-list or grant.
- Examples: BF-069 MCP tool approval (require_approval); AH-020 Escalation flows; AH-234 Approval gates for promotions.

**E. Transform or steer** (122; 41 products, 8 groups). The item proceeds, but changed or directed.
- Transform (about 30): masking, redaction, sanitising, escaping, removal or rewriting of content.
- Steer (about 90): standing configuration that chooses among options without permitting, refusing or capping. Examples are routing, fallback and caching, parameters, region selection, instructions and guidance, encryption keys, version aliases, policy packs, and settings about other controls (precedence, defaults, floors, provider choice).
- Not this: use only when no other mechanism applies; if the setting names what is allowed, refused or capped, code that instead.
- Examples: BF-010 Sensitive information (PII) filter: block or mask; EG-015 PII masking; BF-132 Model or provider fallbacks.

**F. Detect and flag** (92; 32 products, 8 groups). The rule produces a verdict, score or alert and does not itself stop the item.
- Classifiers and hazard labels, detect-only modes, discovery and risk rating, evaluations and tests, drift and anomaly alerts, and soft spend thresholds.
- Not this: if the control documents a block or transform action of its own, code that action instead.
- Examples: BF-082 Prompt injection and jailbreak detection; EG-215 Agent discovery (ISPM); BF-003 Detect-only mode for content filters.

**G. Record and report** (60; 34 products, 8 groups). The rule produces a durable record or report.
- Logs, traces, receipts, audit trails, registries, governance artefacts, activity reports and exports, and log retention.
- Examples: BF-025 Model invocation logging; CD-850 Audit logs and SIEM; AH-529 Receipts (checkout and payment).

**Coding rules for mechanisms**
- Multi-action controls: when a control offers several actions, code Transform if masking or redaction is one of the options. Otherwise code Block if blocking is an option. Otherwise code Detect. An "escalate" option alone does not make it Require a human.
- Retention: retention of logs is Record and report. Retention or deletion of stored customer content is Cap a quantity.
- Documented gaps (non-coverage, blind spots, "not supported"): code the object left uncovered and the mechanism of the control whose limit is documented. Where no control is named, code Detect. In the sample these are BF-004, BF-012, BF-112, BF-113, BF-131, BF-175, BF-234, CD-917, CD-998, CD-1042 and AH-015. Exclude them when counting what products offer.

## Enforcement point (fixed list from the design)

- **input**: before the model, acting on the prompt or incoming message.
- **model_call**: inside the call, covering model choice, routing, parameters, caching and region.
- **output**: after the model, on the response before it is shown or used.
- **tool_action**: before or around a tool call, command or real-world action.
- **data_access**: when the agent or model reads or writes data, files or stores, or data is held at rest.
- **network_egress**: at the network boundary, on destinations, endpoints and transport.
- **identity_permission**: at authentication or authorisation of a user, agent, key or admin.
- **spend_rate**: at a usage meter, covering rates, quotas, budgets and timeouts.
- **human_approval**: at a step where a person approves, reviews or takes over.
- **logging_audit**: when activity is recorded, monitored or reported.
- **lifecycle**: when an AI system or policy is registered, tested, published, versioned, changed or retired.

## Object by mechanism (sample counts)

| Object | Allow | Block | Cap | Human | Transform/steer | Detect | Record |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Harmful content | 2 | 35 | 0 | 1 | 14 | 31 | 0 |
| Prompt attacks | 2 | 4 | 0 | 0 | 5 | 18 | 0 |
| Sensitive data | 0 | 8 | 0 | 0 | 17 | 6 | 0 |
| Answer accuracy | 0 | 1 | 0 | 0 | 4 | 7 | 0 |
| Tools and actions | 53 | 13 | 1 | 18 | 8 | 8 | 0 |
| Autonomy and handover | 2 | 4 | 0 | 15 | 7 | 0 | 0 |
| Data access | 9 | 10 | 0 | 0 | 4 | 1 | 0 |
| Identity | 56 | 10 | 3 | 5 | 9 | 2 | 0 |
| Network | 16 | 6 | 0 | 0 | 0 | 0 | 0 |
| Model choice | 9 | 2 | 2 | 0 | 21 | 0 | 0 |
| Usage limits | 0 | 1 | 50 | 0 | 5 | 2 | 0 |
| Logs | 0 | 0 | 0 | 0 | 4 | 2 | 54 |
| Stored data | 1 | 13 | 10 | 0 | 8 | 0 | 2 |
| Lifecycle | 10 | 6 | 0 | 10 | 16 | 15 | 4 |

## How reconciled

Object decisions:
1. **Twelve one-to-one pairs kept.** These are the S–H pairs that matched on 20 or more controls each. Where S and H agreed, the shared label was kept; 510 controls were kept unchanged on both sorts.
2. **Merged S "Autonomy and human oversight" with H "Conversations, tasks and handover"** into Autonomy and human handover. Both describe the run as a whole. The embedding clusters back this: cluster 30 groups escalation with agent instructions, and cluster 21 groups permission modes.
3. **Split the 17 controls S coded as Autonomy and H coded as Tools.** The rule: approving one named action or transaction belongs to Tools; modes, escalation, takeover, plan review and task state belong to Autonomy. As a result, AP2/ACP mandates, buyer review, 3-D Secure and agent pull-request approvals went to Tools. Run modes, workspace-trust prompts, escalate actions and supervised mode went to Autonomy. Embedding cluster 13 (approvals) and cluster 22 (command approval) sit apart from cluster 21 (modes).
4. **Kept S "Output quality" as Answer accuracy and presentation**, against H, which had merged it into harmful content. Groundedness, schema and disclosure are a different question from harm, and the comparison phase needs them separately. It is small (12 controls, 7 products), but no single product dominates it. Bias, banned substrings and competitor names moved back to Harmful content. Malicious URLs and injection payloads moved to Prompt attacks.
5. **Logs versus lifecycle (11 controls S coded as Logs and H as Lifecycle).** Discovery, inventory, risk rating, evaluation and governance artefacts went to Lifecycle. Records of activity stayed in Logs. Embedding clusters 31 and 32 (discovery, evaluation, AI Control Tower) are separate from cluster 6 (audit logs).
6. **Identity versus tools versus data.** The test is whether the rule names the principal or names the action or source. Permissions naming tools, skills or apps went to Tools (AH-485, AH-041, AH-185, CD-1000). Authentication, keys, sponsors, SCPs on use of the AI service and admin rights over settings went to Identity (CD-995/996/998, AH-406, CD-1026, EG-235). Entra and Okta sponsor and owner controls went to Identity rather than Lifecycle, following S and embedding cluster 34.
7. **Numeric caps go to Usage limits, wherever they are attached.** This covers tool timeouts, MCP output-token caps, loop limits, max_tokens, input and output length scanners, and blocklist size. The exceptions are lifetimes: credential expiry goes to Identity, cache TTL to Model choice, and retention to Stored data or Logs. Per-transaction value caps and budgets on agent payments (AP2) stay in Usage limits, where both sorts put them. They are the closest analogue to trading's maximum order value.
8. **Region and residency of inference go to Model choice, not Network** (BF-020, CD-182, AH-274).
9. **Log content settings go to Logs, not Sensitive data** (BF-215, BF-216). Vendor-side abuse-monitoring storage and telemetry opt-outs go to Stored data (CD-172, CD-1014).
10. **The final object differs from both sorts on 14 controls.** These follow from rules 4, 6 and 7, plus the mode rule in decision 3: AH-542, CD-534, CD-323, CD-816, CD-1036, CD-1026, AH-403, EG-170, EG-018, CD-751, EG-129, EG-119, EG-137 and EG-235.

Mechanism decisions:
1. **Split H's "Permit or set state" (264).** A standing allow-list or grant became Allow-list or grant (151). Configuration that chooses among options became Transform or steer (78). Off switches, opt-outs and exclusions became Block or switch off (23).
2. **Split S's "Transform, redact or steer" (117).** Most stays in Transform or steer (99). Opt-outs and off switches moved to Block (9), cache lifetimes and zero data retention to Cap (5), and preconditions to Allow (2).
3. **Separated allow-list from block by default direction.** Default-closed rules (only what is named passes, including isolation) are Allow-list or grant. Default-open deny-lists and exclusions are Block. This is the most useful distinction for the comparison with cloud IAM and with trading, so it was not merged.
4. **Merged transform/redact with configure/steer to stay within 7 mechanisms.** Eight candidates were on the table: allow, block, cap, human, transform, steer, detect and record. Both transform and steer let the item proceed in altered or directed form, so they sit at the same rung of the outcome ladder. The memo reports the split (about 30 transform, about 90 steer).
   - Rejected: merging detect with record. Real-time detection and after-the-fact records map to different analogues (real-time monitoring versus record-keeping in RTS 6).
   - Rejected: merging block with allow, which would lose decision 3.
5. **Retention.** Log retention is Record; content retention is Cap. This resolves 13 controls S coded as Record and H as Limit.
6. **Multi-action guardrails and gap rows** follow the coding rules above. As a result, guardrails with their own block action moved from Detect to Block (for example AH-051, AH-256, EG-006, EG-027). "Block or mask" filters went to Transform (for example BF-111, EG-047). Documented gaps take the mechanism of the control they qualify.
