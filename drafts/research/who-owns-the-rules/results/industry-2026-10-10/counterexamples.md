# Counter-examples: who owns the rules automated systems follow

Search date: 10 October 2026. About 47 web searches. WebFetch failed on the first try (DNS error on pmc.ncbi.nlm.nih.gov), so as instructed everything below comes from search-result summaries. **Every item is graded S** (search summary only), even where the summary quotes the primary source. Nothing here comes from memory. Before anything is cited publicly, the source should be opened and the item regraded P or R.

The column "Required?" asks whether a regulator, accreditor or insurer required that role or body to hold the decision.

---

## Claim 1

> When a rule that constrains an automated system needs to change and the change affects several functions, the decision goes to a committee or a named senior executive, not to an individual practitioner.

### Candidate counter-examples

**1.1 Mozilla root store: the module owner decides (web PKI / browsers, c. 2008–2024)**
- *Case:* Mozilla appointed a CA Certificates module owner and peers "to make decisions regarding all matters relating to CA certificates included in our root store", and a separate CA Certificate Policy module owner and peers "to maintain this policy". The policy changes only after public consultation. For about 16 years the owner was Kathleen Wilson, whose title was "Root Store Program Manager". She retired on 29 February 2024.
- *Who decided, and at what level:* A named program manager (practitioner level, not an executive), advised by peers and by public discussion on dev-security-policy. Her decisions bind Firefox's automated trust behaviour and affect product, security, partner CAs and users.
- *Required?* No. Mozilla's own governance. The CA/Browser Forum sets baseline rules but has no enforcement role.
- *Strength:* **Moderate to strong.** It is the clearest case of a named non-executive owner holding cross-functional rule decisions. Caveat: the peers and the public consultation make it partly collective, and the e-Guven removal is described as following "consensus" in the forum.
- *Grade:* S
- Mozilla. "Mozilla Root Store Policy." Accessed October 10, 2026. https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/policy/.
- CA/Browser Forum. "Mozilla Browser News" (F2F 61, New Delhi, February 2024). Accessed October 10, 2026. https://cabforum.org/2024/02/26/minutes-of-the-f2f-61-meeting-in-new-delhi-india-february-26-27-2024/2-February-2024-Mozilla%20Browser%20News.pdf.
- CA/Browser Forum. "Mozilla Update, CABF Ottawa F2F," February 2023. Accessed October 10, 2026. https://cabforum.org/uploads/5-2023-February-Mozilla-Update-CABF-Ottawa-F2F.pdf.

**1.2 Progressive Insurance: state and field product managers own pricing (US auto insurance, 1983–2013+)**
- *Case:* Progressive's careers page says state product managers are "fully responsible for the profit and loss" in their state. A Darden case (2010) follows Omar Parvaiz, "field product manager in charge of Tennessee and South Carolina", as he weighs the results of a year-long test of a pricing algorithm he developed. The algorithm changes how marketing costs are allocated in rates, which touches pricing, marketing and finance. On a 2013 earnings call, an executive credited a product manager with "proactive measures on rate level in Florida".
- *Who decided, and at what level:* A mid-level product manager with P&L ownership for one or two states. A separate pricing manager executes the indications.
- *Required?* State insurance departments review rate filings, but no source says a regulator dictates who decides inside the firm.
- *Strength:* **Moderate.** The pattern is clear. The case summary does not say whether Parvaiz could adopt the algorithm on his own or needed sign-off from above.
- *Grade:* S
- Pfeifer, Phillip E., and Benjamin Potter. "Acquisition Cost Allocation at Progressive Insurance." Case M-0785. Charlottesville: Darden Business Publishing, October 25, 2010. https://indiastore.darden.virginia.edu/acquisition-cost-allocation-at-progressive-insurance.
- Progressive. "Product and Process Management." Careers. Accessed October 10, 2026. https://progressive.com/careers/our-teams/product-and-process-management.
- The Progressive Corporation. Q2 2013 earnings call transcript. Accessed October 10, 2026. https://www.roic.ai/quote/PGR:US/transcripts/2013-year/2-quarter.

