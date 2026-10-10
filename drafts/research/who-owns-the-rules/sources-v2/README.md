# Media frames for loop v2

Sampling frames of recorded practitioner speech, built on 10 October 2026 from web-search results only (no
page was opened). They list what to fetch later; they contain no transcripts.

| Frame | Items | URL, title and speaker confirmed | Use |
| --- | --- | --- | --- |
| `media-current.csv` | 90 podcast episodes and YouTube videos, 2024–2026, ten functions | 34 | Stratum S7: people who run functions that use agents describing their work |
| `media-historical.csv` | 52 talks, podcasts and hearings, 1996–2024, eight roles | 15 | Calibration test (loop-design-v2.md, section 8) |

**Cleaned 10 October 2026** (rerun, `cleaning-log.csv`): current frame 87 items (3 dropped as pre-2024), 74 confirmed, 24 vendor or consultant; historical frame 52 items, 39 confirmed. Only 2 confirmed COO items.

## How the frames were built

Searches named a speaker's role and function, never a topic: no "rules", "policy", "governance",
"override" or our own terms. Each row records the query that found it. Vendor and consultant speakers are
flagged and kept under a third of the current frame (22 of 90).

## Before sampling: clean the frames

`fetch_media.py` samples only rows marked `confirmed = yes` unless run with `--include-partial`. To confirm
a partial row:

1. Replace show-page URLs with the episode URL, from the show's RSS feed (18 current rows have a show page
   and a title beginning "unknown").
2. Fill the date from the feed or the video page; drop current items dated before January 2024 (check M073,
   M005, M006, M008, M009, M046).
3. Check the speaker's role and organisation, and the function label, against the episode page.
4. Set `transcript` to `page` or `captions` where one exists.
5. Set `confirmed` to `yes`. Don't change rows for any other reason: the frame is fixed before sampling.

Record every change in a commit of its own, before any transcript is coded.

## Known gaps

- **Current frame:** few sitting COOs describing their own deployments; no in-house accounts payable
  manager; procurement relies on two shows; several YouTube items name no speaker.
- **Historical frame:** no audio or video before 2005 for the CISO, chief knowledge officer or webmaster (the
  earliest CISO item is a 1997 House hearing transcript); no public SRE talk found from 2007 to 2013; DevOps
  items unconfirmed. The CISO calibration case may need written period sources instead, coded the same way.
