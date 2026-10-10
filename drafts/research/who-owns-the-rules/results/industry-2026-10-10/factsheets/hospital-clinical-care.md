# Hospital clinical care: fact sheet

Scope: clinical decision support (CDS), computerised provider order entry (CPOE), alerts, credentialing, clinical protocols.
Compiled 2026-10-10. Facts only; no scores, rankings or cross-industry comparisons.

Grades: P = primary source opened; R = reputable secondary opened; S = search-result summary only (the page itself was not opened). In this run, page fetching was blocked (DNS failures), so every fact is graded S.

## D1 Autonomy and speed

Most of the automated actions in these sources are alerts, warnings and order checks shown to clinicians, not actions taken on their own. In a 2009 *Archives of Internal Medicine* study of alerts shown to 2,872 outpatient clinicians in Massachusetts, New Jersey and Pennsylvania, clinicians overrode more than 90% of drug-interaction alerts and 77% of drug-allergy alerts [1][2] (S). A later scoping review of 34 studies found drug-interaction alert override rates of 55% to 98% [3] (S). The Joint Commission FAQ on auto-verification says a blanket practice of auto-verifying selected medication types, which bypasses pharmacist review, is not acceptable. It says auto-verification can be considered only where a licensed practitioner controls ordering, preparation and administration, as in an emergency department [4] (S). Predictive models run automatically across inpatient populations. A June 2021 *JAMA Internal Medicine* external validation of the Epic Sepsis Model at Michigan Medicine covered 38,455 hospitalisations (6 December 2018 to 20 October 2019). It reported an AUC of 0.63, and the model did not flag about two-thirds of sepsis patients. Epic disputed the method [5][6] (S).

## D2 Can a single automated action move money, bind a contract or harm third parties

In July 2013 at UCSF Benioff Children's Hospital, an order for one 160 mg Septra tablet was entered in a per-kilogram unit. The EHR produced an order for about 38 to 39 times the intended dose, reported as 6,160 mg. A pop-up alert was dismissed, a pharmacist verified the order and a nurse gave the pills. The patient, 16-year-old Pablo Garcia, survived [7][8][9] (S). In Leapfrog's 2008–2010 CPOE Evaluation Tool testing at 214 hospitals, 52% of test adult medication orders and 42.1% of test paediatric orders did not trigger appropriate warnings [10] (S). In 2013 and 2014, 36% of potentially harmful test orders and 13.9% of potentially fatal ones went unflagged [11] (S). The searches did not find examples of a single automated clinical action that moves money or binds a contract (not found).

## D3 How rules constraining automated actors are encoded

Smart infusion pumps carry drug libraries with dose-error-reduction limits. A soft limit raises an alarm that the user can confirm past. A hard limit blocks the infusion and cannot be overridden [12][13] (S). In one study, nurses corrected "wrong dose hard limit" errors 75% of the time with smart pumps and 38% of the time with traditional pumps, with no difference for soft-limit errors. A systematic review found that hard limits intercept most of the errors smart pumps catch, while soft limits are weakened by high override rates [13][14] (S). CPOE systems encode medication checks as decision-support rules. Leapfrog's evaluation tool tests them with simulated orders grouped into categories of error (10 or 12, depending on the tool version) [10][15] (S). The Joint Commission's MM.05.01.01 lists what pharmacist review checks: allergies, drug–drug and drug–food interactions, dose, frequency, route, the effect of lab values, therapeutic duplication and other contraindications [4] (S).

## D4 Regulator, accreditor or insurer requirements on system behaviour and change

Requirements on how the automated systems behave and change:

- **21st Century Cures Act §3060 (enacted 13 December 2016):** took CDS software that meets four criteria out of the FDA's device definition (FD&C Act §520(o)(1)(E)). Software that analyses medical images or device signals fails the first criterion and remains a device [16][17] (S).
- **FDA CDS Software final guidance:** issued September 2022, with an updated final guidance issued 6 January 2026 and re-issued 29 January 2026 [16][17][18] (S).
- **ONC HTI-1 final rule:** released December 2023 and published 9 January 2024. It replaced the 2012-era CDS certification criterion with the Decision Support Interventions criterion at 45 CFR 170.315(b)(11). That criterion has 14 source attributes for predictive DSIs, covering training data, intended use, updating and maintenance, validity and fairness. Developers had to update certified health IT by 31 December 2024, and they must attest each year that DSI documentation has been reviewed and updated [19][20] (S).
- **Joint Commission MM.05.01.01:** requires pharmacist review of medication orders before dispensing, with limited exceptions [4] (S).
- **Leapfrog Group CPOE standard:** at least 85% of inpatient medication orders entered through CPOE, and at least 60% of test orders must trigger the appropriate warning. Leapfrog is a purchaser coalition, not a regulator [11] (S).

## D5 Does changing a rule involve several functions

