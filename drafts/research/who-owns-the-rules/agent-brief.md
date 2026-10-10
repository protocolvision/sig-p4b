# Agent brief: who owns the rules when agents join the business?

This file is the complete instruction for a research run. Paste it, or point a new agent session at it.
It assumes no prior context.

---

You are a research agent. Your job is to test seven hypotheses about how new jobs form, applied to one
kind of work that is appearing as companies put AI agents into their operations. You work from public
sources and write your results to files in this repository.

## Ground rules

1. **Do not open** anything under `drafts/research/who-owns-the-rules/exploratory/`, and do not read the
   group's site pages, blog posts or other drafts, except `src/research-bpm.html` in Phase 3. Those
   contain earlier conclusions; this run must reach its own.
2. Read `drafts/research/who-owns-the-rules/research-design.md` first, then follow it. Its definitions
   (section 3), hypotheses (section 5), methods (section 6), evidence standard (section 7) and outputs
   (section 9) are binding.
3. **Look for evidence against each hypothesis before evidence for it.** Give each rival hypothesis the
   same effort as the hypothesis it challenges.
4. **Grade every claim**: (P) primary source opened and read; (R) reputable secondary source opened and
   read; (S) search-result summary only; (M) model memory. Don't present (S) or (M) claims as
   established. If a page is blocked, say so and grade accordingly; don't fill the gap from memory.
5. **Quote only words you have seen.** Every number names its source document and date. Use Chicago
   notes style.
6. Write plainly. Lead with the finding, then the evidence. Avoid adjectives that carry no information.

## The work, in brief

- **Phase 1.** Code at least twelve role histories (lasting, faded, contested; at least four you choose
  yourself; at least two that came from a social movement or a law). Test H1 and H2.
- **Phase 2.** Apply at least five frameworks for how roles emerge, one at a time, each making its own
  prediction. Collect 2023–2026 job-posting signals. Test H3, H4 and H6. Report where the predictions
  diverge and converge.
- **Phase 3.** Read `src/research-bpm.html`. Build the conditions for a movement's institutional
  expression from at least five historical cases. Map where the AI safety movement has institutionalized.
  Score Business Protocol Management, and the rival (privacy-led AI governance), against each condition.
  Test H5.
- **Phase 4.** A verdict per hypothesis (supported, partly supported, not supported, untestable), with
  confidence and the strongest evidence each way; five to ten dated forecasts with probabilities and the
  public source each will be checked against; what would most change your conclusions. H7 needs field
  data: say what a case study would have to collect, and don't give a verdict.

## Output

Create `drafts/research/who-owns-the-rules/results/run-YYYY-MM-DD/` (today's date) containing:

- `report.md`: start with a one-page summary table (hypothesis, verdict, confidence, key evidence), then
  one section per research question, then forecasts and limitations;
- `role-sheet.csv`: the Phase 1 coding sheet, one row per role, with a grade for each cell;
- `frameworks.md`, `movement-test.md`;
- `sources.md`: every source with its grade;
- `search-log.md`: every query, marked as seeking evidence for or against which hypothesis.

Commit the folder with the message "Research run YYYY-MM-DD: who owns the rules" and push to the branch
you were given. Do not edit any other file.

## When you finish

Reply with the summary table and the three findings you are least confident in.
