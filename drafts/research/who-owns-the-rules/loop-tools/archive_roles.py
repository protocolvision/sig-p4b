"""Download and archive the job descriptions and capability models listed in the role library.

Run on a machine with open network access (the cloud sandbox blocks these hosts).

Usage:
  python3 archive_roles.py [--wayback] [--only ROLE] [--dry-run]

Reads roles/sources-*.csv (columns: role,type,title,owner,date,url,grade). For each URL it saves the
page as fetched (HTML or PDF) and a plain-text copy under roles/archive/<role>/, and records the result
in roles/archive/manifest.csv. With --wayback it also asks the Internet Archive to save the page and
records the snapshot URL, so a public, citable copy survives after a posting is taken down.

roles/archive/ is ignored by git: postings and exam guides are other people's text. Commit the manifest
summary (archive_status.csv, written next to the source lists) instead; cite the snapshot URLs.
"""
import argparse, csv, hashlib, html, pathlib, re, sys, time, urllib.request

HERE = pathlib.Path(__file__).resolve().parent
ROLES = HERE.parent / "roles"
OUT = ROLES / "archive"
UA = {"User-Agent": "Mozilla/5.0 (research archive; protocolsforbusiness.com)"}


def fetch(url, timeout=60):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get_content_type(), r.geturl()


def to_text(raw, ctype):
    if ctype == "application/pdf":
        return None  # keep the PDF; extract text later with pdftotext if needed
    s = raw.decode("utf-8", errors="ignore")
    s = re.sub(r"(?is)<(script|style|nav|header|footer|noscript)[^>]*>.*?</\1>", " ", s)
    s = html.unescape(re.sub(r"(?s)<[^>]+>", "\n", s))
    return "\n".join(l.strip() for l in s.splitlines() if l.strip())


def wayback(url):
    try:
        req = urllib.request.Request("https://web.archive.org/save/" + url, headers=UA)
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.geturl()
    except Exception as e:  # the save endpoint rate-limits; record and move on
        return f"failed: {str(e)[:120]}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wayback", action="store_true")
    ap.add_argument("--only")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    rows = []
    for f in sorted(ROLES.glob("sources-*.csv")):
        rows += list(csv.DictReader(open(f, newline="")))
    if a.only:
        rows = [r for r in rows if r["role"] == a.only]
    OUT.mkdir(parents=True, exist_ok=True)
    status = []
    for r in rows:
        url = r["url"].strip()
        if not url.startswith("http"):
            status.append({**r, "status": "no url", "saved_as": "", "snapshot": ""})
            continue
        key = hashlib.sha1(url.encode()).hexdigest()[:10]
        d = OUT / r["role"]
        if a.dry_run:
            print(r["role"], r["type"], url)
            continue
        d.mkdir(parents=True, exist_ok=True)
        try:
            raw, ctype, final = fetch(url)
            ext = ".pdf" if ctype == "application/pdf" else ".html"
            (d / f"{r['type']}-{key}{ext}").write_bytes(raw)
            text = to_text(raw, ctype)
            if text:
                (d / f"{r['type']}-{key}.txt").write_text(f"SOURCE {final}\nFETCHED {time.strftime('%Y-%m-%d')}\n\n{text}")
            st = "ok"
        except Exception as e:
            st = f"failed: {str(e)[:120]}"
            ext = ""
        snap = wayback(url) if a.wayback else ""
        status.append({**r, "status": st, "saved_as": f"{r['type']}-{key}{ext}" if st == "ok" else "", "snapshot": snap})
        time.sleep(1)
    if status:
        fields = list(status[0].keys())
        for name in (OUT / "manifest.csv", ROLES / "archive_status.csv"):
            with open(name, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=fields)
                w.writeheader()
                w.writerows(status)
        ok = sum(s["status"] == "ok" for s in status)
        print(f"{ok} of {len(status)} saved; see {ROLES / 'archive_status.csv'}", file=sys.stderr)


if __name__ == "__main__":
    main()
