# Review: Phase 4/4b mapping adjudication and coding spot-check

11 October 2026. Fresh Opus reviewer and adjudicator. Inputs:
- the coder outputs `map-forward-S/H`, `map-reverse-S/H` and `reach-S/H`;
- the source lists `comparison-sources.csv` and `conventional-sources.csv`;
- the agent atlas `inventory-all.csv` and `coded-all.csv`;
- the stored pages under `corpus/`.

Outputs: `map-forward.csv`, `map-reverse.csv`, `reach.csv` and `gaps.md`.

## The coding spot-check finds 35 of 40 rows right on all three axes, with every quote verbatim

Sample: 40 rows of `coded-all.csv`, drawn at random with seed 20261011. That gave 24 single-coder rows, 13 from the reconciled sample and 3 held-out rows. For each row I did two things:
- checked by script that the quote appears in the stored page at `source_path`, after normalising whitespace and markup;
- read the surrounding text and judged the object, mechanism and enforcement point against the rules in `taxonomy.md`.

Quote fidelity: all 40 quotes were found verbatim. Two quotes support the control only weakly:
- AH-067 quotes a ServiceNow release-note bug fix ("block and unblock actions fail without an error message"), not the control itself.
- CD-465 quotes only the default ("The sandbox is off by default").

Accuracy counting clear errors only:
- object 38/40 (95%);
- mechanism 39/40 (97.5%);
- enforcement point 37/40 (92.5%);
- all three right 35/40 (87.5%).

If the five borderline rows are also counted as errors, all three are right on 30/40 (75%).

Clear errors:
- EG-205, Intune block of unsanctioned AI app installs. Enforcement point is coded network_egress; it acts at install on a managed device, so lifecycle fits better.
- CD-361, managed settings invalid-entry handling. Enforcement point is coded identity_permission; this is policy management, so lifecycle.
- CD-737, Codex history.persistence. Mechanism is coded Record and report. The taxonomy codes retention of stored content as Cap a quantity, or Block when it is an on/off setting.
- AH-067, AI Control Tower block/unblock of external AI. The object is coded Tools; blocking an external AI system for the organisation is Lifecycle. The quote supports a bug fix, not the control.
- CD-619, Stop hook continuation cap. Coded Autonomy, lifecycle. Reconciliation rule 7 sends numeric caps to Usage limits, so the enforcement point should be spend_rate.

Borderline:
- CD-603. Enforcement point data_access versus tool_action.
- AH-164, label display. Mechanism Transform or steer versus Detect and flag.
- CD-685. Enforcement point identity_permission versus model_call.
- EG-037, Lakera. Detect, though enforce mode can block. The multi-action rule says code Block.
- CD-678. Object Tools versus Lifecycle (settings precedence).

Patterns:
1. Enforcement point is the weakest axis. Settings-management behaviour tends to be coded identity_permission instead of lifecycle.
2. Reconciliation rule 7 (numeric caps go to Usage limits) and the multi-action rule are not applied consistently outside the reconciled sample.
3. Errors concentrate in single-coder rows: 4 of 24 are clear errors, against 1 of 16 reconciled or held-out rows. Single-coder rows are 1,329 of the 2,111 (63%). So counts in `coverage.md` carry somewhat more noise than the Phase 3 kappas (0.86–0.87, measured on held-out rows) suggest. The error rate is not high enough to change any category's product coverage.

## Forward map: 30 disagreements resolved, 9 direct, 9 partial and 12 none

Decision rule, inferred from the 124 agreed cells and applied to the 30 disputed ones:
- **direct**: the analogue applies the same mechanism to a functionally equivalent object, for a core control of the agent category.
- **partial**: the analogue shares the mechanism or the object but not both, or matches only a peripheral control.
- **none**: no control in the domain's collected set acts on a comparable object.

Most adjudications applied the taxonomy's own boundaries. Release-stage and change controls are lifecycle, not model choice or answer accuracy. Real-time monitoring maps to detection, not records, as reconciliation decision 4 says. Three cells were checked against the stored pages:
- Network × cloud is none. `aws-scp.txt` and `azure-deny.txt` contain no network destination rule.
- Identity × card is none. Ramp's "lock date" ends spending on a fund; it is not a credential.
- Sensitive data × API gateway is direct. Cloudflare's page documents PII detection on incoming prompts, usable in rules.

Final totals (154 cells): 38 direct, 40 partial, 76 none.

| domain | direct | partial | none |
| --- | --- | --- | --- |
| algorithmic trading | 4 | 5 | 5 |
| card payments and spend management | 2 | 4 | 8 |
| cloud identity and infrastructure | 3 | 4 | 7 |
| email and DLP | 4 | 5 | 5 |
| IT change management | 3 | 1 | 10 |
| industrial safety | 1 | 3 | 10 |
| application access control | 4 | 2 | 8 |
| ERP segregation of duties | 1 | 4 | 9 |
| robotic process automation | 5 | 8 | 1 |
| API gateway and WAF | 7 | 2 | 5 |
| feature flags and release controls | 4 | 2 | 8 |

By agent category, Tools and actions has an analogue in all 11 domains (8 direct). Stored data has none in 9 of 11, and Answer accuracy none in 8. Robotic process automation and API gateways are the closest domains to agent controls; industrial safety and IT change are the furthest.

## Reverse map: 83 candidate rows merged to 61; 22 dropped because a direct agent equivalent is in the inventory

S listed 59 rows and H listed 56; 32 were on both lists. All `required_by` values match the source CSVs.

