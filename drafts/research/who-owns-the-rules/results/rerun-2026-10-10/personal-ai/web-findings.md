# Personal AI at work: web findings (part A)

Collected 11 October 2026. Every quote below was checked against the stored page text by script (result at the end). Pages are in `corpus/b-raw/personal-ai/web/`. Labels: vendor documentation describes what a product claims to do, not independent testing; vendor surveys are marked; news is marked. Statements marked 'Inference' are ours and carry no quote.

## Prevalence: between roughly half and three-quarters of AI users at work bring their own tools, and a large share use accounts the employer cannot see

| Figure | Sample and method | Date | Sponsor | Quote | Source |
|---|---|---|---|---|---|
| 78% of AI users bring their own AI tools to work | 31,000 knowledge workers, 31 markets, online, fielded by Edelman Data & Intelligence | 15 Feb to 28 Mar 2024 | Microsoft and LinkedIn (vendor-sponsored) | "78% of AI users are bringing their own AI tools to work (BYOAI)" | wti |
| 52% of AI users reluctant to admit using it for important tasks | same | same | Microsoft and LinkedIn (vendor) | "52% of people who use AI at work are reluctant to admit to using it for their most important tasks." | wti |
| Over half of workplace generative AI users lack formal approval (28% of workers use it) | 14,000+ full-time employees, 14 countries, double-anonymous online, YouGov | 18 to 31 Oct 2023 | Salesforce (vendor-sponsored) | "Over a quarter (28%) of workers are currently using generative AI at work, and over half without the formal approval of their employers." | salesforce |
| 47% of generative AI users use personal accounts the company does not oversee (78% a year earlier; approved accounts 25% to 62%) | Netskope cloud-security telemetry (customer base not stated in the news page) | Oct 2024 to Oct 2025, reported 6 Jan 2026 | Netskope (vendor telemetry), as reported by Cybersecurity Dive (news) | "Nearly half (47%) of people using generative AI platforms are doing so through personal accounts that their companies aren’t overseeing" | netskope-cd |
| Nearly 90% of AI logins bypass enterprise oversight: 67% personal accounts, 21.3% corporate accounts without SSO | Telemetry from millions of enterprise browser sessions (exact N not stated) | 2025 report | LayerX (browser-security vendor) | "Nearly 90% of AI logins bypass enterprise oversight either through personal accounts (67%) or corporate accounts not backed by SSO (21.3%)." | layerx |
| 69% of organisations suspect or have evidence staff use prohibited public generative AI | Survey of organisations (cybersecurity leaders); sample size not in the stored page | 2025 survey, published 1 Jul 2025 | Gartner analyst piece, republished by CXOToday (news site) | "69% of organizations suspect or have evidence that employees are using prohibited public generative AI tools." | gartner-cxo |
| Only 16% of organisations block public generative AI by default | same Gartner survey | same | Gartner via CXOToday | "just 16% block public generative AI by default, and only 9% block embedded or custom-built AI." | gartner-cxo |
| 71% of employees reported using AI tools not approved by their employer | Underlying study not named in the page | Cited 7 Sep 2026 | UK NCSC citing an unnamed study (secondary use of a number) | "nearly three-quarters of employees (71%) reported using AI tools that have not been approved by their employer." | ncsc-shadow |

How to read these numbers:

- The figures do not measure the same thing. Microsoft counts AI users who bring their own tools. Salesforce counts users without formal approval. Netskope and LayerX count accounts or logins seen in traffic, which is closer to what a security team can observe. Gartner counts organisations that suspect misuse, not workers.
- The direction over time is not clear. Netskope's telemetry shows personal-account use falling from 78% to 47% in a year, with approved accounts rising, "the percentage of people using personal AI apps (47%) dropped significantly from the prior year, when it was 78%." [netskope-cd] The same report shows switching between personal and enterprise accounts rising.
- Staff hide it. "52% of people who use AI at work are reluctant to admit to using it for their most important tasks." [wti] Self-reported surveys therefore likely undercount.
- Blocking is rare. Gartner says "just 16% block public generative AI by default, and only 9% block embedded or custom-built AI." [gartner-cxo]
- Not retrieved: the primary Netskope report page (404), the Cisco Data Privacy Benchmark page (access denied), the Gartner press release (403). The Microsoft 71% UK figure cited by NCSC has no primary page in this set.

## Controls by layer: controls reach the work device, the corporate network, company-domain identities and the enterprise apps; a personal account on a personal device is outside all of them

### Device (MDM and managed settings)

