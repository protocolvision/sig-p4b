# E-commerce and logistics: fact sheet

Scope: warehouse automation, automated pricing, fulfilment.
Compiled 2026-10-10. Facts only; no scores, rankings or cross-industry comparisons.

Grades: P = primary source opened; R = reputable secondary opened; S = search-result summary only (the page itself was not opened). In this run, page fetching was blocked (DNS failures), so every fact is graded S.

## D1 Autonomy and speed

Amazon deployed its millionth mobile robot in June 2025, at a fulfilment centre in Japan. It says robots assist in about 75% of its customer orders across more than 300 facilities [1][2] (S). The same year it announced DeepFleet, a generative AI foundation model that coordinates robot movements across its network, which Amazon says should cut robot travel time by 10% [1][2] (S). A Profitero analysis found Amazon changing prices more than 2.5 million times a day. By comparison, Walmart and Best Buy each changed prices about 50,000 times in the whole month of November [3] (S). A 360pi analysis estimated Amazon changed prices on 15–18% of its assortment each day in March 2014, and more than 3 million times a day around Black Friday 2013 [4] (S). Documents filed in an NLRB case and reported in April 2019 said Amazon's system "automatically generates any warnings or terminations regarding quality or productivity without input from supervisors". Amazon said no worker is terminated without first meeting a supervisor [5][6] (S).

## D2 Can a single automated action move money, bind a contract or harm third parties

In April 2011, biologist Michael Eisen found the out-of-print book *The Making of a Fly* listed on Amazon at $23,698,655.93. Two sellers' repricing algorithms were raising prices against each other: once a day, profnath set its price to 0.9983 times bordeebook's, and bordeebook then repriced above profnath. The price fell back to about $106 to $135 on 19 April [7][8][9] (S). The FTC and 17 states sued Amazon in September 2023. The partly unsealed complaint alleges that "Project Nessie", a pricing algorithm developed in 2010, raised prices on and off Amazon by predicting which rivals would follow its increases, bringing in more than $1 billion. Amazon says the tool was "grossly mischaracterized" and was stopped several years earlier. On 7 October 2024, the court denied Amazon's motion to dismiss the federal claims [10][11][12] (S). On 6 April 2015, the U.S. Department of Justice charged David Topkins with conspiring to fix prices of posters sold on Amazon Marketplace from about September 2013 to January 2014. He had written pricing-algorithm code to coordinate prices. He pleaded guilty and agreed to a $20,000 fine. DOJ called it its first criminal prosecution of a conspiracy targeting e-commerce [13][14] (S).

## D3 How rules constraining automated actors are encoded

Amazon's Selling Partner API (SP-API) requires sellers to set per-SKU price guardrails (`minimum_seller_allowed_price` and `maximum_seller_allowed_price`) before linking a SKU to an automated pricing rule. Each SKU can carry only one pricing rule at a time [15] (S). ISO 3691-4:2023 sets safety requirements and verification for driverless industrial trucks and their systems; its draft revision names AGVs, autonomous mobile robots and "bots" in its scope [16] (S). It is sold in the U.S. as a package with ANSI/RIA R15.08-1 (industrial mobile robots) and ANSI/ITSDF B56.5 [17] (S). A secondary summary says ISO 3691-4 refers to ISO 13849-1 for the reliability of safety-related control functions and to IEC 61496 for safety laser scanners and similar equipment [18] (S). California AB 701 bans quotas that keep workers from taking rest or bathroom breaks or from complying with health and safety laws [19][20] (S).

## D4 Regulator, accreditor or insurer requirements on system behaviour and change

Rules on how warehouse automation and automated pricing behave:

- **EU Machinery Regulation (EU) 2023/1230:** most rules apply from 20 January 2027. It requires third-party conformity assessment for safety components, and for embedded systems, whose fully or partially self-evolving behaviour uses machine learning to provide safety functions [21][22] (S).
- **California AB 701 (signed 22 September 2021, effective 1 January 2022):** applies to employers with 100 or more employees at one warehouse distribution centre, or 1,000 or more across centres in the state. They must give each worker a written description of each quota and of any adverse action for missing it [19][20] (S).
- **New York Warehouse Worker Protection Act (signed 21 December 2022):** regulates warehouse quotas; its terms were not found in the searches [23] (S).
- **Antitrust law applied to pricing algorithms:** the Sherman Act in the Topkins prosecution (2015) [13] and FTC Act Section 5 in the Nessie claims (2023–2024) [12] (S).

## D5 Does changing a rule involve several functions

The searches did not find a primary or secondary source describing which functions approve a change to a pricing algorithm, a warehouse quota, or robot behaviour inside a retailer or logistics operator (not found). Related facts: Amazon's SP-API places the price floor and ceiling under the seller's control for each SKU [15] (S). AB 701 requires that the quota description given to workers state the number of tasks and the time period [19] (S). Under the EU Machinery Regulation, a notified body outside the manufacturer must assess machine-learning safety components [21][22] (S). Amazon has stated that supervisors can override automated productivity terminations [5] (S).

