# Algorithmic trading: fact sheet

Scope: electronic and algorithmic trading, market access controls.
Compiled 2026-10-10. Facts only; no scores, rankings or cross-industry comparisons.

Grades: P = primary source opened; R = reputable secondary opened; S = search-result summary only (the page itself was not opened). In this run, page fetching was blocked (DNS failures on sec.gov and legislation.gov.uk), so every fact is graded S. Numbers marked as estimates are estimates in the source.

## D1 Autonomy and speed

A 2016 Congressional Research Service overview cites estimates that high-frequency trading made up roughly 55% of U.S. equity volume and about 40% of European equity volume. It also notes that neither the SEC nor the CFTC has a legal definition of HFT [1] (S). A 2010 SEC proposed rule in the Federal Register cites press estimates of 60% to 73% of U.S. equity volume, and TABB Group later revised its own estimate from 73% to 70% [2][3] (S). Coalition Greenwich reports that about 37% of total 2023 institutional volume was executed through algorithms or smart order routers, up from 35% [4] (S). Vendors report that hardware pre-trade risk checks run in under 60 nanoseconds (NanoSpeed) and in 740 nanoseconds wire-to-wire (Fixnetix). These are company claims, not independent benchmarks [5][6] (S). On 1 August 2012, Knight Capital's router sent more than 4 million orders in the first 45 minutes after the open while trying to fill 212 customer orders [7][8] (S).

## D2 Can a single automated action move money, bind a contract or harm third parties

In the Knight Capital event of 1 August 2012, faulty router code produced executed trades. Knight was left with a reported pre-tax loss of about $440 million; some sources give more than $460 million. On 5 August it raised about $400 million from investors led by Jefferies to stay in business [7][9] (S). On 6 May 2010, according to the joint SEC–CFTC report released 30 September 2010, a mutual fund complex started a sell program of 75,000 E-mini S&P 500 contracts (about $4.1 billion). It ran through an automated execution algorithm set to 9% of the previous minute's volume, "without regard to price or time". The Dow fell nearly 1,000 points in under half an hour [10][11] (S). Nearly 21,000 trades from that day were later cancelled as clearly erroneous [11] (S).

## D3 How rules constraining automated actors are encoded

SEC Rule 15c3-5 (the Market Access Rule, adopted November 2010) requires broker-dealers with market access to keep automated, pre-trade controls. The controls must keep orders within pre-set credit and capital thresholds, reject erroneous orders and block orders that breach regulatory requirements. The controls must be under the broker-dealer's "direct and exclusive control", which bans unfiltered ("naked") sponsored access [12][13][14] (S). CME Group's Risk Management Tools encode these limits at the exchange: pre-execution credit limits (Credit Controls/GC2), order blocking (Risk Management Interface), and a Kill Switch. The Kill Switch blocks all new order entry and cancels all working orders at the clearing-entity, execution-firm or sender level. Optional Self-Match Prevention stops orders from accounts with common ownership from trading with each other [15][16] (S). The Limit Up–Limit Down plan was approved by the SEC on 31 May 2012 and started on 4 February 2013. It sets price bands around each stock's five-minute average price: 5% for most S&P 500 and Russell 1000 stocks, 10% for most others. When a stock cannot trade back inside its band, a five-minute pause applies across all markets [17][18] (S).

## D4 Regulator requirements on automated system behaviour and change

Rules on how automated trading systems behave and change:

- **SEC Rule 15c3-5 (2010):** pre-trade risk controls; SEC staff issued FAQs on 15 April 2014 [12][13] (S).
- **SEC Regulation SCI (adopted 19 November 2014):** covers exchanges, large alternative trading systems, clearing agencies and data processors, but not broker-dealers in general. It requires quarterly reports to the SEC on material changes to their systems, business-continuity and disaster-recovery testing, notice of systems problems, and an annual review of systems. It replaced the voluntary Automation Review Policy [19][20] (S).
- **EU Commission Delegated Regulation 2017/589 (RTS 6 under MiFID II Article 17):** requires an annual self-assessment and validation report on algorithmic systems, governance and kill functionality (Article 9). It also requires stress tests at twice the firm's six-month peak message and volume levels (Article 10) [21][22] (S).
- **FINRA Regulatory Notice 15-09 (March 2015):** guidance on supervising algorithmic strategies, covering risk assessment, software and code development and implementation, testing and system validation, trading systems, and compliance [23][24] (S).

## D5 Does changing a rule involve several functions

Under RTS 6 Article 9, three functions take part in the annual validation of algorithmic systems, which includes their governance and approval framework. The risk management function drafts the report, internal audit reviews it where one exists, and senior management approves it. The firm must then fix any deficiencies found [21] (S). FINRA Regulatory Notice 15-09 treats testing before production, separate development environments and documented test results as part of supervising code changes, with compliance as one of its five areas. A law-firm summary adds that FINRA expected its guidelines to apply even to modifications that are not significant [24][25][26] (S). The search results did not confirm whether 15-09 recommends a specific cross-functional committee (not found). In the Knight Capital order, the SEC found that the firm moved a section of router code without proper controls. It also found that the firm did not act on automated email alerts generated by the faulty code before the market opened. The order imposed a $12 million penalty and an independent consultant [7][27] (S).

