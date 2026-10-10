# Who owns the rules? How new roles emerge, and the question protocol thinking has to ask

Research draft, v3 (after review rounds 1–2) · 10 October 2026 · Protocols for Business · for review before any post

> **Status.** Working notes, not for publication. Sources were found through web search on 10 October
> 2026, but this environment could not open the pages themselves. Facts marked **(S)** come from
> search-result summaries of the named page; facts marked **(M)** are from memory. Open each source before
> quoting it. No archived job posting has been retrieved yet (see section 10).

## 1. The problem

Companies putting agents to work are already hiring for it. "AI engineer" topped LinkedIn's 2026 list of
fastest-growing US job titles, with postings up 143% in 2025 (S).[^linkedin] Forward-deployed engineer
postings rose about 800% between January and September 2025 by one Indeed and *Financial Times* count
(S).[^fde] US federal agencies have had to name a Chief AI Officer since 2024 (S).[^caio] Analysts
recommend a named owner for every agent (S).[^forrester]

None of these roles owns the rules agents act under: who may approve, spend, see and release what, and
how those rules change. The group's job template, now the [Business Protocol Lead](../../blyg-src/threads/job-protocol-operations-lead.md),
bets that someone should. This note asks whether history supports that bet, and what question a business
would have to ask for such a role to exist.

The method: trace eight roles from their predecessors through their origin to their successors, name the
business question that made employers hire at each stage, and see which roles lasted, which split, and
which were absorbed into other roles.

## 2. Eight lineages

Each table runs from the work's earlier home to its later ones. The question is the one an executive
would have asked at that stage, as we reconstruct it.

### 2.1 Product management: from brand man to product ops

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | to 1931 | Advertising, sales and manufacturing each held a piece of every brand | — | (S)[^mcelroy] |
| Origin | 1931 | Brand man, P&G | Our own Camay is losing to our own Ivory. Who answers for one brand's results? | McElroy memo, 13 May 1931 (S)[^mcelroy] |
| Branch | 1940s–80s | Product manager in technology (HP; Intuit, founded 1983 by ex-P&G brand manager Scott Cook) | Engineers build what interests them. Who makes sure we build what customers will pay for? | Secondary only; HP date vague (S, M)[^pmhistory] |
| Branch | late 1980s | Program manager, Microsoft (Excel for Mac) | Developers are shipping features nobody can use. Who owns the spec and the trade-offs? | Credited to Jabe Blumenthal; Spolsky says Charles Simonyi used the title earlier (S)[^programmanager] |
| Successor | 2013–2020s | Product operations | Every product team buys its own tools and measures differently. Who answers for the cost and for numbers we can compare? | Vendor growth figures only (S)[^productops] |

- **The first job description.** McElroy's memo is effectively one. Secondary accounts list the duties:
  study the brand's market and competitors, track sales, manage product, advertising and promotion, test
  in the field and talk to customers, and keep the brand profitable, with each man carrying no more than
  two brands (S).[^mcelroy] Its length is disputed (800 words, or three pages). The memo itself, in P&G's
  archives, has not been seen.
- **Outcome.** Lasted, and keeps branching. Each branch answers the same question (who owns the result
  across functions?) in a new medium.

### 2.2 Planning and analysis: from planning programmers to FP&A, analytics engineering and RevOps

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | 1970s | Mainframe corporate planning models run by specialist programmers; budget clerks | Each run costs days, so we test one scenario. Who answers when the untested one happens? | IFPS, late 1970s; about 2,000 firms using or testing planning models by 1976 (S)[^planningmodels] |
| Origin | 1979–85 | The spreadsheet analyst (VisiCalc 1979, Lotus 1-2-3 1983, Excel 1985) | What happens to the plan if one assumption changes? (No "who": no new title followed.) | Bricklin's blackboard story (S)[^visicalc]; product dates (M) |
| Successor | 1980s–2000s | Financial planning and analysis (FP&A) | Each unit defends its own forecast. Who owns the one plan we commit to? | (S)[^fpa] |
| Branch | 2018–19 | Analytics engineer | Our analysts can't trust the numbers they model. Who builds and tests the data underneath? | Term circulating in the dbt community in 2018; first formal write-up early 2019 (S)[^analyticseng] |
| Branch | 2018– | Revenue operations (from sales operations) | Marketing, sales and customer success each report their own numbers. Who owns the funnel between them? | Earliest known use of "Revenue Operations" in 2018 (S)[^revops]. The common "Xerox in the 1970s" origin rests on one unreliable vendor blog. |

- **Outcome.** The spreadsheet created no new title at first. It moved work: bookkeeping and accounting
  clerk jobs fell after 1980 while accountant jobs grew, as NPR's *Planet Money* reported in 2015 (S; the
  often-quoted 400,000 and 600,000 figures are unconfirmed).[^planetmoney] New titles came forty years
  later, when the data under the models and the conflicts between revenue teams needed owners.

