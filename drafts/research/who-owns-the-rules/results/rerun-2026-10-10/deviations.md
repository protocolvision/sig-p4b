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

12. **Speech uses consensus extraction, as filings did (deviation 9).** Haiku and Sonnet extracted all 189
    chunks of 30 timestamped transcripts:
    - Jaccard F1 0.63 (gate 0.7); count ratio 0.857 (passes);
    - per the rule set before the run, only records found by both models are used: 813, or 771 after
      overlap dedupe;
    - a clean Opus check on 25 chunks must reach 0.7 precision and recall.
    The 8 transcript pages without timestamps are extracted too, with paragraph positions.

13. **Speech: consensus fails on recall; choice between union and Sonnet-only fixed before measuring.** The
    clean check of consensus records gave precision 0.83 and recall 0.61 (fail). Two alternatives are
    judged on 25 NEW chunks (seed 20261018), excluding the first sample. A clean Opus reviewer judges every
    record from either model, blind to which model produced it, and lists missed activities. From that
    one review: precision and recall for union, Sonnet-only and Haiku-only. Rule: use the variant passing
    both 0.7 gates; if several pass, the one with higher recall; if none, speech records are reported
    with their measured precision and recall as limits. Speech is descriptive only in any case (H-cal
    refuted).
    **Outcome (blind review, 25 new chunks, 176 gold activities):** consensus P 0.90 / R 0.49; Haiku-only
    0.78 / 0.63; Sonnet-only 0.74 / 0.67; union 0.70 / 0.77 (precision just under the gate). No variant
    passes both gates. Rule 13 says only "report measured limits", so the dataset choice is recorded here:
    **consensus**, the variant already in use under deviation 12, chosen for precision because speech is
    descriptive only and false records would create false descriptions. Every speech count is reported
    as a lower bound (recall about 0.5). The choice was made after seeing the scores; the alternative
    (union) is noted.

14. **Posting selection for extraction, fixed before any posting is extracted** (design section 5 says
    "all postings in the ten S1 occupations and all new-title postings; a stratified 20% of the rest").
    - **Universe:** all crawled postings except the 11 boards in `corpus-b/exclude-boards.txt`. Postings
      are deduplicated on (ats, board_id, id).
    - **Study occupations:** postings whose title maps by override to one of the ten S1 occupations.
    - **New-title postings:** the title (case-insensitive, whole words) contains any of: AI, A.I., agent,
      agents, agentic, LLM, GenAI, "generative AI", "machine learning", automation, "prompt", copilot,
      "intelligent automation", RPA, "AI governance", "responsible AI", "model risk". The list is fixed
      here and includes broad terms on purpose; it identifies candidate agent-work titles, and I1
      reports them by term.
      - "Agent" also catches support, sales and insurance agents. These are kept and reported separately
        as the "agent (human)" term group: titles where "agent" is not next to AI, agentic, autonomous,
        virtual or digital.
    - **The rest:** a 20% random sample stratified by O*NET major group (first two digits) × employer
      type (Fortune 500 or VC software), with seed 20261019.
    - **Extraction:**
      - Haiku extracts all selected postings; Sonnet extracts a 10% random subsample (seed 20261020).
      - Gates as for filings: Jaccard ≥ 0.5 one-to-one, F1 0.7, count ratio [0.8, 1.25].
      - A clean Opus check on 25 postings (seed 20261021) needs precision and recall of 0.7.
      - **If agreement fails, the fallback is decided now:** Sonnet extracts all selected postings, and
        the clean check judges Sonnet-only. Consensus is not used for postings, because consensus cost
        recall in speech.

15. **I3 period postings: DevOps only for the posting-language comparison.** Archive access (CDX
    rate-limited; the availability-API retry found only PJM 2010 pages) gave DevOps 60 postings
    (2011–2016), trading controls 17 and grid 5. The posting-language comparison (embedding similarity and
    duty bundles, design section 3) uses DevOps only. For trading and the grid, I3 relies on dated rule
    texts (I4) and the signature timelines, and their few postings are illustrative. If CDX access
    returns before synthesis, one more collection pass is attempted.

