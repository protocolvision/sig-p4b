# Seeds v2 review

**Scope.** I read: `loop-design-v2.md` §6, `pipeline-review.md` C8, `corpus/seeds/seeds-v2.jsonl` (60 records) and `seeds-v2-key.csv`, plus 40 real filing records from `corpus/b-raw/extract/filings-haiku/tasks.jsonl` (Python `random.seed(1)`, `random.sample`). I did not compare against real job-posting (J) or speech (S) records, because those files were out of scope. Tells for J and S seeds are therefore inferred, not measured.

**Composition.** There are 10 seeds each for PV, RD, PE and AO, plus 10 OT "applies existing rule" and 10 OT unrelated. Compared with v1, this fixes C8's "recall only" point and the RD/PE counts. Three problems remain: the filing seeds are trivially detectable, the negatives are too easy to test over-coding, and second codes are applied inconsistently.

---

## Critical fixes

### K1. The filing seeds are mechanically detectable. Fix all 20 `F…` ids.

The 20 filing seeds differ from the real filing records on structural fields. A string match is enough to find them; nobody has to read the text.

| Feature | Real filings (n=40) | Filing seeds (n=20) |
| --- | --- | --- |
| `doc_id` pattern `F` + 10 digits + `-YY-` + 6 digits + `_n` | 40/40 | **0/20**: they have 13 digits, e.g. `F0001298420286-26-097641_6685` |
| `employer` field present | **0/40** | 20/20 |
| task index `:0` | 2/40 (real indices run to :16) | **20/20** |
| span starts lower-case (fragment) | 17/40 | 0/20 |
| `verbatim: false` | 2/40 | 0/20 |
| performer = person | 17/40 | 17/20 |
| median words | 14 | 18 |

**Rewrite.** Seed ids should be copied from the real format, using a real-looking 10-digit filer prefix and an unused accession. Drop `employer` on F records. Give each seed doc 2–6 sibling tasks with indices other than :0; the siblings can be filler OT tasks drawn from the same invented passage. Let about 40% of spans start mid-sentence in lower case, and set some to `verbatim: false`. Spread performer across person, both and software-or-agent.

All 60 seeds also carry task index `:0`, and each one is the only task in its doc. Apply the same sibling fix to the J and S seeds, unless the real J and S pools are mostly single-task docs. I did not check this.

### K2. The filing seed content is not 10-K content.

Real filing spans are marketing, strategy and risk-factor fragments, for example "incorporate AI into our products and services" and "CrowdStrike is driving the next generation of AI-powered agentic cybersecurity". No real record in the sample describes internal control work. A 10-K would never contain these:
- `F0001298420286-26-097641_6685`: "risk committee … voted to keep the daily payment limit … despite complaints"
- `F0001665100286-26-018158_4122`: "internal audit team … identified the managers who authorize those exceptions"
- `F0001277617287-26-031160_9459`: "documents which approvers certify access the role matrix does not permit"
- `F0001640595281-26-074709_1965`: "records which launch requirements were bypassed"
- `F0001740710286-26-057024_7233`: "Engineering and finance leadership agreed to lift the daily cap…"

**Rewrite.** Recast them in the forms filings actually use:
- Item 1A risk-factor language, e.g. "we have established limits on the transactions our AI agents may execute without human approval, and these limits may prove inadequate"
- Item 9A controls language, e.g. "management identified that certain purchase approvals occurred outside the automated workflow and remediated by…"
- Item 1 governance text, e.g. "our AI governance committee, comprising legal, security and product leaders, approves changes to agent permissions"

Positives that cannot be written credibly as filing text should move to J or S. That keeps the ratio of seeds to real records per source honest.

### K3. Second codes are inconsistent, so PE precision will be mis-scored.

§6 allows two codes. Under the PE proxy, "Setting, changing … permissions, limits, approval gates", every RD seed that changes or keeps an agent's limit or gate is also PE. Only `J479146:0` carries the PE second code. Add `second_code=PE` to:
- `J702326:0`: the 15% discount authority of the quoting agent
- `F0001740710286-26-057024_7233:0`: the spend cap for the agents
- `F0001560559285-26-089929_6220:0`: removing a manual review gate
- `S685184:0`: retiring a sign-off gate
- `S578365:0` and `S829070:0`: the agent's refund and ticket-closing permission (weaker; "keep" decisions)
- `F0001298420286-26-097641_6685:0`: keeping a payment limit (weaker)

Otherwise a coder who correctly codes RD+PE is charged a PE false positive. The alternative is to state in §6 that seeds are scored on primary code only. Pick one of the two and write it down before the run.

### K4. The negatives do not test over-coding.

