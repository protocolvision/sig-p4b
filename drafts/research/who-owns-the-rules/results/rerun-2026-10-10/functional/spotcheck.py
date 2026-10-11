"""Draw the 60-posting spot-check sample (40 weight-proportional from the whole selected set, 20 from AI-titled
postings; seed 20261013). Writes spotcheck-sample.csv (verdicts are added by hand in spotcheck-verdicts.csv)."""
import numpy as np
from common import *
p = load_postings()
rng = np.random.default_rng(20261013)
a = p.sample(40, weights=p.sw, random_state=20261013)
b = p[(p.group == "newtitle") & ~p.doc_id.isin(a.doc_id)].sample(20, random_state=20261014)
s = pd.concat([a.assign(draw="universe-weighted"), b.assign(draw="ai-titled")]).reset_index(drop=True)
s.insert(0, "n", range(1, 61))
s[["n", "draw", "doc_id", "employer", "title", "department", "onet_use", "fn", "fn_src"]].to_csv(OUT / "spotcheck-sample.csv", index=False)
for r in s.itertuples():
    print(r.n, "|", r.employer, "|", r.title, "|", r.department, "|", r.onet_use, "->", r.fn, f"({r.fn_src})")
