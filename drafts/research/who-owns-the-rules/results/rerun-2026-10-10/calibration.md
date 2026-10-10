# Calibration test (loop-design-v2.md section 8): result

Run 2026-10-10 · code `loop-tools/calibration_code.py` · codes `calibration-codes.csv` · raw coder output in
`corpus/b-raw/calibration/` (git-ignored). Opened: design sections 4, 8, 9; `media-historical.csv`; the H
transcripts and manifest; `signatures.csv` and `signatures.md` for written milestones only.

## Verdict (H-cal)

**Refuted, as pre-registered.** For two of the three tested roles (DevOps, CISO) the earliest recording in which
both coders find the authority arrangement is no earlier than postings or official documents. SRE is the only one of
the three where the recording comes first, and by a margin of months against the one written source on the
arrangement (2016), not the two years the hypothesis needs. Under the design's rule (section 8.5), S7 findings
(practitioner speech) are reported as descriptive only.

## Coverage

All 20 H transcripts on file were coded (the manifest marks H009, H030, H049 as "exists" but their files are present).
Other frame items have no transcript on file (unavailable, unfetched or not attempted). H030 (House hearing statement) and H049 (Edge
interview text) are written pages with no timestamps; they are in the set because the frame includes them, and they
are written rather than spoken sources.

| Role | Recordings coded | Dates | Missing from the frame (unavailable) |
| --- | --- | --- | --- |
| SRE | H004, H005, H007 | 2015-11, 2016, 2024-03 | H001 (LISA 2006), H002/H003 (SREcon14), H006 (not on file) |
| DevOps | H009, H011, H013, H014 | 2009-06, 2010-05, 2012-09, 2012-09 | H008, H010, H012 (Debois) not on file |
| CISO | H030, H033, H036, H037 | 1997-11, 2007-02, 2020-09, 2021-03 | H031, H032, H034, H035 not on file |
| Data scientist | H029 | 2021-08 | H022, H023, H027, H026 unavailable or not on file |
| Prompt engineer | H038-H041 | 2023-03 to 2023-10 | none |
| Chief knowledge officer | H047 | 2016-05 | earlier CKO items not on file |
| Social media manager | H018, H021 | 2009-05, 2010-10 | H015, H016, H019 unavailable |
| Webmaster | H049 | 1996-10 | none |

The earliest recordings for SRE (2006, 2014) and the second-earliest CISO items (2003, 2005) are exactly the ones
missing.

## Coder agreement (n = 20 recordings, A = claude-sonnet-5-5, B = claude-haiku-5-5)

An item counts as present only if the coder said so and gave at least one verbatim quote of 40 words or fewer.
(Every "present" had verbatim quotes, so effective and raw codes are identical.)

| Item | Raw agreement | Cohen's kappa | A yes / B yes |
| --- | --- | --- | --- |
| (a) activity bundle | 0.90 | 0.44 | 18 / 18 |
| (b) authority arrangement | 0.95 | 0.89 | 7 / 6 |
| (c) role title | 0.95 | 0.83 | 17 / 16 |

Item (a) has a low kappa because it is almost always "yes" (a high base rate), with two disagreements (H007, H033).
Item (b), the one the test turns on, disagrees once (H011).

## Coded authority arrangement, by recording (b: both coders agree unless noted)

| Role | Recording (frame date) | Coders | Evidence (shortest agreed quote) |
| --- | --- | --- | --- |
| SRE | H004 (2015-11-12) | both yes | "we absolutely need to mandate like a shift system" (00:22:36). Weak: an internal rule for staff on disaster tests |
| SRE | H005 (2016) | both yes | "SRE needs to have the authority to halt launches which will exceed the error budget" (00:21:41). Clear case |
| SRE | H007 (2024-03) | both no | |
| DevOps | H014 (2012-09-25) | both yes | A: developers pushing their own code (00:14:27); B: an "operability review" with yes/no questions (00:34:52). Weak: a process, not a trade-off agreement |
| DevOps | H011 (2010-05-20) | A yes, B no | A: "what was measured on us ... mean time to detect and ... resolve" (00:22:19). Not agreed |
| DevOps | H009, H013 | both no | |
| CISO | H036 (2020-09-03) | both yes | "I said $400,000. I said, go do it." (00:16:11). A retrospective of events from the 1990s |
| CISO | H037 (2021-03) | both yes | a risk acceptance process; "you have the right to move forward with this" (00:14:56 to 00:15:39). Retrospective |
| CISO | H030 (1997), H033 (2007) | both no | H030 uses the title in the introduction; no arrangement stated |
| CKO | H047 (2016-05-03) | both yes | "On top of a 40% budget cut" (00:13:31); three conditions the speaker set for taking the job (00:14:15) |
| Data scientist, prompt engineer, social media manager, webmaster | H029, H038-H041, H018, H021, H049 | both no | |

## Written side (signatures.csv and signatures.md; dated, graded entries only)

Earliest dated written description of the authority arrangement, and the year postings used the title:

| Role | Earliest written description of the arrangement | Postings used the title | Official or other dated documents |
| --- | --- | --- | --- |
| SRE | Error budget and the SLO model published in the SRE book and SREcon16 talk, 2016 (P; month not given). Treynor's 2003 account is a published 2016 retelling, not a 2003 text | NF: no dated SRE postings; only "outside Google by 2012" from a conference programme (P) | Vendor certification 29 Oct 2019 (P); no own occupation code (P, absence) |
| DevOps | NF as an arrangement. The nearest are the cooperation talks (Debois, Aug 2008, P; Velocity 23 Jun 2009, P) and DORA metrics (Mar 2013, P), which are benchmarks (N10 = no) | Mar 2011 (134 SimplyHired results, P); growing Nov 2012 (P) | AWS certification 7 Nov 2014 (P); DOL framework 2025 (P) |
| CISO | Statute: FISMA 17 Dec 2002 "designating a senior agency information security officer" (P). Earlier written: Katz hearing statement 6 Nov 1997 (title and function, P; coded no on the arrangement here) | NF | FISMA 2002 (P); FTC Safeguards Rule May 2002 and its 2021 amendment (reports to the board; P); CISO title 1995 at Citibank (P) |
| Data scientist | NF (N10 = no, NF) | Jan 2012 (806 jobs at $110k, Indeed, P); title coined 2008 | SOC 2018 code adopted 28 Nov 2017 (P) |
| Prompt engineer | NF | Feb 2023 (recruiting ads, P) | none (no code, NF) |
| Chief knowledge officer | NF: not in the signatures | NF | NF |

Social media manager and webmaster are also not covered for the arrangement (no entry).

## Lead times (earliest agreed recording minus earliest written source)

Positive means the recording came first. Year-level granularity; a "month" figure is only as good as the
dates given.

| Role | Earliest agreed recording | Against the written arrangement | Against postings | Against official documents |
| --- | --- | --- | --- | --- |
| SRE | H004, 2015-11 (weak); H005, 2016 (clear) | about 0 to +0.5 year vs the 2016 book (H005 is in 2016 as well, so 0) | NF | +3.9 years vs certification (Oct 2019) |
| DevOps | H014, 2012-09 | NF | **-1.5 years** vs Mar 2011 postings | +2 years vs certification (Nov 2014) |
| CISO | H036, 2020-09 | **-17.7 years** vs FISMA Dec 2002 | NF | **-17.7 years** vs FISMA |
| CKO (comparison) | H047, 2016-05 | NF | NF | NF |
| Data scientist, prompt engineer (comparison) | none agreed | NF | not applicable | not applicable |

Pre-registered test: refuted if for two or more of SRE, DevOps and CISO the earliest recording is no earlier than
postings or official documents.
- SRE: recording earlier than the only dated official document (2019) and no postings are dated, so it does not meet the refutation condition. It also does not show a two-year lead over the written arrangement.
- DevOps: recording (Sep 2012) later than postings (Mar 2011). Meets the condition.
- CISO: recording (Sep 2020) later than the statute (Dec 2002) and the 1997 testimony. Meets the condition.
Result: 2 of 3, so H-cal is refuted. The hypothesis's own positive claim, a two-year lead of speech over
postings, was observed in none of the three.

## Caveats

- **Small n.** Eight roles, one to four recordings each; the three tested roles have 3 to 4 recordings, and
  only 2 to 4 coder-agreed authority hits in total. One extra recording could move the lead times by years.
  Kappa from 20 items with 6 to 7 positives on item (b) is imprecise.
- **Gaps in the historical frame.** The earliest recordings for SRE (H001 2006, H002/H003 2014), DevOps (Debois,
  2009 to 2011) and CISO (2003, 2005) were unavailable or not on file. The finding is therefore "no earlier than
  the earliest available recording", which makes the test biased toward refutation. The frame came from targeted
  searches for known roles, so it says nothing about roles that did not last.
- **Retrospective recordings.** The two CISO hits (2020, 2021) are the first CISO telling stories from the 1990s.
  Coding by recording date, as the design says, dates the telling, not the events. The same applies to H047 (2016).
- **Written side is thin on the arrangement itself.** The signatures document milestones (practice, title,
  certification, statute), not who may decide what. "Earliest written description of the arrangement" was
  therefore taken from the 2016 SRE book, FISMA 2002, and NF for DevOps. NF means not found in the historian's
  session, not absent. Postings years rest on search-result pages (SimplyHired, Indeed) for DevOps and data
  scientist only.
- **Coder quality.** Some agreed hits are weak (H004 and H014 are about internal rules or review steps, not a
  trade-off agreement); only H005 states a clear authority to halt launches. A stricter reading of (b) would leave
  one SRE hit and no DevOps hit, which does not change the verdict (the test then fails for DevOps on NF rather than
  on dates).
- **Transcript errors.** Whisper transcripts misname people and terms (H004's speaker header reads "CRYPA EVANS"
  for Kripa Krishnan; "Crepa" in the text) and include no speaker labels; quotes were checked against the text as
  transcribed. H030 and H049 have no timestamps. H009's speakers do not say "DevOps" at all in the 2009 talk,
  which the (c) code correctly reports as no.
- **Contamination.** The coders are models that know how these roles turned out. The prompt forbade comment on
  persistence, but hindsight in what they treat as an "authority arrangement" cannot be ruled out. The two coders
  are from the same model family.
