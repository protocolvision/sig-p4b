# Who owns the rules? How new roles emerge, and the question a business has to ask

Research draft, v6 (five review rounds, plus seniority) · 10 October 2026 · Protocols for Business · for review before any post

> **Status.** Working notes, not for publication. Sources were found through web search on 10 October
> 2026, but this environment could not open the pages themselves. Facts marked **(S)** come from
> search-result summaries of the named page; facts marked **(M)** are from memory. Open each source before
> quoting it. No archived job posting has been retrieved yet (see section 10).
>
> **For the post.** Suggested order: the problem; three or four short lineages; the counter-cases; the
> conditions; the roles forming now, tested against them; the case for engineering; where the work could
> land; the question and the verdict. Move the full lineage tables, the timeline and the notes to an appendix.

## Summary

**Lineages at a glance.** Work moves between roles more often than roles appear from nothing.

| Lineage | Before | The new role | What it became |
| --- | --- | --- | --- |
| Product | Advertising, sales, manufacturing | Brand man (1931) | Product manager, program manager, product ops |
| Planning | Planning programmers, budget clerks | None: spreadsheets (1979–85) moved work into finance roles | Financial planning and analysis (FP&A), analytics engineer, revenue operations |
| Web | System administrators | Webmaster (1993) | Split: developers, operations, SEO, content |
| Security | Computer (EDP) auditors, security managers | Chief information security officer, CISO (1995) | A disclosed owner of cyber risk (2023); chief trust officer |
| Operations | System administrators | Site reliability engineering, SRE (2003), DevOps (2008–09) | Platform engineering (2019–22) |
| Public voice | Community managers, PR, customer service | Social care (Comcast, 2007–08), social media manager (Ford, 2008) | Social media and social care teams |
| Data | Statisticians, business intelligence analysts | Data scientist (2008) | Machine learning engineer, running models in production (MLOps), AI engineer |
| Model work | — | Prompt engineer (late 2022) | Absorbed: AI engineer, context engineering |
| Counter-cases | — | Chief Knowledge Officer, Y2K office, e-business director, Chief Digital Officer, Chief Diversity Officer, growth hacker, metaverse lead | Faded or folded into existing roles |

**What the lineages suggest.** A role emerges when a cost lands between functions and someone senior asks
who answers for it. In our sample, roles that lasted met three conditions: the trade-off is permanent rather than a
migration; nobody already owns it; and something outside the role keeps asking, with a number the role
controls. Otherwise the work moves into existing roles, as it did in most of our cases. Roles that lasted mostly
started with junior or mid-level practitioners, whose authority came from a rule a senior sponsor signed
(section 6); senior-first hires mostly signalled a transition and faded.

**The question set.** In our reconstructions, lasting roles answered a question of this shape:

> *[A recurring cost] keeps landing between [these functions]. Who answers for it?*

For protocols, five questions a COO can answer from tickets, override logs and a list of approvers within a
month. The first measures the cost; the other four test the three conditions above.

1. **Time to amend.** When a policy keeps getting overridden or worked around, how many days until someone
   fixes it or confirms it, and who is that? Count open cases as well as closed ones.
2. **Wait and override.** For our ten most-used approvals and limits, how long does work wait on each, and
   how often is each overridden?
3. **Permanence** (condition 1). Which of these rules existed before our agent rollout and will still
   exist after it?
4. **Ownership** (condition 2). Who can change each rule? When changing one means changing another
   function's rule, who decides, and how long does that take?
5. **Renewal** (condition 3). Who outside the company already asks about these rules, and how often:
   auditors (in US-listed companies, IT change controls on agents that approve money), customers' security
   reviews, regulators (the EU AI Act's oversight duties from December 2027, date to confirm, where agents
   fall under its high-risk list)?

**Verdict, moderate confidence.** A distinct role is a candidate only where all five answers point the
same way: slow amendments, recurring, owned by no one, permanent, and renewed from outside. Otherwise give
the duty to an existing structure (section 8), with time to amend as its number.

## 1. The problem

Companies putting agents to work are already hiring for it. "AI engineer" topped LinkedIn's 2026 list of
fastest-growing US job titles, measured by members' job starts from 2023 to 2025 (S).[^linkedin] Forward-deployed engineer
postings rose about 800% between January and September 2025 by one Indeed and *Financial Times* count
(S).[^fde] US federal agencies have had to name a Chief AI Officer since 2024 (S).[^caio] Forrester
recommends a named owner for every agent (S).[^forrester]

