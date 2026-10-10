"""Pre-registered clustering pipeline (deviations.md item 16; triangulation-design.md section 5).

Pool: Haiku posting tasks, performer person|both, deduplicated by normalised span within employer,
at most 300 per employer (seed 20261024). Split by posting (seed 20261011) into discovery / holdout.
UMAP (n_neighbors 30, n_components 10, min_dist 0.0, cosine, random_state 42) -> HDBSCAN (min_cluster_size 30,
min_samples 10, eom, prediction_data=True). Holdout: approximate_predict, plus independent clustering; ARI on
points non-noise in both. Noise baseline: three full-pool runs, UMAP seeds 1,2,3, mean pairwise ARI.

Usage (analytics venv): .venv/bin/python cluster_tasks.py [--smoke N]
--smoke N: random N tasks, smaller parameters, outputs to clusters/smoke/; spans missing from the embedding
cache are embedded locally into the smoke folder (the real cache is never written). Code test only.
"""
import sys, argparse, csv, itertools, json, pathlib, random, re, resource, time, hashlib
from importlib.metadata import version

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
TASKS = ROOT / "corpus/b-raw/extract/postings-haiku/tasks.jsonl"
INPUT = ROOT / "corpus/b-raw/extract/postings-input.jsonl"
SELECTION = ROOT / "corpus/b-raw/mapping/selection.csv"
EMBED = ROOT / "corpus/b-raw/embed"
OUT = ROOT / "results/rerun-2026-10-10/clusters"

SEED_POOL, SEED_SPLIT, UMAP_SEED, BASELINE_SEEDS = 20261024, 20261011, 42, (1, 2, 3)
CAP = 300
MODEL = "sentence-transformers/all-mpnet-base-v2"


def norm(s):  # identical to embed_tasks.norm / key
    return re.sub(r"\s+", " ", s).strip()


def key(s):
    return hashlib.sha1(norm(s).lower().encode()).hexdigest()


def load_pool(tasks_path):
    docs = {}
    for line in open(INPUT):
        d = json.loads(line)
        docs[d["id"]] = (d["ats"], d["board_id"], d["posting_id"])
    sel = {}
    with open(SELECTION, newline="") as f:
        for r in csv.DictReader(f):
            sel[(r["ats"], r["board_id"], r["posting_id"])] = (r["employer"], r["group"])
    rows, seen = [], set()
    for line in open(tasks_path):
        t = json.loads(line)
        if t.get("performer") not in ("person", "both"):
            continue
        k = docs.get(t["doc_id"])
        if k is None or k not in sel:
            continue
        emp, grp = sel[k]
        dk = (emp, norm(t["span"]).lower())
        if dk in seen:
            continue
        seen.add(dk)
        rows.append(dict(task_id=t["task_id"], span=norm(t["span"]), ats=k[0], board_id=k[1], posting_id=k[2],
                         employer=emp, group=grp, doc_id=t["doc_id"], skey=key(t["span"])))
    df = pd.DataFrame(rows).sort_values("task_id").reset_index(drop=True)
    n_dedup = len(df)
    rng = np.random.default_rng(SEED_POOL)
    keep = []
    for emp, idx in df.groupby("employer").indices.items():
        idx = np.sort(idx)
        keep.extend(rng.choice(idx, CAP, replace=False) if len(idx) > CAP else idx)
    df = df.loc[np.sort(keep)].reset_index(drop=True)
    return df, n_dedup


def get_embeddings(df, smoke, outdir):
    keys = json.loads((EMBED / "postings.keys.json").read_text()) if (EMBED / "postings.keys.json").exists() else []
    vecs = np.load(EMBED / "postings.npy") if (EMBED / "postings.npy").exists() else np.zeros((0, 768), "float32")
    pos = {k: i for i, k in enumerate(keys)}
    missing = sorted(set(df.skey) - set(pos))
    if missing:
        if not smoke:
            raise SystemExit(f"{len(missing)} spans missing from the embedding cache; run embed_tasks.py first")
        from sentence_transformers import SentenceTransformer
        import torch
        dev = "mps" if torch.backends.mps.is_available() else "cpu"
        text = dict(zip(df.skey, df.span))
        new = SentenceTransformer(MODEL, device=dev).encode([text[k] for k in missing], batch_size=256,
                                                           normalize_embeddings=True, convert_to_numpy=True).astype("float32")
        vecs = np.vstack([vecs, new])
        pos.update({k: len(keys) + i for i, k in enumerate(missing)})
        print(f"smoke: embedded {len(missing)} missing spans locally (not cached)", flush=True)
    return vecs[[pos[k] for k in df.skey]]


