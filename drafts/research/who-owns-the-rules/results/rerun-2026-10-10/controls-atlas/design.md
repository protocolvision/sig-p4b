# Agent and model controls atlas: research plan (pre-registered)

11 October 2026. A second report accompanying "Who owns the rules". Written before any new source is collected.

## Questions

1. What kinds of rules can firms set on AI agents and models today, across enterprise control tooling?
2. How do those controls cluster into a taxonomy: what is constrained, by what mechanism, at which enforcement point, and who sets the rule?
3. How do they compare with control systems in other domains? Which agent controls have a mature analogue, and which analogues have no agent equivalent?

## Unit of analysis

A **control** is one documented setting, policy or feature that constrains, transforms, approves or records what an AI model or agent may do. One product usually has many controls.

Examples:
- Block responses containing a denied topic.
- Cap tokens per user per day.
- Require approval before an agent sends an email.
- Deny network egress except to allowlisted domains.
- Log every tool call.

## Phase 1. Control inventory (documentation, public only)

**Sample, fixed now.** About 45 products in eight groups. Products in groups A and C are reused from the platform-controls study where stored pages exist.

| Group | Products |
| --- | --- |
| A. Business agent platforms | Salesforce Agentforce; Microsoft Copilot Studio; ServiceNow AI Agents; Google Gemini Enterprise / Agent Builder; Workday agents; UiPath; Zendesk AI agents; Intercom Fin; IBM watsonx Orchestrate |
| B. Cloud agent runtimes and model platforms | AWS Bedrock (Agents, AgentCore, Guardrails); Azure AI Foundry (Agent Service, Content Safety, Prompt Shields); Google Vertex AI (Model Armor, safety settings); Databricks Mosaic AI Gateway |
| C. Model provider enterprise and API controls | Anthropic (Claude Enterprise, Console and Admin API, usage and spend limits); OpenAI (ChatGPT Enterprise, API projects, rate and usage limits, data controls); Google Gemini API; Mistral (if documented) |
| D. Coding and desktop agents | Claude Code (permissions, managed settings, hooks); OpenAI Codex; GitHub Copilot (policies, coding agent firewall); Cursor; Amazon Q Developer |
| E. Guardrail frameworks and AI security products | NVIDIA NeMo Guardrails; Guardrails AI; Lakera Guard; Protect AI or Prompt Security (whichever documents controls); Meta Llama Guard / Prompt Guard |
| F. AI and MCP gateways | Cloudflare AI Gateway; Kong AI Gateway; Portkey; LiteLLM proxy (budgets, rate limits); an MCP gateway with public docs (e.g. Docker MCP Gateway or Microsoft MCP support in Azure API Management) |
| G. Identity, data and governance controls | Microsoft Entra Agent ID and Conditional Access; Microsoft Purview (DSPM for AI, DLP); Okta for AI agents; ServiceNow AI Control Tower; Credo AI |
| H. Agent protocols | MCP (authorisation, tool annotations, elicitation); A2A; AP2 (mandates); ACP |

**Extraction.** For each product, record each documented control as one row:
- product, group, control name;
- **object:** what it constrains;
- **mechanism:** what it does;
- **enforcement point:** where in the flow it acts;
- **scope:** whose behaviour it covers (organisation, project, user, agent, tool, session);
- **setter:** who can set it;
- **default:** on or off by default, if documented;
- a verbatim quote of 40 words or fewer, the source URL and the fetch date.

Pages are stored in `corpus/b-raw/controls-atlas/<group>/`. No sign-ins. Quotes are checked by script.

## Phase 2. Taxonomy (built twice, independently, then reconciled)

1. **Normalise.** Merge duplicate controls within a product; keep a distinct row where vendors differ.
2. **Two independent card sorts.** A Sonnet agent and a Haiku agent each build a taxonomy bottom-up from the control rows, without seeing each other's work. Each gives category names, definitions and assignments, on two axes: **object** (what is controlled) and **mechanism** (how).
3. **A data-driven check.** Embed control descriptions (all-mpnet-base-v2, local), cluster them (HDBSCAN), and compare the clusters with both card sorts using adjusted Rand index.
4. **Reconcile.** A fresh Opus agent merges the two sorts into one taxonomy:
   - object axis: 8 to 14 categories;
   - mechanism axis: 4 to 7 categories;
   - enforcement-point axis: fixed list below.
   
   Each category gets a definition and an inclusion rule.

**Fixed enforcement points:**
- before the model (input);
- inside the model call (model choice, parameters);
- after the model (output);
- before a tool or action;
- data access;
- network egress;
- identity and permissions;
- spend and rate;
- human approval;
- logging and audit;
- lifecycle (publish, version, retire).

## Phase 3. Verification

**Coder agreement.**
- Hold out 120 control rows that were not used to build the taxonomy, plus 24 seeded synthetic controls with known categories.
- Two coders from different model families (Haiku, Sonnet) assign each one an object, mechanism and enforcement point.
- Report Cohen's kappa per axis.
- **Gate:** kappa ≥ 0.6 on the object and mechanism axes, and seed accuracy ≥ 0.8.
- If either gate fails, the Opus reconciler revises the definitions once and the hold-out is re-coded. Report both rounds.

**Coverage.** For each category, record how many products and groups document at least one control. A category documented by only one product is flagged.

**Review.** A fresh Opus reviewer:
- spot-checks 40 control rows against the stored pages;
- checks the taxonomy definitions and the coverage counts.

## Phase 4. Comparison with other control systems

Comparison domains, from primary texts and official documentation:
1. **Algorithmic trading:**
   - EU RTS 6: pre-trade controls (price collars, maximum order value and volume, maximum messages), kill function, real-time monitoring, post-trade controls;
   - SEC Rule 15c3-5 (market access controls).
   
   The stored texts from the main study are reused.
2. **Card payments and spend management:** issuer spending limits, merchant-category blocks, transaction approvals.
3. **Cloud identity and infrastructure:** IAM policies and permission boundaries, service control policies, budgets and quotas.
4. **Email and data loss prevention:** outbound mail rules, DLP block and justify, quarantine.
5. **IT change management:** standard, normal and emergency changes; approvals.
6. **Industrial safety systems:** interlocks and safety instrumented functions (IEC 61511 summaries), where public.

**Mapping.** For each agent control category, record:
- the closest analogue in each domain, coded **direct**, **partial** or **none**;
- the reverse direction: analogue controls that have no agent equivalent. Examples to test: a mandatory kill function, maximum order value as a per-action value cap, message throttles, and two-person approval.

Two coders do the mapping and Opus adjudicates.

**Required features.** For each domain, note which controls are *required by law or rule* and which are *optional product features*.

## Phase 5. Report

A second interactive report in the house style, published as an artifact. It contains:
- the taxonomy as an explorable map (categories by enforcement point, with example controls and product coverage);
- the comparison matrix against trading and the other domains;
- the gaps;
- a short "what to require of your vendors" checklist.

Every claim carries a confidence chip. It links to and from the main report, and the data goes to GitHub.

## Limits stated in advance

- Documentation shows what products offer, not what firms switch on.
- Vendor documentation changes quickly; the snapshot is dated.
- Some documentation is gated or rendered by script and cannot be retrieved; this is recorded per product.
- Analogue mappings are judgements, reported with agreement statistics.
