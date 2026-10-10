# Loop design, version 2: calibrated, with practitioner speech

Protocols for Business · version 2 · 10 October 2026 · pre-registered: committed before any v2 evidence is
collected · supersedes [`loop-design.md`](loop-design.md) for the next run; v1 stays as the record of the
first run

## 1. Why a second version

The first run (`results/loop-2026-10-10/`) found no public record of anyone finding unwritten rules (PV)
or deciding rule changes across functions (RD), and found rule design (PE) thin and not clustered. Two
reviews undercut what that result can mean.

**The red team** showed that clusters followed source types, that no rule-design record showed a person
doing the work, that the two coders were the same model with near-identical notes, that the PV definition
needed a stated purpose public summaries rarely give, and that the clustering failed our own stability
test.

**A calibration check** showed that this method, applied early to past roles, would have called brand
management, the CISO and site reliability engineering "absorbed", and would have called the prompt
engineer and the chief knowledge officer distinct roles. Its verdicts are close to a coin toss. The roles
it misses share one feature: an internal agreement gave a practitioner a trade-off to own (a brand's
profit, an error budget, a board mandate), and that agreement stayed out of public documents for years.
That agreement is the RD layer the first run could not see. So "absent in public documents" fits both a
future with no role and a future where a role is forming inside a few firms.

Version 2 adds two kinds of evidence that can reach that layer (practitioner speech and rule-change
events), measures absorption directly, tests whether coders can see PV and RD at all, and tests the method
against history before trusting it on the present. Interviews are replaced by podcast episodes and recorded
talks, which can be sampled, re-run and checked by others.

## 2. What changed

| Issue | Source | Change in v2 |
| --- | --- | --- |
| Public documents miss agreement-based roles | Calibration | New strata: practitioner speech (S7) and rule-change events (S6). A calibration test on historical recordings (section 8) |
| Interviews are costly and not reproducible | Request | Podcast transcripts and YouTube talks replace interviews; frame in `sources-v2/media-current.csv` |
| Postings were found by searching for "agent" | Red team | S1 samples postings for ten existing occupations and records whether agent duties appear. Absorption is measured directly |
| Clusters follow source types | Red team | Duty lists (regulations, vendor guides) are kept as duty sets, not bundles. Clusters are reported with source purity; 80% or more from one stratum is flagged as a source artefact |
| One document dominates a cluster | Red team | At most five records per document |
| Records describe agents, not people | Red team | `performer_type` field; agent-performed records are excluded from bundling |
| No record shows a person doing rule work | Red team | Load-bearing claims need a primary source (P); aggregator pages excluded; vendor documents capped at 15% of the pool and labelled "assumed work" |
| PV needed a stated purpose | Red team | Observable proxies for PV and RD (section 6) |
| Coders could not be shown to see PV or RD | Red team | Twenty seeded records with known codes hidden in the pool; recall reported per code |
| Coders were the same model | Red team | Second coder is a different model or a person; notes never shared |
| AO/PE boundary inconsistent | Red team | A fixed boundary rule (section 6); up to two codes per record, both counted |
| Unstable clustering | Red team | Three repeated clusterings of the final pool give a noise baseline; stability is judged against it |

## 3. Questions

1. **Activities.** As agents take on operational work, which human activities appear, grow, move or shrink,
   and which bundle under one accountability? (As v1.)
2. **Absorption.** In postings for existing occupations, how often do agent and rule duties appear, and in
   which occupations?
3. **Speech.** Do practitioners describe finding unwritten rules, or deciding rule changes across functions,
   when they talk about their work, even though written sources don't?
4. **Agreements.** Do firms outside AI labs assign the trade-off over agent rules to a named person by a
   written rule?
5. **Calibration.** Would this design have detected earlier roles whose authority came from an internal
   agreement, and how early?

## 4. Hypotheses, fixed before the run

| ID | Hypothesis | Refuted if |
| --- | --- | --- |
| H-cal | Practitioner speech describes the authority arrangement of agreement-based roles (SRE, DevOps, CISO) at least two years before postings commonly name the role, while written sources do not | For two or more of SRE, DevOps and CISO, the earliest dated description of the arrangement in recordings is no earlier than in postings or official documents |
| H-speech | PV and RD activities appear in practitioner speech about running agents, in at least 5% of coded activity mentions | Below 2% of coded mentions, with coder recall on seeded PV and RD cases of 0.7 or more |
| H-absorb | Agent and rule duties appear inside postings for existing occupations more often than as new titles | New-title postings outnumber existing-occupation postings that carry agent or rule duties |
| H-federated | Rule design clusters with agent operations inside each function, not in one cross-functional cluster | 60% or more of PE records fall in one cross-functional cluster that is stable against the noise baseline and below the purity threshold |
| H-number | The agent operations bundle lasts only where its holder owns a number (accuracy, containment, error rate) | Agent operations postings and speech show the bundle persisting with no owned number |
| H-agreement | At least one firm outside AI labs has published a rule or policy for its agents that names who may change it | No such document found in S6 (record what was searched) |

