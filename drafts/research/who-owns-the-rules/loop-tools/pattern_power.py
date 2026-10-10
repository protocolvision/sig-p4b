"""Power check and margin for pattern matching (triangulation-design.md, addendum A, A.1 and A.2).

Reads results/rerun-2026-10-10/signatures.csv (value and grade columns). Rules fixed in addendum A.2:

- Feature set. One common set for all patterns: features observable within about three years (late
  features and their late halves excluded) that are graded (P or R, not NF) in at least 5 of the 7
  patterns. A common feature that is NF for a pattern is a missing cell for that pattern: its raw score is
  1 - mean |present - profile| over the cells it does grade.
- Percentiles. Each pattern's raw score is converted to a mid-rank percentile against its own null
  distribution (NREF uniform random presents over the same feature set, separate seed). Ranks and margins
  use these percentiles.
- Truth presents. A feature graded in the truth pattern takes the pattern's value; a feature NF in the
  truth pattern takes a random value from {0, 0.5, 1}. Never "no".
- Noise. Each coder independently moves each feature one step with probability Q: 0 -> 0.5, 1 -> 0.5,
  0.5 -> 0 or 1 at random; an off-grid blend value (0.25, 0.75) moves 0.5 toward the middle.
- Coders. Two coders. Each coder's values are scored separately; a pattern's score is the mean of the two
  coders' percentiles. Values are never averaged into "partial".
- Margin. The smallest margin (step 0.01) at which, with 5% as the bound for every condition:
  (a) for every truth pattern, a different pattern is supported in at most 5% of runs;
  (b) for every pair, under the feature-wise average blend, no pattern is supported in more than 5%;
  (c) for every pair, under the 50/50 random mixture, no pattern is supported in more than 5%;
  (d) under the uniform null, no pattern is supported in more than 5%.
  "Supported" = top percentile score and at least the margin above the next.

Usage: python3 loop-tools/pattern_power.py Q [--drop N01,N08,...] [--out NAME]
       python3 loop-tools/pattern_power.py stages   (A.3 two-stage test, q = 0.2 and 0.3;
       writes results/rerun-2026-10-10/pattern-power-v3.md)
       python3 loop-tools/pattern_power.py a4       (A.4 final: pair Stage 1 + A.3 Stage 2;
       writes results/rerun-2026-10-10/pattern-power-v4.md)
  writes results/rerun-2026-10-10/pattern-power-v2-q<Q>.md (or NAME). --drop removes features (used to
  recalibrate on the features actually scored, after "insufficient" codes are known).
"""
import bisect, collections, csv, pathlib, random, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN = ROOT / "results" / "rerun-2026-10-10"
V = {"yes": 1.0, "partial": 0.5, "no": 0.0}
GRID = (0.0, 0.5, 1.0)
LATE = {"N04", "N04b", "N06", "N06b", "N16", "N16b", "N17", "N18"}
COMMON_MIN = 5
RUNS, NREF, SEED, REF_SEED, FALSE_MAX = 2000, 20000, 20261011, 20261012, 0.05
MARGINS = [round(0.01 * i, 2) for i in range(1, 101)]
TRUNCATED = ["N01", "N04a", "N08", "N12", "N23"]  # A.2 truncation rule may make these "insufficient"


def load():
    prof, graded, allf = collections.defaultdict(dict), collections.defaultdict(dict), []
    for r in csv.DictReader(open(RUN / "signatures.csv", newline="")):
        f = r["feature_id"]
        if f in LATE:
            continue
        if f not in allf:
            allf.append(f)
        prof[r["pattern"]][f] = V[r["value"].strip().lower()]
        graded[r["pattern"]][f] = r["grade"].strip().upper() != "NF"
    return prof, graded, allf


