# Personal and unsanctioned AI at work: what our corpus says (Part B, descriptive)

11 October 2026. Search of posting duty statements, speech spans and filing passages already in the corpus; no new collection. Script: `corpus_search.py` (search), `corpus_code.py` (coding, quote check, tables), `corpus_report.py` (this file). Hits: `corpus-hits.csv`.

## Filings and postings mention the problem mostly as a risk or a duty to use approved tools; practitioners barely mention it

Of 101 kept hits, 72 are posting duty statements (62 postings, 41 employers), 25 are filing passages (17 companies) and 4 are speech passages. Postings that name a control (discover, monitor, block, approve) are concentrated in security roles; filings mostly state the risk of employees using unapproved tools without naming a control; the speech corpus has only two spans on the topic.

## Method

- Sources: `postings-haiku-all.tasks.jsonl` duty spans (25,220 postings with spans, joined to `postings-input.jsonl` group and the load_postings table for employer, title and function via `function_map.py`); `consensus-dedup.jsonl` (862 speech spans); `filings-input-v3.jsonl` (2,216 passages). For speech I also searched the surrounding paragraph text (`speech-input.jsonl`, 189 chunks) and the untimestamped paragraphs (`speech-input-notime.jsonl`, 42) as supplementary sources, because spans are short extracts.
- Search: case-insensitive regular expressions, one per term, in `corpus_search.py` (the term list is the dictionary `TERMS`). Terms that are ambiguous alone (shadow IT, unauthorized, acceptable use, AI tool approval/intake, browser extensions, data leakage, DLP) require an AI or tool word within 80 characters. Each term counts once per span or passage.
- Reading: every hit in speech was read. For postings, hits on the broad terms (approved tools, public AI tools, approval/intake, ChatGPT, DLP, data leakage) were read only if the span contains an AI word; hits on the narrow terms (shadow, unsanctioned, unapproved, unauthorized, personal, BYOD, acceptable use, policy) were all read. For filings, hits were read if the passage contains an AI word and an employee or user word (employee, workforce, personnel, staff, personal, user, shadow, unapproved, internal use and similar); the other filing hits (about 150 passages) are generic cybersecurity or product text with no employee reference and were not coded.
- Kept: text about employees' (or staff's) use of AI tools or agents outside sanctioned channels, or a control or sanction route for that use. Excluded: security vendors describing products to customers (Zscaler, Palo Alto Networks, AvePoint, Netskope; 'shadow AI' appears in their product text), AI security of products and agents built for customers, general AI governance duties, and BYOD or personal-computer mentions with no AI context (for example Comcast 'activating BYOD to the network').
- Coding: who = the function the text assigns the response to (security, IT, legal/compliance, data/AI, business, HR, not stated); for postings it is the role that owns the duty. Response = discover, block, approve/sanction, monitor, train, policy, or 'none stated (risk only)' for filing risk statements that name no response. Function: postings by `function_map.py` (title rules then O*NET, with its stated error); filings by SIC description; speech by the recording's function tag. A posting duty to 'use approved AI tools' is coded approve and flagged tier 'approved-tool duty'; everything else is tier 'control or unsanctioned use'.
- Weights: rest20 postings carry sampling weight 5. Counts below are unweighted spans unless a 'weighted' column says otherwise.
- Quotes are 40 words or fewer, checked by script as substrings of the source text (whitespace normalised; speech timestamps removed). No personal names or emails appear in the quotes; speech is cited by recording id.

## Raw hits per source and term (before reading)

