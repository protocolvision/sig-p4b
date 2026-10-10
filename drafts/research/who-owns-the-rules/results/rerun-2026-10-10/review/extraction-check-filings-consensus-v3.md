# Extraction check: filings-sample-consensus-v3

Source: `corpus/b-raw/review/filings-sample-consensus-v3.jsonl` (25 passages, 35 extracted items). Item-level judgments are in `extraction-check-filings-consensus-v3.csv`.

## Metrics

| Metric | Value | Basis |
|---|---|---|
| Verbatim | 35/35 = 1.00 | all spans match the source after whitespace normalisation |
| Precision (verbatim AND target) | 14/35 = **0.40** | |
| Performer accuracy | 34/35 = **0.97** | |
| Missed target activities | 13 | in 9 of 25 passages |
| Estimated recall | 14/(14+13) = **0.52** | |

## Main error types

**False positives (21 items)**
1. **Product launches and descriptions** (7). These are what the product does or ships, not how teams work. Examples: JFrog "We released significant enhancements to our platform..."; Varonis "In 2022, we introduced the Varonis Data Security Platform..."; Samsara "expanding offerings on our Connected Operations Platform"; BILL "powering our development of AI agents for SMB payables". CarGurus "We calculate IMV..." describes a customer-facing algorithm, and it is also the only performer error ("agent in own operations").
2. **Business model, revenue and accounting statements** (6). Examples: CrowdStrike "We recognize revenue from our subscriptions ratably..."; Trade Desk "We derive substantially all of our revenue from ongoing MSAs"; Asure "We sell our solutions through both direct and partner models".
3. **Investment and intention statements** (5). Examples: Hamilton Beach "We have invested significant resources in our selling and marketing capabilities"; Broadridge "we continue to make investments in initiatives..."; Trade Desk "we have invested in augmenting the capabilities of our platform".
4. **Excluded categories that were still extracted.** FiscalNote's forbearance agreements are financing. Adobe's segment combination is a corporate reporting change.
5. **Vague or anaphoric spans.** C3.ai "We have done this with our strategic vertical industry partner in oil and gas, Baker Hughes".

**Misses (13)**
- **Team, function and agent activity stated in the third person is skipped**, which is the core of the target. Examples: SelectQuote "Advanced predictive analytics help our dedicated, retention-focused customer care ("CCA") team identify consumers at risk of churn..."; Asure "These bots act as digital workers that make us more efficient and eliminate errors."; Asure "a sales representative, who works to close the sale"; Atlassian "Research and development activities primarily include the development and release of new apps and AI agents..."; Omnicom "multiple agencies and disciplines within Omnicom collaborate in formal client networks".
- **The company using its own platform in R&D is missed.** Examples: Seres "using our reverse translational development platform to prioritize future drug targets"; FiscalNote "overlay that data with our sophisticated in-house AI and data science expertise" (borderline).
- In 3 passages (DigitalOcean, Omnicom, SelectQuote) nothing was extracted, although each contains target activity.

**Judgment calls.** Product release announcements (JFrog) were scored as not-target. Hedged risk wording such as Personalis "Our employees and personnel may use generative AI, agentic AI..." was not counted as a miss. A more lenient reading of release announcements would raise precision to about 0.49. The verdict below does not change.

## Verdict

**Not fit for clustering.** Precision is 0.40 and recall is 0.52, both below the 0.7 threshold. Verbatim fidelity (1.00) and performer labelling (0.97) are fine. The weak point is the target boundary. The extractor treats any sentence with "we" plus a verb as an activity, which pulls in product, revenue and investment statements. It also skips activities whose subject is a named team, a sales representative or a bot, and those are exactly the agent and person-in-operations cases the study needs. Recommended fixes before rerunning:
- Add explicit negative examples for product releases, revenue and accounting, and investment sentences.
- Add positive examples where the subject is a team or role ("our X team...", "bots act as...").
