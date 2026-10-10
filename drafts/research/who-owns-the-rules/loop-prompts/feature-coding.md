# Feature-coding prompt (triangulation design, section 6.2)

Fixed before any present-day coding (addendum A.1, point 4). Two coders on different models (Sonnet 5.5 and
Haiku 5.5) each receive this prompt and the inputs below, independently. Coders never see
`signatures.*`, `pattern-power*`, section 2 of the design, or any pattern name. Nothing in this file may
change after coding starts.

---

You are coding how a kind of work is forming in companies today. You will judge 22 features from evidence
files. You do not know, and should not guess, what the features will be compared with. Code only what the
evidence shows, with dates.

## The work being coded

People in companies who deploy AI agents (software that takes actions in business processes) and decide
what those agents may do: configuring, supervising and operating agents; setting, testing and changing the
permissions, limits, approval steps and escalation conditions agents act under; and deciding when those
change. Call this **agent work**. Any job title used mainly for agent work is an **agent-work title**.

## Inputs

Only these files (paths from `results/rerun-2026-10-10/`):

- `instruments/I1*.md` and `.csv`: postings counts, titles over time, duties inside existing occupations
- `instruments/I2*.md` and `clusters/`: task clusters from postings and filings
- `instruments/I3*.md`: present postings compared with period postings (descriptive only)
- `instruments/I4*.csv` and `.md`: functions that laws and rules require
- `instruments/I5*.csv`: vendor role definitions and certifications, with dates
- `instruments/I6*.md`: practitioner speech records (loop v2, stratum S7)
- `corpus-b/filings-*.csv`: filings index and counts

Do not open any other file and do not search the web.

## Scale

For each feature: **yes**, **partial**, **no**, or **insufficient** (the inputs cannot answer it). Give the
evidence: file, record or row, date, and a quote of 40 words or fewer where one exists. "No" needs positive
evidence of absence (a count, a search result of zero, a dated sequence); otherwise use "insufficient".

## Features

Dates refer to the agent era. The **first practice description** is the earliest dated description in the
inputs of a person doing agent work in a company (not a vendor demo).

| ID | Question | Yes means | Partial means |
| --- | --- | --- | --- |
| N01 | Was agent work described at least two years before any agent-work title was common (titles common = in at least 1% of postings that carry agent duties, or named in at least 10 employers' postings)? | Gap of 2 years or more | Gap of 1–2 years, or titles still not common |
| N02 | Do postings or speech combine duties that previously sat in two separate functions (for example business operations or compliance with software engineering) in one role or team? | In a stable cluster or in 10% or more of agent-duty postings | Seen, but below those levels |
| N03 | Order of first dated events: practitioner community (meetups, conferences, open groups) → open tooling → vendor certification → regulation that names the work | That order holds | Order holds for three of the four |
| N04a | Did agent-work title volume rise within about three years of the first practice description? | Clear rise in counts | Rise in some titles only |
| N05 | Are there shared measures of agent work that originated with practitioners (not regulators or vendors)? | Named measures used across firms, originating in practitioner sources | Measures used inside single firms only |
| N06a | Were the first adopters of agent work mostly software-native firms? | Over half of the earliest dated adopters | About half |
| N07 | Do more postings carry agent duties inside existing occupations than under agent-work titles? | Ratio 3:1 or more | Between 1:1 and 3:1 |
| N08 | Did agent-work titles appear in the same year as the first practice description? | Same year | Within one year |
| N09 | Did the practice originate in one firm and spread by imitation of that firm? | One named origin firm that others cite | A few firms |
| N10 | Does the work's authority come from a number its holder owns (an accuracy, error or containment target that sets what the role may decide)? | Stated in postings or speech as the basis for decisions | Number owned but not stated as the basis of authority |
| N11 | Is an agent-work title tied to a legal or regulatory text (the text names or requires it)? | A rule text requires the role | A rule text requires the function, not a named role |
| N12 | Were the first agent-work title holders senior or executive? | Most of the earliest postings or holders are senior or executive | Mixed |
| N13 | Did certification or statute come before a practitioner community? | Yes, dated | Certification before community, statute after |
| N14 | Did agent-work titles boom within 2–3 years of a specific new tool? | Titles name or follow one tool's release | Several tools |
| N15 | Are agent-work duties mainly operating a tool? | Most listed duties are operating, configuring or prompting one product or class of product | About half |
| N16a | Do agent-work titles carry a salary premium over the occupations they came from? | Premium of 15% or more in posted pay | Premium below 15%, or only at some employers |
| N19 | Is agent work being absorbed with no new title, team or measure? | No agent-work title, no team, no measure in the inputs | Titles or teams exist but are rare (under 1% of agent-duty postings) |
| N20 | Were the first holders mostly existing staff given new or added titles? See definition below | Most | Mixed |
| N21 | Did the first agent-work postings sit in operations or IT organisations, not research or analytics? | Most | Mixed |
| N22 | Is the stated purpose coordinating existing functions, not providing a new scarce capability? See definition below | Most stated purposes | Mixed |
| N23 | Do early practitioner talks frame the work as culture or process change, not as a new technique? See definition below | Most talks | Mixed |
| N24 | Did vendors relabel existing products for agent work within about three years? | Dated relabelling by two or more vendors | One vendor |

### Definitions for the interpretive features

- **N20, existing staff.** Count a holder or posting as "existing staff" when the title is a hybrid of an
  existing title ("Operations Manager, AI Agents", "Senior Engineer (Agents)"), when a speaker says they
  moved into the work from their existing job, or when a posting asks for experience in the same function
  it sits in. Count "new hire from outside" when the posting asks for a background outside the function
  (for example a research degree for an operations role) or a speaker says they were hired in for it.
  Postings that say neither are not counted.
- **N22, stated purpose.** "Coordinating existing functions": the purpose names two or more existing
  functions, teams or systems and says the work connects, aligns or hands off between them. "New scarce
  capability": the purpose names a skill or capability the firm lacked and says the role brings it. Code
  from the purpose or summary statements of postings and from speakers' own description of why the role
  exists, not from duty lists.
- **N23, framing.** "Culture or process change": the speaker says the change is about how teams work
  together, ways of working, operating model or habits. "New technique": the speaker presents a method,
  tool or skill. Count only talks dated within three years of the first practice description, and code
  each talk once by its main framing.

## Output

Write `results/rerun-2026-10-10/pattern-match/coder-<name>.csv` with columns
feature_id,value,evidence_file,evidence_row,evidence_date,quote,note. One row per feature, all 22 features.

## Scoring rules (applied by script after both coders finish)

- Each feature's value is the mean of the two coders (yes 1, partial 0.5, no 0). A feature that either
  coder marks "insufficient" is left out of scoring for every pattern.
- Disagreement rate is the share of the scored features on which the coders differ. It chooses the margin
  as fixed in addendum A.1, point 3.
- If more than 8 of the 22 features are left out, the pattern verdict is reported as unreliable and only
  the feature-level results are given.

## Leak check before coding

Before the coders start, run `python3 loop-tools/leak_check.py`. It searches every input file for pattern
names and design terms (DevOps, SRE, site reliability, data scientist, webmaster, prompt engineer, CISO,
brand manager, product manager, mandated officer, tool-operator, scarcity boom, lead-industry, engineering
absorption, H-DevOps, signature). Any hit blocks coding until the file is rewritten neutrally by an agent
that is not a coder. Mentions inside quoted posting text (I3 period postings) are allowed only in
`instruments/I3-period-postings.csv` and the raw history files, which coders do not receive.