**Rivals, given equal effort:** R1, it's all engineering (rule work becomes policy code in platform
teams); R2, privacy-led AI governance absorbs it; R3, agent operations is the durable role and rule work is
a part of it; R4, nobody does PV or RD, in speech or in writing.

## 5. Evidence strata

| Stratum | Sources | Change from v1 |
| --- | --- | --- |
| S1 Postings for existing occupations | A sample of postings for ten occupations: controller, accounts payable specialist, support operations manager, revenue operations manager, procurement specialist, legal operations manager, HR operations specialist, identity and access administrator, compliance analyst, platform engineer. Sample without searching for AI terms; record whether agent or rule duties appear | Measures absorption; replaces keyword search |
| S2 Practitioner writing | Engineering and operations blogs, case studies, postmortems | Primary documents only |
| S3 Regulation and audit | Laws, standards, audit and supervisory guidance | Recorded as duty sets, not bundles |
| S4 Research on work | Studies, surveys, ethnographies | As v1 |
| S5 Vendor documentation | Product and admin guides | Capped at 15% of the pool; labelled "assumed work" |
| S6 Rule-change events | Incident postmortems, policy changelogs, published internal policies for agents, expense or approval policies rewritten for agents, audit findings, enforcement actions, lab scaling-policy revisions | New: where agreements and rule changes become visible |
| S7 Practitioner speech | Podcast episodes and YouTube talks by people running functions that use agents: frame in `sources-v2/media-current.csv` | New: replaces interviews |
| S8 Industry analogues | Industries where rule work for automated actors is already regulated, scored for resemblance to agent-run business; the closest is studied in depth. Design: [`industry-analogue-design.md`](industry-analogue-design.md) | New: shows what rule work becomes once a forcing lever applies |
| H Historical recordings | Talks and podcasts from the formation of SRE, DevOps, social media management, data science, the CISO, prompt engineering and the chief knowledge officer: frame in `sources-v2/media-historical.csv` | New: calibration only, never pooled with S1–S7 |

**Sampling the media frames.** The frames were built by searching for speakers by role and function, not by
topic, and without our vocabulary or words such as rules, policy or governance; each item records the query
that found it. A run samples from the frame at random, stratified by function, with at most two items per
show or channel and at most a third from vendors or consultants. Speakers who sell agent products are kept
but flagged.

**Transcripts.** Fetch with `loop-tools/fetch_media.py` on a machine with open network access: YouTube
captions through `yt-dlp`, podcast transcript pages as text, and a list of items that need manual
transcription. Transcripts stay local (`sources-v2/transcripts/` is ignored by git) because they are other
people's work; only extracted records with quotes of 40 words or fewer are committed.

**Extracting records from speech.** One record per activity a speaker says they or their team do, with a
timestamp. Fields as v1, plus `speaker_relation` (`self`, `own team`, `other team`, `general claim`) and
`performer_type` (`person`, `agent`, `both`). General claims about "companies" are kept but don't count as
evidence of practice.

## 6. Coding, version 2

Each record gets up to two codes; both count in the analysis.

| Code | Observable proxy (record must show at least one) |
| --- | --- |
| PV: finding the rules | Reviewing overrides, exceptions, escalations, workarounds or agent failures *and* naming a rule, a gap between the written and the actual rule, or a change that followed; mapping who may approve, see or change what across teams |
| PE: designing rules | Setting, changing or testing what people or agents may do: permissions, limits, approval gates, escalation and hand-off conditions, never-answer lists, policies an agent reads, interfaces between teams or agents |
| RD: deciding rule changes | A decision to change, keep or retire a rule, limit or threshold, where two or more functions are named or a trade-off is stated (speed and risk, revenue and loss) |
| AO: agent operations | Building, prompting, tuning, supplying content to, monitoring or fixing an agent, where no rule others rely on is set |
| OT: other | Anything else |

