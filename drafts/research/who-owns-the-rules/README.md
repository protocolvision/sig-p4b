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
| Blind run | Not yet run |
| Review of the run | — |
| Post or practice-guide changes | Waiting on the review |

## Files

| File | What it is |
| --- | --- |
| [`research-design.md`](research-design.md) | The question, hypotheses and what would refute them, methods, evidence standard, bias controls, outputs and review steps |
| [`agent-brief.md`](agent-brief.md) | Self-contained instructions for an agent with no prior context to run the design |
| `results/` | One folder per run, created by the agent; reviews go in the same folder |
| [`exploratory/role-emergence.md`](exploratory/role-emergence.md) | Eight role lineages (product management to model work), roles that faded, conditions for emergence and lasting, the seniority finding, the "it's all engineering" case, and the business question (time to amend) |
| [`exploratory/business-protocol-lead-critique.md`](exploratory/business-protocol-lead-critique.md) | Critique of the published job description for a Business Protocol Lead; protocol work compared with agent management; the metric and activity loop; near- and mid-term roles with rough odds; a proposed first role |
| [`exploratory/predicting-roles.md`](exploratory/predicting-roles.md) | How roles have been predicted and documented; six frameworks and their predictions; divergence; convergence on tacit knowledge; a bundling test; predictions to score |
| [`exploratory/bpm-and-ai-safety.md`](exploratory/bpm-and-ai-safety.md) | Test of whether BPM is the AI safety movement's institutional expression in deploying firms; seven conditions from how earlier movements became offices |

## How to run

1. Start a new Claude Code session on this repository, on its own branch.
2. Give it one instruction: *Read `drafts/research/who-owns-the-rules/agent-brief.md` and follow it.*
3. Don't add context; the run is meant to be blind to the exploratory drafts.
4. When it finishes, follow section 10 of the design to review the results against `exploratory/`.

A second run with a different model, compared with the first, is a useful check on the first.