**1.3 Wikipedia edit filter managers (online community, 2009–2020)**
- *Case:* An individual edit filter manager can approve and implement a filter request, "mostly after a discussion". Discussion sometimes happens after the fact, and a filter "may be applied before having been thoroughly tested". The recommended practice is to log only first and announce on the noticeboard. English Wikipedia had 154 edit filter managers in May 2019.
- *Who decided, and at what level:* An individual volunteer holding a granted permission. There is no executive or committee gate on each change.
- *Required?* No.
- *Strength:* **Moderate.** The authority is clearly individual, and filters affect every editor and many workflows. Caveat: this is a volunteer community, not a firm, and part of the evidence comes from a thesis draft rather than the peer-reviewed paper.
- *Grade:* S
- Vaseva, Lyudmila, and Claudia Müller-Birn. "You Shall Not Publish: Edit Filters on English Wikipedia." In *Proceedings of OpenSym 2020*. https://opensym.org/wp-content/uploads/2020/08/os20-paper-a4-vaseva.pdf.

**1.4 Self-serve fraud rules engines: Uber Mastermind and Grab Griffin (ride-hailing and delivery, c. 2016–2021)**
- *Case:* Uber built Mastermind because analysts had to go through engineers (about an hour per rule) to change fraud logic. Afterwards, "risk analysts and engineers add policy-based, modus operandi-based and model-based rules", and later reporting says it let risk analysts build and roll out rules without engineers. Mastermind's rules cover payments fraud, account takeover, driver–rider collusion and promotion abuse, so they reach payments, operations and growth. Grab's Griffin let analysts and data scientists self-serve rule changes and "deploy with a few clicks".
- *Who decided, and at what level:* Analysts (practitioner level) write and deploy the rules.
- *Required?* No regulator requirement is mentioned.
- *Strength:* **Weak to moderate.** It shows practitioners hold the technical means and routine authority. It does not show who signs off on a change with deliberate cross-functional effects (for example, a promotion-abuse rule that blocks a marketing campaign).
- *Grade:* S
- Uber Engineering. "Mastermind: Using Uber Engineering to Combat Fraud in Real Time." Uber Blog, c. 2017. https://www.uber.com/us/en/blog/mastermind/.
- Uber Engineering. "Mitigating Risk in a Three-Sided Marketplace: A Conversation with Trupti Natu and Neel Mouleeswaran on the Uber Eats Risk Team." Uber Blog. https://www.uber.com/en-GB/blog/uber-eats-risk-team/.
- TechCrunch. "Ex-Uber Software Engineers Raise $3M for Sperta." December 16, 2021. https://techcrunch.com/2021/12/16/ex-uber-software-engineers-raise-3m-for-sperta/.
- Grab Engineering. "Griffin." Grab Tech Blog. Accessed October 10, 2026. https://engineering.grab.com/griffin.

**1.5 High-impact rule pushes by practitioners: Cloudflare WAF (2019) and CrowdStrike Channel File 291 (2024) (internet infrastructure and security)**
- *Case:* On 2 July 2019 an engineer on Cloudflare's firewall team "deployed a minor change to the XSS detection rules through an automatic process". The rule went out globally in one step and took down HTTP/HTTPS traffic worldwide for 27 minutes. On 19 July 2024 CrowdStrike shipped a Rapid Response Content update "as part of regular operations". This class of content "previously [was] not subjected to the same internal tests and reviews as software updates".
- *Who decided, and at what level:* At Cloudflare, a practitioner engineer. At CrowdStrike, routine content operations; the sources found do not name a role.
- *Required?* No.
- *Strength:* **Weak as a counter-example to the claim as worded.** The claim is about changes that are known to affect several functions. These were routine changes whose company-wide effect was not intended. They do show that, in practice, rules with very wide reach were changed below committee level, and that both firms added gates only afterwards.
- *Grade:* S
- Cloudflare. "Details of the Cloudflare Outage on July 2, 2019." Cloudflare Blog, July 2019. https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019. (Author and exact date not confirmed by the search.)
- CrowdStrike. "Channel File 291 Incident: Root Cause Analysis." August 6, 2024. https://crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf.
- The Hacker News. "CrowdStrike Reveals Root Cause of Global System Outages." August 2024. https://thehackernews.com/2024/08/crowdstrike-reveals-root-cause-of.html.

