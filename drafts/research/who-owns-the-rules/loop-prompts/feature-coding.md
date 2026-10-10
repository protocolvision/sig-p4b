# Feature-coding prompt (triangulation design, section 6.2)

Fixed before any present-day coding (addendum A.1, point 4; amended by addendum A.2 before any coding).
Two coders on different models (Sonnet 5.5 and Haiku 5.5) each receive this prompt and the inputs below,
independently. Coders never see `signatures.*`, `pattern-power*`, section 2 of the design, or any pattern
name. Nothing in this file may change after coding starts.

---

You are coding how a kind of work is forming in companies today. You will judge 21 features from evidence
files. You do not know, and should not guess, what the features will be compared with. Code only what the
evidence shows, with dates.

## The work being coded

People in companies who deploy AI agents (software that takes actions in business processes) and decide
what those agents may do: configuring, supervising and operating agents; setting, testing and changing the
permissions, limits, approval steps and escalation conditions agents act under; and deciding when those
change. Call this **agent work**. Any job title used mainly for agent work is an **agent-work title**.

## Inputs

Only these files (paths from `results/rerun-2026-10-10/`). Superseded copies whose names end in `-v1` are
not inputs.

- `instruments/I1*.md` and `.csv`: postings (`I1-postings.csv`), titles over time (`I1-titles-by-year.csv`),
  crawl coverage by half-year (`I1-coverage.csv`), duties inside existing occupations
- `instruments/I2*.md` and `.csv`, and `clusters/`: task statements (`I2-tasks.csv`) and task clusters
  (`I2-clusters.csv`) from postings and filings
- `instruments/I3*.md` and `.csv`: present postings compared with period postings (descriptive only)
- `instruments/I4*.md` and `.csv`: functions that laws and rules require
- `instruments/I5*.md` and `.csv`: vendor role definitions (`I5-vendor-roles.csv`), certifications
  (`I5-certifications.csv`), dated practitioner communities and open tooling (`I5-community-tooling.csv`),
  with dates
- `instruments/I6*.md` and `.csv`: practitioner speech records (loop v2, stratum S7; `I6-speech.csv`)
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
| N13 | Did certification (by any body: vendor, professional association or exam board) or statute come before a practitioner community? | Yes, dated | Certification before community, statute after |
| N14 | Did agent-work titles boom within 2–3 years of a specific new tool? | Titles name or follow one tool's release | Several tools |
| N15 | Are agent-work duties mainly operating a tool? | Most listed duties are operating, configuring or prompting one product or class of product | About half |
| N19 | Is agent work being absorbed with no new title, team or measure? | No agent-work title, no team, no measure in the inputs | Titles or teams exist but are rare (under 1% of agent-duty postings) |
| N20 | Were the first holders mostly existing staff given new or added titles? See definition below | Most | Mixed |
| N21 | Did the first agent-work roles or teams sit in operations or IT organisations, not research or analytics? Code only from the sources named under "Coverage rule" | Most | Mixed |
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

### Where each feature is answered

Answer each feature from the files and columns named here. If those columns cannot answer it, code
"insufficient"; do not answer from other files or from your own knowledge.

| ID | File: columns |
| --- | --- |
| N01 | First practice description: earliest `date` in `I6-speech.csv` with `in_company_agent_work` = yes; earliest `posted_date` in `I1-postings.csv` with `agent_duty` = yes; earliest `doc_date` in `I2-tasks.csv` with `source_type` = filing and `performer` = company. Title commonness: `I1-titles-by-year.csv`: `year`, `agent_title`, `share_agent_duty_postings`, `employers`. Truncation rule applies |
| N02 | `I2-clusters.csv`: `stable`, `onet_families`; `I1-postings.csv`: `agent_duty`, `duty_families` |
| N03 | `I5-community-tooling.csv`: `record_type`, `event_date` (the date of community, and of open tooling, is the third-earliest `event_date` of that `record_type`); `I5-certifications.csv`: `launch_date`; `I4-required-functions.csv`: `binding`, `required_function`, `effective_date` |
| N04a | `I1-titles-by-year.csv`: `year`, `agent_title`, `postings`; first practice description as N01. Truncation rule applies |
| N05 | `I6-speech.csv`: `measure_named`, `measure_origin`, `quote`; `I2-clusters.csv`: `label` |
| N06a | Coverage rule. `corpus-b/filings-index.csv`: `filed`, `company`, `software_native`; `I6-speech.csv`: `date`, `employer`, `employer_software_native`; `I5-vendor-roles.csv`: `duties_quote`, `published_date`, only where a row names an adopting customer firm |
| N07 | `I1-postings.csv`: `agent_duty`, `agent_title`, `employer` (count each employer once, as `I1*.md` reports) |
| N08 | `I1-titles-by-year.csv`: first `year` with any `agent_title` postings; first practice description as N01. Truncation rule applies |
| N09 | `I6-speech.csv`: `firm_cited_as_model`, `quote`; `I5-vendor-roles.csv`: `duties_quote` |
| N10 | `I1-postings.csv`: `duties_text`; `I6-speech.csv`: `measure_named`, `quote` |
| N11 | `I4-required-functions.csv`: `names_role`, `role_title`, `binding`, `addressee` |
| N12 | `I1-postings.csv`: `seniority`, `posted_date` for rows with `agent_title` = yes; `I6-speech.csv`: `speaker_seniority`, `date`. Truncation rule applies |
| N13 | `I5-certifications.csv`: `launch_date`; `I4-required-functions.csv`: `effective_date` where `binding` = yes; `I5-community-tooling.csv`: third-earliest `event_date` where `record_type` = community |
| N14 | `I1-titles-by-year.csv`: `year`, `agent_title`, `postings`; `I5-vendor-roles.csv`: `product`, `published_date`; `I5-community-tooling.csv`: `event_date` where `record_type` = open_tooling |
| N15 | `I2-tasks.csv`: `task`, `cluster_id` for postings with `agent_title` = yes in `I1-postings.csv`; `I2-clusters.csv`: `label` |
| N19 | `I1-titles-by-year.csv`: `agent_title`, `share_agent_duty_postings`; `I2-clusters.csv`; `I6-speech.csv`: `team_named`, `measure_named` |
| N20 | `I1-postings.csv`: `title`, `requirements_text`; `I6-speech.csv`: `speaker_path`, `quote` |
| N21 | Coverage rule. `I2-tasks.csv`: `org_unit` where `source_type` = filing; `I6-speech.csv`: `speaker_org_unit`; `I5-vendor-roles.csv`: `duties_quote` |
| N22 | `I1-postings.csv`: `purpose_statement`; `I6-speech.csv`: `role_purpose_quote` |
| N23 | `I6-speech.csv`: `date`, `framing_quote`. Truncation rule applies |
| N24 | `I5-vendor-roles.csv`: `product`, `role_type`, `first_capture`, `published_date` |

