# Clustering stability (SMOKE TEST, not results)

- Holdout ARI (non-noise in both, n=690): **0.6069** (gate 0.6)
- Noise baseline ARI, full pool, UMAP seeds 1/2/3: 1-2 0.9011 (n=2706), 1-3 0.7200 (n=2723), 2-3 0.7441 (n=2835)
- Baseline mean pairwise ARI: **0.7884**
- Discovery clusters: 71; found: **2**; not found: **69**

## Pool and split
- Tasks after performer filter and within-employer dedupe: 116207; after cap 300/employer: 33172; smoke sample: 5000
- Postings: 3380; discovery tasks 2531, holdout tasks 2469
- Noise fraction: discovery 0.297, holdout independent 0.345

## Parameters
- Embedding: sentence-transformers/all-mpnet-base-v2, L2-normalised (cache corpus/b-raw/embed/postings.npy)
- UMAP: n_neighbors 15, n_components 10, min_dist 0.0, metric cosine, random_state 42 (discovery and holdout); baseline seeds [1, 2, 3]
- HDBSCAN: min_cluster_size 10, min_samples 3, eom, prediction_data=True
- Found rule: predicted holdout size >= 5, best Jaccard >= 0.5, overall ARI >= 0.6, employers >= 3
- Seeds: pool cap 20261024, posting split 20261011

## Run
- Runtime 130 s; peak RSS 0.52 GiB
- Packages: umap-learn 0.5.7, hdbscan 0.8.40, scikit-learn 1.6.1, numpy 2.2.3, pandas 2.2.3, sentence-transformers 3.4.1