None of these roles is defined around the rules agents act under: who may approve, spend, see and release what, and
how those rules change. We call these rules a business's *protocols*. The group's job template, now the [Business Protocol Lead](../../blyg-src/threads/job-protocol-operations-lead.md),
bets that someone should. This note asks whether history supports that bet, and what question a business
would have to ask for such a role to exist.

How we checked: trace eight roles from their predecessors through their origin to their successors, name the
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
  study the market, track sales, run advertising and promotion, test in the field, and keep the brand
  profitable. One detail, a limit of two brands per man, is unconfirmed.[^mcelroy] Accounts describe the
  memo as three pages, breaking P&G's one-page rule. The memo itself, in P&G's archives, has not been seen.
- **Outcome.** Lasted, and keeps branching. Each branch answers the same question (who owns the result
  across functions?) in a new medium.

### 2.2 Planning and analysis: from planning programmers to FP&A, analytics engineering and RevOps

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | 1970s | Mainframe corporate planning models run by specialist programmers; budget clerks | Each run costs days, so we test one scenario. Who answers when the untested one happens? | IFPS, late 1970s; nearly 2,000 firms in the US, Canada and Europe using or developing planning models, per a 1976 survey (S)[^planningmodels] |
| Origin | 1979–85 | The spreadsheet analyst (VisiCalc 1979, Lotus 1-2-3 1983, Excel 1985 for the Mac, 1987 for Windows) | What happens to the plan if one assumption changes? (No "who": no new title followed.) | Bricklin's blackboard story (S)[^visicalc]; product dates (S) |
| Successor | 1980s–2000s | Financial planning and analysis (FP&A) | Each unit defends its own forecast. Who owns the one plan we commit to? | (S)[^fpa] |
| Branch | 2018–19 | Analytics engineer | Our analysts can't trust the numbers they model. Who builds and tests the data underneath? | Term circulating in the dbt community in 2018; first formal write-up early 2019 (S)[^analyticseng] |
| Branch | 2018– | Revenue operations (from sales operations) | Marketing, sales and customer success each report their own numbers. Who owns the funnel between them? | Earliest known use of "Revenue Operations" in 2018 (S)[^revops]. The common "Xerox in the 1970s" origin rests on one unreliable vendor blog. |

- **Outcome.** The spreadsheet created no title of its own. It moved work: bookkeeping and accounting
  clerk jobs fell after 1980 while accountant jobs grew, as NPR's *Planet Money* reported in 2015 (S; the
  often-quoted 400,000 and 600,000 figures are unconfirmed).[^planetmoney] Titles tied to the data itself came about forty
  years later, when the data under the models and the conflicts between revenue teams needed owners.

### 2.3 The web: from sysadmin to webmaster to its successors

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | to 1993 | Unix system administrators | — | (S)[^webmasterhist] |
| Origin | 1993–96 | Webmaster | Who is responsible for our website? (Names the technology; the role later split.) | Word first recorded 1993 (S)[^webmaster]. In a 1996 *Web Week* survey, 35% of respondents held the official title, up from none a year earlier (S)[^webmasterhist] |
| Split | late 1990s–2000s | Front-end and back-end developer, operations, SEO specialist, content manager, later UX | Our site is now our storefront. Who answers for search traffic, versus outages, versus off-brand content? | (S)[^webmaster] |
| Fade | 2015–2020 | — | — | Google renamed Webmaster Tools to Search Console (2015, S) and Webmaster Central to Search Central (2020, S)[^webmasterhist] |

- **The job description.** A 1998 webmaster's typical duties: server administration, hand-coded HTML,
  basic graphic design, writing content, and submitting the site to search engines such as AltaVista and
  Yahoo! (S).[^webmaster] RFC 2142 (1997) recorded `webmaster@` as an existing de facto mailbox convention
  (S).[^rfc2142]
- **Outcome.** Split. The work grew; the single owner didn't survive it.