A review of published CDS governance found that some organisations route new decision-support content through existing clinical committees, such as a Pharmacy and Therapeutics (P&T) Committee. Others set up dedicated CDS committees or give approval to one executive, such as the Chief Medical Informatics Officer [21][22] (S). Committees described in the literature combine clinical pharmacists, informatics pharmacists, physicians, ward nurses and ward pharmacists, and P&T committees often give final approval [22] (S). One 54-hospital health system takes alert requests through a ticketing platform. EHR analysts and pharmacy informatics staff review each request first, then a medication-safety workgroup and a clinical workgroup vote on it separately [23] (S). The University of Utah model uses a multi-stakeholder CDS Committee that vets new requests and reviews existing content. It also uses analytics to find high-frequency, low-value alerts [21] (S).

## D6 Does a licensed profession own the consequential decision

The Joint Commission requires a pharmacist to review medication orders before dispensing, with limited exceptions. Concerns must be resolved with the prescriber before dispensing (MM.05.01.01 EP 1, EP 11) [4][24] (S). Joint Commission standards require primary-source verification of a licence when law or regulation requires one. The hospital Medical Staff chapter also requires primary-source verification of an applicant's training and current competence (MS.06.01.03 EP 6; MS.06.01.05 EP 2) [25][26] (S). Verification must come from the issuing source or an approved agent, such as the FSMB Federation Credentials Verification Service, and may be done through secure websites if documented [25][27] (S). In the UCSF 2013 case, a physician placed the order, a pharmacist verified it and a nurse gave the medication [8][9] (S).

## D7 Are overrides, exceptions and near misses recorded and reviewed as data

The Patient Safety and Quality Improvement Act of 2005 (Pub. L. 109-41, signed 29 July 2005) encourages providers to report patient-safety information, errors and near misses to Patient Safety Organizations (PSOs) certified by HHS. It gives that patient safety work product legal privilege and confidentiality protection [28][29] (S). ISMP's Medication Errors Reporting Program collects confidential reports of errors and near misses from practitioners, forwards them to the FDA and manufacturers, and publishes National Alert Network alerts [30] (S). The Joint Commission FAQ says organisations should monitor urgent-use exceptions to pharmacist review so the exception does not become routine [4] (S). Alert-override data is analysed in published studies, including the 2009 multi-state study and the 34-study scoping review [1][3] (S). The searches did not find data on override reporting for automated dispensing cabinets (not found).

## D8 How long the automation has been in widespread use

El Camino Hospital (Mountain View, California) piloted Lockheed's Medical Information System from 1968. The project passed to Technicon in May 1971, and the hospital began going live in December 1971, with most of the hospital on the system about nine months later. It handled orders through light-pen terminals, covering lab scheduling, IV ordering and pharmacy. The system was retired in 2011 [31][32] (S). Whether this was the "first CPOE" is contested [33] (S). An ONC data brief (No. 10, March 2013) reports that hospital adoption of CPOE for medication orders grew 167% between 2008 and 2012, the largest gain among seven Meaningful Use objectives [34] (S). HTI-1 describes its 2023 DSI criterion as the first substantial revision of certified CDS requirements since 2012 [19] (S).

## Sources

