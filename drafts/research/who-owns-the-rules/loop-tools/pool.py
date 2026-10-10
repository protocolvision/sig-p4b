"""Build the shuffled, de-labelled pools for each iteration of the loop.

Usage: python3 pool.py RESULTS_DIR
Strata enter in the pre-registered order (loop-design.md, section 3). Each record gets a random ID that is
the same in every pool, so clusterings can be compared; document IDs are replaced too, so the stratum
is not visible. pool/key.json maps pool IDs back to ledger IDs.
"""
import json, random, sys, pathlib

ORDER = ["S4", "S1", "S5", "S2", "S3"]
SEED = 20261010

res = pathlib.Path(sys.argv[1])
rng = random.Random(SEED)
records = {}
for s in ORDER:
    for line in (res / "ledger" / f"{s}.jsonl").read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            records[r["id"]] = r

ids = list(records)
codes = rng.sample(range(1000, 9999), len(ids))
key = {f"R{c}": i for c, i in zip(codes, ids)}
rev = {v: k for k, v in key.items()}
docs = sorted({r["doc"] for r in records.values()})
dcodes = rng.sample(range(100, 999), len(docs))
dkey = {d: f"D{c}" for d, c in zip(docs, dcodes)}

(res / "pool").mkdir(exist_ok=True)
(res / "pool" / "key.json").write_text(json.dumps({"records": key, "docs": dkey}, indent=1))
for k in range(1, 6):
    pool = []
    for i, r in records.items():
        if i.split("-")[0] in ORDER[:k]:
            q = {f: v for f, v in r.items() if f not in ("id", "doc")}
            pool.append({"id": rev[i], "doc": dkey[r["doc"]], **q})
    rng.shuffle(pool)
    with open(res / "pool" / f"iter-{k}.jsonl", "w") as f:
        for q in pool:
            f.write(json.dumps(q, ensure_ascii=False) + "\n")
    print(f"iter-{k}: {len(pool)} records")
