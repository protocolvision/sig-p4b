"""Score the codebook coding (deviations 6, 8, 17).

Joins coder A and B record codes with the hidden key (corpus/b-raw/coding/record-pool-key.json) and the
seed key (corpus/b-raw/seeds/seeds-v3-key.csv). Reports:
  - seed recall per code (a code counts if either of the coder's two codes matches the true code; on RD
    seeds a PE code is not a false positive, per deviation 8) with Wilson 95% intervals and the gate
    (recall >= 0.7 and lower bound >= 0.5);
  - seed precision per code (among seeds, how often a coder's code matches the seed's true or second code);
  - Cohen's kappa per code between coders on all 410 records (code present vs absent);
  - validation: on real posting records in found clusters, agreement between each record's code and its
    cluster's primary code from the same coder.
Writes results/rerun-2026-10-10/coding/scores.md.
"""
import csv, json, math, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
COD = ROOT / "results" / "rerun-2026-10-10" / "coding"
CODES = ["PV", "PE", "RD", "AO", "OT"]


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - r) / d, (c + r) / d)


def codes_of(row):
    return {x.strip().upper() for x in (row.get("code1", ""), row.get("code2", "")) if x and x.strip()}


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    key = {k["id"]: k for k in json.load(open(ROOT / "corpus/b-raw/coding/record-pool-key.json"))}
    seedkey = list(csv.DictReader(open(ROOT / "corpus/b-raw/seeds/seeds-v3-key.csv")))
    seedtrue = {int(r["seed_n"]): (r["true_code"].upper(), (r.get("second_code") or "").upper()) for r in seedkey}
    coders = {}
    for c in ("A", "B"):
        coders[c] = {r["id"]: codes_of(r) for r in csv.DictReader(open(COD / f"coder{c}-records.csv"))}
    packets = {}
    for c in ("A", "B"):
        packets[c] = {r["packet"]: r for r in csv.DictReader(open(COD / f"coder{c}-packets.csv"))}
    pkey = json.load(open(ROOT / "corpus/b-raw/coding/packet-key.json"))
    cluster_to_packet = {v: k for k, v in pkey.items()}

    out = ["# Codebook coding scores (deviations 6, 8, 17)", ""]
    for c in ("A", "B"):
        out += [f"## Coder {c}", "", "| Code | Seeds | Recall | Wilson 95% | Gate | Seed precision |",
                "| --- | --- | --- | --- | --- | --- |"]
        seeds = [(i, k) for i, k in key.items() if k["_src"] == "seed"]
        for code in ["PV", "PE", "RD"]:
            pos = [(i, k) for i, k in seeds if seedtrue[k["_seed_n"]][0] == code]
            hit = sum(code in coders[c].get(i, set()) for i, _ in pos)
            lo, hi = wilson(hit, len(pos))
            rec = hit / len(pos) if pos else 0
            gate = "pass" if rec >= 0.7 and lo >= 0.5 else "FAIL"
            said = [(i, k) for i, k in seeds if code in coders[c].get(i, set())]
            ok = 0
            for i, k in said:
                t, s = seedtrue[k["_seed_n"]]
                if code in (t, s) or (code == "PE" and t == "RD"):
                    ok += 1
            prec = ok / len(said) if said else float("nan")
            out.append(f"| {code} | {len(pos)} | {rec:.2f} | {lo:.2f}–{hi:.2f} | {gate} | {prec:.2f} (n={len(said)}) |")
        # false positives on negative seeds
        neg = [(i, k) for i, k in seeds if seedtrue[k["_seed_n"]][0] in ("AO", "OT")]
        fp = sum(bool(coders[c].get(i, set()) & {"PV", "PE", "RD"}) for i, _ in neg)
        out += ["", f"Negative seeds coded as PV/PE/RD: {fp} of {len(neg)} ({fp / len(neg):.0%}).", ""]

    ids = sorted(key)
    out += ["## Agreement between coders (all 410 records)", "", "| Code | Kappa | A yes | B yes |", "| --- | --- | --- | --- |"]
    for code in CODES:
        a = [code in coders["A"].get(i, set()) for i in ids]
        b = [code in coders["B"].get(i, set()) for i in ids]
        out.append(f"| {code} | {kappa(a, b):.2f} | {sum(a)} | {sum(b)} |")

    out += ["", "## Validation: record code vs its cluster's primary code (real posting records in found clusters)", ""]
    for c in ("A", "B"):
        rows = [(i, k) for i, k in key.items() if k["_src"] == "real" and k.get("_cluster") is not None
                and k["_cluster"] in cluster_to_packet]
        agree = 0
        for i, k in rows:
            prim = packets[c][cluster_to_packet[k["_cluster"]]]["primary_code"].strip().upper()
            agree += prim in coders[c].get(i, set())
        out.append(f"- Coder {c}: {agree} of {len(rows)} records carry their cluster's primary code "
                   f"({agree / len(rows):.0%})." if rows else f"- Coder {c}: no records")
    out += ["", "## Real records: code counts", "", "| Code | A | B |", "| --- | --- | --- |"]
    real = [i for i, k in key.items() if k["_src"] == "real"]
    for code in CODES:
        out.append(f"| {code} | {sum(code in coders['A'].get(i, set()) for i in real)} | "
                   f"{sum(code in coders['B'].get(i, set()) for i in real)} |")
    (COD / "scores.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
