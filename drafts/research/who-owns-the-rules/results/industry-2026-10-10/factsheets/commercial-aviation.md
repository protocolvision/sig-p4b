# Commercial aviation: fact sheet

Scope: flight automation, airline operations control, safety management.
Compiled 2026-10-10. Facts only; no scores, rankings or cross-industry comparisons.

Grades: P = primary source opened; R = reputable secondary opened; S = search-result summary only (the page itself was not opened). In this run, page fetching was blocked (DNS failures), so every fact is graded S.

## D1 Autonomy and speed

A news report gives an FAA estimate that commercial airline pilots use automation to fly about 90% of the time. The same report cites a U.S. DOT Inspector General finding that the FAA does not know whether pilots are ready to fly manually when needed [1] (S). Cranfield University analysed a year of flight data from about 14,000 Airbus A319 flights averaging just under 72 minutes airborne. The search result did not show its autopilot-use percentage [2] (S). In Airbus Normal Law, fly-by-wire protections keep angle of attack from exceeding "alpha prot" whatever the pilot inputs. "Alpha floor" commands take-off/go-around (TOGA) thrust automatically [3][4] (S). On the Boeing 737 MAX, MCAS acted without crew approval. In the Lion Air accident (October 2018), it pushed the nose down more than 20 times based on a faulty angle-of-attack sensor [5][6] (S). TCAS II resolution advisories are issued by the onboard system, and crews are required to follow them even when they contradict an air traffic controller's instruction [7][8] (S).

## D2 Can a single automated action move money, bind a contract or harm third parties

MCAS activations driven by a single faulty angle-of-attack sensor were linked to the Lion Air 610 crash (October 2018, 189 killed) and the Ethiopian Airlines 302 crash (10 March 2019, 157 killed): 346 deaths in total. The 737 MAX was grounded worldwide from 13 March 2019 [5][6][9] (S). In airline operations control, Southwest Airlines' crew-scheduling system became overloaded during the December 2022 disruption. Southwest cancelled about 16,700 to 16,900 flights affecting more than 2 million passengers [10][11] (S). The U.S. DOT then imposed a $140 million civil penalty, the largest for consumer-protection violations in its history: $35 million as a fine and the rest for passenger compensation. Southwest had already paid more than $600 million in refunds and reimbursements [10][12] (S). The sources describe the scheduling system as overloaded, not as a single automated action causing the loss [11] (S).

## D3 How rules constraining automated actors are encoded

Airbus Normal Law encodes the flight envelope as protections in the flight-control computers: high speed, high angle of attack, alpha floor, load factor, pitch, bank, windshear and low energy. Normal Law is kept after a single failure of a sensor, electrical system, hydraulic system or flight-control computer. Alternate Law follows certain double or triple failures [3] (S). In Alternate Law, conventional stall warning replaces alpha protection [4] (S). After the two 737 MAX crashes, Boeing changed MCAS to use data from both angle-of-attack sensors instead of one [6] (S). Operational limits are also encoded in law. Under 14 CFR 121.533, a domestic flight needs a dispatch release for which the pilot in command and the aircraft dispatcher are jointly responsible, and the release must comply with the carrier's FAA operations specifications [13] (S).

## D4 Regulator, accreditor or insurer requirements on system behaviour and change

Rules on how airborne software and airline safety systems behave and change:

- **FAA AC 20-115C (19 July 2013):** recognised RTCA DO-178C as an acceptable (not the only) means of showing that airborne software meets airworthiness requirements. AC 20-115D is described as the current version [14][15] (S).
- **DO-178C design assurance levels:** Level A (catastrophic failure condition) to Level E (no safety effect), set through the system safety assessment. Level A carries 71 objectives, including modified condition/decision coverage (MC/DC) [14][15] (S).
- **14 CFR Part 5 (2015):** required Part 121 air carriers to have a Safety Management System with four components: safety policy, safety risk management, safety assurance and safety promotion [16][17] (S).
- **Part 5 expansion (final rule published 26 April 2024):** extended Part 5 to Part 135 operators, §91.147 air tour operators and certain Part 21 production and type certificate holders. It was issued in response to a Congressional mandate and NTSB recommendations and aligns with ICAO Annex 19 [16][17] (S).
- **ICAO TCAS mandate:** ICAO mandated TCAS globally for aircraft above 5,700 kg from 2003 [7] (S). Switzerland's FOCA restated in bulletin SAND-2015-001 that crews must follow TCAS RAs [8] (S).