**1.6 Early platform rule-writers: Facebook 2008–09 and Twitter 2009 (online platforms)**
- *Case:* Dave Willner worked at Facebook from 2008 and "wrote the internal content rules that became Facebook's first published community standards". He later became head of content policy. Del Harvey joined Twitter in 2008 as its 25th employee to fight spam accounts. In early 2009 she was "reportedly the only one at Twitter dealing with spam and abuse".
- *Who decided, and at what level:* Individual practitioners at the time they wrote the rules.
- *Required?* No.
- *Strength:* **Weak to moderate.** These are start-up cases with few functions, and the rules were applied mostly by human moderators rather than automated systems. They are counter-examples only in early-stage firms. Once the firms scaled, the decisions moved to forums (see "Evidence that supports Claim 1" below).
- *Grade:* S
- Tech Policy Press. "Considering Trust and Safety's Past, Present, and Future." Accessed October 10, 2026. https://www.techpolicy.press/considering-trust-and-safetys-past-present-and-future.
- "Why Facebook Can't Fix Itself." *New Yorker*. (Author and date not confirmed by the search.) Mirror consulted: https://rotund.notion.site/Why-Facebook-Can-t-Fix-Itself-The-New-Yorker-c7257072685f4b139dce9ea93eb5d810.
- Radiolab. "Post No Evil." WNYC, August 17, 2018. https://radiolab.org/podcast/post-no-evil.

**1.7 "Artisanal" moderation at small platforms (online platforms, c. 2018)**
- *Case:* Caplan found that at Vimeo, Medium, Patreon and Discord, policy writing and enforcement happen in the same small in-house team, with little automation. At industrial platforms (Facebook, Google), policy development is kept separate.
- *Who decided, and at what level:* Small teams. Seniority is not specified.
- *Required?* No.
- *Strength:* **Weak.** The report is about structure, not decision rights, and it describes low automation.
- *Grade:* S
- Caplan, Robyn. *Content or Context Moderation? Artisanal, Community-Reliant, and Industrial Approaches.* New York: Data & Society, November 2018. https://datasociety.net/output/content-or-context-moderation/.

**1.8 System-level bureaucracies: designers hold the discretion (government, c. 2002)**
- *Case:* Bovens and Zouridis argue that in agencies such as Dutch student-grant and tax administration, discretion moves from street-level officials to "system analysts and software designers", who translate law into decision rules. They propose hardship clauses and panels to bring that discretion back under control.
- *Who decided, and at what level:* Practitioner-level designers, in practice rather than on paper.
- *Required?* No. The authors present it as a gap in constitutional control.
- *Strength:* **Moderate as a conceptual counter-example.** It is a peer-reviewed argument that, in practice, the rule decision sits with practitioners. The formal authority still lies with law and ministers.
- *Grade:* S
- Bovens, Mark, and Stavros Zouridis. "From Street-Level to System-Level Bureaucracies: How Information and Communication Technology Is Transforming Administrative Discretion and Constitutional Control." *Public Administration Review* 62, no. 2 (2002): 174–84. https://doi.org/10.1111/0033-3352.00168. PDF: https://toonaangevend-werk-van-mark-bovens.sites.uu.nl/wp-content/uploads/sites/1208/2025/06/Public-Administration-Review-2002-Bovens-From-Street‐Level-to-System‐Level-Bureaucracies-How-Information-and.pdf.

**1.9 Job postings that give analysts ownership of rules (airlines, retail, banking, ad tech, logistics; 2020s)**
- *Cases:*
  - A Virgin Atlantic revenue management analyst uses "O&D business rules and demand influence rules".
  - An American Airlines analyst adjusts seat availability across fare classes.
  - A Vanguard senior analyst "owns fraud rules and controls across debit cards and real-time payment rails", with "rule governance, change controls".
  - A Longo's senior pricing analyst "administers and maintains pricing strategies and supporting rules" and is business owner of the Price Master tool.
  - A yield analyst at a publisher "propose[s] and appl[ies]" changes to Unified Pricing Rules.
  - A Shurtape senior transportation analyst is asked to "establish business rules ... between the Transportation department and other departments".
