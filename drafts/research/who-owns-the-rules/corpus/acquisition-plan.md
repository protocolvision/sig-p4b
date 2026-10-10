# Corpus acquisition plan

Protocols for Business · 10 October 2026 · for the end-to-end rerun ([`../RERUN.md`](../RERUN.md))

## 1. Why a corpus

Every claim in the first round of research rests on search-engine summaries: the cloud environment could
not open a single page. The rerun builds a local corpus first (the files themselves, with extracted text),
then redoes every study from that corpus, so each claim can cite a document and a passage. The corpus is
the research database.

## 2. Structure

| Path | Contents | In git? |
| --- | --- | --- |
| `corpus/manifest.csv` | Every source to acquire: id, category, kind, URL, where it was first cited. Built by `loop-tools/build_manifest.py` from all research files plus `planned.csv` | Yes |
| `corpus/planned.csv` | New sources named in section 4, once their URLs are resolved (columns: category, title, publisher, year, url) | Yes |
| `corpus/index.csv` | One row per source after acquisition: status, bytes, hash, date, final URL, Internet Archive snapshot | Yes |
| `corpus/raw/` | Files as fetched (HTML, PDF) | No: other people's work |
| `corpus/text/` | Extracted text, one file per source id, with a header naming the URL and date | No |
| `corpus/records/` | Records extracted from the text for each study (JSON Lines), with source id and a quote of 40 words or fewer | Yes |

Citations in the rerun use the source id (for example `C039b3999`) plus the snapshot URL, so a reader can
check a claim after a posting disappears.

## 3. Rules for acquisition

1. **Acquire what is already cited first** (`manifest.csv`, 1,224 sources at the time of writing), so
   every existing claim can be checked and regraded P (read in full) or dropped.
2. **Then add new sources by the selection rules below**, never by searching for our hypotheses' words
   (protocol, rules, governance, override) except where a rule says so.
3. **Record every search** used to find a new source in `corpus/search-log.csv` (date, query, engine,
   results kept), so selection can be audited.
4. **Snapshot** every page with `--wayback`; job postings disappear within weeks.
5. **Sources that need a browser** (status `needs-browser`): open them in the browser, save the main text
   to `corpus/text/<id>.txt` with the same header, and set the status to `ok-browser` in `index.csv`.
6. **Don't commit** raw files or full text. Commit `index.csv`, `planned.csv`, `search-log.csv` and
   `records/`.

## 4. New sources to add

### 4.1 Research reports (category `research-report`)

Acquire the latest edition of each, and the previous edition where it exists, as PDF:

- IAPP and Credo AI, *AI Governance Profession Report* (2025, and any 2026 edition); IAPP *Organizational
  Digital Governance Report* (2024, 2025); IAPP *Salary and Jobs Report* (2025–26).
- World Economic Forum, *Future of Jobs Report 2025*.
- Microsoft, *Work Trend Index* (2025 and 2026 annual reports).
- Anthropic, *Economic Index* reports (September 2025, January 2026, and later).
- Stanford HAI, *AI Index Report* (2025, 2026).
- Indeed Hiring Lab: AI at Work (2025) and posting analyses on AI terms in job ads (2025–26).
- LinkedIn Economic Graph: Work Change Report and AI talent reports (2025–26).
- Lightcast and Revelio Labs: public reports on AI-related postings and task pruning (2025–26).
- OECD, *Employment Outlook* chapters on AI (2023–2025).
- Atalay, Phongthiengtham, Sotelo and Tannenbaum, "The Evolution of Work in the United States" (2020) and
  its public data; Autor et al., "New Frontiers" (2024).

### 4.2 Primary rule texts (category `rule-text`)

- EU AI Act (Regulation 2024/1689), Articles 4, 14, 26 and Annex III; the 2026 AI Omnibus regulation.
- Commission Delegated Regulation 2017/589 (RTS 6); SEC Rule 15c3-5; FINRA Regulatory Notices 15-09 and
  16-21; PRA Supervisory Statement SS5/18; FCA *Algorithmic Trading Compliance in Wholesale Markets* (2018)
  and its 2025 multi-firm review.
- NERC PER-003 and PER-005; FERC Order 693.
- NIST AI Risk Management Framework 1.0 and the Generative AI Profile; ISO/IEC 42001 (purchase or the
  public preview).
- California SB 53; Colorado SB 26-189.
- Visa's rules for agent-initiated transactions (April 2026) and Mastercard Agent Pay requirements;
  Amazon's agent terms (seller agreement, March 2026); Google Play's policy on autonomous agents (2026);
  Microsoft Entra Agent ID documentation on owners and sponsors.
- Anthropic's Responsible Scaling Policy (all versions and the changelog); OpenAI's Preparedness Framework
  v2; Google DeepMind's Frontier Safety Framework v3.

### 4.3 Job postings (category `job-posting`)

Two samples, kept separate (loop v2, strata S1 and S1b):

- **S1, existing occupations.** For each of ten occupations (controller, accounts payable specialist,
  support operations manager, revenue operations manager, procurement specialist, legal operations manager,
  HR operations specialist, identity and access administrator, compliance analyst, platform engineer),
  eight postings from 2025–26 found by title and location only, on employer career sites or applicant
  tracking systems (Greenhouse, Lever, Ashby, Workday). Draw employers from a fixed list: the Fortune 500
  plus 50 venture-backed software firms, sampled at random with seed 20261010.
- **S1b, new titles.** Every posting already cited in `roles/`, plus up to five more per role found by exact
  title, so each role has 6–10 full postings.

### 4.4 Capability models (category `capability-model`)

Official versions, not prep-site summaries: Salesforce Agentforce Specialist exam guide; Microsoft AB-620,
AB-730 and Copilot Studio applied skills; Intercom and Zendesk AI certifications; UiPath agentic and Workato
Agent Studio certifications; ServiceNow AI Control Tower role definitions; IAPP AIGP body of knowledge
(current version); ISACA AAIA and AAISM exam outlines; FINRA Series 57 content outline; NERC system
operator certification content outline; AMIA clinical informatics core competencies and the ABPM content
outline; SFIA 9 skills related to AI; any published GTM engineer, legal engineer or forward-deployed
engineer curriculum or career ladder.

### 4.5 Practitioner speech (category `media-current`, `media-historical`)

The two frames in `sources-v2/`. Clean them first (`sources-v2/README.md`), then fetch captions and
transcript pages with `acquire.py --kind video` and the podcast transcript pages; transcribe audio for items
with no transcript (for example with Whisper) and save to `corpus/text/<id>.txt`.

### 4.6 Rule-change events (category `rule-change-event`)

Postmortems and policy changes in which a company changed, kept or retired a rule that people or agents act
under, 2023–2026: published incident reports (Replit, Cursor, AWS, and others in the activity ledger),
regulator orders (SEC, FCA, PRA, FTC, EU Digital Services Act decisions), policy changelogs (lab scaling
policies; expense and approval policies rewritten for agents). Target 40 events.

## 5. Quality checks before analysis

- At least 80% of manifest sources `ok` or `ok-browser`; list the rest with reasons.
- Every role in `roles/` has six or more full postings and at least one official capability model.
- Every load-bearing claim in the first-round findings is matched to a corpus passage or marked
  "not confirmed".
