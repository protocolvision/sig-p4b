"""Corpus B, design 4.2: SEC filings (10-K, 10-Q) that use agent-related phrases, plus a 10-K denominator.

Standard library only. Resumable: every stage skips work already on disk. Stays under 5 requests/sec.

Stages (run all by default, or name them):
  search       EDGAR full-text search, each phrase x each window, all pages -> corpus/b-raw/filings/search-hits.jsonl
  fetch        primary document of each matched filing -> corpus/b-raw/filings/<accession>.txt
  passages     sections + +/-150-word passages -> corpus/b-raw/filings/passages.jsonl, results/.../filings-index.csv
  denominator  quarterly form.idx -> distinct 10-K filers per year, frame CIK map, filings-denominator.csv

Usage: python3 edgar_fetch.py [search] [fetch] [passages] [denominator] [--limit N]

Passage text stays under corpus/b-raw/ (git-ignored). Only counts and ids go to results/.
"""
import csv
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "corpus" / "b-raw" / "filings"
OUT = ROOT / "results" / "rerun-2026-10-10" / "corpus-b"
FRAME = ROOT / "corpus" / "staging" / "s1-employer-frame.csv"
IDX_CACHE = RAW / "full-index"

# SEC's fair-access check rejects the bare form of the declared agent on www.sec.gov
# (403 "Undeclared Automated Tool"), so the domain is written as a URL. Same identity.
UA = "Protocols for Business research (https://protocolsforbusiness.com)"
PHRASES = ["AI agent", "AI agents", "agentic", "autonomous agents", "digital workers", "digital labor"]
END = "2026-10-10"
WINDOWS = [(f"{y}-01-01", f"{y}-12-31" if y < 2026 else END) for y in range(2022, 2027)]
FORMS = "10-K,10-Q"
WORDS = 150
MIN_GAP = 0.22  # seconds between requests: under 5/sec

_last = [0.0]
DONE = set()


def get(url, tries=6):
    delay = 2.0
    for i in range(tries):
        wait = MIN_GAP - (time.monotonic() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.monotonic()
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if i == tries - 1:
                raise
        except Exception:
            if i == tries - 1:
                raise
        time.sleep(delay)
        delay *= 2
    return None


# ---------------------------------------------------------------- search
def search_window(phrase, start, end, sink):
    """All hits for phrase in [start, end]; splits the window if the 10,000-hit cap is reached."""
    if (phrase, f"{start}..{end}") in DONE:
        return
    base = {"q": f'"{phrase}"', "forms": FORMS, "dateRange": "custom", "startdt": start, "enddt": end}
    frm, total = 0, None
    rows = []
    while True:
        url = "https://efts.sec.gov/LATEST/search-index?" + urllib.parse.urlencode({**base, "from": frm})
        data = json.loads(get(url))
        if total is None:
            total = data["hits"]["total"]["value"]
            if total >= 10000 and start < end:
                from datetime import date, timedelta
                a, b = date.fromisoformat(start), date.fromisoformat(end)
                mid = a + (b - a) / 2
                search_window(phrase, start, mid.isoformat(), sink)
                search_window(phrase, (mid + timedelta(days=1)).isoformat(), end, sink)
                sink(phrase, f"{start}..{end}", [], total)
                return
        hits = data["hits"]["hits"]
        if not hits:
            break
        for h in hits:
            s = h["_source"]
            acc, _, fname = h["_id"].partition(":")
            rows.append({
                "phrase": phrase, "window": f"{start}..{end}", "accession": acc, "file": fname,
                "cik": (s.get("ciks") or [""])[0],
                "company": re.sub(r"\s*\(CIK \d+\)\s*$", "", (s.get("display_names") or [""])[0]).strip(),
                "form": s.get("form"), "file_type": s.get("file_type"), "filed": s.get("file_date"),
                "period": s.get("period_ending"),
            })
        frm += len(hits)
        if frm >= total:
            break
    sink(phrase, f"{start}..{end}", rows, total)


def stage_search():
    RAW.mkdir(parents=True, exist_ok=True)
    hits_f, done_f = RAW / "search-hits.jsonl", RAW / "search-done.txt"
    done = set(done_f.read_text().splitlines()) if done_f.exists() else set()

    def sink(phrase, window, rows, total):
        with open(hits_f, "a") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
        with open(done_f, "a") as f:
            f.write(f"{phrase}|{window}|{total}\n")
        DONE.add((phrase, window))
        print(f"search {phrase!r} {window}: {total} hits", flush=True)

    DONE.update(tuple(x.split("|")[:2]) for x in done)
    for phrase in PHRASES:
        for start, end in WINDOWS:
            search_window(phrase, start, end, sink)


def load_hits():
    f = RAW / "search-hits.jsonl"
    seen, filings = set(), {}
    phrases = defaultdict(set)
    for line in open(f):
        r = json.loads(line)
        key = (r["phrase"], r["accession"], r["file"])
        if key in seen:
            continue
        seen.add(key)
        ft = r.get("file_type") or ""
        if not (ft.startswith("10-K") or ft.startswith("10-Q")):
            continue  # exhibits
        phrases[r["accession"]].add(r["phrase"])
        if r["accession"] not in filings:
            filings[r["accession"]] = r
    for a, r in filings.items():
        r["search_phrases"] = sorted(phrases[a])
    return filings


# ---------------------------------------------------------------- fetch + text
class Text(HTMLParser):
    BLOCK = {"p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "h5", "h6", "table", "ul", "ol", "section", "hr", "title"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "ix:header"):
            self.skip += 1
        if tag in self.BLOCK:
            self.out.append("\n")
        elif tag in ("td", "th"):
            self.out.append(" ")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "ix:header"):
            self.skip = max(0, self.skip - 1)
        if tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)