- Claude Code takes policy from the organisation: "Managed settings : settings your organization deploys, by a managed-settings.json file, an MDM policy, or server-managed settings from the claude.ai console." [claude-managed] Users cannot override it: "Nothing in your own settings files or --settings overrides a managed key" [claude-managed].
- It can pin the tool to the company account: "To require that developers’ claude.ai logins belong to a specific Anthropic organization, set forceLoginMethod and forceLoginOrgUUID in managed settings ." [claude-iam] Limit, in the vendor's own words: "claude setup-token and /install-github-app : enforce only forceLoginMethod , so they can mint a token in a different organization" [claude-iam].
- Cursor offers "MDM policies - Enforce allowed team IDs and extensions on user devices" [cursor-ent].
- Endpoint DLP (Microsoft Purview) covers onboarded machines only: "Endpoint data loss prevention (Endpoint DLP) extends the activity monitoring and protection capabilities of DLP to Windows 10/11, macOS (the three latest released major versions) devices" [edlp-ai]. It can redirect uploads: "If they're using an unallowed browser, the upload activity is blocked and the user is redirected to use Microsoft Edge." [edlp-ai]
- Reach: managed or enrolled devices only. Inference: none of this reaches a personal laptop or phone, where the employee may run any client with any account.

### Browser

- Microsoft Purview DSPM for AI needs an extension for third-party AI sites: "Install Microsoft Purview browser extension" [purview-dspm] then "A prerequisite for third-party AI sites." [purview-dspm]
- Chrome Enterprise Premium lists "Chrome Enterprise Premium's enhanced DLP features, like real-time copy/paste restrictions, data masking to redact sensitive data being typed into LLMs and dynamic watermarking" [chrome-ai-ref] (Google marketing text).
- Reach: managed browser profiles and installed extensions. Inference: a personal account used in a different browser or on another device is not seen. LayerX (vendor) reports the scale of the blind spot: "Over two-thirds of corporate login events are done without SSO." [layerx]
- Not retrieved: Google's April 2024 Chrome Enterprise DLP post (the stored page lost its body), and any vendor page showing a browser tool that tells a personal ChatGPT login from a corporate one. A search summary names Harmonic and Kovrr as claiming this, unverified here.

### Identity (SSO enforcement, tenant restrictions, domain capture)

- Entra tenant restrictions: "With tenant restrictions, organizations can specify the list of tenants that users on their network are permitted to access." [entra-tr] It depends on the corporate network path: "Clients must be forced to use the proxy for all requests to login.microsoftonline.com , login.microsoft.com , and login.windows.net ." [entra-tr] Inference: it governs Microsoft identity sign-ins, so it does not by itself stop a personal Claude or ChatGPT account. It does block Microsoft consumer apps: "The tenant restrictions feature also supports blocking the use of all Microsoft consumer applications (MSA apps) such as OneDrive, Hotmail, and Xbox.com." [entra-tr]
- Claude domain capture (Enterprise plan only): "Domain claiming lets Enterprise admins discover, claim, and migrate existing personal Claude accounts (Free, Pro, and Max) on a verified company domain into their Enterprise workspace." [claude-claim] The policy it sets: "no non-Enterprise accounts can exist on your verified domain." [claude-claim] It needs actively enforced SSO: "Enforce SSO (not just configured—SSO must be actively enforced)." [claude-claim]
- On Team plans the lever is weaker: "Team plans can verify a domain and block new personal accounts from being created, but admins can't claim or migrate existing accounts." [claude-claim]
- Personal accounts survive if the email differs or the user chooses: "Keep both accounts: Your personal account stays active." [claude-move] Inference: capture works on the company email domain; an account registered with a private Gmail address is not on the domain and is not reached.
- GitHub enterprise-managed users are fenced in: "Managed user accounts cannot create public content or collaborate outside your enterprise." [gh-ent-managed] The Copilot policy page stored here covers licensed users only: "When an organization owner assigns a Copilot license to a member of their organization, the availability of features and models is controlled by policies." [copilot-policy] It does not state anything about blocking personal Copilot accounts, so we make no claim on that.
- Not retrieved: OpenAI help pages on domain verification and claiming (403 to automated fetch). A search summary said verification and claiming are separate and claiming is limited to approved use cases; this is unverified here, so no claim is made.

### Network, secure web gateways and SaaS discovery (CASB)