### 2.4 Security: from computer (EDP) auditor to CISO to disclosed owner

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | 1970s–80s | EDP auditor; bank "data security officer"; security manager under the CIO | Our auditors keep finding the same control gaps. Who fixes them? | ISACA retrospective by a former bank data security officer (S)[^isaca] |
| Origin | 1995 | Chief Information Security Officer, Citicorp (Steve Katz) | A hacker moved about $10 million out of customer accounts (most recovered). Who is accountable to the board? | Levin theft (1994; all but $400,000 recovered); board told the CEO to hire a security executive (S)[^katz] |
| Spread | 2000s–2010s | CISO, mostly reporting to the CIO at first | — | Fewer than half of the Fortune 1000 had a full-time CISO in 2010 (CMU CyLab); about 62% of the Fortune 500 had one by 2019 (S)[^cisoshare] |
| Successor | 2023– | A named, disclosed owner of cyber risk | The board must now state who manages cyber risk. Which role, with what expertise, do we report in our annual filing? | SEC Regulation S-K Item 106, adopted 26 July 2023; in early 2024 filings, 85% named a CISO or similar role and 62% a dedicated information-security leader (S)[^item106] |
| Branch | 2010s– | Chief trust officer | Customers' security reviews are stalling deals. Who owns trust as a sales asset? | Forrester (S)[^trust] |

- **Personal liability.** In October 2023 the SEC sued SolarWinds and its CISO personally; most of the case
  was dismissed in July 2024 and the SEC dropped the rest in November 2025 (S).[^solarwinds]
- **Outcome.** Lasted and climbed. Since 2023, regulation requires listed US companies to disclose which managers handle cyber risk; most name a CISO.

### 2.5 Operations: from sysadmin to SRE and DevOps to platform engineering

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | to 2003 | System administrators | Ops headcount grows in step with traffic. Who can break that link? | SRE book, "The Sysadmin Approach to Service Management" (S)[^sre] |
| Origin | 2003 | Site reliability engineer, Google | Outages follow releases, and no one owns reliability. Who answers for it while we keep shipping? | Treynor Sloss: "SRE is what happens when you ask a software engineer to design an operations team"; ops work capped at 50% (S)[^sre] |
| Origin | 2008–09 | DevOps (practice, then title) | Developers are paid to change things, operations to keep them stable. How do we stop the two fighting? (No "who": its founders meant a practice.) | Shafer's "Agile Infrastructure" session, Toronto, August 2008; "10+ Deploys per Day", Velocity 2009; first devopsdays, Ghent, 2009 (S)[^devops] |
| Pushback | 2012 | — | — | Humble: "there is no such thing as a devops team" (S)[^humble] |
| Successor | 2019–22 | Platform engineer | Every team rebuilds its own pipeline. Who cuts the duplicated cost and cognitive load? | *Team Topologies* (2019); Gartner Hype Cycle 2022 (S)[^platform] |

- **Outcome.** SRE lasted as a role with an explicit contract (error budgets, the 50% cap). DevOps became
  both a practice and a title, against its founders' advice. Platform engineering builds on DevOps rather
  than replacing it.

### 2.6 Public voice: from community manager to social care and social media manager

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | 1980s–2000s | Bulletin-board sysops; online community managers (AOL, The WELL from 1991, games); PR; customer service | — | (S)[^community] |
| Origin | 2007–08 | Social customer service at Comcast (Frank Eliason) | Customers complain in public faster than our call centre can respond. Who answers? | Informal from September 2007, official February 2008; about ten staff by 2009 (S)[^comcast] |
| Origin | 2008 | Head of social media, Ford (Scott Monty) | Bloggers and customers shape our brand before PR can respond. Who speaks for the company in public, in real time? | Hired mid-2008; formal title "Global Digital & Multimedia Communications Manager" (S)[^ford] |
| Spread | 2010s | Social media manager; social care teams | — | About 64,000 US social media managers in 2022, by Revelio Labs' own count (S)[^revelio] |

- **Outcome.** Lasted and multiplied. The first holders did the work under existing titles.