### 2.3 The web: from sysadmin to webmaster to its successors

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | to 1993 | Unix system administrators | — | (S)[^webmasterhist] |
| Origin | 1993–96 | Webmaster | Who is responsible for our website? (Names the technology; the role later split.) | Word first recorded 1993 (S)[^webmaster]. In a 1996 *Web Week* survey, 35% of respondents held the official title, up from none a year earlier (S)[^webmasterhist] |
| Split | late 1990s–2000s | Front-end and back-end developer, operations, SEO specialist, content manager, later UX | Our site is now our storefront. Who answers for search traffic, versus outages, versus off-brand content? | (S)[^webmaster] |
| Fade | 2015–2020 | — | — | Google renamed Webmaster Tools to Search Console (2015, M) and Webmaster Central to Search Central (2020, S)[^webmasterhist] |

- **The job description.** A 1998 webmaster's typical duties: server administration, hand-coded HTML,
  basic graphic design, writing content, and submitting the site to search engines such as AltaVista and
  Yahoo! (S).[^webmaster] RFC 2142 (1997) recorded `webmaster@` as an existing de facto mailbox convention
  (S).[^rfc2142]
- **Outcome.** Split. The work grew; the single owner didn't survive it.

### 2.4 Security: from EDP auditor to CISO to named, disclosed owner

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | 1970s–80s | EDP auditor; bank "data security officer"; security manager under the CIO | Our auditors keep finding the same control gaps. Who fixes them? | ISACA retrospective by a former bank data security officer (S)[^isaca] |
| Origin | 1994 or 1995 | Chief Information Security Officer, Citicorp (Steve Katz) | We lost $10 million to a hacker. Who is accountable to the board? | Levin theft; board told the CEO to hire a security executive (S)[^katz] |
| Spread | 2000s–2010s | CISO, mostly reporting to the CIO at first | — | About half of the Fortune 1000 by 2010 (S, vendor figures)[^cisoshare] |
| Successor | 2023– | A named, disclosed owner of cyber risk | The board must now state who manages cyber risk. Whose name and qualifications go in the 10-K? | SEC Regulation S-K Item 106, adopted 26 July 2023; 62% of first-year filers named a CISO-type role (S)[^item106] |
| Branch | 2015– | Chief trust officer | Customers' security reviews are stalling deals. Who owns trust as a sales asset? | Forrester, 2022 (S)[^trust] |

- **Personal liability.** In October 2023 the SEC sued SolarWinds and its CISO personally; most of the case
  was dismissed in July 2024 and the SEC dropped the rest in November 2025 (S).[^solarwinds]
- **Outcome.** Lasted and climbed. Regulation now requires companies to name the owner.

### 2.5 Operations: from sysadmin to SRE and DevOps to platform engineering

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | to 2003 | System administrators | Ops headcount grows in step with traffic. Can we afford that? | SRE book, "The Sysadmin Approach to Service Management" (S)[^sre] |
| Origin | 2003 | Site reliability engineer, Google | Outages follow releases, and no one owns reliability. Who answers for it while we keep shipping? | Treynor Sloss: "SRE is what happens when you ask a software engineer to design an operations team"; ops work capped at 50% (S)[^sre] |
| Origin | 2008–09 | DevOps (practice, then title) | Developers are paid to change things, operations to keep them stable. How do we stop the two fighting? | Shafer's "Agile Infrastructure" session, Toronto, August 2008; "10+ Deploys per Day", Velocity 2009; first devopsdays, Ghent, 2009 (S)[^devops] |
| Pushback | 2012 | — | — | Humble: "there is no such thing as a devops team" (S)[^humble] |
| Successor | 2019–22 | Platform engineer | Every team rebuilds its own pipeline. Who cuts the duplicated cost and cognitive load? | *Team Topologies* (2019); Gartner Hype Cycle 2022 (S)[^platform] |

- **Outcome.** SRE lasted as a role with an explicit contract (error budgets, the 50% cap). DevOps became
  both a practice and a title, against its founders' advice. Platform engineering builds on DevOps rather
  than replacing it.

### 2.6 Public voice: from community manager to social media manager to social care

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | 1980s–2000s | Bulletin-board sysops; online community managers (AOL, The WELL from 1991, games); PR; customer service | — | (S)[^community] |
| Origin | 2007–08 | Social customer service at Comcast (Frank Eliason) | Customers complain in public faster than our call centre can respond. Who answers? | Informal from September 2007, official February 2008; 11 staff by 2009 (S)[^comcast] |
| Origin | 2008 | Head of social media, Ford (Scott Monty) | Bloggers and customers shape our brand before PR can respond. Who speaks for the company in public, in real time? | Hired July 2008; formal title "Global Digital & Multimedia Communications Manager" (S)[^ford] |
| Spread | 2010s | Social media manager; social care teams | — | About 64,000 US social media managers in 2022, by Revelio Labs' own count (S)[^revelio] |

- **Outcome.** Lasted and multiplied. The first holders did the work under existing titles.