def to_text(raw):
    s = raw.decode("utf-8", errors="replace")
    p = Text()
    p.feed(s)
    t = "".join(p.out).replace("\xa0", " ").replace("​", "")
    lines = [re.sub(r"[ \t\r\f\v]+", " ", l).strip() for l in t.split("\n")]
    return "\n".join(l for l in lines if l)


def stage_fetch(limit=None):
    filings = load_hits()
    todo = [a for a in sorted(filings) if not (RAW / f"{a}.txt").exists()]
    print(f"fetch: {len(filings)} filings, {len(todo)} to fetch", flush=True)
    for n, a in enumerate(todo[:limit] if limit else todo, 1):
        r = filings[a]
        url = f"https://www.sec.gov/Archives/edgar/data/{int(r['cik'])}/{a.replace('-', '')}/{r['file']}"
        try:
            raw = get(url)
        except Exception as e:
            print(f"  FAIL {a} {url}: {e}", flush=True)
            continue
        if raw is None:
            print(f"  404 {a} {url}", flush=True)
            continue
        txt = to_text(raw) if re.search(rb"<(html|div|p|body|table)", raw[:200000], re.I) else raw.decode("utf-8", "replace")
        (RAW / f"{a}.txt").write_text(txt)
        if n % 100 == 0:
            print(f"  fetched {n}/{len(todo)}", flush=True)


# ---------------------------------------------------------------- sections + passages
ITEM = re.compile(r"^item\s*(\d{1,2})\s*([a-c])?(?![a-z0-9])", re.I)
PART = re.compile(r"^part\s+(iv|iii|ii|i)(?![a-z])", re.I)


def section_of(form, part, num, letter):
    letter = (letter or "").upper()
    if form.startswith("10-K"):
        return {("1", ""): "business", ("1", "A"): "risk_factors", ("7", ""): "mdna", ("9", "A"): "controls"}.get((num, letter), "other")
    if part == 2:
        return "risk_factors" if (num, letter) == ("1", "A") else "other"
    return {("2", ""): "mdna", ("4", ""): "controls"}.get((num, letter), "other")


def split_sections(text, form):
    """Return [(char_offset, section)] boundaries from item headings at line start."""
    marks, part, off = [(0, "other")], 1, 0
    for line in text.split("\n"):
        if len(line) < 220:
            m = PART.match(line)
            if m:
                part = {"i": 1, "ii": 2, "iii": 3, "iv": 4}[m.group(1).lower()]
            m = ITEM.match(line)
            if m:
                marks.append((off, section_of(form, part, m.group(1), m.group(2))))
        off += len(line) + 1
    return marks