class Model:
    def __init__(self, prof, graded, feats, q):
        self.prof, self.graded, self.feats, self.q = prof, graded, feats, q
        self.pats = list(prof)
        self.use = {p: [f for f in feats if graded[p][f]] for p in self.pats}
        ref = random.Random(REF_SEED)
        self.ref = {p: [] for p in self.pats}
        for _ in range(NREF):
            x = {f: ref.choice(GRID) for f in feats}
            for p in self.pats:
                self.ref[p].append(self.raw(x, p))
        for p in self.pats:
            self.ref[p].sort()

    def raw(self, x, p):
        u = self.use[p]
        return 1 - sum(abs(x[f] - self.prof[p][f]) for f in u) / len(u)

    def pct(self, x, p):
        s, r = self.raw(x, p), self.ref[p]
        return (bisect.bisect_left(r, s - 1e-12) + bisect.bisect_right(r, s + 1e-12)) / 2 / len(r)

    def val(self, p, f, rng):
        return self.prof[p][f] if self.graded[p][f] else rng.choice(GRID)

    def truth(self, t, rng):
        return {f: self.val(t, f, rng) for f in self.feats}

    def blend_avg(self, a, b, rng):
        return {f: (self.val(a, f, rng) + self.val(b, f, rng)) / 2 for f in self.feats}

    def blend_mix(self, a, b, rng):
        return {f: self.val(rng.choice((a, b)), f, rng) for f in self.feats}

    def null(self, rng):
        return {f: rng.choice(GRID) for f in self.feats}

    def code(self, x, rng):
        out = {}
        for f, v in x.items():
            if rng.random() < self.q:
                v = rng.choice((0.0, 1.0)) if v == 0.5 else (v + 0.5 if v < 0.5 else v - 0.5)
            out[f] = v
        return out

    def run(self, x, rng):
        """Two coders code the same present; returns ranked [(score, pattern)] and their disagreement."""
        c1, c2 = self.code(x, rng), self.code(x, rng)
        sc = sorted((((self.pct(c1, p) + self.pct(c2, p)) / 2), p) for p in self.pats)[::-1]
        return (sc[0][1], sc[0][0] - sc[1][0]), sum(c1[f] != c2[f] for f in self.feats) / len(self.feats)


def supported(r, m):
    """r = (top pattern, gap to the next)."""
    return r[0] if r[1] >= m - 1e-9 else None


