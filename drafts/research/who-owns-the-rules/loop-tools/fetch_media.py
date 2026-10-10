"""Fetch transcripts for a stratified random sample of the media frames (loop-design-v2.md, section 5).

Run on a machine with open network access (the cloud sandbox blocks most hosts).
Needs: yt-dlp on PATH for YouTube captions; Python 3.9+.

Usage:
  python3 fetch_media.py FRAME.csv --per-function 4 --seed 20261010 [--dry-run]

Writes plain-text transcripts to sources-v2/transcripts/<id>.txt (ignored by git: they are other
people's work) and a manifest, sources-v2/transcripts/manifest.csv, listing what was fetched, what
failed and what needs manual transcription. Commit only extracted records, never transcripts.
"""
import argparse, csv, html, pathlib, random, re, subprocess, sys, tempfile, urllib.request
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "sources-v2" / "transcripts"


def sample(rows, per_function, seed, group="function"):
    """Stratified random sample: per_function items per group, at most two per show,
    at most a third from vendors or consultants."""
    rng = random.Random(seed)
    by = defaultdict(list)
    for r in rows:
        by[r.get(group) or "unknown"].append(r)
    picked = []
    for g in sorted(by):
        items = by[g][:]
        rng.shuffle(items)
        shows, vendors, chosen = defaultdict(int), 0, []
        for r in items:
            show = r.get("show_or_channel") or r.get("show_or_event") or ""
            if shows[show] >= 2:
                continue
            is_vendor = r.get("vendor_or_consultant") == "yes"
            if is_vendor and vendors + 1 > per_function / 3:
                continue
            chosen.append(r)
            shows[show] += 1
            vendors += is_vendor
            if len(chosen) == per_function:
                break
        picked += chosen
    return picked


def youtube(url, dest):
    with tempfile.TemporaryDirectory() as tmp:
        cmd = ["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", "en.*",
               "--sub-format", "vtt", "-o", f"{tmp}/%(id)s.%(ext)s", url]
        subprocess.run(cmd, check=True, capture_output=True, timeout=180)
        vtts = list(pathlib.Path(tmp).glob("*.vtt"))
        if not vtts:
            raise RuntimeError("no captions")
        lines, last = [], None
        for line in vtts[0].read_text(errors="ignore").splitlines():
            if "-->" in line:
                stamp = line.split(" --> ")[0].split(".")[0]
                continue
            text = re.sub(r"<[^>]+>", "", line).strip()
            if not text or text == last or text.startswith(("WEBVTT", "Kind:", "Language:")):
                continue
            lines.append(f"[{stamp}] {text}")
            last = text
        dest.write_text("\n".join(lines))


def page(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research transcript fetch)"})
    raw = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", errors="ignore")
    raw = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", raw)
    text = html.unescape(re.sub(r"(?s)<[^>]+>", "\n", raw))
    text = "\n".join(l.strip() for l in text.splitlines() if l.strip())
    dest.write_text(f"SOURCE {url}\n\n{text}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("frame")
    ap.add_argument("--per-function", type=int, default=4)
    ap.add_argument("--seed", type=int, default=20261010)
    ap.add_argument("--group", default=None, help="column to stratify by (default: function, or role for the historical frame)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.frame, newline="")))
    group = a.group or ("function" if "function" in rows[0] else "role")
    picked = sample(rows, a.per_function, a.seed, group)
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = OUT / "manifest.csv"
    new = not manifest.exists()
    with open(manifest, "a", newline="") as mf:
        w = csv.writer(mf)
        if new:
            w.writerow(["id", "url", "status", "note"])
        for r in picked:
            dest = OUT / f"{r['id']}.txt"
            if a.dry_run:
                print(r["id"], r.get(group), r["url"])
                continue
            if dest.exists():
                w.writerow([r["id"], r["url"], "exists", ""])
                continue
            try:
                if "youtube.com" in r["url"] or "youtu.be" in r["url"]:
                    youtube(r["url"], dest)
                elif r.get("transcript") == "page":
                    page(r["url"], dest)
                else:
                    w.writerow([r["id"], r["url"], "manual", "no transcript source; transcribe audio"])
                    continue
                w.writerow([r["id"], r["url"], "ok", dest.name])
            except Exception as e:  # keep going; the manifest records failures
                w.writerow([r["id"], r["url"], "failed", str(e)[:200]])
    print(f"{len(picked)} items sampled from {len(rows)}; manifest: {manifest}", file=sys.stderr)


if __name__ == "__main__":
    main()
