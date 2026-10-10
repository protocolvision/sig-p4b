"""Acquire the research corpus: download every source in corpus/manifest.csv and extract text.

Run on a machine with open network access. Needs Python 3.9+, and for full coverage yt-dlp (video and
podcast captions) and pdftotext (poppler). Sources that need a logged-in or JavaScript browser are listed
as `needs-browser`; save those by hand or with a browser agent to corpus/text/<id>.txt.

Usage:
  python3 acquire.py [--category CAT] [--kind KIND] [--wayback] [--limit N] [--retry-failed]

Writes:
  corpus/raw/<id>.<ext>   the file as fetched           (ignored by git: other people's work)
  corpus/text/<id>.txt    extracted text, with a header  (ignored by git)
  corpus/index.csv        one row per source: status, bytes, sha1, fetched, final_url, snapshot (committed)
"""
import argparse, csv, hashlib, html, pathlib, re, shutil, subprocess, sys, tempfile, time, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
CORPUS = HERE.parent / "corpus"
RAW, TEXT, INDEX = CORPUS / "raw", CORPUS / "text", CORPUS / "index.csv"
UA = {"User-Agent": "Mozilla/5.0 (Protocols for Business research corpus; protocolsforbusiness.com)"}
FIELDS = ["id", "category", "kind", "url", "status", "bytes", "sha1", "fetched", "final_url", "snapshot", "note"]


def http_get(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get_content_type(), r.geturl()


def html_text(raw):
    s = raw.decode("utf-8", errors="ignore")
    s = re.sub(r"(?is)<(script|style|nav|header|footer|noscript|svg)[^>]*>.*?</\1>", " ", s)
    s = html.unescape(re.sub(r"(?s)<[^>]+>", "\n", s))
    return "\n".join(l.strip() for l in s.splitlines() if l.strip())


def pdf_text(path):
    if not shutil.which("pdftotext"):
        return None
    out = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, timeout=120)
    return out.stdout.decode("utf-8", errors="ignore")


def captions(url):
    if not shutil.which("yt-dlp"):
        raise RuntimeError("yt-dlp not installed")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", "en.*",
                        "--sub-format", "vtt", "-o", f"{tmp}/%(id)s.%(ext)s", url],
                       check=True, capture_output=True, timeout=300)
        vtts = sorted(pathlib.Path(tmp).glob("*.vtt"))
        if not vtts:
            raise RuntimeError("no captions")
        lines, last, stamp = [], None, ""
        for line in vtts[0].read_text(errors="ignore").splitlines():
            if "-->" in line:
                stamp = line.split(" --> ")[0].split(".")[0]
                continue
            t = re.sub(r"<[^>]+>", "", line).strip()
            if t and t != last and not t.startswith(("WEBVTT", "Kind:", "Language:")):
                lines.append(f"[{stamp}] {t}")
                last = t
        return "\n".join(lines)


def wayback(url):
    try:
        req = urllib.request.Request("https://web.archive.org/save/" + url, headers=UA)
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.geturl()
    except Exception as e:
        return f"failed: {str(e)[:100]}"


def acquire(row, use_wayback):
    sid, url = row["id"], row["url"]
    today = time.strftime("%Y-%m-%d")
    rec = {k: row.get(k, "") for k in ("id", "category", "kind", "url")}
    rec.update(status="", bytes="", sha1="", fetched=today, final_url="", snapshot="", note="")
    try:
        if row["kind"] == "video":
            text = captions(url)
            (TEXT / f"{sid}.txt").write_text(f"SOURCE {url}\nFETCHED {today}\nKIND captions\n\n{text}")
            rec.update(status="ok", bytes=len(text), sha1=hashlib.sha1(text.encode()).hexdigest()[:12], note="captions")
        else:
            raw, ctype, final = http_get(url)
            ext = ".pdf" if ctype == "application/pdf" else ".html"
            path = RAW / f"{sid}{ext}"
            path.write_bytes(raw)
            text = pdf_text(path) if ext == ".pdf" else html_text(raw)
            if text and len(text) > 400:
                (TEXT / f"{sid}.txt").write_text(f"SOURCE {final}\nFETCHED {today}\nKIND {ctype}\n\n{text}")
                rec.update(status="ok")
            else:
                rec.update(status="needs-browser", note="little text extracted; likely JavaScript or login")
            rec.update(bytes=len(raw), sha1=hashlib.sha1(raw).hexdigest()[:12], final_url=final)
    except urllib.error.HTTPError as e:
        rec.update(status="needs-browser" if e.code in (401, 403, 429) else "failed", note=f"HTTP {e.code}")
    except Exception as e:
        rec.update(status="failed", note=str(e)[:150])
    if use_wayback and rec["status"] in ("ok", "needs-browser") and row["kind"] != "video":
        rec["snapshot"] = wayback(url)
    return rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category")
    ap.add_argument("--kind")
    ap.add_argument("--wayback", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--retry-failed", action="store_true")
    a = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    TEXT.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(CORPUS / "manifest.csv", newline="")))
    done = {r["id"]: r for r in csv.DictReader(open(INDEX, newline=""))} if INDEX.exists() else {}
    todo = [r for r in rows
            if (not a.category or r["category"] == a.category) and (not a.kind or r["kind"] == a.kind)
            and (r["id"] not in done or (a.retry_failed and done[r["id"]]["status"] != "ok"))]
    if a.limit:
        todo = todo[: a.limit]
    for i, r in enumerate(todo, 1):
        done[r["id"]] = acquire(r, a.wayback)
        print(f"[{i}/{len(todo)}] {done[r['id']]['status']:13} {r['url'][:90]}", file=sys.stderr)
        if i % 20 == 0 or i == len(todo):
            with open(INDEX, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=FIELDS)
                w.writeheader()
                w.writerows(sorted(done.values(), key=lambda x: x["id"]))
        time.sleep(0.5)
    from collections import Counter
    print(Counter(d["status"] for d in done.values()), file=sys.stderr)


if __name__ == "__main__":
    main()