## D6 Does a licensed profession own the consequential decision

FINRA Regulatory Notice 16-21 (June 2016) announced an SEC-approved (7 April 2016) amendment to NASD Rule 1032(f), effective 30 January 2017. It requires people who are mainly responsible for designing, developing or significantly modifying algorithmic trading strategies in equity, preferred or convertible debt securities to register as Securities Traders and pass the Series 57 exam. The same applies to people who supervise that work day to day [28][29] (S). Registration brings a qualification exam and continuing education [29] (S). In this framework the registered person owns the design or change of the strategy. The search results did not establish whether a registered person approves individual orders (not found).

## D7 Are overrides, exceptions and near misses recorded and reviewed as data

SEC Rule 613 (adopted July 2012; effective 1 October 2012) required the exchanges and FINRA to build the Consolidated Audit Trail. It records customer and order events from inception through routing, modification, cancellation and execution. Data is due by 8:00 a.m. ET the next trading day. When fully built, the CAT was projected to take in more than 58 billion records a day [30][31][32] (S). Regulation SCI requires SCI entities to notify the SEC of "SCI events" (systems disruptions, compliance issues and intrusions) and to report them on a scale set by severity [19][20] (S). The Dutch AFM reviewed firms' 2019 RTS 6 self-assessments, including kill functionality. It reported governance shortcomings such as insufficient information and structures that did not follow RTS 6 [22] (S). After 6 May 2010, exchanges cancelled nearly 21,000 trades as erroneous [11] (S).

## D8 How long the automation has been in widespread use

Instinet, founded in 1969, is described by the SEC Historical Society as the first electronic trading system [33][34] (S). Instinet's timeline dates Nasdaq's launch as an electronic market to 1971; this is a company-published date [34] (S). The SEC's 1996 Order Handling Rules enabled electronic communication networks (ECNs). U.S. equity quoting moved fully to decimals by April 2001, and Regulation NMS was adopted in 2005, which Instinet says drove more volume into electronic markets [33][34][35] (S). Estimates of HFT's share of U.S. equity volume were already at 60% to 73% by 2009–2010 [2][3] (S).

## Sources

