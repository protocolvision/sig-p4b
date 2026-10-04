# Reading landscape (draft)

A 3D map of the group's readings. Each point is a passage of a reading, placed by what it says; the terrain
rises where readings cluster; the year's route runs through it. Preview (with the repo's local server
running): http://localhost:8000/drafts/landscape/explorer/

Pipeline, run from this folder with the local venv (`uv venv --python 3.12 .venv` and
`uv pip install --python .venv/bin/python fastembed umap-learn scikit-learn scipy numpy trafilatura requests`):

1. `python corpus.py` (add `--full` for all ~490 readings) → `data/corpus.json`
2. `.venv/bin/python fetch.py` → `cache/text/` (gitignored; passage text never ships)
3. `.venv/bin/python layout.py` → `data/landscape.json` (passages embedded locally with bge-small, UMAP
   seeded weakly by the current syllabus areas, k-means areas named by anchor readings, density terrain)

The explorer (`explorer/`) loads three.js from jsDelivr and reads `data/landscape.json` and
`tools/sessions.json` dates. Not deployed: `deploy.sh` excludes `drafts/`.
