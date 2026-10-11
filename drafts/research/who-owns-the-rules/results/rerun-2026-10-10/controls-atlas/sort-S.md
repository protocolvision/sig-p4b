# Card sort S (Sonnet): taxonomy built bottom-up from 662 controls

Two axes. Every control has exactly one object and one mechanism. Counts are in sort-S.csv.

## Object axis (14)

| Object | n | Definition | Inclusion rule | Examples |
| --- | --- | --- | --- | --- |
| Harmful and policy content | 76 | Classifying or filtering the substance of prompts and responses against safety or topic policy. | Toxicity, hazard categories, denied topics, blocklists, moderation thresholds, guardrail enforcement modes. | BF-001, AH-209, EG-141 |
| Prompt attacks and untrusted input | 33 | Defending the model against adversarial or untrusted input. | Injection, jailbreak, hidden text, tool-result screening, input validation and templates. | BF-082, AH-255, AH-419 |
| Sensitive data in AI traffic | 33 | Detecting or removing PII, secrets and confidential data in what flows to and from models. | PII, DLP, secrets, masking and redaction of prompts, responses, tool arguments. | BF-010, EG-047, BF-226 |
| Output quality and format | 17 | Checking responses for correctness or form rather than harm. | Groundedness, schema, relevance, URL validity, length, disclosure. | BF-056, BF-173, EG-027 |
| Tool and action use | 96 | What an agent may do: tools, MCP servers, actions, execution sandboxes, side effects. | Tool and server allow/deny, per-tool approval, action filters, runtime action policy, execution isolation. | BF-068, CD-300, EG-269 |
| Autonomy and human oversight | 26 | When a human must confirm, take over, or when autonomy is granted. | Escalation to humans, takeover, supervised modes, delegated mandates, scheduled autonomy. | AH-020, AH-510, AH-378 |
| Data and knowledge access | 22 | What data, files and knowledge sources an agent or model can read. | Knowledge base scoping, file read/write boundaries, content exclusions, grounding sources. | AH-246, CD-831, AH-183 |
| Identity, authentication and permissions | 84 | Who or what the caller is and what it is entitled to. | SSO, roles, RBAC, tokens, keys, agent identities, conditional access, sponsorship, access reviews. | CD-079, EG-164, BF-187 |
| Network and external connectivity | 23 | Which networks, hosts and endpoints can be reached. | Egress allow-lists, firewalls, private endpoints, TLS, SSRF protection, IP allow-lists. | BF-067, AH-493, CD-771 |
| Model selection and call configuration | 34 | Which model serves a call and how: routing, fallback, caching, region, parameters. | Model allow-lists, routing, load balancing, fallbacks, cache, inference region, kill switch for third-party models. | BF-198, BF-143, AH-270 |
| Spend, rate and resource limits | 55 | Numeric ceilings on usage, cost, time and size. | Rate limits, token caps, budgets, quotas, timeouts, concurrency, size and iteration caps. | CD-030, BF-229, AH-300 |
| Logging, monitoring and audit | 73 | Keeping a record or watching behaviour after the fact. | Audit logs, traces, telemetry, alerts, discovery and inventory, risk detection, log content settings. | BF-025, CD-850, EG-281 |
| Retention, privacy and training use | 32 | What is stored, for how long, who may learn from it, where it lives. | Retention windows, deletion, zero data retention, training opt-outs, encryption keys. | CD-049, CD-136, AH-009 |
| Lifecycle and governance | 58 | Publishing, versioning, approval gates, risk assessment, retiring, testing and policy management. | Publish gates, promotion approvals, registries, risk intake, evaluations, policy packs, offboarding, state machines. | AH-234, AH-060, EG-230 |

## Mechanism axis (7)

| Mechanism | n | Definition | Inclusion rule | Examples |
| --- | --- | --- | --- | --- |
| Block or deny | 122 | Stops or disables something outright. | Deny, reject, disable, fail-closed, kill switch, cancel, hard stop. | BF-007, EG-023, AH-270 |
| Allow-list or scoped grant | 140 | Permits only what is named or granted. | Allow-lists, roles, scopes, ACLs, permission sets, registries of approved items, identity binding. | BF-068, AH-485, CD-300 |
| Limit or quota | 54 | Caps a quantity. | Rate, token, budget, time, count, size limits and expiry. | CD-030, BF-229, AH-324 |
| Require approval or human step | 50 | A person or authentication step must happen before proceeding. | Approval, confirmation, escalation, verification, review gates. | BF-069, AH-020, AH-234 |
| Transform, redact or steer | 117 | Changes content, configuration or behaviour rather than stopping it. | Masking, sanitising, routing, fallback, caching, settings, guidance, opt-outs. | BF-010, BF-143, EG-015 |
| Detect, score or alert | 113 | Classifies, scores or flags without itself enforcing. | Classifiers, detectors, monitors, alerts, evaluations, documented non-coverage. | EG-141, BF-082, EG-215 |
| Record or retain | 66 | Writes down or keeps what happened. | Logs, traces, audit trails, retention, receipts. | BF-025, AH-192, CD-049 |

## Judgement calls

- Guardrail rows covering both prompts and responses are filed under Harmful and policy content rather than split by direction.
- Approval of a single tool call sits in Tool and action use with mechanism Require approval; escalation to a human sits in Autonomy and human oversight.
- Documented gaps (for example BF-004, BF-012, BF-113) are filed under the object they fail to cover, with mechanism Detect.
- Vague or advisory rows (for example CD-884, CD-1017) took the nearest object with Transform, redact or steer.
- Mechanism "Transform, redact or steer" absorbs configuration settings that change behaviour without a deny or limit; it is the broadest category and the most likely to split on reconciliation.
