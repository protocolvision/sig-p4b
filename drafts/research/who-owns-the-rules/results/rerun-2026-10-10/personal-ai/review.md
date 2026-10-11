# Personal AI at work: fresh review of parts A and B

11 October 2026. I checked every prevalence row and 20 control claims against the stored pages. The quotes are verbatim; the problems are in the framing.

## Critical fixes

1. **The telemetry measures personal accounts on company paths, not the personal-device gap.** Netskope's 47% comes from its own proxy traffic. LayerX's 67% comes from its extension in "millions of enterprise browser sessions". Both counts exist only because a company control saw those logins and told personal accounts from corporate ones. Reword the prevalence heading and the "nearly 90% … bypass oversight" line accordingly. No source measures personal accounts on personal devices. LayerX's split also contradicts the "Not retrieved: a browser tool that tells personal from corporate logins" line.
2. **The NCSC 71% is not a Microsoft figure.** The page says only "one study". Delete "The Microsoft 71% UK figure".
3. **The AI Act Art 4 entry leads with superseded wording.** "ensure a sufficient level" is the page header. The same page says that after the Omnibus (in force mid-July 2026) "no specific – or 'sufficient' - level is mandated". Lead with the amended text. Add that Art 4 has applied since 2 February 2025. Keep the 2 versus 3 August flag.
4. **Claude "Keep both accounts" is mis-scoped.** It applies to joining without domain capture [claude-move]. Under capture, unmigrated accounts "are deactivated" [claude-claim]. Personal accounts survive only under a Team plan, under Enterprise without capture, or on a non-company email (the last is inference).
5. **Recall in filings is weak, and the vendor exclusion was applied unevenly.** Of the 10 dropped candidates I checked, 6 are wrongly dropped:
   - Freshworks #625 ("unauthorized use or misuse of generative or agentic AI by our employees");
   - Tenable #746;
   - IDT #603;
   - Sprinklr #631;
   - Rubrik #827;
   - speech M064 #444 ("bad enough on your personal laptop but … at the corporate level"). It is the only practitioner passage on this.

   The other 4 (Comcast BYOD, "personal accountability", Zscaler product text, Anthropic BYOD #73) were rightly dropped. Kept Tenable #90 is attack-surface product text and should go, as Zscaler's did. Restoring these strengthens "filings state risk, not controls".

## Coding check (15 kept hits)

10 are fair: AlphaSense #10–12, Corebridge #19, Cencora #23, OneTrust #33–34, CDW #51, Rimini #85 and speech #98/#100. 5 are not:
- Pacific Life #0 is DLP admin on a sanctioned platform. Drop it or code it approve.
- Cencora #22 and Abbott #67 are about AI product security. Drop both.
- Upstart #86 is risk-only, not policy.
- Arcturus #77 and M052 #99 do not name security. Code who as not stated.

The 25 filing passages hold about 15 distinct texts (Tenable, JFrog, Upstart, WD/Sandisk repeat); report those.

**Security concentration holds, but it is thinner than the count suggests.** The 22 of 34 control spans in security roles come from 14 employers, and Cencora, AlphaSense and CDW supply 10 of them. After the drops it is about 19 of 31. Note that the search terms are security vocabulary, which builds in part of the result.

## Smaller flags

- Entra: say "v1 needs a proxy" (v2 not retrieved).
- Claude Code documents more edges than the findings report: the interactive login does not enforce forceLoginMethod, Console credentials are not checked against the org, and server-managed settings "can't redirect a developer's first login".
- Netskope: the base is customers that already run a proxy.
- Samsung: the scope quote is third-hand (Fox, citing Bloomberg).
- NL AP: the news text says "employers shared". Paraphrase. The Microsoft and Salesforce surveys (2024, 2023) predate agents.

## Statements solid enough for the section

1. **Personal-account use is common, and the visible part is shrinking.** Personal accounts fell from 78% to 47% and approved accounts rose from 25% to 62% (Oct 2024–Oct 2025): "Nearly half (47%) of people using generative AI platforms are doing so through personal accounts" [netskope-cd]. *Caveat:* vendor telemetry via news; covers company paths only.
2. **Blocking is rare, and bans stopped at company property.** 16% of organisations block public genAI by default (Gartner 2025). Samsung banned genAI "on company-owned devices as well as internal networks" [samsung-fox]. *Caveat:* Gartner gives no sample size; the Samsung report is third-hand, from 2023.
3. **Network controls reach only traffic the company routes.** "organizations can specify the list of tenants that users on their network are permitted to access" [entra-tr]. *Caveat:* v1, vendor documentation.
4. **Identity reach follows the email domain and the plan.** Claude Enterprise capture: "no non-Enterprise accounts can exist on your verified domain". Team plans only block new accounts [claude-claim]. *Caveat:* one vendor, since ChatGPT and Gemini pages were not retrieved; private-email accounts are out of reach (inference).
5. **Even on managed machines, pinning has holes.** "claude setup-token and /install-github-app : enforce only forceLoginMethod , so they can mint a token in a different organization" [claude-iam]. *Caveat:* vendor documentation.
6. **The advice is to reduce the risk, and hiring follows security.** "The use of shadow AI is unlikely to disappear completely." [ncsc-shadow]. About 19 of 31 control duties in our postings sit in security roles. *Caveat:* the NCSC text is a blog post; postings show hiring plans, not practice.

## Proposed figure

Columns: (1) company device; (2) personal device, work identity; (3) personal device, personal account.

| Layer | (1) | (2) | (3) | Evidence |
|---|---|---|---|---|
| Device (MDM, endpoint DLP, managed settings) | Yes | No | No | edlp-ai "Once devices are onboarded"; claude-managed |
| Browser (managed profile or extension) | Yes | Only if managed | No | purview-dspm "prerequisite"; layerx |
| Identity (SSO, tenant restrictions, capture) | Yes | Partial: capture reaches any account on the domain | No | entra-tr; claude-claim |
| Network (SWG, inline CASB) | Yes, on-network or with the client | No | No | gsa-ai "client-based"; zt-ai099 |
| Company apps (API CASB, MCP portal, conditional access) | Yes | Yes | Only if the agent uses company credentials | cf-secure "without having to install the Cloudflare device client"; cf-mcp; Cencora posting "managed and unmanaged endpoints" |
| Policy, training, law | Yes | Yes | Yes, but not technical | ncsc-shadow; ec-ai-lit; cnil-deploy |

Hatch the inferred cells (every "No" in columns 2 and 3, and company apps in column 3). No stored page states them.
