# Seeds v3 review

**Scope.** I read `loop-design-v2.md` §6, `review/seeds-v2-review.md`, `deviations.md` item 6, `corpus/b-raw/seeds/seeds-v3.jsonl` (120 records) and `seeds-v3-key.csv`. For comparison I used:

- 40 random spans from `extract/filings-haiku/tasks.jsonl` (41,868 spans; `random.seed(3)`);
- 40 random bullets from the raw postings in `corpus/b-raw/postings/*.jsonl` (20,875 postings), plus a further 40 drawn from the 3,726 posting bullets that mention AI agents.

No posting *task* records exist yet: the postings have not been extracted, so I compared seeds against raw posting bullets. No speech records exist either (`audio/` holds only mp3), so I skipped speech. I coded all 120 seeds blind before I opened the key. Format tells that the merge removes (ids, task index, model, `verbatim`) are ignored here, as instructed. I did not modify the seed files.

**Composition.** There are 20 seeds in each of six groups: PV, PE, RD, AO, applies-existing-rule OT and unrelated OT. Each group splits 6–7 / 6–7 / 6–7 across filing, posting and speech.

---

## 1. Were the v2 review's content fixes made?

| v2 item | Status | Notes |
| --- | --- | --- |
| Miscode: error-budget freeze call keyed RD | **Fixed** | Seed 30 is now "decide with product whether to raise the … threshold". |
| Miscode: reported decision, speaker only ran the migration | **Partly fixed** | Seed 15 adds "I was in the room". This is weak participation, but I accept it as RD. |
| Ambiguous: standing read-only limit with no actor | **Fixed** | Seed 12: "the controllership function established…". |
| Ambiguous: "conversation flows" (AO/PE) | **Fixed** | Seed 92 now says knowledge articles and answer templates. |
| Ambiguous: policy PDFs uploaded to the bot (AO/PE) | **Not fixed** | Seed 19 is unchanged, and §6 still lists "policies an agent reads" under PE. I code it AO and agree with the key, but the codebook ambiguity remains. |
| Paging tiers with no agent (PE, weak) | **Worse** | Seed 46 now only describes how alerts route. There is no act of setting the rule (see §2). |
| PE second codes on RD seeds | **Partly fixed, inconsistent** | PE is a second code on 12 RD seeds. It is missing on 8, 30, 63, 72, 99 and 110, which change or keep a limit, threshold, gate or access just as the others do. Seed 25 (keep the refund limit) gets PE; seed 8 (keep the disbursement limit) does not. |
| Hard negatives (AO near the PE boundary; OT that looks like PV, RD or PE) | **Fixed** | All 10 rewrites the v2 review proposed are present (31, 34, 61, 83, 106; 29, 51, 62, 94, 105), plus more (6, 17, 37, 68, 71, 96, 111; 2, 5, 44, 50, 59, 77, 95). Rule vocabulary now appears in 14/20 applies-rule seeds and 12/20 AO seeds, against 13–14/20 positives. Keywords alone no longer separate positives from negatives. |
| Agent-era unrelated OT | **Fixed, with two miscodes** | Seeds 75, 100, 107, 108, 119, 18 and 28 are now agent-era. But 32 and 38 are AO under §6 (see §2). |
| No proxy phrasing | **Mostly fixed** | The verbatim gap phrases ("never states", "nobody wrote down") are gone. What remains: RD seeds still name two functions explicitly in 11/20 (other groups ≤ 2/20). PV still uses "outside the workflow" (27, 54), "in practice" (57) and "map who can approve what" (93), which is the PV proxy almost word for word. Seed 36 has "must not answer … handoff". Because negatives now share the vocabulary, this matters much less than it did in v2. |
| No length tell | **Fixed** | Median words per group: PV 16, PE 17, RD 17, AO 18.5, applies-rule 18.5, unrelated 15. The ranges overlap fully (10–24). |
| Lower-case fragments and performer spread | **Partly fixed** | 64/120 spans start in lower case. Performer is still mostly `person` (see §3). |
| PV+PE double-code case | **Fixed** | Seeds 14 and 76. |
| Domains beyond SRE and clinical work | **Fixed** | Seeds now cover AP, procurement, IAM, refunds, underwriting and HR. |
| Sourcing (§6: "modelled on documented historical practice") | **Regressed** | 38 of 60 positives are keyed `invented scenario, no cited source`. Deviation 6 does not record this departure from §6. Add it there. |
| Scoring rule for second codes (primary only, or both) | **Not visible** | Deviation 6 does not state one. See the recommendation in §4. |

