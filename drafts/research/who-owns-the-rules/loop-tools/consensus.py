"""Consensus extraction from two runs (deviation 9).

Keeps spans found by both models: one-to-one greedy matching per document on word-set Jaccard >= 0.5, the
rule fixed in log.md. The kept span uses run B's text (Sonnet). Unmatched spans from either run go to a
separate file, flagged with the model that found them, and are excluded from clustering.

Usage: python3 loop-tools/consensus.py RUN_A RUN_B OUT_NAME
Reads corpus/b-raw/extract/<run>/tasks.jsonl; writes corpus/b-raw/extract/<OUT_NAME>/consensus.jsonl,
single-model.jsonl and report.json.
"""
import collections, json, pathlib, re, sys

EXTRACT = pathlib.Path(__file__).resolve().parent.parent / "corpus" / "b-raw" / "extract"


def toks(s):
    return set(re.findall(r"[a-z0-9]+", s.lower()))


def load(run):
    by_doc = collections.defaultdict(list)
    for line in open(EXTRACT / run / "tasks.jsonl"):
        r = json.loads(line)
        by_doc[r["doc_id"]].append(r)
    return by_doc


def main():
    run_a, run_b, out_name = sys.argv[1:4]
    a, b = load(run_a), load(run_b)
    out = EXTRACT / out_name
    out.mkdir(parents=True, exist_ok=True)
    kept = single_a = single_b = 0
    with open(out / "consensus.jsonl", "w") as fc, open(out / "single-model.jsonl", "w") as fs:
        for doc in sorted(a.keys() | b.keys()):
            ra, rb = a.get(doc, []), b.get(doc, [])
            used = set()
            for x in ra:
                tx = toks(x["span"])
                best, j = 0.0, None
                for k, y in enumerate(rb):
                    if k in used:
                        continue
                    ty = toks(y["span"])
                    s = len(tx & ty) / len(tx | ty) if tx | ty else 0.0
                    if s > best:
                        best, j = s, k
                if j is not None and best >= 0.5:
                    used.add(j)
                    rec = dict(rb[j], consensus_jaccard=round(best, 3), span_a=x["span"])
                    fc.write(json.dumps(rec) + "\n")
                    kept += 1
                else:
                    fs.write(json.dumps(dict(x, found_by=run_a)) + "\n")
                    single_a += 1
            for k, y in enumerate(rb):
                if k not in used:
                    fs.write(json.dumps(dict(y, found_by=run_b)) + "\n")
                    single_b += 1
    report = {"run_a": run_a, "run_b": run_b, "docs": len(a.keys() | b.keys()), "consensus": kept,
              "single_a": single_a, "single_b": single_b}
    (out / "report.json").write_text(json.dumps(report, indent=1))
    print(json.dumps(report))


if __name__ == "__main__":
    main()
