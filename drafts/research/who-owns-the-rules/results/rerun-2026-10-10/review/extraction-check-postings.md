# Extraction check: job postings sample (rerun 2026-10-10)

Source: `corpus/b-raw/review/postings-sample.jsonl`, with 25 postings and 276 extracted items. Each item was judged by hand against the posting text. The verbatim test was mechanical: a substring match after whitespace normalisation. Item-level judgments are in `extraction-check-postings.csv`.

## Headline numbers

| Metric | Value | Basis |
|---|---|---|
| Precision (verbatim AND task) | **0.967** (267/276) | strict character match |
| Precision, with curly/straight quotes and full-/half-width punctuation treated as equal | 0.982 (271/276) | sensitivity check |
| Precision, if the 9 borderline items are also counted as non-tasks | 0.935 (258/276) | pessimistic bound |
| Verbatim rate | 0.982 (271/276) | |
| Task rate | 0.982 (271/276) | |
| Estimated recall | **0.894** (271 / (271 + 32)) | 32 missed duties with new content |
| Estimated recall, also counting 7 missed restatements of extracted duties | 0.874 (271/310) | pessimistic bound |
| Performer accuracy | **1.000** (276/276) | every item was labelled `person` |

How recall was estimated: the true positives are the 271 extracted items that are real tasks. The misses are duties I found in the posting that no extracted item covers. A miss that only restates an extracted bullet is listed in the CSV with `counted in recall: no` and is left out of the headline figure.

## Error types

**1. Duties in prose paragraphs are skipped (the main recall loss, 32 of 32 counted misses).** When a posting has a bulleted responsibilities list, the extractor often ignores the summary or overview paragraphs above it. It does this inconsistently: in Leidos, McKesson, Nordstrom R-865703, Nike and Databricks it did pull prose duties.
- Grafana: the whole "The Opportunity" paragraph was missed, which is 6 duties, including "own the regional build-out with your sales leader counterparts, adopting existing OSS Specific GTM strategies and developing new ones as needed". Recall for this posting is 9/15 = 0.60.
- Home Depot: the "Position Purpose" paragraph was missed, including "drive AI adoption and data science innovation across Store Operations, while enhancing and scaling existing data science and analytical products". 4 counted misses.
- Visa: the "Role Summary" was missed, including "support the design, implementation, and maintenance of data pipelines and processing jobs ...". Recall for this posting is 9/13 = 0.69.
- Cencora: the role's core duty, "ensures the quality and integrity of all the processes related to stored material ...", was missed.
- Inconsistency between the two Humana postings: "help patients regain strength, mobility and independence" was extracted from R-414387, but the same clause was missed in R-417160.

**2. Qualifications extracted as tasks (5 items).** These come from lists headed by qualification wording such as "You own this if you have", "Competencies" or "good fit if you".
- Nordstrom: "Ability to train and deliver POS/register training to support onboarding of new hires"
- Databricks: "Experience practicing live/vibe coding sessions with stakeholders"
- Anthropic Auth: "build primitives that are easy for other engineers to adopt correctly ..."
- Home Depot: "Deep understanding of IT needs for the team ..." This one is under Key Responsibilities, but it describes knowledge, not an action.

**3. Small departures from verbatim copying (5 items).**
- Typographic normalisation, 4 items: curly apostrophes became straight ones (Clio ×2, Nordstrom ×1), and half-width parentheses became full-width （） (DXC, Japanese text).
- One real word drop: "Experience establishing virtual teams" where the posting says "Experience **in** establishing" (Databricks). This item is also a qualification.

**4. Inconsistent splitting (minor; not counted as an error).** Some multi-task sentences are split, such as Graybar "Give presentations ..." and "answer questions ...", and Humana OT items 2/3, 8/9 and 10/11. Others are not, such as McKesson "drive project execution, manage risks, facilitate decision-making, and provide clear communication ...". All split parts are verbatim.

**5. Borderline items accepted as tasks (9).** Five are catch-alls: "Other duties as assigned" (TJX), "Other responsibilities as assigned" (Kohl's), and "Perform any other duties ..." / "Perform other duties as required" (Cencora, Accendra). Two are topic lists with no action verb (NVIDIA "Game Performance optimization, Linux Kernel, ..."; Anthropic "Global distribution and multi-region failover ..."). The other two are TJX "May be cross-trained ..." and Grafana "Executive sponsorship of key accounts ... will be key to your success". If the downstream analysis wants catch-alls removed, filter them out after extraction.

**Performer labels.** All 276 items are labelled `person`, and this is correct for every one. The sample contains no task done by software or an agent, so this check confirms there are no false `software/agent` labels. It does **not** test whether the extractor can spot non-human performers.

## Verdict at the 0.7 threshold

- Precision 0.967 (pessimistic bound 0.935): **PASS**
- Recall 0.894 (pessimistic bound 0.874): **PASS**
- Overall: **PASS.** Even the pessimistic bounds stay well above 0.7 for both metrics.

Caveats:
- Recall falls below 0.7 in individual postings that carry duties mainly in prose (Grafana 0.60, Visa 0.69).
- The recall estimate rests on a single reviewer's reading of the prose.
- Performer discrimination is untested in this sample.
- A cheap fix is to tell the extractor to also read summary and overview paragraphs, and to skip any list headed by qualification language.