1. Congressional Research Service. "High Frequency Trading: Overview of Recent Developments." CRS Report R44443, April 4, 2016. https://www.everycrsreport.com/files/20160404_R44443_b0a051ddc80e111d9c7ac5f4eb92c8eae4549e26.html.
2. U.S. Securities and Exchange Commission. Proposed rule, *Federal Register* 75 (2010): 21473. https://www.govinfo.gov/link/fr/75/21473.
3. Global Custodian. "New TABB Group Research on High-Frequency Trading." Accessed October 10, 2026. https://www.globalcustodian.com/?p=22663.
4. The TRADE. "E-trading Platforms Experienced Increased Share of US Equity Trading Volume in 2023." Accessed October 10, 2026. https://www.thetradenews.com/e-trading-platforms-experienced-increased-share-of-us-equity-trading-volume-in-2023/.
5. Finextra. "NanoSpeed Releases Latest Nano-Risk FPGA." Accessed October 10, 2026. https://www.finextra.com/pressarticle/57445/nanospeed-releases-latest-nano-risk-fpga.
6. The TRADE. "Fixnetix Claims 'World's Fastest' Pre-trade Risk Checks." Accessed October 10, 2026. https://www.thetradenews.com/fixnetix-claims-39world39s-fastest39-pre-trade-risk-checks.
7. jrvarma.in. "SEC Order Explains Knight Capital Systems Failure." Blog post, 2013. https://www.jrvarma.in/blog/Y2013/Knight-Capital.html.
8. Mondo Visione. "SEC Charges Knight Capital with Violations of Market Access Rule." October 16, 2013. https://mondovisione.com/news/sec-charges-knight-capital-with-violations-of-market-access-rule-20131016/.
9. Wikipedia. "Knight Capital Group." Accessed October 10, 2026. https://en.wikipedia.org/wiki/Knight_Capital_Group.
10. Christian Science Monitor. "'Flash Crash' Report: A Tale of How Not to Make a Big Trade." October 1, 2010. https://www.csmonitor.com/Business/2010/1001/Flash-crash-report-A-tale-of-how-not-to-make-a-big-trade.
11. PlanAdviser. "Regulators Release Flash Crash Probe Report." 2010. https://www.planadviser.com/regulators-release-flash-crash-probe-report/.
12. WilmerHale. "SEC Staff Issues First Set of FAQs on Rule 15c3-5, Risk Management Controls for Brokers or Dealers with Market Access." 2014. https://www.wilmerhale.com/en/insights/client-alerts/sec-staff-issues-first-set-of-faqs-on-rule-15c3-5-risk-management-controls-for-brokers-or-dealers-with-market-access.
13. Cadwalader. "The SEC Publishes Final Rule Regulating Access to Securities Markets." 2010. https://cadwalader.com/resources/clients-friends-memos/the-sec-publishes-final-rule-regulating-access-to-securities-markets.
14. FINRA. "Market Access Rule." *2022 Report on FINRA's Examination and Risk Monitoring Program*. https://www.finra.org/rules-guidance/guidance/reports/2022-finras-examination-and-risk-monitoring-program/market-access-rule.
15. CME Group. "Risk Management Tools." User help system. Accessed October 10, 2026. https://www.cmegroup.com/tools-information/webhelp/globex-credit-controls/Content/Risk_Mgmt_Tools.pdf.
16. CME Group. "Kill Switch." Client systems wiki. Accessed October 10, 2026. https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/46140937/Kill+Switch.
17. Harvard Law School Forum on Corporate Governance. "'Limit Up-Limit Down' Plan and Circuit Breakers Approved." June 13, 2012. https://corpgov.law.harvard.edu/2012/06/13/limit-up-limit-down-plan-and-circuit-breakers-approved/.
18. U.S. Securities and Exchange Commission. Investor bulletin on circuit breakers and LULD. https://www.sec.gov/investor/alerts/circuitbreakersbulletin.htm.
19. U.S. Securities and Exchange Commission. "Regulation Systems Compliance and Integrity." *Federal Register*, December 5, 2014. https://www.federalregister.gov/documents/2014/12/05/2014-27767/regulation-systems-compliance-and-integrity.
20. WilmerHale. "SEC Adopts Regulation Systems Compliance and Integrity." 2014. https://www.wilmerhale.com/en/insights/client-alerts/sec-adopts-regulation-systems-compliance-and-integrity.
21. Commission Delegated Regulation (EU) 2017/589 of 19 July 2016 (RTS 6). UK retained version. https://www.legislation.gov.uk/eur/2017/589.
22. Autoriteit Financiële Markten (AFM). "RTS 6 analyse 2019." https://www.afm.nl/~/profmedia/files/onderwerpen/mifid-ii/rts6-analyse-2019.pdf.
23. FINRA. "Regulatory Notice 15-09: Guidance on Effective Supervision and Control Practices for Firms Engaging in Algorithmic Trading Strategies." March 2015. https://www.finra.org/rules-guidance/notices/15-09.
24. Skadden. "FINRA Provides Guidance on Effective Supervision and Control Practices." May 2015. https://www.skadden.com/-/media/files/publications/2015/05/finraprovidesguidanceoneffectivesupervisionandcont.pdf.
25. Cahill. "SEC, FINRA Obligations in Changing AI Regulatory Landscape." *Law360*, July 2, 2025. https://www.cahill.com/publications/client-alerts/2025-07-02-ai-compliance-considerations-meeting-sec-and-finra-obligations-in-an-ever-evolving-regulatory-landscape/.
26. McDermott (mcdermottlaw.com). Commentary on FINRA algorithmic trading registration proposal. https://www.mcdermottlaw.com/?p=342015.
27. Mondo Visione. "SEC Charges Knight Capital with Violations of Market Access Rule." October 16, 2013. https://mondovisione.com/news/sec-charges-knight-capital-with-violations-of-market-access-rule-20131016/.
28. FINRA. "Regulatory Notice 16-21: SEC Approves Rule to Require Registration of Associated Persons Involved in the Design, Development or Significant Modification of Algorithmic Trading Strategies." June 2016. https://www.finra.org/rules-guidance/notices/16-21.
29. Norton Rose Fulbright. "FINRA Adopts Rule Relating to Algorithmic Trading Strategies." 2016. https://www.nortonrosefulbright.com/en/knowledge/publications/8358afa4/finra-adopts-rule-relating-to-algorithmic-trading-strategies.
30. U.S. Securities and Exchange Commission. "Consolidated Audit Trail." Release No. 34-67457, 2012. https://SEC.gov/rules/final/2012/34-67457.pdf.
31. WilmerHale. "SEC Adopts Consolidated Audit Trail Rule." July 12, 2012. https://www.wilmerhale.com/en/insights/publications/sec-adopts-consolidated-audit-trail-rule-july-12-2012.
32. CAT NMS, LLC. "CAT FINRA Press Release." February 2019. https://catnmsplan.com/wp-content/uploads/2019/02/CAT_FINRA_Press_Release_FINAL.pdf.
33. Securities and Exchange Commission Historical Society. "Increments and ECNs." Virtual museum gallery. https://www.sechistorical.org/museum/galleries/msr/msr04b_increments_ecns.php.
34. Instinet. "History." Accessed October 10, 2026. https://www.instinet.com/history.
35. Comerford, John. Testimony before the House Financial Services Committee, June 27, 2017. https://financialservices.house.gov/uploadedfiles/hhrg-115-ba16-wstate-jcomerford-20170627.pdf.