- *Who decided, and at what level:* Analysts and senior analysts.
- *Required?* Banking has regulatory oversight of fraud controls. The others do not.
- *Strength:* **Weak.** Job postings describe scope, not decision rights. Several (Citi, Walmart) put the rules inside a policy or under a senior manager.
- *Grade:* S
- Virgin Atlantic. "Revenue Management Analyst" (2319). https://careersuk.virgin-atlantic.com/search-and-apply/revenue-management-analyst-2319.
- American Airlines. "Analyst, Revenue Management Pricing & Yield Management." https://jobs.aa.com/job/Analyst%2C-Revenue-Management-Pricing-&-Yield-Management/86957-en_US/.
- Hackajob. "Fraud Strategy Senior Analyst" (Vanguard). https://hackajob.com/job/0fdeee22-9531-11f1-a7b8-0a05e249917d-fraud-strategy-senior-analyst.
- Longo's. "Senior Pricing Analyst." https://jobs.jobvite.com/longos/job/o9QNAfw6.
- Talentify. "Yield and Monetization Analyst (Contract)." https://www.talentify.io/job/yield-and-monetization-analyst-contract-redwood-city-california-us-remote-jobs-nzojqnhkdfpj.
- Shurtape. "Sr. Transportation Analyst." https://careers-shurtape.icims.com/jobs/1981/sr.-transportation-analyst/job.
- (All accessed October 10, 2026.)

**1.10 Analysts overriding the revenue management system (airlines, 2010s)**
- *Case:* A practitioner column reports that RM analysts "may override the system regularly based on their individual 'judgement'". Weatherford's simulations model analysts' "user influence" on the RM system.
- *Who decided, and at what level:* Analysts.
- *Required?* No.
- *Strength:* **Weak.** These are overrides of outputs, not changes to rules.
- *Grade:* S
- Bacon, Tom. "When RM Becomes Revenue 'Mismanagement'." Reuters Events Travel. https://www.reutersevents.com/travel/node/55982.

**1.11 Organisation-wide rules against committees: Netflix and Booking.com (tech, 2011–2020)**
- *Case:* Netflix's culture memo "avoids decision-making by committee". Each significant decision has an "informed captain", at any level, who farms for dissent and then decides. At Booking.com, "anyone can test anything — without management's permission", and senior management declined to veto a test it doubted.
- *Who decided, and at what level:* Any employee or the captain.
- *Required?* No.
- *Strength:* **Weak on fit.** Neither source is specifically about rules that constrain automated systems, and Booking.com's rule covers testing rather than permanent change.
- *Grade:* S
- Netflix. "Netflix Culture Memo." Accessed October 10, 2026. https://jobs.netflix.com/culture.
- Thomke, Stefan. "Building a Culture of Experimentation." *Harvard Business Review*, 2020 (issue not confirmed by the search). Reprint consulted: https://www.wnccumc.org/detail/building-a-culture-of-experimentation-18654079.

### Evidence found that supports Claim 1 (for balance)
- **Hospitals.** A 2020 JAMIA systematic review found that all eight hospital papers on optimising CDS alerts used a multidisciplinary committee. NewYork-Presbyterian, Utah and Cleveland Clinic all route alert changes through committees. Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC7810441.
- **Facebook.** By 2018 changes to the Community Standards, ads policies and "major News Feed ranking changes" went to the biweekly Product Policy Forum, a cross-functional body. Source: https://about.fb.com/news/2018/11/content-standards-forum-minutes/.
- **Google search.** Ranking changes go through launch reports and a search quality meeting where cross-functional trade-offs are weighed. Source: https://search.googleblog.com/2012/03/video-search-quality-meeting-uncut.html.
- **Google content removals (2008).** Nicole Wong, "The Decider", was a VP and deputy general counsel, i.e. a named senior executive. She decided individual removals rather than rule changes. Source: https://www.pri.org/stories/2008-11-29/googles-gatekeepers.
- **Wikipedia bots.** New bots need approval from the Bot Approvals Group, a committee.
- **Walmart.** A *senior manager* owns the end-to-end fraud rules program. Source: https://careers.walmart.com/us/en/jobs/R-2415481.