- Microsoft Defender for Cloud Apps (via Microsoft Zero Trust guidance): "Defender for Cloud Apps maintains a catalog of generative AI applications with risk scores based on factors like data handling practices, compliance certifications, and security posture." [zt-ai099] "administrators can review discovered apps, mark them as sanctioned or unsanctioned, and create policies that enforce those decisions" [zt-ai099].
- Entra Internet Access: "Microsoft Entra Internet Access's first Secure Web Gateway (SWG) features include web content filtering based on domain names." [gsa-ai] Source filtering is client-based only: "Source traffic type filtering is available only for client-based Global Secure Access connections." [gsa-ai]
- Palo Alto Networks (vendor docs): "Fine-grained data exfiltration and access control policies let you control the data exposed to GenAI apps while simultaneously allowing you to block access when necessary." [pan-aias]
- Zscaler (vendor marketing): "Access decided per user, per app, per risk. Approve, isolate, or block." [zscaler-ai]
- Cloudflare shows the sanctioned-app limit clearly: "Cloudflare supports API-based cloud access security broker (CASB) integrations with popular AI services like OpenAI (ChatGPT) , Anthropic (Claude) , and Google Gemini ." [cf-secure] These see the company's own tenants: "you can immediately gain visibility into how your employees are using sanctioned AI tools without having to install the Cloudflare device client on every user's machine." [cf-secure]
- Reach: traffic that passes through the company network or a company client, plus API links into company tenants. Inference: a personal device on home broadband or mobile data is off this path; domain-level blocking cannot tell a personal ChatGPT login from a company one on the same domain, which is why vendors add tenant or account checks.

### Data loss prevention for prompts

- Purview can inspect sensitive data sent to AI over the network: "Detect sensitive info shared with AI via network , which uses network data security to detect sensitive info types shared with AI apps in browsers, applications, APIs, add-ins, and more" [purview-dspm]
- Reach: the same as the layer it rides on (device, browser or network). Netskope telemetry reports the result: "a year-over-year doubling in “the number of incidents of users sending sensitive data to AI apps,” with the average company experiencing 223 such incidents per month" [netskope-cd] (vendor, news report).

### AI and MCP gateways

- Claude Code can route through a company gateway or cloud provider: "model traffic and authentication go to your provider or gateway instead of api.anthropic.com , claude.ai , or platform.claude.com" [claude-network].
- Cloudflare MCP portals put agent tool access behind company login: "Cloudflare Access logs the individual requests made using the tools in the portal." [cf-mcp]
- Zscaler markets an AI Gateway: "Adopt agents at full speed. With control. Every agent registered. Every action authorized." [zscaler-ai] (marketing).
- Reach: only agents configured to use the gateway. Inference: an employee's own agent pointed at a personal subscription skips it, though it still has to touch company apps, where the enterprise-app controls apply.

### Vendor enterprise controls

- Cursor: "Privacy Mode User choice Enforce org-wide Enforce org-wide" [cursor-ent] (plan table; individual users choose, Teams and Enterprise can enforce).
- Claude, GitHub and Cursor each have a way to bind the tool to a company org, but each works through managed devices or company-domain identity. ChatGPT and Gemini controls were not retrieved.

## Company approaches: early reaction was bans scoped to company devices and networks; current advice from Gartner and the UK NCSC is to discover, sanction, train and monitor rather than block

- Ban (news, 2023). Samsung: "Samsung Electronics Co. is banning employee use of popular generative AI tools like ChatGPT after discovering staff uploaded sensitive code to the platform" [samsung-bloom]. Scope, per Fox Business citing a Samsung representative: "banned the use of generative artificial intelligence services on company-owned devices as well as internal networks" [samsung-fox]. Inference: the ban's reach matched the layers the company controls.
- Sanction a replacement alongside the ban. Samsung: "While Samsung is creating its own internal AI tools for translation, document summarization and software development, it is also working on ways to block the upload of sensitive company information to external services." [samsung-mobsyrup] (news).
- Wider restrictions (news). Semafor: "Major banks and technology companies have imposed restrictions on their employees’ use of ChatGPT, the artificial intelligence tool, over concerns about confidential data leaks." [semafor] TechCrunch lists "banks like Bank of America, Citi, Deutsche Bank, Goldman Sachs, Wells Fargo , and JPMorgan , as well as Walmart and telecom giant Verizon have also restricted their staff from accessing ChatGPT" [techcrunch-apple]. These were reports of restrictions in 2023, not company-published policies.
- Monitor and offer a licence. Gartner analyst advice: "Effective management of shadow AI also requires the deployment of security controls, such as web-based monitoring, data leakage prevention and emerging AI usage control technologies." [gartner-cxo] And: "offering flexible options like enterprise AI licenses or internal chatbots for scenarios involving sensitive data." [gartner-cxo]
- Train. Salesforce (vendor survey): "nearly 7 in 10 global workers have never completed or received training on how to use generative AI safely and ethically at work." [salesforce]
- Do not rely on bans. UK NCSC, 7 September 2026: "The use of shadow AI is unlikely to disappear completely." [ncsc-shadow] "the goal should be to reduce risk rather than assume it can be eliminated." [ncsc-shadow]
- Not retrieved: adopted acceptable-use policies from named companies. A search returned only templates, which we did not use.