### 2.7 Data: from statistician to data scientist to ML and AI engineer

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Before | 1989–2000s | Statistician; business intelligence analyst | Our warehouse reports what happened. Who can tell us why? | Jeff Wu proposed renaming statisticians "data scientists" in 1997; "business intelligence" popularised from 1989, origin disputed (S)[^datahist] |
| Origin | 2008 | Data scientist (LinkedIn, Facebook) | Our product produces data no team can analyse, and growth decisions are made blind. Who answers for what the data says? | Patil and Hammerbacher; Hammerbacher's 2009 chapter in *Beautiful Data* says "research scientist" didn't fit (S)[^datascience] |
| Recognition | 2012, 2018 | — | — | HBR, October 2012[^hbr]; US occupational code 15-2051 in 2018 (S)[^soc] |
| Successor | mid-2010s | Machine learning engineer; MLOps (about 2020) | Our models never leave the notebook. Who gets them into production? | (S)[^mle] |
| Successor | 2023 | AI engineer | Who builds products on models? (Names the technology.) | swyx's essay "The Rise of the AI Engineer" (2023; month M) (S)[^aieng] |

- **Outcome.** Lasted, then branched toward production and products.

### 2.8 Model work: from prompt engineer to context engineering and AI engineering

| Stage | Years | Role | The business question | Evidence |
| --- | --- | --- | --- | --- |
| Origin | late 2022 (month M) | Staff prompt engineer, Scale AI (Riley Goodside) | How do we get reliable work out of these models? (Names the technology, no "who"; the role was absorbed.) | Alexandr Wang called him the first person hired with the title (S)[^goodside] |
| Peak | 2023 | Prompt engineer | — | Anthropic's posting at $175,000–$335,000: the field "is arguably less than two years old" (S)[^anthropic] |
| Absorbed | 2025 | — | — | WSJ, April 2025: "suddenly obsolete"; Indeed searches for the title down from 144 to 20–30 per million (S)[^wsj] |
| Successor | June 2025 | Context engineering (practice) | Our agents fail because they lack the right information at each step. Who designs what they see? | Tobi Lütke's preference for the term, endorsed by Andrej Karpathy (S)[^context] |
| Successor | 2023– | AI engineer; AI trainer | — | (S)[^aieng] |

- **Outcome.** Absorbed within about two years. The skill became general literacy; the harder work moved
  to AI engineers and to context engineering.

## 3. Roles forming now

| Role | Since | The business question | Status |
| --- | --- | --- | --- |
| Forward-deployed engineer | Palantir, early 2010s; surge 2025 | How do we get our AI working inside each customer's operations? | Growing fast (S)[^fde] |
| AI engineer | 2023 | Who builds products on models? | #1 fastest-growing US title, 2026 (S)[^linkedin] |
| Chief AI Officer | US federal agencies, 2024 | Who coordinates AI use and manages its risk? | A 2025 White House budget-office memo (M-25-21) kept the role but called its holders "change agents and AI advocates", which sounds like a temporary role. IBM reports 76% of surveyed organisations had one in 2026, up from 26% in 2025 (S)[^caio][^ibm] |
| Governance, risk and compliance (GRC) engineer | about 2024 | Our compliance evidence is collected by hand once a year. Who turns controls into code? | A manifesto and vendor career guides; sources disagree on whether it's a title or a capability (S)[^grc] |
| Named agent owner | 2025–26 | Who manages each agent's lifecycle? | Analyst recommendation, not a title (S)[^forrester] |
| Agent supervisor | 2026 | Who oversees agents doing work people used to do? | Gartner expects infrastructure staff to shift to supervising agents (S)[^gartner] |
| AI agent manager | 2025–26 | Who sets agents' tasks, reviews their output and handles the exceptions they can't? | Defined in *Harvard Business Review* by Srinivasan and Wei; no standard title, no senior track (S)[^agentmgr] |

All but one of these questions name the technology. In our sample (section 6), roles like that were
usually short-lived, though roles tied to infrastructure, like database administrator, lasted. Only the GRC engineer's question names a recurring cost.

## 4. Timeline

