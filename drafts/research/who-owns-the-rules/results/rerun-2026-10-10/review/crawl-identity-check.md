# Crawl identity check: corpus B rerun, 2026-10-10

Scope: this review looks only for critical issues. Inputs were `corpus-b/boards.csv`, `corpus-b/crawl-index.csv`, `corpus/staging/s1-employer-frame.csv` and the first 5 lines of each posting file checked. Every employer in `boards.csv` is in the frame.

**Count discrepancy.** The brief says there are 33 `workday-probe` boards. `boards.csv` has **56**: 53 crawled `ok`, 2 `empty` (Qualcomm, EchoStar) and 1 `capped` (TJX). All 56 are checked below. Every one of them carries the note "tenant guessed from employer name, company identity not verifiable via API".

**Method deviation.** For the identity verdicts I read only the first 5 lines of each file. For the duplicate check (part 3), a script hashed ids, URLs and title+description across all lines of every posting file. Only the counts and board pairs it found were read.

## 1. Per-board identity

### All workday-probe boards (56)

| Employer (frame) | board_id | Match? | Reason |
|---|---|---|---|
| Centene | centene | yes | LTSS care management; Superior HealthPlan is a Centene subsidiary |
| Freddie Mac | freddiemac | yes | "At Freddie Mac…", McLean VA |
| **Prudential Financial** | prudential | **no** | This is Prudential plc (Asia): Phnom Penh, Hong Kong, Singapore, "Kuala Lumpur (Group Head Office)". It is a separate company from US Prudential Financial |
| TJX | tjx | yes | TK Maxx, HomeGoods and Marshalls; "TJX Companies" (capped, see section 2) |
| Cisco Systems | cisco | yes | "Cisco's core Switching…", Splunk, a Cisco company |
| Intel | intel | yes | Intel Foundry, Hillsboro and Leixlip |
| Plains GP Holdings | plains | yes | Plains midstream crude, Houston and Midland |
| Abbott Laboratories | abbott | yes | "Abbott is a global healthcare leader" |
| Qualcomm | qualcomm | unsure | empty board (0 postings), nothing to verify |
| Salesforce | salesforce | yes | "About Salesforce" |
| Visa | visa | yes | "Visa is a world leader in payments" |
| Gilead Sciences | gilead | yes | Gilead, plus Kite (CAR-T), a Gilead company |
| Baker Hughes | bakerhughes | yes | "Baker Hughes stands as a leading…" |
| **Applied Materials** | applied | **no** | This is **Applied Industrial Technologies** (NYSE: AIT), a bearings and industrial distributor, not the semiconductor equipment maker |
| AutoNation | autonation | yes | AutoNation dealerships |
| Truist Financial | truist | yes | Truist template text, banker roles in Charlotte and Florida |
| Carrier Global | carrier | yes | "Carrier Global Corporation"; Viessmann is a Carrier subsidiary |
| Danaher | danaher | yes | Cytiva, SCIEX and Leica, each "one of Danaher's 15+ operating companies" |
| Avnet | avnet | yes | "At Avnet…"; Tria, an Avnet company |
| CDW | cdw | yes | "At CDW…" |
| Goodyear Tire & Rubber | goodyear | yes | "About Goodyear", Akron HQ |
| Ameriprise Financial | ameriprise | yes | Ameriprise, plus Columbia Threadneedle (an Ameriprise subsidiary) |
| Corteva | corteva | yes | "Corteva Agriscience" |
| Republic Services | republic | yes | waste and recycling roles (sorter, diesel tech) |
| Devon Energy | devonenergy | yes | "At Devon…", North Dakota and Oklahoma field roles |
| EchoStar | echostar | unsure | empty board (0 postings), nothing to verify |
| Ecolab | ecolab | yes | Ecolab; CoolIT, an Ecolab company |
| IQVIA Holdings | iqvia | yes | "IQVIA is looking to hire…" |
| Baxter International | baxter | yes | "At Baxter…" |
| Regeneron Pharmaceuticals | regeneron | yes | "Regeneron is founded on…", Tarrytown |
| **Western & Southern Financial Group** | western | **no** | This is **Western Colorado University** (Gunnison, CO): dean, provost and bus driver roles |
| Labcorp Holdings | labcorp | yes | "Labcorp is a global leader in laboratory services" |
| Ryder System | ryder | yes | "At Ryder…" |
| DuPont | dupont | yes | "At DuPont…", DuPont Water Solutions |
| LPL Financial Holdings | lplfinancial | yes | "At LPL…", Fort Mill/Charlotte |
| Westlake | westlake | yes | Westlake, Westlake Royal Building Products |
| Assurant | assurant | yes | "GCC-Assurant", Assurant security |
| Crown Holdings | crownholdings | yes | "Crown Holdings, Inc.", CROWN Bevcan |
| Graybar Electric | graybar | yes | "Representatives at Graybar…" |
| Chipotle Mexican Grill | chipotle | yes | "Chipotle has always done things differently" |
| Burlington Stores | burlington | yes | "Burlington Stores, Inc." |
| SpartanNash | spartannash | yes | SpartanNash, now part of C&S Wholesale Grocers |
| Ace Hardware | acehardware | yes | Ace Hardware Home Services (acquired HVAC brands) |
| Analog Devices | analogdevices | yes | "Analog Devices, Inc. (NASDAQ: ADI)" |
| Regions Financial | regions | yes | "a career at Regions"; Ascentium is a Regions subsidiary |
| Dover | dover | yes | Dover Corporation segments (DII, DPC, Dover Food Retail) |
| **Taylor Morrison Home** | taylor | **no** | This is **Taylor Corporation** (printing and manufacturing: Navitor, Venture Solutions, Acrylic Design Associates), not the homebuilder |
| Masco | masco | yes | Delta Faucet, Behr and BrassCraft are Masco brands |
| KBR | kbr | yes | "with KBR!" |
| **Williams-Sonoma** | williams | **no** | This is **The Williams Companies** (energy and pipelines; Houston Tower, Tulsa HQ), not the retailer |
| CACI International | caci | yes | CACI clearance-role template, DC/VA |
| Core & Main | coreandmain | yes | "Core & Main is a leader…" |
| Ingredion | ingredion | yes | "About Ingredion" |
| Cohesity | cohesity | yes | "Cohesity is the leader in AI-powered data security" |
| Automation Anywhere | automationanywhere | yes | "Automation Anywhere is the leader in APA" |
| Clio | clio | yes | "Clio is the global leader in legal AI" |

