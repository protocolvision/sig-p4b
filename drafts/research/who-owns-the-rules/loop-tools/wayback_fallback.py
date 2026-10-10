"""Fill corpus gaps from existing Internet Archive copies before the browser pass.

For each source in corpus/index.csv whose status is needs-browser or failed, look up the closest existing
snapshot (Wayback availability API), fetch the archived original (id_ form, no toolbar), extract text as
acquire.py does, and set status to ok-wayback. The text header names the snapshot URL and its date, so a
citation can say exactly which copy was read. Sources with no usable snapshot keep their status and go to
the browser pass.

Usage: python3 loop-tools/wayback_fallback.py [--limit N]
"""
import argparse, csv, hashlib, json, sys, time, urllib.parse

from acquire import FIELDS, INDEX, RAW, TEXT, html_text, http_get, pdf_text


def snapshot(url):
    q = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    raw, _, _ = http_get(q, timeout=60)
    closest = json.loads(raw).get("archived_snapshots", {}).get("closest")
    if not closest or closest.get("status") != "200":
        return None, None
    ts = closest["timestamp"]
    return f"https://web.archive.org/web/{ts}id_/{url}", ts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(INDEX, newline="")))
    todo = [r for r in rows if r["status"] in ("needs-browser", "failed") and r["kind"] != "video"]
    if a.limit:
        todo = todo[: a.limit]
    got = 0
    for i, r in enumerate(todo, 1):
        try:
            snap, ts = snapshot(r["url"])
            if snap:
                raw, ctype, _ = http_get(snap, timeout=90)
                ext = ".pdf" if ctype == "application/pdf" else ".html"
                path = RAW / f"{r['id']}{ext}"
                path.write_bytes(raw)
                text = pdf_text(path) if ext == ".pdf" else html_text(raw)
                if text and len(text) > 400:
                    TEXT.joinpath(f"{r['id']}.txt").write_text(
                        f"SOURCE {r['url']}\nSNAPSHOT {snap}\nSNAPSHOT_DATE {ts[:8]}\nKIND {ctype}\n\n{text}")
                    r.update(status="ok-wayback", bytes=len(raw), sha1=hashlib.sha1(raw).hexdigest()[:12],
                             snapshot=snap, note=f"archived copy {ts[:8]}; was {r['status']}: {r['note']}"[:200])
                    got += 1
        except Exception as e:
            r["note"] = (r["note"] + f"; wayback: {str(e)[:60]}")[:200]
        print(f"[{i}/{len(todo)}] {r['status']:13} {r['url'][:90]}", file=sys.stderr)
        if i % 20 == 0 or i == len(todo):
            with open(INDEX, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=FIELDS)
                w.writeheader()
                w.writerows(rows)
        time.sleep(1)
    print(f"recovered {got} of {len(todo)} from archived copies", file=sys.stderr)


if __name__ == "__main__":
    main()
