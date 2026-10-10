# Extraction check: speech sample

Source: `corpus/b-raw/review/speech-sample.jsonl` (25 chunks, 82 extracted records, 5 chunks with no records). Each record was checked by hand against its chunk. Verbatim matching was scripted, ignoring timestamps and whitespace. Row-level judgements are in `extraction-check-speech.csv`.

## Numbers

| Metric | Value |
|---|---|
| Verbatim | 82/82 (1.00) |
| **Precision** (verbatim AND target) | **68/82 = 0.83** |
| Missed target activities | 43 (9 of them borderline) |
| **Estimated recall** 68/(68+43) | **0.61** (0.67 if the 9 borderline misses are excluded) |
| Relation accuracy | 75/82 = 0.91 for all records; 64/68 = 0.94 for target records |
| Performer accuracy | 80/82 = 0.98 for all records; 67/68 = 0.99 for target records |

Recall is estimated only from the misses in these 25 chunks. One overlapping passage (M081_c01/c02) is counted once.

## Main error types

**Recall (the main problem)**
1. **Dense self-reports are under-extracted.** M024_c03 (Cargill CIO) has 4 records and 7 misses, including "we've chosen to flip that mix", "as we insource, we are targeting everything from cybersecurity talent…", "in last fiscal year, we targeted to hire at least 300" and "half my job was spent just saying, No, it's not ready for that yet". M040_c07 misses "actually even wrote a book about it", "I've used a lot of that learning today for for AI" and "my FP&amp;A team going through redesigning that workflow".
2. **Chunks with zero records that do contain activities.** M056_c01 has "We really encourage clients to focus on…" and "We've estimated up to potentially 3 million…". M088_c02 has "I have taken a youngster as my reverse mentor" and "I'm learning new tools".
3. **General claims are almost never captured.** The sample has 1 general-claim record, and it is not an activity. Misses include "you'll see a ton of examples of people that are leveraging agents to help serve their customers" (M056_c01) and "A lot of folks we chat to say support and sales are their top two use cases for agents" (M073_c04).
4. **Agent-performed actions are missed.** Examples: "Now it just books the meeting." (M073_c06) and "so we're adding like voice and video to this agent as well".

**Precision (14 non-target records)**
1. **States, roles and dispositions extracted as activities (6).** "Obviously I work for a German company", "I'm accountable for those financial outcomes", "We have this line at Shopify, which is AI replaces tasks, not jobs.", "they're willing to change their processes" / "They're willing to use tech.", and "Board members want to know how companies…".
2. **Product pitches (3).** "That's something my company helps with.", "We have dozens of AI agents already set up at Artificial Intelligence Risk Inc." and "We have AI courts."
3. **Fragments without the activity (3).** "We actually exceeded that.", "we're in the process of doing that", and the malformed "I'm also adding like Jason Stealthy already has um voice".
4. **Host speech or talk narration (2).** "We're distributed on Substack and LinkedIn." comes from the host. "let me also take you through the span of time…" is narration, not work.

**Relation errors (7 records, 4 of them on target records)**
- **Other teams in the same company labelled "own team".** These are the Prudential marketing-technology team (M081_c01:1, :2) and the adidas Brazil team (M018_c01:7, :8).
- **McKinsey observations about client companies labelled "own team" instead of "general claim".** These are M056_c00:1 and :3.
- **The host's line M064_c06:3.**

**Performer errors (2 records).** M016_c01:7 is labelled "both", but the team does the rebuilding. M052_c03:1 is labelled "person", but it describes agents.

## Verdict (threshold 0.7 for both)

- Precision 0.83: **pass**
- Recall 0.61 (0.67 under the strict count): **fail**

**Overall: FAIL.** The extractor is accurate when it fires, with clean verbatim spans and mostly correct labels. But it misses about 4 in 10 target activities, and it nearly never captures general claims. The recall gap is concentrated in long first-person answers and in chunks it left empty. Fix recall before running at scale, for example with a second pass per chunk asking "what else did the speaker or their team do?". Also tighten the rules for own team versus other team and for excluding states and pitches.