## Regulation: AI literacy duties and data-protection warnings reach the employer, but no stored text says whether an employee's personal account counts as the employer's deployment

- EU AI Act Art 4, Commission Q&A: "Article 4 of the AI Act requires providers and deployers of AI systems to ensure a sufficient level of AI literacy of their staff and other persons dealing with AI systems on their behalf." [ec-ai-lit] No measurement duty: "Article 4 of the AI Act does not entail an obligation to measure the knowledge of AI of employees." [ec-ai-lit]
- Timing and change: "The supervision and enforcement rules apply from 3 August 2026 onwards." [ec-ai-lit] The same page says the Digital Omnibus amended Art 4 in mid-July 2026 and that "no specific – or ‘sufficient’ - level is mandated" [ec-ai-lit]. The same page also gives 2 August 2026 for national authorities starting supervision, so the date is inconsistent inside the source.
- Dutch data protection authority (AP), August 2024, reported by NL Times (news; the AP original was not retrieved): "By entering personal data into AI chatbots, the companies offering the chatbot can gain unauthorized access to that personal data" [nl-ap]. Its advice: "If organizations allow the use of chatbots, they should make it clear to employees what data they can and cannot enter into the bot." [nl-ap] It reported breaches from staff use: "The authority has received several reports of data leaks that occurred because employers shared personal data of, for example, patients or clients with the chatbot." [nl-ap]
- CNIL, 18 July 2024: "Framing Uses : Define a list of authorised and prohibited uses based on the associated risks" [cnil-deploy] and "Training and Raising Awareness : Educate end-users, about both prohibited uses and the risks involved in official uses." [cnil-deploy]
- UK NCSC (security body, not a data regulator), 7 September 2026: "Employees who transfer sensitive or proprietary information to consumer AI services will likely reduce the organisation's visibility and control over that information." [ncsc-shadow]
- Not retrieved: any ICO text on staff use of public AI tools (the ICO page stored earlier was general AI guidance and was dropped), EDPB statements, and any sector regulator statement. Inference: the duties above fall on the employer as data controller or deployer; whether a personal account on a personal device counts as the employer's use is untested in these sources.

## Synthesis: the reachable boundary is the managed device, the company network, the company-domain identity and the company's own app tenants; the main gap is a personal account on a personal device

- Controls work where the company owns something: the laptop (MDM, endpoint DLP, managed settings), the browser profile, the network path, the email domain, and its own tenants in the AI vendors.
- Each vendor control has a stated edge. Claude domain capture needs the company domain and Enterprise plan; Entra tenant restrictions need the corporate proxy; Cloudflare's CASB sees sanctioned tenants; Claude Code login pinning needs managed settings and still has gaps in token paths.
- Telemetry says the problem is shrinking but large: 47% of generative AI users on unmanaged personal accounts (Netskope, vendor), down from 78%. Nearly 90% of AI logins bypass oversight in LayerX's browser data (vendor).
- Blocking is uncommon (16%, Gartner) and the bans documented in 2023 were scoped to company devices and networks, so a ban leaves the personal route open.
- Both Gartner's analyst piece and the NCSC steer toward discovery, enterprise licences, training and coaching, not prohibition.
- Regulators put the duty on the employer (training, clear rules on what data may be entered) without giving employers new technical reach.
- Main gap: a personal subscription on a personal device, with work content copied in by hand or sent from an agent the employee runs. No control in this set sees it; the only levers left are policy, training, a good sanctioned alternative, and controls on the company apps and data that the agent must touch.
- Second gap: coverage differs by vendor and plan (Claude Team versus Enterprise; ChatGPT and Gemini pages not retrieved), so a company cannot assume one policy covers every tool.
- Evidence gap: prevalence numbers come mostly from vendors with products to sell, measure different things, and no independent survey of personal-account use on personal devices was found.

## Quote check

66 of 66 quotes pass the verbatim and 40-word check.
