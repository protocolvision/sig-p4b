"""Q1 (AI-title demand), Q2 (agent duties in existing-title postings), Q3 (activities by function). Writes tables-q1q3.csv."""
import re
from common import *
from i1_twophase import wilson as _w, codes, CONF

T = Table()
p = load_postings()
dc = pd.read_csv(OUT / "doc-duty-counts.csv.gz")
p = p.merge(dc, on="doc_id", how="left")
for c in ["n_duty", "k_flag"]:
    p[c] = p[c].fillna(0).astype(int)

# ---------------- Q1 ----------------
AI_FAM = {"ai_ml": {"ai", "machine learning", "llm", "genai", "generative ai", "copilot", "prompt", "responsible ai", "model risk"},
          "automation": {"automation", "rpa", "intelligent automation"}, "agent": {"agent", "agents", "agentic"}}
p["ai_title"] = p.group == "newtitle"
p["fam"] = p.term.map(lambda t: next((f for f, s in AI_FAM.items() if t in s), None) if isinstance(t, str) else None)
for f in FUNCTIONS + ["ALL"]:
    d = p if f == "ALL" else p[p.fn_q1 == f]
    if not len(d): continue
    neff = kish(d.sw)
    wd = d.sw.sum()
    for meas, mask in (("ai_title_share", d.ai_title), ("ai_ml_title_share", d.ai_title & (d.fam == "ai_ml")),
                       ("automation_title_share", d.ai_title & (d.fam == "automation")), ("agent_title_share", d.ai_title & (d.fam == "agent"))):
        wn = d.sw[mask].sum()
        _, lo, hi = wilson(wn / wd * neff, neff)
        T.add("Q1", f, meas, wn / wd, lo, hi, len(d))
    T.add("Q1", f, "ai_title_postings_n", int(d.ai_title.sum()), None, None, len(d))
    T.add("Q1", f, "weighted_postings", float(wd), None, None, len(d))
# share of all AI-titled postings that sit in each function
tot = p.ai_title.sum()
for f in FUNCTIONS:
    k = int((p.ai_title & (p.fn_q1 == f)).sum())
    pr, lo, hi = wilson(k, tot)
    T.add("Q1", f, "share_of_all_ai_titled", pr, lo, hi, int(tot))

# census cross-check on all titles of postings-mapped-v2 (non-excluded boards)
m = pd.read_csv(ROOT / "corpus/b-raw/mapping/postings-mapped-v2.csv", usecols=KEY + ["title", "onet_code"])
ex = {l.strip() for l in open(RUN / "corpus-b/exclude-boards.txt") if l.strip() and not l.startswith("#")}
m = m[~(m.ats + "-" + m.board_id.astype(str)).isin(ex)].drop_duplicates(KEY)
TERMS = [r"AI", r"A\.I\.", r"agentic", r"LLM", r"GenAI", r"generative AI", r"machine learning", r"automation", r"prompt",
         r"copilot", r"intelligent automation", r"RPA", r"AI governance", r"responsible AI", r"model risk", r"agents?"]
TRX = re.compile(r"(?<![\w.])(?:" + "|".join(TERMS) + r")(?![\w])", re.I)
ADJ = r"(?:AI|A\.I\.|agentic|autonomous|virtual|digital)"
AGX = re.compile(r"(?<![\w.])(?:" + ADJ + r"[\s\-/]+agents?|agents?[\s\-/]+" + ADJ + r")(?![\w])", re.I)
BARE = re.compile(r"(?<![\w.])agents?(?![\w])", re.I)
def is_ai_title(t):
    t = str(t)
    hits = [h.group(0).lower() for h in TRX.finditer(t)]
    if not hits: return False
    if all(h in ("agent", "agents") for h in hits):
        return bool(AGX.search(t))      # bare "agent" counts only when next to AI/agentic/autonomous/virtual/digital
    return True
m["ai_title"] = m.title.map(is_ai_title)
m["fn_q1"] = [assign(t, c, strip_ai=True)[0] for t, c in zip(m.title, m.onet_code)]
for f in FUNCTIONS + ["ALL"]:
    d = m if f == "ALL" else m[m.fn_q1 == f]
    pr, lo, hi = wilson(int(d.ai_title.sum()), len(d))
    T.add("Q1", f, "census_ai_title_share", pr, lo, hi, len(d))

# ---------------- Q2 ----------------
key = json.load(open(ROOT / "corpus/b-raw/coding/phase2-key.json"))
cod = RUN / "coding"
a, b, adj = codes(cod / "phase2-coderA.csv"), codes(cod / "phase2-coderB.csv"), codes(cod / "phase2-adjudicated.csv")
final = {i: (a[i] if a[i] == b.get(i) else adj.get(i, a[i])) for i in a}
ph = pd.DataFrame([dict(qid=i, group=key[i]["group"], doc_id=key[i]["task_id"].rsplit(":", 1)[0], codes=final[i]) for i in final])
ph = ph.merge(p[["doc_id", "fn", "group"]].rename(columns={"group": "pgroup"}), on="doc_id", how="left")
assert ph.fn.notna().all()
ph["conf"] = ph.codes.map(lambda s: bool(s & CONF))
rate = {}
for g in ("S1", "rest20", "newtitle"):
    sub = ph[ph.group == g]
    rate[g] = wilson(int(sub.conf.sum()), len(sub))   # (p, lo, hi)