### 2.7 Data: from statistician to data scientist to ML and AI engineer

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | 1989–2000s | Statistician; business intelligence analyst | Our warehouse reports what happened. Who can tell us why? | Jeff Wu proposed renaming statisticians "data scientists" in 1997; "business intelligence" popularised from 1989, origin disputed (S)[^datahist] |
| Origin | 2008 | Data scientist (LinkedIn, Facebook) | Our product produces data no team can analyse, and growth decisions are made blind. Who answers for what the data says? | Patil and Hammerbacher; Hammerbacher's 2009 chapter in *Beautiful Data* says "research scientist" didn't fit (S)[^datascience] |
| Recognition | 2012, 2018 | — | — | HBR, October 2012[^hbr]; US occupational code 15-2051 in 2018 (S)[^soc] |
| Successor | mid-2010s | Machine learning engineer; MLOps (about 2020) | Our models never leave the notebook. Who gets them into production? | (S)[^mle] |
| Successor | 2023 | AI engineer | Who builds products on top of models? | swyx's essay "The Rise of the AI Engineer" (2023; month M) (S)[^aieng] |

- **Outcome.** Lasted, then branched toward production and products.

### 2.8 Model work: from prompt engineer to context engineering and AI engineering

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Origin | December 2022 | Staff prompt engineer, Scale AI (Riley Goodside) | How do we get reliable work out of these models? (Names the technology, no "who"; the role was absorbed.) | Alexandr Wang called him the first person hired with the title (S)[^goodside] |
| Peak | 2023 | Prompt engineer | — | Anthropic's posting at $175,000–$335,000: the field "is arguably less than two years old" (S)[^anthropic] |
| Absorbed | 2025 | — | — | WSJ, April 2025: "suddenly obsolete"; Indeed postings flat at about 3,000 (S)[^wsj] |
| Successor | June 2025 | Context engineering (practice) | Our agents fail because they lack the right information at each step. Who designs what they see? | Tobi Lütke's preference for the term, endorsed by Andrej Karpathy (S)[^context] |
| Successor | 2023– | AI engineer; AI trainer | — | (S)[^aieng] |

- **Outcome.** Absorbed within about two years. The skill became general literacy; the harder work moved
  to AI engineers and to context design.

## 3. Roles forming now

| Role | Since | The business question | Status |
| --- | --- | --- | --- |
| Forward-deployed engineer | Palantir, about 2011; surge 2025 | How do we get our AI working inside each customer's operations? | Growing fast (S)[^fde] |
| AI engineer | 2023 | Who builds products on models? | #1 fastest-growing US title, 2026 (S)[^linkedin] |
| Chief AI Officer | US federal agencies, 2024 | Who coordinates AI use and manages its risk? | Kept by M-25-21 (April 2025) as a "change agent and AI advocate", which is transition language. IBM reports 76% of surveyed organisations had one in 2026, up from 26% in 2025 (S)[^caio][^ibm] |
| GRC engineer | about 2024 | Our compliance evidence is collected by hand once a year. Who turns controls into code? | A manifesto and vendor career guides; sources disagree on whether it's a title or a capability (S)[^grc] |
| Named agent owner | 2025–26 | Who manages each agent's lifecycle? | Analyst recommendation, not a title (S)[^forrester] |
| Agent supervisor | 2026 | Who oversees agents doing work people used to do? | Gartner expects infrastructure staff to shift to supervising agents (S)[^gartner] |

All but one of these questions name the technology. By the pattern in section 6, that marks them as
transition roles or skills in the making. Only the GRC engineer's question names a recurring cost.

## 4. Timeline

| Year | Event | Lineage |
| --- | --- | --- |
| 1931 | McElroy's "brand man" memo at P&G | Product |
| 1976 | About 2,000 firms using corporate planning models | Planning |
| 1979 | VisiCalc ships | Planning |
| late 1980s | Program manager role at Microsoft | Product |
| 1993 | "Webmaster" first recorded | Web |
| 1994/95 | Steve Katz becomes the first CISO, at Citicorp | Security |
| 1996 | 35% of *Web Week* respondents hold the title webmaster | Web |
| 1997 | RFC 2142 records `webmaster@`; Wu proposes "data scientist" for statisticians | Web, Data |
| 2003 | Treynor Sloss starts SRE at Google | Operations |
| 2007–08 | Comcast's social care; Ford's head of social media | Public voice |
| 2008 | Patil and Hammerbacher name the data scientist; "Agile Infrastructure" in Toronto | Data, Operations |
| 2009 | "10+ Deploys per Day"; first devopsdays | Operations |
| 2011 | Palantir's forward-deployed engineers | Agents |
| 2012 | Humble: "no such thing as a devops team"; HBR on data scientists | Operations, Data |
| 2018 | "Data Scientists" enters the US occupational classification; "revenue operations" and "analytics engineer" appear | Data, Planning |
| 2019 | *Team Topologies* defines platform teams | Operations |
| 2020 | Google renames Webmaster Central | Web |
| Dec 2022 | First staff prompt engineer, at Scale AI | Model work |
| 2023 | SEC Item 106 requires a named owner of cyber risk; Anthropic's prompt engineer posting; "AI engineer" | Security, Model work |
| 2024 | US agencies required to name Chief AI Officers | Agents |
| 2025 | Prompt engineering "obsolete"; context engineering named; FDE postings up about 800% | Model work, Agents |
| 2026 | AI engineer tops LinkedIn's fastest-growing titles | Agents |
| Dec 2027 | EU AI Act deployer obligations for high-risk systems apply, including human oversight by people with the necessary competence, training and authority (S)[^aiact] | Agents |

