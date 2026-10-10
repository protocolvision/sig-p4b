"""Two-phase estimate of postings with agent duties (deviation 24).

Phase 1: the lexical flag (i1_labour.lex_flag) marks postings with any flagged task.
Phase 2: 600 sampled flagged tasks (150 S1, 300 rest20, 150 new-title) were coded by two agents; final codes
are agreed codes plus blind Opus adjudication of disagreements. A task is "confirmed" if its final code
includes AO, PE or RD.

Per group g with confirmation rate p_g (Wilson interval), a flagged posting with k flagged tasks is
estimated to have at least one confirmed task with probability 1 - (1 - p_g)^k (assumes tasks confirm
independently within a posting; stated as a limitation). Estimated confirmed postings = sum over flagged
postings of that probability × the sampling weight (rest20 inverse sampling fraction, column `sw`).
Writes results/rerun-2026-10-10/instruments/I1-twophase.md and appends rows to I1-tables.csv.
"""
import csv, json, math, pathlib, sys

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN = ROOT / "results" / "rerun-2026-10-10"
sys.path.insert(0, str(ROOT / "loop-tools"))
from i1_labour import lex_flag  # noqa: E402

CONF = {"AO", "PE", "RD"}


def wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 0.0, 0.0
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return p, (c - r) / d, (c + r) / d


def codes(path, idcol="id"):
    return {r[idcol]: {x.strip().upper() for x in (r["code1"], r.get("code2", "")) if x and x.strip()}
            for r in csv.DictReader(open(path))}


def main():
    cod = RUN / "coding"
    a, b = codes(cod / "phase2-coderA.csv"), codes(cod / "phase2-coderB.csv")
    adj = codes(cod / "phase2-adjudicated.csv")
    final = {i: (a[i] if a[i] == b.get(i) else adj.get(i, a[i])) for i in a}
    key = json.load(open(ROOT / "corpus/b-raw/coding/phase2-key.json"))
    rate = {}
    for g in ("S1", "rest20", "newtitle"):
        ids = [i for i, k in key.items() if k["group"] == g]
        k = sum(bool(final[i] & CONF) for i in ids)
        rate[g] = (k, len(ids)) + wilson(k, len(ids))

    # flagged tasks per posting
    doc_group = {}
    for line in open(ROOT / "corpus/b-raw/extract/postings-input.jsonl"):
        r = json.loads(line)
        doc_group[r["id"]] = r["group"]
    kflag = {}
    for line in open(ROOT / "corpus/b-raw/extract/postings-haiku-all.tasks.jsonl"):
        r = json.loads(line)
        if lex_flag(r["span"]):
            kflag[r["doc_id"]] = kflag.get(r["doc_id"], 0) + 1
    p = pd.read_csv(RUN / "instruments" / "I1-posting-level.csv.gz")
    p["k"] = p["doc_id"].map(kflag).fillna(0).astype(int)
    p["sw"] = p["sw"].fillna(1.0)

    out = ["# I1 two-phase estimate (deviation 24)", "",
           "Confirmation rate of flagged tasks (final code AO, PE or RD; agreed codes plus blind adjudication):", "",
           "| Group | Confirmed / sampled | Rate | Wilson 95% |", "| --- | --- | --- | --- |"]
    for g, (k, n, pr, lo, hi) in rate.items():
        out.append(f"| {g} | {k} / {n} | {pr:.3f} | {lo:.3f}–{hi:.3f} |")
    est = {}
    for g in ("S1", "rest20", "newtitle"):
        sub = p[(p.group == g) & (p.k > 0)]
        vals = []
        for pr in rate[g][2:]:
            vals.append(float(((1 - (1 - pr) ** sub.k) * sub.sw).sum()))
        est[g] = vals  # point, low, high
    total_new = float(p[p.group == "newtitle"].sw.sum())
    out += ["", "Estimated postings with at least one confirmed agent duty (weighted):", "",
            "| Group | Point | Low | High | Flagged postings (weighted) |", "| --- | --- | --- | --- | --- |"]
    for g, (pt, lo, hi) in est.items():
        flagged = float(p[(p.group == g) & (p.k > 0)].sw.sum())
        out.append(f"| {g} | {pt:.0f} | {lo:.0f} | {hi:.0f} | {flagged:.0f} |")
    ex_pt = est["S1"][0] + est["rest20"][0]
    ex_lo = est["S1"][1] + est["rest20"][1]
    ex_hi = est["S1"][2] + est["rest20"][2]
    nt_pt, nt_lo, nt_hi = est["newtitle"]
    out += ["", f"New-title postings (all, weighted): {total_new:.0f}; of which estimated with a confirmed agent duty: "
            f"{nt_pt:.0f} ({nt_lo:.0f}–{nt_hi:.0f}).", "",
            "**Ratio, existing postings with a confirmed agent duty : new-title postings with a confirmed agent duty**: "
            f"{ex_pt / nt_pt:.2f} (range {ex_lo / nt_hi:.2f}–{ex_hi / nt_lo:.2f}, crossing the interval ends).", "",
            f"**Ratio against all new-title postings**: {ex_pt / total_new:.2f} (range {ex_lo / total_new:.2f}–{ex_hi / total_new:.2f}).", "",
            "Limitations: independence of task confirmation within a posting; coder agreement on phase-2 tasks is "
            "moderate (kappa 0.61–0.64 for AO and PE before adjudication); lexical screen recall is below 1, so "
            "postings with agent duties that use none of the terms are missed in both groups.", ""]
    (RUN / "instruments" / "I1-twophase.md").write_text("\n".join(out))
    print("\n".join(out))


if __name__ == "__main__":
    main()
