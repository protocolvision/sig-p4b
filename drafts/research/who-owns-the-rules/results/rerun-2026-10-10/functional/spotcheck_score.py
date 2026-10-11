"""Score the hand spot check. Verdicts were entered by the analyst (an AI agent, not an independent coder) from the
title, employer and department shown in the sample files, judging whether the assigned function is the
business function the title most plausibly belongs to. wrong = clearly another function; partial = defensible but
a better home exists. Strict accuracy counts correct only; lenient counts partial as correct."""
from common import *
# sample 1 = first draw, scored with the first version of the map (before any rule edits)
V1 = {"wrong": [14, 15, 18, 22, 24, 29, 37, 45, 55, 58], "partial": [31, 40, 43, 44, 49, 53]}
# sample 2 = fresh draw (seed 20261013) scored with the final map in function_map.py
V2 = {"wrong": [15], "partial": [5, 28, 38, 50, 57]}
rows = []
for name, f, v in (("first map, first draw", "spotcheck-sample-v1.csv", V1), ("final map, fresh draw", "spotcheck-sample.csv", V2)):
    s = pd.read_csv(OUT / f)
    s["verdict"] = np.where(s.n.isin(v["wrong"]), "wrong", np.where(s.n.isin(v["partial"]), "partial", "correct"))
    s.to_csv(OUT / f.replace("sample", "verdicts"), index=False)
    for sub, d in (("all 60", s), ("universe-weighted 40", s[s.draw == "universe-weighted"]), ("AI-titled 20", s[s.draw == "ai-titled"])):
        k = int((d.verdict == "correct").sum()); pr = int((d.verdict == "partial").sum()); n = len(d)
        rows.append(dict(map=name, subset=sub, n=n, correct=k, partial=pr, wrong=n - k - pr, strict=round(k / n, 3),
                         strict_lo=round(wilson(k, n)[1], 3), strict_hi=round(wilson(k, n)[2], 3), lenient=round((k + pr) / n, 3)))
r = pd.DataFrame(rows); r.to_csv(OUT / "spotcheck-accuracy.csv", index=False); print(r.to_string())
