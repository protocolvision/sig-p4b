"""Data-driven check for the controls atlas taxonomy (design Phase 2, step 3).

Embeds each control's name + object + mechanism with all-mpnet-base-v2 (local), reduces with UMAP (cosine, 10 dims,
seed 42) and clusters with HDBSCAN (min_cluster_size 15). Writes embed-clusters.csv (control_id, cluster) and
embed-clusters.md (cluster sizes and the 8 most central control names per cluster). A 2D projection is saved for the report.
"""
import pathlib, json
import numpy as np, pandas as pd
HERE = pathlib.Path(__file__).resolve().parent
df = pd.read_csv(HERE / "inventory-all.csv").fillna("")
text = (df.control_name + ". " + df.object + ". " + df.mechanism).tolist()
from sentence_transformers import SentenceTransformer
import torch
dev = "mps" if torch.backends.mps.is_available() else "cpu"
X = SentenceTransformer("sentence-transformers/all-mpnet-base-v2", device=dev).encode(text, batch_size=128, normalize_embeddings=True, convert_to_numpy=True)
import umap, hdbscan
Z = umap.UMAP(n_neighbors=20, n_components=10, min_dist=0.0, metric="cosine", random_state=42).fit_transform(X)
cl = hdbscan.HDBSCAN(min_cluster_size=15, min_samples=5).fit_predict(Z)
Z2 = umap.UMAP(n_neighbors=20, n_components=2, min_dist=0.15, metric="cosine", random_state=42).fit_transform(X)
Z2 = (Z2 - Z2.min(0)) / (Z2.max(0) - Z2.min(0))
df["cluster"] = cl; df["x"] = Z2[:, 0].round(4); df["y"] = Z2[:, 1].round(4)
df[["control_id", "cluster", "x", "y"]].to_csv(HERE / "embed-clusters.csv", index=False)
out = ["# Embedding clusters (data-driven check)", "", f"{len(df)} controls; {len(set(cl)) - (1 if -1 in cl else 0)} clusters; noise {int((cl == -1).sum())}.", ""]
for c in sorted(set(cl)):
    if c == -1: continue
    m = np.where(cl == c)[0]; cen = X[m].mean(0); cen /= np.linalg.norm(cen)
    top = m[np.argsort(-(X[m] @ cen))][:8]
    out.append(f"- **{c}** ({len(m)}; {df.iloc[m]['product'].nunique()} products): " + " | ".join(df.iloc[top]['control_name'].str.slice(0, 60)))
(HERE / "embed-clusters.md").write_text("\n".join(out))
print("\n".join(out[:4]))
