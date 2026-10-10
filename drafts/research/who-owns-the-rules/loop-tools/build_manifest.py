"""Build corpus/manifest.csv: every source URL cited anywhere in the research, plus the planned additions.

Usage: python3 build_manifest.py
Re-run after any research file changes. IDs are stable (hash of the URL), so re-running never renumbers.
"""
import csv, hashlib, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
PAT = re.compile(r"https?://[^\s)\]\"'<>,|`]+")
SKIP_DIRS = {"archive", "transcripts", "raw", "text", "corpus", "report", "loop-tools", "loop-prompts"}

CATEGORY = [
    ("results/loop-2026-10-10/ledger", "activity-evidence"),
    ("factsheets", "industry-factsheet"),
    ("timeline-", "industry-timeline"),
    ("counterexamples", "industry-check"),
    ("gatekeepers", "industry-check"),
    ("roles/", "role-library"),
    ("media-current", "media-current"),
    ("media-historical", "media-historical"),
    ("exploratory/", "exploratory"),
]


def category(path):
    s = str(path)
    for key, cat in CATEGORY:
        if key in s:
            return cat
    return "other"


def kind(url):
    u = url.lower()
    if "youtube.com" in u or "youtu.be" in u:
        return "video"
    if any(h in u for h in ("podcasts.apple.com", "open.spotify.com", "podbean", "buzzsprout", "libsyn", "transistor.fm", "simplecast")):
        return "podcast"
    if u.endswith(".pdf") or "/pdf/" in u:
        return "pdf"
    if any(h in u for h in ("greenhouse.io", "lever.co", "ashbyhq.com", "myworkdayjobs.com", "icims.com", "linkedin.com/jobs", "indeed.com", "ziprecruiter", "builtin", "glassdoor")):
        return "job-posting"
    return "html"


def main():
    rows = {}
    for p in sorted(ROOT.rglob("*")):
        if p.is_dir() or SKIP_DIRS & set(p.relative_to(ROOT).parts) or p.suffix not in (".md", ".csv", ".jsonl", ".json"):
            continue
        urls = PAT.findall(p.read_text(errors="ignore"))
        if p.suffix == ".csv":  # read url columns whole, so URLs with spaces survive
            with open(p, newline="") as f:
                rd = csv.DictReader(f)
                if rd.fieldnames and "url" in rd.fieldnames:
                    urls = [r["url"].strip().replace(" ", "%20") for r in rd if (r.get("url") or "").startswith("http")]
        for u in urls:
            u = u.rstrip(".;:")
            if u in rows:
                rows[u]["cited_in"] += 1
                continue
            rows[u] = {
                "id": "C" + hashlib.sha1(u.encode()).hexdigest()[:8],
                "category": category(p.relative_to(ROOT)),
                "kind": kind(u),
                "url": u,
                "first_cited_in": str(p.relative_to(ROOT)),
                "cited_in": 1,
            }
    planned = ROOT / "corpus" / "planned.csv"
    if planned.exists():
        for r in csv.DictReader(open(planned, newline="")):
            u = r["url"].strip()
            if u and u not in rows:
                rows[u] = {"id": "C" + hashlib.sha1(u.encode()).hexdigest()[:8], "category": r["category"],
                           "kind": kind(u), "url": u, "first_cited_in": "corpus/planned.csv", "cited_in": 0}
    out = ROOT / "corpus" / "manifest.csv"
    out.parent.mkdir(exist_ok=True)
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "category", "kind", "url", "first_cited_in", "cited_in"])
        w.writeheader()
        w.writerows(sorted(rows.values(), key=lambda r: (r["category"], r["id"])))
    print(f"{len(rows)} sources -> {out}")


if __name__ == "__main__":
    main()
