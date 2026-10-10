# Where agent rules change: results

10 October 2026. Pre-registered in `design.md`. Reviewed by a fresh Opus agent in `review.md`, whose fixes are applied: Agentforce coded as admin, UiPath coded as test before publish, and three silent business-owner fields recoded from no to not documented.

## Verdict under the reading rule: mixed

| Condition | Result | Rule |
| --- | --- | --- |
| 1. Products in groups A–C that document limits changed in a product, platform or managed config by a named permission | **15 of 26 (58%)** | needs two-thirds (18). **Fails.** Excluding four pure retrieval failures: 15 of 22 (68%), sensitivity only |
| 2. Of those, products that document at least one change control | 13 of 15 (8 of 15 counting only controls on the changes themselves) | needs half. Holds |
| 3. Recode: tool_change against decision | 25 against 16 | tool_change must lead. Holds, but rests on two speakers (below) |
| H-none (fewer than half document any in-product way) | 25 of 26 document where limits are set | not met |
| H-decide (decision at least 2 to 1 over tool_change) | not met on final codes | not met |

H-local is **not supported** as pre-registered. Its rivals are not supported either.

## What the evidence shows

**By product group:**
- **Enterprise assistants and coding agents** fit H-local most closely: 7 of 8 pass condition 1.
  - In Claude Enterprise and Claude Code, ChatGPT Enterprise, Codex, GitHub Copilot and Cursor, an owner or admin role sets agent limits in admin settings or managed config.
  - The organisation-level setting overrides the user.
  - Most products keep an audit log.
  - None of the eight names a business owner separate from the admin.
- **Business agent platforms** split.
  - Copilot Studio, Agent 365 and Entra, Workday, UiPath, Intercom, AWS AgentCore and Agentforce document an admin or permission that changes limits.
  - Gemini Enterprise, Zendesk, IBM Orchestrate and Okta don't, or only document who can reach an agent.
  - ServiceNow could not be retrieved.
- **Governance platforms** hold inventories, approvals and audit evidence. All but Purview name no editor of the limits.
- **Protocols** leave limits to whoever implements them (MCP, A2A), or to the end user through signed mandates (AP2).

**Two layers sit side by side.** Several sources pair the technical editor with a business decider:
- "These guardrails are controlled by your admin and typically signed off by your internal leadership or key decision-makers." (Salesforce, sf-guard)
- "Sponsors: Business representatives accountable for the agent's purpose and lifecycle decisions", listed beside technical owners. (Microsoft Entra, ms-entra)
- "our AI governance committee (including leaders from our Engineering, Product, Legal, and Information Security teams) performs an analysis and review of each AI tool for which pre-approval is required" (Rubrik 10-Q, 0001943896-25-000042_3)

**Recode (P2).** The sources split by kind:
- **Speech** is mostly people changing agents themselves: 24 tool_change against 6 decision. Examples: "We changed the guard rails" (M021) and "I uploaded our brand guidelines" (M073).
- **Postings** are mostly governance roles defining policy: 10 decision against 1 tool_change. Example: "Define how AI agents are provisioned, governed, monitored, and decommissioned."

**Limits of the recode.**
- 17 of the 24 speech tool_change codes come from two speakers (M073, M072). Without them, decision leads 16 to 8.
- Agreement between the coders beyond chance was low (0.20). Both passed every seeded item, but one coded leniently and one strictly. 32 of the 41 positive codes rest on the Opus adjudication.

**Filings (P3; single coder).** 127 passages discuss AI or agent controls, from 59 filers. Mostly vendors describe controls as product features: 51 in-product settings and 18 separate platforms. They seldom say who manages them; the only named human owners each come from one company. Departures from the plan: P3 searched nine terms instead of six and added a "customer" code. Cite P3 as company counts, not percentages.

## Reading

Where the rule change happens is answered: in admin settings, by a product role, usually under central policy. Who decides it is not. Vendors increasingly build the split into the product: an admin who edits, and a sponsor or "internal leadership" who signs off. The public record shows the edit permission much more clearly than the sign-off. So the gap the report describes is narrower than "no one". The change itself has an owner, a product permission. The decision behind it has no named holder outside a few vendor role designs and one company's committee.

## Cannot say

- whether these permissions are used, who holds them, or whether sign-off happens or is recorded;
- anything about the platforms whose documentation could not be retrieved: ServiceNow, parts of Salesforce, IBM, Credo, Zendesk and Okta;
- anything after October 2026.
