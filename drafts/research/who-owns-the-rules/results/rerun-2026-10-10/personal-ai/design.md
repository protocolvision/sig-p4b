# Personal AI at work: design (descriptive)

11 October 2026, added at the user's request and written before collection.

## Question

Employees use their own AI subscriptions and run their own agents for work. Company controls can only reach some layers:
- the work device;
- the browser;
- the identity and sign-in;
- the network;
- the enterprise apps the agent touches.

We ask three things:
- how common personal AI use at work is;
- what controls are emerging at each layer;
- how companies are handling it: banning, sanctioning enterprise licences, or monitoring.

## Parts

**A. Published evidence (desk research, official or primary sources only).**
- **Prevalence:** surveys with a stated method, giving sample size, date and question wording. Vendor surveys are labelled as such.
- **Controls, by layer:**
  - device: MDM, managed settings for AI tools;
  - browser: enterprise browsers and extensions;
  - identity: SSO enforcement, tenant restrictions, domain capture of consumer accounts;
  - network and SaaS discovery: secure web gateways and cloud access security brokers with AI app catalogues;
  - data loss prevention for prompts;
  - AI and MCP gateways;
  - vendor enterprise controls: Claude, ChatGPT, Copilot, Gemini.
- **Company approaches:** published AI acceptable-use policies, documented bans or restrictions, and incidents.
- **Regulation and liability:** EU AI Act Art 4 (AI literacy), data protection guidance on staff use of public AI tools, and sector regulator statements.

**B. Our corpus (no new collection).**
Search the following for "shadow AI", "personal", "unapproved", "unsanctioned", "approved tools", "acceptable use", "BYO" and similar, then code each hit:
- the postings' duty statements (`postings-haiku-all.tasks.jsonl`);
- the practitioner speech spans;
- the 2,216 filing passages.

Codes per hit:
- **who:** security, IT, legal, data/AI, business;
- **response:** discover, block, sanction or approve, monitor, train, policy.

Report counts by function and up to eight verbatim examples.

## Rules

- Every claim carries a verbatim quote of 40 words or fewer from a stored page, checked by script.
- Prevalence figures carry sample, date and sponsor.
- No sign-ins.
- A fresh Opus agent reviews A and B before anything enters the report.
