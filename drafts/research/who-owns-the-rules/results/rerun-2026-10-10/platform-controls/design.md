# Where agent rules change: platform controls study (pre-registered)

Protocols for Business · 10 October 2026 · added to the rerun at the user's request. This file is committed before any new source is collected or coded.

## Question

The rerun found that no public source names who decides when an AI agent's rules change. The user proposed an explanation, which we call **H-local**: agent controls live in software, either in separate governance platforms or built into each agent product or protocol. Whoever administers that software changes the rules locally. Ownership of a rule change is therefore a product permission, not a role in the organisation.

The rival explanations are:
- **H-decide:** changes are decided by people or bodies outside the tools (managers, committees, policy owners) and then implemented. The decision is simply unrecorded in public sources.
- **H-none:** most products give no in-product way to change an agent's limits, so changes happen through code releases or vendor defaults.

## Parts

### P1. Platform census (public documentation)

Sample, fixed now. One row per product; where a product has no public admin documentation, that is recorded as a result.

| Group | Products |
| --- | --- |
| A. Business agent platforms | Salesforce Agentforce; Microsoft Copilot Studio; Microsoft Agent 365 / Entra Agent ID; Google Gemini Enterprise (Agentspace); ServiceNow AI Agents; Workday Agent System of Record; UiPath agentic automation; Zendesk AI agents; Intercom Fin; AWS Bedrock AgentCore; IBM watsonx Orchestrate; Okta for AI agents |
| B. Governance platforms | ServiceNow AI Control Tower; IBM watsonx.governance; Credo AI; Microsoft Purview (AI governance features); OneTrust AI governance; Holistic AI |
| C. Enterprise AI assistants and coding agents | Claude Enterprise / Team admin controls; Claude Code managed settings and permissions; ChatGPT Enterprise admin controls; OpenAI Codex (enterprise and workspace controls); GitHub Copilot (organisation and enterprise policies, coding agent); Gemini Code Assist enterprise; Amazon Q Developer; Cursor business or enterprise |
| D. Protocols | Model Context Protocol (authorisation, server admin); Agent2Agent (A2A); Agent Payments Protocol (AP2); Agentic Commerce Protocol (ACP); Visa Intelligent Commerce or Mastercard Agent Pay developer terms (whichever has public docs) |

Codebook, one row per product. Every code needs a verbatim quote of 40 words or fewer from a stored page, plus its URL and fetch date.
- `limits_location`: where an agent's limits, permissions or guardrails are set.
  - **in_product:** a setting in the agent product.
  - **separate_platform:** a governance or identity product.
  - **code_or_config:** files, policy-as-code or managed settings.
  - **protocol_spec:** the spec leaves it to the implementer.
  - **not_documented.**
- `change_permission`: who can change those limits: the named role or permission (admin, owner, maker, org owner and so on), or "not documented".
- `change_controls`: any of approval workflow, versioning or history, audit log, test or staging before publish. Otherwise none or not documented.
- `business_owner_field`: whether the product names a business owner or sponsor separate from the admin (yes, no, not documented).
- `central_override`: whether a central admin can override or block local changes, such as an org policy over a project, or a managed setting over a user (yes, no, not documented).

### P2. Recode of existing evidence (no new collection)

Items:
- the agent-related posting tasks from phase 2 whose final code includes AO, PE or RD;
- the timestamped speech spans whose final code includes AO, PE or PV.

Question per item:
- **tool_change:** the text describes changing an agent's setting, permission, prompt or guardrail in a tool or platform.
- **decision:** it describes deciding or approving what an agent may do, separate from making the change.
- **both.**
- **neither.**

Two blind coders from different model families (Haiku and Sonnet), plus 30 hidden seeded items (10 for each of tool_change, decision and neither). Seed recall must reach 0.7 for each code. Disagreements go to blind Opus adjudication.

### P3. Filings

Search the 2,216 consensus filing passages for governance-platform and guardrail terms ("guardrail", "governance platform", "control tower", "agent registry", "permissions", "human oversight"). Code each hit for who is said to manage the control: IT or security, a business owner, a committee or board, the vendor, or not stated.

## Reading rule

**H-local is supported** if all three hold:
- in P1, at least two-thirds of groups A–C document limits that are changed in a product, platform or managed config by a named permission;
- in P1, at least half of those document at least one change control;
- in P2, tool_change items outnumber decision items.

**H-local fails** in either case:
- fewer than half of the products in groups A–C document an in-product or platform way to change limits (H-none);
- in P2, decision items outnumber tool_change items by at least 2 to 1 (H-decide).

Any other pattern is **mixed** and is reported as such. P3 is descriptive.

Expected limits:
- documentation describes what products allow, not what firms do;
- speech recall is about 0.5;
- the census is one point in time (October 2026).

## Process

1. Sonnet agents fetch and store public documentation in `corpus/b-raw/platforms/` (raw text, one file per page) and code P1, with quotes checked by script.
2. Two coder agents run P2 blind; a script scores the seeds.
3. A Sonnet agent runs P3.
4. A fresh Opus agent reviews each product for critical fixes.
5. Results go to `results/rerun-2026-10-10/platform-controls/`. The report section is written only after the review.