### Verdict on Claim 1
I found about **eight credible counter-examples**. Three are moderate to strong: Mozilla's root store module owner, Progressive's state and field product managers, and Wikipedia's edit filter managers. Five are weak to moderate: the self-serve fraud engines, the Cloudflare and CrowdStrike pushes, the early Facebook and Twitter rule-writers, Bovens and Zouridis, and the job postings. Every item is graded S.

None of them is a clean case of a mid-level practitioner in a large firm deliberately deciding a change known to affect several functions, without a committee or executive sign-off. Each one either:
- is routine tuning whose cross-functional effect is incidental (fraud engines, WAF, RM),
- sits outside a firm (Mozilla, Wikipedia),
- comes from an early-stage company (Facebook 2008, Twitter 2009), or
- rests on a P&L-owner model where the "practitioner" is effectively a small business head (Progressive).

The documented cases of deliberate, cross-functional rule change at scale (hospitals, Facebook, Google search) do go to committees.

**The claim is weakened but not overturned.** It should be qualified to large, mature organisations making deliberate changes. It does not hold for:
- routine rule tuning, which practitioners own in many firms and which has caused company-wide outages,
- open-source and community governance, which uses named owners,
- decentralised P&L-owner models.

---

## Claim 2

> Industries that automated heavily but faced little regulation of how the automated systems behave did not create dedicated roles or bodies for the rules those systems follow.

### Candidate counter-examples

**2.1 Platform content and ranking policy teams, and Facebook's Product Policy Forum (online platforms, 2008–2018+)**
- *Case:* Facebook's Product Policy team holds a forum every two weeks on changes to the Community Standards, ads policies and "major News Feed ranking changes". Safety, counter-terrorism, operations, product, legal, communications and other functions take part, and minutes and a change log are published. Klonick describes Facebook, Twitter and YouTube building a rule system that resembles the American legal system, with revised rules and trained decision-makers. She also asks why platforms moderate at all, given §230 immunity.
- *Body and level:* A dedicated policy team and a cross-functional forum. Monika Bickert (VP) chaired it in 2018.
- *Required?* No in the US (§230). Germany's NetzDG (2017) and the EU DSA (2022) came after the teams existed.
- *Strength:* **Strong.** These are dedicated bodies for the rules that automated ranking and enforcement follow, in an industry without behaviour regulation. Caveat: by 2018 political and regulatory pressure was rising.
- *Grade:* S
- Meta. "Product Policy Forum Minutes." November 2018. https://about.fb.com/news/2018/11/content-standards-forum-minutes/.
- Meta. "Policy Forum Minutes." Transparency Center. Accessed October 10, 2026. https://transparency.meta.com/policies/improving/policy-forum-minutes.
- Klonick, Kate. "The New Governors: The People, Rules, and Processes Governing Online Speech." *Harvard Law Review* 131 (2018): 1598. https://harvardlawreview.org/2018/04/the-new-governors-the-people-rules-and-processes-governing-online-speech/.

**2.2 Trust & Safety Professional Association (online platforms, 2018–2020)**
- *Case:* TSPA was founded in 2020 as a 501(c)(6) professional association for "professionals who develop and enforce principles and policies that define acceptable behavior and content online". It grew out of the COMO conferences (2018–19). This is a professional body for the rule-writing role.
- *Required?* No. It predates the DSA.
- *Strength:* **Moderate to strong.** It is evidence that the role had become a recognised profession.
- *Grade:* S
- Trust & Safety Professional Association. "About TSPA." Accessed October 10, 2026. https://www.tspa.org/about-tspa/.
- Goldman, Eric. "A Pre-History of the Trust & Safety Professional Association (TSPA)." Technology & Marketing Law Blog. https://blog.ericgoldman.org/?p=21254.

