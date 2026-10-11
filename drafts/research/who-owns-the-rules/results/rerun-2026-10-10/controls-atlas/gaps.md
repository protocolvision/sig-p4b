# Gaps: comparison controls with no direct agent equivalent (Phase 4 and 4b)

11 October 2026. Opus adjudication of `map-reverse-S.csv` and `map-reverse-H.csv`. Final list in `map-reverse.csv`: 61 comparison control types lack a direct agent equivalent (11 none, 50 partial). 13 of them are required by law, 5 by regulator guidance, 4 by a standard, and 39 are product features.

Ranking rule: first, whether the control is required by law, regulator guidance or a standard in its home domain (`required_by`, checked against `comparison-sources.csv` and `conventional-sources.csv`); second, the consequence if an agent lacks it (irreversible or unbounded harm ranks above loss of oversight or efficiency). Agent control ids are from `inventory-all.csv`.

## Nine of the ten largest gaps are legal duties in trading; the agent equivalents are optional features or absent

The trading rules (EU RTS 6, SEC Rule 15c3-5) require controls that bound what an automated system can do in one action, in aggregate, and in an emergency. For agents, the same controls are missing or exist only as optional features of a few vendors or protocols; nothing in the sources collected requires them of agents.

1. **Kill functionality** (RTS 6, law; agent equivalent partial). RTS 6 requires a firm to "cancel immediately, as an emergency measure, any or all of its unexecuted orders". Agent off switches stop new sign-ins (Entra blueprint disable EG-186, disable risky agent EG-173), and MCP and A2A cancel one task at a time (AH-427). None cancels all pending agent actions, and none is required. Consequence: a misbehaving agent keeps acting while the firm finds each run.

2. **Firm-wide risk limits** (RTS 6, law; none). Orders that "risk compromising the investment firm's own risk thresholds" must be blocked. No agent control limits the total exposure that all of a firm's agents create. Spend caps meter API cost (CD-852), and AP2 budgets cover one user's mandate (AH-524). Consequence: many agents, each within its own limits, can add up to an unbounded exposure.

3. **Maximum value per action** (RTS 6, law; partial). Per-action value caps exist only for agent payments, through AP2 amount ranges (AH-523) and ACP allowances (AH-532). No vendor documents a value cap on other tool calls that move value, such as orders placed through an API, refunds or transfers. Consequence: one wrong call can carry any amount.

4. **Post-trade controls and reversal** (RTS 6, law; partial). RTS 6 requires action, up to shutting the algorithm down, when a post-trade check triggers. Agent actions are logged (AH-192), but no vendor documents an automatic after-the-fact check that stops the agent. Gemini Code Assist states there is no undo for changes made outside the IDE (CD-1042). Consequence: errors are found late and stay in place.

5. **Implausible-order rejection and price collars** (15c3-5 and RTS 6, law; partial). These reject orders outside price or size bounds, or duplicates. Agents have schema validation of tool inputs (AH-416), fixed amount ranges for payments (AH-523) and idempotency keys (AH-536). These catch malformed or repeated calls. They do not catch well-formed calls with implausible values. Consequence: "valid but wrong" actions pass.

6. **Throttle with human re-enable** (RTS 6, law; partial). After a set number of repeated executions, the system must be "automatically disabled until re-enabled by a designated staff member". Agents have loop and iteration caps (AH-279, AH-435, BF-197). These end the run, and the next run starts unchecked. Consequence: a faulty loop recurs across runs.

7. **Firm's exclusive control of its controls** (15c3-5, law; partial). Managed rules outrank user settings (CD-314). Anthropic, however, documents server-managed settings as "a client-side control, not a security boundary" (CD-411), and a local administrator can edit the managed source (CD-682). Consequence: a user can change the limits the firm set.

8. **Accountable executive certification** (15c3-5, law; partial). The CEO must certify each year that the controls comply. The only agent analogue is a ServiceNow AI Control Tower record of control attestations (EG-263). It has no named signatory, no cadence and no legal duty behind it. Consequence: no single person is answerable for agent controls working.

9. **Stress testing** (RTS 6, law; partial). RTS 6 requires tests at twice the peak message volume of the last six months. Agent vendors offer vulnerability tests (AH-243), conversation simulators (AH-352) and batch tests (AH-387), but none documents a load test. Consequence: medium. It ranks here mainly because the law requires it.

## Outside trading, the largest gap is that guardrails are not required to be independent of the agent; segregation of duties comes next

10. **Independent safety layer** (BS EN 61511 via an HSE bulletin, standard; "SIS independent of BPCS" partial, "no shared devices" none). The standard requires the safety system to be "separate and independent" of the process control system. Gateway and guardrail services do run outside the agent (BF-129, EG-021). No vendor, though, documents a requirement that the guardrail share no model, host or runtime with the agent it guards. Client-side settings are explicitly not a boundary (CD-411). Consequence: a single failure can disable both the agent and its check, which is the failure HSE investigated.

Segregation of duties (product feature in SAP and Oracle; partial) is the next gap. The only agent analogue is Lakera's detection of one fixed "toxic combination" (EG-062). No vendor offers a configurable rule stopping one agent from holding conflicting tools, such as "create vendor" plus "approve payment". The consequence is high, but the stored SAP and Oracle pages present SoD as a product feature, not a legal duty, so it ranks eleventh under the rule above.

## Considered and not ranked

- Quick disable (FINRA 15-09, guidance). One-step disable exists for Entra (EG-173) and ServiceNow (AH-066) agents, so this overlaps with gap 1.
- Emergency shutdown, inspect-and-test, risk assessment (HSE, guidance). These are partly met by off switches, pre-publish evaluations and AI risk ratings.
- Emergency change and change-type definitions (IT change). These are product features or a standard. The Atlassian source is a vendor explainer page.
- Quarantine, DLP user override and guarded rollout. These are product features with moderate consequence.

## Where the evidence is weak

Each agent-side "partial" rests on documentation of what is offered, not on what firms switch on. Several of the closest agent controls come from pages that are not product documentation:
- EG-277 (drift alerts) and EG-269 come from Credo AI marketing pages.
- AH-052 and AH-060 come from ServiceNow community articles.
- AH-008, AH-015, AH-020 and AH-022 come from Salesforce Trailhead training modules.

None of the top ten rests only on these pages. On the comparison side, the IT change rows come from an Atlassian explainer, and the NIST CM-3 text comes from the CSF Tools third-party mirror.
