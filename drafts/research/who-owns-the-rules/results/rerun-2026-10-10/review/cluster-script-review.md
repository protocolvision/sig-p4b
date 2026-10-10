# Review: loop-tools/cluster_tasks.py against deviations.md item 16 (2026-10-10)

Scope: `loop-tools/cluster_tasks.py`, `loop-tools/embed_tasks.py`, the smoke outputs in
`clusters/smoke/`, checked against item 16 and its clarification. Reviewed before any real run.

**Verdict: no critical defects. The script was not changed, so there is no `cluster_tasks-pre-review.py`.**
I reran the smoke test (`--smoke 5000`). `clusters.csv` and `assignments.csv.gz` came out byte-identical
to the earlier run. I also recomputed the split, ARI, Jaccard and employer counts independently from
`assignments.csv.gz`, and they match.

## Checks

1. **Split by posting.** The script shuffles posting keys `(ats, board_id, posting_id)` with
   `random.Random(20261011)` and puts half in discovery. Tasks inherit their posting's half. In the
   smoke run, 0 of 3,380 postings have tasks in both halves. All ids are strings, no posting triple
   is duplicated in `postings-input.jsonl`, and no posting maps to two employers in `selection.csv`. OK.
2. **Holdout projection.** UMAP is fit on the discovery half only, and `um_d.transform(Xh)` projects
   the holdout into that same 10-D space. `approximate_predict` then runs on the HDBSCAN model fit in
   that space. The holdout embeddings are identical in kind to discovery: same cache, same model,
   L2-normalised. This is the right way to do it and the test is valid.

   Caveat (not a defect): `transform` places new points relative to the discovery graph, so predicted
   labels may be somewhat cleaner than the points warrant. The independent holdout clustering, which
   gets its own UMAP fit, is the side that guards against this.
3. **ARI and the found rule.** `ari_both` masks to points that are non-noise in both labelings. My
   recomputed smoke ARI is 0.6069 on n=690, matching the script. The full-run parameters are
   min_pred 30, Jaccard ≥ 0.5, ARI ≥ 0.6 and min_emp 10, exactly as specified. Jaccard is computed
   between a cluster's predicted holdout set and each independent holdout cluster, and the best one
   is kept. The employer count uses the discovery cluster's members. The spec says "its tasks", so
   this reading is defensible; state it in the report. Smoke mode scales the parameters down
   (nn 15, mcs 10, ms 3, min_pred 5, min_emp 3) and labels the output SMOKE.
4. **Noise baseline.** It makes three independent UMAP+HDBSCAN fits on the full pool `X`, with seeds
   1, 2 and 3. It reports the three pairwise ARIs and their mean, using the same non-noise-in-both mask
   as the holdout. The spec doesn't fix how noise is handled here, so state this convention beside
   the number.
5. **Seeds, order of dedupe and cap.** The seeds are pool cap 20261024, split 20261011, UMAP 42 for
   discovery and holdout, and 1/2/3 for the baseline. All are constants and all appear in
   `stability.md`. Dedupe (employer + normalised lowercased span) runs before the 300-per-employer cap,
   as the clarification requires. Verified on the current extraction: 116,207 tasks after dedupe and
   33,172 after the cap. The maximum per employer is 300, there are no remaining duplicates, and
   calling `load_pool` twice gives identical frames.
6. **Determinism.** Two smoke runs gave byte-identical outputs. UMAP with `random_state` runs
   single-threaded and `transform_seed` is fixed. HDBSCAN and `approximate_predict` are deterministic.
   Set iteration never affects output order.

## Non-critical notes (no change made)

- Dedupe keeps the *first* occurrence in `tasks.jsonl` line order, so which posting (and therefore
  which half) a duplicate span lands in depends on file order. This is deterministic for a fixed
  file. If the credit-blocked batch is redone by rewriting rather than appending, the pool can shift
  slightly. Sorting by `task_id` before dedupe would make it order-independent.
- `corpus/b-raw/embed/` is currently empty. The real run will exit until `embed_tasks.py` has been run
  on the final `tasks.jsonl`. `embed_tasks.py` hard-codes `device="mps"`.
- The earlier `stability.md` showed "peak RSS 565.69 GiB". The rerun reports 0.52 GiB, so that line is
  cosmetic and has no effect on results.
- The "20 most central spans" are ranked by cosine similarity to the embedding-space centroid, and
  each is truncated to 40 words. The spec doesn't define "central", so record this choice.