## D5 Does changing a rule involve several functions

Under 14 CFR Part 5, safety risk management is one of an SMS's four required components [16] (S). Training and vendor sources describe SMS management of change as a repeatable process to identify, assess and control risks from changes to procedures, systems and new technology. They list operations, continuing airworthiness (maintenance), air navigation services and airports as domains it must cover [18][19] (S). An ICAO-hosted presentation by Hong Kong's civil aviation authority lists the criticality and stability of systems as factors in managing change [20] (S). A dispatch release is a joint pilot–dispatcher responsibility under 14 CFR 121.533 [13] (S). The searches did not find a primary airline or regulator document describing which functions sign off on a change to flight automation logic (not found).

## D6 Does a licensed profession own the consequential decision

Under 14 CFR 121.533, the pilot in command and the aircraft dispatcher are jointly responsible for preflight planning, delay and dispatch release. The dispatcher monitors the flight and can cancel or redispatch it. In flight, the pilot in command has full control and authority over the aircraft and crew [13] (S). Aircraft dispatchers are certificated under 14 CFR Part 65 Subpart C. Applicants need a knowledge test, a practical test, and either two years of qualifying experience in the last three years or an approved course. The rule was most recently amended in 2024 (Amdt. 65-65, 89 FR 80053, 1 October 2024) [21][22] (S). The searches did not confirm the airline first-officer airline transport pilot (ATP) certificate requirement (not found).

## D7 Are overrides, exceptions and near misses recorded and reviewed as data

The Aviation Safety Reporting System (ASRS), funded by the FAA and run by NASA, takes voluntary, confidential incident reports. A 1997 SAE paper reported growth from about 3,000 to 32,000 reports a year [23] (S). Flight Operational Quality Assurance (FOQA) programmes analyse recorded flight data from normal line operations; a 2008 article said twenty U.S. airlines analysed FOQA parameters routinely [24] (S). Aviation Safety Action Programs (ASAP) are partnerships between the FAA, the certificate holder and usually the employees' labour organisation. Event review committees that include an FAA inspector handle the reports, which are also archived with NASA ASRS [24][25] (S). The FAA's ASIAS programme lets the FAA and airlines query de-identified aggregate safety data across private and government servers [26] (S).

## D8 How long the automation has been in widespread use

Sperry developed a gyroscopic autopilot in 1912. Lawrence Sperry demonstrated it in 1914 at the Concours de la Sécurité en Aéroplane in Paris, in a Curtiss C-2 [27][28] (S). In 1930, a more compact Sperry autopilot held a U.S. Army Air Corps aircraft on heading and altitude for three hours [27] (S). The Airbus A320, described as the first airliner with fully digital fly-by-wire flight controls, first flew on 22 February 1987. It entered service with Air France in March–April 1988; sources differ on the exact date [29][30][31] (S). TCAS became a global ICAO requirement for aircraft above 5,700 kg from 2003 [7] (S). Part 121 SMS became mandatory in 2015 [16] (S). The searches did not confirm the history of autoland certification (not found).

## Sources