**2.3 CA/Browser Forum and browser root programs (web PKI, 2005–present)**
- *Case:* CAs and browser makers formed a voluntary forum in 2005. It adopted the Baseline Requirements v1.0 in November 2011, and all public CAs must meet them, checked by annual audits that are reported to browsers. Browser root programs, such as Mozilla's module owner and peers (item 1.1), are dedicated roles for the trust rules that browsers apply automatically.
- *Required?* No government regulation is cited for publicly trusted TLS. Enforcement comes from the browsers' root programs.
- *Strength:* **Strong.**
- *Grade:* S
- "CA/Browser Forum." Wikipedia. Accessed October 10, 2026. https://en.wikipedia.org/wiki/CA/Browser_Forum.
- DigiCert. "DigiCert's Introduction to the CAB Forum." January 21, 2021. https://www.digicert.com/blog/digicerts-introduction-to-the-cab-forum.

**2.4 Coalition for Better Ads and Chrome's ad filter (ad tech, 2016–2019)**
- *Case:* An industry coalition published the Better Ads Standards in March 2017. Chrome began filtering ads automatically on non-compliant sites on 15 February 2018 and extended this worldwide in July 2019. The coalition "writes no code and serves no ads". Enforcement is done by browsers.
- *Required?* No.
- *Strength:* **Strong.** It is a dedicated body whose rules are enforced by an automated system. Caveat: it was partly a response to ad-blocking and to fears of regulation, and Google is both a member and the enforcer.
- *Grade:* S
- News/Media Alliance. "Better Ad Standards to Be Enforced by Google, Coalition." https://www.newsmediaalliance.org/alliance-better-ads-launch/.
- Chromium Blog. "Building a Better World Wide Web." January 2019. https://blog.chromium.org/2019/01/building-better-world-wide-web.html.

**2.5 IAB Tech Lab and the OpenRTB consortium (programmatic advertising, 2010–present)**
- *Case:* The OpenRTB Consortium formed in November 2010 to specify how automated auctions behave. IAB Tech Lab was founded in 2014, and ads.txt followed in 2017 as an anti-fraud rule. By 2023 Tech Lab had more than 1,000 member companies and more than 23 working groups.
- *Required?* No.
- *Strength:* **Moderate.** It sets protocols and signals, and describes itself as not providing "industry governance or policy counsel".
- *Grade:* S
- IAB Tech Lab. "IAB Tech Lab Roadmap," May 2023. https://iabcanada.com/wp-content/uploads/2023/06/IAB-Tech-Lab_Roadmap-May-2023.pdf.
- IAB. *OpenRTB API Specification Version 2.5.* November 2016. https://www.iab.com/wp-content/uploads/2016/03/OpenRTB-API-Specification-Version-2-5-FINAL.pdf.

**2.6 Wikipedia's Bot Approvals Group and edit filter managers (online community, 2004–present)**
- *Case:* The BAG, founded around 2004, must approve a bot's purpose and implementation before it runs, with trial periods. It approved HagermanBot in 2006, which proved controversial. Edit filter managers are a separate permission-holding role (item 1.3).
- *Required?* No.
- *Strength:* **Strong** for non-commercial settings.
- *Grade:* S
- Geiger, R. Stuart. "The Lives of Bots." arXiv:1810.09590, 2018. Also in *Wikipedia @ 20* (MIT Press, 2020). https://arxiv.org/abs/1810.09590.
- Dalgali, Ali, and Kevin Crowston. Paper on Wikipedia bots and the Bot Approvals Group, prepared for HICSS (c. 2019). Syracuse University. https://genres.syr.edu/sites/default/files/HICSS_WikipediaPaper_3.9.new%20kc%20%282%29.pdf. **Note:** the search summary gave only the authors, the venue and the BAG details, not the title. Confirm the title before citing.

