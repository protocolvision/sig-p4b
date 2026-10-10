# Pattern signatures (historical), written before present-day coding

Protocols for Business · rerun 2026-10-10 · triangulation design section 6.1 · historian agent (Opus), fresh
context

## Scope and rules followed

- **Inputs read:** `triangulation-design.md` (all of it), `sources-v2/media-historical.csv`, and
  `loop-design-v2.md` section 8. No `results/` folder (except writing into this one), `roles/`,
  `exploratory/`, `report/`, `README.md`, `research-design.md` or `industry-analogue-design.md` was opened.
- **Evidence:** every dated entry comes from a source fetched and read on 2026-10-10. Text is saved in
  `corpus/b-raw/signatures/<id>.txt` (git-ignored). The first line of each file is `SOURCE <url> FETCHED 2026-10-10`.
  Source IDs in the tables (for example `dv-sodr-2014`) are those file names.
- **Grades:** (P) primary, read; (R) reputable secondary, read; (S) search-engine summary only, page not read
  or not readable; (M) memory. No entry below is graded M. **NF** means not found: no source was found, and
  the feature value then defaults to `no`. Load-bearing timeline entries are P or R; S entries are context
  only and are marked as such.
- **"Not found" means not found in this session.** It does not mean the event never happened. Gaps were not
  filled from memory, including where the historian believes a date is known.
- **Present-day agent era:** not considered.

## Feature definitions (neutral; IDs used by the scoring script)

| ID | Feature |
| --- | --- |
| N01 | Practice described ≥2 years before a common title |
| N02 | Duties from two previously separate functions merged |
| N03 | Community before tooling before certification before regulation |
| N04 | Title rose then fragmented or was renamed within ~10 years |
| N05 | Shared metrics originated with practitioners, not regulators |
| N06 | Diffusion from software-native to enterprise to regulated sectors |
| N07 | More postings carry the practice as a duty/skill than as a title |
| N08 | Title and practice appeared together |
| N09 | Single-firm origin |
| N10 | Authority from an owned number |
| N11 | Title tied to a legal text |
| N12 | Senior/executive at first appearance |
| N13 | Certification/statute before practitioner community |
| N14 | Title boom within 2–3 years of a new tool |
| N15 | Duties are operating a tool |
| N16 | Salary-premium title boom then split into narrower titles |
| N17 | Mature in one industry long before others |
| N18 | Carried by people moving between industries |
| N19 | No new title, team or metric (absorbed into engineering) |

Values are `yes`, `no` or `partial`. Where a pattern has several cases (P2, P3, P6), `partial` often means
the cases disagree; the text says which.

---

## 1. DevOps (H-DevOps)

### Timeline

| Milestone | Date | Evidence | Source | Grade |
| --- | --- | --- | --- | --- |
| First practice description | 4–8 Aug 2008 | Debois, "Agile Infrastructure and Operations: How Infra-gile are You?", Agile 2008, Toronto. Slides: "IT people, Operations separated from Dev. by design"; agile (Scrum) applied to a data-centre move | `dv-crossref-debois-2008`, `dv-debois-agile2008-slides` (Wayback capture 2010-09-24) | P |
| Related earlier context | 23 Jun 2008 | Velocity 2008, "Web Performance and Operations Conference": its first year. This is about operations performance, not yet the dev/ops merge | `dv-agileadmin-velocity2008` | P |
| Practice made public | 23 Jun 2009 (talk); reports 25 and 28 Jun 2009 | Allspaw and Hammond, "10+ Deploys Per Day: Dev and Ops Cooperation at Flickr", Velocity 2009: "on a normal day there are 10 full deployments" | `dv-dck-velocity2009`, `dv-hammond-velocity2009` | P |
| First community or conference | 2009 (after June 2009; exact dates not verified) | devopsdays Ghent 2009, "the first conference that focuses on bringing the best of both worlds together"; programme: Puppet, cucumber-nagios, Flapjack, Kanban in operations, CI pipelines. Organisers later: about "60 something people in Gent" | `dv-wb-devopsdays-2009`, `dv-devopsdays-ghent-2009-program`, `dv-devopsdays-2009-legacy`, `dv-infoq-5yrs` (Dec 2014 interview) | P |
| First open tooling | Jan 2009 (Chef repository created); Puppet already presented as an established tool at devopsdays 2009 | GitHub API `created_at` 2009-01-15 for chef/chef; Ghent programme "Building Agile Infrastructures with Puppet" | `gh-chef-chef`, `dv-devopsdays-ghent-2009-program` | P |
| First vendor certification | Announced 7 Nov 2014 (beta at re:Invent 10–14 Nov 2014) | AWS Certified DevOps Engineer – Professional | `dv-aws-devops-cert-2014` | P |
| First regulation | not found | No legal text requiring a DevOps role or practice was found | — | NF |
| First official occupation code | 23 Apr 2025 (apprenticeship); O*NET sample title (undated) | US DOL Office of Apprenticeship Bulletin 2025-82: new National Occupational Framework "DevOps Engineer", O*NET 15-1252.00 (Software Developers). O*NET lists "DevOps Engineer (Development Operations Engineer)" among reported titles for 15-1252.00. There is no separate SOC code | `dv-dol-nof-devops-2025`, `dv-onet-15-1252` | P |
| Title emergence | by Mar 2011 | SimplyHired, "devops engineer": 134 results (HP, Symantec, Yelp, MuleSoft, Path). The 2014 report says "named DevOps departments have only come into existence in the past five years" | `dv-wb-simplyhired-devops-engineer-2011`, `dv-sodr-2014` | P |
| Title growth | Nov 2012; Mar 2013; Jul 2014 | SimplyHired "devops", 1,671 results (Home Depot, PTC, WalmartLabs). Puppet Labs: "Job listings for 'DevOps' are up by 75 percent". Indeed "Devops Engineer", 2,858 results | `dv-wb-simplyhired-devops-2012`, `dv-sodr-2013-blog`, `dv-wb-indeed-devops-engineer-2014` | P |
| Title peak or fade | not found | Google Trends could not be fetched (HTTP 429). No dated peak was found | — | NF |
| Rename or split | 10–11 Apr 2023 | CNCF Platforms white paper: "Inspired by the cross-functional cooperation promised by DevOps, platform engineering has begun to emerge in enterprises" | `dv-cncf-platforms-announce`, `dv-cncf-platforms-wp` | P |
| First shared metrics | Mar 2013 (survey Dec 2012); formalised Jun 2014; extended 2018 | 2013: deploy frequency, change success rate, time to restore. 2014: deployment frequency, lead time for changes, mean time to recover, change fail rate. 2018: availability added. CNCF 2023 recommends the same DORA metrics | `dv-sodr-2013-blog`, `dv-sodr-2014`, `dv-sodr-2018`, `dv-cncf-platforms-wp` | P |
| Diffusion across sector types | 2012 → 2014 → 2018 | 2012 postings at a retailer and an industrial software firm. 2014 respondents: technology 22.7%, web software 10.9%, finance/banking 7.4%, government 4.5%, healthcare 3.0%; DevOps departments more often in "entertainment, technology and web software". 2018: technology 40%, financial services 15%, government 6%, healthcare and pharma 5%; "high performers in both non-regulated and highly regulated industries" | `dv-wb-simplyhired-devops-2012`, `dv-sodr-2014`, `dv-sodr-2018` | P |

