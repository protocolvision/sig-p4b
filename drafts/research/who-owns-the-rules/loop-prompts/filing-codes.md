# Filing passage codes (deviation 10)

Fixed before any passage is coded. Two coders on different models (Haiku 5.5 on all passages, Sonnet 5.5
on a 10% sample) code each passage independently. Agreement is Cohen's kappa per code, accepted at 0.6
or more; a clean Opus check of 25 passages must reach 0.7 precision and recall per code with at least 5
positives in the sample, or the code is reported as unreliable.

---

You read one passage from a company's annual or quarterly report (US SEC filing). Answer each question
yes or no **for this company**, using only what the passage states. For every yes, copy the shortest exact
quote (40 words or fewer) that shows it.

| Code | Question | Yes only if the passage says |
| --- | --- | --- |
| `own_use` | Does the company use AI agents or automated software agents in its own operations? | The company, its people or its functions use, deploy, run or pilot agents or automation in their own work (not only selling them) |
| `product` | Does the company sell or offer AI agent products or services to others? | It describes agent products, features or services offered to customers |
| `reorg` | Has the company reorganised teams or functions around AI or agents? | A change to teams, reporting lines or operating model linked to AI, especially one joining business and technology functions |
| `body` | Has the company created or named a body or officer with decision rights over AI? | A committee, council, board oversight assignment, chief AI officer or similar is named as overseeing, approving or governing AI use |
| `metric` | Does the company report an operating measure of its AI or agent use? | A measure of use, accuracy, containment, productivity, cost or volume attributed to the company's own AI or agent use |
| `controls` | Does the company describe controls or oversight over its AI systems? | Specific practices: human review, approval steps, monitoring, testing, limits, policies for AI use (not generic risk language) |
| `workforce` | Does the company describe changes to its people's roles, skills or headcount because of AI? | Hiring, retraining, new roles, role changes or reductions attributed to AI or agents |
| `rule_cited` | Does the company cite a law or regulation as a reason for what it does with AI? | A named law, regulation or regulator linked to the company's AI practices (give the name) |

Rules: answer from the passage only. A statement that something "may", "could" or "will" happen is no,
except for `controls` and `body`, where a stated policy in force counts. Generic risk-factor language with
no described practice is no. Output JSON: one object per code with `value` (yes or no) and `quote` (empty
when no), plus `rule_name` when `rule_cited` is yes.
