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