## 5. Roles that didn't last

The eight lineages above are documented because they mostly succeeded. These are the counter-cases.

| Role | Years | The business question | What happened |
| --- | --- | --- | --- |
| Chief Knowledge Officer | mid-1990s–2000s | Our expertise walks out of the door. Who owns our intellectual capital? | Never common: about 50 worldwide around 2000. Duties went to CIOs and chief learning officers (S)[^cko] |
| Y2K program office | 1997–2000 | A dated failure could stop operations. Who answers to the board and regulators by 31 December 1999? | Disbanded on schedule; the President's Council closed in spring 2000 (S)[^y2k] |
| E-business director | 1999–2002 | Online sales compete with our stores and catalogues. Who owns the online channel? | Handed to CIOs, then to marketing and commerce (S)[^ebiz] |
| Chief Digital Officer | 2012–2022 | Digital entrants are taking our customers. Who leads the transformation? | Share of the 2,500 largest listed companies with one rose from 6% (2014) to 21% (2018), while new appointments fell from 160 (2016) to 54 (2018). Strategy& expected the role to disappear (S)[^cdo] |
| Chief Diversity Officer | surge 2020–21; cuts 2022–25 | We face public, employee and legal pressure on equity. Who answers? | The only C-suite role with falling hires in 2022; many renamed or folded in 2025 (S)[^cdio] |
| Growth hacker | 2010–about 2018 | We have no marketing budget. Who finds growth through product and data? | Became growth marketing and product growth teams (S)[^growth] |
| Metaverse lead | 2022–23 | Who leads our metaverse strategy? | Disney opened its division in February 2022 and closed it in March 2023 (S)[^metaverse] |

What the counter-cases show:

- **A senior sponsor creates a role; it doesn't keep it.** Every failure except the growth hacker and the
  metaverse lead had one. Y2K had the strongest board and regulator pressure of any case, and ended anyway.
- **Transition roles end when the transition does.** Y2K, e-business and the Chief Digital Officer were
  hired to change the organisation, and their success made them redundant. The CISO, SRE, the brand
  manager and the controller are hired to hold a balance indefinitely.
- **In 2016, "digital against legacy" looked as permanent as "development against operations".** The
  e-business director and the CDO met the conditions as they looked at the time. A test has to work
  before the fact.
- **A role can lose its question.** The Chief Diversity Officer faded when the outside pressure that
  created it reversed.

## 6. What makes a role emerge, and what makes it last

| Lineage | New capability | The gap between functions | What happened to the role |
| --- | --- | --- | --- |
| Product | Mass advertising | Advertising, sales, production | Lasted; keeps branching |
| Planning | Spreadsheet | None at first | No new title for decades; work moved to existing roles |
| Web | The web | Small at first | Split into specialties |
| Security | Networked banking | Large, made visible by a loss | Lasted, climbed, now legally named |
| Operations | Web-scale software | Development against operations | SRE lasted; DevOps became practice and title; platform teams followed |
| Public voice | Social platforms | PR, marketing, customer service | Lasted, multiplied |
| Data | Cheap storage and compute | Engineering against analysis | Lasted, then branched |
| Model work | Large language models | Small | Absorbed into AI engineering and context design |

