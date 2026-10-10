"""Score speech extraction variants against the blind review (deviation 13).

Joins the reviewer's judgements (speech-v2-judged.csv, speech-v2-gold.csv) with the hidden key of which
model produced each record. Matched spans between the two models (word-set Jaccard >= 0.5, one-to-one)
count once in the union. For each variant (union, Sonnet-only, Haiku-only, consensus):
  precision = records that are verbatim and target / records
  recall    = gold activities covered by at least one target record / gold activities
Applies the pre-registered choice rule and writes results/rerun-2026-10-10/review/speech-v2-scores.md.
"""
import collections, csv, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
REV = ROOT / "results" / "rerun-2026-10-10" / "review"
KEY = ROOT / "corpus" / "b-raw" / "review" / "speech-sample-v2-key.json"


def toks(s):
    return set(re.findall(r"[a-z0-9]+", s.lower()))


def main():
    key = {k["rid"]: k for k in json.load(open(KEY))}
    judged = {r["rid"]: r for r in csv.DictReader(open(REV / "speech-v2-judged.csv"))}
    gold = collections.defaultdict(set)
    for r in csv.DictReader(open(REV / "speech-v2-gold.csv")):
        gold[r["doc_id"]].add(r["gold_n"])
    by_doc = collections.defaultdict(lambda: {"H": [], "S": []})
    for rid, k in key.items():
        by_doc[k["doc_id"]][k["model"]].append(rid)

    # pair Haiku and Sonnet records per document (one-to-one, Jaccard >= 0.5)
    pairs = {}
    for doc, m in by_doc.items():
        used = set()
        for h in m["H"]:
            th = toks(key[h]["span"])
            best, j = 0.0, None
            for s in m["S"]:
                if s in used:
                    continue
                ts = toks(key[s]["span"])
                v = len(th & ts) / len(th | ts) if th | ts else 0.0
                if v > best:
                    best, j = v, s
            if j is not None and best >= 0.5:
                used.add(j)
                pairs[h] = j

    consensus_s = set(pairs.values())
    variants = {
        "sonnet_only": [r for r in key if key[r]["model"] == "S"],
        "haiku_only": [r for r in key if key[r]["model"] == "H"],
        "consensus": sorted(consensus_s),
        "union": [r for r in key if key[r]["model"] == "S"] + [h for h in key if key[h]["model"] == "H" and h not in pairs],
    }

    def good(rid):
        j = judged.get(rid, {})
        yes = lambda v: str(v).strip().lower() in ("yes", "y", "1", "true")
        return yes(j.get("verbatim")) and yes(j.get("is_target"))

    n_gold = sum(len(v) for v in gold.values())
    rows = []
    for name, rids in variants.items():
        tp = sum(good(r) for r in rids)
        covered = set()
        for r in rids:
            if good(r):
                for g in (judged[r].get("covers_gold_n") or "").replace(";", ",").split(","):
                    if g.strip():
                        covered.add((key[r]["doc_id"], g.strip()))
        p = tp / len(rids) if rids else 0.0
        rc = len(covered) / n_gold if n_gold else 0.0
        rows.append((name, len(rids), round(p, 3), round(rc, 3), p >= 0.7 and rc >= 0.7))
    passing = [r for r in rows if r[4]]
    choice = max(passing, key=lambda r: r[3])[0] if passing else "none (report measured limits)"
    lines = ["# Speech extraction variants (deviation 13)", "", f"Gold activities: {n_gold} in {len(gold)} chunks.", "",
             "| Variant | Records | Precision | Recall | Passes both 0.7 |", "| --- | --- | --- | --- | --- |"]
    lines += [f"| {n} | {k} | {p} | {r} | {'yes' if ok else 'no'} |" for n, k, p, r, ok in rows]
    lines += ["", f"**Chosen by the pre-registered rule: {choice}**", ""]
    (REV / "speech-v2-scores.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
