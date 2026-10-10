# Passage codes: independent check of the automated coding

Sample: the 40 passages in `corpus/b-raw/review/passages-sample-consensus.jsonl`, with 8 codes each (320 decisions).
Codebook: `loop-prompts/filing-codes.md`, applied strictly.
I coded every passage from `source_text` alone, saved the codes, and only then opened the automated values.
Row-level detail is in `passage-codes-check.csv`. Where the two codings differ, the `note` column gives the reason.

Overall agreement is 310 of 320 decisions (96.9%). All 10 disagreements are borderline readings of the codebook rather than clear misreadings.

## Precision and recall

"Mine" here means the reference coding. Precision = TP / automated yes. Recall = TP / my yes.
Wilson 95% intervals are given where the denominator is 5 or more.

| Code | Automated yes | My yes | TP | Precision (95% CI) | Recall (95% CI) | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| own_use | 21 | 17 | 16 | 0.76 [0.55, 0.89] | 0.94 [0.73, 0.99] | Fit for use (precision is the weak side) |
| product | 26 | 26 | 26 | 1.00 [0.87, 1.00] | 1.00 [0.87, 1.00] | Fit for use |
| reorg | 4 | 4 | 4 | 1.00 (n=4) | 1.00 (n=4) | Too few positives to judge |
| body | 3 | 4 | 3 | 1.00 (n=3) | 0.75 (n=4) | Too few positives to judge |
| metric | 4 | 5 | 4 | 1.00 (n=4) | 0.80 [0.38, 0.96] | Too few positives to judge |
| controls | 9 | 8 | 8 | 0.89 [0.56, 0.98] | 1.00 [0.68, 1.00] | Fit for use |
| workforce | 4 | 3 | 3 | 0.75 (n=4) | 1.00 (n=3) | Too few positives to judge |
| rule_cited | 3 | 3 | 3 | 1.00 (n=3) | 1.00 (n=3) | Too few positives to judge |

Verdict rule: a code is fit for use when precision and recall are both at least 0.7 and both the automated and the reference coding have at least 5 positives. For metric, my coding has 5 positives but the automated coding has only 4, so its precision rests on 4 cases. I have treated it as too few to judge.

The intervals are wide even for the codes that pass. The lower bounds for own_use precision (0.55) and controls precision (0.56) are both under 0.7. "Fit for use" therefore means the point estimates clear the bar. It does not mean the sample proves they do.

## Main error patterns

1. **own_use is too generous: "uses AI" gets read as "uses agents".** This accounts for 5 false positives. The automated coder says yes when a company says it uses AI internally, even though no agents or automation are named:
   - Workday 0001327811-25-000198_2 and 0001327811-26-000026_3: "we are increasingly using AI products and technologies in the course of running our business".
   - DoorDash 0001792789-26-000050_0: AI "in support of internal business operations". Here agents appear only as consumer-side technology.
   - Nutanix 0001193125-26-394793_10: "use of generative AI by our workforce", in risk-factor framing.
   - Cloudflare 0001477333-26-000054_0 (MD&A): a "plan ... to accelerate our evolution to an agentic AI-first operating model". This is a plan and a workforce cut, with no stated use of agents. The companion risk-factor passage (_4) does state that AI and automation tools are in use, and both codings mark that one yes.
   If the study's construct is "AI in own operations" rather than "agents", these become correct. The codebook wording ("agents or automation") should settle this one way or the other.
2. **own_use is missed when the operation is also the product.** Rapid7 0001560327-26-000008_0 describes agentic AI "developed and tested in our managed SOC", a service Rapid7 runs itself. The automated coder saw only `product`. The same passage gave the metric miss: AI triage "reduces false positives by up to 99.93%". That measure belongs to the company's own MDR operation, though it reads like marketing (borderline).
3. **Generic principles counted as controls.** Intuit 0000896878-26-000014_0: "adhere to responsible AI principles" and "ensuring the customer remains in control" describe no specific practice. This is the only controls false positive.
4. **Avoided hiring counted as workforce change.** Asure 0000884144-23-000012_0 says RPA bots let the company "scale the business without ... hir[ing] additional staff". No headcount change is reported, and RPA is not AI.
5. **Chief AI Officer not coded as body.** Recursion 0001601830-26-000098_0: "Hoifung Poon, Ph.D., appointed Chief AI Officer". The codebook names a CAIO as an example of a body. The passage does not spell out oversight duties, so this is borderline. It is the only body disagreement.

There were no disagreements on product, reorg or rule_cited.

## Caveats

- Only one reviewer coded the sample, and several disagreements sit on genuine ambiguities in the codebook (AI vs agents, CAIO without a stated remit, the 99.93% claim). A second human pass on the 10 disagreeing rows would firm up the own_use precision figure.
- The sample has 4 or fewer positives for reorg, body, workforce and rule_cited. Judging those codes needs a positive-enriched sample, such as passages pre-screened by keyword.
- Rubrik's two passages (_6 and _8) are near-duplicates, so they count twice in own_use, product, body and controls.
