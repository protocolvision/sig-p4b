# Insurance: fact sheet

Scope: automated underwriting and claims.
Compiled 2026-10-10. Facts only; no scores, rankings or cross-industry comparisons.

Grades: P = primary source opened; R = reputable secondary opened; S = search-result summary only (the page itself was not opened). In this run, page fetching was blocked (DNS failures), so every fact is graded S.

## D1 Autonomy and speed

Gen Re's 2025 survey of U.S. individual life insurers estimated that about 12% of 2024 applications went through fully automated decisioning. Another 47% went through accelerated but not fully automated underwriting, and 41% through traditional underwriting. Eligibility for an accelerated path ranged from 15% to 100% by company [1][2] (S). PartnerRe's 2024 survey reported accelerated underwriting turnaround of 8 days on average, against 28 days for full underwriting [3] (S). Gen Re's 2024 group medical survey found that 81% of participating companies had an evidence-of-insurability system that can approve coverage without a medical underwriter's review [4] (S). In June 2023, Lemonade said its claims bot "AI Jim" settled a UK bike-theft claim in two seconds. In that time it checked policy conditions, ran anti-fraud algorithms, approved the claim, sent bank payment instructions and told the customer. This is a company-announced record [5][6] (S). For health claims, vendor and case-study sources report auto-adjudication rates of about 48% to 84% at individual payers and administrators, with a stated industry benchmark of 95%. These figures are not independently verified [7][8] (S).

## D2 Can a single automated action move money, bind a contract or harm third parties

Lemonade's AI Jim approves claims and sends payment instructions to the bank without a person approving each payment [5][6] (S). Cigna has said its PXDX system automatically pays provider claims submitted with the correct diagnosis codes. ProPublica reported that Cigna medical directors used the system to deny more than 300,000 claims over two months in 2022, averaging 1.2 seconds per claim. Cigna called the report "riddled with factual errors" and said PXDX uses no AI or machine learning [9][10] (S). A class action filed 14 November 2023 in the U.S. District Court for Minnesota alleges that UnitedHealth's naviHealth unit used the nH Predict model to cut off post-acute care for Medicare Advantage members. It alleges a 90% error rate, measured by denials reversed on appeal, and says only 0.2% of members appeal. UnitedHealth says the tool is a guide and is not used for coverage decisions, and that the suit has no merit [11][12] (S).

## D3 How rules constraining automated actors are encoded

Pricing rules are written into filed rate manuals. California requires every prior-approval property and casualty rate application to include a complete rate manual with all current rates, rating factors and rating rules. Filings go electronically through the NAIC's SERFF system [13] (S). New Jersey (N.J.A.C. 11:3-16.6) requires spreadsheet values in filings to be given as formulas, plus proposed manual rate and rule pages [13] (S). Under South Carolina's prior-approval system, rates may not be used until the Department approves them [13] (S). Celent describes a second generation of life-insurance automated underwriting engines that added user interfaces, exposed rules and override capability for human underwriters [14] (S). Lemonade describes routing in which AI Jim either pays a claim instantly or passes it to a human claims handler [6] (S).

## D4 Regulator, accreditor or insurer requirements on system behaviour and change

Requirements on how automated underwriting, pricing and claims systems behave and change:

- **NAIC Model Bulletin: Use of Artificial Intelligence Systems by Insurers (adopted 4 December 2023):** expects insurers to keep a documented AI Systems (AIS) Program to manage the risk of inaccurate or unfairly discriminatory decisions. It is guidance for state regulators, not a model law. 24 states had adopted it by March 2025 [15][16][17] (S).
- **Colorado SB21-169 (signed July 2021):** covers insurers' use of external consumer data, algorithms and predictive models that lead to unfair discrimination [18][19] (S).
- **Colorado Regulation 10-1-1 (adopted 21 September 2023):** sets governance and risk-management framework requirements for life insurers. A draft quantitative-testing regulation was released on 27 September 2023 [18][19] (S).
- **California SB 1120 (signed September 2024, effective 1 January 2025):** bars AI tools from denying, delaying or modifying care based on medical necessity. Decisions must rest on the individual patient's records, not solely on a group dataset [20][21] (S).
- **EU AI Act Annex III point 5:** treats AI for risk assessment and pricing of natural persons in life and health insurance as high-risk. Sources report that a 2026 Digital Omnibus moved the Annex III deadline from 2 August 2026 to 2 December 2027; not confirmed against the Official Journal [22][23] (S).

