# Citation audit: findings.md (phase 5)

Independent check of 10 randomly drawn corpus citations in `results/rerun-2026-10-10/findings.md` (as on disk 2026-10-10 21:24), and of the same items in `report/who-owns-the-rules.html` (report-data JSON). Source text was taken from raw folders only: `sources-v2/transcripts/` (with dates from `sources-v2/media-current.csv`), `corpus/text/`, `corpus/b-raw/postings/`. Counts were recomputed from the stored passage files in `corpus/b-raw/extract/`, which is a derived folder, used here only to recount a figure.

## Sampling frame and draw

I listed 33 corpus-pointing citations in findings.md, sorted them, and drew 10 with `random.Random(20261010).sample(sorted_list, 10)`.

Frame (sorted): F-body; F-content; F-item9A; F-share-all; F-share-frame; I3-#12 (Merck); I3-#19 (JLL); I3-#3a (IQVIA reporting line); I3-#3b (IQVIA "governance committee seat"); I3-counts (27/30, 13/21, 41/60, 57/60); I4-C9b1da45a; I4-CO-SB26-189-act; I4-Cef3dde3f; I4-counts (111/19/32/15); I4-omnibus (Reg 2026/1744 dates); I5-agentforce-spec (2025-03-03); I5-aigp (2024-03-05); I5-ms-entra-owners; I5-relabel-einstein (2024-09-12); I5-relabel-gemini (2025-10-09); I5-servicenow (2025-03-12); I5-tooling (2023-08-15); M010; M016; M021; M024; M065a (compliance approval); M065b (AI guild); M072 (20% quote); M072_c07:1 (RD replaced); R0397; REQ-47040 (24 of 53); speech-first (2024-11-28).

Draw, in draw order: M010; I4-omnibus; I5-tooling; M024; F-content; M016; M065a; I3-#3b; I4-C9b1da45a; I4-Cef3dde3f.

## Results