| Year | Event | Lineage |
| --- | --- | --- |
| 1931 | McElroy's "brand man" memo at P&G | Product |
| 1976 | Nearly 2,000 firms using or developing corporate planning models | Planning |
| 1979 | VisiCalc ships | Planning |
| late 1980s | Program manager role at Microsoft | Product |
| 1993 | "Webmaster" first recorded | Web |
| 1995 | Steve Katz becomes the first CISO, at Citicorp | Security |
| 1996 | 35% of *Web Week* respondents hold the title webmaster | Web |
| 1997 | RFC 2142 records `webmaster@`; Wu proposes "data scientist" for statisticians | Web, Data |
| 2003 | Treynor Sloss starts SRE at Google | Operations |
| 2007–08 | Comcast's social care; Ford's head of social media | Public voice |
| 2008 | Patil and Hammerbacher name the data scientist; "Agile Infrastructure" in Toronto | Data, Operations |
| 2009 | "10+ Deploys per Day"; first devopsdays | Operations |
| early 2010s | Palantir's forward-deployed engineers | Forming now |
| 2012 | Humble: "no such thing as a devops team"; HBR on data scientists | Operations, Data |
| 2018 | "Data Scientists" enters the US occupational classification; "revenue operations" and "analytics engineer" appear | Data, Planning |
| 2019 | *Team Topologies* defines platform teams | Operations |
| 2020 | Google renames Webmaster Central | Web |
| late 2022 | First staff prompt engineer, at Scale AI | Model work |
| 2023 | SEC Item 106 requires disclosure of who manages cyber risk; Anthropic's prompt engineer posting; "AI engineer" | Security, Model work, Data |
| 2024 | US agencies required to name Chief AI Officers | Forming now |
| 2025 | Prompt engineering "obsolete"; context engineering named; FDE postings up about 800% | Model work, Agents |
| 2026 | AI engineer tops LinkedIn's fastest-growing titles | Forming now |
| Dec 2027 | EU AI Act: companies using high-risk AI systems must assign trained human overseers (S, date to confirm)[^aiact] | Forming now |

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
  metaverse lead had one. Y2K had heavy board and regulator pressure, and ended anyway.
- **Transition roles end when the transition does.** Y2K, e-business and the Chief Digital Officer were
  hired to change the organisation, and their success made them redundant. The CISO, SRE, the brand
  manager and the controller are hired to hold a balance indefinitely.
- **In 2016, "digital against legacy" looked as permanent as "development against operations".** The
  e-business director and the Chief Digital Officer met the conditions as they looked at the time. So the test has to be applied
  before the fact, and it can still be wrong (section 6).
- **A role can lose its question.** The Chief Diversity Officer faded when the outside pressure that
  created it reversed.

## 6. What makes a role emerge, and what makes it last

| Lineage | New capability | The gap between functions | What happened to the role |
| --- | --- | --- | --- |
| Product | Mass advertising | Advertising, sales, production | Lasted; keeps branching |
| Planning | Spreadsheet | None at first | No title of its own; work moved into finance (FP&A), then to data roles from 2018 |
| Web | The web | Small at first | Split into specialties |
| Security | Networked banking | IT, audit and business lines; made visible by a loss | Lasted, climbed, now disclosed in annual reports |
| Operations | Web-scale software | Development against operations | SRE lasted; DevOps became practice and title; platform teams followed |
| Public voice | Social platforms | PR, marketing, customer service | Lasted, multiplied |
| Data | Cheap storage and compute | Engineering against analysis | Lasted, then branched |
| Model work | Large language models | None clear | Absorbed into AI engineering and context engineering |

**Why roles emerge.** Usually a new capability makes some work cheap. A cost then lands between functions
until someone senior asks who answers for it. Y2K and the Chief Diversity Officer show the capability
isn't required.

By "lasted" we mean still hired under that title, or a direct successor's, fifteen years later.

**Why roles last.** Three conditions, meant as tests before the fact. Section 5's Chief Digital Officer
shows they can still mislead: in 2016 its conflict looked permanent.

1. **The conflict comes from a permanent trade-off in the business model, not from a migration.** Speed
   against stability, revenue against risk, one brand against another never end. Old channel against new,
   legacy against digital, pre-2000 dates against post-2000 end when the migration completes. The test:
   *would this conflict still exist if the transition finished tomorrow?*
2. **Nobody already owns the trade-off.** Most permanent trade-offs have an owner. The roles that lasted
   took one nobody held: no one owned a single brand's results in 1931, or reliability while shipping in
   2003.
