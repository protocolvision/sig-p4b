"""Q5: security review, AI governance, guardrail/permission and service-management duty statements by posting function.
Duty statements = 305,533 spans of postings-haiku-all.tasks.jsonl (counts per posting from tasks_pass.py, keyword lists in
q5_keywords.py). Rate per 1,000 duty statements = sum(sw * matching duties) / sum(sw * duties) * 1000, sw = rest20 sampling weight.
Intervals: 95% percentile bootstrap over postings within sampling group (2,000 resamples). Also: share of postings with at least
one matching duty (weighted, Wilson on Kish n)."""
from common import *
from q5_keywords import FAMILIES
T = Table()
p = load_postings().merge(pd.read_csv(OUT / "doc-duty-counts.csv.gz"), on="doc_id", how="left")
for c in ["n_duty", "k_flag"] + list(FAMILIES): p[c] = p[c].fillna(0).astype(int)
p = p[p.n_duty > 0].copy()
print("postings with duties:", len(p))
fns = FUNCTIONS
pops = {"all_weighted": p, "existing_weighted": p[p.group.isin(["S1", "rest20"])], "ai_titled": p[p.group == "newtitle"]}
rng = np.random.default_rng(20261016)
B = 2000
for pop, d in pops.items():
    fidx = d.fn.map({f: i for i, f in enumerate(fns)}).values
    sw = d.sw.values; nd = d.n_duty.values
    groups = [np.where(d.group.values == g)[0] for g in d.group.unique()]
    fams = list(FAMILIES)
    H = np.stack([d[f].values for f in fams], 1)
    def rates(ix):
        den = np.bincount(fidx[ix], weights=sw[ix] * nd[ix], minlength=len(fns))
        out = np.zeros((len(fams), len(fns) + 1))
        for j in range(len(fams)):
            num = np.bincount(fidx[ix], weights=sw[ix] * H[ix, j], minlength=len(fns))
            out[j, :-1] = num / np.maximum(den, 1e-9) * 1000
            out[j, -1] = num.sum() / den.sum() * 1000
        return out, den
    pt, den0 = rates(np.arange(len(d)))
    bs = np.zeros((B,) + pt.shape)
    for r in range(B):
        ix = np.concatenate([rng.choice(g, len(g)) for g in groups])
        bs[r] = rates(ix)[0]
    lo, hi = np.percentile(bs, [2.5, 97.5], axis=0)
    for i, f in enumerate(fns + ["ALL"]):
        dd = d if f == "ALL" else d[d.fn == f]
        if not len(dd): continue
        T.add("Q5", f, f"{pop}:duty_statements_weighted", float((dd.sw * dd.n_duty).sum()), None, None, int(dd.n_duty.sum()))
        for j, fam in enumerate(fams):
            T.add("Q5", f, f"{pop}:{fam}_per_1000_duties", float(pt[j, i]), float(lo[j, i]), float(hi[j, i]), int(dd.n_duty.sum()))
            T.add("Q5", f, f"{pop}:{fam}_duty_count_unweighted", int(dd[fam].sum()), None, None, int(dd.n_duty.sum()))
            share = float(dd.sw[dd[fam] > 0].sum() / dd.sw.sum()); ne = kish(dd.sw)
            _, l2, h2 = wilson(share * ne, ne)
            T.add("Q5", f, f"{pop}:{fam}_posting_share", share, l2, h2, len(dd))
T.df().to_csv(OUT / "tables-q5.csv", index=False)
print(len(T.rows))
