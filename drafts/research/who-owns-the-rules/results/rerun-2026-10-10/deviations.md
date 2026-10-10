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