| id | claim in findings.md | source path | verbatim? | date? | fair? | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M010 | F7: speaker describes a central body: "I'm on the AI Governance Council and we've just had our second meeting." (2025-07-22) | sources-v2/transcripts/M010.txt [00:34:24]; media-current.csv | yes | yes (2025-07-22) | yes | **pass** | The council is mentioned while discussing a Copilot pilot, not agents. That matches F7's own limit: no body is shown to decide agent rules, and none is agent-specific. |
| I4-omnibus | F4: Reg 2026/1744 moves Annex III high-risk obligations to 2 Dec 2027, "and others" to 2 Aug 2028 | corpus/text/C8b5bc20b.txt (amended Art 113(c)) | n/a (paraphrase) | yes (signed 8 Jul 2026; 2 Dec 2027 and 2 Aug 2028 confirmed) | mostly | **pass** | "Others" is loose. The 2 Aug 2028 date covers Annex I (Art 6(1)) high-risk systems, not all other obligations. Art 26(2) is in Ch. III §3, so the Annex III move does apply to it. Suggest "Annex I systems to 2 August 2028". |
| I5-tooling | F6: open agent tooling, third-earliest 2023-08-15 | none in the corpus. Only the derived `instruments/I5-community-tooling.csv` (AgentOps, "GitHub API created_at") | n/a | **cannot verify** | partly | **fail** | No raw copy of the GitHub API response or repo page exists in corpus/text or b-raw, so the id does not resolve to a stored source. `instruments/I5.md` still says the tooling CSV "is absent", which contradicts I5c.md. Two of the three counted repos show licence "NOASSERTION", which fails A.2's OSI-licence rule. F6 does disclose that licences were not checked. On the lenient reading the date would be 2023-01-31. |
| M024 | F7: one of 5 speakers describing "a central body between functions", listed under "AI governance councils, guilds or centres of excellence": "we have a strat and gov team that sit in the middle" (2025-06-30) | sources-v2/transcripts/M024.txt [00:05:59]; media-current.csv | yes ("So we have…") | yes (2025-06-30) | **no** | **fail** | The context is how a CIDO organised the digital/IT organisation into four groups, with "the processes and the tools and the governance and the strategy" team in the middle. It is a general IT strategy-and-governance team inside one function, not an AI governance body. Nothing nearby ties it to AI or agents. As an example of an AI council or guild it overstates. Drop it or relabel it as a central IT governance team. |
| F-content | F5: 2,216 passages; product 1,342, own use 369, controls 109; vendors supply 64% | corpus/b-raw/extract/passages-consensus.jsonl + filings-input-v3.jsonl (recount) | n/a | n/a | mostly | **pass** | Recount matches exactly: 2,216; 1,342 / 369 / 109; vendor 1,428 of 2,216 = 64.4%, with the SIC rule re-applied. Caveat: 903 of the 2,216 passages (41%) come from 10-Qs, but F5 is framed around 10-Ks. Among 10-K passages only, the vendor share is 60.3% (792 of 1,313). |
| M016 | F1: the one PV span is about a budget overrun: "I have a couple of associates … that have exceeded their replic budget in only two weeks" (2026-07-27) | sources-v2/transcripts/M016.txt [00:22:17–00:22:24]; media-current.csv | yes (ellipsis drops "our employees, we call them associates,") | yes (2026-07-27) | yes | **pass** | "replic" is the transcript's rendering of "Replit" (the next turn says Replit), so it is quoted faithfully. Calling it "about a budget overrun" is accurate, and it shows how thin the PV evidence is. |
| M065a | F1: nearest case to a cross-function rule change: "I had to modify a bit our compliance approval process for new tools" (2025-10-28) | sources-v2/transcripts/M065.txt [00:36:38–00:36:43]; media-current.csv | yes | yes (2025-10-28) | yes | **pass** | In context, an engineering leader fast-tracked compliance approval of new AI tools. It is about tool approval, not agent rules, so "nearest case" is a fair label. |
| I3-#3b | F7: IQVIA lists a "governance committee seat" among an AI security architect's duties | corpus/b-raw/postings/workday-iqvia.jsonl, R1549373 (posted 2026-06-18) | **no** | yes (2026 snapshot) | yes | **fail** | The quoted phrase does not occur in the posting. It is the I3 table's paraphrase, put in quotation marks. The posting says: "Represent Security Architecture in IQVIA's existing AI governance committees and taskforces" and "IQVIA has existing AI governance committees and taskforces in place." The substance holds (and is stronger), but the quote is not verbatim. |
| I4-C9b1da45a | F4: EU AI Act Art 26(2): "Deployers shall assign human oversight to natural persons who have the necessary competence, training and authority" | corpus/text/C9b1da45a.txt (Reg 2024/1689) | yes (sentence continues ", as well as the necessary support") | yes (2024 act; report says 2024) | yes | **pass** | It sits under "Obligations of deployers of high-risk AI systems". It is about oversight, not change ownership, as F4 says. |
| I4-Cef3dde3f | F4: PRA SS5/18 (guidance): "each algorithm to have assigned owners, who are accountable for the algorithm's use and performance" | corpus/text/Cef3dde3f.txt §3.3(a) | yes | yes (June 2018; report says 2018) | yes | **pass** | It sits in §3 "Algorithm approval process", which covers "customisation of, or amendment to, existing algorithms". Counting it as a change owner and labelling it guidance (a supervisory statement) are both correct. |

## Drift between findings.md and the report (report-data JSON)

- **M010.** Report sources table: 2025-07-22, used for "archetypes (council)". No drift.
- **I4-omnibus.** The timeline item "Dec 2027: scheduled: EU AI Act high-risk duties apply" drops that only Annex III systems move to that date (Annex I moves to Aug 2028). Minor simplification.
- **I5-tooling.** The report timeline says "the third-earliest open agent **framework** in August 2023". The three counted repos (Phoenix, Langfuse, AgentOps) are observability and monitoring tools, not agent frameworks. This is drift from findings.md's "open agent tooling". The year offsets (0.6, 1.55, 2.2, 3.4, 4.3; now 3.15) recompute correctly from 2023-08-15.
- **M024.** Not in the report. No drift, but the fairness problem stays in findings.md.
- **F-content.** The report says "Agent language in 10-Ks rose … to 6.75% in 2026; vendors supply 64% of the passages". The 64% includes 10-Q passages, so attaching it to 10-Ks is imprecise (10-K only: 60.3%).
- **M016 and M065a.** Not quoted in the report. No drift.
- **I3-#3b.** The report lists I3 #3 (IQVIA, 2026, "archetypes") but does not repeat the "governance committee seat" quote. No drift.
- **C9b1da45a.** The report quote is identical to findings.md and the date (2024) is correct. Related drift: the F4 body in the report says change owners appear in "trading **rules**", where findings.md says "trading texts". The report's caveat does note that 8 of 12 are guidance.
- **Cef3dde3f.** Report: "PRA SS5/18 (guidance)", 2018. No drift.

