"""Embed extracted task spans locally (triangulation-design.md, section 5).

Embeddings are cached by span text (SHA-1 of the normalised span), so rerunning after more postings are
extracted only embeds new spans. Model: sentence-transformers/all-mpnet-base-v2, run locally (MPS when
available). Output: corpus/b-raw/embed/<name>.npy (float32, L2-normalised) and <name>.keys.json (span hashes
in row order).

Usage (analytics venv): .venv/bin/python embed_tasks.py TASKS.jsonl [TASKS2.jsonl ...] --name postings
"""
import argparse, hashlib, json, pathlib, re

import numpy as np
from sentence_transformers import SentenceTransformer

OUT = pathlib.Path(__file__).resolve().parent.parent / "corpus" / "b-raw" / "embed"
MODEL = "sentence-transformers/all-mpnet-base-v2"


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def key(s):
    return hashlib.sha1(norm(s).lower().encode()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tasks", nargs="+")
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    npy, kfile = OUT / f"{a.name}.npy", OUT / f"{a.name}.keys.json"
    keys = json.loads(kfile.read_text()) if kfile.exists() else []
    vecs = np.load(npy) if npy.exists() else np.zeros((0, 768), dtype="float32")
    have = set(keys)
    new = {}
    for path in a.tasks:
        for line in open(path):
            span = json.loads(line)["span"]
            k = key(span)
            if k not in have and k not in new:
                new[k] = norm(span)
    print(f"{len(have)} cached, {len(new)} new spans", flush=True)
    if new:
        model = SentenceTransformer(MODEL, device="mps")
        texts = list(new.values())
        emb = model.encode(texts, batch_size=256, show_progress_bar=False, normalize_embeddings=True,
                           convert_to_numpy=True).astype("float32")
        vecs = np.vstack([vecs, emb])
        keys += list(new.keys())
        np.save(npy, vecs)
        kfile.write_text(json.dumps(keys))
    print(f"total {len(keys)} embeddings, model {MODEL}", flush=True)


if __name__ == "__main__":
    main()
