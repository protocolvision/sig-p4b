# Forecast: agent and model controls, 11 October 2026 to 10 October 2027

11 October 2026. These forecasts follow the Phase 2b design. Each one is a dated, checkable statement with a probability. Each rests on one or more of three grounds:
- **(a)** the quarterly trend in `timeline-analysis.md`;
- **(b)** previews and betas in `timeline-final.csv` that have no GA event in the record;
- **(c)** scheduled rules. For these I use the main report's dates:
  - EU AI Act Art 4, applying since 2 February 2025;
  - Colorado SB26-189 from 1 January 2027;
  - EU Annex III from 2 December 2027 under the Omnibus.

"Not GA in the record" means only that the three collectors found no GA event by 10 October 2026. Some of these may already be GA. Where that is plausible, the forecast resolves on documentation and the probability is raised. Probabilities are the authors' judgement, informed by the base rates noted under each forecast.

## Summary

| # | By | Statement | Probability | Ground |
|---|---|---|---|---|
| 1 | 2027-09-30 | A re-run of Phase 2b with the same vendors, method and unit finds at least 165 vendor × object × level control types available (146 at Q3 2026) | 0.70 | a |
| 2 | 2027-09-30 | At least 50% of new availability events in Q4 2026–Q3 2027 are at levels 4–5 (64% in the previous four quarters, falling) | 0.70 | a |
| 3 | 2027-09-30 | At least four vendors in the atlas sample have a GA level-5 control: a central, declarative policy evaluated on agent tool calls (two now: AWS, Anthropic) | 0.60 | a, b |
| 4 | 2027-09-30 | Databricks documents Unity Gateway service policies (external guardrail and request-tag policies before model or MCP calls) as generally available | 0.65 | b |
| 5 | 2027-06-30 | Google documents the Model Armor integration with Agent Gateway as generally available | 0.60 | b |
| 6 | 2027-09-30 | Microsoft documents the Foundry Agent Service human-in-the-loop approval step as generally available | 0.60 | b |
| 7 | 2027-06-30 | Anthropic documents Claude Enterprise inference hooks (external allow/deny verdict before inference) as generally available | 0.55 | b |
| 8 | 2027-03-31 | GitHub documents the Agent HQ enterprise agent governance layer (policies, audit, allowed agents) as generally available (resolves yes if it already is) | 0.75 | b |
| 9 | 2027-10-10 | At least two of the nine group-A business agent platforms publish documentation that maps an agent oversight, review or override feature explicitly to EU AI Act Art 14 or 26, or to Colorado SB26-189 | 0.60 | c |
| 10 | 2027-10-10 | No vendor in the atlas sample documents one control that cancels all in-flight actions of all of a tenant's agents (not only blocking new sign-ins) | 0.75 | a, c |
| 11 | 2027-10-10 | AWS, Databricks, Anthropic or Microsoft publishes a documented example policy that caps a numeric argument, such as an amount, on a non-payment agent tool call | 0.50 | a, b |
| 12 | 2027-10-10 | No binding law or rule in force in the EU, UK, US federal law or Colorado requires a kill function or a per-action value cap specifically for AI agents | 0.85 | c |

## Evidence for each forecast

**1. Scope keeps growing, but more slowly than in 2025 (0.70).** The series:
- 2025 added 55 types;
- 2026 Q1–Q3 added 19 (5, 7 and 7);
- the last four quarters added 32.

At the 2026 pace, Q3 2027 reaches about 171. At the four-quarter pace it reaches about 178. 165 needs 19 more types, the 2026 pace for only three quarters. The main risk is that the slowdown reflects vendors running out of cells to fill, which would put growth below 5 a quarter. A re-run may also backfill earlier events, which would move the baseline. Resolve on the count to 2027-09-30, whatever the backfill.

**2. Agent-scoped controls stay the majority of new events (0.70).** The share of new events at levels 4–5 was 71%, 69%, 61% and 52% in Q4 2025 to Q3 2026, and 64% across those four quarters. The trend is falling because identity, spend and model controls at levels 1–3 have come back. A threshold of 50% allows that decline to continue for one more year at about the same rate. This is the least robust measure, because level 4 is a broad level (see `timeline-analysis.md`).

**3. More central policy engines reach GA (0.60).**
- GA level-5 controls now: P-085 (AWS AgentCore Policy, GA March 2026, after a December 2025 preview, P-082) and P-115 (Anthropic, GA September 2026).
- In preview or beta:
  - A-050, GitHub Agent HQ, preview October 2025;
  - A-058, Microsoft Agent 365 control plane, early access November 2025;
  - G-108, Databricks service policies, beta October 2026.
