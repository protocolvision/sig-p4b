# Who owns the rules? A research project

Protocols for Business · started October 2026 · not published on the site (`drafts/` is excluded from the build)

When companies put AI agents to work, someone has to own the rules those agents act under, and how those
rules change. This project asks whether that work becomes a new role, gets absorbed into existing ones,
or disappears into engineering; how such roles have formed before; and where Business Protocol Management
fits, including whether it is the AI safety movement's expression inside ordinary companies.

## Status

| Stage | State |
| --- | --- |
| Exploratory research | Done; four drafts, hypotheses not findings |
| Research design | Version 1, ready |
| Activity-first loop, v1 | Run 10 October 2026: `results/loop-2026-10-10/`, report published |
| Red team and calibration | Done; both undercut what v1 can conclude |
| Loop v2 design | Pre-registered: calibration test, practitioner speech (podcasts, talks), rule-change events, seeded cases |
| Media frames for v2 | `sources-v2/`: current practitioners and historical recordings |
| Loop v2 run | Not yet run |
| Post or practice-guide changes | Waiting on the review |

## Files

| File | What it is |
| --- | --- |
| [`research-design.md`](research-design.md) | The question, hypotheses and what would refute them, methods, evidence standard, bias controls, outputs and review steps |
| [`agent-brief.md`](agent-brief.md) | Self-contained instructions for an agent with no prior context to run the design |
| [`loop-design.md`](loop-design.md) | v1 activity-first loop, pre-registered and run on 10 October 2026 |
| [`loop-design-v2.md`](loop-design-v2.md) | v2 loop: fixes from the red team and the calibration check; podcasts and talks in place of interviews |
| `loop-prompts/` | Agent prompts: v1 templates and [`v2.md`](loop-prompts/v2.md) |
| `loop-tools/` | `pool.py`, `analyze.py` (v1); `fetch_media.py` (fetches captions and transcript pages for a stratified sample; run on a laptop) |
| `sources-v2/` | `media-current.csv` and `media-historical.csv`: sampling frames of podcast episodes and videos. Transcripts are fetched locally and never committed |
| `report/` | Source of the published report page |
| `results/` | One folder per run, created by the agent; reviews go in the same folder |
| [`exploratory/role-emergence.md`](exploratory/role-emergence.md) | Eight role lineages (product management to model work), roles that faded, conditions for emergence and lasting, the seniority finding, the "it's all engineering" case, and the business question (time to amend) |
| [`exploratory/business-protocol-lead-critique.md`](exploratory/business-protocol-lead-critique.md) | Critique of the published job description for a Business Protocol Lead; protocol work compared with agent management; the metric and activity loop; near- and mid-term roles with rough odds; a proposed first role |
| [`exploratory/predicting-roles.md`](exploratory/predicting-roles.md) | How roles have been predicted and documented; six frameworks and their predictions; divergence; convergence on tacit knowledge; a bundling test; predictions to score |
| [`exploratory/bpm-and-ai-safety.md`](exploratory/bpm-and-ai-safety.md) | Test of whether BPM is the AI safety movement's institutional expression in deploying firms; seven conditions from how earlier movements became offices |

## How to run

**Loop v2 (next).**

1. On a laptop with open network access and `yt-dlp` installed, fetch transcripts for a stratified sample
   of each frame:
   `python3 loop-tools/fetch_media.py sources-v2/media-current.csv --per-function 4` and
   `python3 loop-tools/fetch_media.py sources-v2/media-historical.csv --per-function 4`.
   Check `sources-v2/transcripts/manifest.csv` for items that need manual transcription.
2. Start a Claude Code session there, on its own branch, and run `loop-design-v2.md`, section 10, with the
   prompts in `loop-prompts/v2.md`. Use a different model, or a person, as the second coder.
3. Review against v1 and the exploratory drafts, as in `research-design.md`, section 10.

**Agent brief (v1 desk run).** Start a new session on its own branch and give it one instruction:
*Read `drafts/research/who-owns-the-rules/agent-brief.md` and follow it.* Don't add context.
