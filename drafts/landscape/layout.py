#!/usr/bin/env python3
"""Step 3: passages -> embeddings -> 2D map, areas and a density terrain -> data/landscape.json.

- Each reading's cached text is split into ~220-word passages (at most 40 per reading, spread
  evenly), plus one passage made of its title, citation and quote.
- Passages are embedded locally with BAAI/bge-small-en-v1.5 (fastembed, ONNX).
- UMAP projects all passages to 2D. Session readings carry their syllabus area as a weak seed
  (target_weight), so the current orientation shapes the map without dictating it.
- Readings are clustered into areas on their mean embedding; each area is named from the
  seed areas it contains, or flagged for a human name.
- A Gaussian density of the passages becomes the terrain height.
Only titles, links, citations, verified quotes and coordinates are written out, never passage text.
"""
import json, re
from pathlib import Path
import numpy as np
from fastembed import TextEmbedding
import umap
from sklearn.cluster import KMeans
from scipy.ndimage import gaussian_filter

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
CACHE = HERE / "cache"
WORDS, MAX_PASSAGES, GRID = 220, 24, 200
SEED_NAMES = {"swarms": "Swarms", "nature": "Nature coordinates", "records": "Records and logs",
              "boards": "Boards and buses", "people": "People and organisations",
              "firm": "The firm, re-seen", "tending": "Tending the environment"}
SEEDS = list(SEED_NAMES)
N_AREAS = 10
KEEP = 400
# Area names come from an anchor reading, so names survive re-clustering. Unanchored areas get keywords.
ANCHORS = [
    ("Protocol Field Guide v1.1", "Protocols and agents"),
    ("Massed Muddler Intelligence", "Scaling, automation and coordination"),
    ("The Nature of the Firm", "Firms, measurement and governance"),
    ("Aviation Safety Reporting System: program summary", "Safety, reporting and oversight"),
    ("The Log: What every software engineer should know about real-time data's unifying abstraction", "Systems, logs and failures"),
    ("Quorum Sensing in Bacteria", "Biology and information"),
    ("General-Purpose Technologies as Annealing Agents", "Culture, time and soft technologies"),
    ("The Republic of Science", "Science, learning and knowledge"),
    ("Augmenting Human Intellect", "Computing and human augmentation"),
    ("Can Programming Be Liberated", "Programming and coordination languages"),
]
PALETTE = ["#d9e6c3", "#f0d3e3", "#cfe3f0", "#efe0c8", "#cfdcf5", "#f5d9cf", "#d6ecdc", "#e7dcf0", "#f3e6c9", "#d3e9ec", "#ecd6de", "#dfe3c8"]
INK = ["#44621a", "#83325e", "#1c5877", "#6e4a12", "#1f4e9c", "#8a3b22", "#23633a", "#6b3478", "#7a5418", "#1f5f5a", "#7d2f4f", "#4d5a17"]


def passages(r):
    words = (CACHE / "text" / f"{r['id']}.txt").read_text().split()
    head = " ".join(x for x in (r["title"], r.get("cite", ""), r.get("quote", "")) if x)
    chunks = [" ".join(words[i:i + WORDS]) for i in range(0, len(words), WORDS)]
    chunks = [c for c in chunks if len(c.split()) > 60]
    if len(chunks) > MAX_PASSAGES:
        idx = np.linspace(0, len(chunks) - 1, MAX_PASSAGES).round().astype(int)
        chunks = [chunks[i] for i in idx]
    return [head] + chunks


