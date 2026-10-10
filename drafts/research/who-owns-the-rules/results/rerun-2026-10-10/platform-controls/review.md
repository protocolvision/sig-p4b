# Review: platform controls study (fresh Opus, 10 Oct 2026)

All census quotes match the cited stored pages (checked by script). The fixes concern coding judgement, not fabrication.

## Critical fixes

1. **The Agentforce permission is documented, so the "not documented" code is wrong.** sf-guard says: "These guardrails are controlled by your admin and typically signed off by your internal leadership or key decision-makers." Set change_permission to *admin*.
2. **UiPath change_controls should be *test before publish*.** ui-guardrails says: "Test thresholds during evaluation."
3. **Silence was coded as *no* for business_owner_field** (Copilot Studio, Intercom, AWS). Recode to *not documented*.
4. **Many "audit log" codes log agent activity, not changes to limits.** Examples: Workday, Purview, Codex. Condition 2 survives either reading, but the report should not say these products audit rule changes.
5. **Retrieval failures, not silence.** Nothing was retrievable for ServiceNow AI Agents (JS shell). ServiceNow Control Tower rests only on a user's community post (official docs are JS, product page 403). IBM watsonx.governance docs returned 403 or a JS shell. Credo's docs are gated (401). Partial: Zendesk, Okta, Salesforce Help, IBM Orchestrate.
6. **P3 departs from the pre-registration.** It searched nine terms where the design named six (it added access control, audit trail and approval), and it added a *customer* code that is not in the codebook. Disclose both.

## Census: the borderline decisions

Ten rows checked against stored pages. Borderline decisions:
- **Gemini Enterprise: fail.** goog-iam lists `agents.update`, but no agent limits.
- **Zendesk: fail.** zd-access controls which users can reach an agent, not what the agent may do.
- **IBM Orchestrate: fail** (no role named).
- **Okta and the five governance platforms with no named editor: fail.**
- **Gemini Code Assist: fail.** Tool limits are set "in your Gemini settings JSON" by each developer, which is not a named permission.
- **Purview: pass.** A DLP policy "prevents Microsoft 365 Copilot and agents from summarizing data" with sensitivity labels, set by the Compliance Administrator role.

## Applying the reading rule

**Condition 1 fails: 15 of 26 (58%) is below two-thirds (needs 18).** The 15 products that pass:
- Agentforce, Copilot Studio, Agent 365/Entra, Workday, UiPath, Intercom Fin, AWS AgentCore;
- Purview;
- Claude Enterprise, Claude Code, ChatGPT Enterprise, Codex, GitHub Copilot, Amazon Q, Cursor.

**Sensitivity check:** excluding the four pure retrieval failures gives 15/22 (68%), which narrowly passes. The strict count still decides.

**Condition 2 holds: 13 of 15 document a change control.** Agentforce and Amazon Q do not. Counting only logs or gates on changes (not agent activity), 8 of 15 still clears half.

**Condition 3 holds, but barely: tool_change 25 vs decision 16** (see P2).

**H-none is not met.** 25 of 26 products document some in-product, platform or config place where limits are set; ServiceNow AI Agents is the exception. **H-decide is not met** on the final codes.

**Verdict: mixed.** The study does not support H-local under its own rule. Governance platforms document where limits live but not who may edit them; agent products mostly name an editor (group C passes 7 of 8).

## P2: the tool_change lead is fragile

Coder S coded *neither* on 278 of 288 real items; coder H coded 70 positive. Both scored 10/10 on the seeds, so the seeds were too prototypical to test where each coder draws the line. That is why kappa is 0.20.

S is the more miscalibrated coder: it rejected plain tool changes such as "I uploaded our brand guidelines" and "I set it to weekly". H is lenient. The adjudicator split almost evenly (32 to H, 29 to S). As a result, 32 of the 41 positive codes rest on one Opus adjudication.

I checked all 41 positives. About 5 tool_change codes are weak:
- L050 "here's a pool of data";
- L210 (garbled);
- L238 (prospective);
- L260 (building the agent, not changing it);
- L112 "We trained it" (unclear).

About 5 decision codes are weak:
- L036, L126 and L301 concern staff use of AI, not agent limits;
- L220 and L247 are generic governance boilerplate.

Dropping both sets leaves roughly 20 vs 11: even-handed.

The fragility is structural:
- **Two speakers carry the tool_change lead.** 17 of the 24 tool_change speech codes come from M073 (12) and M072 (5). M073 alone supplies 55 of 171 speech items: one practitioner tuning one chatbot. Without these two speakers the count is 8 tool_change vs 16 decision, which meets the H-decide 2:1 threshold.
- **The coders' agreed items reverse the direction.** On the 9 positives both coders chose, decision leads 5 to 4.
- **The two sources split by kind.** Postings are almost all decision (10 vs 1) and speech is mostly tool_change, so the result depends on the mix of sources.

## P3: single-coder risk

Of ten rows checked, seven are sound (Rubrik ×2, Extreme, Salesforce, SoundHound, Innodata, Microsoft). Three are doubtful:
- **Elastic is coded it_or_security**, but "human analysts handle judgment, verification, and approval" describes the product's users.
- **Blackbaud is coded customer**, but "defined governance and user controls" names nobody, so not_stated fits better.
- **Datavault is coded business_owner** for "executives, compliance teams, and domain experts", which is a mixed group.

The rare codes that matter for "who decides" each rest on one filer: committee_or_board is Rubrik only (5 repeated passages), business_owner is Datavault only, and it_or_security is Elastic only. With one coder, no seeds and judgement-heavy customer-vs-vendor calls, P3 should be cited only as filer counts with quotes, never as percentages.

## What the evidence says

Where products document agent limits, the limits sit in admin settings: permission sets, org policies and managed config. A named product role edits them, and central policy usually overrides local settings. Group C documents this most completely. Governance platforms record policies, approvals and owners, but none of the stored pages names who may edit an enforceable limit. Several sources pair a technical editor with a business decider: both layers, not permissions replacing decisions. Three quotes for a report:

- "These guardrails are controlled by your admin and typically signed off by your internal leadership or key decision-makers." (sf-guard, Salesforce Trailhead)
- "Sponsors: Business representatives accountable for the agent's purpose and lifecycle decisions" (ms-entra, set beside "Owners: Technical administrators…")
- "our AI governance committee (including leaders from our Engineering, Product, Legal, and Information Security teams) performs an analysis and review of each AI tool for which pre-approval is required" (Rubrik 10-Q, 0001943896-25-000042_3)

It cannot say whether firms use these permissions or who holds them, whether sign-off happens or is recorded, anything about unretrieved platforms, or anything beyond October 2026; and the speech evidence is two speakers deep.