- Base rate: AWS took 3 months from preview to GA. If two of the three reach GA, the forecast resolves yes.
- A-070 records Purview data security for Agent 365 as GA on 1 May 2026. Agent 365 itself may therefore already be GA (inference). If so, the forecast needs only one more.

**4. Databricks service policies reach GA (0.65).** Databricks moved AI Gateway from beta (G-095, February 2026) to Unity Gateway GA (G-103, August 2026) in 6 months. ABAC grants for MCP reached GA in August 2026 (G-106). Service policies have been beta since at least G-103 ("remain in Beta") and gained new types in October 2026 (G-107, G-108).

**5. Model Armor with Agent Gateway reaches GA (0.60).** The base rates are mixed:
- the MCP-server integration went from preview (P-083, December 2025) to GA (P-091, April 2026) in 4.5 months;
- the GKE and load-balancer integration (P-056, April 2025) and the Vertex default configuration (P-065, July 2025) have no GA event after 15 to 18 months.

The deadline is set at June 2027, 14 months after the preview (P-092, April 2026).

**6. Foundry human-in-the-loop approval reaches GA (0.60).** It has been in preview since August 2026 (P-108). Microsoft's base rates:
- Agent Service: preview December 2024 to GA May 2025 (P-044 to P-058), 5 months;
- Entra Agent ID: preview May 2025 to GA April 2026 (P-061 to A-067), 11 months;
- Task Adherence: preview November 2025 (P-078), not GA in the record.

**7. Anthropic inference hooks reach GA (0.55).** In beta since 5 August 2026 (P-110). Anthropic's base rates:
- Managed Agents: beta April 2026 (P-088), with GA features from May 2026 (P-095, P-111, P-112, P-115);
- task budgets: beta April 2026 (P-090), not GA in the record after 6 months.

**8. GitHub Agent HQ governance reaches GA (0.75).** In preview since October 2025 (A-050). GitHub's agent controls in the record moved from preview to GA in 6 to 11 months:
- MCP allowlists: preview September 2025 (A-040), GA August 2026 (A-076);
- CLI controls: preview October 2025 (A-046), GA April 2026 (A-068).

**9. Vendors map oversight features to the scheduled laws (0.60).**
- Colorado's designated-reviewer duty starts 1 January 2027. EU Annex III deployer oversight (Art 26(2)) applies from 2 December 2027.
- All nine group-A platforms already document escalation, takeover or approval controls (coverage: Autonomy 8 of 9, Tools 8 of 9).
- Mapping these to a law is cheap, and it is already common for GDPR. This forecast is an inference.
- Risk: vendors may describe compliance in marketing pages rather than in documentation. Resolve on any official vendor page, documentation or trust-centre page.

**10. No all-agent kill function (0.75).**
- None of the 289 availability events and none of the 2,046 inventory controls cancels pending actions across all agents.
- The closest controls are:
  - Entra "disable risky agent" and blueprint disable, which stop sign-ins (EG-173, EG-186);
  - ServiceNow agent containment (AH-066);
  - MCP task cancellation, one task at a time (AH-427).
- The Autonomy object added no vendor in 2026.
- No scheduled rule requires a kill function (gap 1 in `gaps.md`).
- The 0.25 for a yes reflects how close the Microsoft and ServiceNow containment controls already are.

**11. A documented per-call value cap outside payments (0.50).**
- Two vendors now run central policy engines that evaluate each tool request:
  - AWS AgentCore Policy, Cedar (BF-027, "evaluates each request against defined policies in the policy engine before allowing tool access");
  - Databricks service policies (G-108).
- In principle these can test a tool argument against a number. This is an inference. No stored page documents a value cap (gap 3 in `gaps.md`).
- The only value rule in the corpus outside the payment protocols is a prompt instruction: UiPath's example tells the agent to escalate refunds "over $100" (`ui-prompts.txt`). That is a natural-language rule, not an enforced one.
- Resolve yes on a documented example or a built-in setting.

**12. No binding agent-specific control law (0.85).**
- The binding or scheduled rules in the main report require AI literacy (Art 4) and named overseers (Art 26(2), Colorado). They do not require controls.
- The main report forecasts that finance regulators will reuse trading templates (0.6 by end 2027). That forecast covers guidance and supervisory expectations. Forecast 12 counts only binding text in force. The 0.15 covers a binding finance-sector rule, or a change made during the Annex III run-up.