Result: **5 of 56 workday-probe boards belong to the wrong company**, which is 5 of the 54 that are not empty. The cause in each case is that the guessed tenant slug is a generic word (prudential, applied, western, taylor, williams).

### Random sample of 20 other boards (seed 7)

How the sample was drawn: boards whose method is not `workday-probe` and that have a posting file on disk, sorted by (ats, board_id), then `random.Random(7).sample(list, 20)`.

| Employer | ats / board_id | method | Match? | Reason |
|---|---|---|---|---|
| CarMax | workday / carmax | careers-page-link | yes | "CarMax, the way your career should be" |
| Aramark | smartrecruiters / aramark | slug-probe | yes | "At Aramark…" |
| Ferguson Enterprises | workday / ferguson | careers-page-link | yes | "Since 1953, Ferguson…" |
| Xylem | workday / xylem | careers-page-link | yes | "Xylem is a Fortune 500 global water solutions company" |
| Attentive | greenhouse / attentive | slug-probe | yes | "Attentive® is the AI marketing platform" |
| Checkr | greenhouse / checkr | slug-probe | yes | "About Checkr" |
| Oneok | workday / oneok | careers-page-link | yes | "#WeAreONEOK" |
| Fivetran | greenhouse / fivetran | slug-probe | yes | "From Fivetran's founding…" |
| Corebridge Financial | workday / corebridgefinancial | careers-page-link | yes | "At Corebridge Financial…" |
| J.M. Smucker | workday / smucker | careers-page-link | yes | Smucker plants (Topeka, Emporia), coffee equipment |
| Brex | greenhouse / brex | slug-probe | yes | "Brex is the intelligent finance platform" |
| Motorola Solutions | workday / motorolasolutions | careers-page-link | yes | "At Motorola Solutions…" |
| News Corp. | smartrecruiters / newscorp | slug-probe | yes | News Corp Australia; only 1 posting |
| Airtable | greenhouse / airtable | slug-probe | yes | "Airtable helps organizations build…" |
| Dataiku | greenhouse / dataiku | careers-page-link | yes | "Dataiku is the Platform for AI Success" |
| Home Depot | workday / homedepot | careers-page-link | yes | "a career at The Home Depot" |
| Bank of America | workday / ghr | careers-page-link | yes | "At Bank of America…" (tenant is named ghr) |
| Celonis | greenhouse / celonis | slug-probe | yes | "Celonis is the trusted platform…" |
| Universal Health Services | smartrecruiters / universalhealthservicesinc | slug-probe | yes | "at UHS…", acute and behavioral health; only 1 posting |
| Dialpad | greenhouse / dialpad | careers-page-link | yes | "About Dialpad" |

All 20 sampled boards match.

### Outside the sample: wrong boards found by a name-match sweep

A script checked the first 5 lines of every board for the employer's name. Boards with fewer than 3 hits were read by hand. The following are critical:

| Employer | ats / board_id | method | Match? | Reason |
|---|---|---|---|---|
| **Flock Safety** | ashby / demo.flocksafety-sandbox.com | careers-page-link | **no** | Ashby **demo sandbox**: "Example org is a leading software company… backed by Example Capital"; 11 placeholder jobs |
| **VF** | workday / condenast | careers-page-link | **no** | Condé Nast and The New Yorker (1 World Trade Center), not VF Corp |
| **Glean** | smartrecruiters / glean | slug-probe | **no** | Glean.ai expense-management startup (Howard Katzenberg), not Glean the enterprise AI search company |
| **Celanese** | smartrecruiters / celanese | slug-probe | **no** | Staffing-agency text ("our client's busy technology distribution facility"), identical admin-assistant posts across cities |
| **Insight Enterprises** | smartrecruiters / insightinc | slug-probe | **no** | Contract-recruiter posts ("Hi We are looking to hire…", London contracts); slug company name is "insightinc" |
| **Uber Technologies** | smartrecruiters / uber | slug-probe | **no** | The only posting is "Test UAT" with boilerplate EEO text (test posting) |
| Kimberly-Clark | smartrecruiters / kimberlyclark | slug-probe | unsure | 1 posting (Ikorodu, Nigeria), generic text that never names K-C |
| Caterpillar | smartrecruiters / caterpillarinc | slug-probe | yes (weak) | 1 posting, Peoria IL, Caterpillar "Operating & Execution Model" language |
| Kenvue | smartrecruiters / kenvue | slug-probe | yes | Kenvue named; Skillman NJ |
| Sonic Automotive | smartrecruiters / sonicautomotive | slug-probe | yes | EchoPark is a Sonic brand |
| Loews | workday / loewscorp | careers-page-link | yes | "Loews Corporation is seeking…" |

## 2. Capped boards

| Employer | board | board size (listing total) | postings kept | share kept | share lost |
|---|---|---|---|---|---|
| CVS Health | workday / cvshealth (careers-page-link) | 18,577 | 1,015 | ~5.5% | **~94.5%** |
| TJX | workday / tjx (workday-probe) | 11,053 | 1,118 | ~10.1% | **~90%** |

The index notes say "capped at 5000", but in both cases the listing returned only about 1,040 and 1,140 rows, and then 80 and 85 detail fetches failed. **The real limit was listing pagination, not the 5,000 cap.** The note and the `capped` status therefore understate how much was lost. The kept rows are whatever the listing returned first. That set is not random: CVS's first rows were posted most recently, and TJX's first rows lean heavily toward TJX Europe (TK Maxx in the UK, PL and DE). Both boards are the right company. The problem is coverage and order bias, not identity. Do not use these two boards in any per-employer rate or count without a caveat or a re-crawl.

## 3. Duplicate postings across boards

- **Same `id` across boards: 652 collisions across ~65 board pairs.** All of them are Workday requisition ids such as `R946` or `JR10164`. The largest are analogdevices/sysco (76), regeneron/xylem (58), dover/micron (52) and applied/micron (47).
- **Same title + description across boards: 0.** Same URL across boards: 0. Same title + location + first 400 characters of description: 0.
- **Conclusion:** none of the id collisions is a real duplicate. Workday req ids are only unique within a tenant. Known subsidiary pairs (AIG/Corebridge, Corteva/DuPont, GE Aerospace/GE Vernova, Cigna/Prudential) share ids but no content. **Critical caveat:** `id` alone is not a unique key. Any join, dedup or count keyed on `id` will silently merge unrelated postings. Use `(ats, board_id, id)` or `url`.

## Boards to EXCLUDE

| board file (`<ats>-<board_id>`) | Frame employer | Why |
|---|---|---|
| `workday-prudential` | Prudential Financial | Prudential plc (Asia), a different company |
| `workday-applied` | Applied Materials | Applied Industrial Technologies |
| `workday-western` | Western & Southern Financial Group | Western Colorado University |
| `workday-taylor` | Taylor Morrison Home | Taylor Corporation |
| `workday-williams` | Williams-Sonoma | The Williams Companies |
| `workday-condenast` | VF | Condé Nast |
| `ashby-demo.flocksafety-sandbox.com` | Flock Safety | Ashby demo placeholder jobs |
| `smartrecruiters-glean` | Glean | Glean.ai (expense software), a different company |
| `smartrecruiters-celanese` | Celanese | staffing-agency postings |
| `smartrecruiters-insightinc` | Insight Enterprises | contract-recruiter postings |
| `smartrecruiters-uber` | Uber Technologies | single "Test UAT" posting |

Review before use (not excluded): `smartrecruiters-kimberlyclark` (identity unsure, 1 posting); `workday-cvshealth` and `workday-tjx` (right company, but only ~5–10% of each board was captured, in listing order); `workday-qualcomm` and `workday-echostar` (empty). Not checked: about 150 non-workday-probe boards that were outside the sample of 20 and passed the name-match sweep. The sweep only checks the first word of the employer name, so a wrong company that happens to share that word would pass it.