1. Business Insurance. "Flying on Autopilot Improves Airline Safety but Can Lead to Errors." https://www.businessinsurance.com/insurers-regulators-want-commercial-airline-pilots-to-get-more-manual-flying-ex/.
2. Cranfield University. "How Long Do Pilots Really Spend on Autopilot?" https://insights.cranfield.ac.uk/blog/how-long-do-pilots-really-spend-on-autopilot.
3. FlyByWire Simulations. "Normal Law Protections in the A320." Documentation. https://docs.flybywiresim.com/pilots-corner/a32nx/a32nx-advanced-guides/protections/overview/.
4. PlaneFYI. "Stall Protection System." https://planefyi.com/systems/stall-protection/.
5. Insurance Journal. Report on 737 MAX angle-of-attack sensors. April 11, 2019. https://www.insurancejournal.com/news/national/2019/04/11/523464.htm.
6. Jalopnik. "Recent Boeing 737 MAX Crashes May Be the Result of a Single Faulty Sensor." 2019. https://jalopnik.com/recent-boeing-737-max-crashes-may-be-the-result-of-a-si-1833380459.
7. PlaneFYI. "TCAS System." https://planefyi.com/de/systems/tcas-system/.
8. Swiss Federal Office of Civil Aviation (FOCA). "SAND-2015-001." https://www.bazl.admin.ch/en/foca-sand-2015-001-en.
9. AVweb. "Ethiopian Max Crash: Flight Data Implicates AoA Sensor." 2019. https://avweb.com/?p=87941.
10. NPR. "Southwest Will Pay a $140 Million Fine for Its Meltdown during the 2022 Holidays." December 18, 2023. https://www.npr.org/2023/12/18/1219906471/southwest-airlines-2022-meltdown-fined-faa.
11. Fox Business. "Southwest Airlines Reaches $140M Settlement with DOT for 2022 Holiday Debacle." December 2023. https://www-ak-ms.foxbusiness.com/lifestyle/southwest-airlines-reaches-140m-settlement-dot-2022-holiday-debacle.
12. NerdWallet. "Southwest Faces $140 Million Penalty for 2022 Holiday Meltdown." https://www.nerdwallet.com/article/travel/southwest-faces-140-million-penalty-for-2022-holiday-meltdown.
13. Legal Information Institute. "14 CFR § 121.533 - Responsibility for Operational Control: Domestic Operations." https://www.law.cornell.edu/cfr/text/14/121.533.
14. Wikipedia. "DO-178." https://www.wikipedia.com/wiki/DO-178.
15. Rapita Systems. "DO-178C Guidance." https://www.rapitasystems.com/node/528.
16. Federal Aviation Administration. "Safety Management Systems." Final rule. *Federal Register* 89, no. 82 (April 26, 2024). https://www.govinfo.gov/content/pkg/FR-2024-04-26/html/2024-08669.htm.
17. Federal Aviation Administration. "SMS Final Rule." https://www.faa.gov/newsroom/sms_final_rule.pdf.
18. SMS Pro Aviation Safety Software Blog. "Management of Change in Aviation Safety: A Guide for SMS Success." https://aviationsafetyblog.asms-pro.com/blog/management-of-change-in-aviation-safety-a-guide-for-sms-succes.
19. SAS Sofia. "EASA Compliant Safety Management System – Management of Change – 2 Days." Course outline. https://sassofia.com/course/easa-compliant-safety-management-system-management-of-change-2-days.
20. Hong Kong Civil Aviation Department. "SMS: ANSP Perspective." ICAO APRAST/6, 2015. https://www.icao.int/APAC/Meetings/2015%20APRAST6/05%20-%20HKG_CAD%20-%20SMS_ANSP%20Perspective.pdf.
21. Legal Information Institute. "14 CFR § 65.55 - Knowledge Requirements." https://www.law.cornell.edu/cfr/text/14/65.55.
22. Legal Information Institute. "14 CFR § 65.57 - Experience or Training Requirements." https://www.law.cornell.edu/cfr/text/14/65.57.
23. SAE International. "The US Aviation Safety Reporting System." Technical paper 975562, 1997. https://saemobilus.sae.org/papers/us-aviation-safety-reporting-system-975562.
24. Flight Safety Foundation. *AeroSafety World*, May 2008, 25–29. https://flightsafety.org/wp-content/uploads/2016/10/asw_may08_p25-29.pdf.
25. Federal Aviation Administration. "Report to Congress on ASAP and FOQA." https://www.faa.gov/sites/faa.gov/files/2021-11/Report-to-Congress-on-ASAP-and-FOQA.pdf.
26. Melby, Paul. "ASIAS." MITRE presentation, 2009. https://c3.nasa.gov/dashlink/static/media/other/Paul_Melby_MITRE_ASIAS_TTS_2009.pdf.
27. Wikipedia. "Autopilot." https://en.wikipedia.org/wiki/Autopilot.
28. U.S. Department of Transportation, Monroney Aeronautical Center. "Celebrating 100 Years of Autopilot." https://www.esc.gov/monroneynews/archive/Vol_5/TG/05_3.asp.
29. AirlineGeeks. "'Delightfully Responsive and Reassuringly Stable to Fly:' Marking 30 Years of the Airbus A320." February 22, 2017. https://airlinegeeks.com/2017/02/22/delightfully-responsive-and-reassuringly-stable-to-fly-marking-30-years-of-the-airbus-a320/.
30. Airbus. "Fly-by-wire (1980–1987)." Commercial aircraft history. https://airbus.com/en/our-history/commercial-aircraft-history/fly-by-wire-1980-1987.
31. Simple English Wikipedia. "Airbus A320 Family." https://simple.wikipedia.com/wiki/A320.