**Why roles emerge.** Usually a capability makes a new kind of work cheap (though Y2K and the Chief
Diversity Officer show it isn't necessary), and a cost lands between existing functions until someone
senior asks who answers for it.

**Why roles last.** Two further conditions, each testable before the fact:

1. **The conflict comes from a permanent trade-off in the business model, not from a migration.** Speed
   against stability, revenue against risk, one brand against another: these never end. Old channel
   against new, legacy against digital, pre-2000 dates against post-2000: these end when the migration
   completes. The test: *would this conflict still exist if the transition finished tomorrow?*
2. **Something outside the role keeps renewing the question.** A recurring, countable cost or a number the
   role controls (an error budget, fraud losses, a brand's profit), a regulator or auditor, or customers who
   demand it. Roles held up only by a sponsor (the Chief Knowledge Officer, the Chief Digital Officer)
   fade when the sponsor moves on.

When the work is a skill rather than a conflict (HTML, prompting, growth tactics), it moves into many
existing roles, as the webmaster's and the prompt engineer's work did. The work doesn't disappear; the
single owner does.

Three further patterns:

- **Questions that name the technology predict short-lived roles.** Webmaster, prompt engineer, Chief
  Digital Officer, metaverse lead: each question named the technology, and each role split, was absorbed
  or faded. The data scientist is the exception, and its question can be restated as a cost (growth
  decisions made blind). Questions that name a cost or a conflict (Camay against Ivory, a $10 million
  theft, outages after releases) produced the roles that lasted.
- **The title trails the work by years.** Eliason and Monty did the work under other titles; Facebook's
  data scientists were first hired as analysts and research scientists; official classification took ten
  years.
- **Regulation is the strongest renewer.** Sarbanes-Oxley section 404 (2002) made internal controls an
  audited duty; SEC Item 106 (2023) made companies name who manages cyber risk; the EU AI Act will require
  named, competent human oversight of high-risk AI from December 2027.

## 7. The case that it's all engineering

The strongest version of the challenge:

- **Protocols in this sense are code.** Permissions, spending limits, approval workflows and output checks
  are built by engineers. SRE is the precedent: an operations problem solved by hiring software engineers.
  GRC engineering and platform engineering show the same move in compliance and infrastructure.
- **The most recent analogue was absorbed in two years.** Prompt engineering went from a $335,000 posting
  to "obsolete". Protocol thinking may become a skill every engineer and manager learns.
- **Engineering is absorbing risk work.** Gartner predicts that by 2028 half of content risk roles will
  move from legal and cybersecurity into AI engineering (S).[^gartner] AI engineer is the fastest-growing
  title.
- **The DevOps founders warned against exactly this.** Humble's objection to a "devops team" applies to a
  "protocol team": a layer between those who set rules and those who build them.

Where the challenge is weaker:

- **Engineering builds rules but doesn't decide them.** Which discount limit, whose approval, what data may
  leave: these trade revenue against risk. Engineering didn't settle development against operations either,
  until SRE's error budget turned the conflict into a number.
- **Security is engineered too, and the CISO still exists.** Since 2023 US listed companies must name who
  owns cyber risk. A function built in code can still need an accountable owner.
- **New roles are already forming around agents.** Forward-deployed engineers, Chief AI Officers and named
  agent owners exist because someone must answer for agents in the business. The open question is whether
  rule ownership becomes one of them, or a duty inside one.

**The incumbent.** A steady-state owner of business rules already exists: the controller and the internal
controls function, audited under Sarbanes-Oxley in listed companies. It owns rules about money and
reporting, mostly tested once a year. GRC engineering is turning those controls into code.

**Verdict, moderate confidence.** A standalone "protocol" role is less likely than the duties landing in
an existing or forming role: internal controls and GRC engineering, revenue operations, a Chief AI
Officer's office, or platform engineering. A distinct role is likely only where agents are slowed or
exposed by rules no one owns, at a cost that recurs and can be counted.

## 8. Applying the pattern to protocols

| Candidate gap | Permanent trade-off? | What renews it | Who might absorb it | Likely outcome |
| --- | --- | --- | --- | --- |
| What each agent may see, do and spend | Yes: access against safety | Security incidents, audits | Security, identity and access management | Absorbed into security |
| Day-to-day oversight of agents in each team | No: a skill that spreads | Nothing outside the team | Every manager | Becomes a skill, as prompting did |
| "Get our agents deployed" | No: a migration | A sponsor | Chief AI Officer, forward-deployed engineers | Transition role; ends when deployment is routine |
| Which business rules become enforced in systems, and how they change as the business grows | Yes: revenue against risk, speed against control | Deals waiting on approvals, incidents traced to rules, and from December 2027 EU oversight duties | Nobody today: security, finance, legal, sales and engineering each hold a piece | Candidate for a role, or a mandate for internal controls, RevOps or platform engineering |

Only the fourth gap passes both tests for lasting. It also tells us how a protocol role would have to be
framed: as refereeing revenue against risk with a number it controls (approval wait times, exception
rates, incidents traced to rules), not as "getting agents deployed". The second framing is a transition
role.

## 9. The question a business needs to ask today

Each lasting role began with a question that named a cost and asked who answers for it, and something kept
asking it. The equivalent for protocols, without naming the technology:

> **Our growth waits on rules nobody owns: approvals, limits and data permissions. Who answers for what
> each rule costs us, in deals delayed and in damage done, and who may change it?**

How the answer points to a structure:

- **"The CTO" or "engineering"** → no new role; protocol thinking becomes an engineering skill.
- **"The CISO"** → security absorbs it, and the rules lean toward restriction.
- **"The controller"** → internal controls absorbs it, and the rules lean toward audit.
- **"The COO", or each function separately** → the gap is real. If its cost recurs and can be counted,
  expect a role, under whatever title the company already uses.

Agents make the question urgent, because they hit unowned rules faster and more often than people do. They
are the reason to ask now, not the subject of the question.

## 10. Gaps and next research steps

- **Archived job postings.** None retrieved. Try the Wayback Machine for early career pages (Google SRE,
  LinkedIn and Facebook data teams, Ford), the `misc.jobs.offered` Usenet archive for 1990s webmaster
  postings, newspaper classifieds, P&G's archives for the McElroy memo, and Hammerbacher's 2009 chapter.
- **Posting counts over time.** Indeed Hiring Lab, LinkedIn Economic Graph or Lightcast for "DevOps
  engineer" (2010–15), "prompt engineer" (2022–25), and any "agent operations" or "AI controls" titles now.
- **Regulation.** Confirm the EU AI Act's post-Omnibus dates and the exact Article 26(2) wording.
- **Counter-evidence.** Companies that tried a dedicated "AI governance" or "agent operations" team and
  folded it back into engineering.

## 11. Assumptions to pressure-test

- [ ] **Survivorship.** Section 5 adds seven counter-cases, but failed roles still leave fewer traces than
  successful ones.
- [ ] **Reconstructed questions.** Each business question is our reading. McElroy's memo asked for staff.
- [ ] **Vendor numbers.** CISO coverage, FDE growth, product-ops growth and LinkedIn rankings come from
  industry sources with their own methods and interests.
- [ ] **New titles versus new occupations.** Autor and colleagues estimate about 60% of 2018 US employment
  was in titles that did not exist in 1940; a 2026 replication counting people rather than titles finds
  about 9% (S).[^autor]
- [ ] **US-centric.** All eight lineages are American or US-reported.

## Notes

(S) from a search-result summary of the named page, not opened. (M) from memory.

[^mcelroy]: Neil H. McElroy, memorandum to Procter & Gamble management, 13 May 1931, as described in Ken Norton, "Product Management Was Born in 1931 (Maybe, Sort Of)," *Bring the Donuts*, https://www.bringthedonuts.com/essays/product-management-mcelroy-memo-turns-ninety/; and "Brand Men & the History of Product Management," *Productside*, https://productside.com/brand-men-the-history-of-product-management/. (S)
[^pmhistory]: "History of Product Management," *Product Manager Academy*, https://productmanageracademy.substack.com/p/114-history-of-product-management; "The History and Evolution of Product Management," *Miles Education*, https://mileseducation.com/blog/accounting/the-history-and-evolution-of-product-management. (S)
[^programmanager]: Scott Berkun, *The Art of Project Management* (O'Reilly, 2005), ch. 1, https://www.oreilly.com/library/view/the-art-of/0596007868/0596007868_artprojectmgmt-CHP-1-SECT-4.html; Joel Spolsky, "How to Be a Program Manager," *Joel on Software*, 9 March 2009, https://www.joelonsoftware.com/2009/03/09/how-to-be-a-program-manager/. (S)
[^productops]: "Lessons from Over 5 Years in Product Ops," *Product-Led Alliance*, https://www.productledalliance.com/lessons-from-over-5-years-in-product-ops/. (S, vendor figures)
[^planningmodels]: Thomas H. Naylor and Daniel R. Gattis, "Corporate Planning Models," *California Management Review* 18, no. 4 (1976), https://cmr.berkeley.edu/1976/08/18-4-corporate-planning-models/; "IFPS," *Wikipedia*, https://en.wikipedia.org/wiki/IFPS. (S)
[^visicalc]: "VisiCalc," *Wikipedia*, https://en.wikipedia.org/wiki/VisiCalc; "How VisiCalc's Spreadsheets Changed the World," *The New Stack*, https://thenewstack.io/how-visicalcs-spreadsheets-changed-the-world/. (S)
[^fpa]: "FP&A," *Wikipedia*, https://en.wikipedia.org/wiki/FP%26A. (S)
[^analyticseng]: "Emerging Data Roles: The Analytics Engineer," *Data Council*, https://www.datacouncil.ai/blog/emerging-data-roles-the-analytics-engineer. (S)
[^revops]: "Revenue Operations," *EverybodyWiki*, https://en.everybodywiki.com/Revenue_Operations; on the Xerox claim, "The Evolution to Revenue Operations," *Traction Complete*, https://tractioncomplete.com/articles/the-evolution-to-revenue-operations. (S)
[^planetmoney]: "Episode 606: Spreadsheets!," *Planet Money*, NPR, February 2015, transcript at https://www.npr.org/transcripts/389027988; "How the Electronic Spreadsheet Revolutionized Business," NPR, 27 February 2015, https://www.npr.org/2015/02/27/389585340/how-the-electronic-spreadsheet-revolutionized-business. (S)
[^webmaster]: "Webmaster," *Wikipedia*, https://en.wikipedia.org/wiki/Webmaster; "What Happened to the Webmaster," *The History of the Web*, https://thehistoryoftheweb.com/postscript/what-happened-to-the-webmaster/. (S)
[^webmasterhist]: "Job Profile: Webmaster," *Certification Magazine*, https://certmag.com/articles/job-profile-job-webmaster-constantly-evolved-since-1990s; "Webmaster," *Mewayz Wiki*, https://wiki.mewayz.com/wiki/Webmaster. (S)
[^rfc2142]: D. Crocker, "Mailbox Names for Common Services, Roles and Functions," RFC 2142, May 1997, https://www.rfc-editor.org/info/rfc2142. (S)
[^isaca]: "Information Security Matters: Fifty Years of Information Security—A Recollection," *ISACA Journal* 1 (2019), https://www.isaca.org/resources/isaca-journal/issues/2019/volume-1/information-security-matters-fifty-years-of-information-securitya-recollection. (S)
[^katz]: "CISO Conversations: Steve Katz, the World's First CISO," *SecurityWeek*, https://www.securityweek.com/ciso-conversations-steve-katz-worlds-first-ciso/; "The Past, Present and Future of Chief Information Security Officers," *Cybersecurity Ventures*, https://cybersecurityventures.com/the-past-present-and-future-of-chief-information-security-officers-cisos/. (S)
[^cisoshare]: "38% of the Fortune 500 Do Not Have a CISO," *Help Net Security*, 1 October 2019, https://www.helpnetsecurity.com/2019/10/01/fortune-500-ciso/; "C-Suite Shuffle: The CISO's Evolving Role and Reporting Structure," *CSO*, https://www.csoonline.com/article/572253/c-suite-shuffle-the-ciso-s-evolving-role-and-reporting-structure.html. (S)
[^item106]: DLA Piper, "Updates to Form 10-K for Fiscal Year 2023," February 2024, https://www.dlapiper.com/insights/publications/2024/02/updates-to-form-10-k-for-fiscal-year-2023. (S)
[^trust]: "The Rise of the Chief Trust Officer: Where Does the CISO Fit?," *CSO*, https://www.csoonline.com/article/4085479/the-rise-of-the-chief-trust-officer-where-does-the-ciso-fit.html. (S)
[^solarwinds]: "SolarWinds Dismissed: What the SEC's U-Turn Signals for Cyber Enforcement," *Harvard Law School Forum on Corporate Governance*, 7 December 2025, https://corpgov.law.harvard.edu/2025/12/07/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement/. (S)
[^sre]: Benjamin Treynor Sloss, "Introduction," in *Site Reliability Engineering: How Google Runs Production Systems*, ed. Betsy Beyer et al. (O'Reilly, 2016), https://sre.google/sre-book/introduction/. (S)
[^devops]: "The Origins of DevOps: What's in a Name?," *DevOps.com*, https://devops.com/the-origins-of-devops-whats-in-a-name/; "The Incredible True Story of How DevOps Got Its Name," *New Relic*, https://blog.newrelic.com/engineering/devops-name/. (S)
[^humble]: Jez Humble, "There's No Such Thing as a 'Devops Team'," *Continuous Delivery*, October 2012, https://continuousdelivery.com/2012/10/theres-no-such-thing-as-a-devops-team/. (S)
[^platform]: "How Team Topologies Supports Platform Engineering," *The New Stack*, https://thenewstack.io/how-team-topologies-supports-platform-engineering/; "SRE vs DevOps vs Platform Engineering," *Humanitec*, https://humanitec.com/blog/sre-vs-devops-vs-platform-engineering. (S)
[^community]: "Online Community Manager," *Wikipedia*, https://en.wikipedia.org/wiki/Online_community_manager; "The WELL," *Wikipedia*, https://en.wikipedia.org/wiki/The_WELL. (S)
[^comcast]: "Comcast: Twitter Has Changed the Culture of Our Company," *TechCrunch*, 20 October 2009, https://techcrunch.com/2009/10/20/comcast-twitter-has-changed-the-culture-of-our-company; "Frank Eliason," *Technical.ly*, https://technical.ly/startups/frank-eliason-comcast/. (S)
[^ford]: "Ford's Big Twitter," *Campaign*, https://www.campaignlive.co.uk/article/ford-s-big-twitter/4xy465k56zzvwwat1zxsp6mgnv; Neville Hobson, "FIR Interview: Scott Monty, Head of Social Media, Ford Motor Company," 12 December 2008, https://nevillehobson.com/2008/12/12/fir-interview-scott-monty-head-of-social-media-ford-motor-company/. (S)
[^revelio]: Revelio Labs, "How Social Media Manager Went from Intern-Tier to Full-On Career," https://www.reveliolabs.com/news/social/how-social-media-manager-went-from-inter-tier-to-full-on-career/. (S)
[^datahist]: "50 Years of Data Science" survey literature, https://arxiv.org/pdf/2007.03606; "Disputed History of the Term Business Intelligence," *Software Memories*, 2 December 2007, https://www.softwarememories.com/2007/12/02/disputed-history-of-the-term-business-intelligence. (S)
[^datascience]: Jeff Hammerbacher, "Information Platforms and the Rise of the Data Scientist," in *Beautiful Data*, ed. Toby Segaran and Jeff Hammerbacher (O'Reilly, 2009), as summarized at https://arxiv.org/pdf/2311.03292; "Jeff Hammerbacher," *Wikipedia*, https://en.wikipedia.org/wiki/Jeff_Hammerbacher. (S)
[^hbr]: Thomas H. Davenport and D. J. Patil, "Data Scientist: The Sexiest Job of the 21st Century," *Harvard Business Review*, October 2012. (S)
[^soc]: U.S. Bureau of Labor Statistics, "Employment and Wages for Newly Defined Occupations, May 2021," *The Economics Daily*, 2022, https://www.bls.gov/opub/ted/2022/employment-and-wages-for-newly-defined-occupations-may-2021.htm. (S)
[^mle]: "Where Do Machine Learning Engineers Work?," *Gradient Flow*, https://gradientflow.com/where-do-machine-learning-engineers-work/. (S)
[^aieng]: swyx (Shawn Wang), "The Rise of the AI Engineer," *Latent Space*, 2023, as discussed at https://podcast.scrimba.com/146. (S; month from memory)
[^goodside]: "Riley Goodside," *PromptLayer Glossary*, https://www.promptlayer.com/glossary/riley-goodside; https://news.pedaily.cn/202212/505153.shtml. (S)
[^anthropic]: "Prompt Engineer and Librarian," Anthropic job posting, 2023, as reported in *Fortune*, 9 March 2023, https://www.fortune.com/2023/03/09/new-ai-jobs-chatgpt-like-assistants. (S)
[^wsj]: "The Hottest AI Job of 2023 Is Already Obsolete," *Wall Street Journal*, April 2025, as reported in *Entrepreneur*, https://www.entrepreneur.com/business-news/ai-is-taking-over-for-prompt-engineers/490762. (S)
[^context]: "Shopify CEO and Ex-OpenAI Researcher Agree That Context Engineering Beats Prompt Engineering," *The Decoder*, June 2025, https://the-decoder.com/shopify-ceo-and-ex-openai-researcher-agree-that-context-engineering-beats-prompt-engineering/. (S)
[^fde]: "Forward-Deployed Engineers Emerge as One of AI's Fastest-Growing Jobs," *PYMNTS*, 2026, https://www.pymnts.com/news/artificial-intelligence/2026/forward-deployed-engineers-emerge-as-one-of-ais-fastest-growing-jobs/; Bloomberry, "What I Learned Analyzing 1K Forward Deployed Engineer Jobs," https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/. (S)
[^linkedin]: LinkedIn News, "LinkedIn Jobs on the Rise 2026: The 25 Fastest-Growing Roles in the U.S.," https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-roles-us-linkedin-news-dlb1c. (S)
[^caio]: Office of Management and Budget, Memorandum M-24-10, 28 March 2024, as summarized by Crowell & Moring, https://www.crowell.com/en/insights/client-alerts/omb-releases-final-guidance-memo-on-the-governments-use-of-ai; Memorandum M-25-21, "Accelerating Federal Use of AI through Innovation, Governance, and Public Trust," April 2025, https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf. (S)
[^grc]: "GRC Engineering Manifesto," https://grc.engineering/; Vanta, "The 8 Values of GRC Engineering," https://www.vanta.com/collection/grc/grc-engineering-values. (S)
[^forrester]: Forrester, "The State of Agentic AI in 2026: Companies Are Chasing, Few Are Catching," https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/. (S)
[^gartner]: Gartner, "Gartner Announces Top Predictions for Data and Analytics in 2026," 11 March 2026, https://www.gartner.com/en/newsroom/press-releases/2026-03-11-gartner-announces-top-predictions-for-data-and-analytics-in-2026; Itential, "Gartner Predicts 2026: AI Agents Will Reshape Infrastructure & Ops," https://www.itential.com/resource/analyst-report/gartner-predicts-2026-ai-agents-will-reshape-infrastructure-operations/. (S)
[^aiact]: Regulation (EU) 2024/1689 (AI Act), Article 26, as summarized at https://artificialintelligenceact.eu/article/26/; post-Omnibus application dates as reported by *Data Protection Report*, July 2026, https://www.dataprotectionreport.com/2026/07/the-eu-ai-act-when-does-it-become-enforceable-now/. (S)
[^autor]: David Autor, Caroline Chin, Anna Salomons and Bryan Seegmiller, "New Frontiers: The Origins and Content of New Work, 1940–2018," *Quarterly Journal of Economics* 139, no. 3 (2024), https://economics.mit.edu/sites/default/files/2022-11/ACSS-NewFrontiers-20220814.pdf; the 2026 replication is reported at https://www.nakedcapitalism.com/2026/09/new-jobs-in-140-years-of-data-why-the-ai-displacement-fear-is-overstated-and-what-to-worry-about-instead.html. (S)
[^cko]: "Chief Knowledge Officer," *Wikipedia*, https://en.wikipedia.org/wiki/Chief_knowledge_officer; Michael J. Earl and Ian A. Scott, "What Is a Chief Knowledge Officer?," *Sloan Management Review* 40, no. 2 (1999), https://sloanreview.mit.edu/article/what-is-a-chief-knowledge-officer. (S)
[^y2k]: "President's Y2K Council Disbands," *Nextgov*, April 2000, https://nextgov.com/people/2000/04/presidents-y2k-council-disbands/241668. (S)
[^ebiz]: "Chief Web Officer," *Wikipedia*; "Is Your E-Business Plan Radical Enough?," *MIT Sloan Management Review*, https://sloanreview.mit.edu/?p=2964. (S)
[^cdo]: Strategy&, "2019 Chief Digital Officer Study," https://www.strategyand.pwc.com/gx/en/insights/2019/cdo/2019-cdo-study-global-findings.pdf; "The Disappearing CDO," *TechRepublic*, 2022, https://www.techrepublic.com/article/disappearing-cdo-cio-next/. (S)
[^cdio]: "Diversity Roles Cut in Layoffs," *Fortune*, 22 May 2023, https://fortune.com/2023/05/22/diversity-roles-cut-layoffs. (S)
[^growth]: "Growth Hacking," *Wikipedia*, https://en.wikipedia.org/wiki/Growth_hacking. (S)
[^metaverse]: "Disney's Metaverse Chief Departs Shortly After Division Shutdown," *Campaign Asia*, https://www.campaignasia.com/article/disneys-metaverse-chief-departs-shortly-after-division-shutdown/485682. (S)
[^ibm]: IBM, "IBM Study: CEOs Are Reshaping C-Suite Roles for the AI Era," 4 May 2026, https://newsroom.ibm.com/2026-05-04-ibm-study-ceos-are-reshaping-c-suite-roles-for-the-ai-era. (S; samples may differ between years)