1. Harvard Gazette. "Clinicians Override Most Medication Safety Alerts." February 2009. https://news.harvard.edu/gazette/story/2009/02/clinicians-override-most-medication-safety-alerts/.
2. "Overrides of Medication Alerts in Ambulatory Care." *Archives of Internal Medicine* (2009). Abstract record at https://read.qxmd.com/read/19204222/overrides-of-medication-alerts-in-ambulatory-care.
3. University of Arizona. "Overriding Drug-Drug Interaction Alerts in Clinical Decision Support Systems: A Scoping Review." https://experts.arizona.edu/en/publications/overriding-drug-drug-interaction-alerts-in-clinical-decision-supp/.
4. The Joint Commission. "Medication Dispensing - Use of Auto-verification Technology." Standards FAQ, Medication Management. https://jointcommission.org/standards/standard-faqs/critical-access-hospital/medication-management-mm/000002352.
5. Michigan Medicine. "Popular Sepsis Prediction Tool Less Accurate than Claimed." June 2021. https://michiganmedicine.org/health-lab/popular-sepsis-prediction-tool-less-accurate-claimed.
6. HealthDay. "Clinical Benefit of Epic Sepsis Model in Question." 2021. https://www.healthday.com/healthpro-news/infectious-disease/epic-sepsis-model-has-poor-discrimination-of-sepsis-2653467079.html.
7. MetaFilter. "The Overdose - Harm in a Wired Hospital." 2015. https://metafilter.com/148555/The-Overdose-Harm-in-a-Wired-Hospital.
8. Telecare Aware. "Weekend Must Read: How an EHR in a Teaching Hospital Gave a Patient a 39X Overdose." 2015. https://telecareaware.com/must-weekend-read-how-an-ehr-in-a-teaching-hospital-gave-a-patient-a-39x-overdose/.
9. WGBH News. "When Technology and Patient Care Collide." April 11, 2016. https://www.wgbh.org/news/2016-04-11/when-technology-and-patient-care-collide.
10. Healthcare Innovation. "Leapfrog Group Releases New CPOE Study." https://www.hcinnovationgroup.com/clinical-it/clinical-documentation/article/13013555/leapfrog-group-releases-new-cpoe-study.
11. The Leapfrog Group. "Despite Improvement, New Report Reveals Technology to Prevent Medication Errors Fails Too Often." https://www.leapfroggroup.org/node/290.
12. Pharmaceutical Journal. "Developing a Drug Library for 'Smart' IV Infusion Devices: A Smart Move?" https://pharmaceutical-journal.com/article/ld/developing-a-drug-library-for-smart-iv-infusion-devices-a-smart-move.
13. Hospital Pharmacy Europe. "Smart Infusion Pumps' Role in Safe Drug Administration." https://hospitalpharmacyeurope.com/news/editors-pick/smart-infusion-pumps-role-in-safe-drug-administration/.
14. Kuitunen, S., et al. Article on smart infusion pump drug libraries. *BMC Pediatrics* 22 (2022). https://bmcpediatr.biomedcentral.com/counter/pdf/10.1186/s12887-022-03183-8.pdf.
15. Patient Safety & Quality Healthcare. "The Leapfrog CPOE Evaluation Tool." https://psqh.com/analysis/the-leapfrog-cpoe-evaluation-tool.
16. Ropes & Gray. "Is Your Clinical Decision Support Software a Medical Device?" October 2022. https://www.ropesgray.com/en/newsroom/alerts/2022/october/is-your-clinical-decision-support-software-a-medical-device.
17. U.S. Food and Drug Administration. Clinical Decision Support Software guidance document. Search-result link: https://fda.gov/media/162880/download.
18. U.S. Food and Drug Administration. "Town Hall: Clinical Decision Support Software Final Guidance." March 11, 2026. https://www.fda.gov/medical-devices/medical-devices-news-and-events/town-hall-clinical-decision-support-software-final-guidance-03112026.
19. Office of the National Coordinator for Health IT. "HTI-1 Final Rule: Decision Support Interventions Fact Sheet." December 2023. https://www.healthit.gov/sites/default/files/page/2023-12/HTI-1_DSI_fact%20sheet_508.pdf.
20. Drummond Group. "Unveiling Progress: Analyzing the Evolution from the HTI-1 Proposed Rule to Final Rule." https://www.drummondgroup.com/blog/analyzing-hti-1-final-rule/.
21. Article on clinical decision support governance (University of Utah model). PubMed Central. https://pmc.ncbi.nlm.nih.gov/articles/PMC3116253.
22. Review of published CDS governance studies, table ocaa279-T3. PubMed Central. https://pmc.ncbi.nlm.nih.gov/articles/PMC7810441/table/ocaa279-T3.
23. Southeastern Residency Conference 2025. "Implementing a Pharmacy Clinical Decision Support Council for a 54-Hospital Health System." https://2025southeasternresidencyco.sched.com/event/1wqxX/implementing-a-pharmacy-clinical-decision-support-council-for-a-54-hospital-health-system.
24. Wolters Kluwer. "Ten Things Your Joint Commission Surveyor Is Looking For." 2026. https://www.wolterskluwer.com/ja-jp/expert-insights/ten-things-your-joint-commission-surveyor-is-looking-for.
25. Certiphi Screening. "The Joint Commission's Primary Source Verification Requirements." https://certiphi.com/resource-center/background-screening/the-joint-commissions-primary-source-verification-requirements.
26. The Joint Commission. Standards FAQ, Medical Staff (MS). https://www.jointcommission.org/standards/standard-faqs/critical-access-hospital/medical-staff-ms/000001440.
27. Federation of State Medical Boards. "FCVS TJC Principles." Updated October 2017. https://preproduction.fsmb.org/siteassets/fcvs/fcvs_tjc_principles-updated-10_2017-1.pdf.
28. AHRQ PSNet. "Patient Safety and Quality Improvement Act of 2005." https://psnet.ahrq.gov/issue/patient-safety-and-quality-improvement-act-2005.
29. Mondaq. "Patient Safety and Quality Improvement Act of 2005 Signed into Law." September 9, 2005. https://mondaq.com/unitedstates/consumer/34760/patient-safety-and-quality-improvement-act-of-2005-signed-into-law.
30. AHRQ PSNet. "ISMP Medication Errors Reporting Program." https://psnet.ahrq.gov/issue/ismp-medication-errors-reporting-program.
31. Engineering and Technology History Wiki. "Milestones: Pioneering Medical Information System, 1965-1974." https://ethw.org/Milestones:Pioneering_Medical_Information_System,_1965-1974.
32. Technicon. "El Camino Hospital Article." 1977. https://ieeemilestones.ethw.org/w/images/f/f5/Technicon_19771233_ECH_Article.pdf.
33. LIMSwiki. "Computerized Physician Order Entry." https://limswiki.org/index.php/CPOE.
34. Office of the National Coordinator for Health IT. "ONC Data Brief No. 10." March 2013. https://www.healthit.gov/sites/default/files/oncdatabrief10final.pdf.