Note: the shared metrics come from research run by a vendor (Puppet Labs) with IT Revolution and
ThoughtWorks, later DORA at Google. This is practitioner and vendor research, not regulation.

### Feature profile

| ID | Value | Evidence |
| --- | --- | --- |
| N01 | yes | Practice Aug 2008 (Debois) and Jun 2009 (Velocity); title in postings by Mar 2011 and common by Nov 2012. About 2.5 to 4 years, so the margin is thin (P) |
| N02 | yes | "Dev and Ops cooperation"; devopsdays 2009: "operations and sysadmins are becoming programmers"; Debois: Ops "separated from Dev. by design" (P) |
| N03 | partial | Community (2009) → certification (2014) → no regulation holds. But open tooling (Chef Jan 2009; Puppet presented as existing) **preceded** the first community (P) |
| N04 | partial | Platform engineering is named as DevOps's successor form in Apr 2023, about 14 years after 2009, outside the ~10-year window. No fade of the "DevOps engineer" title was found (P/NF) |
| N05 | yes | Metrics from the State of DevOps surveys (2013–2018), not from any regulator; vendor-sponsored (P) |
| N06 | yes | Tech and web share falls and finance and government shares rise between 2014 and 2018; regulated sectors are named explicitly in 2018 (P) |
| N07 | partial | Indirect only. "DevOps engineer" titles appear inside ordinary IT ops (4.6%) and development (5.4%) departments (2014). Keyword searches return many postings titled otherwise (Indeed 2014: "Senior Systems Engineer", "Software Engineering Manager"). No count of duty postings against title postings exists (P, weak) |
| N08 | no | Practice (2008) preceded the title (2011) (P) |
| N09 | no | Several origins: Debois (consultant, Belgium), Flickr/Yahoo, the Velocity community (P) |
| N10 | no | Metrics are benchmarks; no evidence that a DevOps role draws authority from a number it owns (P) |
| N11 | no | NF |
| N12 | no | Early titles are engineer-level ("DevOps Engineer", "Systems Engineer (DevOps)"); in 2014, 55% of DevOps department respondents were DevOps or systems engineers (P) |
| N13 | no | Certification (2014) came five years after the community (2009) (P) |
| N14 | partial | The title rose 2011–2012, two to three years after Chef (2009), but sources tie it to a movement, not to one tool (P) |
| N15 | partial | Postings name configuration management and "various DevOps tools", but duties also include process and cooperation (P) |
| N16 | no | No salary-premium evidence found (NF) |
| N17 | partial | Concentrated in web/tech first (2014), spreading within about 5–9 years, not decades (P) |
| N18 | no | NF |
| N19 | no | New title, departments and metrics all appeared (P) |

---

## 2. SRE (P1)

### Timeline

