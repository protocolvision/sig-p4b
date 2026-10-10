"""Speech stratum post-processing: dedupe overlaps between adjacent chunks, draw the clean-review sample.

Run after: extract_tasks.py collect for speech-haiku and speech-sonnet, then consensus.py speech-haiku speech-sonnet speech-consensus.
Writes corpus/b-raw/extract/speech-consensus/consensus-dedup.jsonl and corpus/b-raw/review/speech-sample.jsonl.
"""
import collections, json, pathlib, random, re
R = pathlib.Path(__file__).resolve().parent.parent
EX = R / "corpus/b-raw/extract"
SEED = 20261017

def toks(s): return set(re.findall(r"[a-z0-9]+", s.lower()))
def jac(a, b): return len(a & b) / len(a | b) if a | b else 0.0

docs = {json.loads(l)["id"]: json.loads(l) for l in open(EX / "speech-input.jsonl")}
recs = [json.loads(l) for l in open(EX / "speech-consensus/consensus.jsonl")]
def cidx(d): return int(d.rsplit("_c", 1)[1])
recs.sort(key=lambda r: (docs[r["doc_id"]]["transcript_id"], cidx(r["doc_id"]), r["task_id"]))
kept, dropped = [], 0
for r in recs:
    t = docs[r["doc_id"]]["transcript_id"]; ci = cidx(r["doc_id"]); tk = toks(r["span"])
    if any(docs[k["doc_id"]]["transcript_id"] == t and 0 < ci - cidx(k["doc_id"]) <= 1 and jac(tk, toks(k["span"])) >= 0.8 for k in kept):
        dropped += 1; continue
    r["transcript_id"] = t; r["function"] = docs[r["doc_id"]]["function"]
    r["vendor_or_consultant"] = docs[r["doc_id"]]["vendor_or_consultant"]
    kept.append(r)
with open(EX / "speech-consensus/consensus-dedup.jsonl", "w") as f:
    for r in kept: f.write(json.dumps(r) + "\n")
print("consensus", len(recs), "dedup dropped", dropped, "kept", len(kept))

by_fn = collections.defaultdict(list)
for d in docs.values(): by_fn[d["function"]].append(d["id"])
rng = random.Random(SEED); fns = sorted(by_fn)
for f in fns: by_fn[f].sort()
pick = []
# round-robin over functions in shuffled order until 25 chunks (stratified by function)
rng.shuffle(fns)
for f in fns: rng.shuffle(by_fn[f])
i = 0
while len(pick) < 25 and any(by_fn.values()):
    f = fns[i % len(fns)]; i += 1
    if by_fn[f]: pick.append(by_fn[f].pop())
bydoc = collections.defaultdict(list)
for r in kept: bydoc[r["doc_id"]].append(r)
with open(R / "corpus/b-raw/review/speech-sample.jsonl", "w") as f:
    for did in pick:
        d = docs[did]
        f.write(json.dumps({"doc_id": did, "source_text": d["text"], "function": d["function"],
            "transcript_id": d["transcript_id"], "start": d["start"], "end": d["end"],
            "extracted": [{k: r[k] for k in ("task_id", "span", "speaker", "speaker_relation", "performer_type", "timestamp", "verbatim")} for r in bydoc[did]]}) + "\n")
print("sample", len(pick), "records in sample", sum(len(bydoc[d]) for d in pick))