def analyse(prof, graded, feats, q):
    M = Model(prof, graded, feats, q)
    pats, rng = M.pats, random.Random(SEED)
    sims, dis = {}, []
    for t in pats:
        sims[t] = []
        for _ in range(RUNS):
            r, d = M.run(M.truth(t, rng), rng)
            sims[t].append(r)
            dis.append(d)
    pairs = [(a, b) for i, a in enumerate(pats) for b in pats[i + 1:]]
    avg = {pr: [M.run(M.blend_avg(*pr, rng), rng)[0] for _ in range(RUNS)] for pr in pairs}
    mix = {pr: [M.run(M.blend_mix(*pr, rng), rng)[0] for _ in range(RUNS)] for pr in pairs}
    nul = [M.run(M.null(rng), rng)[0] for _ in range(RUNS)]

    def rates(m):
        wrong = {p: max(sum(supported(r, m) == p for r in sims[t]) / RUNS for t in pats if t != p) for p in pats}
        ba = {p: max(sum(supported(r, m) == p for r in runs) / RUNS for runs in avg.values()) for p in pats}
        bm = {p: max(sum(supported(r, m) == p for r in runs) / RUNS for runs in mix.values()) for p in pats}
        nu = {p: sum(supported(r, m) == p for r in nul) / RUNS for p in pats}
        return wrong, ba, bm, nu

    def worst(m):
        return max(max(d.values()) for d in rates(m))

    margin = next((m for m in MARGINS if worst(m) <= FALSE_MAX), None)

    # Null top shares: uniform presents, one coder, no noise (the reference null), and the two-coder null.
    top_ref, top_raw = collections.Counter(), collections.Counter()
    nrng = random.Random(SEED + 7)
    for _ in range(RUNS * 5):
        x = M.null(nrng)
        for counter, fn in ((top_ref, M.pct), (top_raw, M.raw)):
            s = {p: fn(x, p) for p in pats}
            best = max(s.values())
            winners = [p for p in pats if abs(s[p] - best) < 1e-12]
            for p in winners:
                counter[p] += 1 / len(winners)
    top_two = collections.Counter(r[0] for r in nul)

    # Ideal (noiseless) gap: median over draws of the NF cells.
    ideal = {}
    for t in pats:
        gaps, runner = [], collections.Counter()
        for _ in range(500):
            x = M.truth(t, rng)
            s = sorted(((M.pct(x, p), p) for p in pats), reverse=True)
            gaps.append(s[0][0] - s[1][0] if s[0][1] == t else -(s[0][0] - next(v for v, p in s if p == t)))
            runner[s[1][1] if s[0][1] == t else s[0][1]] += 1
        gaps.sort()
        ideal[t] = (gaps[len(gaps) // 2], runner.most_common(1)[0][0])
    return dict(M=M, sims=sims, margin=margin, rates=rates(margin) if margin else None, dis=sum(dis) / len(dis),
                top_ref=top_ref, top_raw=top_raw, top_two=top_two, ideal=ideal, n=RUNS * 5)


def table(res, title):
    M, pats, m = res["M"], res["M"].pats, res["margin"]
    L = [f"## {title}", "",
         f"Features scored ({len(M.feats)}): {', '.join(M.feats)}. Missing cells (NF in the pattern): "
         + "; ".join(f"{p} {', '.join(f for f in M.feats if not M.graded[p][f])}"
                     for p in pats if len(M.use[p]) < len(M.feats)) + ".", ""]
    if m is None:
        return L + ["**No margin up to 1.00 meets the 5% bound on every condition.**", ""]
    wrong, ba, bm, nu = res["rates"]
    L += [f"**Margin: {m:.2f}** (percentile points, two coders; worst false-support rate "
          f"{max(max(d.values()) for d in res['rates']):.1%}). Mean simulated coder disagreement when a "
          f"pattern is the truth: {res['dis']:.2f}.", "",
          "| Truth | Supported when true | Top when true | False support: other truths (worst) "
          "| Average blend (worst pair) | Mixture blend (worst pair) | Null | Ideal gap | Nearest |",
          "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for t in pats:
        sup = sum(supported(r, m) == t for r in res["sims"][t]) / RUNS
        top = sum(r[0] == t for r in res["sims"][t]) / RUNS
        g, near = res["ideal"][t]
        L.append(f"| {t} | {sup:.0%} | {top:.0%} | {wrong[t]:.1%} | {ba[t]:.1%} | {bm[t]:.1%} | {nu[t]:.1%} "
                 f"| {g:.2f} | {near} |")
    fam = [(t, res["ideal"][t][1]) for t in pats if res["ideal"][t][0] < m]
    L += ["", "**Families** (median noiseless percentile gap below the margin): "
          + ("; ".join(f"{a} with {b}" for a, b in fam) or "none"), "",
          f"**Null top shares** ({res['n']} uniform random presents; 1/7 = 14.3%):", "",
          "| Pattern | Percentile, one coder, no noise | Percentile, two coders with noise | Raw score (A.1 rule) |",
          "| --- | --- | --- | --- |"]
    for p in pats:
        L.append(f"| {p} | {res['top_ref'][p] / res['n']:.1%} | {res['top_two'][p] / RUNS:.1%} "
                 f"| {res['top_raw'][p] / res['n']:.1%} |")
    return L + [""]


# ---------------------------------------------------------------- Addendum A.3: two-stage test
PAIR = ("DevOps", "Scarcity boom then specialisation")
KS = [0.5 * i for i in range(1, 13)]


def distance(prof, graded, a, b, feats):
    u = [f for f in feats if graded[a][f] and graded[b][f]]
    return sum(abs(prof[a][f] - prof[b][f]) for f in u) / len(u)


def families(prof, graded, feats):
    """A.3 rule: link two patterns when their ideal distance is at most half the median of all pairwise
    distances; families are the connected components (single linkage)."""
    pats = list(prof)
    d = {(a, b): distance(prof, graded, a, b, feats) for i, a in enumerate(pats) for b in pats[i + 1:]}
    vals = sorted(d.values())
    med = (vals[len(vals) // 2] + vals[(len(vals) - 1) // 2]) / 2
    thr = med / 2
    comp = {p: {p} for p in pats}
    for (a, b), v in d.items():
        if v <= thr + 1e-12 and comp[a] is not comp[b]:
            merged = comp[a] | comp[b]
            for p in merged:
                comp[p] = merged
    fams, seen = [], set()
    for p in pats:
        if p not in seen:
            fams.append(tuple(q for q in pats if q in comp[p]))
            seen |= comp[p]
    return fams, d, med, thr


def s2_features(prof, graded, feats):
    a, b = PAIR
    return [f for f in feats if graded[a][f] and graded[b][f] and abs(prof[a][f] - prof[b][f]) >= 0.5]


def s2_stat(x, prof, feats):
    a, b = PAIR
    return sum((abs(x[f] - prof[b][f]) > abs(x[f] - prof[a][f])) - (abs(x[f] - prof[a][f]) > abs(x[f] - prof[b][f]))
               for f in feats)


def fname(f):
    return " + ".join("Scarcity boom" if p == PAIR[1] else p for p in f)


def stages(q, runs=RUNS):
    prof, graded, allf = load()
    pats = list(prof)
    feats = [f for f in allf if sum(graded[p][f] for p in pats) >= COMMON_MIN]
    fams, dist, med, thr = families(prof, graded, feats)
    s2 = s2_features(prof, graded, feats)
    s2t = [f for f in s2 if f not in TRUNCATED]
    M = Model(prof, graded, feats, q)
    rng = random.Random(SEED)
    famof = {p: f for f in fams for p in f}

    def one(x):
        c1, c2 = M.code(x, rng), M.code(x, rng)
        ps = {p: (M.pct(c1, p) + M.pct(c2, p)) / 2 for p in pats}
        fs = sorted(((max(ps[p] for p in f), f) for f in fams), reverse=True)
        return (fs[0][1], fs[0][0] - fs[1][0], (s2_stat(c1, prof, s2) + s2_stat(c2, prof, s2)) / 2,
                (s2_stat(c1, prof, s2t) + s2_stat(c2, prof, s2t)) / 2)

    pairs = [(a, b) for i, a in enumerate(pats) for b in pats[i + 1:]]
    truth = {t: [one(M.truth(t, rng)) for _ in range(runs)] for t in pats}
    avg = {pr: [one(M.blend_avg(*pr, rng)) for _ in range(runs)] for pr in pairs}
    mix = {pr: [one(M.blend_mix(*pr, rng)) for _ in range(runs)] for pr in pairs}
    nul = [one(M.null(rng)) for _ in range(runs)]

    def fsup(r, m):
        return r[0] if r[1] >= m - 1e-9 else None

    def s1_rates(m):
        """Worst false-support rate per family under each condition (support of a family is false unless
        it contains the truth, or both parents of a blend)."""
        out = {}
        for F in fams:
            w = max([sum(fsup(r, m) == F for r in truth[t]) / runs for t in pats if t not in F] or [0])
            ba = max([sum(fsup(r, m) == F for r in avg[pr]) / runs for pr in pairs
                      if not (pr[0] in F and pr[1] in F)] or [0])
            bm = max([sum(fsup(r, m) == F for r in mix[pr]) / runs for pr in pairs
                      if not (pr[0] in F and pr[1] in F)] or [0])
            nu = sum(fsup(r, m) == F for r in nul) / runs
            out[F] = (w, ba, bm, nu)
        return out

    m1 = next((m for m in MARGINS if max(max(v) for v in s1_rates(m).values()) <= FALSE_MAX), None)

    a, b = PAIR
    pr = tuple(sorted(PAIR, key=pats.index))
    s2_conds = {"DevOps true": truth[a], "Scarcity true": truth[b], "average blend": avg[pr], "mixture blend": mix[pr]}

    def s2_wrong(k, idx):
        return {"Scarcity call, DevOps true": sum(r[idx] <= -k for r in truth[a]) / runs,
                "DevOps call, Scarcity true": sum(r[idx] >= k for r in truth[b]) / runs,
                "DevOps call, average blend": sum(r[idx] >= k for r in avg[pr]) / runs,
                "Scarcity call, average blend": sum(r[idx] <= -k for r in avg[pr]) / runs,
                "DevOps call, mixture blend": sum(r[idx] >= k for r in mix[pr]) / runs,
                "Scarcity call, mixture blend": sum(r[idx] <= -k for r in mix[pr]) / runs}

    ks = {idx: next((k for k in KS if max(s2_wrong(k, idx).values()) <= FALSE_MAX), None) for idx in (2, 3)}
    dfam = famof[a]

    L = ["# Pattern-matching power check, v3 (two-stage test)", "",
         f"Addendum A.3, triangulation-design.md. Noise q = {q} per coder, two coders, {runs} runs per "
         f"condition, seed {SEED}; percentile null {NREF} presents, seed {REF_SEED}. Same 15 features, NF "
         "randomisation, noise, blends and null as A.2.", "",
         "## Stage 1: families", "",
         f"Rule: two patterns are linked when their ideal distance (mean |difference| over the common "
         f"features both grade) is at most half the median of the 21 pairwise distances; families are the "
         f"connected components. Median {med:.3f}, threshold {thr:.3f}.", "",
         "Closest pairs: " + "; ".join(f"{fname((x,))}–{fname((y,))} {v:.3f}"
                                       for (x, y), v in sorted(dist.items(), key=lambda kv: kv[1])[:6]) + ".", "",
         "Families: " + "; ".join(f"{{{fname(f)}}}" for f in fams) + ".", ""]
    if m1 is None:
        L += ["**No Stage 1 margin up to 1.00 meets the 5% bound.**", ""]
    else:
        rates = s1_rates(m1)
        L += [f"**Stage 1 margin: {m1:.2f}** (percentile points; family score = best member's two-coder "
              f"percentile). Worst false-support rate {max(max(v) for v in rates.values()):.1%}.", "",
              "| Family | Supported when a member is true (each member) | False: other truths | Average blend "
              "| Mixture blend | Null | Null top share |", "| --- | --- | --- | --- | --- | --- | --- |"]
        for F in fams:
            pw = ", ".join(f"{fname((t,))} {sum(fsup(r, m1) == F for r in truth[t]) / runs:.0%}" for t in F)
            w, ba, bm, nu = rates[F]
            top = sum(r[0] == F for r in nul) / runs
            L.append(f"| {fname(F)} | {pw} | {w:.1%} | {ba:.1%} | {bm:.1%} | {nu:.1%} | {top:.1%} |")
        L.append("")
    for idx, fs, lab in ((2, s2, "all six features"), (3, s2t, "truncation rule applied")):
        k = ks[idx]
        L += [f"## Stage 2: DevOps against Scarcity boom ({lab})", "",
              f"Features ({len(fs)}): {', '.join(fs)}. Statistic: per feature +1 if the coded value is closer "
              "to DevOps, −1 if closer to Scarcity boom, 0 if tied; summed per coder; mean of the two coders.", ""]
        if k is None:
            L += ["**No k meets the 5% bound on every wrong call.**", ""]
            continue
        wr = s2_wrong(k, idx)
        L += [f"**k = {k}**. Wrong-call rates: " + "; ".join(f"{n} {v:.1%}" for n, v in wr.items()) + ".", "",
              "| Truth | DevOps over Scarcity | Not distinguishable | Scarcity over DevOps |", "| --- | --- | --- | --- |"]
        for n, rs in s2_conds.items():
            d_ = sum(r[idx] >= k for r in rs) / runs
            s_ = sum(r[idx] <= -k for r in rs) / runs
            L.append(f"| {n} | {d_:.0%} | {1 - d_ - s_:.0%} | {s_:.0%} |")
        L.append("")
        if m1 is not None:
            def verdict(r):
                return fsup(r, m1) == dfam and r[idx] >= k
            L += [f"**H-DevOps \"supported\" under A.3 ({lab})**: DevOps true {sum(map(verdict, truth[a])) / runs:.0%}; "
                  f"Scarcity true {sum(map(verdict, truth[b])) / runs:.1%}; worst other truth "
                  f"{max(sum(map(verdict, truth[t])) / runs for t in pats if t not in PAIR):.1%}; worst average blend "
                  f"{max(sum(map(verdict, avg[p])) / runs for p in pairs):.1%}; worst mixture blend "
                  f"{max(sum(map(verdict, mix[p])) / runs for p in pairs):.1%}; null {sum(map(verdict, nul)) / runs:.1%}. "
                  f"\"Family only\" when DevOps true: "
                  f"{sum(fsup(r, m1) == dfam and -k < r[idx] < k for r in truth[a]) / runs:.0%}.", ""]
    return L


# ---------------------------------------------------------------- Addendum A.4: final scoring
def a4(q, runs=RUNS):
    """Stage 1: the pair (DevOps, its nearest pattern Scarcity boom) scored as max of the two percentiles,
    against the best of the other five. Stage 2 as in A.3."""
    prof, graded, allf = load()
    pats = list(prof)
    feats = [f for f in allf if sum(graded[p][f] for p in pats) >= COMMON_MIN]
    a, b = PAIR
    others = [p for p in pats if p not in PAIR]
    s2 = s2_features(prof, graded, feats)
    s2t = [f for f in s2 if f not in TRUNCATED]
    M = Model(prof, graded, feats, q)
    rng = random.Random(SEED)

    def one(x):
        c1, c2 = M.code(x, rng), M.code(x, rng)
        ps = {p: (M.pct(c1, p) + M.pct(c2, p)) / 2 for p in pats}
        return (max(ps[a], ps[b]) - max(ps[p] for p in others),
                (s2_stat(c1, prof, s2) + s2_stat(c2, prof, s2)) / 2,
                (s2_stat(c1, prof, s2t) + s2_stat(c2, prof, s2t)) / 2)

    pairs = [(x, y) for i, x in enumerate(pats) for y in pats[i + 1:]]
    truth = {t: [one(M.truth(t, rng)) for _ in range(runs)] for t in pats}
    avg = {pr: [one(M.blend_avg(*pr, rng)) for _ in range(runs)] for pr in pairs}
    mix = {pr: [one(M.blend_mix(*pr, rng)) for _ in range(runs)] for pr in pairs}
    nul = [one(M.null(rng)) for _ in range(runs)]
    false_pairs = [pr for pr in pairs if not (pr[0] in PAIR and pr[1] in PAIR)]

    def rate(rs, m):
        return sum(r[0] >= m - 1e-9 for r in rs) / runs

    def false_rates(m):
        return {"truths": {t: rate(truth[t], m) for t in others},
                "average blend": max(rate(avg[pr], m) for pr in false_pairs),
                "mixture blend": max(rate(mix[pr], m) for pr in false_pairs),
                "null": rate(nul, m)}

    def worst(m):
        fr = false_rates(m)
        return max(max(fr["truths"].values()), fr["average blend"], fr["mixture blend"], fr["null"])

    m = next((x for x in MARGINS if worst(x) <= FALSE_MAX), None)
    K = {1: 4.0, 2: 3.0}  # A.3: k = 4 on six features, k = 3 on the four left after truncation
    L = [f"## q = {q}", "",
         f"Two coders, {runs} runs per condition, seed {SEED}; percentile null {NREF} presents, seed "
         f"{REF_SEED}. Pair = {{DevOps, Scarcity boom}}; pair score = max of the two percentiles, compared "
         "with the best of the other five.", ""]
    if m is None:
        return L + ["**No Stage 1 margin up to 1.00 meets the 5% bound.**", ""]
    fr = false_rates(m)
    L += [f"**Stage 1 margin: {m:.2f}** (worst false-support rate {worst(m):.1%}).", "",
          f"Stage 1 power (pair passes): DevOps true **{rate(truth[a], m):.0%}**; Scarcity boom true "
          f"**{rate(truth[b], m):.0%}**; average blend of the two {rate(avg[tuple(sorted(PAIR, key=pats.index))], m):.0%}; "
          f"mixture blend of the two {rate(mix[tuple(sorted(PAIR, key=pats.index))], m):.0%}.", "",
          "False support for the pair: " + "; ".join(f"{t} true {v:.1%}" for t, v in fr["truths"].items())
          + f"; worst average blend involving another pattern {fr['average blend']:.1%}; worst mixture blend "
          f"{fr['mixture blend']:.1%}; null {fr['null']:.1%}.", "",
          "| Truth | Stage 2 set | k | supported | family only | not supported: Stage 2 says Scarcity "
          "| not supported: pair not picked |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for t in PAIR + tuple(others):
        for idx, lab in ((1, "six features"), (2, "truncated (four)")):
            k, rs = K[idx], truth[t]
            sup = sum(r[0] >= m - 1e-9 and r[idx] >= k for r in rs) / runs
            fam = sum(r[0] >= m - 1e-9 and -k < r[idx] < k for r in rs) / runs
            sc = sum(r[0] >= m - 1e-9 and r[idx] <= -k for r in rs) / runs
            L.append(f"| {fname((t,))} | {lab} | {k:g} | {sup:.1%} | {fam:.1%} | {sc:.1%} | {1 - sup - fam - sc:.1%} |")
    return L + [""]


def main():
    args = sys.argv[1:]
    if args and args[0] == "a4":
        L = ["# Pattern-matching power check, v4 (addendum A.4, final)", ""]
        for q in (0.2, 0.3):
            L += a4(q)
        (RUN / "pattern-power-v4.md").write_text("\n".join(L))
        print("\n".join(L))
        return
    if args and args[0] == "stages":
        L = []
        for q in (0.2, 0.3):
            L += stages(q) + ["---", ""]
        (RUN / "pattern-power-v3.md").write_text("\n".join(L))
        print("\n".join(L))
        return
    q = float(args[0]) if args else 0.2
    drop = set(args[args.index("--drop") + 1].split(",")) if "--drop" in args else set()
    out = args[args.index("--out") + 1] if "--out" in args else f"pattern-power-v2-q{q}.md"
    prof, graded, allf = load()
    pats = list(prof)
    count = {f: sum(graded[p][f] for p in pats) for f in allf}
    feats = [f for f in allf if count[f] >= COMMON_MIN and f not in drop]
    left = [f"{f} ({count[f]} of 7)" for f in allf if count[f] < COMMON_MIN]
    main_res = analyse(prof, graded, feats, q)
    L = ["# Pattern-matching power check, v2", "",
         f"Addendum A.2, triangulation-design.md. Noise q = {q} per coder, two coders, {RUNS} runs per "
         f"condition, seed {SEED}; null reference {NREF} presents, seed {REF_SEED}. Scores are mid-rank "
         "percentiles against each pattern's own null; margins are in percentile points.", "",
         f"Common feature set: observable-now features graded in at least {COMMON_MIN} of 7 patterns. "
         f"Not scored: {', '.join(left)}" + (f"; dropped by --drop: {', '.join(sorted(drop))}" if drop else "")
         + ".", ""]
    L += table(main_res, "Main result")
    if not drop:
        trunc = [f for f in feats if f not in TRUNCATED]
        L += ["Sensitivity (not the pre-registered margin): if the truncation rule makes all five of "
              f"{', '.join(TRUNCATED)} \"insufficient\", the script recalibrates on the remaining "
              f"{len(trunc)} features, as follows.", ""]
        L += table(analyse(prof, graded, trunc, q), "Sensitivity: truncation-exposed features insufficient")
    (RUN / out).write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