def passages_for(text, form):
    marks = split_sections(text, form)
    starts = [m[0] for m in marks]
    import bisect
    words = [(m.start(), m.end()) for m in re.finditer(r"\S+", text)]
    wstarts = [w[0] for w in words]
    out = []
    for phrase in PHRASES:
        pat = re.compile(r"(?<![A-Za-z0-9])" + r"\s+".join(map(re.escape, phrase.split())) + r"(?![A-Za-z0-9])", re.I)
        for m in pat.finditer(text):
            sec = marks[bisect.bisect_right(starts, m.start()) - 1][1]
            i = bisect.bisect_right(wstarts, m.start()) - 1
            j = bisect.bisect_right(wstarts, m.end() - 1) - 1
            a, b = max(0, i - WORDS), min(len(words), j + 1 + WORDS)
            out.append((phrase, sec, text[words[a][0]:words[b - 1][1]].replace("\n", " ")))
    return out


def stage_passages():
    filings = load_hits()
    OUT.mkdir(parents=True, exist_ok=True)
    rows, nfiles = [], 0
    with open(RAW / "passages.jsonl", "w") as pf:
        for a in sorted(filings):
            p = RAW / f"{a}.txt"
            r = filings[a]
            if not p.exists():
                continue
            nfiles += 1
            ps = passages_for(p.read_text(), r["form"])
            for phrase, sec, passage in ps:
                pf.write(json.dumps({"accession": a, "cik": r["cik"], "company": r["company"], "form": r["form"],
                                     "filed": r["filed"], "section": sec, "phrase": phrase, "passage": passage}) + "\n")
            found = sorted({x[0] for x in ps})
            rows.append([a, r["cik"], r["company"], r["form"], r["filed"], ";".join(sorted(set(found) | set(r["search_phrases"]))),
                         len(ps), ";".join(f"{k}:{v}" for k, v in sorted(Counter(x[1] for x in ps).items()))])
    with open(OUT / "filings-index.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["accession", "cik", "company", "form", "filed", "phrases", "n_passages", "sections"])
        w.writerows(rows)
    print(f"passages: {nfiles} filings with text of {len(filings)}", flush=True)


# ---------------------------------------------------------------- denominator
def quarters():
    for y in range(2022, 2027):
        for q in range(1, 5):
            if y == 2026 and q == 4:
                continue  # 2026 Q4 has not begun
            yield y, q


def parse_idx(raw):
    """Yield (form, name, cik, date). Parsed from the right: long names overflow the fixed columns."""
    pat = re.compile(r"^(.*?)\s+(\d+)\s+(\d{4}-\d\d-\d\d|\d{8})\s+edgar/\S+\s*$")
    for l in raw.decode("latin-1").splitlines():
        m = pat.match(l)
        if not m:
            continue
        head = m.group(1)
        form, name = head[:12].strip(), head[12:].strip()
        d = m.group(3).replace("-", "")
        yield form, name, m.group(2), f"{d[:4]}-{d[4:6]}-{d[6:]}"


SUFFIX = {"inc", "incorporated", "corp", "corporation", "co", "company", "ltd", "limited", "plc", "llc", "lp", "the", "de", "new", "nv", "sa", "ag", "holdings", "holding", "group", "cl", "class", "com"}


OVERRIDE = {  # frame name -> EDGAR registrant name where the plain name does not match (checked by hand)
    "Fannie Mae": "Federal National Mortgage Association", "Freddie Mac": "Federal Home Loan Mortgage Corp",
    "UPS": "United Parcel Service", "GE Aerospace": "General Electric", "Honeywell Technologies": "Honeywell International",
    "AIG": "American International Group", "U.S. Bancorp": "US Bancorp", "Bank of New York (BNY)": "Bank of New York Mellon",
    "Charles Schwab": "Schwab Charles", "W.R. Berkley": "Berkley W R", "Fidelity National Information (FIS)": "Fidelity National Information Services",
    "Expeditors Intl. of Washington": "Expeditors International of Washington", "Williams": "Williams Companies",
    "Discover": "Discover Financial Services", "DuPont": "DuPont de Nemours", "Franklin Templeton": "Franklin Resources",
    "D.R. Horton": "Horton D R", "C.H. Robinson Worldwide": "C H Robinson Worldwide", "J.B. Hunt Transport Services": "Hunt J B Transport Services",
    "O'Reilly Automotive": "O Reilly Automotive", "J.M. Smucker": "Smucker J M", "VF": "V F",
    "TIAA": "-", "Motive": "-",  # "-": no registrant of that name (TIAA Real Estate Account, Forge Global are not the firm)
    "Jones Financial (Edward Jones)": "Jones Financial Companies",
}


def norm(s, strip_suffix=True):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub("['\u2019]", "", s)
    s = re.sub(r"(?<=\b[a-z])\.(?=[a-z]\b)", "", s, flags=re.I)  # D.R. -> DR
    s = re.sub(r"/[a-z]{2,3}/?", " ", s.lower())  # EDGAR state tags like /DE/
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    t = s.split()
    if strip_suffix:
        while t and t[-1] in SUFFIX and len(t) > 1:
            t.pop()
        if t and t[0] == "the":
            t.pop(0)
    return " ".join(t)


def stage_denominator():
    OUT.mkdir(parents=True, exist_ok=True)
    IDX_CACHE.mkdir(parents=True, exist_ok=True)
    tenk = defaultdict(set)            # year -> ciks filing a 10-K (10-K, 10-KT; amendments excluded)
    names = defaultdict(Counter)       # cik -> names seen on 10-K filings
    for y, q in quarters():
        p = IDX_CACHE / f"{y}-QTR{q}.idx"
        if not p.exists():
            raw = get(f"https://www.sec.gov/Archives/edgar/full-index/{y}/QTR{q}/form.idx")
            if raw is None:
                print(f"  no index {y} Q{q}", flush=True)
                continue
            p.write_bytes(raw)
        for form, name, cik, date in parse_idx(p.read_bytes()):
            if form in ("10-K", "10-KT"):
                c = str(int(cik))
                tenk[int(date[:4])].add(c)
                names[c][name] += 1

    filings = load_hits()
    match_k = defaultdict(set)  # year -> ciks with a matched 10-K
    match_any = defaultdict(set)
    for r in filings.values():
        y, c = int(r["filed"][:4]), str(int(r["cik"]))
        match_any[y].add(c)
        if r["form"] in ("10-K", "10-KT"):
            match_k[y].add(c)

    # frame -> CIK
    byname = defaultdict(set)
    for c, cnt in names.items():
        for nm in cnt:
            byname[norm(nm)].add(c)
    nfil = {c: sum(1 for y in tenk if c in tenk[y]) for c in names}
    prefix_idx = sorted(byname)
    frame = []
    with open(FRAME) as f:
        for r in csv.DictReader(f):
            emp = r["employer"].strip()
            n = norm(OVERRIDE.get(emp, emp))
            cands, mtype = byname.get(n, set()), "exact"
            if not cands:
                cands = {c for k in prefix_idx if k.startswith(n + " ") for c in byname[k]}
                mtype = "prefix"
            if emp in OVERRIDE and cands:
                mtype = "override"
            if not cands:
                frame.append([emp, r["type"], "", "", "none", 0])
                continue
            best = max(cands, key=lambda c: (nfil[c], -len(names[c].most_common(1)[0][0])))
            frame.append([emp, r["type"], best, names[best].most_common(1)[0][0], mtype, len(cands)])
    with open(OUT / "frame-cik.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["employer", "type", "cik", "edgar_name", "match_type", "n_candidates"])
        w.writerows(frame)
    fciks = {r[2] for r in frame if r[2]}

    with open(OUT / "filings-denominator.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["year", "tenk_filers", "tenk_filers_matching", "share", "frame_ciks_matched", "frame_tenk_filers",
                    "frame_tenk_filers_matching", "frame_share", "filers_matching_any_10k_or_10q"])
        for y in range(2022, 2027):
            n, m = len(tenk[y]), len(match_k[y])
            fk, fm = tenk[y] & fciks, match_k[y] & fciks
            w.writerow([y, n, m, f"{m / n:.4f}" if n else "", len(fciks), len(fk), len(fm),
                        f"{len(fm) / len(fk):.4f}" if fk else "", len(match_any[y])])
    print("denominator written", flush=True)


def main():
    args = sys.argv[1:]
    limit = None
    if "--limit" in args:
        i = args.index("--limit")
        limit = int(args[i + 1])
        del args[i:i + 2]
    stages = args or ["search", "fetch", "passages", "denominator"]
    if "search" in stages:
        stage_search()
    if "fetch" in stages:
        stage_fetch(limit)
    if "passages" in stages:
        stage_passages()
    if "denominator" in stages:
        stage_denominator()


if __name__ == "__main__":
    main()
