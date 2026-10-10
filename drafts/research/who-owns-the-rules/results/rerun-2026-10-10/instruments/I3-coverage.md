# I3 coverage (collected 2026-10-10)

Collection only. Postings are single job pages fetched in id_ form from the Internet Archive, selected by title.

## Counts per history per year (snapshot year)

| History | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (a) DevOps and operations, 2008-2016 | 0 | 0 | 0 | 0 | 12 | 12 | 11 | 3 | 11 | 11 | 60 |
| (b) Trading controls, 2005-2016 | 6 | 4 | 2 | 3 | 0 | 1 | 0 | 0 | 1 | 0 | 17 |
| (c) Grid control room, 2005-2016 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 5 |

Sources: (a) jobs.github.com, careers.stackoverflow.com; (b) efinancialcareers.com (2007-08, mostly recruiter-posted), jobview.monster.com; (c) jobview.monster.com, careers-pjm.icims.com (2010, 3 PJM postings: Master Coordinator system operator, Sr. Trainer for operator training, transmission planning Engineer; the last two are adjacent to, not in, the control room).
Max 3 postings per employer applied. Employer is as shown on the page (recruiters appear as employers).

## Gaps

- Target was 30-60 per history. (a) meets it; (b) has 17; (c) has 2.
- (a) has nothing for 2008-2010 (the formative DevOps years) and only 3 for 2014. GitHub Jobs starts 2011; Stack Overflow Careers captures are 2015-16.
- (b) has nothing for 2005-06 and 2011-2016 except 2 postings. Titles are mostly "trading systems support", algorithmic or high-frequency trading specialists and risk control roles; few postings use market-access or pre-trade control titles. Several are developer-adjacent rather than controls roles.
- (c) is effectively empty. Title-prefix queries for system operator, reliability coordinator, transmission operator and control room operator returned mostly power-plant control-room postings (excluded, apart from one Dominion generation control room posting). No ISO/RTO or utility career page capture with a single posting was found: PJM, ERCOT, CAISO, NYISO and MISO career URLs returned only landing pages or nothing.

## Limited by archive access (do not read as absence)

- The Wayback CDX endpoint timed out and refused connections for much of the session (rate limiting after heavy use; the coordinator later instructed 1 CDX request per 10 s with backoff). Many planned queries failed, in particular: Indeed viewjob title prefixes, Monster title prefixes for DevOps, most trading prefixes, most grid prefixes, Dice, CareerBuilder, SimplyHired, Craigslist, and employer career pages of banks, exchanges, ISOs/RTOs and utilities.
- Fetching was throttled; of 1000 sampled efinancialcareers captures only about 179 were retrieved before stopping. Only 2007-2008 efinancialcareers captures were listed.
- The availability API was not used; no known-URL career pages were identified to feed it.
- Histories and years most limited: (c) all years; (b) 2005-06 and 2011-2016; (a) 2008-2010 and 2014.

## Addendum: availability-API pass (no CDX), 2026-10-10

Targets were grid 20 and trading 30. Result: grid 5 (+3), trading 17 (+0). Targets not met.
- Method: archive.org/wayback/available at 3 s spacing for about 100 employer career URLs x even years 2006-2016, then snapshot fetches (id_) of landing pages and their links.
- Landing pages captured: PJM (2009, 2012, 2015), ERCOT (2008, 2012, 2014, 2016), CAISO (2015), ISO-NE (2014), SPP (2008-2016), NERC, FINRA (2008-2010), ICE (2012, 2013), NYX (2012, 2013), Nasdaq OMX (2010-2015), CBOE (2006-2016), DTCC (2008-2016), CME (2015), JPMorgan, Goldman Sachs, SEC.
- Postings reachable: only PJM's icims job pages (2010). Individual posting URLs linked from other landing pages were not archived: ERCOT 2008 list (System Operator 1, 2, Sr. and about 50 other roles; none captured), ICE JobPostings.shtml?job.id= (about 45 titles in 2012 and 2013 lists, including Risk Analyst, Market Regulation Analyst, Trade Operations Analyst; none captured), FINRA recruitmax and Taleo, Nasdaq Taleo, CBOE UltiPro.
- No capture at all for MISO, NYISO, CAISO CurrentJobs, ISO-NE open-positions, NERC employment, CMEGroup job pages, NYSE careers.
- Web search (title-based) only returned current third-party postings; no use for 2005-2016 URLs.
- Remaining gaps: grid 2005-2009 and 2011-2016 (all but 2009, 2010, 2014); trading 2005-06 and 2011-2016; any ISO/RTO other than PJM; any exchange or bank posting. The ICE and ERCOT title lists above are evidence that such postings existed; recovering them needs CDX or another source of exact URLs.