C8 asked for near-misses. The negatives are not near-misses.
- **Unrelated OT (10).** None of them mentions AI or an agent (0/10), and all are 7–13 words: payroll, journal entries, a warehouse lease, a trademark dispute. In the real filing sample, 18 of 40 records mention AI. These seeds test nothing. Replace at least 6 with agent-era OT that matches what the corpus actually holds, e.g. "deploy AI agents to triage support tickets and schedule appointments", "rely on third parties to support our use of AI".
- **AO (10).** Only `S901710:0` ("policy PDFs" in the bot's knowledge base) and `F0001174447287-26-062644_5552:0` ("conversation flows") come near the PE boundary. The other eight never mention a limit, escalation, approval or policy, so a coder who over-codes rule work loses nothing on them. Rewrite at least 5 so that a rule appears but is not set, each paired with the boundary rule:
  - `J288499:0` → "Rewrite the claims-intake assistant's system prompt so it states the $2,000 escalation threshold set by claims leadership, and test it on sample emails" (AO: it writes the prompt and does not set the threshold).
  - `J800675:0` → "Build regression tests checking that the contract-summary agent still hands off to a lawyer on the clauses legal listed" (AO, although the PE proxy includes "testing what … agents may do". This is the sharpest boundary case in the codebook.)
  - `J172103:0` → "Fix the enrichment agent's failing tool calls after security revoked its CRM write scope" (AO: the rule change is someone else's).
  - `S830901:0` → "rewriting the invoice-matching prompt so it applies the tolerance finance gave us" (AO).
  - `F0001497183281-26-025119_8996:0` → drop the codebook-verbatim wording "builds, prompts and monitors" (see K5) and add "within the review policy set by our compliance function".
- **Applies-existing-rule OT (10).** All ten are the easy form, "approve X within policy/cap/matrix". None looks like PV or RD while being OT. Rewrite at least 5 as hard negatives:
  - `J360494:0` → "Handle the expense claims the audit agent escalates and override its decision when the receipt is valid" (OT; overrides without review and without naming a rule; looks like PV).
  - `J796414:0` → "Grant one-off access exceptions requested through the IAM workflow and log them" (OT; the PV proxy mentions exceptions).
  - `J460160:0` → "Attend the weekly change advisory board with finance and IT and record which changes were approved" (OT; two functions named, but no decision on a rule; looks like RD).
  - `S980770:0` → "I check whether the agent's refunds last month stayed under the cap and send the numbers to finance" (OT; reviewing agent output against an existing rule without finding a gap; looks like PV).
  - `F0001417225286-26-075078_2320:0` → "our AI agent escalates claims above its authority to a human adjuster, who decides them under the policy terms" (OT; a hand-off is executed, not set; looks like PE).

### K5. The positives are written in the codebook's own proxy phrasing.

C8 flagged this, and v2 still does it. Each RD seed names two functions and/or states a trade-off in the proxy's words:
- `J714006:0` "weighing roadmap dates against reliability work"
- `F…7233` "weighing launch speed against cost overruns"
- `F…6685` "with representatives from treasury and operations"
- `S578365:0` "Support and risk argued…"

PE seeds lift words directly from the proxy:
- `J401924:0` "Configure approval gates"
- `S835567:0` "must never answer … and the hand-off"
- `J864878:0` "escalation criteria"

PV seeds spell out the "gap between written and actual rule" wording:
- `J917710:0` "that the payment policy never states"
- `S597128:0` "not in any playbook"
- `S168157:0` "nobody wrote down"
- `J163616:0` "the real cutoff"
- `S708064:0` "laid the escalation page next to what people actually did"

A coder who keys on these phrases scores well on seeds and badly on real records, so recall is inflated. **Rewrite.** Keep the facts but make the rule and the second function implicit, as real postings put it. For example, `J702326:0` → "Own discount governance for the quoting agent; partner with Legal and Sales Ops on approval thresholds". Real text rarely states the trade-off, so drop the explicit trade-off clauses.

### K6. Length predicts the code within the seed set.

| Seed type | Median words | Range |
| --- | --- | --- |
| Positives | 24 | 19–31 |
| AO | 16.5 | 11–21 |
| Applies-existing-rule | 12 | 9–19 |
| Unrelated | 11 | 7–13 |

A rule of "≥19 words → rule code" classifies about 55 of 60 seeds correctly. **Rewrite.** Match the length distribution across types. Pad negatives with realistic context, and cut 5–8 positives to 10–15 words, e.g. `S578365:0`, `S829070:0`, `S685184:0`, `S168157:0` and `S597128:0`.

---

## Miscoded or ambiguous seeds

| Seed | Key | My code | Why |
| --- | --- | --- | --- |
| `J714006:0` | RD | **OT** (or ambiguous) | Running the freeze call when the budget is spent *applies* the error-budget policy. No rule, limit or threshold is changed, kept or retired. Rewrite: "…decide with product whether to raise the error-budget threshold that triggers a launch freeze". |
| `S355953:0` | RD | **OT** (as written) | The speaker's own task is "I just ran the migration". The decision belongs to the CISO and the head of platform. Either code the reported decision (and say so in §6), or rewrite in the first person as a participant in the decision. |
| `F0001995044285-26-090443_1417:0` | PE | ambiguous PE/OT | It states that a standing limit exists ("The Company limits agents to read-only…"), not that someone set or changed it. Add an actor and an act, e.g. "our controllership function established…". |
| `S901710:0` | AO | ambiguous AO/PE | The PE proxy includes "policies an agent reads", and here the speaker uploads policy PDFs into the bot. The intended key, AO, holds only if "policies an agent reads" means policies that govern the agent. Clarify §6, or replace the seed. |
| `F0001174447287-26-062644_5552:0` | AO | ambiguous AO/PE | Virtual-agent "conversation flows" normally encode the hand-off to a live agent, which the boundary rule makes PE. Change it to "knowledge articles and greeting/answer templates". |
| `S185831:0` | PE | PE (weak) | Paging tiers are escalation conditions, so PE holds. But no agent appears, and alert routing sits close to AO/ops tuning. Acceptable; consider adding the agent. |
| RD seeds listed in K3 | RD | RD+PE | Second code missing. |

The other 21 positives and 19 negatives match their keys under §6.

---

## Tells (summary)

1. **Structural (filings).** `doc_id` has 13 digits instead of 10. The `employer` field is present on all 20, against 0 of 40 real filings. Every seed is task `:0` with no sibling tasks.
2. **Register.** Every seed is a complete, capitalized clause (0/60 start lower-case, against 17/40 real). None is a sentence fragment, a list of things, or marketing language. All 60 are `verbatim: true`.
3. **Field values.** 55 of 60 seeds have performer = person, against 17 of 40 real filings. The speech seeds' `speaker_relation` is only ever self or own team. All seeds have model `claude-haiku-5-5`; check that this matches the model used for real J and S extraction.
4. **Employers.** Every employer is invented, and the names follow one pattern (bird, tree or place word + industry noun: "Kestrel Cloud", "Tallow & Reed"). Real filings name real issuers (CrowdStrike, Adobe, NVIDIA). "Juniper Networks Co." is close to a real company; rename it.
5. **Codebook-proxy phrasing** (K5) and the **length gradient** (K6).
6. **Unverified for J and S.** Real speech is likely to contain fillers, hedges and run-ons; the seeds are clean single sentences. Sample 40 real S and J records and match them before the run.
7. **Source analogues.** Four positives say almost the same thing: "outage/release consuming >20% / a fifth of the error budget" (`F…1965`, `J935601:0`), and the freeze/exception policy (`S383051:0`, `F…1417`). The near-duplicates make the set easier to spot.

---

## Power (gate in §6)

Wilson 95% intervals at n=10:

| Observed recall | Interval |
| --- | --- |
| 7/10 | 0.40–0.89 |
| 8/10 | 0.49–0.94 |
| 10/10 | 0.72–1.00 |

As a test of whether true recall is at least 0.7, the gate passes a coder whose true recall is 0.5 with probability 0.17, and one at 0.6 with probability 0.38. It fails a coder whose true recall is exactly 0.7 with probability 0.35. **Not adequate.** At 7/10 the interval cannot separate 0.5 from 0.85. Getting the interval half-width to about ±0.15 at 0.7 needs about 30–35 seeds per code; at n=30, 21/30 gives 0.52–0.83.

Cheaper options:
- Pool PV+RD (20 seeds: 14/20 gives 0.48–0.85).
- Make the gate one-sided on the lower Wilson bound (e.g. lower bound ≥ 0.5).
- Pre-register the gate as "observed recall ≥ 0.8".

Whichever is chosen, §6 still describes 20 positives (10 PV, 5 RD, 5 PE) and no negatives. Update it to the v2 counts and add the precision rule.

---

## Minor issues

- **Key location.** `seeds-v2-key.csv` sits next to `seeds-v2.jsonl` in `corpus/seeds/`. C8 asked for a git-ignored path that coders cannot reach. Move the key out of the corpus tree entirely, and give coders only the merged pool.
- **Source URLs.** `modelled_on` for `J542182:0`, `S578365:0` and `S835567:0` reads "(not sourced)". §6 requires seeds modelled on documented practice. Source them or note the exception.
- **Analogue domains.** Every analogue comes from SRE or clinical alert fatigue, so PV seeds lean on the error budget and overrides. Add one or two from other documented domains, e.g. bank credit-limit reviews and SOX deficiency remediation.
- **Second codes in negatives.** `S467188:0` has performer "both" and the speaker approves the agent's queue. That is fine as OT, but the key should state that AO is not a second code.
- **Missing PV+PE second code.** `S383051:0` and `F…7164` are clean PE. No seed tests the PV+PE double-code case, e.g. finding a gap and then changing the rule.
- **Filing performer.** The AO and PE filing seeds are "person". Real extraction often gives "both" when an agent is in the clause.
