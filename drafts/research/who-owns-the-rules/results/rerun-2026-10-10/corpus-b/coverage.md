# Employer coverage by sector (pipeline-review C6)

Recomputed 10 October 2026 from `boards.csv` and `frame-cik.csv` (550 frame employers: 500 Fortune 500 + 50 venture-backed software). Sector = EDGAR SIC code from the submissions JSON (`https://data.sec.gov/submissions/CIK##########.json`, 477 CIKs, User-Agent "Protocols for Business research (https://protocolsforbusiness.com)", about 4 requests per second). Tech = SIC 3570-3579, 3670-3679, 7370-7379. Employers with no CIK are split by frame type: the 50 venture-backed software firms (2 of them have a CIK but are kept in this group by frame type) and the 25 Fortune 500 firms with no EDGAR match (mutuals and private). "Crawlable" = `boards.csv` status `found` (a board with an API we can read). Not crawlable = status `none` (no board found) or `not-crawlable` (a board on an ATS the crawler cannot read, e.g. SuccessFactors, iCIMS, Taleo).

| Sector | Frame | Crawlable | Share | S1 employers |
|---|---|---|---|---|
| Manufacturing | 139 | 52 | 37% | 13 |
| Retail and wholesale | 88 | 37 | 42% | 3 |
| Finance, insurance, real estate | 79 | 32 | 41% | 7 |
| VC software (not SEC filers) | 50 | 36 | 72% | 3 |
| Tech (SIC 357x, 367x, 737x) | 40 | 20 | 50% | 8 |
| Utilities | 33 | 5 | 15% | 0 |
| Transport and telecom | 31 | 7 | 23% | 4 |
| Services (other) | 40 | 18 | 45% | 4 |
| Mining, construction, agriculture | 25 | 8 | 32% | 1 |
| Mutuals and private (no SEC filing) | 25 | 9 | 36% | 1 |
| **All** | 550 | 224 | 41% | 44 |

Crawlable status for the whole frame: found 224, not-crawlable 73, none 253. Against the review's table: Retail and wholesale (88/37), Finance (79/32), Utilities (33/5) and Transport and telecom (31/7) reproduce exactly; Manufacturing (139 vs 137), Tech (40 vs 42) and VC software (50 vs 48, because 2 venture-backed firms have a CIK) differ by 2. The review's table has no rows for Services (other) and Mining, construction, agriculture (65 employers, 26 crawlable), which are added here. Utilities (15%) and Transport and telecom (23%) stay the least covered; VC software (72%) the most.

## S1 sample: 59 postings (`planned-4.3-located.csv`, rows starting `S1 `)

Location comes from the posting text (the Workday LOCATION field, else the location in the posting title or body); see `corpus/staging/planned-4.3-located.csv`, columns `location_country`, `us`, `location_source`. Multi-location postings are classified by the first location listed (8 postings); one posting (TIAA Director, Financial Controller) has an empty location field and is classed India with low confidence from a "- IN" suffix.

| Employer type | Employers | Postings | US | Non-US | US share |
|---|---|---|---|---|---|
| Fortune 500 | 41 | 55 | 27 | 28 | 49% |
| Venture-backed software | 3 | 4 | 0 | 4 | 0% |
| **All** | 44 | 59 | 27 | 32 | 46% |

By sector of the posting employer (Fortune 500 sector from SIC):

| Sector | Postings | US | Non-US |
|---|---|---|---|
| Manufacturing | 14 | 4 | 10 |
| Tech (SIC 357x, 367x, 737x) | 13 | 8 | 5 |
| Finance, insurance, real estate | 9 | 4 | 5 |
| Services (other) | 7 | 4 | 3 |
| VC software (not SEC filers) | 4 | 0 | 4 |
| Retail and wholesale | 4 | 3 | 1 |
| Transport and telecom | 4 | 2 | 2 |
| Mutuals and private (no SEC filing) | 2 | 1 | 1 |
| Mining, construction, agriculture | 2 | 1 | 1 |

Board system of the S1 postings' employers: {'workday': 44, 'none': 9, 'greenhouse': 5, 'smartrecruiters': 1}.