### Truncation rule (N01, N08, N04a, N12, N23)

Find the first practice description and the source type it comes from. Corpus start by source type:
postings, the first half-year in `I1-coverage.csv` with `share` of 0.30 or more; speech, 1 January 2024;
filings, 1 January 2022; vendor documents, the earliest `first_capture` in `I5-vendor-roles.csv`. If the
first practice description is dated within 12 months of the corpus start for its source type, code N01,
N08, N04a, N12 and N23 as **insufficient**, with the note "truncated". The start of the corpus, not the
start of the practice, would then set these answers.

### Coverage rule (N06a, N21, and the diffusion sequence)

The job-board crawl misses most of the largest technology firms and most utilities and transport firms.
Code N06a and N21, and any statement about the order in which kinds of firm took up agent work, only from
filings (`corpus-b/filings-index.csv`, and `I2-tasks.csv` rows with `source_type` = filing), practitioner
speech (`I6*`) and vendor documents (`I5-vendor-roles.csv`). Do not use `I1*` postings for them. Say in the
note that this rule was applied.

## Output

Write `results/rerun-2026-10-10/pattern-match/coder-<name>.csv` with columns
feature_id,value,evidence_file,evidence_row,evidence_date,quote,note. One row per feature, all 21 features.

## Scoring rules (applied by script after both coders finish)

- Scored features (15): N01, N02, N03, N04a, N06a, N08, N09, N12, N13, N15, N19, N20, N21, N22, N23. The
  other six (N05, N07, N10, N11, N14, N24) are reported feature by feature and not scored.
- A scored feature that either coder marks "insufficient" is left out for every pattern and both coders.
- Each coder's values are scored separately (yes 1, partial 0.5, no 0). Values are never averaged between
  coders. Each coder's raw score for each comparison is converted to a percentile against that
  comparison's own null distribution on the same features; the two coders' percentiles are then averaged
  (addendum A.2).
- Disagreement rate is the share of the scored features on which the coders differ. It chooses the margin
  as fixed in addendum A.2, point 9.
- If any scored feature is left out, the margins are recalculated on the remaining features with
  `python3 loop-tools/pattern_power.py <q> --drop <features>` for q = 0.2 and q = 0.3, before the scores
  are read.
- If more than 5 of the 15 scored features are left out, the pattern verdict is reported as unreliable
  and only the feature-level results are given.

## Leak check before coding

Before the coders start, run `python3 loop-tools/leak_check.py`. It scans every file listed under Inputs
(all I1–I6 `.md` and `.csv` files except `-v1` copies, `clusters/`, and `corpus-b/filings-*.csv`) for
pattern and design labels (DevOps, SRE, site reliability, webmaster, prompt engineer, CISO, mandated
officer, tool-operator, scarcity boom, boom then specialisation, lead-industry, data scientist pattern,
brand management pattern, product management pattern, engineering absorption, H-DevOps, signature). It
matches them only in prose: in `.csv` files, every column except those whose header contains "title" or
"occupation"; in `.md` files, every line except table cells under such headers. Common occupation names
are not labels and are not matched. Any hit blocks coding until it is cleared by an agent that is not a
coder: prose written by an instrument agent is rewritten neutrally; a label inside a quoted source passage
is replaced by "[label removed]" and the rest of the quote is kept. Raw period-posting text for I3 is kept in
`history/I3-period-postings.csv`, outside `instruments/`; coders do not receive it.
