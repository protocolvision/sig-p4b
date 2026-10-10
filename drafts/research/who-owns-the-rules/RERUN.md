# End-to-end rerun from a local corpus

Protocols for Business · runbook · 10 October 2026

The first round of research ran in a cloud container that could not open web pages, so every claim rests on
search-engine summaries. This runbook redoes it on a computer with open network and browser access: build
the corpus first, then rerun every study from it, then update the report, the executive summary and the
recommendation. Follow the phases in order; each ends with a commit.

## How to start

From a terminal on a computer with network access:

```
cd sig-p4b && git pull
bash drafts/research/who-owns-the-rules/loop-tools/check_setup.sh
claude "$(cat drafts/research/who-owns-the-rules/rerun-prompt.md)"
```

The check script lists anything missing (Python 3.9+, `yt-dlp`, `pdftotext`, the `claude` CLI, network
reach; Whisper is optional, for podcasts with no transcript) and rebuilds the manifest. The prompt is in
[`rerun-prompt.md`](rerun-prompt.md). The run takes many hours; phase 1 can be left running with the
acquirer alone (`python3 loop-tools/acquire.py --wayback` from `drafts/research/who-owns-the-rules/`)
before starting Claude Code.

If the terminal session has no Artifact tool, phase 4 still updates `report/who-owns-the-rules.html` in the
repository; publish it to the existing link afterwards from any Claude session that has the tool.

## Phase 0. Check the environment (10 minutes)

1. `curl -sI https://www.finra.org | head -1` and `curl -sI https://web.archive.org | head -1` both return
   HTTP status lines.
2. `python3 drafts/research/who-owns-the-rules/loop-tools/build_manifest.py` rebuilds the manifest.
3. Create `results/rerun-<date>/` and copy this runbook's phase checklist into `results/rerun-<date>/log.md`.

## Phase 1. Build the corpus

Follow [`corpus/acquisition-plan.md`](corpus/acquisition-plan.md).

1. Acquire what is already cited: `python3 loop-tools/acquire.py --wayback` (resumable; re-run with
   `--retry-failed`). Expect several hours for about 1,200 sources.
2. Open each `needs-browser` source in the browser and save its text as the plan describes.
3. Resolve the new sources in the plan's section 4 to URLs in `corpus/planned.csv`, logging every search in
   `corpus/search-log.csv`; rebuild the manifest; acquire again.
4. Clean the two media frames (`sources-v2/README.md`), then acquire captions and transcripts.
5. Run the quality checks in the plan's section 5. Commit `index.csv`, `planned.csv`, `search-log.csv`.

## Phase 2. Verify the first round

For every load-bearing claim in `results/loop-2026-10-10/`, `results/industry-2026-10-10/`,
`exploratory/` and `roles/`, find the passage in the corpus. Write `results/rerun-<date>/verification.csv`
(claim, file, source id, passage of 40 words or fewer, verdict: confirmed, corrected, not found). Correct
quotes, dates and figures in a new copy of each findings file; never edit the first-round files.

## Phase 3. Rerun the studies from the corpus

Use agents for collection and coding as before, but every record must cite a corpus id and a passage.

1. **Role library.** Bring each role in `roles/` to 6–10 full postings and official capability models;
   recode activities with the v2 scheme (`loop-design-v2.md`, section 6).
2. **Loop v2.** Run `loop-design-v2.md`, section 10, end to end, with strata S1–S7 drawn from the corpus,
   seeded cases, a second coder from a different model, the noise baseline and the calibration test on
   historical recordings.
3. **Industry analogue.** Regrade the ten fact sheets from corpus text, rescore with two fresh scorers,
   and re-check the trading, grid and control timelines and the gatekeeper table against primary texts.
4. **Red team** each study with a fresh agent, as in the first round.

## Phase 4. Synthesis and deliverables

1. **Findings.** `results/rerun-<date>/findings.md`: verdict per hypothesis, confidence, the corpus
   passages that carry it, and what changed since the first round.
2. **Report.** Update `report/who-owns-the-rules.html` (five pages, under seven minutes, same structure)
   and republish it to the same artifact. From a new session, read it first:
   `Artifact action=read url=https://claude.ai/artifact/Q2mMJCrKKXRQdAxLUPVQCG`, then publish with that
   `url`. Cite corpus ids in a sources appendix.
3. **Executive summary.** `results/rerun-<date>/exec-summary.md`: ten bullets for a chief executive, the
   problem first, then approach, findings, forecast and the recommendation, with confidence marked.
4. **Recommendation.** `results/rerun-<date>/recommendation.md`: how protocol vision and Business Protocol
   Management diffuse through an organisation. Start from the provisional version in
   [`recommendation-draft.md`](recommendation-draft.md) and keep only what the rerun supports. Required
   sections: the problem; the evidence; by layer (finding rules, designing rules, deciding changes): who
   holds it, at what seniority, with what artefact and measure; by stage (today, after an outside rule,
   after a sector regulation); by function; the training path (watching, workshops, simulations); what not
   to do; assumptions to test; predictions to register.
5. Commit and push; update the status table in `README.md`.

## Phase 5. Review

Compare the rerun with the first round as in `research-design.md`, section 10: agreement, disagreement,
new findings, and a random audit of ten citations against the corpus by hand.