---

## 2. Blind coding against the key

I coded all 120 seeds blind, then compared them with the key. "Exact" means my code set (primary plus second) equals the key's.

| Group | n | Primary agrees | Exact set agrees |
| --- | --- | --- | --- |
| PV | 20 | 20 | 19 |
| PE | 20 | 18 | 18 |
| RD | 20 | 15 | 10 |
| AO | 20 | 20 | 20 |
| OT applies rule | 20 | 20 | 20 |
| OT unrelated | 20 | 18 | 18 |
| **All** | 120 | **111 (92.5%)** | 105 (87.5%) |

### Primary-code disagreements (the key is wrong or ambiguous)

| Seed | Key | Mine | Span (abridged) | Reasoning |
| --- | --- | --- | --- | --- |
| 32 | OT (unrelated) | AO | "Deploy AI agents to triage support tickets and schedule appointments…" | Deploying agents is building an agent; §6 AO covers "building … an agent". Ambiguous at best. |
| 38 | OT (unrelated) | AO | "we are building an AI assistant that summarizes customer calls…" | This is the AO definition word for word. Miskeyed. |
| 45 | PE | OT | "we hand incident command to the next region … has to get a clear acknowledgement" | The team is *following* a hand-off procedure. The procedure is set in seed 120. Under §6 this is applying an existing rule, so OT. |
| 46 | PE | OT (ambiguous) | "only the severe alerts page anyone on my team, everything else goes to a queue" | This describes how routing currently works. No one sets, changes or tests anything. It could be read as PE only if the speaker is presumed to own the routing. |
| 53 | RD | PE | "we decided to retire half of our low-severity pager alerts, they were just noise" | It is a decision to retire escalation conditions, but RD needs two functions or a stated trade-off, and neither is present. Under §6 it is PE. |
| 39 | RD (+PE) | PE | "we determined that agents should no longer be permitted to send customer communications without review…" | No second function and no trade-off. It is PE only. |
| 69 | RD (+PE) | PE | "decided to extend the autonomous trading limits of the pricing agent to two additional product lines" | Same as 39. |
| 109 | RD (+PE) | PE | "Lead the monthly decision on which refund types the support agent keeps and which return to human review" | Same as 39. |

Seeds 39, 69 and 109 appear as primary agreements in the table above only in the sense that the key carries PE. My primary code is PE, and their RD code fails §6's RD condition. A coder who applies §6 literally will miss RD on all four of 39, 53, 69 and 109. That depresses measured RD recall for reasons that have nothing to do with the coder.

### Second-code differences (no exclusion needed)

| Seed | Key | Mine | Note |
| --- | --- | --- | --- |
| 8, 30, 63, 72, 99, 110 | RD | RD+PE | Each keeps, raises or retires a limit, threshold, gate, requirement or access right, which is PE under §6. This is inconsistent with 9, 11, 13, 25, 49, 64, 70, 78 and 86. |
| 76 | PV+PE | PV | "recommend changes" proposes a change and does not make one, so I see no PE. |

### Weak but kept

- **3 (PV).** "document the conditions they cited". The rule is only implicit.
- **82 (PV).** "ten of eleven had the same reason". The rule is not named.
- **15 (RD).** The speaker was "in the room".
- **110 (RD).** A committee is implied to be cross-functional, but no functions are named.
- **17 and 31 (AO).** These test agents against rules, and the PE proxy includes "testing what … agents may do". The boundary rule resolves them to AO. They are the sharpest cases in the set and are intended as such.

---

## 3. Remaining content tells

### Seeds against real records

