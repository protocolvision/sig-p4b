# Extraction check: SEC filings sample

Source: `corpus/b-raw/review/filings-sample.jsonl` (25 passages, 220 extracted items). Item-level judgements are in `extraction-check-filings.csv`.

## Numbers

| Measure | Value | Basis |
|---|---|---|
| Precision (verbatim AND activity) | **0.39** | 86 / 220 |
| Performer accuracy | **0.92** | 203 / 220 |
| Estimated recall | **0.97** | 86 / (86 + 3 missed) |
| Verbatim rate | 0.98 | 216 / 220 |

Rule used for borderline cases: a product capability sold to customers ("the platform orchestrates…", "customers can…") is a feature description, not an activity. Software the company runs on its own operations counts as an activity (VIDA's internal agents, GBTG's internal AI, SS&C's agents "running live within SS&C"), and so do managed services the company performs (Zscaler MDR, XBP transaction processing). If every product feature were counted as an activity, precision would still be only about 0.69 (152 / 220).

Recall is an estimate and probably too high. The extractor over-collects, so very little is left out. The only misses were accounting steps (IBM segment allocation) and one incorporation date (Avalon).

## Most common errors

1. **Product feature descriptions extracted as activities (66 items).**
   - "The C3 AI orchestrator coordinates multiple AI agents, invokes specialized machine-learning models or mathematical tools as necessary and handles all data types and tasks" (C3.ai)
   - "Enables secure access to cloud and on-premises applications from any device with a single entry of their user credentials" (Okta)
2. **Things done by markets, competitors, customers or regulators (29 items).** These come mostly from risk-factor and industry-overview sections.
   - "traditional and non-traditional competitors use other, new data sources and technologies, including generative AI, to derive similar insights" (American Express)
   - "enterprises continue to migrate increasing numbers of applications and services to either private clouds or public clouds offered by third parties" (Extreme Networks)
3. **Strategy postures, goals and forecasts presented as activities (17 items of posture or goal, plus 15 forecasts or intentions).**
   - "We expect to continue to invest heavily in generative AI" (C3.ai)
   - "remain committed to organic initiatives and a programmatic approach to growth through tuck-in acquisitions and divestitures" (OpenText)

Smaller issues:
- 5 items are boilerplate or definitions, for example "We compensate for this limitation by providing specific information…".
- 4 items are not verbatim: one has an inserted "...", two have curly quotes changed to straight ones, and one has a changed capital letter.
- There are truncated fragments such as "By managing access at the user level, it allows".
- Performer errors are rare. They are mostly company development work labelled "software or agent" (Avalon) and acquired service businesses labelled software (Visa's Prisma and Newpay).

## Verdict

**The extraction is not fit for clustering activities.** Recall (0.97) is above the 0.7 threshold, but precision (0.39) is far below it. Clusters would be dominated by product-marketing language and market trends rather than what companies actually do.

## Prompt fix

Replace the instruction with:

> List every activity that THIS company, its employees, or software it runs on its own operations has actually performed, is performing, has started or has stopped, as stated in the passage. Copy each one exactly, character for character (keep quotes, capitals and punctuation; never use "..."), one complete clause per item.
>
> Do NOT include:
> - what a product or platform can do, is designed to do, or enables customers to do ("X enables…", "customers can…", "allows organizations to…"), unless the passage says the company itself runs it on its own operations or delivers it as a service it performs;
> - actions by customers, partners, competitors, regulators, acquired companies before the acquisition, or "the market";
> - forecasts, intentions and plans ("expect", "intend", "plan", "will", "potential", "may", "could");
> - goals, priorities or commitments ("focused on", "committed to", "our strategy is");
> - risk statements, accounting definitions, and non-GAAP or legal boilerplate.
>
> Before you output an item, check that the grammatical subject is the company (we, the Company, a named subsidiary), its people, or its internal systems, and that the verb describes something done rather than something possible. If none qualify, return [].

Add two or three negative examples from this sample (a C3.ai feature line, an American Express risk line, an OpenText priority line) as few-shot "do not extract" cases. Then rerun this check on a new sample.