|  | posting spans | filing passages | speech spans | speech paragraphs | speech untimestamped paragraphs |
|---|---|---|---|---|---|
| AI tool approval/intake | 59 | 16 | 1 | 1 | 0 |
| AI usage policy | 24 | 4 | 0 | 0 | 0 |
| BYOD | 16 | 1 | 0 | 0 | 0 |
| ChatGPT (usage policy) | 30 | 7 | 1 | 10 | 2 |
| DLP (AI) | 43 | 13 | 0 | 0 | 0 |
| acceptable use (AI) | 1 | 1 | 0 | 0 | 0 |
| approved tools / AI tools | 108 | 19 | 0 | 1 | 0 |
| bring your own | 0 | 5 | 0 | 0 | 0 |
| browser extension(s) (AI) | 1 | 6 | 0 | 0 | 0 |
| consumer AI | 0 | 1 | 0 | 0 | 0 |
| data leakage (AI/prompts) | 55 | 63 | 0 | 1 | 0 |
| personal account(s) | 8 | 0 | 0 | 0 | 0 |
| personal device(s) | 4 | 6 | 0 | 1 | 0 |
| public AI tools | 51 | 154 | 0 | 1 | 0 |
| sanctioned AI | 7 | 5 | 0 | 0 | 0 |
| shadow AI | 7 | 4 | 0 | 0 | 0 |
| shadow IT (AI context) | 1 | 1 | 0 | 0 | 0 |
| unapproved | 3 | 5 | 0 | 0 | 0 |
| unauthorized (AI/tools) | 14 | 75 | 0 | 0 | 0 |
| unsanctioned | 2 | 5 | 0 | 0 | 0 |
| TOTAL | 434 | 391 | 2 | 15 | 2 |

Most raw hits are not about personal AI use. 'public AI tools' hits are mostly 'third-party AI' or 'external AI' in product text, and the postings' 'approved tools' hits are mostly about integrating with approved systems. 'personal account(s)' in postings is 'personal accountability'.

## Kept hits by source and response

| response | filing | posting | speech (paragraph) | speech (span) | speech (untimestamped) | total |
|---|---|---|---|---|---|---|
| approve | 3 | 44 | 0 | 1 | 1 | 49 |
| block | 1 | 2 | 0 | 0 | 0 | 3 |
| discover | 0 | 4 | 0 | 0 | 0 | 4 |
| monitor | 0 | 8 | 0 | 0 | 0 | 8 |
| none stated (risk only) | 13 | 0 | 0 | 0 | 0 | 13 |
| policy | 7 | 10 | 2 | 0 | 0 | 19 |
| train | 1 | 4 | 0 | 0 | 0 | 5 |
| total | 25 | 72 | 2 | 1 | 1 | 101 |

Speech: M065, M052 and M081 are timestamped; M067 is untimestamped and shown separately. M041, M053 and M054 gave no relevant hits. M052 and M081 come from the paragraph text, not from extracted spans.

## Postings: roles that carry the duty

| function | spans | weighted | approved-tool duty | control or unsanctioned use |
|---|---|---|---|---|
| security | 23 | 27 | 1 | 22 |
| IT and infrastructure | 12 | 24 | 7 | 5 |
| manufacturing/field | 7 | 35 | 6 | 1 |
| software engineering | 7 | 15 | 5 | 2 |
| executive/strategy | 5 | 13 | 4 | 1 |
| finance and accounting | 5 | 17 | 3 | 2 |
| data and AI/ML | 3 | 11 | 3 | 0 |
| marketing | 3 | 15 | 3 | 0 |
| customer service/support | 2 | 2 | 2 | 0 |
| operations and supply chain | 2 | 2 | 1 | 1 |
| other | 2 | 6 | 2 | 0 |
| legal and compliance | 1 | 1 | 1 | 0 |
| total | 72 | 168 | 38 | 34 |

Security roles hold 22 of the 34 control spans in postings. Outside security, the typical duty is simply to use approved AI tools (38 spans, mostly software, manufacturing, IT and finance roles at a few employers such as Micron, Amgen and Visa).

## Postings and filings: who and response

| who | filing | posting | total |
|---|---|---|---|
| IT | 0 | 9 | 9 |
| business | 0 | 1 | 1 |
| data/AI | 0 | 2 | 2 |
| not stated | 24 | 39 | 63 |
| security | 1 | 21 | 22 |
| total | 25 | 72 | 97 |

Postings, response by tier:

| response | approved-tool duty | control or unsanctioned use | total |
|---|---|---|---|
| approve | 34 | 10 | 44 |
| block | 0 | 2 | 2 |
| discover | 0 | 4 | 4 |
| monitor | 0 | 8 | 8 |
| policy | 2 | 8 | 10 |
| train | 2 | 2 | 4 |
| total | 38 | 34 | 72 |

