# I6 extraction: practitioner speech (S7, M-frame)

Prompt `speech` v1 in `loop-tools/extract_tasks.py`; post-processing `loop-tools/speech_post.py`. Models: claude-haiku-5-5 and claude-sonnet-5-5, all chunks, batch API. Seed for sample 20261017.

- Transcripts chunked: 30 of 38 M transcript files. Excluded: 8 files with no `[HH:MM:SS]` timestamps (M013, M032, M041, M053, M054, M067, M068, M077 are show-notes or summary pages, not timestamped speech).
- Chunks: 189 (about 1,200 words, 100-word overlap), 0 failed requests.
- Records: Haiku 1,215; Sonnet 1,366. Verbatim rate (timestamps stripped): Haiku 0.973, Sonnet 0.997.
- Agreement (Jaccard >= 0.5, one-to-one): 813 matched; P(Haiku vs Sonnet) 0.669, R 0.595, F1 0.630; exact-match F1 0.368 (diagnostic); median per-chunk count ratio 0.857 (gate 0.8-1.25 passed); 6 chunks where exactly one model returned nothing.
- Consensus records: 813 (Sonnet text); after dropping 42 overlap duplicates between adjacent chunks (Jaccard >= 0.8, earlier kept): **771**. Single-model spans (402 Haiku, 553 Sonnet) are in `single-model.jsonl`, excluded.
- Of the 771, 1 are non-verbatim (flagged); 4 are `general claim` (kept, flagged, not evidence of practice).

## Consensus records by function

| Function | Chunks | Records |
|---|---|---|
| sales, RevOps and go-to-market | 36 | 216 |
| finance | 29 | 122 |
| procurement | 29 | 116 |
| IT, identity and security | 19 | 99 |
| engineering and platform | 24 | 93 |
| risk and compliance | 16 | 49 |
| legal and legal ops | 17 | 29 |
| customer support/CX | 9 | 26 |
| general operations leadership (COO) | 7 | 17 |
| HR and people ops | 3 | 4 |

## By speaker_relation

| Value | Records |
|---|---|
| own team | 514 |
| self | 244 |
| other team | 9 |
| general claim | 4 |

## By performer_type

| Value | Records |
|---|---|
| person | 587 |
| both | 123 |
| agent | 61 |

## Vendor or consultant share (media-current.csv)

- Transcripts: 6 of 30 chunked transcripts are vendor or consultant speakers (20%); design cap is one third.
- Chunks: 31 of 189 (16%).
- Consensus records: 70 of 771 (9%) come from vendor or consultant speakers; they are flagged, not removed.

## Outputs

- `corpus/b-raw/extract/speech-input.jsonl`, `speech-haiku/`, `speech-sonnet/`, `speech-consensus/{consensus,single-model,consensus-dedup}.jsonl`
- `corpus/b-raw/review/speech-sample.jsonl`: 25 chunks, round-robin across functions in seed order, with source text and dedup consensus records (82 records).
- Note: the first collect check counted timestamps inside clauses as non-verbatim (0.60); collect now strips `[HH:MM:SS]` for speech.
