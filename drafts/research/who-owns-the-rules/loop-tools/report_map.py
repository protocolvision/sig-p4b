"""2D map of duty statements for the report's method walkthrough (display only; not an analysis input).

Takes the discovery half of the leaf clustering (clusters/leaf/assignments.csv.gz), samples about 3,000
statements (all members of the 8 stable work clusters and the 4 large unstable AI clusters, plus a seeded
sample of other-cluster and noise statements), projects their cached mpnet embeddings to 2D with UMAP
(cosine, n_neighbors 30, min_dist 0.15, seed 7) and writes report/data/map.json.
"""
import csv, gzip, json, pathlib, sys
import numpy as np, pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "loop-tools"))
from cluster_tasks import get_embeddings, norm, key  # noqa: E402

LEAF = ROOT / "results/rerun-2026-10-10/clusters/leaf"
WORK = {2, 19, 43, 67, 69, 76, 83, 111}
LANG = {0, 6, 10}
AI_UNSTABLE = {110, 112, 113, 21}

df = pd.read_csv(LEAF / "assignments.csv.gz", usecols=["task_id", "half", "cluster_id"])
df = df[df.half == "discovery"].reset_index(drop=True)
want, span = set(df.task_id), {}
for line in open(ROOT / "corpus/b-raw/extract/postings-haiku-all.tasks.jsonl"):
    t = json.loads(line)
    if t["task_id"] in want:
        span[t["task_id"]] = norm(t["span"])
df["span"] = df.task_id.map(span)
assert df.span.notna().all(), df.span.isna().sum()
df["skey"] = df.span.map(key)
rng = np.random.default_rng(7)
cid = df.cluster_id.values
keep = np.isin(cid, list(WORK | AI_UNSTABLE))
other = np.where((cid >= 0) & ~keep & ~np.isin(cid, list(LANG)))[0]
noise = np.where(cid < 0)[0]
idx = np.sort(np.concatenate([np.where(keep)[0], rng.choice(other, 800, replace=False), rng.choice(noise, 1100, replace=False)]))
sub = df.loc[idx].reset_index(drop=True)
X = get_embeddings(sub, False, None)
import umap
Z = umap.UMAP(n_neighbors=30, n_components=2, min_dist=0.15, metric="cosine", random_state=7).fit_transform(X)
Z = (Z - Z.min(0)) / (Z.max(0) - Z.min(0))
labels = {int(r["cluster_id"]): r["label"] for r in csv.DictReader(open(LEAF / "labels.csv"))}
size = {int(r["cluster_id"]): (int(r["size_discovery"]), int(r["n_employers"]), float(r["best_holdout_jaccard"]))
        for r in csv.DictReader(open(LEAF / "clusters.csv"))}
pts = []
for (x, y), c, s in zip(Z, sub.cluster_id, sub.span):
    c = int(c)
    kind = "work" if c in WORK else "ai" if c in AI_UNSTABLE else "noise" if c < 0 else "other"
    p = [round(float(x), 4), round(float(y), 4), c if kind in ("work", "ai") else -1 if kind == "noise" else -2]
    if kind in ("work", "ai") and rng.random() < 0.25:
        p.append(s[:110] + ("…" if len(s) > 110 else ""))
    pts.append(p)
out = dict(n_discovery=int(len(df)), n_shown=len(pts),
           clusters={c: dict(label=labels[c], kind="work" if c in WORK else "ai", size=size[c][0], employers=size[c][1],
                             jaccard=size[c][2]) for c in sorted(WORK | AI_UNSTABLE)},
           points=pts)
(ROOT / "report/data/map.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
print(len(pts), "points;", (ROOT / "report/data/map.json").stat().st_size // 1024, "KB")
