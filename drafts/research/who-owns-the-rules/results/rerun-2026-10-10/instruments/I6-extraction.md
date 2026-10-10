# I6 extraction: practitioner speech (S7, M-frame)

Prompt `speech` v1 in `loop-tools/extract_tasks.py`; post-processing `loop-tools/speech_post.py`. Models: claude-haiku-5-5 and claude-sonnet-5-5, all chunks, batch API. Seed for sample 20261017.

- Transcripts chunked: 38 of 38 M transcript files: 30 timestamped (batch 1) and 8 without timestamps (batch 2: M013, M032, M041, M053, M054, M067, M068, M077; chunked by paragraph, `position` field e.g. "para 14-22"; scraped pages that include show-notes and ads, so some records may not be speech).
- Chunks: 189 timestamped + 42 paragraph-position = 231 (about 1,200 words, 100-word overlap), 0 failed requests in both batches.
- Batch 1 (timestamped, 189 chunks): Haiku 1,215, Sonnet 1,366 records; verbatim 0.973 / 0.997. Agreement (Jaccard >= 0.5, one-to-one): 813 matched; P 0.669, R 0.595, F1 0.630; exact F1 0.368; median count ratio 0.857 (gate passed); 6 chunks with exactly one model empty. Consensus 813, 771 after overlap dedupe (42 dropped).
- Batch 2 (no timestamps, 42 chunks, reported separately): Haiku 156, Sonnet 198 records; verbatim 0.936 / 1.000. AGREE_NT
- **Combined consensus records after dedupe: 862** (771 + 91; batch 2 consensus 101, 10 overlap duplicates dropped). Per-transcript batch 2: {'M041': 20, 'M053': 18, 'M054': 18, 'M067': 35}. Timestamp field is empty or unreliable for batch 2.
- Of the 862, 1 are non-verbatim (flagged); 6 are `general claim` (kept, flagged, not evidence of practice).

## Consensus records by function (combined)

| Function | Chunks | Records |
|---|---|---|
| sales, RevOps and go-to-market | 37 | 216 |
| finance | 29 | 122 |
| procurement | 29 | 116 |
| IT, identity and security | 22 | 99 |
| engineering and platform | 26 | 93 |
| customer support/CX | 27 | 81 |
| risk and compliance | 16 | 49 |
| HR and people ops | 21 | 40 |
| legal and legal ops | 17 | 29 |
| general operations leadership (COO) | 7 | 17 |

## By speaker_relation (combined)

| Value | Records |
|---|---|
| own team | 561 |
| self | 285 |
| other team | 10 |
| general claim | 6 |

## By performer_type (combined)

| Value | Records |
|---|---|
| person | 646 |
| both | 141 |
| agent | 75 |

## Vendor or consultant share (media-current.csv, combined)

- Transcripts: 9 of 38 (24%); design cap is one third.
- Chunks: 45 of 231 (19%).
- Consensus records: 105 of 862 (12%); flagged, not removed.

## Outputs

- `corpus/b-raw/extract/speech-input.jsonl`, `speech-input-notime.jsonl`, runs `speech-haiku/`, `speech-sonnet/`, `speech-nt-haiku/`, `speech-nt-sonnet/`, `speech-consensus/` (consensus-dedup.jsonl holds both batches), `speech-nt-consensus/`
- `corpus/b-raw/review/speech-sample.jsonl`: 25 chunks from batch 1 only (not redrawn), 82 records.
- Note: collect strips `[HH:MM:SS]` before the verbatim check for speech (first pass gave a false 0.60).