def main():
    corpus = json.loads((DATA / "corpus.json").read_text())
    texts, owner = [], []
    for k, r in enumerate(corpus):
        for p in passages(r):
            texts.append(p); owner.append(k)
    owner = np.array(owner)
    print(f"{len(texts)} passages from {len(corpus)} readings")

    # per-passage cache, so adding a reading only embeds its own passages
    import hashlib
    keys = [hashlib.sha1(t.encode()).hexdigest() for t in texts]
    store = CACHE / "emb_store.npz"
    known = dict(np.load(store)) if store.exists() else {}
    missing = [i for i, k in enumerate(keys) if k not in known]
    if missing:
        model = TextEmbedding("BAAI/bge-small-en-v1.5")
        for i, v in zip(missing, model.embed([texts[i] for i in missing], batch_size=64)):
            known[keys[i]] = np.asarray(v, dtype=np.float32)
        np.savez(store, **known)
    print(f"embedded {len(missing)} new passages")
    E = np.array([known[k] for k in keys], dtype=np.float32)
    E /= np.linalg.norm(E, axis=1, keepdims=True)

    # relevance filter: keep the core (sessions, companions, inventory) and the readings closest to it
    Rall = np.array([E[owner == k].mean(0) for k in range(len(corpus))])
    Rall /= np.linalg.norm(Rall, axis=1, keepdims=True)
    core = [k for k, r in enumerate(corpus) if r["source"] != "readings"]
    S = Rall @ Rall[core].T
    score = np.sort(S, axis=1)[:, -5:].mean(1)
    rest = sorted((k for k in range(len(corpus)) if k not in set(core)), key=lambda k: -score[k])
    keep = sorted(core + rest[:max(0, KEEP - len(core))])
    dropped = [{"title": corpus[k]["title"], "url": corpus[k]["url"], "score": round(float(score[k]), 3)}
               for k in rest[max(0, KEEP - len(core)):]]
    (DATA / "excluded.json").write_text(json.dumps(dropped, ensure_ascii=False, indent=1))
    remap = {k: i for i, k in enumerate(keep)}
    mask = np.isin(owner, keep)
    E, owner = E[mask], np.array([remap[o] for o in owner[mask]])
    corpus = [corpus[k] for k in keep]
    print(f"kept {len(corpus)} readings ({len(dropped)} excluded as off-topic), {len(E)} passages")

    # weak seed: passages of session readings carry their syllabus area
    y = np.array([SEEDS.index(corpus[o]["seed"]) if corpus[o].get("seed") else -1 for o in owner])
    reducer = umap.UMAP(n_neighbors=15, min_dist=0.35, metric="cosine", target_weight=0.2,
                        target_metric="categorical", random_state=7)
    XY = reducer.fit_transform(E, y=y)
    lo, hi = np.percentile(XY, 2, axis=0), np.percentile(XY, 98, axis=0)
    XY = np.clip((XY - lo) / (hi - lo), -0.04, 1.04)  # robust 0..1, outliers pulled to the edge
    XY = 0.08 + (XY + 0.04) / 1.08 * 0.84

    # reading-level embeddings and positions
    R = np.array([E[owner == k].mean(0) for k in range(len(corpus))])
    R /= np.linalg.norm(R, axis=1, keepdims=True)
    RXY = np.array([np.median(XY[owner == k], 0) for k in range(len(corpus))])
    np.save(CACHE / "reading_emb.npy", R)

    # areas: cluster readings on their embedding
    labels = KMeans(n_clusters=N_AREAS, n_init=50, random_state=7).fit_predict(np.hstack([R, 0.9 * RXY]))
    areas, used = [], set()
    for a in range(N_AREAS):
        members = [k for k in range(len(corpus)) if labels[k] == a]
        titles = {corpus[k]["title"] for k in members}
        name = None
        for anchor, nm in ANCHORS:
            if nm not in used and any(t.startswith(anchor[:40]) for t in titles):
                name = nm; used.add(nm); break
        if not name:
            words = re.findall(r"[A-Za-z]{5,}", " ".join(corpus[k]["title"] for k in members).lower())
            common = [w for w in sorted(set(words), key=words.count, reverse=True)
                      if w not in {"about", "their", "which", "protocol", "protocols"}][:3]
            name = "Unnamed: " + ", ".join(common)
        areas.append({"id": a, "name": name, "count": len(members), "color": PALETTE[a], "ink": INK[a],
                      "x": float(RXY[members, 0].mean()), "y": float(RXY[members, 1].mean())})

    # terrain: passage density, smoothed
    # every reading contributes equal mass, so long texts don't dominate the terrain
    counts = np.bincount(owner)
    H, _, _ = np.histogram2d(XY[:, 1], XY[:, 0], bins=GRID, range=[[0, 1], [0, 1]], weights=1.0 / counts[owner])
    H = gaussian_filter(H, sigma=GRID / 34)
    H = (H / H.max()) ** 0.65
    # area of each grid cell = area of nearest reading
    gx, gy = np.meshgrid((np.arange(GRID) + .5) / GRID, (np.arange(GRID) + .5) / GRID)
    cells = np.stack([gx.ravel(), gy.ravel()], 1)
    d = ((cells[:, None, :] - RXY[None, :, :]) ** 2).sum(-1)
    A = labels[d.argmin(1)].reshape(GRID, GRID)

    readings = []
    for k, r in enumerate(corpus):
        pts = XY[owner == k]
        readings.append({"id": r["id"], "title": r["title"], "url": r["url"], "cite": r.get("cite", ""),
                         "year": r.get("year"), "quote": r.get("quote", ""), "source": r["source"],
                         "session": r.get("session"), "read": bool(r.get("read")), "area": int(labels[k]),
                         "x": round(float(RXY[k, 0]), 4), "y": round(float(RXY[k, 1]), 4),
                         "p": [[round(float(a), 4), round(float(b), 4)] for a, b in pts]})
    dates = [s["date"] for s in json.loads((HERE / "planned_arc.json").read_text())]
    for r in readings:
        if r["session"]:
            r["date"] = dates[r["session"] - 1]
    route = [r["id"] for r in sorted((r for r in readings if r["session"]), key=lambda r: r["session"])]
    sig = [r for r in readings if r["source"] == "inventory" and "Protocolized" in r["cite"]]
    dest = {"x": round(float(np.mean([r["x"] for r in sig])), 4), "y": round(float(np.mean([r["y"] for r in sig])), 4)}
    out = {"grid": GRID, "height": [round(float(v), 3) for v in H.ravel()],
           "areaGrid": A.ravel().tolist(), "areas": areas, "readings": readings,
           "route": route, "dest": dest}
    (DATA / "landscape.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")))
    print("areas:", [(a["name"], a["count"]) for a in areas])
    print("written data/landscape.json", round((DATA / "landscape.json").stat().st_size / 1024), "KB")


if __name__ == "__main__":
    main()