16. **Clustering parameters, fixed before any clustering** (design section 5 gives the method, not the
    settings).
    - **Pool.** Haiku posting tasks from the final extraction (after the credit-blocked batch is redone),
      performer = person or both. At most 300 tasks per employer, drawn at random (seed 20261024), so that
      large Workday boards cannot dominate. Deduplicated by normalised span within employer.
    - **Split.** A random half for discovery and the other half as holdout, by POSTING (all tasks of one
      posting fall in the same half), seed 20261011.
    - **Embedding.** all-mpnet-base-v2, L2-normalised.
    - **Reduction.** UMAP: n_neighbors 30, n_components 10, min_dist 0.0, metric cosine, random_state
      fixed per run.
    - **Clustering.** HDBSCAN: min_cluster_size 30, min_samples 10, cluster_selection_method "eom".
    - **Holdout test.**
      - Assign holdout points to discovery clusters with `hdbscan.approximate_predict`.
      - Cluster the holdout independently with the same settings.
      - Compute the adjusted Rand index between the two labelings, on points that are non-noise in both.
      - A discovery cluster counts as **found** if its predicted holdout members reach 30 or more, its best-
        matching independent holdout cluster overlaps it with Jaccard ≥ 0.5, the overall ARI is 0.6 or more,
        and its tasks come from at least 10 distinct employers.
    - **Noise baseline.** Three more full runs with different UMAP seeds on the full pool; the mean
      pairwise ARI is reported beside the holdout ARI (loop v2 section 7).
    - **Labels.** Each found cluster is labelled by a model reading its 20 most central spans, blind to the
      codebook and the hypotheses. The codebook is applied only afterwards (section 5).
    Clarification, before any real run: dedupe within employer comes BEFORE the 300-per-employer cap, so
    the cap counts distinct tasks. The pool is 116,207 tasks after the performer filter and dedupe, and
    33,172 after the cap (partial extraction; recomputed on the final pool).
    Choices the spec left open, stated before the real run (Opus code review, `review/cluster-script-review.md`):
    - the noise baseline drops noise points in the same way as the holdout test;
    - employer counts per cluster use discovery members only;
    - when a span repeats within an employer, it is assigned to the posting that comes first in tasks.jsonl
      (deterministic for a fixed file).

17. **Codebook coding by cluster, with record-level seed and validation sample (user direction: efficiency,
    10 October 2026).** Loop v2 section 6 codes every record with two coders of different models. To
    avoid about 33,000 × 2 API calls, coding moves to Claude Code agents on the user's account. Fixed
    before any coding:
    - **Cluster coding.** Each FOUND cluster is coded from 40 spans: its 20 most central plus 20 random
      members (seed 20261025). Two independent coders (Sonnet and Haiku agents, each with its own context)
      give up to two codes (PV, PE, RD, AO, OT) per cluster with a share estimate, using the v2 codebook
      and boundary rule verbatim. Disagreements are reported, not reconciled.
    - **Record pool for seeds and validation.** 300 real records (stratified across found clusters and
      noise, seed 20261026) mixed with the 110 retained v3 seeds. All get neutral ids and real-record
      fields; `performer` is hidden. The same two coders code every record.
    - **Gates (as in deviation 6).**
      - Seed recall ≥ 0.7 per code with Wilson lower bound ≥ 0.5.
      - Seed precision is reported.
      - Kappa per code between coders.
    - **Validation.** On the 300 real records, agreement between a record's own code and its cluster's
      code is reported per code. This is the information lost by cluster-level coding.
    - Cluster-level shares replace record counts in every finding that cites codebook counts, and the
      report says so.

18. **Occupation codes: descriptive only after two failed checks; cross-function merging measured from task
    clusters.**
    - **The checks.** Both mappings failed the gate (error ≤ 10%), each judged by a clean Opus check of 200
      titles:
      - v1 top-10 candidates: assigned 16% error, none 90% wrong;
      - v2 two-stage: assigned 21% error, major group correct 82%; none 82% wrong; overrides 10% error.
      A third round is not run.
    - **Decided before I1 uses any code:**
      1. Detailed O*NET codes are not used for any inference. They are reported only as description,
         with the measured error.
      2. Major groups are used descriptively, with their measured accuracy (about 83%) stated beside every
         figure.
      3. The study-occupation group (overrides, 10% error, all errors non-finance "controller" titles
         already excluded in v2) and the new-title term groups (deviation 14) stay as the basis of the
         absorption comparison. Neither depends on model codes.
      4. N02 and D2 (duties from two previously separate functions in one posting) are measured from TASK
         content. Each found cluster gets a function family in its blind label step (finance,
         sales/RevOps, customer support, HR, legal, procurement, IT/security, software engineering,
         data/ML, operations, other). A posting "combines functions" when its tasks fall in clusters of two
         or more families, at least one of them business and at least one technical. The rate is reported
         over time and by group.
      5. "None" titles are treated as unknown, not as a category.

