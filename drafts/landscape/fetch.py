#!/usr/bin/env python3
"""Step 2: fetch each reading's openly available text -> cache/text/<id>.txt (gitignored).

HTML goes through trafilatura, PDFs through pdftotext. When a page is blocked or empty, the
reading falls back to its title, citation, quote and excerpt. Text never leaves the cache:
only positions computed from it are published.
"""
import json, re, subprocess, tempfile, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests, trafilatura

HERE = Path(__file__).resolve().parent
CACHE = HERE / "cache/text"
CACHE.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"}
MAX_WORDS = 15000


def fallback(r):
    return "\n".join(x for x in (r["title"], r.get("cite", ""), r.get("quote", ""), r.get("excerpt", "")) if x)


def openalex_abstract(r):
    m = re.search(r"(10\.\d{4,9}/[^\s?#]+)", r["url"])
    ssrn = re.search(r"ssrn\.com/.*abstract_id=(\d+)", r["url"])
    doi = m.group(1) if m else (f"10.2139/ssrn.{ssrn.group(1)}" if ssrn else "")
    if not doi:
        return ""
    try:
        w = requests.get(f"https://api.openalex.org/works/doi:{doi}", timeout=25).json()
    except Exception:
        return ""
    inv = w.get("abstract_inverted_index") or {}
    pos = {i: word for word, ii in inv.items() for i in ii}
    return " ".join(pos[i] for i in sorted(pos))


def fetch(r):
    out = CACHE / f"{r['id']}.txt"
    if out.exists() and "--refresh" not in sys.argv:
        return r["id"], "cached", len(out.read_text().split())
    text, how = "", "fallback"
    if r.get("local_pdf") and Path(r["local_pdf"]).exists():
        text = subprocess.run(["pdftotext", "-q", r["local_pdf"], "-"], capture_output=True, text=True, timeout=60).stdout
        out.write_text(" ".join(text.split()[:MAX_WORDS]))
        return r["id"], "local-pdf", min(len(text.split()), MAX_WORDS)
    try:
        resp = requests.get(r["url"], headers=UA, timeout=25, allow_redirects=True)
        ctype = resp.headers.get("content-type", "")
        if resp.ok and ("pdf" in ctype or resp.content[:4] == b"%PDF"):
            with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
                f.write(resp.content); f.flush()
                text = subprocess.run(["pdftotext", "-q", f.name, "-"], capture_output=True, text=True, timeout=60).stdout
            how = "pdf"
        elif resp.ok:
            text = trafilatura.extract(resp.text, include_comments=False, include_tables=False) or ""
            how = "html"
    except Exception as e:  # network errors fall back to metadata
        how = f"error:{type(e).__name__}"
    words = text.split()
    if len(words) < 150:  # blocked or thin page: try the paper's abstract from OpenAlex when the link is a DOI
        text = (text + "\n" + openalex_abstract(r)).strip()
        words = text.split()
    if len(words) < 150:
        text, how = fallback(r) + ("\n" + text if text else ""), how + "+fallback"
        words = text.split()
    out.write_text(" ".join(words[:MAX_WORDS]))
    return r["id"], how, min(len(words), MAX_WORDS)


def main():
    corpus = json.loads((HERE / "data/corpus.json").read_text())
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(fetch, corpus))
    status = {i: {"how": h, "words": w} for i, h, w in results}
    (HERE / "data/fetch_status.json").write_text(json.dumps(status, indent=1))
    full = sum(1 for s in status.values() if "fallback" not in s["how"])
    print(f"{full}/{len(status)} readings with full text; {sum(s['words'] for s in status.values())} words total")


if __name__ == "__main__":
    main()