## D6 Does a licensed profession own the consequential decision

OSHA's powered industrial truck standard (29 CFR 1910.178(l), 1998 rule) requires employers to train forklift operators, certify that training, and evaluate each operator at least once every three years. Refresher training is required after an accident or near miss, observed unsafe operation, or a change of truck type or workplace conditions [24][25] (S). Industry guidance notes that there is no government-issued "OSHA forklift licence": certification is an employer record [26] (S). The searches found no licensed profession that owns automated pricing or warehouse robot decisions (not found).

## D7 Are overrides, exceptions and near misses recorded and reviewed as data

Employers record workplace injuries for OSHA. A December 2024 Senate HELP Committee report (led by Senator Sanders), based on an 18-month investigation, found that Amazon warehouses recorded more than 30% more injuries than the warehousing industry average in 2023. It also alleged that Amazon manipulated injury data to make its warehouses look safer. Amazon disputes this, saying OSHA found only minor clerical errors [27][28] (S). Amazon reported that in 2022 recordable injuries were 15% lower, and lost-time incidents 18% lower, at robotic sites than at non-robotic sites. Its 2022 safety report said 55% of recordable injuries were work-related musculoskeletal disorders [29][30] (S). Under OSHA 1910.178(l), a near-miss incident involving a forklift operator triggers refresher training [24] (S). The searches did not find a programme that records overrides of automated pricing or robot-control decisions as data (not found).

## D8 How long the automation has been in widespread use

Kiva Systems was founded in 2003 (as Distrobot, renamed in 2005) [31][32] (S). Staples was its first customer, installing a system in a Pennsylvania distribution centre in 2006 and a second in Colorado in 2007 [32] (S). Before Amazon bought Kiva in 2012 for $775 million, its clients included Staples, Gap, Walgreens, Zappos and Diapers.com; Kiva later became Amazon Robotics [1][33][34] (S). Amazon reached one million deployed robots in June 2025 [1][2] (S). The FTC complaint dates Amazon's Project Nessie pricing algorithm to 2010 [10] (S). Algorithmic repricing between Marketplace sellers was visible by April 2011 [7] (S). The searches did not find the history of automated storage and retrieval systems before Kiva (not found).

## Sources