def run_umap_hdbscan(X, seed, P, fit_umap_only=False):
    import umap, hdbscan
    um = umap.UMAP(n_neighbors=P["nn"], n_components=10, min_dist=0.0, metric="cosine", random_state=seed).fit(X)
    Z = um.embedding_
    cl = hdbscan.HDBSCAN(min_cluster_size=P["mcs"], min_samples=P["ms"], cluster_selection_method="eom",
                         prediction_data=True).fit(Z)
    return um, cl


def ari_both(a, b):
    from sklearn.metrics import adjusted_rand_score
    m = (a >= 0) & (b >= 0)
    return (adjusted_rand_score(a[m], b[m]) if m.sum() > 1 else float("nan")), int(m.sum())


def top_spans(X, spans, members, n=20):
    c = X[members].mean(0)
    c /= np.linalg.norm(c) + 1e-12
    order = members[np.argsort(-(X[members] @ c))][:n]
    out = []
    for i in order:
        w = spans[i].replace("|", "/").split()
        out.append(" ".join(w[:40]))
    return " | ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", type=int, default=0)
    ap.add_argument("--tasks", default=str(TASKS))
    a = ap.parse_args()
    smoke = a.smoke > 0
    P = dict(nn=15, mcs=10, ms=3, min_pred=5, min_emp=3) if smoke else dict(nn=30, mcs=30, ms=10, min_pred=30, min_emp=10)
    outdir = OUT / "smoke" if smoke else OUT
    outdir.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    df, n_dedup = load_pool(a.tasks)
    n_pool = len(df)
    if smoke:
        df = df.sample(n=min(a.smoke, len(df)), random_state=SEED_POOL).sort_values("task_id").reset_index(drop=True)
    X = get_embeddings(df, smoke, outdir)
    spans = df.span.values
    print(f"pool {len(df)} tasks, {df.employer.nunique()} employers", flush=True)

    # split by posting
    postings = sorted(set(zip(df.ats, df.board_id, df.posting_id)))
    rng = random.Random(SEED_SPLIT)
    rng.shuffle(postings)
    disc_set = set(postings[: len(postings) // 2])
    is_disc = np.array([(a_, b_, c_) in disc_set for a_, b_, c_ in zip(df.ats, df.board_id, df.posting_id)])
    di, hi = np.where(is_disc)[0], np.where(~is_disc)[0]
    Xd, Xh = X[di], X[hi]

    import hdbscan
    um_d, cl_d = run_umap_hdbscan(Xd, UMAP_SEED, P)
    lab_d = cl_d.labels_
    pred_h, _ = hdbscan.approximate_predict(cl_d, um_d.transform(Xh))
    _, cl_h = run_umap_hdbscan(Xh, UMAP_SEED, P)
    lab_h = cl_h.labels_
    ari, n_both = ari_both(pred_h, lab_h)
    print(f"holdout ARI {ari:.3f} on {n_both} points", flush=True)

    rows = []
    hsets = {c: set(np.where(lab_h == c)[0]) for c in set(lab_h) if c >= 0}
    emp_d = df.employer.values[di]
    for c in sorted(set(lab_d) - {-1}):
        mem = np.where(lab_d == c)[0]
        pset = set(np.where(pred_h == c)[0])
        best = max((len(pset & s) / len(pset | s) for s in hsets.values()), default=0.0) if pset else 0.0
        ne = len(set(emp_d[mem]))
        found = bool(len(pset) >= P["min_pred"] and best >= 0.5 and ari >= 0.6 and ne >= P["min_emp"])
        rows.append(dict(cluster_id=c, size_discovery=len(mem), size_holdout_pred=len(pset),
                         best_holdout_jaccard=round(best, 4), n_employers=ne, found=found,
                         top20_central_spans=top_spans(Xd, spans[di], mem)))
    cdf = pd.DataFrame(rows, columns=["cluster_id", "size_discovery", "size_holdout_pred", "best_holdout_jaccard",
                                      "n_employers", "found", "top20_central_spans"])
    cdf.to_csv(outdir / "clusters.csv", index=False)

    asg = df[["task_id", "ats", "board_id", "posting_id", "employer", "group"]].copy()
    asg["half"] = np.where(is_disc, "discovery", "holdout")
    asg["cluster_id"] = -1
    asg.loc[asg.index[di], "cluster_id"] = lab_d
    asg.loc[asg.index[hi], "cluster_id"] = pred_h
    asg["holdout_independent_cluster"] = -2  # -2: not applicable (discovery half); -1: noise
    asg.loc[asg.index[hi], "holdout_independent_cluster"] = lab_h
    asg.to_csv(outdir / "assignments.csv.gz", index=False)

    # noise baseline: full pool, three UMAP seeds
    base = []
    for s in BASELINE_SEEDS:
        _, cl = run_umap_hdbscan(X, s, P)
        base.append(cl.labels_)
        print(f"baseline seed {s}: {len(set(cl.labels_) - {-1})} clusters", flush=True)
    pairs = [(f"{i + 1}-{j + 1}", *ari_both(base[i], base[j])) for i, j in itertools.combinations(range(3), 2)]
    mean_base = float(np.nanmean([p[1] for p in pairs]))

    elapsed = time.time() - t0
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024**3 if sys.platform == "darwin" else 1024**2)
    nf = int(cdf.found.sum())
    pk = ["umap-learn", "hdbscan", "scikit-learn", "numpy", "pandas", "sentence-transformers"]
    md = [f"# Clustering stability{' (SMOKE TEST, not results)' if smoke else ''}", "",
          f"- Holdout ARI (non-noise in both, n={n_both}): **{ari:.4f}** (gate 0.6)",
          "- Noise baseline ARI, full pool, UMAP seeds 1/2/3: " + ", ".join(f"{p[0]} {p[1]:.4f} (n={p[2]})" for p in pairs),
          f"- Baseline mean pairwise ARI: **{mean_base:.4f}**",
          f"- Discovery clusters: {len(cdf)}; found: **{nf}**; not found: **{len(cdf) - nf}**",
          "", "## Pool and split",
          f"- Tasks after performer filter and within-employer dedupe: {n_dedup}; after cap {CAP}/employer: {n_pool}"
          + (f"; smoke sample: {len(df)}" if smoke else ""),
          f"- Postings: {len(postings)}; discovery tasks {len(di)}, holdout tasks {len(hi)}",
          f"- Noise fraction: discovery {np.mean(lab_d < 0):.3f}, holdout independent {np.mean(lab_h < 0):.3f}",
          "", "## Parameters",
          f"- Embedding: {MODEL}, L2-normalised (cache {EMBED.relative_to(ROOT)}/postings.npy)",
          f"- UMAP: n_neighbors {P['nn']}, n_components 10, min_dist 0.0, metric cosine, random_state {UMAP_SEED} "
          f"(discovery and holdout); baseline seeds {list(BASELINE_SEEDS)}",
          f"- HDBSCAN: min_cluster_size {P['mcs']}, min_samples {P['ms']}, eom, prediction_data=True",
          f"- Found rule: predicted holdout size >= {P['min_pred']}, best Jaccard >= 0.5, overall ARI >= 0.6, "
          f"employers >= {P['min_emp']}",
          f"- Seeds: pool cap {SEED_POOL}, posting split {SEED_SPLIT}",
          "", "## Run", f"- Runtime {elapsed:.0f} s; peak RSS {rss:.2f} GiB",
          "- Packages: " + ", ".join(f"{p} {version(p)}" for p in pk if _has(p))]
    (outdir / "stability.md").write_text("\n".join(md) + "\n")
    print("\n".join(md[2:7]), f"\nruntime {elapsed:.0f}s peak RSS {rss:.2f} GiB", flush=True)


def _has(p):
    try:
        version(p)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    main()