Several "not documented" claims by the coders are contradicted by `inventory-all.csv`. These 22 rows were dropped, each with the agent control that covers it:
- maximum messages limit: Agentforce email frequency limit (AH-022), MCP tool rate limiting (AH-418);
- conditional access risk signal: Entra risk-based Conditional Access for agents (EG-171);
- conditional access session control: token lifetimes (AH-189, AH-463, AH-048);
- attended robot permission limit: Workday delegate mode, the intersection of user and agent rights (AH-179), and Okta (EG-220);
- credential store and credential asset: AH-191, AH-219, BF-041, AH-142;
- data policy connector grouping: Copilot Studio same-data-group rule (AH-120);
- allowed or blocked merchants: AP2 allowed merchants and payees (AH-518, AH-520);
- lock date: ACP and AP2 expiry (AH-533, AH-515);
- default daily limit: AH-158;
- real-time authorization webhook: PreToolUse decisions and failClosed (CD-613, CD-827). Hooks are best-effort in places (CD-607);
- DLP notification: BF-017, AH-156;
- rule test modes: detect-only and inspect-only modes (BF-003, AH-074);
- kill switch flags: EG-186, AH-270, CD-522;
- environment separation: AH-220, AH-151;
- feature filter: hooks, CD-613;
- targeting rule: AH-026, AH-089, EG-267;
- geographic match: Conditional Access location for agents (EG-161);
- normal change, management of change and material change review: AI steward approvals and promotion gates (EG-232, EG-261, AH-234). These three exist as optional features. The forward map already coded them direct, so keeping them in the reverse list would contradict it.

On the 13 rows where the coders split none versus partial, 5 became partial and 8 became none.
- Partial: SoD access risk, with Lakera's toxic-combination detection (EG-062), which neither coder cited; firefighter log review; quarantine, with the Claude Code recently-denied list (CD-709); redirect; card-present restriction.
- None: conflict simulation, control with incident investigation, firefighter ID, DLP user override, guarded rollout, no shared devices, define change types, emergency change.

Two rows both coders called none became partial:
- annual CEO certification, on the strength of ServiceNow control attestations (EG-263);
- scheduled flag change, on the strength of Intercom's scheduled content switch (AH-369).

Final list: 61 rows, 50 partial and 11 none. 13 are required by law, 5 by regulator guidance, 4 by a standard and 39 are product features.

## Reach: coders agreed on 7 of 14 categories; the 7 splits are resolved by consistency with the conventional coding

| category | decision | why |
| --- | --- | --- |
| Answer accuracy | determinism mixed | Schema and disclosure checks are deterministic; groundedness is a classifier. |
| Model choice | determinism mixed | Semantic caching matches by similarity (BF-234). |
| Model choice | position boundary | Routing sits in gateways around the model. |
| Usage limits | position boundary | Provider and gateway meters sit around the model, as gateway rate limits do in the conventional set. |
| Identity | position boundary | The checks gate the agent from outside its logic. |
| Identity | reach company systems only | Policies cover tenant-registered resources (EG-164, CD-997). |
| Tools and actions | reach any system the identity touches | Tool calls run with held credentials against external systems (CD-627, CD-1042). |
| Network | reach end-user tools | Coding-agent egress is enforced on the user's machine, as for the data and autonomy rows the coders agreed. |
| Lifecycle | reach end-user tools | Managed settings and app-install blocks reach user devices, and the documented failures are where they stop. |

Evidence check: all 109 distinct evidence ids cited by either coder exist in `inventory-all.csv`. I read the quote for every id cited as a failure mode, and each supports the stated failure. There is one exception. H cited CD-076 (workspace geo fixed at creation) as a Stored data failure, but it is coded Model choice and is not a failure, so it was rejected. Stored data and Answer accuracy have no limitation rows in the inventory, and `reach.csv` says so rather than inferring that they have no failures.

## Claims that rest on marketing or non-documentation pages

In the agent inventory:
- 18 rows cite Credo AI product pages (agent-governor, ai-agent-registry, solutions). These include EG-269, a reach evidence id, and EG-277, a closest-control id.
- 3 rows cite Workday's newsroom or homepage (AH-203, AH-204, AH-206).
- 8 rows cite openai.com/enterprise-privacy.
- 33 rows cite ServiceNow community articles, including AH-052 and AH-060.
- 37 rows cite Salesforce Trailhead training modules, including AH-008, AH-015, AH-020, AH-022 and AH-024.

Trailhead and the community articles are vendor-authored but not reference documentation.

In the comparison set:
- the IT change management types (standard, normal, emergency) come from an Atlassian ITSM explainer page;
- NIST SP 800-53 CM-3 is quoted from the CSF Tools third-party mirror, not from NIST;
- industrial safety rests on one HSE bulletin quoting BS EN 61511, not on the standard itself.

These are flagged in the `source_flag` column of `map-forward.csv` and in the notes of `map-reverse.csv`. No top-10 gap in `gaps.md` depends only on a flagged page.

## Inconsistencies left for the report

The coders' forward and reverse maps were not coded against each other. The forward map called the Tools × card analogue (the real-time authorization webhook) direct. The reverse map then listed the same webhook as lacking a direct equivalent. The same happened with Logs × email (DLP incident report) and Lifecycle × industrial safety (management of change). The adjudicated files are now consistent: a comparison control appears in `map-reverse.csv` only if no agent control in the inventory is a direct equivalent.

What remains is a distinction the report should make explicit: "exists as an optional feature at some vendors" (no gap row) is different from "required". The gap ranking uses `required_by` in the home domain for that reason.