## D5 Does changing a rule involve several functions

Law-firm summaries of the NAIC Model Bulletin say it expects an AI governance structure that draws on several units: business units, product specialists, actuarial, data science and analytics, underwriting, claims, compliance and legal. Each has defined responsibilities and reporting lines, and the structure is accountable to senior management and the board [24][25][26] (S). One summary notes that this committee language was described from the draft bulletin [27] (S). A change to a filed rating system crosses into the regulator. New Jersey requires a cover letter, a description of the changes, compliance calculations and proposed manual pages for changes that need approval. Massachusetts requires actuarial support for rate and rule changes [13] (S). Under Colorado's SB21-169 framework, insurers must show that their models do not discriminate unfairly. A vendor source gives deadlines of 1 June 2024 for progress reports and 1 December 2024 for that showing [18][28] (S).

## D6 Does a licensed profession own the consequential decision

California SB 1120 (2024) requires medical-necessity determinations in utilisation review to be made by a licensed physician or a licensed healthcare professional, not by an AI tool [20][21] (S). ProPublica's 2023 reporting notes that many states require medical directors to review patient files before denying claims for medical reasons [9] (S). A 2018 Carrier Management article reported that 34 states required independent adjusters to be licensed and 15 required staff adjusters to be. A later AgentSync piece gives 16 states for staff adjusters [29][30] (S). The Actuarial Standards Board's ASOP No. 56 (Modeling), effective for work on or after 1 October 2020, applies to actuaries who design, develop, select, modify, use or review models. That includes actuaries using models built by others when they are responsible for the output [31][32] (S). The searches did not establish whether a credentialed actuary must sign rate filings (not found).

## D7 Are overrides, exceptions and near misses recorded and reviewed as data

State market-conduct examinations test claims handling against NAIC unfair-claims model acts by sampling claim files. A Maine examination of Hartford Life and Accident reviewed 55 long-term-disability claim files. A North Carolina examination of USAA entities used a 3% error tolerance for claims and 0% for unlicensed adjusters [33][34] (S). Appeal outcomes are used as evidence of model error: the nH Predict complaint bases its 90% figure on denials reversed through internal appeals or administrative law judge rulings [11] (S). A compliance vendor reports that the NAIC's AI examination tool, renamed the AI Risk Evaluation Supplement, was piloted with 12 states in March 2026 [26] (S). The searches did not find a programme that records underwriter or adjuster overrides of automated decisions as data (not found).

## D8 How long the automation has been in widespread use

A chief underwriter at iA Financial Group says the industry has discussed automating underwriting since the 1980s, with early rules-based engines in the 1990s [35] (S). Celent describes "expert" underwriting engines from about 25 years before its article that needed programming to write rules and failed to take hold. A later generation added interfaces and overrides but was limited by cost and underwriter distrust [14] (S). Munich Re's 2022 survey dates the earliest accelerated underwriting programmes to 2012. The Society of Actuaries' *Risk Management* newsletter dates accelerated underwriting to the early 2000s [36][37] (S). Industry reporting says the COVID-19 pandemic sped up adoption of fluidless and accelerated underwriting [35] (S). Cigna has said PXDX technology is more than a decade old [10] (S).

## Sources