19. **Clustering: degenerate EOM solution, rerun with leaf selection (post hoc, both reported).** The
    pre-registered run (eom) gave holdout ARI 0.017 and 0 clusters found. Diagnosis: the independent
    holdout clustering collapsed into one cluster holding 24,515 of 25,553 points (96%), with 0% noise.
    That is a known HDBSCAN eom failure on near-uniform density. Meanwhile the discovery half gave 89
    clusters, and the three full-pool baselines gave 159–175 clusters with mean pairwise ARI 0.86. A
    stability test against one blob cannot be read.
    - **Rule, set before rerunning:** a solution is degenerate if one cluster holds more than half of its
      points. If any solution in a run is degenerate, the whole run (discovery, holdout and baselines) is
      repeated with cluster_selection_method = "leaf". Every other parameter and the found rule are
      unchanged.
    - The eom result is kept (`clusters/stability-eom.md`) and reported beside the leaf result
      (`clusters/leaf/`). The change was made after seeing a failure, and the report says so.

20. **Language clusters are excluded from work-bundle inference (post hoc, rule stated).** The embedding
    model (all-mpnet-base-v2) is English-centred, so non-English postings cluster by language rather than
    by work.
    - **Rule:** a cluster is a language artefact if more than 50% of its 20 central spans are mostly
      non-Latin script, or fewer than 30% contain common English function words (the, and, to, of, with,
      for).
    - **Outcome:** 8 of 114 clusters are artefacts, 3 of them among the 11 found (clusters 0 Chinese and
      Japanese, 6 Spanish, 10 Polish). **8 found work clusters remain.**
    - Language artefacts are reported, not interpreted.
    - **Limitation, stated in the report:** non-English duties sit mostly in language clusters or noise,
      so the activity analysis (I2) effectively describes English-language postings.
    - The rule was written after seeing cluster 0, which is why it is post hoc.

21. **I1 labour-market measures, fixed before any I1 figure is computed.**
    - **Agent or AI duty:** a posting task whose span contains any title term of deviation 14 (AI, A.I.,
      agentic, LLM, GenAI, "generative AI", "machine learning", automation, prompt, copilot, "intelligent
      automation", RPA, "AI governance", "responsible AI", "model risk"). "Agent" or "agents" counts only
      next to AI, agentic, autonomous, virtual or digital (as in deviation 14). This is lexical and
      transparent. It is validated on the 300 real records of the coding pool against the coders' AO, PE
      and RD codes, and the agreement is reported.
    - **Absorption (N07, H-absorb):** among postings in existing occupations, defined as the S1 study
      occupations plus, separately, all non-new-title postings, the number with at least one agent or AI
      duty, set against the number of new-title postings (deviation 14, excluding human-agent titles).
      Reported as a ratio, weighted by employer (each employer weight 1), and also unweighted, by employer
      type and US vs non-US.
    - **Cross-function postings (N02, D2):**
      - **Primary:** share of postings with tasks in found work clusters of two or more function families,
        at least one business and one technical (reviewed labels).
      - **Secondary (descriptive):** the same using all non-artefact clusters.
      - Reported for new-title postings vs other postings.
    - **New-title spread:** new-title postings per employer and the share of employers with at least one,
      by employer type and sector. No time trend: the crawl is current-only and the historical board crawl
      was not built, so N04a is coded from other instruments or marked insufficient.
    - Occupation codes appear only descriptively (deviation 18).

22. **Speech codes: adjudication of disagreements.** Two coders (Sonnet A, Haiku B) coded all 862 speech
    records:
    - kappa PV 0.28, PE 0.66, RD 0.33, AO 0.56, OT 0.58;
    - coder A defaulted unflagged records to OT, which likely under-codes AO.
    Speech is descriptive only (H-cal refuted), so a full recode is not run. Instead:
    - a clean Opus adjudicator codes every record on which the coders differ, blind to which coder gave
      which code;
    - it also checks 40 random records that both coded OT;
    - final speech codes = the agreed codes, plus the adjudicated codes for disagreements;
    - kappa is reported as measured, and the both-OT check is reported as a miss rate.

23. **Feature coders' inputs limited to the neutral write-ups and tables (before any feature coding).** The
    leak check finds pattern words inside RAW data files: posting text in `clusters/*.csv`, and the I3 data
    files, where one history is labelled with a pattern name. The feature-coding prompt's input list is
    narrowed to:
    - `instruments/I1.md` … `I6.md` and `instruments/I*-tables.csv`;
    - `corpus-b/filings-*.csv`.
    The raw cluster and I3 data files are excluded; I2.md and I3.md summarise them neutrally.
    `leak_check.py` scans exactly this list, and coding starts only when it is clean. I5c (community and
    tooling dates, specified in A.2 but not yet collected) is collected first and summarised into I5.md.