1. The Robot Report. "Amazon Launches New AI Foundation Model, Deploys 1 Millionth Robot." 2025. https://www.therobotreport.com/amazon-launches-new-ai-foundation-model-deploys-1-millionth-robot/.
2. Automated Warehouse. "Amazon Deploys 1 Millionth Robot, Launches New AI Foundation Model." 2025. https://www.automatedwarehouseonline.com/amazon-deploys-million-robots-launches-new-ai-foundation-model/.
3. Quartz. "Amazon Changes Its Prices More than 2.5 Million Times a Day." https://qz.com/157828/amazon-changes-its-prices-more-than-2-5-million-times-a-day.
4. Retail Customer Experience. "Three Things You Need to Know about Amazon's Price Strategy." https://www.retailcustomerexperience.com/articles/three-things-you-need-to-know-about-amazons-price-strategy/.
5. CBS News. "Amazon under Fire for Software That Recommends Firing Workers." 2019. https://cbsnews.com/news/amazon-under-fire-for-software-that-recommends-firing-workers.
6. Technical.ly. "Report: Amazon Fired 300 Baltimore Fulfillment Center Employees in a Year over Productivity." 2019. https://technical.ly/startups/report-amazon-fired-300-baltimore-fulfillment-center-employees-in-a-year-over-productivity.md.
7. Techdirt. "The Infinite Loop of Algorithmic Pricing on Amazon... or How a Book on Flies Cost $23,698,655.93." April 25, 2011. https://archive.techdirt.com/articles/20110425/03522114026/infinite-loop-algorithmic-pricing-amazon-how-book-flies-cost-2369865593.shtml.
8. The Register. "Amazon Pricing Algorithms." April 26, 2011. https://www.theregister.com/2011/04/26/amazon_pricing_algorithms/.
9. Wikipedia. "The Making of a Fly." https://en.wikipedia.org/wiki/The_Making_of_a_Fly.
10. PYMNTS. "FTC Alleges Amazon Deployed Secret Algorithm to Raise Prices." 2023. https://www.pymnts.com/legal/2023/ftc-alleges-amazon-deployed-secret-algorithm-to-raise-prices/.
11. GeekWire. "FTC vs. Amazon Filing Reveals More Claims about Jeff Bezos' Alleged Role, Project Nessie and More." 2023. https://www.geekwire.com/2023/ftc-vs-amazon-filing-reveals-more-claims-about-jeff-bezos-alleged-role-project-nessie-and-more/.
12. BCLP. "The FTC and State Case against Amazon Highlights Risks and Impacts from Using Pricing Algorithms." https://www.bclplaw.com/en-US/insights/the-ftc-and-state-case-against-amazon-highlights-risks-and-impacts-from-using-pricing-algorithms.html.
13. U.S. Department of Justice, Antitrust Division. Press release on Topkins prosecution, April 6, 2015. https://www.justice.gov/atr/public/press_releases/2015/313011.htm.
14. Mondaq. "First E-Commerce Price-Fixing Prosecution Yields Swift Guilty Plea." 2015. https://mondaq.com/unitedstates/trade-regulation-practices/390624/first-e-commerce-price-fixing-prosecution-yields-swift-guilty-plea.
15. Amazon. "Manage Automated Pricing Rules with SP-API." Selling Partner API documentation. https://developer-docs.amazon.com/sp-api/docs/manage-automated-pricing-rules.
16. International Organization for Standardization. "ISO 3691-4" catalogue page (ISO/DIS revision, ref. 88615). https://www.iso.org/es/contents/data/standard/08/86/88615.html.
17. ANSI Webstore. "ISO 3691-4 / ANSI/RIA R15.08-1 / ANSI/ITSDF B56.5" package. https://webstore.ansi.org/standards/iso/iso3691ansiriar1508itsdfb56.
18. Fabrico. "ISO 3691-4 Driverless Industrial Trucks." Blog. https://www.fabrico.io/blog/iso-3691-4-driverless-industrial-trucks/.
19. Norton Rose Fulbright. "New California Law to Regulate Productivity Quotas at Large Warehouse Distribution Centers." 2021. https://www.nortonrosefulbright.com/de-de/wissen/publications/f77dd228/new-california-law-to-regulate-productivity-quotas-at-large-warehouse-distribution-centers.
20. Fisher Phillips. "California Employers with Warehouse Distribution Centers Face First-in-Nation Law Regulating Production Quotas." 2021. https://www.fisherphillips.com/print/v2/content/27237/california-employers-with-warehouse-distribution-centers-face-first-in-nation-law-regulating-production-quotas.pdf.
21. European Parliament, Legislative Observatory. "Regulation on Machinery Products." Document summary. https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1749182.
22. Baker McKenzie. "Machinery Regulation." *Global Compliance News*, December 2024. https://www.globalcompliancenews.com/wp-content/uploads/sites/43/2024/12/Baker-McKenzie-Machinery-Regulation.pdf.
23. JD Supra. "Distribution Centers: New Legislation." Topic page. https://www.jdsupra.com/topics/distribution-centers/new-legislation/.
24. Occupational Safety and Health Administration. "Powered Industrial Trucks (Forklift) eTool: Training Assistance." https://www.osha.gov/etools/powered-industrial-trucks/training.
25. Occupational Safety and Health Administration. "Powered Industrial Truck Operator Training." Final rule, *Federal Register*, December 1, 1998. https://www.osha.gov/sites/default/files/laws-regs/federalregister/1998-12-01-1.pdf.
26. Heavy Vehicle Inspection. "OSHA Forklift Certification Requirements: Training & Evaluation." https://heavyvehicleinspection.com/blog/post/osha-forklift-certification-requirements-training.
27. U.S. Senate Committee on Health, Education, Labor and Pensions. "Sanders Releases Sweeping Report Exposing How Amazon's Obsession with Speed Injures Workers at Unprecedented Rates." December 2024. https://www.help.senate.gov/dem/newsroom/press/news-sanders-releases-sweeping-report-exposing-how-amazons-obsession-with-speed-injures-workers-at-unprecedented-rates.
28. NPR. "Amazon Manipulated Injury Data to Make Warehouses Appear Safer, a Senate Probe Finds." December 16, 2024. https://www.npr.org/2024/12/16/nx-s1-5230240/amazon-injury-warehouse-senate-investigation.
29. GeekWire. "New Robots Are Making Amazon's Warehouses More Efficient. Can They Also Make Them Safer?" 2023. https://www.geekwire.com/2023/new-robots-are-making-amazons-warehouses-more-efficient-can-they-also-make-them-safer/.
30. Retail Brew. "Amazon Says New Robots Will Improve Safety. Critics Aren't So Sure." October 31, 2023. https://www.retailbrew.com/stories/2023/10/31/amazon-says-new-robots-will-improve-safety-critics-aren-t-so-sure.
31. NPR. "Mick Mountz, Founder of Kiva Systems." June 28, 2013. https://www.npr.org/2013/06/28/196630096/mick-mountz-founder-of-kiva-systems.
32. The Robot Report. "Kiva Systems Creators Inducted into National Inventors Hall of Fame." https://www.therobotreport.com/kiva-systems-creators-inducted-into-national-inventors-hall-of-fame-2/.
33. SingularityHub. "Amazon Goes Robotic, Acquires Kiva Systems, Makers of the Warehouse Robot." March 21, 2012. https://singularityhub.com/2012/03/21/amazon-goes-robotic-acquires-kiva-systems-makers-of-the-warehouse-robot.
34. Dealroom. "Kiva Systems." https://app.dealroom.co/companies/kiva_systems.
