# Final adversarial review: controls atlas

11 October 2026. A fresh Opus reviewer. I recomputed the counts from the CSVs and searched `inventory-all.csv` for each "no product does X" claim.

## Critical fixes: four blind-spot claims are contradicted by the inventory, and "no law requires" is contradicted by the study's own record

1. **Kill function (gap 1, blind spot 1, forecast 10).** EG-237 is ServiceNow's "Pause … global transaction processing across all MCP servers simultaneously". The inventory calls it a "kill-switch analogue", but no output cites it.
   - The blind-spot search claim ("only AH-270") is wrong.
   - Narrow the claim to "no control cancels in-flight actions across all of a firm's agents".
   - Forecast 10 must say whether a gateway-wide pause counts. As written, it may already resolve against itself.
2. **Law.** Several statements are contradicted by the study's own `instruments/I4-required-functions.csv`:
   - gaps.md: "nothing … requires them of agents";
   - gap 1: "none is required";
   - lineage-final.md: "agents have no date yet";
   - log line 161: "no law yet requires any vendor control".
   
   That file records EU AI Act Art 14(4)(e), a "'stop' button" for high-risk systems. It is enacted and applies from 2 December 2027 (Annex III). Say "none in force yet" and cite it. Forecast 12 survives only through "specifically for AI agents".
3. **Two-person approval (blind spot 4).** Copilot Studio documents "multistage approvals" in agent flows (AH-136). ServiceNow has sub-approvals (EG-232).
4. **Post-action checks (gap 4, blind spot 6).** Four documented controls detect behaviour and stop the agent:
   - EG-169 and EG-171 (Entra), AH-171 (Agent 365), CD-719 (Codex) and EG-239 (ServiceNow).
   
   Narrow the claim to "no check on the business effects of completed actions, and no reversal".
5. **Delegation (blind spot 8).** The claim "nothing on chain depth or scope" is contradicted for subagents: CD-302, CD-447 (delegated task screened at spawn), EG-255 (numeric subagent limits) and CD-835. Restrict it to cross-agent (A2A) chains.
6. **Cross-run throttle (blind spot 9).** Some counters already persist across runs:
   - AH-405, CD-027, CD-212 and CD-445.
   
   What is missing is narrower: a counter of repeated errors that only a person can re-enable.
7. **"Nine of ten largest gaps are trading law."** This is true by construction. The ranking puts law first, and all 13 law rows are trading, the only domain where binding law was collected. Say so in the heading.
8. **Level-5 GA.** A-058's stage note says Agent 365 was "later updated to GA", and P-102's URL reads "generally-available". The claim "only two GA" and forecast 3's baseline probably undercount.
9. **"Agents fastest of any domain."** This holds only on the product-only column. Counting standards, APIs reached stage 5 in 3.7 years (XACML), against 3.3 for agents. Both baselines are censored. Downgrade it and name the rule.

## Other corrections

- **Products vs vendors.** The 46 products are 31 vendors. At vendor level, Tools and Sensitive data lead (26), Logs follows (25), and Network is lowest (10, against 12 for Answer accuracy). Report both levels.
- **Thin cells.** 95 of 370 product × object cells rest on one row, and 28 on a single single-coder row.
- **Non-reference pages.** Three products rest wholly on such pages:
  - Agentforce: Trailhead, 37 of 37 rows;
  - ServiceNow AI Agents: community and store pages, 35 of 35;
  - Credo AI: product pages, 18 of 18.
  
  Forecast 9's "all nine" leans on them.
- **Timeline coverage.** The timeline has no events for ServiceNow, Workday, IBM or Gemini Enterprise. "Autonomy and accuracy stalled in 2026" is partly an artefact of collection.
- **Wording and anchors.**
  - "Roughly doubled each year" is wrong: growth was ×4.2, ×2.9 and ×1.8.
  - The 2021 start point is a Credo AI marketing page in the archive (A-001).
  - The first level-5 events (A-050, A-058) are launch blogs; cite P-085 (GA).
- **Normalisation.** Vendor names in `timeline-final.csv` are not normalised (Okta and Okta (Auth0)), so a naive recount gives 147 types and 27 vendors.

**Confirmed by recomputation:** every coverage table, the map totals (38/40/76; 61 reverse rows), the timeline counts (289 availability events; 268/16/5 by evidence), the seven level-5 events, and the quarterly shares and type counts.

## Forecasts are dated and checkable; one may already be resolved

- Forecast 10: see fix 1.
- Forecast 3: re-baseline (fix 8).
- Forecasts 1 and 2 need a re-run of a judgement-coded instrument; pre-commit it with blind coders.
- Forecast 9's "already common for GDPR" has no evidence behind it.
- No other forecast is resolved in the record.

## Deviations to disclose (only the first is logged)

1. The taxonomy was built on a balanced sample of 662.
2. 1,329 rows (63%) were coded by a single coder (Sonnet), and the held-out rows carry Sonnet's code only. Single-coder clear errors: 4 of 24.
3. Determinism, position and reach coding was not done for the six Phase 4 domains.
4. The determinism × reach map from Addendum 3 is missing.
5. Timeline events have no mechanism or enforcement-point codes.
6. No reverse-map agreement is reported (32 of 83 rows overlapped). Two-person approval was never mapped.
7. Lineage coder 1 was the collector, not blind. The log says coder 2 was Opus; the file says Sonnet.
8. Sample changes:
   - Gemini Code Assist added;
   - Lakera and the archived LLM Guard chosen;
   - AWS split into three products.
9. Level 4 is defined differently in Phase 2b ("agent-aware") and Addendum 3 ("identity- or actor-aware").
10. There is no per-row fetch date.
11. Comparison sources:
    - no Visa or Mastercard documentation;
    - industrial safety rests on one HSE bulletin;
    - NIST CM-3 comes from a mirror;
    - IT change comes from an Atlassian explainer.
12. Three CDX request pairs were sent under 5 seconds apart.

## Ten strongest, safest findings

1. **High.** 2,111 controls (2,046 excluding gap rows) from 46 products and 31 vendors sort reliably into 14 objects and 7 mechanisms. Kappa 0.86–0.87, seeds ≥0.96.
2. **High.** Identity, logs, tools and usage limits are near-universal: at least 32 of 46 products and at least 25 of 31 vendors.
3. **High.** Controls moved from content to action. Events at levels 4–5 were 5% in 2024 and 54% in 2025, and the result holds on primary sources only.
4. **High.** Anthropic documents its managed settings as "a client-side control, not a security boundary" (CD-411), and a local administrator can edit them (CD-682). Gemini Code Assist has "no undo" for external changes (CD-1042).
5. **High.** Conventional enterprise controls are mostly deterministic, 72 of 83. Classifier-based agent controls cluster in content and injection.
6. **Medium-High.** Value caps exist only in the payment protocols (AH-523, AH-532). A text search finds none on other tool calls.
7. **Medium-High.** Central runtime policy engines are new. The first GA is AWS AgentCore Policy, March 2026 (P-085), and only a handful of vendors have one.
8. **Medium.** Off switches block sign-ins or pause gateways (EG-173, EG-186, EG-237). None documents cancelling in-flight actions across all agents.
9. **Medium.** Approvers are increasingly models: CD-731 (Codex), EG-250 (ServiceNow), AH-136 (Copilot Studio) and AH-285 (UiPath escalation memory).
10. **Medium.** Trading law requires kill functions, firm-wide limits, per-order caps and throttles. For agents these are optional or absent, and none is required before December 2027.
