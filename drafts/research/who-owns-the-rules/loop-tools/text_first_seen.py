#!/usr/bin/env python3
"""Find the earliest Wayback snapshot of a URL that contains a phrase.
usage: text_first_seen.py URL "key phrase" [--from 2020]
Lists monthly 200-status captures (CDX collapse=timestamp:6), then binary-searches
(id_ form) assuming that once the phrase appears it stays. Also checks the latest
snapshot first; if absent there, prints 'not in archive'. Standard library only."""
import sys, re, json, time, html, urllib.request, urllib.parse

def get(url, tries=6, timeout=60):
    delay = 5
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception as e:
            err = e
            time.sleep(delay); delay *= 2
    raise RuntimeError("fetch failed: %s %s" % (url, err))

def norm(t):
    t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t).replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", t).lower()

def captures(url, since):
    q = ("https://web.archive.org/cdx/search/cdx?url=%s&output=json&from=%s"
         "&filter=statuscode:200&collapse=timestamp:6" % (urllib.parse.quote(url, safe=":/"), since))
    d = json.loads(get(q) or "[]")
    return [r[1] for r in d[1:]]

def has(ts, url, phrase):
    """True/False if fetched; None if the fetch failed after retries (not treated as absence)."""
    time.sleep(1.5)
    try:
        return phrase in norm(get("https://web.archive.org/web/%sid_/%s" % (ts, url)))
    except RuntimeError:
        return None

def main():
    url, phrase = sys.argv[1], norm(sys.argv[2]).strip()
    since = sys.argv[sys.argv.index("--from") + 1] if "--from" in sys.argv else "2020"
    caps = captures(url, since)
    if not caps:
        print("not in archive\tno captures"); return
    r = has(caps[-1], url, phrase)
    if r is None:
        print("lookup failed\tlatest capture %s could not be fetched" % caps[-1]); return
    if r is False:
        print("not in archive\tlatest capture %s lacks phrase" % caps[-1]); return
    lo, hi = 0, len(caps) - 1          # hi known to contain phrase
    failed = False
    while lo < hi:
        mid = (lo + hi) // 2
        r = has(caps[mid], url, phrase)
        if r is True: hi = mid
        elif r is False: lo = mid + 1
        else:                           # fetch failure: try the next snapshot instead
            failed = True
            r2 = has(caps[mid + 1], url, phrase) if mid + 1 < hi else None
            if r2 is True: hi = mid + 1
            else: lo = mid + 1
    print("%s\thttps://web.archive.org/web/%sid_/%s%s" % (caps[hi], caps[hi], url, "  [some fetches failed: date may be late]" if failed else ""))

if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        print("lookup failed\t%s" % str(e)[-120:])
