# Review: signatures-agents.md (fresh fact-check, 2026-10-11)

Scope: every double-quoted string in the timeline table, checked against the stored files that row cites (`corpus/b-raw/signatures/agents/`). Normalisation: whitespace collapsed, curly quotes and dashes made straight, `*` removed, case ignored. Script: `qc.py` in the session scratchpad (not saved to the repo).

## All 50 evidence quotes pass, but the Article 4 quote is superseded text

- 48 of 53 quoted strings match the cited file directly.
- 2 match once a space before a comma is ignored. The source split a link onto its own line, giving "TAU-bench , an agentic" and "SWE-bench , we actually". Pass: `anthropic-claude35-sonnet-upgrade-2024` and `anthropic-building-effective-agents` (lines 35-37 and 194-195).
- 3 strings are search-term labels, not evidence: "ai agent engineer", "agent engineer" and "agentic ai engineer". The first is in no stored file, and the other two appear only in files the row does not cite. They need no source, but they should be set in code font so a later check does not read them as quotes.
- **Substantive problem:** the Art. 4 quote ("shall take measures to ensure, to their best extent, a sufficient level of AI literacy") is in `artai-act-art4.txt`, but the explorer labels it "amended". The current text reads "shall take measures to support the development of AI literacy … This obligation does not require providers or deployers to guarantee any specific [level]". The draft uses the amended text for Art. 26 and the old text for Art. 4. Quote the amended wording.

## Dates: all 15 confirmed, with four wording fixes

| Claim | Stored evidence | Verdict |
| --- | --- | --- |
| ReAct 6 Oct 2022 | arXiv v1 "Thu, 6 Oct 2022" | OK |
| LangChain repo 17 Oct 2022 | API `created_at` 2022-10-17T02:58:36Z, MIT | OK |
| First agents commit 22 Nov 2022 | "(WIP) agents (#171)" 2022-11-22 | **Reword.** "add react chain (#24)" landed 27 Oct 2022 and "mrkl (#42)" 5 Nov 2022. Say "first commit named agents". |
| Adept ACT-1 14 Sep 2022 | "September 14, 2022 — Adept Team" (Wayback) | OK |
| Klarna 27 Feb 2024 | "New York, NY – February 27, 2024" | OK |
| AI Engineer Summit 8-10 Oct 2023 | "October 8 - 10 • San Francisco" | OK. The page also contains a typo, "Sunday, Oct 9"; ignore it. |
| Latent Space 30 Jun 2023 | "Jun 30, 2023" | OK |
| Indeed "llm engineer" 1,578, 15 May 2024 | capture 20240515011130, "1,578 jobs". The exact-URL CDX query returned one capture. | OK. This counts keyword matches, not job titles. |
| SWE-bench 10 Oct 2023 | arXiv v1 "Tue, 10 Oct 2023" | OK |
| Salesforce AI Associate 6 Sep 2023 | Salesforce Ben: "released on the 6th September". The year is inferred from "Published September 07, 2023". | OK, grade R |
| AWS AI Practitioner beta 13 Aug 2024 | blog dated 25 Jun 2024: "beta registration opens August 13, 2024" | **Reword** as "announced to open". The stored August blog does not confirm the opening date. |
| AI Specialist exams from 9 Sep 2024 | Trailhead capture of 15 Aug 2024: "Exam dates start Sept 9". The year comes from the capture date. | OK |
| Agentforce Specialist 3 Mar 2025 | two trade-press pieces, plus a Trailhead capture of 20 Mar 2025 that shows the new name | OK. This is a **rename** of the AI Specialist credential, not a new one. |
| EU Art. 4 applies 2 Feb 2025 | Art. 113(a), amended text: "Chapters I and II shall apply from 2 February 2025" | OK. Use the amended Art. 4 wording. |
| Art. 26 applies 2 Dec 2027 (amended) | Art. 113(c)(i), new text: "2 December 2027 as regards … Annex III". Annex I systems: 2 Aug 2028. | OK. **Add** "Annex III high-risk only" and note the date was moved from 2 Aug 2026. |
| Colorado 1 Jan 2027 | Holland & Knight: "takes effect January 1, 2027". The bill summary has duties "starting January 1, 2027", while the legislature lists the session-law effective date as 05/14/2026. | **Reword** as "obligations apply from 1 Jan 2027". Grade can rise to P/R. |

## Agents reached an agent-named credential about twice as fast

Each gap runs from the date the practice went public. Neither credential below names agents:

| Path | Start | Credential | Years |
| --- | --- | --- | --- |
| DevOps | 23 Jun 2009 | AWS DevOps Engineer, 7 Nov 2014 | 5.4 |
| Data science | 9 Apr 2009 | Cloudera CCP:DS, 28 Mar 2014 | 5.0 (4.0 if the INFORMS CAP exam, Apr 2013, counts; that date is search-only) |

For agents, starting from 6 Oct 2022 (17 Oct 2022 gives the same result to one decimal):

| Agent credential | Date | Years |
| --- | --- | --- |
| AI Associate (AI literacy, not agents) | 6 Sep 2023 | 0.9 |
| AWS AI Practitioner (announced) | 13 Aug 2024 | 1.9 |
| AI Specialist | 9 Sep 2024 | 1.9 |
| **Agentforce Specialist (first agent-named)** | 3 Mar 2025 | **2.4** |
| Microsoft AB-100 | 21 Oct 2025 | 3.0 |

**(a) Most defensible number: 2.4 years.** That is 2.1 to 2.3 times faster than the comparison cases. The 0.9-year figure is not defensible, because the AI Associate is a general AI credential for business users.

**Start dates do not match.** The DevOps and data-science starts are firms showing their practice. The agents start is a research paper and an open library. Measured from a firm milestone, the gap is 2.5 years from Adept (14 Sep 2022) or 1.0 year from Klarna (27 Feb 2024). The "about twice as fast" finding holds either way.

## Binding law arrives in two steps, and none of it names agents

| Duty on deployers | Applies from | Years after Oct 2022 |
| --- | --- | --- |
| EU Art. 4, AI literacy (in force; softened by amendment) | 2 Feb 2025 | 2.3 |
| Colorado SB 189, duties on deployers of covered ADMTs (scheduled) | 1 Jan 2027 | 4.2 |
| EU Art. 26, high-risk deployer duties (scheduled; already postponed once) | 2 Dec 2027 | 5.2 |

**(b) Most defensible number: 4.2 years**, the first substantive deployer duty (Colorado). Art. 4 is binding at 2.3 years but is a literacy duty only. Art. 26 is the date most exposed to slipping again. None of these laws names agents. They reach agent deployments only when the agent makes a consequential decision or a high-risk decision.

"Which neither had" is too strong. `signatures.md` reports no regulation found (NF) for DevOps or data science, which shows only what this search found.

## Suggested wording

The current sentence is not fair on two counts. It counts scheduled law as law the field already "faces", and it states as fact that DevOps and data science had no such law, when the search only failed to find one. Suggested replacement:

> Agent work reached its first agent-named vendor credential (Salesforce's Agentforce Specialist, March 2025) about 2.4 years after the practice went public in October 2022, roughly twice as fast as DevOps (5.4 years) or data science (5.0 years). It also already sits under a general EU duty on deployers (AI literacy, from February 2025), with substantive deployer duties scheduled within four to five years: Colorado from January 2027 and the EU's high-risk rules from December 2027. We found no binding text aimed at DevOps or data-science work over a comparable span. None of these laws names agents.
