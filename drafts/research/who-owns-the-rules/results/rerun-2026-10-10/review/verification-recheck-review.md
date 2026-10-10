# Verification recheck: adversarial review (2026-10-10)

**Recommended headline (random150, CSV as it stands):** Of 130 checkable claims, 87 (67%) were confirmed by an acquired source, 4 (3.1%, 95% CI 1.2–7.6%) were contradicted by one, and 39 (30%, 22.8–38.4%) had no supporting passage in the corpus, 16 of them because the cited page was never acquired.

If the two misclassifications below are fixed, this becomes 88 confirmed, 5 contradicted (3.8%, 1.7–8.7%) and 37 unsupported (28.5%, 21.4–36.7%).

## The counts reproduce exactly
Every tally matches the CSVs. random150: 87/4/39/20; 43/130 = 33.1% (25.6–41.5%); 27/114 = 23.7% (16.8–32.3%). Industry: 31/20/4/15. Loop-redteam: 52/9/0/9. Loop-analysis is unchanged (122/4/1). Exactly 12 rows flipped to confirmed (8 from unverifiable, 4 from not found). The "16 never acquired" figure holds if it means rows where the cited ids are failed or needs-browser: I count 15 where every cited id failed, plus CL0711 (2 of 3 failed). Six more not-found rows cite a stub or the wrong page (CL1656, CL0963, CL2115, CL1523, CL1578, CL0397). So 22 of the 39 rest on the cited item being absent, not on a check against its text.

Industry deserves its own line: 20 of 55 checkable claims (36%, 24.9–49.6%) were contradicted by a source. That is a real error rate, and much higher than random150's.

## Not found is mostly right, but 2 of 12 are wrong
I searched `corpus/text` and the text folders under `b-raw` (filings, postings, history, onet, signatures, vendor, mapping, seeds) for 12 rows. Seven of those rows cite pages that were never acquired.

- **CL2011 should be confirmed.** The cited PER-005-2 PDF (`Cb1d56448`) has a version table reading "2 2/6/2014 Adopted by the NERC Board of Trustees". The rechecker searched long-form dates only and missed the numeric format.
- **CL1680 should be corrected.** The cited Talkdesk page (`Cfa61a3c0`) says "The application was posted on 04/14/2026". The claim of 11 May 2026 is contradicted, not merely unsupported.
- These eight hold: CL1242, CL1442, CL2041, CL1327, CL2037 and CL1237 (all not acquired), plus CL1618 and CL0864. Two leads turned out to be false: a Memorial Hermann posting rates Epic Clinical Builder as "preferred" with no 90-day clause, and the only "March 13, 2019" hits are spam comments.
- **CL0393 is about half confirmable.** The DSA's 2022 date appears in the corpus (Regulation (EU) 2022/2065; a 10-K gives entry into force on 17 Nov 2022). NetzDG appears without a date.
- **CL1618's evidence column is wrong.** It cites Databricks, but the claim is about Scale AI. The verdict stands.

A 2-in-12 miss rate suggests that about 5–7 of the 39 not-found rows may be misfiled.

## Of the 12 flips to confirmed, 7 are fully supported and 5 only partly
Every passage exists in the cited file.

- **Fully supported (7):** CL2502, CL2504, CL1971, CL1645 and CL2151 hold. So do CL1161 (trivial metadata) and CL0967, although "shareable" is not in the FIX text.
- **Partial, counted as confirmed (5):**
  - CL0530: no 2025 ride figure; the corpus has 150k a week in Oct 2024 and 500k in Mar 2026.
  - CL0815: no thresholds and no Citadel argument; the source describes a filing to offer the switch "by March 1, 2014", so the "2014" filing date is shaky.
  - CL0903: no FRCC $350k and no "largest since 2007".
  - CL1817: no FedRAMP or NIST 800-53, although "controls ... as code" is present.
  - CL1966: Consilio not checked.

The rule is applied inconsistently. These partial claims count as confirmed, yet CL0537 counts as not found even though its month is attested ("grounded worldwide since last month", April 2019) and only the day is missing. Either add a "partial" verdict or apply one rule to both. If partials became not found, confirmed would fall to 82.

## The 6+ not-checkable moves are sound, with one exception
I checked all 23 rows that moved to not checkable from confirmed or not found, and 6 of those from unverifiable:
- Bare list markers ("1.", "5."): CL0215, CL0162, CL1159.
- Headings: CL0244, CL0170.
- Forecasts: CL0230 to CL0234.
- Author recommendations: CL0221, CL2317.

All of these are genuinely uncheckable. Reclassifying v1 markers that had been counted as confirmed (17 rows across files) is correct, and it removes inflation from v1.

One exception is CL0299, a heading that asserts "1983–2013+". It contains a checkable date range, and the 1983 start is unattested, so it belongs in not found. Also worth noting: the negative-search statements (CL0508, CL0519, CL0783) are defensible as not checkable, but they are claims about the research process, not about the world.

## "Error" is the wrong word for "not found"
A not-found row is no evidence either way, and 22 of the 39 never had the cited text to check. Calling 33.1% an "error rate" invites readers to take it as the share of false statements, which the data cannot show. Report two rates:
- **Contradicted by a source:** 3.1% in random150 and 36.4% in industry. Only this is evidence of error.
- **No supporting passage in the corpus:** 30.0%. This measures how traceable the claims are, and it mixes acquisition gaps with possible fabrication.

Drop "error rate" from the headline, and give the 23.7% acquired-only figure as a sensitivity check rather than as a second error rate.