**2.7 E-commerce fraud rule teams and the Merchant Risk Council (online retail, 2000–present)**
- *Case:* Merchant fraud professionals formed the MRC in 2000 as a nonprofit. Large merchants have dedicated fraud rules programs; for example, a Walmart senior manager "owns the end-to-end fraud rules program", including governance.
- *Required?* Merchant fraud rules are not directly regulated. PCI DSS covers data security, and card-network chargeback rules are private ordering.
- *Strength:* **Moderate.** Card-network rules act as private regulation.
- *Grade:* S
- Merchant Risk Council. "About the MRC." Accessed October 10, 2026. https://merchantriskcouncil.org/who-we-are.
- Walmart. "Senior Manager, Business Analysis and Insights, Risk Analytics, Fraud Rules" (R-2415481). https://careers.walmart.com/us/en/jobs/R-2415481.

**2.8 Airline yield and revenue management units after deregulation (airlines, 1978–1990s)**
- *Case:* After US deregulation, American Airlines set up yield management, a name coined by Robert Crandall, together with the DINAMO system. The work came from American Airlines Decision Technologies and won the 1991 Edelman award. Revenue management analysts now set the inventory controls and business rules that the RM system applies.
- *Required?* No. Fare regulation was removed in 1978.
- *Strength:* **Moderate.** Sources confirm a dedicated unit and practice, but not a "department" by that name. One source notes that GDSs, not only deregulation, drove the change.
- *Grade:* S
- Smith, Barry C., John F. Leimkuhler, and Ross M. Darrow. "Yield Management at American Airlines." *Interfaces* 22, no. 1 (1992): 8–31. https://pubsonline.informs.org/doi/fpi/10.1287/inte.22.1.8.
- "Yield Management." Wikipedia. Accessed October 10, 2026. https://en.wikipedia.org/wiki/Yield_management.

**2.9 Google search quality launch process (web search, 2000s–2012+)**
- *Case:* Ranking changes require launch reports, sometimes more than 25 pages, and a search quality meeting where experts weigh relevance, spam, latency and cost. No revenue measure is used.
- *Required?* No.
- *Strength:* **Moderate.**
- *Grade:* S
- Singhal, Amit. "Video: Search Quality Meeting, Uncut." Inside Search (Google), March 2012. https://search.googleblog.com/2012/03/video-search-quality-meeting-uncut.html.

**2.10 Riot Games player behaviour team (online games, c. 2011–2015)**
- *Case:* Riot staffed a dedicated team of statisticians, psychologists and designers, led by the "lead designer of social systems". It ran the Tribunal and later machine-learning penalty systems.
- *Required?* No.
- *Strength:* **Moderate to weak.** It is a single firm, and the system was partly community-voted.
- *Grade:* S
- SiliconANGLE. "How League of Legends Fights Player Abuse with Machine Learning." July 9, 2015. https://siliconangle.com/2015/07/09/how-league-of-legends-fights-player-abuse-with-machine-learning/.

**Possible but unverified: hospital CDS committees.** These are widespread (see "Evidence that supports Claim 1"), and most CDS is lightly regulated as a medical device. I did not find a source saying whether accreditors or Meaningful Use required the committees, so this is not counted.

**Not a clean counter-example: the Freddie Mac "Enterprise Rule Steward".** The role existed, but in a regulated GSE. Source: https://bpminstitute.org/resources/articles/towards-business-rule-stewardship-and-governance.

### Verdict on Claim 2
I found **eight or nine credible counter-examples** (items 2.1 to 2.9), and four of them are strong:
- platform policy teams and Facebook's forum,
- the CA/Browser Forum and browser root programs,
- the Coalition for Better Ads,
- Wikipedia's BAG.

All are graded S. **The claim does not survive as stated.** Lightly regulated, heavily automated sectors repeatedly created dedicated roles (policy managers, root store managers, fraud strategy, revenue management) and dedicated bodies (policy forums, industry standards bodies, approval groups).

A narrower version might hold. In several cases the trigger was something other than regulation:
- a dominant gatekeeper's private ordering (browsers, card networks, Google),
- reputational crisis,
- the threat of regulation (ad-blocking and EU pressure, political pressure on platforms).

The useful reframing is therefore that *some* binding external pressure, not necessarily regulation, preceded the dedicated roles. Testing that would need cases where no such pressure existed, and this search did not look for them.
