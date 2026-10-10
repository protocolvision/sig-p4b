# Clustering stability

- Holdout ARI (non-noise in both, n=9482): **0.0168** (gate 0.6)
- Noise baseline ARI, full pool, UMAP seeds 1/2/3: 1-2 0.8344 (n=19812), 1-3 0.8366 (n=19394), 2-3 0.9181 (n=19327)
- Baseline mean pairwise ARI: **0.8630**
- Discovery clusters: 89; found: **0**; not found: **89**

## Pool and split
- Tasks after performer filter and within-employer dedupe: 213938; after cap 300/employer: 50675
- Postings: 14079; discovery tasks 25122, holdout tasks 25553
- Noise fraction: discovery 0.522, holdout independent 0.000

## Parameters
- Embedding: sentence-transformers/all-mpnet-base-v2, L2-normalised (cache corpus/b-raw/embed/postings.npy)
- UMAP: n_neighbors 30, n_components 10, min_dist 0.0, metric cosine, random_state 42 (discovery and holdout); baseline seeds [1, 2, 3]
- HDBSCAN: min_cluster_size 30, min_samples 10, eom, prediction_data=True
- Found rule: predicted holdout size >= 30, best Jaccard >= 0.5, overall ARI >= 0.6, employers >= 10
- Seeds: pool cap 20261024, posting split 20261011

## Run
- Runtime 240 s; peak RSS 2.02 GiB
- Packages: umap-learn 0.5.7, hdbscan 0.8.40, scikit-learn 1.6.1, numpy 2.2.3, pandas 2.2.3, sentence-transformers 3.4.1
