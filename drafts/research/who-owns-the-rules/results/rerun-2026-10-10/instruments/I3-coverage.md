# I3 coverage (collected 2026-10-10)

Collection only. Postings are single job pages fetched in id_ form from the Internet Archive, selected by title.

## Counts per history per year (snapshot year)

| History | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (a) DevOps and operations, 2008-2016 | 0 | 0 | 0 | 0 | 12 | 12 | 11 | 3 | 11 | 11 | 60 |
| (b) Trading controls, 2005-2016 | 6 | 4 | 2 | 3 | 0 | 1 | 0 | 0 | 1 | 0 | 17 |
| (c) Grid control room, 2005-2016 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |

Sources: (a) jobs.github.com, careers.stackoverflow.com; (b) efinancialcareers.com (2007-08, mostly recruiter-posted), jobview.monster.com; (c) jobview.monster.com.
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