1. Gen Re. "From AU to Next Gen: Understanding the Latest Underwriting Trends." July 2025. https://www.genre.com/us/knowledge/publications/2025/july/from-au-to-next-gen-understanding-the-latest-underwriting-trends-en.
2. Insurance Business. "Life Insurers Widen Accelerated Underwriting – Gen Re." https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/life-insurers-widen-accelerated-underwriting--gen-re-560575.aspx.
3. PartnerRe. "Accelerated Underwriting Survey." White paper, October 2024. https://www.partnerre.com/wp-content/uploads/2024/10/PartnerREWhitepaper_AUWSurvey_Final-1.pdf.
4. Insurance Business. "Automation Surges in US Group Medical Underwriting – Gen Re." https://www.insurancebusinessmag.com/reinsurance/news/breaking-news/automation-surges-in-us-group-medical-underwriting--gen-re-554546.aspx.
5. Insurance Times. "How AI Helped an Insurtech Pay Out a UK Claim in Just Two Seconds." 2023. https://insurancetimes.co.uk/news/how-ai-helped-an-insurtech-pay-out-a-uk-claim-in-just-two-seconds/1444812.article.
6. Insurtech Digital. "Speeding Up Claims: Lemonade Hails 2-Second Insurance Payout." 2023. https://insurtechdigital.com/articles/speeding-up-claims-lemonade-hails-2-second-insurance-payout.
7. CitiusTech. "AI/ML & Automation." Case study, 2024. https://www.citiustech.com/hubfs/citiustech-2024/market/providers/intelligence-automation/case-studies/AIML%20%26%20Automation.pdf.
8. Fuse Insight. "The Full Claims Automation Myth." https://www.fuseinsight.com/blog/full-claims-automation-myth/.
9. Becker's Payer Issues. "Cigna Physicians Deny Claims en Masse without Reading Them: ProPublica Report." 2023. https://www.beckerspayer.com/payer/home-page/cigna-physicians-deny-claims-en-masse-without-reading-them-propublica-report.html.
10. Becker's Payer Issues. "Cigna Hits Back on ProPublica Report 'Riddled with Factual Errors.'" 2023. https://www.beckerspayer.com/?p=10624.
11. STAT News. Reporting on UnitedHealth nH Predict lawsuit. November 2023. https://www.statnews.com/?p=1089881.
12. TechSpot. "UnitedHealthcare Legal Battle over AI Denials of Critical Medical Care." 2023. https://www.techspot.com/news/100895-unitedhealthcare-legal-battle-over-ai-denials-critical-medical.html.
13. California Department of Insurance. "Prior Approval Rate Filing Instructions." Edition June 2, 2025. https://www.insurance.ca.gov/0250-insurers/0800-rate-filings/0200-prior-approval-factors/upload/PriorAppRateFilingInstr_Ed06-02-2025.pdf. Also: N.J.A.C. 11:3-16.6, https://regulations.justia.com/states/new-jersey/title-11/chapter-3/subchapter-16/section-11-3-16-6/; South Carolina Department of Insurance, Bulletin 2006-09, https://online.doi.sc.gov/Eng/Public/Bulletins/Bulletin2006-09.pdf; Massachusetts, "Motor Vehicle Rate/Rule Filings," https://www.mass.gov/doc/motor-vehicle-raterule-filings-word/download.
14. Celent. "Life Insurance Automated Underwriting – A 25 Year Journey." https://celent.com/insights/571780504.
15. National Association of Insurance Commissioners. "NAIC Model Bulletin: Use of Artificial Intelligence Systems by Insurers." https://content.naic.org/sites/default/files/inline-files/AI%20Model%20Bulletin%20-%20April%202024.pdf.
16. Quarles. "Nearly Half of States Have Now Adopted NAIC Model Bulletin on Insurers' Use of AI." 2025. https://quarles.com/newsroom/publications/nearly-half-of-states-have-now-adopted-naic-model-bulletin-on-insurers-use-of-ai.
17. Holland & Knight. "The Implications and Scope of the NAIC Model Bulletin." May 2025. https://www.hklaw.com/en/insights/publications/2025/05/the-implications-and-scope-of-the-naic-model-bulletin.
18. Locke Lord. "QuickStudy: Colorado Exposes Draft Life Insurance [Quantitative Testing Regulation]." October 2023. https://lockelord.com/newsandevents/publications/2023/10/quickstudy-colorado-exposes-draft-life-insurance.
19. Milliman. "Protecting Consumers: Colorado's Antidiscrimination Law and Insurance." March 2024. https://www.milliman.com/en/insight/protecting-consumers-colorado-antidiscrimination-law-insurance.
20. California State Senate, District 13. "Landmark Law Prohibits Health Insurance Companies from Using AI to Deny Healthcare Coverage." December 9, 2024. https://sd13.senate.ca.gov/news/press-release/december-9-2024/landmark-law-prohibits-health-insurance-companies-using-ai-to.
21. Law360. "A Look at Calif.'s New AI Law for Health Insurers." https://www.law360.com/articles/1888226/a-look-at-calif-s-new-ai-law-for-health-insurers.
22. actuary.info. "EU AI Act High-Risk Insurance Underwriting August 2026." https://actuary.info/insights/eu-ai-act-high-risk-insurance-underwriting-august-2026.
23. actuary.info. "EU AI Act August 2026: Carrier High-Risk Compliance Gaps." https://actuary.info/insights/eu-ai-act-august-2026-carrier-high-risk-compliance-gaps.
24. Quarles. "States Adopt NAIC Model Bulletin on Insurers' Use of AI." https://www.quarles.com/newsroom/publications/states-adopt-naic-model-bulletin-on-insurers-use-of-ai.
25. Debevoise. "Insurance Industry Corporate Governance Newsletter." November 2023. https://www.debevoise.com/insights/publications/2023/11/insurance-industry-corporate-governance-newsletter.
26. Optro. "NAIC AI Model Bulletin." https://optro.ai/blog/naic-ai-model-bulletin.
27. Carlton Fields. "NAIC Innovation, Cybersecurity, and Technology." *Expect Focus*, 2023. https://carltonfields.com/insights/expect-focus/2023/naic-innovation-cybersecurity-and-technology.
28. Credo AI. "Colorado SB21-169: 8 Things You Need to Know about Colorado's New AI Insurance Regulation." January 2024. https://www.credo.ai/blog/colorado-sb21-169-8-things-you-need-to-know-about-colorados-new-ai-insurance-regulation.
29. Carrier Management. Article on adjuster licensing. June 20, 2018. https://carriermanagement.com/news/2018/06/20/180788.htm.
30. AgentSync. "The 7-Step Challenge of Life and Health Adjuster Licensing and 4 Ways to Make Compliance Easier." https://agentsync.io/blog/compliance/the-7-step-challenge-of-life-and-health-adjuster-licensing-and-4-ways-to-make-compliance-easier.
31. Actuarial Standards Board. "ASB Adopts ASOP No. 56." December 2019. https://www.actuarialstandardsboard.org/asb-adopts-asop-no-56/.
32. Casualty Actuarial Society. "Actuarial Standards Board Adopts ASOP No. 56." https://casact.org/article/actuarial-standards-board-adopts-asop-no-56.
33. Maine Bureau of Insurance. Market conduct examination report, Hartford Life and Accident, 2011. https://www11.maine.gov/pfr/insurance/themes/insurance/pdf/exam_rpts/2011/hartfordLife_accident_mcreport_2011.pdf.
34. North Carolina Department of Insurance. Market conduct examination report, USAA Casualty, 2019. https://ncdoi.gov/documents/market-regulations/usaa-casualty-report-2019/open.
35. Advisor.ca. "Pandemic Sped Up Life Underwriting, Prepared the Industry for AI." https://www.advisor.ca/insurance/pandemic-sped-up-life-underwriting-prepared-the-industry-for-ai/.
36. Munich Re. "A Decade into Accelerated Underwriting." 2022 Accelerated Underwriting Survey. https://www.munichre.com/us-life/en/insights/future-of-risk/2022-Accelerated-Underwriting-Survey.html.
37. Society of Actuaries. *Risk Management* newsletter, issue 44, May 2019. https://www.soa.org/4a0987/globalassets/assets/library/newsletters/risk-management-newsletter/2019/may/rm-2019-iss-44-morant.pdf.
