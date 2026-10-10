# Rerun log, 10 October 2026

Branch `rerun-2026-10-10`. Runbook: [`../../RERUN.md`](../../RERUN.md).

## Phase checklist

- [x] Phase 0. Check the environment: python3 3.14.3, yt-dlp, pdftotext, claude ok; whisper missing (optional). finra.org, web.archive.org, youtube.com, eur-lex reachable. Manifest rebuilt: 1,264 sources.
- [ ] Phase 1. Build the corpus
  - [ ] 1.1 `acquire.py --wayback` (and `--retry-failed`)
  - [ ] 1.2 `needs-browser` sources saved by hand or browser
  - [ ] 1.3 New sources (plan §4) resolved into `corpus/planned.csv`, searches in `corpus/search-log.csv`; manifest rebuilt; acquire again
  - [ ] 1.4 Media frames cleaned; captions and transcripts acquired
  - [ ] 1.5 Quality checks (plan §5); commit `index.csv`, `planned.csv`, `search-log.csv`
- [ ] Phase 2. Verify the first round (`verification.csv`)
- [ ] Phase 3. Rerun the studies from the corpus (role library, loop v2, industry analogue, red team)
- [ ] Phase 4. Synthesis and deliverables (findings, report, exec summary, recommendation)
- [ ] Phase 5. Review

## Notes