## Conclusion

7 of 10 drawn citations pass. All five drawn speech and rule-text quotes are verbatim, correctly dated and resolve to stored sources (M010, M016, M065, C9b1da45a, Cef3dde3f), and the filing content counts recompute exactly from the stored consensus file. Three fail:

- **M024 (fairness).** A general IT strategy-and-governance team is presented as an example of an AI governance council or guild.
- **IQVIA I3 #3 (not verbatim).** "Governance committee seat" is an instrument paraphrase in quotation marks. The posting's real wording supports the claim and should replace it.
- **The 2023-08-15 open-tooling date (does not resolve).** Its only support is a derived CSV citing the GitHub API, with no stored raw source, and it is contradicted by stale text in `I5.md`.

Lesser issues to fix:
- the Omnibus "others" wording;
- the 10-Q share hidden inside F5's 10-K framing (64.4% vendor overall, 60.3% for 10-Ks only);
- report drift: "framework" for tooling, "trading rules" for trading texts, and 64% attached to 10-Ks.

With a 3-in-10 failure rate (Wilson 95% about 11–60%), a full pass over the remaining quotes in findings.md is warranted before publication. The failures look like paraphrase and labelling errors rather than fabricated sources.

## Full pass (remaining 23)

Same method as the sample: each id was resolved to a stored raw source (`sources-v2/transcripts/` with dates from `media-current.csv`; `corpus/text/`; `corpus/b-raw/postings/`, `filings/`, `vendor/`), and the quote, date and use were checked against it. Counts were recomputed from these files:
- `corpus-b/filings-denominator.csv` and `filings-index.csv`;
- `corpus/b-raw/filings/` (Item 9A re-parse with the pipeline's own heading regex);
- `coding/speech-*.csv`;
- `clusters/leaf/assignments.csv.gz`;
- the I3 and I4 tables.

Derived files (`instruments/*`, `I5-browser-pass.csv`) were used only to see where a date came from, never as support.

| id | claim in findings.md | source path | verbatim? | date? | fair? | verdict | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-share-all | F5: 10-K filers using an agent phrase, 0.05/0.06/0.12/1.71/6.75% (2022–26) | corpus-b/filings-denominator.csv; filings-index.csv | n/a | yes | yes | **pass** | 4/7667, 4/7255, 8/6774, 112/6565, 422/6255 recompute exactly. The index reproduces the 2022–25 numerators exactly; for 2026 it gives 424 CIKs against 422, which is immaterial. |
| F-share-frame | F5: frame employers 0, 0, 0.21, 3.8, 18.0% (77 of 428) | same | n/a | yes | yes | **pass** | 1/470, 18/471, 77/428 recompute. The index gives 77 frame CIKs for 2026, the same as the file. |
| F-body | F7: "body" yes in 9 of 2,216 passages, "from at most 9 of 465 filers (1.9%)" | corpus/b-raw/extract/passages-consensus.jsonl (recount); raw text checked in corpus/b-raw/filings/ (Rubrik, IQVIA, ACCO) | n/a | n/a | **loose** | **pass** | 9 of 2,216 and 465 filers recompute. The 9 passages come from **5** filers: Rubrik 5 (10-K and 10-Qs repeating one sentence), Manhattan Associates, DarioHealth, ACCO and IQVIA. So the exact figure is 5 of 465 (1.1%), not "at most 1.9%". The bound is true but overstates by about 70%. This does not change the F2 verdict (still under 5%). |
| F-item9A | F5: none of 539 10-Ks with a detectable Item 9A uses an agent phrase in that item | corpus/b-raw/filings/*.txt (re-parse) | n/a | n/a | yes | **pass** | Zero phrase hits in any Item 9A section, confirmed. My re-parse finds an Item 9A heading in 529 of 560 10-K and 10-K/A files (539 of 551 per `log.md`). The denominator differs slightly by heuristic, but the nil result holds. |
| I3-#12 | F3: Merck: "Support security architecture reviews and risk assessments for AI systems, AI applications, AI agents, and AI-enabled platforms across the enterprise." | corpus/b-raw/postings/workday-msd.jsonl, R411511 (posted 2026-08-21) | yes | yes (2026) | yes | **pass** | The title is "AI Security Architect - Associate Director". |
| I3-#19 | F3: JLL's role reports to a "Regional Business Governance & Compliance Director", outside security | corpus/b-raw/postings/workday-jll.jsonl, REQ534894 (posted 2026-09-29) | yes | yes | yes | **pass** | The role supports "a financial institution client account" (an outsourced facilities portfolio). The reporting-line quote is exact. |
| I3-#3a | F3: IQVIA's AI Security Architect "reports to the Security Architecture leader" | corpus/b-raw/postings/workday-iqvia.jsonl, R1549373 (2026-06-18) | yes | yes | yes | **pass** | The source reads "…function and reports to the Security Architecture leader responsible for IQVIA's enterprise AI security direction". |
| I3-counts | DevOps question and archetype 3: 27 of 30 ask for AI-specific experience; 13 of 21 name AI or ML teams; period DevOps postings asked for operations (41 of 60) and programming (57 of 60) experience | instruments/I3.md and I3-tables.csv (coded reading of raw postings and corpus/b-raw/history/) | n/a | n/a | **mostly** | **pass** | All four counts reconcile with the I3 rows: 30 − 3 "no" (#7, #22, #24) = 27; 21 named teams; 25 + 16 = 41; 33 + 24 = 57. Two framing issues. (1) 27 includes 4 "preferred or optional"; only 23 require it. (2) "Period DevOps postings" are 60 operations and systems-engineering postings, of which only 26 carry a DevOps-style compound title. |
| I4-CO-SB26-189-act | F4: effective 1 January 2027: "individual designated by the deployer who has authority to approve, modify, or override a consequential decision" | corpus/text/CO-SB26-189-act.txt (6-1-1701(15); Section 5) | yes (statute in capitals) | yes ("this act takes effect January 1, 2027") | **mostly** | **pass** | The quote is the definition of "meaningful human review". The operative duty (6-1-1704) is to give, **on the consumer's request** after an adverse outcome, "an opportunity for meaningful human review … to the extent commercially reasonable". F4's quote is fair. Archetype 4's "require deployers … to name trained people" overstates it for Colorado. |
| I4-counts | F4: 111 provisions from 19 texts; 32 regulate change; 15 name an owner (12 trading, 3 labs, 0 of 4 AI law); 8 of 12 from guidance (5 FCA, 3 PRA) | instruments/I4-tables.csv (by_family, by_rule, change_owners_named) | n/a | n/a | yes | **pass** | 53+7+37+13+1 = 111; 25+0+4+3 = 32; 12+0+0+3 = 15; 19 by_rule rows. The trading owners split RTS 6 ×3, FINRA 16-21 ×1 (binding), PRA ×3 and FCA ×5 (guidance), so 8 of 12 is guidance. Provision coding itself was not re-read against all 19 texts. |
| I5-agentforce-spec | F6: first agent-scoped certification 2025-03-03 (Agentforce Specialist) | corpus/b-raw/vendor/salesforcebreak.txt (24 Feb 2025); sf-ai-specialist-rename.txt (18 Feb 2025) | n/a | yes ("credential will be updated to Agentforce Specialist on March 3, 2025") | yes | **pass** | This is a rename of the AI Specialist credential, not a launch, as I5 records. Both sources were published before the event, so the date is as announced. |
| I5-aigp | F6: AI-governance certification 2024-03-05 (IAPP AIGP) | corpus/b-raw/vendor/iapp-aigp-pr.txt is an **empty fetch** (header only); I5-certifications.csv says "as reported in search summary" | n/a | **cannot verify** (year only: corpus/text/Cd3561f83.txt "Launched in 2024") | yes | **fail** | The id does not resolve to stored text carrying the day. Only the year 2024 is supported by a stored source. The order claim (certification before agent-scoped ones) survives at year level. |
| I5-ms-entra-owners | F6 and archetypes: "Sponsors provide business accountability for agents, making lifecycle decisions without technical administrative access." (2025-11-05) | corpus/b-raw/vendor/ms-entra-owners.txt (fetched 2026-10-10, page last updated 2026-07-21) | yes | **no** (day not stored) | yes | **fail** | The quote is exact on the stored page. 2025-11-05 comes from a GitHub commit recorded only in the derived browser pass, and that note itself says the commit had different wording ("agentic applications"), with the exact sentence first appearing 2025-11-09. The stored `ms-entra-ignite.txt` lists "Agent owners, sponsors, and managers" as new at Ignite 2025, so **November 2025** is supported. |
| I5-relabel-einstein | F6: Einstein Copilot became Agentforce on 2024-09-12 | none stored. The date comes from browser pass B11, a Salesforce newsroom URL not in corpus/text or b-raw/vendor. | n/a | **cannot verify** | yes | **fail** | `I5-relabel.csv` still gives 2024-09-17 (from a search summary), so the instrument files disagree with each other. Either store the 12 Sep 2024 press release or say "September 2024". N24 = yes for both coders is confirmed (`pattern-match/result.md`). |
| I5-relabel-gemini | F6: Agentspace became Gemini Enterprise on 2025-10-09 | corpus/b-raw/vendor/goog-gem-relnotes.txt | yes (release note) | yes ("October 09, 2025 … Google Agentspace is part of Gemini Enterprise") | yes | **pass** | |
| I5-servicenow | F6: vendor agent roles: ServiceNow, 2025-03-12 | corpus/b-raw/vendor/sn-aict-roles.txt is an **empty JS shell**; corpus/text/Ce30904d7 and Cf7d364f5 carry no date and no role wording | n/a | **cannot verify** | **no** | **fail** | 2025-03-12 is the Yokohama release-family GA date, taken from an unstored docs page (browser pass B5). It is not the date the AI Steward or AI Asset Owner roles were defined, as I5.md itself says. These are AI-governance admin roles, not agent roles. Presenting the date as "vendor agent roles: ServiceNow, 2025-03-12" overstates on both counts. |
| M021 | F1: "We changed the guard rails" (2025-09-19; functions not stated) | sources-v2/transcripts/M021.txt [00:04:58–00:05:00]; media-current.csv | yes (drops the stutter "We we") | yes | yes | **pass** | Next: "We allowed new rules to exist, but we also had to tell people what the benefit was". The context is service-desk AI adoption at VOIS. "Nearest case", with functions unstated, is fair. |
| M065b | F7: "we decided to create like an AI guild" (2025-10-28) | sources-v2/transcripts/M065.txt [00:36:09–00:36:13] | yes | yes | **mostly** | **pass** | It sits alongside "a front-end guild … a back-end guild" in an engineering organisation. Its purpose was "to gather like the best practices of each pod" and evangelise. It is a guild, as F7 says, but it is engineering-internal and not a governance body. Counting it among "central bodies between functions" (I6) is generous. |
| M072 | F2: "she spends 20% of her time managing the agents, orchestrating the agents." (2026-01-01) | sources-v2/transcripts/M072.txt [00:12:32–00:12:37]; media-current.csv | yes | yes (2026-01-01, filled in from "unknown" per cleaning-log) | yes | **pass** | The speaker describes his chief AI officer ("chief A officer" in the transcript). |
| M072_c07:1 | F1: before adjudication each coder coded RD on 3 spans; on M072_c07:1 the adjudicator replaced an RD both coders gave | coding/speech-coderA.csv, coderB.csv, adjudicated.csv, final.csv; span text in M072.txt [00:38:18] | yes (span "we decided we would reactivate the folks that sales decide was not worth their time") | n/a | yes | **pass** | A: RD on M021_c00:7, M065_c06:2, M072_c07:1. B: RD on M072_c07:1, M073_c00:11, M073_c01:0. Final M072_c07:1 = AO (adjudicated). The timestamped recount matches exactly: 771 spans, OT 600, AO 150, PE 21, PV 1, RD 0. Pre-adjudication PV+RD is 4 (A) and 9 (B). |
| R0397 | F1: "turn goals into … rules, constraints … that AI systems can execute" (2026) | corpus/b-raw/coding/record-pool-key.json → corpus/b-raw/postings/greenhouse-cribl.jsonl 6214825004 (posted 2026-10-05) | yes (ellipses drop "clear specifications," and "and acceptance criteria"; "reliably" cut at the end) | yes | yes | **pass** | Cribl, "Staff Software Engineer, Agentic Tools". The line reads "Practice intent engineering: …". |
| REQ-47040 | F3: in the holdout half, 24 of cluster 111's 53 tasks come from Thrivent REQ-47040, "Principal Engineer - AI Security"; without it, 29 members and Jaccard 0.432 | corpus/b-raw/postings/workday-thrivent.jsonl (posted 2026-06-03); clusters/leaf/assignments.csv.gz | yes (title) | yes | yes | **pass** | Recomputed exactly: 53 holdout predicted, 24 from REQ-47040; 29 without it; Jaccard 29 vs 34 = 0.4318. Discovery cluster 111 has 35 tasks, 19 postings and 18 employers, also exact. |
| speech-first | F6: the first speech record is 2024-11-28 | media-current.csv; sources-v2/transcripts/M001.txt; coding/speech-final.csv | n/a | yes | yes | **pass** | M001 (2024-11-28) is the earliest of the 34 coded speakers. M002 (2024-04-18) is listed in media-current but has no transcript and was not coded. It also falls after 2024-03-05, so the conclusion is unaffected. |

**Pass count: 19 of 23.** The four failures are all I5 dates that do not resolve to a stored raw source:
- **AIGP 2024-03-05.** Only the year is stored.
- **Entra 2025-11-05.** Only November 2025 is stored, and the derived note puts the exact sentence at 11-09.
- **Einstein to Agentforce 2024-09-12.** Nothing is stored, and the instruments disagree (09-12 against 09-17).
- **ServiceNow 2025-03-12.** Nothing is stored, it is a release-family date, and the roles are not agent roles.

Every speech, posting and rule-text quote in the remaining 23 is verbatim and correctly dated. Every count recomputes exactly or within heuristic noise (Item 9A denominator). The one loose count is F7's filer figure: it is 5 filers, not "at most 9".

**Combined with the sample: 26 of 33 pass.** The 7 failures are:
- M024: fairness;
- IQVIA "governance committee seat": not verbatim;
- 5 vendor or tooling dates without a stored raw source (I5-tooling, AIGP, Entra day, Einstein, ServiceNow).

F6's dated order is the weakest part of findings.md. Of its seven dates, only Agentforce Specialist (2025-03-03), Gemini (2025-10-09) and Colorado (2027-01-01) resolve to stored text. The order itself (tooling, then certification, then vendor roles, then law) survives at year level, except that the tooling year is unsupported (sample result).

### Drift in the report (who-owns-the-rules.html) for these 23

- **Matches findings.md.** R0397 quote (F1), M072 quote and date (F2), Merck quote (F3), the REQ-47040 caveat (24 of 53), the filing shares (0.12% in 2024, 6.75% in 2026) and 1 of 771 (H-speech row).
- **Entra date.** The F5 quote id "ms-entra-owners (2025-11-05)" and sources row "2025-11-05" carry the unsupported day. The timeline's "Nov 2025" is supported.
- **AIGP date.** The timeline "Mar 2024 … IAPP AIGP" (year 0.6) carries the unsupported month. Einstein, Gemini and ServiceNow are not in the report.
- **Phase change row.** It says "at most 1.9% of filers"; the exact figure is 1.1% (5 of 465). The archetypes paragraph says "9 of 2,216 filing passages" (correct) without the 5-filer count.
- **Designated overseer archetype.** "From 2027 the law requires deployers … to name trained people with authority to oversee and override it." This overstates on two points:
  - Colorado only requires, on request and where commercially reasonable, an opportunity for review by a designated individual.
  - The EU duty for Annex III applies from 2 Dec 2027, and for Annex I from 2 Aug 2028.
- **27 of 30.** The patterns prose and the builder archetype say postings "ask for" AI-specific experience (27 of 30), but 4 of the 27 only prefer it.
- **M073 date (outside the 33).** The sources table gives M073 as "2026", but `media-current.csv` has 2025-09-23.

### Corrections (current text → replacement)

**findings.md**
1. F6, dated order: "AI-governance certification: 2024-03-05 (IAPP AIGP);" → "AI-governance certification: 2024 (IAPP AIGP; the stored source gives the year only);". Alternatively, store the IAPP launch release in `corpus/b-raw/vendor/iapp-aigp-pr.txt` (currently an empty fetch) and keep the day.
2. F6, dated order: "vendor agent roles: ServiceNow, 2025-03-12; Microsoft Entra, 2025-11-05;" → "vendor agent roles: Microsoft Entra, November 2025 (listed as new at Ignite 2025);"
3. F6 quote: "(ms-entra-owners, 2025-11-05)" → "(ms-entra-owners; new at Microsoft Ignite, November 2025)".
4. F6 relabel: "Einstein Copilot became Agentforce on 2024-09-12" → "Einstein Copilot became Agentforce in September 2024". Also align `I5-relabel.csv` (2024-09-17) or store the press release.
5. Section 2, "Business sponsor": "(Microsoft Entra, 2025-11-05)" → "(Microsoft Entra, November 2025)".
6. F7 filings: "The "body" code is yes in 9 of 2,216 passages, from at most 9 of 465 filers (1.9%)." → "The "body" code is yes in 9 of 2,216 passages, from 5 of 465 filers (1.1%; one vendor, Rubrik, supplies 5 of the 9)."
7. Verdict table, Phase change: "F2: about 1% of spans, at most 1.9% of filers." → "F2: about 1% of spans, 1.1% of filers (5 of 465)."
8. DevOps question: "27 of 30 of today's AI-titled postings ask for AI-specific experience;" → "27 of 30 of today's AI-titled postings ask for or prefer AI-specific experience (23 require it);"
9. DevOps question: "period DevOps postings asked for both operations experience (41 of 60) and programming experience (57 of 60)." → "period operations and systems-engineering postings (2011–16; 26 of 60 with a DevOps-style title) asked for both operations experience (41 of 60) and programming experience (57 of 60)."
10. Archetype 3: "and ask for AI-specific experience (27 of 30)" → "and ask for or prefer AI-specific experience (27 of 30; 23 require it)".
11. Archetype 4: "Binding law will require deployers of high-risk or consequential-decision AI to name trained people with authority to oversee, override or review outputs: EU AI Act Art 26(2) and Colorado SB26-189." → "Binding law will require deployers of high-risk AI to assign trained people with authority to oversee it (EU AI Act Art 26(2)), and Colorado deployers to offer, on request after an adverse decision and where commercially reasonable, review by a designated individual with authority to override it (SB26-189)."
12. Optional, F7 examples: after "we decided to create like an AI guild" (M065, 2025-10-28), add "(an engineering best-practice guild)".

**report/who-owns-the-rules.html**
1. report-data F5 quote id: "ms-entra-owners (2025-11-05)" → "ms-entra-owners (November 2025)". Sources row ms-entra-owners date: "2025-11-05" → "2025-11".
2. report-data timeline present[0]: "date": "Mar 2024" → "2024". Keep year 0.6, or store the IAPP source and keep Mar 2024.
3. Hypothesis-verdicts script, Phase change row: "About 1% of spans, at most 1.9% of filers; two other features untestable" → "About 1% of spans, 1.1% of filers (5 of 465); two other features untestable".
4. Static archetypes paragraph: "and in 9 of 2,216 filing passages" → "and in 9 of 2,216 filing passages from 5 filers".
5. Static archetype "The designated overseer": "From 2027 the law requires deployers of high-risk or consequential AI to name trained people with authority to oversee and override it." → "From late 2027 the EU AI Act requires deployers of high-risk AI to assign trained people with authority to oversee it, and from 2027 Colorado requires deployers to offer, on request and where commercially reasonable, review by a designated person who can override a consequential decision."
6. Static archetype "The AI or agent builder": "ask for AI-specific experience (27 of 30)" → "ask for or prefer AI-specific experience (27 of 30)". report-data patterns prose: "Postings ask for scarce AI-specific experience (27 of 30)" → "Postings ask for or prefer scarce AI-specific experience (27 of 30)".
7. report-data sources row M073: "date": "2026" → "2025-09-23".