Postings: weighted spans are 168 (42 control, 126 approved-tool duty).

## Filings: industries

| function | passages |
|---|---|
| Services-Prepackaged Software | 9 |
| Finance Services | 4 |
| Computer Storage Devices | 2 |
| Pharmaceutical Preparations | 2 |
| Computer Peripheral Equipment, NEC | 1 |
| Crude Petroleum & Natural Gas | 1 |
| Retail-Department Stores | 1 |
| Retail-Retail Stores, NEC | 1 |
| Services-Business Services, NEC | 1 |
| Services-Engineering, Accounting, Research, Management | 1 |
| Services-Help Supply Services | 1 |
| Telephone Communications (No Radiotelephone) | 1 |

Thirteen of 25 filing passages state the risk without a response; the rest name a policy (7), an approval route (3), a prohibition (1) or training (1). No filing passage mentions monitoring other than Arcturus's data-exfiltration detection, which sits in the same passage coded 'approve'.

## Examples

Verbatim, 40 words or fewer, checked by script.

1. [posting, security, AlphaSense; who: security; response: discover] "Continuously monitor CASB/SWG, OAuth, and endpoint telemetry to discover unsanctioned AI tools, browser extensions, and API-level agents in use across the business."
2. [posting, IT and infrastructure, OneTrust; who: IT; response: discover] "discover unsanctioned models, applications, and agents"
3. [posting, security, CDW; who: security; response: approve] "Design and mature the process, criteria, and risk tiers used to approve, restrict, monitor, or block AI use cases, platforms, vendors, and shadow AI."
4. [filing, Services-Business Services, NEC, Rimini Street, Inc.; who: not stated; response: block] "Further, while we prohibit the use of artificial intelligence (AI) technologies by our employees unless incorporated into one of our product or service offerings or approved in accordance with internal policies, incorporating AI technologies, including agentic AI technologies, in our"
5. [filing, Services-Prepackaged Software, JFrog Ltd; who: not stated; response: policy] "identified risks relating to our employees’ use of generative AI, but personnel may unknowingly or otherwise inappropriately enter proprietary or sensitive information, data, or code into AI tools, may use tools making use of AI agents or other types of"
6. [filing, Pharmaceutical Preparations, Arcturus Therapeutics Holdings Inc.; who: security; response: approve] "We have adopted certain enterprise AI platforms, which our employees may access following internal review and approval processes."
7. [speech, engineering and platform; who: not stated; response: approve] "I had to modify a bit our compliance approval process for new tools"
8. [speech-text, risk and compliance; who: security; response: policy] "They're allowed to use AI for the calls they get, for a knowledge center to answer questions and to review their performance on a call."

## Limits

- Postings state what a role does, not what a company practises, so a duty to 'discover unsanctioned AI tools' shows that the function exists in the hiring plan, not how common unsanctioned use is. Filings are risk disclosures; the same company text repeats across filings (JFrog three passages, Tenable five, Upstart three), and each passage is counted once.
- Speech has almost no coverage: the interview sample is about AI adoption and the extractor kept task spans, so the topic appears in only four passages.
- The filings prefilter and the AI-word prefilter for postings are judgement filters; recall of the terms outside them was not checked beyond the raw table. Function labels inherit the function map's O*NET error.
- The 'approved-tool duty' tier is a wide reading of 'controls on use'; the 'control or unsanctioned use' tier is the narrower one.

## Opus review adjustments (11 October 2026)

`review.md`: drop Pacific Life #0, Cencora #22, Abbott #67 and Tenable #90 (product text); recode Upstart #86 as risk only; Arcturus #77 and M052 #99 are not security. Wrongly dropped and to add as risk statements: Freshworks #625, Tenable #746, IDT #603, Sprinklr #631, Rubrik #827; speech M064 #444 (personal laptop vs corporate level). Security concentration after fixes: about 19 of 31 control duties, at 14 employers (three supply 10). The 25 filing passages hold about 15 distinct texts. The report uses the adjusted figures.