3. **Something outside the role keeps renewing the question, and the role controls a number.** A recurring,
   countable cost (an error budget, fraud losses, a brand's profit), a regulator or auditor, or customers who
   demand it. Roles held up only by a sponsor (the Chief Knowledge Officer, the Chief Digital Officer)
   faded when the sponsor moved on.

### Who held new roles first

Most roles that lasted began with junior or mid-level practitioners and grew upward. Most roles that began
as senior hires faded.

| Role | First holders | Seniority at the start | Lasted? |
| --- | --- | --- | --- |
| Brand man (1931) | McElroy was 26; P&G recruited brand assistants straight from university (S)[^pgbrand] | Junior | Yes |
| Spreadsheet analyst | Analysts and associates in finance teams (M) | Junior | Yes, inside finance |
| Webmaster | Often whoever knew HTML (M) | Junior to mid | Split |
| SRE (2003) | A senior lead; engineers hired at the normal engineering bar (S)[^sre] | Mid, under a senior lead | Yes |
| DevOps | Sysadmins and developers, from the grassroots (S)[^devops] | Mid | Yes |
| Social media manager | Mid-level managers (Eliason, Monty's "Communications Manager" title); mass hiring junior, "intern-tier" (S)[^revelio] | Junior to mid | Yes |
| Data scientist | Practitioners, many young PhDs (M) | Mid | Yes |
| Prompt engineer | Practitioners, well paid, not executives | Mid | Absorbed |
| Forward-deployed engineer | Palantir hires new graduates as "Deltas" (S)[^fdegrad] | Junior to mid | Growing |
| CISO (1995) | Katz, on a board mandate | Senior | Yes: the exception |
| Chief Knowledge, Digital and Diversity Officers; metaverse leads | Executives | Senior | Faded |
| Chief AI Officer | Executives | Senior | Too early to tell |

**Two readings.** Senior-first hires are how companies signal a transition, and transitions end.
Practitioner roles are how a capability becomes routine, and they grow a senior layer later: brand men
became brand managers and then chief marketing officers; data science got chief data officers above it;
SRE got vice presidents. The CISO shows the other route: a visible loss, a board mandate and later
regulation can create a senior role directly.

**Authority came from an agreement, not from rank.** The early SRE could stop launches because Google's
error budget policy, approved in advance by the people who make the business decision, said so (S).[^ebpolicy]
The brand man's authority came from answering for one brand's profit. In both cases a senior sponsor
signed the rule once, and practitioners applied it every day. For protocol work, the equivalent would be
an amendment rule and an autonomy budget signed by the COO, applied by practitioners.

Caveat: the seniority of early holders is partly from memory, and junior roles that faded leave even fewer
traces than senior ones.

**Counter-examples to keep in view.**

- **Roles named after a technology that lasted:** database administrator, network engineer, ERP consultant,
  cloud architect (M). The better split: technology that becomes *infrastructure with its own maintenance
  load* keeps a role; technology that becomes *literacy* (HTML, prompting) is absorbed; technology that
  *fails* (the metaverse) takes its role with it.
- **A permanent trade-off whose role faded:** Microsoft folded its software test engineers into a single
  engineer role in 2014 (S).[^sdet] Change advisory boards, committees that approve each change to
  production systems, weighed speed against stability for decades. Research for *Accelerate* found their
  approvals went with slower delivery and no fewer failed changes (S).[^cab] The trade-off moved into engineering practice.
- **A legal mandate without a dedicated role:** GDPR requires many companies to name a data protection
  officer (DPO). Yet in a 2018 survey, 62% of in-house lawyers gave the duty to existing staff, and
  outsourced DPOs became common (S).[^dpo] Regulation renews the *duty*; it doesn't guarantee a role.

**Further patterns, with the same caution.**

- **In our sample, questions that name the technology went with short-lived roles** (webmaster, prompt
  engineer, metaverse lead), and questions that name a cost or a conflict went with
  roles that lasted. This is our reconstruction; the data scientist fits only when its question is
  restated as a cost.
- **The title trails the work by years.** Eliason and Monty did the work under other titles; Facebook's
  first data team considered the titles analyst and research scientist and rejected them; official classification took ten
  years.

## 7. The case that it's all engineering

**The strongest case.** Every rule in question (discount limits, approval chains, data leaving the company,
spending caps) ends up as policy written in code: access scopes, policy engines, checks in the release
pipeline. Deciding what a rule says happens once, in the function that already owns the risk. What
follows (versioning, testing, rollout and rollback) is engineering work, and SRE showed engineers can own a
business trade-off once it is a number. Next, agents will carry limits among themselves through
agent-to-agent protocols, signed mandates and spending tokens, and monitors will flag violations faster
than any reviewer. A human rule owner in the middle repeats the change advisory board, which research links
to slower delivery and no fewer failures. Rule changes can go through code review, with finance, security
and legal approving their own lines. No new role, only tooling and peer review.

**Where it is weaker.**

- **Engineering builds rules but doesn't decide them.** Which discount limit, whose approval, what data may
  leave: these trade revenue against risk. In the SRE case, a number (the error budget), owned by a new team,
  settled the conflict; the question is who sets and owns the equivalent number for business
  rules.
- **Security is engineered too, and the CISO still exists.** Since 2023 US listed companies must disclose who
  manages cyber risk. A function built in code can still need an accountable owner.
- **New roles are already forming around agents.** Forward-deployed engineers, Chief AI Officers and named
  agent owners exist because someone must answer for agents in the business.

**What would decide between the views.**

- **Who approves rule changes.** In companies running many agents, do business owners approve changes to
  policy code, or only engineers?
- **How often rules change across functions.** Rare changes suit a committee or the function that owns the
  risk; frequent ones that cut across functions need an owner.
- **Time to amend.** How long it takes to change a wrong rule once it is found, in companies with and
  without a named owner.
- **Incident attribution.** Are incidents traced to a wrong or unowned rule, or to an implementation bug?
- **Titles over time.** Whether "AI governance", "agent operations" or "AI controls" titles persist or fold
  back into engineering (section 10).

The verdict is at the end of section 9, after the question that tests it.

## 8. Applying the pattern to protocols

| Candidate gap | Permanent trade-off? | Already owned? | What renews it | Likely outcome |
| --- | --- | --- | --- | --- |
| What each agent may see, do and spend | Yes: access against safety | Yes: security, identity and access management | Incidents, audits | Absorbed into security |
| Day-to-day oversight of agents in each team | No: a skill that spreads | Each manager | Nothing outside the team | Becomes a skill, as prompting did |
| "Get our agents deployed" | No: a migration | Chief AI Officer, forward-deployed engineers | A sponsor | Transition role; ends when deployment is routine |
| Which business rules become enforced in systems, and how they change together as the business grows | Yes: revenue against risk, speed against control | Split: finance, security, legal and sales each own pieces; no one owns how they change together | Deals waiting on approvals, incidents traced to rules, and from December 2027 (date to confirm) EU oversight duties | Candidate for a role, or a mandate for an existing structure |

**Where the fourth gap could land.**

| Structure | Strength | Risk |
| --- | --- | --- |
| CFO organisation: deal desk, FP&A, controller | Already owns discount and spending limits and their delays | Leans to cost control over growth |
| Internal controls and GRC engineering | Audited, already turning controls into code | Tests once a year; leans to compliance |
| Enterprise risk / chief risk officer | Owns the risk register across functions | Far from day-to-day work |
| Revenue operations | Owns the funnel's systems and data | Only covers revenue-side rules |
| Platform engineering | Builds and runs the enforcement | Doesn't decide the trade-offs |
| A council or committee | Cheap, cross-functional | Can become a change advisory board |
| A champions network in each function | Close to the work | No one answers for the whole |
| Vendor and agent-platform defaults | No headcount | The vendor's rules become yours by default |
| Each team owns its interface rules | Matches Amazon's rule that teams talk only through published interfaces | No one owns how rules interact |
| A dedicated role | One owner for how rules change together | Can become a slow approval board; needs a number it controls |

**A tension in our own material.** The Business Protocol Lead template says the role *finds* the rules
("security, finance and legal decide what the rules say; engineering builds them"). By section 6, a role
that lasts has to own a number. Section 9 proposes one: how fast wrong rules get changed. Section 9's question is
built to show which it should be.

## 9. The question a business needs to ask today

In our reconstructions, lasting roles began with a question that named a cost and asked who answers for
it, and something kept asking it. The protocol version should be measurable, neutral about technology,
and able to come out against a new role:

> **When a policy keeps getting overridden or worked around, how many days until someone fixes it or
> confirms it, and who is that?**

To answer it from records: start the clock when a rule crosses a threshold (for example, more than a set
number of overrides in 30 days, or a formal request to change it), stop it at a recorded decision to change
or keep the rule, and count the cases still open. The Summary lists the four questions that interpret the
answer; the critique (`business-protocol-lead-critique.md`, section 6) sets out the measurement.

How the answer points to a structure:

- **Short time to amend, a named owner** → no new role; the current structure works.
- **Long time to amend, but rare** → a committee or the function that owns the risk is enough.
- **Long time to amend, recurring, ownership split across functions** → a candidate role, or a mandate for
  one of the structures in section 8, with time to amend as the number it controls.

Our hypothesis is that agents hit wrong or unowned rules faster and more often than people do. One
illustration: in the Hugging Face incident, OpenAI's agents used a package repository as a message board,
a use no rule had anticipated (S).[^hf] That is why to ask now. The question itself is about rules.

**Verdict, moderate confidence.** A distinct role is a candidate only where all five answers in the
Summary point the same way: slow amendments, recurring, owned by no one, permanent, and renewed from
outside. Otherwise give the duty to an existing structure (section 8), with time to amend as its number.
That is the likelier outcome in most companies, as it was for the DPO.

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
- [ ] **Reconstructed, and so partly circular.** Each business question is our reading, written knowing how
  the role turned out, and then used to explain the outcome. McElroy's memo asked for staff. Test the
  conditions on roles forming now (section 3) and check back in two years.
- [ ] **Base rate.** We have no count of all new titles that appeared and how many lasted, so we can't say
  how unusual the lasting ones are.
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
[^webmasterhist]: "Webmaster," *The Princeton Review* careers, https://www.princetonreview.com/careers/183/webmaster (the 1996 *Web Week* survey); "Job Profile: Webmaster," *Certification Magazine*, https://certmag.com/articles/job-profile-job-webmaster-constantly-evolved-since-1990s; "Webmaster," *Mewayz Wiki*, https://wiki.mewayz.com/wiki/Webmaster. (S)
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
[^sdet]: "How Microsoft Does Quality Assurance," *The Pragmatic Engineer*, https://newsletter.pragmaticengineer.com/p/how-microsoft-does-quality-assurance. (S)
[^cab]: Nicole Forsgren, Jez Humble and Gene Kim, *Accelerate: The Science of Lean Software and DevOps* (IT Revolution, 2018), as summarized in "Change-Advisory Board," *Wikipedia*, https://en.wikipedia.org/wiki/Change-advisory_board, and "Change Advisory Boards Don't Work," *Octopus Deploy*, https://octopus.com/blog/change-advisory-boards-dont-work. (S)
[^dpo]: "GDPR Says Companies Must Have a Data Privacy Officer," *SHRM*, citing an Association of Corporate Counsel survey (2018), https://www.shrm.org/topics-tools/employment-law-compliance/gdpr-says-companies-must-data-privacy-officer; IAPP, "Outsourcing Your DPO," https://www.iapp.org/resources/article/series-outsourcing-your-dpo. (S)
[^hf]: OpenAI, "The Hugging Face Incident and the Road Ahead," 2026, https://openai.com/index/hugging-face-incident-and-the-road-ahead/; the group's first reading of the year. (S)
[^pgbrand]: "The History of Procter & Gamble's Brand Strategy," *LiveAbout*, https://www.liveabout.com/market-research-history-brand-management-at-pandg-2297141; "Deb Henretta," *Wikipedia*, https://en.wikipedia.org/wiki/Deb_Henretta (hired as a brand assistant after her master's in 1985). (S)
[^fdegrad]: Palantir, "Forward Deployed Software Engineer, New Grad," https://jobs.lever.co/palantir/2e6b0ac8-83e9-4be5-a3aa-cf319f751728; "Dev versus Delta: Demystifying Engineering Roles at Palantir," https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87. (S)
[^ebpolicy]: Google, *The Site Reliability Workbook*, "Implementing SLOs" and Appendix B, "Example Error Budget Policy," https://sre.google/workbook/implementing-slos/. (S)
[^agentmgr]: Suraj Srinivasan and Vivienne Wei, on the "agent manager," *Harvard Business Review*, as summarized at https://blog.theinterviewguys.com/what-an-ai-agent-manager-actually-does/; titles and hiring in "AI Agent Manager Jobs in 2026," https://www.aicodex.to/articles/agent-operator-job-market-2026. (S)