**Boundary rule.** Setting an agent's escalation, hand-off or never-answer conditions is PE (others rely
on it); writing its prompts, content or tests is AO. Applying an existing rule (an agent or person
approving within policy) is OT.

**Seeded cases.** A separate agent writes twenty records with known codes (ten PV, five RD, five PE),
modelled on documented historical practice in other fields (for example an error-budget decision, a policy
change after repeated escalations), in the same format as real records. They are hidden in the pool. Coder
recall on seeds is reported per code. If recall for PV or RD is below 0.7, an absence of PV or RD is
reported as uninterpretable. Seeds are removed before clustering.

**Coders.** Coder A is the model used for collection; coder B is a different model or a person. They
never see each other's notes. Kappa is reported per code, including on seeds.

## 7. Clustering, version 2

- **Bundling evidence,** in order: the same person or team describing several activities (speech, postings,
  practitioner writing); the same performer across documents; the same decision; the same knowledge.
  Items listed together in a regulation or vendor guide are a duty set, not a bundle.
- **Agent-performed records** are excluded from bundling and reported separately as automation.
- **Within and across strata:** cluster each stratum on its own and the pooled set; report each cluster's
  source purity. A pooled cluster with 80% or more of its records from one stratum is flagged as a possible
  source artefact.
- **Noise baseline:** three fresh clusterers run on the same final pool; their mean pairwise adjusted Rand
  index is the baseline. Accumulation rounds (one stratum added per round, random order drawn before the
  run) are stable if each of the last two transitions reaches 0.6 and is no more than 0.1 below the
  baseline.

## 8. Calibration test

Run before the present-day analysis is interpreted.

1. **Media lead.** Code each item in `media-historical.csv` for whether it describes (a) the activity
   bundle, (b) the authority arrangement (an agreement on a trade-off, a mandate, a budget, an owned
   number), and (c) the role's title. Record the date of each.
2. **Written comparison.** For each role, take the earliest dated description of the arrangement in
   written public sources and the year postings commonly used the title (from the exploratory lineages,
   checked against primary sources where possible).
3. **Lead time.** The difference between the earliest recording and the earliest written source that
   describes the arrangement. H-cal is tested on SRE, DevOps and CISO; social media manager, data scientist,
   prompt engineer and chief knowledge officer are comparison cases.
4. **Contamination.** Coders know how these roles turned out. To limit hindsight, they code only what a
   recording says, with its date, and never whether the role lasted. A blind agent backtest on period
   sources is not used for this reason. A human-coded backtest on archived job advertisements (for example
   the Atalay et al. newspaper data, or Internet Archive captures of job boards) is listed as a separate,
   optional study.
5. **Use.** If H-cal holds, S7 is treated as an early-warning source and its PV and RD findings carry
   weight. If it fails, S7 findings are reported as descriptive only.

## 9. Interpretation rules, fixed before the run

- v1 thresholds stand (60% for "clusters together", 40% for "dispersed" and co-clustering), applied to
  records with person performers only, after removing seeds, and only to clusters that are not flagged as
  source artefacts.
- PV or RD "absent" may be reported only if seed recall for that code is 0.7 or more.
- Findings from S7 are reported separately from written strata, then pooled.
- Every finding is labelled with the strata that support it; a finding supported by one stratum is
  reported as single-source.
- The calibration result is reported first and decides how much weight S7 carries.

## 10. Run order

1. Fetch transcripts for a stratified random sample of the two media frames (`loop-tools/fetch_media.py`).
2. Collect S1–S7 with the v2 rules; one collector per stratum, as in v1.
3. Write seeds; build pools; hide seeds.
4. Code (two coders, different models or a person); report seed recall.
5. Cluster: within strata, accumulation rounds, and three repeats on the final pool.
6. Run the calibration test.
7. Scripted analysis, red team, report.

## 11. Outputs

`results/loop-v2-YYYY-MM-DD/`: as v1, plus `seeds/` (seed records and their codes, kept out of the pool
copies the clusterers see), `calibration.md`, `purity.md`, and `media-records/` (records extracted from
transcripts, with timestamps and short quotes).

## 12. Limits

- Podcasts and talks favour articulate, senior, often vendor-adjacent speakers; frontline practice is
  underrepresented.
- What people say they do differs from what they do; speech is evidence of how work is described.
- Historical recordings before about 2005 are scarce, which weakens the CISO calibration case.
- Coders and collectors still share model knowledge of how past roles turned out.
- Transcripts from automatic captions contain errors; quotes must be checked against the audio before
  publication.