| Milestone | Date | Evidence | Source | Grade |
| --- | --- | --- | --- | --- |
| First practice description | 2003 (internal; published account 2016) | Treynor "joined Google as Site Reliability Tsar in 2003", grew "an original core of 7 'production' engineers". SRE book: "SRE is what happens when you ask a software engineer to design an operations team" | `sre-srecon14-keys`, `sre-book-intro` | P |
| First public talk | 2006 (LISA '06) | Limoncelli, "Site Reliability at Google/My First Year at Google" | `sre-lisa06` | P |
| First community or conference | May 2014 | Inaugural SREcon14 (USENIX), Santa Clara | `sre-srecon14-home`, `sre-srecon14-keys` | P |
| First open tooling | not found | No SRE-specific open tool with a dated source was found | — | NF |
| First vendor certification | 29 Oct 2019 (delivery Jan 2020) | DevOps Institute "SRE Foundation", "based in large part on ... Google's Site Reliability Engineering book" | `sre-devopsinst-sre-foundation-2019` | P |
| First regulation / occupation code | not found | No law found. O*NET keyword search maps "site reliability engineer" onto existing codes (15-1252.00, 15-1221.00, 15-1299.08 …); there is no own code | `sre-onet-search` | P (absence) |
| Title emergence | 2003 (Google); outside Google by 2012 | Groupon SRE team founded 2012; LinkedIn SRE (joined 2012); Twitter Aurora/Mesos SRE team; Dropbox, Netflix and Facebook speakers at SREcon14 | `sre-srecon14-program` | P |
| Title peak or fade | not found | — | — | NF |
| Rename or split | not found | — | — | NF |
| First shared metrics | public by 2016 | SLOs and error budgets: "the error budget is one minus the availability target"; 50% cap on ops work; SREcon16 "Service Levels and Error Budgets" | `sre-book-intro`, `sre-srecon16-slo` | P |
| Diffusion across sector types | 2013–14; 2019; 2024 | Google SREs at healthcare.gov (SREcon14); "rapid acceleration of enterprise interest" (2019); "the rest of the SaaS industry has come to adopt the SRE name" and "the SRE book arguably accelerated SRE adoption" (2024) | `sre-srecon14-healthcaregov`, `sre-devopsinst-sre-foundation-2019`, `sre-prodcast-treynor` | P |

### Feature profile

| ID | Value | Evidence |
| --- | --- | --- |
| N01 | no | Title and practice both date from 2003 at Google (P) |
| N02 | yes | Software engineering applied to operations work; the book names the "development/ops split" it replaces (P) |
| N03 | partial | Community (2014) → certification (2019) → no regulation fits; no open tool was found; the start was one firm, not a community (P/NF) |
| N04 | no | No rename or fragmentation found (NF) |
| N05 | yes | SLOs and error budgets are practitioner (Google) constructs (P) |
| N06 | partial | Google → web firms (2012–14) → enterprise interest (2019); government via healthcare.gov. No dated entry into regulated industries found (P) |
| N07 | no | NF |
| N08 | yes | 2003 (P) |
| N09 | yes | Google (P) |
| N10 | yes | Error budget: "We can spend the budget on anything we want, as long as we don't overspend it" (P) |
| N11 | no | NF |
| N12 | no | Engineer-level team; the founder was a manager ("Tsar"), but the role itself is engineer-level (P) |
| N13 | no | Certification 2019, after SREcon 2014 (P) |
| N14 | no | NF |
| N15 | no | Duties are engineering and running services, not operating a tool (P) |
| N16 | no | NF |
| N17 | partial | About a decade inside Google before other firms (2003 → 2012); within software rather than across industries (P) |
| N18 | partial | Carried by ex-Google people: Dickerson (Google SRE 2006–2013) to healthcare.gov; Murphy (Microsoft, Google, Amazon). These are moves between firms more than between industries (P, CSV H003/H007 and pages) |
| N19 | no | New title, team and metric (P) |

---

## 3. Mandated officer (P2): CISO, data protection officer, compliance officer

### Timeline

| Milestone | Date | Evidence | Source | Grade |
| --- | --- | --- | --- | --- |
| First practice description | 1985 (security); 1977 (data protection in law) | Katz: "1985–1995, Vice President and Head of Information Security for JP Morgan", before the CISO title | `p2-katz-1997-hearing` | P |
| First community or conference | 1989 (security); 2000 (privacy) | (ISC)²: "From our first days in 1989". IAPP "founded in 2000". CSI Annual Security Conference running by 1998 | `p2-isc2-history`, `p2-iapp-about`, `p2-wb-isc2-1998` | P |
| First open tooling | not applicable / not found | — | — | NF |
| First certification | by Dec 1998 (CISSP; year of launch not verified) | (ISC)² site Dec 1998: CISSP exam, CBK seminars, "fellow CISSPs" | `p2-wb-isc2-1998` | P |
| First regulation (DPO) | 27 Jan 1977 | Bundesdatenschutzgesetz, BGBl. I S. 201: § 28 "Bestellung eines Beauftragten für den Datenschutz", § 29 "Aufgaben" (private-sector bodies) | `p2-bdsg-1977-bgbl`, `p2-computerwoche-bdsg-1977` | P |
| Regulation (DPO, EU) | 24 Oct 1995; 27 Apr 2016 | Directive 95/46/EC Art. 18(2): controller may appoint "a personal data protection official". GDPR Art. 37 "Designation of the data protection officer"; 37(5) "expert knowledge of data protection law" | `p2-dir9546-eurlex`, `p2-gdpr-eurlex` | P |
| Regulation (compliance) | Nov 1991; 24 Dec 2003 | US Sentencing Guidelines Ch. 8: effective programme requires "specific individual(s) within high-level personnel ... overall responsibility to oversee compliance". SEC Rules 206(4)-7 and 38a-1: "designate a chief compliance officer"; "position of sufficient seniority and authority" | `p2-ussc-1991-ch8`, `p2-fr-2003-sec-cco` | P |
| Regulation (security officer) | 17 Dec 2002 (two texts) | FISMA (PL 107-347) § 3544(a)(3)(A): "designating a senior agency information security officer". FTC Safeguards Rule (67 FR 36493, 23 May 2002); 2021 amendment (86 FR 70304): "Designate a Qualified Individual", reporting "at least annually, to your board of directors" | `p2-fisma-2002`, `p2-ecfr-16cfr314` | P |
| Official occupation code | not found | The SOC page for compliance officers could not be fetched (BLS blocks automated requests; Wayback was offline at the time) | — | NF |
| Title emergence | 1995 (CISO); Mar 2000 (CPO); Dec 2003 (CCO by rule) | Katz: "1995 – Present, Chief Information Security Officer, Citibank". DoubleClick names a Chief Privacy Officer (NYC press release, 5 Mar 2000). IBM names a CPO, 29 Nov 2000; "less than 75 chief privacy officers in place now" | `p2-katz-1997-hearing`, `p2-nyc-polonetsky-2000`, `p2-cw-ibm-cpo-2000` | P |
| Title peak or fade | not found | — | — | NF |
| Rename or split | not found | The Safeguards Rule's "Qualified Individual" (2021) avoids the CISO title, but that is wording, not a split | `p2-ecfr-16cfr314` | P (weak) |
| First shared metrics | not found | — | — | NF |
| Diffusion across sector types | 1985–1995 banks → 2002 federal agencies and financial institutions → 2016 all controllers (GDPR) | Banks first (JP Morgan, Citibank), then statute by sector | sources above | P |

### Feature profile

| ID | Value | Evidence |
| --- | --- | --- |
| N01 | partial | CISO: a security head existed from 1985, ten years before the 1995 title (P). DPO and CCO: title and duties were defined together in legal text (P) |
| N02 | no | Each officer holds one function (security, privacy or compliance) (P) |
| N03 | partial | Security: community and certification (1989, ≤1998) came before statute (2002). DPO: statute (1977) came decades before community (IAPP 2000). Compliance: community NF (P) |
| N04 | no | NF |
| N05 | no | NF |
| N06 | no | Regulated finance came first, then government, then all sectors by statute; the reverse direction (P) |
| N07 | no | NF |
| N08 | partial | DPO and CCO: yes (statutory title with duties). CISO: no (function before title) (P) |
| N09 | partial | CISO title from one firm (Citibank/Citicorp, 1995; "first CISO" per H034–H037). DPO and CCO from statute (P) |
| N10 | no | NF |
| N11 | yes | BDSG 1977 § 28; Directive 95/46 Art. 18; GDPR Art. 37; SEC 2003; FISMA 2002. CISO initially firm-chosen (P) |
| N12 | yes | "Chief" titles at first appearance; CCO "sufficient seniority"; Sentencing Guidelines "high-level personnel"; CPOs described as "executives" (P) |
| N13 | partial | DPO yes (1977 statute → 2000 community); compliance yes (1991 guidelines, no earlier community found); CISO no (P) |
| N14 | no | NF |
| N15 | no | Duties are oversight and programme ownership (P) |
| N16 | no | NF |
| N17 | partial | Banking had security heads and CISOs well before other sectors (1985/1995 → 2002). The spread followed statute more than imitation (P) |
| N18 | no | NF |
| N19 | no | New titles created (P) |

---

## 4. Tool-operator fade (P3): webmaster, prompt engineer

### Timeline: webmaster

| Milestone | Date | Evidence | Source | Grade |
| --- | --- | --- | --- | --- |
| Tool | 6 Aug 1991 | Berners-Lee on alt.hypertext: "The WorldWideWeb (WWW) project aims to allow links to be made to any information anywhere" | `p3-tbl-1991-announce` | P |
| First practice description / title emergence | 1993 (first known use of the word, per Merriam-Webster, cited by Google 2020) | — | `p3-google-search-central-2020` | R |
| Practitioner account | 1996 | Kip Parent, "The Webmaster", SGI: "responsible for all aspects of SGI's activities on the Web ... managing creative, technical, production, and electronic sales staff" | `p3-edge-kipparent-1996` | P |
| Standardisation (not regulation) | May 1997 | RFC 2142: standard mailbox "WEBMASTER HTTP" | `p3-rfc2142-1997` | P |
| First community | not found | — | — | NF |
| First certification | by Feb 2000 (Version 4 already existed); 5 Dec 2000 | ProsoftTraining "Certified Internet Webmaster (CIW)"; Novell merges its CIP into CIW | `p3-novell-ciw-2000` | P |
| Official occupation code | undated | O*NET 15-1299.01 Web Administrators appears in keyword results | `sre-onet-search` (list), `p6-onet-search-responsive` | P (weak) |
| Postings | Feb 2009; May 2011 | SimplyHired "Webmaster": 962 (2009), 2,226 (2011); many government contractors (SAIC, ManTech, CSC, CACI) | `p3-wb-simplyhired-webmaster-2009`, `p3-wb-simplyhired-webmaster-2011` | P |
| Fade / split | 11 Nov 2020 | Google: "the term is becoming archaic ... very few web professionals identify themselves as webmasters ... more likely to call themselves SEO, online marketer, blogger, web developer, or site owner"; Webmasters Central renamed Search Central | `p3-google-search-central-2020` | P |

### Timeline: prompt engineer

| Milestone | Date | Evidence | Source | Grade |
| --- | --- | --- | --- | --- |
| Tool | 28 May 2020 | "Language Models are Few-Shot Learners" (GPT-3), submitted 28 May 2020 | `p3-gpt3-paper-2020` | P |
| Practice description | 2022 | Goodside "began posting GPT-3 prompt examples ... in 2022"; ChatGPT's release "the single biggest event in the history of prompt engineering" (date of ChatGPT not fetched) | `p3-gradient-goodside-2023`, `p3-interconnects-goodside-2024` | P |
| Title emergence | Feb 2023 | Daily Maverick, 19 Feb 2023: "a brand new AI job description just starting to pop up in recruiting ads". Washington Post, 25 Feb 2023: "Tech's hottest new job: AI whisperer" (headline via Willison). Goodside described as "first Staff Prompt Engineer" (Scale AI) | `p3-dailymaverick-2023-02-19`, `p3-willison-2023-02-25`, `p3-gradient-goodside-2023` | P |
| Practitioner media | Mar–Jul 2023 | a16z, 9 Mar 2023: "Will the prompt engineer be more like the highly sought after DevOps engineer, or a proficiency like Excel ...?" Semafor, Jul 2023: "This job didn't exist a year ago" | `p3-a16z-parsons-2023`, `p3-semafor-2023-07` | P |
| First community / tooling / certification / regulation | not found | — | — | NF |
| Fade | 2025 | IW Köln, 8 Jul 2025: employers "schreiben aber fast keine Stellen aus"; the prompt engineer "nicht als eigenständiger Beruf etablieren konnte". Oulu study: under 0.5% of sampled postings (72 of 20,662) | `p3-iwkoeln-prompt`, `p3-arxiv-oulu-2025` | R |
| Duty against title | Jan 2026 | RezScore (via a blog): 5 of 66,785 résumés list the title; 7,359 postings mention prompt engineering in the text | `p3-rezscore-2026` | S (low-quality secondary, read) |
| Search interest | 2023 | Indeed searches 2 → 144 per million (Jan → Apr 2023), then 20–30 per million | search summary only | S (context only) |

### Feature profile

| ID | Value | Evidence |
| --- | --- | --- |
| N01 | partial | Webmaster: no (tool 1991, word 1993) (P/R). Prompt engineer: few-shot prompting described May 2020, title early 2023, about 2.5 years (P) |
| N02 | partial | Webmaster at SGI spanned "creative, technical, production, and electronic sales" (P). Prompt engineer: no |
| N03 | no | Tool first, then title, then certification (CIW); no community found first (P/NF) |
| N04 | partial | Prompt engineer rose 2023 and was "not established" by 2025: yes (R). Webmaster fragmentation is dated only to 2020, about 27 years after the title, and postings were still rising in 2011 (P) |
| N05 | no | NF |
| N06 | no | NF; webmaster postings in 2009–11 are heavy in government contracting (P), with no software-native-first sequence |
| N07 | partial | Prompt engineering: mentions far outnumber title holders (R/S). Webmaster: NF |
| N08 | partial | Webmaster: yes. Prompt engineer: practice before title (P) |
| N09 | no | Many firms (P) |
| N10 | no | NF |
| N11 | no | NF (RFC 2142 is a technical convention, not law) |
| N12 | no | Mid-level or individual-contributor roles (P) |
| N13 | no | (P) |
| N14 | yes | Webmaster within about 2 years of the WWW (P/R); prompt engineer within months of ChatGPT and about 2.5 years of GPT-3 (P) |
| N15 | yes | Operating the web server and site; writing inputs for AI systems ("präzise und effektive Eingaben für KI-Systeme zu erstellen") (R/P) |
| N16 | partial | Prompt engineer: "zeitweise hohe Gehälter" promised, then folded rather than split (R). Webmaster: split into narrower titles (P) but no salary premium found |
| N17 | no | NF |
| N18 | no | NF |
| N19 | no | New titles appeared (P) |

---

## 5. Scarcity boom then specialisation (P4): data scientist

### Timeline

| Milestone | Date | Evidence | Source | Grade |
| --- | --- | --- | --- | --- |
| First practice description | 1 Apr 2001 (term in use earlier) | Cleveland, "Data Science: An Action Plan for Expanding the Technical Areas of the Field of Statistics" (Bell Labs record). Alvarado traces the term to the 1960s and C. F. J. Wu's 1985 call to "call ourselves ... Data Scientists" | `p4-cleveland-2001-belllabs`, `p4-arxiv-ds-1963-2012` | P / R |
| Practice in firms | by 2008–2009 | Hammerbacher "conceived, built, and led the Data team at Facebook" (CMU, 9 Apr 2009). Loukides (2 Jun 2010): Facebook's group "possibly the first data science group at a consumer-oriented web property" | `p4-cmu-hammerbacher-2009`, `p4-loukides-2010-what-is-ds` | P |
| Title emergence | 2008 | Patil (Sep 2011): "Starting in 2008, Jeff Hammerbacher and I sat down to share our experiences ... the story on how we came up with the title 'Data Scientist'" | `p4-kdnuggets-patil-2011` | P |
| First community or conference | Feb 2011 (Strata, per CSV H026; conference page not fetched) | — | `media-historical.csv` H026 only | S |
| First open tooling | not dated | Loukides 2010 names Hadoop, R and Python as the data scientist's tools; no dated release fetched | `p4-loukides-2010-what-is-ds` | P (undated) |
| First certification | Apr 2013 (S); 28 Mar 2014 (P) | INFORMS CAP, first exam Apr 2013 (search only). Cloudera "industry's first hands-on data science certification", CCP:DS | `p4-cloudera-ccpds-2014` | P (S for CAP) |
| Official occupation code | proposed 22 Jul 2016; adopted 28 Nov 2017 (2018 SOC) | "Data Scientists" (15-2051) "among the occupations new to the proposed structure"; final notice of the 2018 SOC | `soc-fr-2016-recommendations`, `p4-fr-2017-soc2018`, `p4-onet-15-2051` | P |
| Title boom / premium | Jan 2012; Oct 2012; Jan 2016 | Indeed "Data Scientist $110,000": 806 jobs (Jan 2012). HBR Oct 2012 "Sexiest Job of the 21st Century" (date only; paywalled). Glassdoor 2016: data scientist ranked first (median base $116,840, per search summary) | `p4-wb-indeed-ds-110k-2012`, `p4-hbr-2012-sexiest`, `p4-csmonitor-glassdoor-2016` | P / R (salary figure S) |
| Shortage | Dec 2017 | LinkedIn: "Data scientist roles have grown over 650 percent since 2012, but currently 35,000 people in the US have data science skills" | `p4-linkedin-emerging-2017` | P |
| Split | Dec 2017; 27 Jan 2019 | LinkedIn: machine learning engineer top emerging job, "more specialized machine learning and data-specific roles". Kaminsky, "The Analytics Engineer": a new role at "the intersection of the skill sets of data scientists, analysts, and data engineers" | `p4-linkedin-emerging-2017`, `p4-locallyoptimistic-ae-2019` | P |
| Title peak or fade | not found | — | — | NF |
| First shared metrics | not found | — | — | NF |
| Diffusion across sector types | 2013; 2017 | 2013 postings include "Clinical Data Scientist" at Target (retail). 2017: demand "in sectors like retail and finance" | `p4-wb-simplyhired-data-scientist-2013`, `p4-linkedin-emerging-2017` | P |

### Feature profile

| ID | Value | Evidence |
| --- | --- | --- |
| N01 | yes | Practice and term (2001; Facebook data team before 2008) came well before a common title (2011–12) (P/R) |
| N02 | yes | Statistics and software engineering combined ("hard scientists" writing Python, R and Hadoop) (P) |
| N03 | partial | Tools came before community (Hadoop is named in 2009–10 talks before Strata 2011), then certification (2013–14), then an occupation code (2016–17). Community was not first (P/S) |
| N04 | yes | New narrower titles (ML engineer 2017, analytics engineer 2019) within about 9–11 years of the 2008 title (P) |
| N05 | no | NF |
| N06 | partial | Web firms (Facebook, LinkedIn) → retail and finance (2013–17). No dated regulated-sector stage (P) |
| N07 | no | NF |
| N08 | no | Practice preceded title (P/R) |
| N09 | no | Two firms (Facebook, LinkedIn) plus an older academic term (P) |
| N10 | no | NF |
| N11 | no | The occupation code is statistical, not a legal mandate (P) |
| N12 | no | The early title holders' seniority varies; the role itself is not executive (P) |
| N13 | no | (P) |
| N14 | no | Not tied to one new tool in the sources read (NF) |
| N15 | no | (P) |
| N16 | yes | Premium (806 postings at $110k in Jan 2012; ranked best job in 2016), then specialised titles (2017–19) (P/R) |
| N17 | no | NF |
| N18 | partial | Recruited from other fields ("best data scientists tend to be 'hard scientists,' particularly physicists"), a move between disciplines rather than industries (P) |
| N19 | no | (P) |

---

## 6. Lead-industry diffusion (P5): brand or product management

### Timeline

| Milestone | Date | Evidence | Source | Grade |
| --- | --- | --- | --- | --- |
| First practice description | 13 May 1931 (practice older) | McElroy memo, P&G: duties of "brand men"; "In past years the brand men have been forced to do work that should have been passed on to assistant brand men" | `p5-mcelroy-memo-1931` (scan read page by page) | P |
| Title emergence | by 1931 ("brand man", "assistant brand man") | Same memo | `p5-mcelroy-memo-1931` | P |
| Owned number | 1931 | Brand man to "study carefully shipments of his brands by units", make sure money "can be expected to produce results at a reasonable cost per case" | `p5-mcelroy-memo-1931` | P |
| Diffusion in consumer goods | 1950s–mid-1960s | "not until the 1950's that it picked up steam in the USA reaching its peak in the mid-1960's" (1994 column) | `p5-um-malta-1994` | R |
| Becomes a standard | "since the 1930s" | Aimé et al.: "Since the 1930s, the Brand Manager System (BMS) has become a marketing organization standard. Yet, its relevance is questioned with the digital revolution" | `p5-repec-aime-bms`, `p5-lbs-dying-breed` | R |
| Carried to software | 1976 → 1983 | Scott Cook, P&G brand manager (joined 1976), co-founded Intuit 1983: "I took the P&G playbook and really applied it in a different category" | `p5-wisc-cook-interview` | P |
| Carried to software (2) | written c. 1996–97 (republished 2012) | Horowitz (Netscape), "Good Product Manager/Bad Product Manager": "A good product manager is the CEO of the product"; note "written 15 years ago" | `p5-a16z-horowitz-gpmbpm` | P |
| Rename or split | not dated | Norton: brand management "would come to hardware and software companies and transform into product marketing and ultimately product management"; McElroy later mentored Hewlett and Packard | `p5-bringthedonuts-mcelroy` | R |
| Community, tooling, certification, regulation, occupation code | not found | — | — | NF |
| Title peak or fade | mid-1960s peak (R); "dying breed?" question (R, undated) | — | `p5-um-malta-1994`, `p5-lbs-dying-breed` | R |
| Shared metrics | not found beyond the internal per-brand numbers in the memo | — | — | NF |

### Feature profile

| ID | Value | Evidence |
| --- | --- | --- |
| N01 | yes | "Brand men" were working before the 1931 memo; the system spread in the 1950s–60s (P/R) |
| N02 | yes | Brand men take "a very heavy share of individual brand responsibility" from Division and District (sales) Managers and own advertising spend (P) |
| N03 | no | NF |
| N04 | no | Lasted decades (R) |
| N05 | partial | Per-brand numbers (units shipped, cost per case) came from inside the firm, not from regulators; no evidence they were shared across firms (P) |
| N06 | no | Consumer goods first, software decades later (P/R) |
| N07 | no | NF |
| N08 | partial | Title and duties visible together in 1931; whether either came first is not known (P) |
| N09 | yes | P&G (P/R) |
| N10 | partial | The brand man answers for shipments by brand and cost per case (P) |
| N11 | no | NF |
| N12 | no | "Brand man" and "assistant brand man" are mid-level promotion-department posts (P) |
| N13 | no | NF |
| N14 | no | NF |
| N15 | no | (P) |
| N16 | no | NF |
| N17 | yes | Consumer goods 1931 → US spread 1950s–60s → software 1980s–90s (P/R) |
| N18 | yes | Cook (P&G → Intuit), stated directly (P) |
| N19 | no | (P) |

---

## 7. Engineering absorption (P6)

### Choice of cases

The design describes P6 as "rule work becomes configuration and policy code in platform teams; no new
title, no merged team, no new metric". Two cases were chosen before searching, for these reasons:

1. **Policy as code (Open Policy Agent, 2015–2021).** This is the literal form of the pattern: authorisation
   and compliance rules moved out of services into declarative policy run by platform teams. It is recent
   and well dated, and it reached regulated firms.
2. **Responsive web design (2010–2015).** This is a clear case of new cross-cutting work: one site for every
   device. It was taken up by existing front-end and design roles. Its dates are firm (an article, a W3C
   standard, a search-engine ranking change).

Excluded: release engineering and infrastructure as code (they did produce titles, such as DevOps
engineer), and accessibility and localisation (they have specialist titles).

### Timeline

| Milestone | Date | Evidence | Source | Grade |
| --- | --- | --- | --- | --- |
| RWD: first practice description | 25 May 2010 | Marcotte, "Responsive Web Design", A List Apart; author "an independent web designer" | `p6-ala-responsive-2010` | P |
| RWD: tooling/standard | 19 Jun 2012 | CSS3 Media Queries, W3C Recommendation | `p6-w3c-mediaqueries-2012` | P |
| RWD: vendor metric | 26 Feb 2015 (effective 21 Apr 2015) | Google: "mobile-friendliness as a ranking signal"; Mobile-Friendly Test (a vendor's test, not a practitioner metric) | `p6-google-mobile-friendly-2015` | P |
| RWD: title / occupation | none found | O*NET keyword "responsive web designer" maps to existing codes 15-1255.00 (Web and Digital Interface Designers) and 15-1254.00 (Web Developers) | `p6-onet-search-responsive` | P (absence) |
| OPA: first open tooling | 28 Dec 2015 | GitHub repository created; "general-purpose policy engine" | `gh-open-policy-agent-opa` | P |
| OPA: practice description | undated documentation | "decouple policy from the service"; "policies to be specified declaratively" | `p6-opa-docs-philosophy` | P |
| OPA: community | 29 Mar 2018 (sandbox; accepted Apr 2018) → incubation 2019 → graduation 4 Feb 2021 | CNCF; Styra engineer as "Technical Lead for OPA" | `p6-cncf-opa-sandbox-2018`, `p6-cncf-opa-graduation-2021` | P |
| OPA: diffusion | 4 Feb 2021 | "used in production by organizations like Goldman Sachs, Netflix, Pinterest, and T-Mobile"; 91% of 150+ surveyed organisations use it at some stage | `p6-cncf-opa-graduation-2021` | P |
| Certification, regulation, title, rename, shared metrics | not found | No "policy engineer" title, certification or OPA-specific metric was found | — | NF |

### Feature profile

| ID | Value | Evidence |
| --- | --- | --- |
| N01 | no | No common title ever appears (P, absence) |
| N02 | partial | RWD joins design and front-end code; OPA brings security and compliance rules into platform engineering. Absorbed into existing roles, not merged into a new one (P) |
| N03 | no | Tools and standards came first (P) |
| N04 | no | No title (P) |
| N05 | no | The only metric found is a vendor ranking signal (P) |
| N06 | partial | OPA: Netflix and Pinterest alongside Goldman Sachs and T-Mobile by 2021, so the order cannot be told apart (P) |
| N07 | partial | By construction the work is a duty, not a title; no posting counts were made (P, weak) |
| N08 | no | (P) |
| N09 | partial | OPA came from one firm (Styra); RWD from one author (P) |
| N10 | no | NF |
| N11 | no | NF |
| N12 | no | NF |
| N13 | no | NF |
| N14 | no | No title boom (P) |
| N15 | partial | The work is writing configuration and policy code (CSS media queries, Rego) (P) |
| N16 | no | NF |
| N17 | no | NF |
| N18 | no | NF |
| N19 | yes | No new title or occupation; no practitioner metric (P, absence-based) |

---

## 8. Final table: patterns × features (input to the scoring script)

The same values, with grades, are in `signatures.csv` (columns pattern, feature_id, feature, value, grade).

| Feature | DevOps | SRE | Mandated officer | Tool-operator fade | Scarcity boom then specialisation | Lead-industry diffusion | Engineering absorption |
|---|---|---|---|---|---|---|---|
| N01 practice described >=2 years before a common title | yes | no | partial | partial | yes | yes | no |
| N02 duties from two previously separate functions merged | yes | yes | no | partial | yes | yes | partial |
| N03 community before tooling before certification before regulation | partial | partial | partial | no | partial | no | no |
| N04 title rose then fragmented or was renamed within ~10 years | partial | no | no | partial | yes | no | no |
| N05 shared metrics originated with practitioners, not regulators | yes | yes | no | no | no | partial | no |
| N06 diffusion from software-native to enterprise to regulated sectors | yes | partial | no | no | partial | no | partial |
| N07 more postings carry the practice as a duty/skill than as a title | partial | no | no | partial | no | no | partial |
| N08 title and practice appeared together | no | yes | partial | partial | no | partial | no |
| N09 single-firm origin | no | yes | partial | no | no | yes | partial |
| N10 authority from an owned number | no | yes | no | no | no | partial | no |
| N11 title tied to a legal text | no | no | yes | no | no | no | no |
| N12 senior/executive at first appearance | no | no | yes | no | no | no | no |
| N13 certification/statute before practitioner community | no | no | partial | no | no | no | no |
| N14 title boom within 2-3 years of a new tool | partial | no | no | yes | no | no | no |
| N15 duties are operating a tool | partial | no | no | yes | no | no | partial |
| N16 salary-premium title boom then split into narrower titles | no | no | no | partial | yes | no | no |
| N17 mature in one industry long before others | partial | partial | partial | no | no | yes | no |
| N18 carried by people moving between industries | no | partial | no | no | partial | yes | no |
| N19 no new title, team or metric (absorbed into engineering) | no | no | no | no | no | no | yes |

### Notes for scoring

- **Where the historical record contradicts the design's own signatures.** DevOps D3 order: tooling (Chef,
  Puppet) came before the first community, so N03 is `partial`. DevOps D4 rename: platform engineering is
  dated 2023, about 14 years on, so N04 is `partial`. Data scientist matches the DevOps features N01, N02 and
  N04 at least as well as DevOps does. Present-day evidence that fits N01, N02 or N04 does not by itself
  separate H-DevOps from P4.
- **Separating features in the historical record.** DevOps alone has `yes` on both N05 and N06. N05 is
  shared with SRE, and N06 is not shared with any pattern. N10 and N08 separate SRE. N11 and N12 separate P2.
  N14 and N15 separate P3. N16 separates P4. N17 and N18 separate P5. N19 separates P6.
- **`no` with grade NF** means the feature was not found. It does not mean absence was shown. A script that
  wants to treat such cells as missing can filter on `grade == NF`.

---

## 9. Sources (grades)

P = primary, read; R = reputable secondary, read; S = search summary only, or a low-quality secondary.
File = `corpus/b-raw/signatures/<id>.txt`.

### DevOps

| ID | Source | Date | Grade |
| --- | --- | --- | --- |
| dv-crossref-debois-2008 | Crossref record, Debois, Agile 2008 (DOI 10.1109/agile.2008.42) | Aug 2008 | P |
| dv-debois-agile2008-slides | Debois, Agile Infrastructure & Operations slides (Wayback 2010 capture of jedi.be) | 2008 | P |
| dv-agileadmin-velocity2008 | Mueller, "The Velocity 2008 Conference Experience – Part I" | 23 Jun 2008 | P |
| dv-dck-velocity2009 | Data Center Knowledge, "Velocity: Flickr on Devs, Ops and Teamwork" | 25 Jun 2009 | P |
| dv-hammond-velocity2009 | Hammond, "Dev and Ops Cooperation at Velocity 2009" | 28 Jun 2009 | P |
| dv-wb-devopsdays-2009 | devopsdays.org homepage, Wayback 2009 | 2009 | P |
| dv-devopsdays-ghent-2009-program | Ghent 2009 programme | 2009 | P |
| dv-devopsdays-2009-legacy | legacy.devopsdays.org Ghent 2009 | 2009 | P |
| dv-infoq-5yrs | InfoQ, interview with Debois and Buytaert, "5 years DevOps Days" | Dec 2014 | P (participant recollection) |
| gh-chef-chef | GitHub API, chef/chef created_at | 2009-01-15 | P |
| dv-sodr-2013-blog | Puppet Labs, "2013 State of DevOps: Benchmark your organization" (Wayback) | Mar 2013 | P |
| dv-sodr-2014 | 2014 State of DevOps Report (dora.dev PDF) | Jun 2014 | P |
| dv-sodr-2018 | Accelerate: State of DevOps 2018 (PDF) | 2018 | P |
| dv-aws-devops-cert-2014 | AWS, "New AWS Certification Available for DevOps Engineers" | 7 Nov 2014 | P |
| dv-wb-simplyhired-devops-engineer-2011 | SimplyHired "devops engineer", Wayback | 15 Mar 2011 | P |
| dv-wb-simplyhired-devops-2012 | SimplyHired "devops", Wayback | 28 Nov 2012 | P |
| dv-wb-indeed-devops-engineer-2014 | Indeed "Devops Engineer", Wayback | 30 Jul 2014 | P |
| dv-cncf-platforms-announce | CNCF blog, platforms white paper announcement | 11 Apr 2023 | P |
| dv-cncf-platforms-wp | CNCF Platforms White Paper | 2023 | P |
| dv-dol-nof-devops-2025 | US DOL OA Bulletin 2025-82, NOF DevOps Engineer | 24 Apr 2025 | P |
| dv-onet-15-1252 | O*NET 15-1252.00 Software Developers | current | P |
| — | State of DevOps 2013 full PDF (Puppet, dora.dev): 404, not read | — | — |
| — | Google Trends "devops": HTTP 429, not read | — | — |

### SRE

| ID | Source | Date | Grade |
| --- | --- | --- | --- |
| sre-book-intro | Google SRE book, Introduction (Treynor Sloss) | 2016 | P |
| sre-lisa06 | USENIX LISA '06, Limoncelli | 2006 | P |
| sre-srecon14-home | USENIX SREcon14 page | May 2014 | P |
| sre-srecon14-keys | SREcon14, Treynor "Keys to SRE" | May 2014 | P |
| sre-srecon14-program | SREcon14 programme (speaker bios) | May 2014 | P |
| sre-srecon14-healthcaregov | SREcon14, Dickerson | May 2014 | P |
| sre-srecon16-slo | SREcon16, Jones and Murphy, SLOs and error budgets | 2016 | P |
| sre-lisa15-krishnan | LISA15, Krishnan | 12 Nov 2015 | P |
| sre-srecon24-murphy | SREcon24, Murphy "20 Years of SRE" | 18 Mar 2024 | P |
| sre-prodcast-treynor | Google SRE Prodcast with Treynor Sloss | 18 Sep 2024 | P |
| sre-devopsinst-sre-foundation-2019 | DevOps Institute press release, SRE Foundation | 29 Oct 2019 | P |
| sre-onet-search | O*NET keyword search "site reliability engineer" | current | P |

### Mandated officer

| ID | Source | Date | Grade |
| --- | --- | --- | --- |
| p2-katz-1997-hearing | Statement of Stephen R. Katz, House Science Committee | 6 Nov 1997 | P |
| p2-exabeam-katz-2020 | Exabeam podcast page, "Lessons Learned from the First CISO" | 3 Sep 2020 | P (page summary) |
| p2-isc2-history | (ISC)² about page | current | P (organisation self-history) |
| p2-wb-isc2-1998 | (ISC)² homepage, Wayback | Dec 1998 | P |
| p2-iapp-about | IAPP about page | current | P (organisation self-history) |
| p2-bdsg-1977-bgbl | BDSG, BGBl. I 1977 S. 201 (Paderborn scan) | 27 Jan 1977 | P |
| p2-computerwoche-bdsg-1977 | Computerwoche, "BDSG unterzeichnet" | 4 Feb 1977 | P |
| p2-dir9546-eurlex | Directive 95/46/EC | 24 Oct 1995 | P |
| p2-gdpr-eurlex | Regulation (EU) 2016/679 | 27 Apr 2016 | P |
| p2-ussc-1991-ch8 | US Sentencing Guidelines Manual 1991, Chapter 8 | 1 Nov 1991 | P |
| p2-fr-2003-sec-cco | SEC final rule IA-2204, 68 FR 74714 | 24 Dec 2003 | P |
| p2-fisma-2002 | Public Law 107-347 (E-Government Act; FISMA Title III) | 17 Dec 2002 | P |
| p2-ecfr-16cfr314 | 16 CFR Part 314 (Safeguards Rule), current with history notes | 2002 / 2021 | P |
| p2-nyc-polonetsky-2000 | NYC Mayor's press release #092-00 | 5 Mar 2000 | P |
| p2-cw-ibm-cpo-2000 | Computerworld, "IBM joins chief privacy officer trend" | 29 Nov 2000 | P |
| — | NYDFS 23 NYCRR 500 text: fetch failed, not used | — | — |
| — | BLS SOC 2000 13-1041: blocked, not used | — | — |

### Tool-operator fade

| ID | Source | Date | Grade |
| --- | --- | --- | --- |
| p3-tbl-1991-announce | Berners-Lee, alt.hypertext post | 6 Aug 1991 | P |
| p3-edge-kipparent-1996 | Brockman, Digerati ch. 23, Kip Parent | 1996 | P |
| p3-rfc2142-1997 | RFC 2142, Mailbox Names | May 1997 | P |
| p3-novell-ciw-2000 | Novell/ProsoftTraining press release, CIW | 5 Dec 2000 | P |
| p3-princetonreview-webmaster | Princeton Review, Webmaster career profile | undated | R |
| p3-wb-simplyhired-webmaster-2009 | SimplyHired "Webmaster", Wayback | 23 Feb 2009 | P |
| p3-wb-simplyhired-webmaster-2011 | SimplyHired "webmaster", Wayback | 6 May 2011 | P |
| p3-google-search-central-2020 | Google, "Goodbye Google Webmasters, hello Google Search Central" | 11 Nov 2020 | P |
| p3-gpt3-paper-2020 | arXiv 2005.14165 | 28 May 2020 | P |
| p3-gradient-goodside-2023 | The Gradient podcast, Goodside | 1 Jun 2023 | P |
| p3-twiml-goodside-2023 | TWIML 652, Goodside | 23 Oct 2023 | P |
| p3-interconnects-goodside-2024 | Interconnects, Goodside interview transcript | 30 Sep 2024 | P |
| p3-a16z-parsons-2023 | a16z podcast, Guy Parsons | 9 Mar 2023 | P |
| p3-dailymaverick-2023-02-19 | Daily Maverick, prompt engineer | 19 Feb 2023 | P |
| p3-willison-2023-02-25 | Willison blog linking the Washington Post article | 25 Feb 2023 | P (headline only) |
| p3-semafor-2023-07 | Semafor newsletter, Goodside | 21 Jul 2023 | P |
| p3-iwkoeln-prompt | IW-Kurzbericht 57/2025, Engler | 8 Jul 2025 | R |
| p3-arxiv-oulu-2025 | arXiv 2506.00058, prompt engineer skills in LinkedIn postings | 2025 | R |
| p3-rezscore-2026 | Profolio blog on RezScore/Adzuna data | 2026 | S (low-quality secondary) |

### Scarcity boom then specialisation

| ID | Source | Date | Grade |
| --- | --- | --- | --- |
| p4-cleveland-2001-belllabs | Nokia Bell Labs publication record, Cleveland 2001 | 1 Apr 2001 | P (record only) |
| p4-arxiv-ds-1963-2012 | Alvarado, "Data Science from 1963 to 2012" | 2023/24 | R |
| p4-cmu-hammerbacher-2009 | CMU PDL SDI seminar, Hammerbacher | 9 Apr 2009 | P |
| p4-loukides-2010-what-is-ds | Loukides, "What is data science?", O'Reilly Radar | 2 Jun 2010 | P |
| p4-kdnuggets-patil-2011 | KDnuggets excerpt of Patil, Building Data Science Teams | Sep 2011 | P (excerpt) |
| p4-hbr-2012-sexiest | HBR, Davenport and Patil (paywalled; date and summary only) | Oct 2012 | P (metadata only) |
| p4-wb-indeed-ds-110k-2012 | Indeed "Data Scientist $110,000", Wayback | 28 Jan 2012 | P |
| p4-wb-simplyhired-data-scientist-2013 | SimplyHired "data scientist", Wayback | 25 Aug 2013 | P |
| p4-cloudera-ccpds-2014 | Data Center Knowledge, Cloudera CCP:DS | 28 Mar 2014 | P |
| p4-csmonitor-glassdoor-2016 | CS Monitor on Glassdoor best jobs 2016 | 20 Jan 2016 | R |
| soc-fr-2016-recommendations | 81 FR (2016-17424), SOC Policy Committee recommendations | 22 Jul 2016 | P |
| p4-fr-2017-soc2018 | 82 FR 56271 (2017-25622), SOC revision for 2018 | 28 Nov 2017 | P |
| p4-onet-15-2051 | O*NET 15-2051.00 Data Scientists | current | P |
| p4-linkedin-emerging-2017 | LinkedIn 2017 US Emerging Jobs Report | Dec 2017 | P |
| p4-locallyoptimistic-ae-2019 | Kaminsky, "The Analytics Engineer" | 27 Jan 2019 | P |
| — | INFORMS CAP 2013; Glassdoor median salary figure | — | S |

### Lead-industry diffusion

| ID | Source | Date | Grade |
| --- | --- | --- | --- |
| p5-mcelroy-memo-1931 | McElroy memo (3-page scan; transcribed by reader) | 13 May 1931 | P |
| p5-bringthedonuts-mcelroy | Norton, "Product Management Was Born in 1931 (Maybe, Sort Of)" | 2021 | R |
| p5-um-malta-1994 | Caruana, brand manager system column (Univ. of Malta repository) | 1994 | R |
| p5-repec-aime-bms | Aimé, Berger-Remy, Laporte, BMS twenty years after Low and Fullerton (abstract) | c. 2015–17 | R |
| p5-lbs-dying-breed | LBS record of the same paper | — | R |
| p5-wisc-cook-interview | Wisconsin School of Business, conversation with Scott Cook | undated (recent) | P |
| p5-a16z-horowitz-gpmbpm | Horowitz, Good Product Manager/Bad Product Manager | c. 1996–97; republished 2012 | P |
| — | Low and Fullerton 1994 (JMR): not read | — | — |

### Engineering absorption

| ID | Source | Date | Grade |
| --- | --- | --- | --- |
| p6-ala-responsive-2010 | Marcotte, "Responsive Web Design" | 25 May 2010 | P |
| p6-w3c-mediaqueries-2012 | W3C Media Queries Recommendation | 19 Jun 2012 | P |
| p6-google-mobile-friendly-2015 | Google, "Finding more mobile-friendly search results" | 26 Feb 2015 | P |
| p6-onet-search-responsive | O*NET keyword "responsive web designer" | current | P |
| gh-open-policy-agent-opa | GitHub API, OPA created_at | 2015-12-28 | P |
| p6-opa-docs-philosophy | OPA documentation, Philosophy | current | P |
| p6-cncf-opa-sandbox-2018 | CNCF blog, CNCF to host OPA | 29 Mar 2018 | P |
| p6-cncf-opa-graduation-2021 | CNCF announcement, OPA graduation | 4 Feb 2021 | P |

### Media-historical CSV items used (metadata only unless a page ID is listed above)

H001 → `sre-lisa06`; H002 → `sre-srecon14-keys`; H003 → `sre-srecon14-healthcaregov`; H004 →
`sre-lisa15-krishnan`; H005 → `sre-srecon16-slo`; H006 → `sre-prodcast-treynor`; H007 →
`sre-srecon24-murphy`; H008 → `dv-agileadmin-velocity2008`; H009 → `dv-dck-velocity2009`,
`dv-hammond-velocity2009` (the video itself was not watched); H023 → `p4-cmu-hammerbacher-2009`;
H026 (Strata 2011) metadata only (S); H030 → `p2-katz-1997-hearing`; H036 → `p2-exabeam-katz-2020`;
H038 → `p3-a16z-parsons-2023`; H039 → `p3-gradient-goodside-2023`; H041 → `p3-twiml-goodside-2023`;
H045 → `p3-interconnects-goodside-2024`; H049 → `p3-edge-kipparent-1996`. H022 (Varian, McKinsey) and the
McKinsey 2011 big data report timed out and were not used.
