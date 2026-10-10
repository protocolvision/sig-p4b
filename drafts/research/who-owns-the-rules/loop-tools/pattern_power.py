"""Power check and margin for pattern matching (triangulation-design.md, addendum A).

Reads results/rerun-2026-10-10/signatures.csv. Uses only features observable within about three years
(late features and their late halves are excluded; duplicates N04b and N06b are dropped). For each pattern
as the truth, simulates coding noise (each feature moves one step with probability Q) and records how
often each pattern would be declared "supported" at a given margin. The margin is the smallest value at
which a wrong pattern is supported in at most 5% of runs, for every truth, AND no pattern is supported in
more than 5% of runs when the truth is a 50/50 blend of two patterns or a random profile (addendum A,
amendment 1). Patterns whose ideal margin is below that value form families.

Usage: python3 loop-tools/pattern_power.py [Q]   (writes results/rerun-2026-10-10/pattern-power-q<Q>.md)
"""
import collections, csv, pathlib, random

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN = ROOT / "results" / "rerun-2026-10-10"
V = {"yes": 1.0, "partial": 0.5, "no": 0.0}
LATE = {"N04", "N04b", "N06", "N06b", "N16", "N16b", "N17", "N18"}
import sys
Q = float(sys.argv[1]) if len(sys.argv) > 1 else 0.2
RUNS, SEED, FALSE_MAX = 2000, 20261011, 0.05
MARGINS = [round(0.01 * i, 2) for i in range(1, 41)]


def load():
    prof, nf, names = collections.defaultdict(dict), collections.defaultdict(set), {}
    for r in csv.DictReader(open(RUN / "signatures.csv", newline="")):
        f = r["feature_id"]
        if f in LATE:
            continue
        prof[r["pattern"]][f] = V[r["value"].strip().lower()]
        names[f] = r["feature"]
        if r["grade"].strip().upper() == "NF":
            nf[r["pattern"]].add(f)
    return prof, nf, names


def score(present, pat, prof, nf):
    use = [f for f in prof[pat] if f not in nf[pat]]
    return 1 - sum(abs(present[f] - prof[pat][f]) for f in use) / len(use)


def ranked(present, prof, nf):
    return sorted(((score(present, p, prof, nf), p) for p in prof), reverse=True)


def noisy(p, rng):
    return {f: min(1.0, max(0.0, v + rng.choice([-0.5, 0.5]))) if rng.random() < Q else v for f, v in p.items()}


def main():
    prof, nf, names = load()
    pats = list(prof)
    rng = random.Random(SEED)
    sims = {t: [ranked(noisy(prof[t], rng), prof, nf) for _ in range(RUNS)] for t in pats}

    feats = sorted(next(iter(prof.values())))
    blends = {f"{a} + {b}": [ranked(noisy({f: (prof[a][f] + prof[b][f]) / 2 for f in feats}, rng), prof, nf)
                             for _ in range(RUNS // 4)]
              for i, a in enumerate(pats) for b in pats[i + 1:]}
    null = [ranked({f: rng.choice([0.0, 0.5, 1.0]) for f in feats}, prof, nf) for _ in range(RUNS)]

    def false_rate(m):
        worst = 0.0
        for t, runs in sims.items():
            worst = max(worst, sum(1 for s in runs if s[0][1] != t and s[0][0] - s[1][0] >= m) / RUNS)
        for runs in blends.values():
            worst = max(worst, sum(1 for s in runs if s[0][0] - s[1][0] >= m) / len(runs))
        return max(worst, sum(1 for s in null if s[0][0] - s[1][0] >= m) / len(null))

    margin = next(m for m in MARGINS if false_rate(m) <= FALSE_MAX)
    ideal = {t: ranked(prof[t], prof, nf) for t in pats}
    lines = [
        "# Pattern-matching power check", "",
        f"Addendum A, triangulation-design.md. Features observable now: {len(names)} "
        f"({', '.join(sorted(names))}). Noise q = {Q}, {RUNS} runs per truth, seed {SEED}.", "",
        f"**Margin: {margin}** (smallest at which a wrong pattern is supported in at most "
        f"{FALSE_MAX:.0%} of runs, for every truth; worst false rate {false_rate(margin):.1%}).", "",
        "| Truth | Ideal margin over runner-up | Runner-up | Supported when true | Top when true |",
        "| --- | --- | --- | --- | --- |",
    ]
    families = []
    for t in pats:
        s = ideal[t]
        sup = sum(1 for r in sims[t] if r[0][1] == t and r[0][0] - r[1][0] >= margin) / RUNS
        top = sum(1 for r in sims[t] if r[0][1] == t) / RUNS
        lines.append(f"| {t} | {s[0][0] - s[1][0]:.2f} | {s[1][1]} | {sup:.0%} | {top:.0%} |")
        if s[0][0] - s[1][0] < margin:
            families.append((t, s[1][1]))
    lines += ["", "**Families** (ideal margin below the threshold; reported together, then as not yet "
              "distinguishable): " + ("; ".join(f"{a} with {b}" for a, b in families) or "none"), ""]
    (RUN / f"pattern-power-q{Q}.md").write_text("\n".join(lines))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
