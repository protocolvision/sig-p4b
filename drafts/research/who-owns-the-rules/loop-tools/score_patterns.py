"""Apply the pre-registered pattern-scoring rules (addenda A.1–A.4, reading rule, feature-coding.md) to the two
blind feature coders' outputs. Writes results/rerun-2026-10-10/pattern-match/result.md."""
import csv, pathlib
RUN = pathlib.Path(__file__).resolve().parent.parent / "results" / "rerun-2026-10-10"
V = {"yes": 1.0, "partial": 0.5, "no": 0.0}
def load(n): return {r["feature_id"]: r["value"].strip().lower() for r in csv.DictReader(open(RUN / "pattern-match" / f"coder-{n}.csv"))}
S, H = load("sonnet"), load("haiku")
feats = sorted(S)
out_left = [f for f in feats if S[f] == "insufficient" or H.get(f) == "insufficient"]
scored = [f for f in feats if f not in out_left]
dis = sum(S[f] != H[f] for f in scored) / len(scored) if scored else 1
lines = ["# Pattern-match result (blind feature coding, scored by rule)", "",
         "| Feature | Sonnet | Haiku |", "| --- | --- | --- |"] + [f"| {f} | {S[f]} | {H.get(f)} |" for f in feats]
lines += ["", f"Features left out (either coder 'insufficient'): {len(out_left)} — {', '.join(out_left)}.",
          f"Scored features: {len(scored)}. Coder disagreement rate on scored features: {dis:.2f}.", ""]
if len(out_left) > 8:
    lines += ["**Pattern verdict: unreliable** (more than 8 of the features left out; feature-coding.md scoring rules). "
              "Per the rule, only feature-level results are given. This is the outcome the A.2–A.4 power analysis anticipated "
              "for about three years of evidence; it is not evidence for or against any pattern.", ""]
# Stage 2 head-to-head (A.3): DevOps vs scarcity on the separating features still scored
SEP = ["N15", "N04a", "N20", "N21", "N22", "N23"]
DEV = {"N15": "partial", "N04a": "yes", "N20": "yes", "N21": "yes", "N22": "yes", "N23": "yes"}
SCA = {"N15": "no", "N04a": "partial", "N20": "no", "N21": "no", "N22": "no", "N23": "partial"}
avail = [f for f in SEP if f in scored]
def h2h(c):
    s = 0
    for f in avail:
        x = V[c[f]]; d, sc = abs(x - V[DEV[f]]), abs(x - V[SCA[f]])
        s += 1 if d < sc else (-1 if sc < d else 0)
    return s
sums = (h2h(S), h2h(H))
lines += [f"Head-to-head (A.3) features available: {len(avail)} of 6 ({', '.join(avail)}). Sums: Sonnet {sums[0]:+d}, "
          f"Haiku {sums[1]:+d}, mean {sum(sums)/2:+.1f}.",
          "Decision thresholds were pre-set only for 6 features (k = 4) and 4 features (k = 3). With "
          f"{len(avail)} features no threshold was fixed, so under the reading rule the head-to-head is "
          "**not distinguishable**; the direction of each separating feature is reported descriptively.", ""]
(RUN / "pattern-match" / "result.md").write_text("\n".join(lines))
print("\n".join(lines[-8:]))