Non-US postings by country: India 4, United Kingdom 3, Ireland 3, Canada 2, Philippines 2, Poland 2, Turkey 2, China 2, Malaysia 1, Colombia 1, Mexico 1, Singapore 1, Indonesia 1, Bulgaria 1, Netherlands 1, Bahrain 1, Hungary 1, Romania 1, Spain 1, United Arab Emirates 1.

The review's offshore shared-service pattern is confirmed: 32 of 59 S1 postings (54%) are outside the US. Per-role breakdown:

| Study occupation | US | Non-US |
|---|---|---|
| HR operations specialist | 1 | 7 |
| accounts payable specialist | 3 | 5 |
| compliance analyst | 4 | 4 |
| controller | 6 | 2 |
| legal operations manager | 2 | 0 |
| platform engineer | 4 | 4 |
| procurement specialist | 2 | 6 |
| revenue operations manager | 5 | 3 |
| support operations manager | 0 | 1 |

## Uncrawlable big-tech and finance names

Every frame employer in the Tech sector (SIC 357x, 367x, 737x) or in finance/insurance/real estate (SIC 6000-6799) whose board is not `found`, with the reason in `boards.csv` (status/ATS). The review's named firms are in bold.

**Tech (SIC 357x, 367x, 737x): 20 of 40 not crawlable**

Advanced Micro Devices (other-ats); **Alphabet** (no board found); Amphenol (no board found); **Apple** (no board found); Automatic Data Processing (no board found); Broadcom (no board found); Cognizant Technology Solutions (no board found); Dell Technologies (no board found); Electronic Arts (no board found); Hewlett Packard Enterprise (no board found); International Business Machines (no board found); Intuit (no board found); **Meta Platforms** (no board found); **Microsoft** (no board found); **Oracle** (no board found); Sanmina (no board found); Science Applications International (no board found); Super Micro Computer (no board found); Texas Instruments (no board found); Vertiv Holdings (no board found).

**Finance, insurance, real estate: 47 of 79 not crawlable**

Aflac (other-ats); American Express (other-ats); American Financial Group (no board found); American Tower (no board found); Apollo Global Management (no board found); Arthur J. Gallagher (no board found); Bank of New York (BNY) (no board found); Berkshire Hathaway (no board found); BlackRock (no board found); CBRE Group (no board found); Capital One Financial (no board found); Charles Schwab (no board found); Cincinnati Financial (no board found); Citizens Financial Group (no board found); Discover (no board found); Equitable Holdings (other-ats); Fidelity National Financial (no board found); Fifth Third Bancorp (no board found); First Citizens BancShares (no board found); **Goldman Sachs Group** (no board found); Hartford Insurance Group (no board found); Huntington Bancshares (no board found); Interactive Brokers Group (no board found); Intercontinental Exchange (no board found); **JPMorgan Chase** (no board found); Jefferies Financial Group (no board found); Jones Financial (Edward Jones) (no board found); KeyCorp (no board found); Lincoln National (no board found); M&T Bank (no board found); Marsh & McLennan (other-ats); MetLife (no board found); Molina Healthcare (no board found); Morgan Stanley (other-ats); Old Republic International (no board found); PNC Financial Services Group (no board found); Principal Financial (no board found); Progressive (no board found); Raymond James Financial (no board found); Reinsurance Group of America (no board found); StoneX Group (no board found); Synchrony (no board found); U.S. Bancorp (no board found); UnitedHealth Group (other-ats); W.R. Berkley (other-ats); Wells Fargo (no board found); Welltower (no board found).

The review's eight named firms:  Alphabet (Tech (SIC 357x, 367x, 737x), none); Amazon (Retail and wholesale, none); Apple (Tech (SIC 357x, 367x, 737x), none); Goldman Sachs Group (Finance, insurance, real estate, none); JPMorgan Chase (Finance, insurance, real estate, none); Meta Platforms (Tech (SIC 357x, 367x, 737x), none); Microsoft (Tech (SIC 357x, 367x, 737x), none); Oracle (Tech (SIC 357x, 367x, 737x), none).



Caveat on `boards.csv`: 7 of the 44 S1 employers (TIAA, 3M, Fox, Capital One, Verizon, Thermo Fisher, PNC; 9 postings) have ats `none` in `boards.csv`, so `boards.csv` under-counts crawlable boards relative to the S1 walk (`s1-walk-log.csv`). The Crawlable column above uses `boards.csv` as the task specified; it is a lower bound.
