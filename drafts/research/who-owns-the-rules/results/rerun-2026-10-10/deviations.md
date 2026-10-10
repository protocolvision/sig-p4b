# Deviations from the runbook and designs

Rerun of 10 October 2026. Each entry: what the runbook or design says, what was done, why.

1. **Wayback snapshots taken in a separate pass.** RERUN.md phase 1.1 runs `acquire.py --wayback`, which
   saves each page to the Internet Archive inline. The save endpoint took about two minutes per source
   (over 30 hours for 1,264 sources). Sources were fetched with `acquire.py` without `--wayback`, then
   snapshotted in a second, throttled pass; the `snapshot` column in `corpus/index.csv` is filled from that
   pass. Fetch dates and snapshot dates can differ by up to a day.

2. **Paywalled IAPP reports read through proxies.** Acquisition plan §4.1 asks for three IAPP member-only
   reports (AI Governance Profession 2025, Organizational Digital Governance 2025, Salary and Jobs 2025–26).
   No member access is available. They are represented by IAPP's free summaries and press releases, and by
   news and blog coverage that quotes them (`category = research-report-proxy`). Any figure from them is
   graded R (secondary, read in full) at best, never P, and is cited to the proxy, not to the report. Figures
   that proxies report differently are flagged rather than reconciled.

3. **Phases 3 and 4 reorganised around an independent corpus and six instruments.** RERUN.md phase 3 reruns
   each study from the round-one corpus. At the user's direction (10 October 2026), the rerun adds the
   general hypothesis that AI is a DevOps-like phase change, builds a rule-sampled Corpus B with no
   round-one selection, runs six forecasting instruments on it blind to round one, and verifies round one
   (phase 2) only after Corpus B findings are committed. Pre-registered in
   [`../../triangulation-design.md`](../../triangulation-design.md). Loop v2's methods and hypotheses are
   unchanged; its strata S1–S5 draw from Corpus B. A split-half of the round-one corpus was considered and
   rejected: both halves would share round one's selection and codebook.

4. **Archived copies before the browser pass.** Acquisition plan §3.5 sends `needs-browser` sources to a
   browser. Before that, `loop-tools/wayback_fallback.py` fetched the closest existing Internet Archive copy
   of each `needs-browser` or `failed` source (status `ok-wayback`). The text header records the snapshot
   URL and date. An archived copy may differ from the version round one cited; claims checked against one
   cite the snapshot. Only sources with no usable copy go to the browser.

5. **Extraction check by a clean agent, not a person.** Triangulation design section 5 says "a person checks 50
   records by hand before analysis". At the user's direction (10 October 2026), a fresh Opus agent does the
   check instead: a model family different from both extractors (Haiku, Sonnet), with no design files,
   hypotheses or codebook in its context, only the 50 sampled records and their source texts. It judges
   verbatim match, whether each span is a task, the performer label, and missed tasks (precision and a recall
   estimate). Limitation: a model checking models can share their blind spots; field work is the human check.

6. **Seeds and the recall gate (loop v2 section 6), changed before any coding.** Section 6 calls for 20 seeds
   (10 PV, 5 RD, 5 PE) and a recall gate of 0.7. Two Opus reviews (`review/pipeline-review.md` C8 and
   `review/seeds-v2-review.md`) found that this tests recall only, cannot fail a coder whose true recall is
   0.5 with any reliability, and that the seeds could be identified by format and length. Changes:
   - 20 seeds per positive code and 60 negatives (AO, applies-an-existing-rule, unrelated);
   - precision is reported too;
   - a code's absence is interpretable only if seed recall is 0.7 or more AND its Wilson 95% lower bound is
     0.5 or more;
   - seeds take real-record format at merge;
   - the key is held outside git until coding ends, with its SHA-256 committed in `log.md` beforehand.

7. **Location and coverage (review C6).**
   - S1 was drawn by title without a location filter (the plan says title and location): 32 of 59 postings
     are non-US, mostly shared-service centres. S1 is not redrawn. Every S1 and I1 rate is reported
     separately for US and non-US postings, and by sector and firm type, weighted by employer.
   - Board coverage is 41% of the frame and misses most large tech and finance firms. Features about early
     adopters and diffusion (N06a, N21, D6) are therefore coded from filings, speech and vendor documents,
     not from the board crawl.

8. **Seeds v3: final handling, fixed before any coding** (`review/seeds-v3-review.md`). The key is unchanged
   (SHA-256 in `log.md`).
   - **Dropped:** seeds 19 (unresolved ambiguity), 32, 38, 39, 45, 46, 53, 69, 109 (miskeyed or failing
     the RD test) and 112 (duplicate of 79). RD keeps 16 seeds, so its gate is 12 of 16 plus the Wilson
     lower bound of 0.5.
   - **PE second codes are inconsistent in the key** (missing on 8, 30, 63, 72, 99 and 110, among others).
     Rule: on any RD seed, a coder's PE code is not counted as a false positive.
   - **Merge:** `performer` is hidden from coders, because it cues negatives.
   - **Reporting:** seed recall is reported as an upper bound. The filing and posting seeds are more
     specific than real records, and 38 of 60 positives are invented scenarios with no cited source.
     Speech seeds were not compared with real speech records, which did not yet exist.

9. **Filings: consensus extraction after a narrow gate miss.** Filings v3 (prompt v3, merged windows,
   per-company dedupe) reached Jaccard F1 0.689 between Haiku and Sonnet on the 10% sample (gate 0.7);
   count ratio 1.00 (gate passed); exact F1 0.386. Rather than loosen the gate or revise the prompt again,
   Sonnet extracts all 2,216 passages and the filings extraction used downstream is the **consensus set**:
   spans found by both models (one-to-one Jaccard ≥ 0.5, Sonnet's span text kept). Single-model spans are
   kept in a separate file, flagged, and excluded from clustering. The 0.689 is reported. A clean Opus
   check of the consensus set on 25 fresh passages must reach 0.7 precision and recall before use.
   Vendor filers (SIC 7370–7374, 3570–3579) supply 64% of passages and are analysed separately from
   adopters.

10. **Filings leave the activity clustering; coded by passage instead.** Three filing extractions failed the
    clean check:
    - v1: precision 0.39;
    - v2: prompt corrected, superseded before checking;
    - v3 consensus: precision 0.40, recall 0.52.
    Both models agree on product, revenue and financing statements and miss team-subject activities. The
    cause is the source: filings seldom describe internal work, so span extraction of work activities is
    the wrong tool. Filings are removed from I2 clustering (postings remain the activity source). They are
    coded by passage with the fixed codebook `loop-prompts/filing-codes.md` (own use, product, reorg,
    body, metric, controls, workforce, rule cited). These serve the purposes section 4.2 gave filings
    (F1–F3, D2, I4 citations, diffusion). Gates: kappa 0.6 or more per code, and a clean Opus check with
    0.7 precision and recall per code.

11. **Passage coding: full second coder and consensus values.** On the 10% overlap (222 passages), own_use
    (kappa 0.77), product (0.79) and controls (0.67) pass. reorg, body, metric, workforce and rule_cited
    fail, but each has 0–12 positives in the overlap, too few for kappa. Before any further results:
    - Sonnet codes all 2,216 passages, and kappa is recomputed on the full set with the gate unchanged (0.6).
    - Each code's final value is yes only when both models say yes.
    - The clean Opus check (40 passages, at least 5 positives per code) measures precision and recall of
      these consensus values.
    - A code that fails kappa or the clean check is reported as unreliable and not used for F1–F3.