ex_ = p[p.group.isin(["S1", "rest20"])].copy()
ex_["pc"] = [1 - (1 - rate[g][0]) ** k for g, k in zip(ex_.group, ex_.k_flag)]
ex_["pc_lo"] = [1 - (1 - rate[g][1]) ** k for g, k in zip(ex_.group, ex_.k_flag)]
ex_["pc_hi"] = [1 - (1 - rate[g][2]) ** k for g, k in zip(ex_.group, ex_.k_flag)]
# reproduce I1-twophase totals
chk = {g: float((ex_[ex_.group == g].pc * ex_[ex_.group == g].sw).sum()) for g in ("S1", "rest20")}
print("two-phase reproduction (published: S1 189, rest20 2340):", chk)

rng = np.random.default_rng(20261015)
B = 2000
fns = FUNCTIONS
fidx = ex_.fn.map({f: i for i, f in enumerate(fns)}).values
gidx = {g: np.where(ex_.group.values == g)[0] for g in ("S1", "rest20")}
ntask = {g: int((ph.group == g).sum()) for g in ("S1", "rest20")}
kconf = {g: int(ph[ph.group == g].conf.sum()) for g in ("S1", "rest20")}
k_arr, sw_arr = ex_.k_flag.values, ex_.sw.values
est_b = np.zeros((B, len(fns) + 1)); den_b = np.zeros((B, len(fns) + 1))
for r in range(B):
    num = np.zeros(len(fns)); den = np.zeros(len(fns))
    for g, ix in gidx.items():
        s = rng.choice(ix, len(ix))
        pg = rng.binomial(ntask[g], kconf[g] / ntask[g]) / ntask[g]
        v = (1 - (1 - pg) ** k_arr[s]) * sw_arr[s]
        num += np.bincount(fidx[s], weights=v, minlength=len(fns))
        den += np.bincount(fidx[s], weights=sw_arr[s], minlength=len(fns))
    est_b[r, :-1] = num / np.maximum(den, 1e-9); est_b[r, -1] = num.sum() / den.sum()
    den_b[r, :-1] = den; den_b[r, -1] = den.sum()
for i, f in enumerate(fns + ["ALL"]):
    d = ex_ if f == "ALL" else ex_[ex_.fn == f]
    if not len(d): continue
    wd = d.sw.sum(); neff = kish(d.sw)
    flag_w = d.sw[d.k_flag > 0].sum()
    _, lo, hi = wilson(flag_w / wd * neff, neff)
    T.add("Q2", f, "flagged_share_existing", flag_w / wd, lo, hi, len(d))
    pt = float((d.pc * d.sw).sum()) / wd
    lo_b, hi_b = np.percentile(est_b[:, i], [2.5, 97.5])
    T.add("Q2", f, "confirmed_agent_duty_share_existing", pt, float(lo_b), float(hi_b), len(d))
    T.add("Q2", f, "confirmed_agent_duty_band_rates_only", pt, float((d.pc_lo * d.sw).sum() / wd), float((d.pc_hi * d.sw).sum() / wd), len(d))
    T.add("Q2", f, "confirmed_agent_duty_postings_weighted", float((d.pc * d.sw).sum()), None, None, len(d))
    T.add("Q2", f, "existing_postings_weighted", float(wd), None, None, len(d))
    # direct phase-2 rate by function (existing-title tasks only)
    sub = ph[(ph.group.isin(["S1", "rest20"])) & ((ph.fn == f) if f != "ALL" else True)]
    pr, lo, hi = wilson(int(sub.conf.sum()), len(sub))
    T.add("Q2", f, "phase2_task_confirmation_rate_existing", pr, lo, hi, len(sub))

# ---------------- Q3 ----------------
CODES = ["AO", "PE", "PV", "RD"]
for f in fns + ["ALL"]:
    for lab, gs in (("all", ["S1", "rest20", "newtitle"]), ("existing", ["S1", "rest20"]), ("newtitle", ["newtitle"])):
        sub = ph[ph.group.isin(gs) & ((ph.fn == f) if f != "ALL" else True)]
        n = len(sub)
        T.add("Q3", f, f"phase2_tasks_sampled_{lab}", n, None, None, n)
        for c in CODES:
            k = int(sub.codes.map(lambda s: c in s).sum())
            pr, lo, hi = wilson(k, n)
            T.add("Q3", f, f"{c}_count_{lab}", k, None, None, n)
            if lab == "all": T.add("Q3", f, f"{c}_share_of_sampled_tasks", pr, lo, hi, n)
# platform-controls P2, posting items
pf = pd.read_csv(RUN / "platform-controls/p2-final.csv")
pf = pf[pf.kind == "posting"].copy()
pf["doc_id"] = pf.orig_id.map(lambda q: key[q]["task_id"].rsplit(":", 1)[0])
pf = pf.merge(p[["doc_id", "fn"]], on="doc_id", how="left")
assert pf.fn.notna().all()
for f in fns + ["ALL"]:
    sub = pf if f == "ALL" else pf[pf.fn == f]
    if not len(sub): continue
    for lab in ("tool_change", "decision", "neither"):
        T.add("Q3", f, f"p2_{lab}_count", int((sub.final == lab).sum()), None, None, len(sub))

T.df().to_csv(OUT / "tables-q1q3.csv", index=False)
ph.drop(columns=["codes"]).assign(codes=ph.codes.map(lambda s: "+".join(sorted(s)))).to_csv(OUT / "phase2-with-function.csv", index=False)
print(len(T.rows), "rows")
