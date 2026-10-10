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