1. **The filing positives describe internal control work that real filings almost never contain.** Of 41,868 real filing spans, 492 (1.2%) combine AI/agent with a rule word, and they are product or risk language, e.g. "governance guardrails ensure agents act only on information each user is authorized to see" and "may operate with limited human oversight". A search for internal-control acts with AI ("internal audit", "audit committee", "management elected", "we determined", "decided to", "we eliminated", "approval tiers", "controllership") returns **1 irrelevant hit**. The 20 filing positives (1, 3, 4, 8, 12, 13, 14, 39, 49, 54, 57, 60, 64, 65, 69, 73, 98, 99, 115, 120) state specific internal decisions, limits and reviews. Most filing applies-rule seeds (5, 22, 23, 29, 52, 87, 116) are similarly concrete. The rule "concrete internal procedure in a 10-K span → seed" finds about 30 of the 40 filing seeds. Dropping seeds cannot fix this.
2. **Posting seeds are more specific than real postings.** Seed postings are all imperative duty lines that name thresholds ($500, $2,000), counterpart functions or agent types. Real agent-related bullets have a median of 24 words. They are dominated by skills and marketing ("Experience with … agentic AI orchestration (tools, workflows, guardrails)", "Agentforce is the future of AI"). Their rule words are generic ("access control, monitoring and human oversight"). No seed posting is a qualification line or a marketing line. None of the 40 random posting bullets mentioned AI at all.
3. **Performer.** Real filings: 17/40 person, 18/40 software or agent, 3 both, 2 unclear. Seed filings: 28/40 person, 9 both, 3 software or agent. No seed is `unclear`. All 20 AO seeds are `person`, although each clause contains an agent. The real extractor tends to give `both` or `software or agent` when an agent is in the clause.
4. **Agent-free positives.** Seeds 30, 35, 45, 46, 53, 58, 63, 74, 80, 82, 98 and 120 carry the SRE and clinical analogues and mention no agent or AI. In an agent-filtered corpus, rule work with no agent is unusual. This is moderate.
5. **Speech is unmeasured.** No transcripts exist. Seed speech is clean, single-clause and first-person, with hedges in only a few ("honestly", "basically").
6. **Duplication inside the set.** Seeds 79 and 112 are the same fact (Nordic expansion, hiring account executives) in speech and in filing form. Seeds 45 and 120 are the same hand-off procedure. Seed 75 copies a real filing span ("incorporate AI into our products and services") and is harmless.

### Positives against negatives (within the seed set)

7. **Performer.** Performer ≠ person on 18 seeds, and 13 of them are negatives (applies-rule 9, unrelated 4). All RD, AO, posting-positive and speech-positive seeds are `person`. Performer = `software or agent` occurs only in applies-rule seeds (3/3).
8. **Decision verbs and named functions.** Decision verbs (decided, retire, kept, raise, elected, determined…) appear in 19/20 RD seeds against ≤ 3/20 in every other group. Two or more named functions appear in 11/20 RD seeds against ≤ 2/20 elsewhere. The first is close to the definition of RD and is acceptable. The second is the proxy and remains a cue.
9. **Unrelated negatives contain no rule vocabulary** (0/20). They test only the OT/AO boundary, which is acceptable now that 40 hard negatives exist.

---

## 4. Verdict

**Usable with listed exclusions.**

**Drop:** 32, 38, 39, 45, 46, 53, 69, 109.
**Optional:** drop 112 (duplicate of 79).

After the drops: PV 20, PE 18, RD 16, AO 20, applies-rule 20, unrelated 18. The RD gate (recall ≥ 0.7 and Wilson lower bound ≥ 0.5) then needs 12/16 (0.75, lower bound 0.505). PE needs 14/18. Every RD kind keeps at least 5 seeds.

These conditions require no edit to the seeds or the key. Record them in `deviations.md` before coding:

1. **Second-code scoring.** A PE code on any RD seed is never scored as a false positive. A missing PE on 76 is not scored as a miss. Score recall on the primary code, and score PE recall only on the PE group plus 14.
2. **Sourcing.** Record that 38 of 60 positives are invented and not modelled on documented practice, which departs from §6.
3. **What seed recall measures.** Report seed recall as recall on explicit, seed-style text. Tells 1 and 2 mean filing and posting seeds are much more explicit than real records, so seed recall is an upper bound for real records. A pass licenses "absence is interpretable" only for rule work stated as plainly as the seeds state it.
4. **Performer at merge.** If the merged pool shows `performer` to coders, hide it or regenerate it with the real extractor. Otherwise tells 3 and 7 stay live.
5. **Speech and posting comparison.** Repeat this comparison against extracted posting and speech records once they exist.
