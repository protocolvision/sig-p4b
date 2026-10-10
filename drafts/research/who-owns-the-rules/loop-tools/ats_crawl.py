"""Corpus B postings: discover public job boards for the 550-employer frame, then crawl every open posting.

Needs Python 3.9+, standard library only, open network access.

Usage:
  python3 ats_crawl.py discover [--limit N] [--only NAME] [--workers 16]
  python3 ats_crawl.py crawl    [--limit N] [--only NAME] [--workers 32] [--retry-failed] [--cap 5000]

discover reads corpus/staging/s1-employer-frame.csv and writes
  results/rerun-2026-10-10/corpus-b/boards.csv
    employer,type,ats,board_id,workday_host,workday_site,method,evidence_url,status,note
  Order of attack: (a) careers page links (guessed <co>.com/careers, careers.<co>.com, one level deep),
  (b) slug probes against the public Greenhouse / Lever / Ashby / SmartRecruiters APIs with a company-name
  plausibility check, (c) Workday tenant/site probes. ats is one of greenhouse, lever, ashby, smartrecruiters,
  workday, other-ats (icims, taleo, successfactors, eightfold, phenom: not crawlable) or none.

crawl reads boards.csv and writes
  corpus/b-raw/postings/<ats>-<board_id>.jsonl   one posting per line (git-ignored; other people's text)
  results/rerun-2026-10-10/corpus-b/crawl-index.csv
    employer,ats,board_id,postings,fetched,status,note
  Resumable: boards already status ok/capped in crawl-index.csv are skipped; per-posting-detail crawls
  (SmartRecruiters, Workday) also skip posting ids already in the jsonl. No topic filtering. Capped at 5000
  postings per employer; the cap is noted.

Rate limit: 2 requests/sec per host.
"""
import argparse, csv, html, json, pathlib, re, socket, sys, threading, time, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
FRAME = ROOT / "corpus" / "staging" / "s1-employer-frame.csv"
OUT = ROOT / "results" / "rerun-2026-10-10" / "corpus-b"
BOARDS, INDEX = OUT / "boards.csv", OUT / "crawl-index.csv"
POSTINGS = ROOT / "corpus" / "b-raw" / "postings"
UA = "Protocols for Business research (protocolsforbusiness.com)"
TODAY = time.strftime("%Y-%m-%d")
CAP = 5000
BFIELDS = ["employer", "type", "ats", "board_id", "workday_host", "workday_site", "method", "evidence_url", "status", "note"]
IFIELDS = ["employer", "ats", "board_id", "postings", "fetched", "status", "note"]
OTHER_ATS = {"icims": r"icims\.com", "taleo": r"taleo\.net", "successfactors": r"(?:successfactors\.(?:com|eu)|jobs\.sap\.com)",
             "eightfold": r"eightfold\.ai", "phenom": r"(?:phenompeople\.com|phenom\.com|\.phenomcdn)"}
CRAWLABLE = ["workday", "greenhouse", "lever", "ashby", "smartrecruiters"]

# ---------------------------------------------------------------- http with per-host rate limit
_hosts, _hl = {}, threading.Lock()


def _wait(host):
    with _hl:
        h = _hosts.setdefault(host, [threading.Lock(), 0.0])
    with h[0]:
        d = h[1] + 0.5 - time.time()
        if d > 0:
            time.sleep(d)
        h[1] = time.time()


def http(url, data=None, headers=None, timeout=30, tries=3):
    """Return (status, body_bytes, final_url). status 0 means network failure. Never raises."""
    host = urllib.parse.urlsplit(url).netloc
    hd = {"User-Agent": UA, "Accept": "application/json, text/html;q=0.9, */*;q=0.5"}
    hd.update(headers or {})
    body = json.dumps(data).encode() if data is not None else None
    if body:
        hd["Content-Type"] = "application/json"
    last = (0, b"", url)
    for i in range(tries):
        _wait(host)
        try:
            req = urllib.request.Request(url, data=body, headers=hd)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(200_000_000), r.geturl()
        except urllib.error.HTTPError as e:
            last = (e.code, e.read(200_000) if e.fp else b"", url)
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 * (i + 1) * (3 if e.code == 429 else 1))
                continue
            return last
        except Exception as e:
            last = (0, str(e).encode()[:200], url)
            if "Name or service" in str(e) or "nodename" in str(e):
                return last
            time.sleep(1 + i)
    return last


def jget(url, **kw):
    st, b, u = http(url, **kw)
    if st != 200:
        return st, None
    try:
        return st, json.loads(b)
    except Exception:
        return st, None


def strip_html(s):
    if not s:
        return ""
    s = html.unescape(s) if "&lt;" in s else s
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h\d|tr|ul|ol)>", "\n", s)
    s = re.sub(r"(?i)<li[^>]*>", "- ", s)
    s = html.unescape(re.sub(r"(?s)<[^>]+>", " ", s))
    s = re.sub(r"[ \t\r\f\v\xa0]+", " ", s)
    return "\n".join(l.strip() for l in s.splitlines() if l.strip())


# ---------------------------------------------------------------- names and slugs
SUFFIX = {"inc", "corp", "corporation", "company", "co", "group", "holdings", "holding", "companies", "the", "ltd", "plc",
          "llc", "lp", "enterprises", "incorporated", "limited", "and", "of", "stores", "technologies", "technology"}


def words(name):
    n = name.lower().replace("&", " and ").replace("'", "").replace("’", "")
    return [w for w in re.split(r"[^a-z0-9]+", n) if w]


def core_words(name):
    w = words(name)
    c = [x for x in w if x not in SUFFIX]
    return c or w


def norm(s):
    return "".join(core_words(s)) if s else ""


def slugs_for(name):
    c, w = core_words(name), words(name)
    out = []
    for s in ["".join(c), "-".join(c), "".join(w), c[0] if len(c) > 1 and len(c[0]) >= 4 else "",
              "".join(c) + "inc", "".join(c) + "hq", "".join(c) + "careers"]:
        if s and s not in out:
            out.append(s)
    return out[:6]


def name_match(employer, other):
    a, b = norm(employer), norm(other)
    if not a or not b:
        return False
    if a == b:
        return True
    # the employer's whole core name must sit at the start or end of the board's name ("Careers at KKR");
    # a board named only for the employer's first word ("Charles" for Charles Schwab) is not accepted
    return len(a) >= 4 and (b.startswith(a) or b.endswith(a))


def mentions(employer, texts):
    """Employer display name (case-sensitive core) appears in at least half of the sample texts."""
    core = " ".join(w.capitalize() if w.islower() else w for w in re.split(r"\s+", re.sub(r"[,.]", "", employer)) if w.lower() not in SUFFIX) or employer
    pats = {core, employer, " ".join(core_words(employer)).title()}
    hits = sum(1 for t in texts if any(re.search(r"\b" + re.escape(p) + r"\b", t) for p in pats if p))
    return bool(texts) and hits >= max(1, (len(texts) + 1) // 2), hits, len(texts)


# ---------------------------------------------------------------- board verification (shared by links and probes)
def verify(ats, bid, employer, wd=None, strict=False, typ=""):
    """Return (ok, evidence_url, note). strict means the slug was only guessed, so require a name match."""
    if ats == "greenhouse":
        url = f"https://boards-api.greenhouse.io/v1/boards/{bid}"
        st, j = jget(url)
        if not j:
            return False, url, f"http {st}"
        nm = j.get("name", "")
        if strict and not name_match(employer, nm):
            return False, url, f"name mismatch: board '{nm}'"
        return True, url, f"board name '{nm}'"
    if ats == "lever":
        url = f"https://api.lever.co/v0/postings/{bid}?mode=json&limit=8"
        st, j = jget(url)
        if not isinstance(j, list) or not j:
            return False, url, f"http {st}" if st != 200 else "no postings"
        if strict and typ == "fortune500" and len(j) < 10:
            return False, url, f"only {len(j)} postings; too few to trust a guessed slug for a large firm"
        if strict:
            ok, h, n = mentions(employer, [p.get("descriptionPlain", "") + (p.get("additionalPlain") or "") for p in j[:5]])
            if not ok:
                return False, url, f"name not in postings ({h}/{n})"
            return True, url, f"employer name in {h}/{n} sampled postings"
        return True, url, f"{len(j)}+ postings"
    if ats == "ashby":
        url = f"https://api.ashbyhq.com/posting-api/job-board/{bid}"
        st, j = jget(url)
        if not j or not isinstance(j.get("jobs"), list):
            return False, url, f"http {st}"
        if not j["jobs"]:
            return not strict, url, "empty board"
        if strict and typ == "fortune500" and len(j["jobs"]) < 10:
            return False, url, f"only {len(j['jobs'])} jobs; too few to trust a guessed slug for a large firm"
        if strict:
            ok, h, n = mentions(employer, [p.get("descriptionPlain") or strip_html(p.get("descriptionHtml", "")) for p in j["jobs"][:5]])
            if not ok:
                return False, url, f"name not in postings ({h}/{n})"
            return True, url, f"employer name in {h}/{n} sampled postings; {len(j['jobs'])} jobs"
        return True, url, f"{len(j['jobs'])} jobs"
    if ats == "smartrecruiters":
        url = f"https://api.smartrecruiters.com/v1/companies/{bid}/postings?limit=5"
        st, j = jget(url)
        if not j or not j.get("totalFound"):
            return False, url, f"http {st}" if st != 200 else "no postings"
        nm = (j["content"][0].get("company") or {}).get("name", "")
        if strict and not name_match(employer, nm):
            return False, url, f"name mismatch: company '{nm}'"
        return True, url, f"company '{nm}'; {j['totalFound']} postings"
    if ats == "workday":
        host, site, tenant = wd
        url = wd_api(host, site, tenant)
        st, j = jget(url, data={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""})
        if not j or "total" not in j:
            return False, url, f"http {st}"
        return True, url, f"{j['total']} postings"
    return False, "", "unknown ats"


# Workday: host is https://<tenant>.wdN.myworkdayjobs.com (or https://wdN.myworkdaysite.com with tenant in path).
def wd_parse(u):
    """Return (host, tenant, site) from a Workday URL, or None."""
    m = re.match(r"https?://([a-z0-9-]+)\.(wd\d+)\.myworkdayjobs\.com/(?:wday/cxs/[^/]+/|[a-z]{2}-[A-Za-z]{2}/)?([A-Za-z0-9_%.\-]+)", u)
    if m and m.group(3).lower() not in ("login", "assets", "wday", "favicon.ico", "robots.txt", "userhome", "api"):
        return f"https://{m.group(1)}.{m.group(2)}.myworkdayjobs.com", m.group(1), m.group(3)
    m = re.match(r"https?://(wd\d+)\.myworkdaysite\.com/(?:[a-z]{2}-[A-Za-z]{2}/)?recruiting/([A-Za-z0-9_\-]+)/([A-Za-z0-9_%.\-]+)", u)
    if m:
        return f"https://{m.group(1)}.myworkdaysite.com", m.group(2), m.group(3)
    return None


def wd_api(host, site, tenant):
    return f"{host}/wday/cxs/{tenant}/{site}/jobs"


# ---------------------------------------------------------------- (a) careers pages
GH = re.compile(r"(?:boards|job-boards)(?:\.eu)?\.greenhouse\.io/(?:embed/job_board(?:/js)?\?for=|v1/boards/)?([A-Za-z0-9_-]+)")
GH_FOR = re.compile(r"greenhouse\.io/embed/job_board[^\"'\s]*?[?&]for=([A-Za-z0-9_-]+)")
LV = re.compile(r"jobs\.(?:eu\.)?lever\.co/([A-Za-z0-9_.-]+)")
AB = re.compile(r"jobs\.ashbyhq\.com/([A-Za-z0-9_.%-]+)")
SR = re.compile(r"(?:jobs|careers)\.smartrecruiters\.com/([A-Za-z0-9_-]+)")
WD = re.compile(r"https?:(?:\\?/){2}[a-z0-9-]+\.wd\d+\.myworkdayjobs\.com(?:\\?/)[^\s\"'<>)\\]*|https?:(?:\\?/){2}wd\d+\.myworkdaysite\.com(?:\\?/)recruiting(?:\\?/)[^\s\"'<>)\\]*")
BADSLUG = {"embed", "v1", "boards", "jobs", "api", "static", "assets", "js", "css", "img", "favicon.ico"}


def find_ats(text, final_urls):
    """Scan page text for ATS links. Returns dict ats -> list of ids (workday: list of (host,tenant,site))."""
    blob = text.replace("\\/", "/") + "\n" + "\n".join(final_urls)
    found = {a: [] for a in CRAWLABLE}
    for rx in (GH, GH_FOR):
        for m in rx.finditer(blob):
            s = m.group(1)
            if s.lower() not in BADSLUG and s not in found["greenhouse"]:
                found["greenhouse"].append(s)
    for m in LV.finditer(blob):
        if m.group(1) not in found["lever"]:
            found["lever"].append(m.group(1))
    for m in AB.finditer(blob):
        s = urllib.parse.unquote(m.group(1))
        if s not in found["ashby"]:
            found["ashby"].append(s)
    for m in SR.finditer(blob):
        if m.group(1).lower() not in ("oneclick-ui", "company") and m.group(1) not in found["smartrecruiters"]:
            found["smartrecruiters"].append(m.group(1))
    for m in WD.finditer(blob):
        p = wd_parse(m.group(0).replace("\\/", "/"))
        if p and p not in found["workday"]:
            found["workday"].append(p)
    other = [k for k, rx in OTHER_ATS.items() if re.search(rx, blob, re.I)]
    return found, other


LINKRX = re.compile(r'(?is)<a\b[^>]*?href=["\']([^"\'#]+)["\']')


def career_links(base, text):
    out = []
    for h in LINKRX.findall(text):
        h = html.unescape(h.strip())
        if h.startswith(("mailto:", "javascript:", "tel:")):
            continue
        u = urllib.parse.urljoin(base, h)
        if re.search(r"(?i)career|job|search|opportunit|openings|apply|work-?with|join", u) and u.startswith("http"):
            out.append(u)
    seen, res = set(), []
    for u in out:
        k = u.split("#")[0]
        if k not in seen:
            seen.add(k)
            res.append(k)
    return res


def fetch_page(url):
    st, b, fu = http(url, tries=2, timeout=20, headers={"Accept": "text/html,*/*;q=0.8"})
    return st, b.decode("utf-8", "ignore") if st == 200 else "", fu


def careers_scan(employer):
    """Return (found, other, visited_urls) from careers-page crawling, one level deep."""
    c, w = core_words(employer), words(employer)
    doms = []
    for s in ["".join(c), "".join(w), "-".join(c)]:
        if s and s + ".com" not in doms:
            doms.append(s + ".com")
    found = {a: [] for a in CRAWLABLE}
    other, visited, pages = set(), [], 0
    for dom in doms[:2]:
        try:
            socket.gethostbyname(dom)
        except Exception:
            continue
        starts = [f"https://www.{dom}/careers", f"https://{dom}/careers", f"https://careers.{dom}", f"https://www.{dom}/jobs"]
        got_any = False
        for u in starts:
            st, txt, fu = fetch_page(u)
            if st != 200:
                continue
            got_any = True
            visited.append(fu)
            f, o = find_ats(txt, [fu])
            for k in f:
                found[k] += [x for x in f[k] if x not in found[k]]
            other |= set(o)
            # follow links one level deep, careers-like links first
            for l in career_links(fu, txt)[:8]:
                if pages >= 14:
                    break
                host = urllib.parse.urlsplit(l).netloc
                pages += 1
                st2, t2, fu2 = fetch_page(l)
                f2, o2 = find_ats(t2 if st2 == 200 else "", [fu2, l])
                for k in f2:
                    found[k] += [x for x in f2[k] if x not in found[k]]
                other |= set(o2)
            if any(found.values()):
                break
        if got_any:
            break
    return found, sorted(other), visited


# ---------------------------------------------------------------- (c) Workday probes
WD_HOSTS = ["wd1", "wd5", "wd3", "wd12", "wd501", "wd503", "wd2", "wd103"]


def wd_sites(slug, name):
    cap = slug.capitalize()
    return ["External", slug, cap, "Careers", slug + "careers", cap + "Careers", cap + "_Careers", "External_Career_Site",
            "ExternalCareerSite", "careers", "jobs", cap + "Jobs", slug + "_External", "External_Careers", cap + "External", slug + "external", cap + "ExternalCareerSite", cap + "_External", cap + "Careers_External", cap + "CareerSite", cap + "_Careers_External"]


def workday_probe(employer):
    for slug in slugs_for(employer)[:4]:
        for wd in WD_HOSTS:
            host = f"https://{slug}.{wd}.myworkdayjobs.com"
            # wildcard DNS: a valid tenant answers 404/200 to a bogus site, a missing tenant answers 422
            st, _, fu = http(f"{host}/wday/cxs/{slug}/ExternalZz/jobs", data={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""}, tries=1, timeout=15)
            if st not in (200, 404, 400, 500):
                continue
            st2, _, fu = http(host + "/", tries=1, timeout=15)
            p = wd_parse(fu)
            sites = [p[2]] if p else []
            for s in wd_sites(slug, employer):
                if s not in sites:
                    sites.append(s)
            for s in sites[:22]:
                ok, ev, note = verify("workday", None, employer, wd=(host, s, slug))
                if ok:
                    return host, slug, s, ev, note
    return None


# ---------------------------------------------------------------- discover
def discover_one(row):
    emp, typ = row["employer"], row["type"]
    r = {k: "" for k in BFIELDS}
    r.update(employer=emp, type=typ, status="none", method="", ats="none")
    notes = []
    # (a) careers page
    try:
        found, other, visited = careers_scan(emp)
    except Exception as e:
        found, other, visited = {a: [] for a in CRAWLABLE}, [], []
        notes.append(f"careers scan error {str(e)[:60]}")
    if visited:
        notes.append("careers page: " + visited[0])
    else:
        notes.append("careers page not reachable")
    cands = []
    for p in found["workday"]:
        cands.append(("workday", p))
    for a in ("greenhouse", "lever", "ashby", "smartrecruiters"):
        for s in found[a][:3]:
            cands.append((a, s))
    others_seen = [f"{a}:{x if isinstance(x, str) else x[1]}" for a, x in cands]
    chosen = None
    for a, x in sorted(cands, key=lambda t: CRAWLABLE.index(t[0])):
        if a == "workday":
            ok, ev, note = verify("workday", None, emp, wd=(x[0], x[2], x[1]))
        else:
            # link found on the employer's own careers site: not a guess, but keep a loose sanity check
            ok, ev, note = verify(a, x, emp, strict=False)
        if ok:
            chosen = (a, x, ev, note)
            break
        notes.append(f"link {a} {x if isinstance(x, str) else x[1]+'/'+x[2]} failed: {note}")
    if chosen:
        a, x, ev, note = chosen
        r.update(ats=a, method="careers-page-link", evidence_url=ev, status="found", note=note)
        if a == "workday":
            r.update(board_id=x[1], workday_host=x[0], workday_site=x[2])
        else:
            r.update(board_id=x)
        extra = [o for o in others_seen if not o.startswith(a + ":" + (x if isinstance(x, str) else x[1]))]
        r["note"] = "; ".join([note] + (["also linked: " + ",".join(extra[:4])] if extra else []) + (["other-ats links: " + ",".join(other)] if other else []))
        return r
    # (b) slug probes
    for slug in slugs_for(emp):
        for a in ("greenhouse", "lever", "ashby", "smartrecruiters"):
            ok, ev, note = verify(a, slug, emp, strict=True, typ=typ)
            if ok:
                r.update(ats=a, board_id=slug, method="slug-probe", evidence_url=ev, status="found", note=note)
                if other:
                    r["note"] += "; other-ats links: " + ",".join(other)
                return r
    # (c) workday tenant probe
    try:
        w = workday_probe(emp)
    except Exception:
        w = None
    if w:
        host, slug, site, ev, note = w
        r.update(ats="workday", board_id=slug, workday_host=host, workday_site=site, method="workday-probe", evidence_url=ev,
                 status="found", note=note + "; tenant guessed from employer name, company identity not verifiable via API")
        return r
    if other:
        r.update(ats="other-ats", status="not-crawlable", method="careers-page-link", evidence_url=visited[0] if visited else "",
                 note="links to " + ",".join(other) + "; " + "; ".join(notes))
        return r
    r["note"] = "; ".join(notes)[:400] + "; slug probes tried: " + ",".join(slugs_for(emp))
    return r


def read_frame():
    with open(FRAME, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})
    tmp.replace(path)


def cmd_discover(a):
    frame = read_frame()
    if a.only:
        frame = [r for r in frame if a.only.lower() in r["employer"].lower()]
    if a.redo:  # re-run only employers whose current boards.csv row has this method (e.g. after tightening a rule)
        redo = {r["employer"] for r in csv.DictReader(open(BOARDS, newline="", encoding="utf-8")) if a.redo in (r["method"], r["ats"])}
        frame = [r for r in frame if r["employer"] in redo]
    if a.limit:
        frame = frame[:a.limit]
    partial = bool(a.only or a.limit or a.redo)
    old = list(csv.DictReader(open(BOARDS, newline="", encoding="utf-8"))) if partial and BOARDS.exists() else []
    results, lock = {}, threading.Lock()

    def work(row):
        try:
            r = discover_one(row)
        except Exception as e:
            r = {k: "" for k in BFIELDS}
            r.update(employer=row["employer"], type=row["type"], ats="none", status="error", note=f"{type(e).__name__}: {str(e)[:150]}")
        with lock:
            results[row["employer"]] = r
            print(f"[{len(results)}/{len(frame)}] {r['employer']}: {r['ats']} {r['board_id']} ({r['method']})", flush=True)
            if not partial and len(results) % 25 == 0:
                write_csv(BOARDS, BFIELDS, [results[x["employer"]] for x in frame if x["employer"] in results])
        return r

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(work, frame))
    rows = [results[x["employer"]] for x in frame]
    if partial:  # merge into the existing file, keeping frame order
        by = {o["employer"]: o for o in old}
        by.update(results)
        full = [x["employer"] for x in read_frame()]
        rows = [by[e] for e in full if e in by]
    write_csv(BOARDS, BFIELDS, rows)
    from collections import Counter
    print(Counter((r["type"], r["ats"]) for r in rows))


# ---------------------------------------------------------------- crawl
def posting(emp, ats, bid, id_, title, loc, dept, posted, url, text, **extra):
    d = dict(id=str(id_), employer=emp, ats=ats, board_id=bid, title=title or "", location=loc or "", department=dept or "",
             posted_date=posted or "", url=url or "", description_text=text or "", fetched=TODAY)
    d.update({k: v for k, v in extra.items() if v})
    return d


def load_ids(path):
    ids = set()
    if path.exists():
        for l in open(path, encoding="utf-8"):
            try:
                ids.add(json.loads(l)["id"])
            except Exception:
                pass
    return ids


class Sink:
    """Append-only jsonl writer used for ATSs that need one request per posting (resumable)."""
    def __init__(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.path, self.n = path, 0
        self.f = open(path, "a", encoding="utf-8")

    def add(self, d):
        self.f.write(json.dumps(d, ensure_ascii=False) + "\n")
        self.f.flush()
        self.n += 1

    def close(self):
        self.f.close()


def write_all(path, items):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        for d in items:
            f.write(json.dumps(d, ensure_ascii=False) + "\n")
    tmp.replace(path)


def crawl_greenhouse(b, path, cap):
    st, j = jget(f"https://boards-api.greenhouse.io/v1/boards/{b['board_id']}/jobs?content=true", timeout=120)
    if j is None:
        return None, f"http {st}"
    jobs = j.get("jobs", [])
    items = [posting(b["employer"], "greenhouse", b["board_id"], p["id"], p.get("title"), (p.get("location") or {}).get("name"),
                     "; ".join(d.get("name", "") for d in p.get("departments", [])), p.get("first_published") or p.get("updated_at"),
                     p.get("absolute_url"), strip_html(p.get("content"))) for p in jobs[:cap]]
    write_all(path, items)
    return len(items), (f"capped at {cap} of {len(jobs)}" if len(jobs) > cap else "")


def crawl_lever(b, path, cap):
    items, skip = [], 0
    while len(items) < cap:
        st, j = jget(f"https://api.lever.co/v0/postings/{b['board_id']}?mode=json&skip={skip}&limit=100", timeout=60)
        if j is None:
            if not items:
                return None, f"http {st}"
            break
        if not j:
            break
        for p in j:
            cats = p.get("categories") or {}
            parts = [p.get("descriptionPlain") or strip_html(p.get("description"))]
            for l in p.get("lists") or []:
                parts.append((l.get("text") or "") + "\n" + strip_html(l.get("content")))
            parts.append(p.get("additionalPlain") or strip_html(p.get("additional")))
            ts = p.get("createdAt")
            items.append(posting(b["employer"], "lever", b["board_id"], p["id"], p.get("text"), cats.get("location"),
                                 cats.get("department") or cats.get("team"),
                                 time.strftime("%Y-%m-%d", time.gmtime(ts / 1000)) if ts else "", p.get("hostedUrl"),
                                 "\n".join(x for x in parts if x), commitment=cats.get("commitment")))
        if len(j) < 100:
            break
        skip += 100
    note = ""
    if len(items) > cap:
        note = f"capped at {cap}"
        items = items[:cap]
    write_all(path, items)
    return len(items), note


def crawl_ashby(b, path, cap):
    st, j = jget(f"https://api.ashbyhq.com/posting-api/job-board/{b['board_id']}?includeCompensation=true", timeout=120)
    if j is None:
        return None, f"http {st}"
    jobs = j.get("jobs", [])
    items = []
    for p in jobs[:cap]:
        comp = (p.get("compensation") or {}).get("compensationTierSummary") or (p.get("compensation") or {}).get("scrapeableCompensationSalarySummary")
        items.append(posting(b["employer"], "ashby", b["board_id"], p.get("id"), p.get("title"), p.get("location"),
                             p.get("department") or p.get("team"), p.get("publishedAt"), p.get("jobUrl"),
                             p.get("descriptionPlain") or strip_html(p.get("descriptionHtml")), compensation=comp))
    write_all(path, items)
    return len(items), (f"capped at {cap} of {len(jobs)}" if len(jobs) > cap else "")


def crawl_sr(b, path, cap):
    base = f"https://api.smartrecruiters.com/v1/companies/{b['board_id']}/postings"
    have = load_ids(path)
    listing, off, total = [], 0, None
    while len(listing) < cap:
        st, j = jget(f"{base}?limit=100&offset={off}")
        if j is None:
            if not listing:
                return None, f"list http {st}"
            break
        total = j.get("totalFound", 0)
        c = j.get("content", [])
        listing += c
        if not c or len(listing) >= total:
            break
        off += 100
    sink, fails = Sink(path), 0
    for p in listing[:cap]:
        if str(p["id"]) in have:
            continue
        st, d = jget(f"{base}/{p['id']}")
        if d is None:
            fails += 1
            continue
        secs = ((d.get("jobAd") or {}).get("sections")) or {}
        text = "\n\n".join(strip_html((secs.get(k) or {}).get("text", "")) for k in ("companyDescription", "jobDescription", "qualifications", "additionalInformation"))
        loc = d.get("location") or {}
        sink.add(posting(b["employer"], "smartrecruiters", b["board_id"], p["id"], d.get("name"),
                         ", ".join(x for x in (loc.get("city"), loc.get("region"), loc.get("country", "").upper()) if x),
                         (d.get("department") or {}).get("label"), d.get("releasedDate"), d.get("postingUrl") or d.get("applyUrl"), text.strip()))
    sink.close()
    n = len(load_ids(path))
    note = f"capped at {cap} of {total}" if (total or 0) > cap else ""
    if fails:
        note = (note + "; " if note else "") + f"{fails} detail fetches failed"
    return n, note


def crawl_workday(b, path, cap):
    host, site, tenant = b["workday_host"], b["workday_site"], b["board_id"]
    api = wd_api(host, site, tenant)
    have = load_ids(path)
    listing, off, total = [], 0, None
    while len(listing) < cap:
        st, j = jget(api, data={"appliedFacets": {}, "limit": 20, "offset": off, "searchText": ""}, timeout=60)
        if j is None:
            if not listing:
                return None, f"list http {st}"
            break
        if total is None or j.get("total"):
            total = j.get("total", total)
        c = j.get("jobPostings", [])
        if not c:
            break
        listing += c
        off += 20
        if total is not None and off >= total:
            break
    sink, fails, seen, todo = Sink(path), 0, set(), []
    for p in listing[:cap]:
        ep = p.get("externalPath")
        if not ep or ep in seen:
            continue
        seen.add(ep)
        pid = ep.rsplit("_", 1)[-1] if "_" in ep else ep
        if pid not in have and ep not in have:
            todo.append((p, ep, pid))
    wl = threading.Lock()

    def one(t):
        p, ep, pid = t
        st, d = jget(f"{host}/wday/cxs/{tenant}/{site}{ep}")
        info = (d or {}).get("jobPostingInfo")
        if not info:
            return 1
        rec = posting(b["employer"], "workday", tenant, info.get("jobReqId") or pid, info.get("title") or p.get("title"),
                      info.get("location") or p.get("locationsText"), "", info.get("startDate") or p.get("postedOn"),
                      info.get("externalUrl") or f"{host}/{site}{ep}", strip_html(info.get("jobDescription")),
                      time_type=info.get("timeType"))
        with wl:
            sink.add(rec)
        return 0

    with ThreadPoolExecutor(4) as ex:
        fails = sum(ex.map(one, todo))
    sink.close()
    # ids were stored as jobReqId, so count lines rather than matching externalPath
    n = sum(1 for _ in open(path, encoding="utf-8")) if path.exists() else 0
    note = f"capped at {cap} of {total}" if (total or 0) > cap else ""
    if len(listing) < min(total or 0, cap):
        note = (note + "; " if note else "") + f"listing returned {len(listing)} of {total}"
    if fails:
        note = (note + "; " if note else "") + f"{fails} detail fetches failed"
    return n, note


CRAWLERS = {"greenhouse": crawl_greenhouse, "lever": crawl_lever, "ashby": crawl_ashby, "smartrecruiters": crawl_sr, "workday": crawl_workday}


def safe(s):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s)


def cmd_crawl(a):
    boards = list(csv.DictReader(open(BOARDS, newline="", encoding="utf-8")))
    if a.only:
        boards = [b for b in boards if a.only.lower() in b["employer"].lower()]
    if a.limit:
        boards = boards[:a.limit]
    idx = {}
    if INDEX.exists():
        for r in csv.DictReader(open(INDEX, newline="", encoding="utf-8")):
            idx[r["employer"]] = r
    lock = threading.Lock()

    def flush():
        write_csv(INDEX, IFIELDS, list(idx.values()))

    def work(b):
        emp, ats = b["employer"], b["ats"]
        if ats not in CRAWLERS:
            r = dict(employer=emp, ats=ats, board_id=b["board_id"], postings=0, fetched=TODAY, status="skipped",
                     note="not crawlable" if ats == "other-ats" else "no board discovered")
        else:
            old = idx.get(emp)
            if old and old["status"] in ("ok", "capped") and old["board_id"] == b["board_id"] and old["ats"] == ats:
                return
            if old and old["status"] == "failed" and not a.retry_failed:
                return
            path = POSTINGS / f"{ats}-{safe(b['board_id'])}.jsonl"
            try:
                n, note = CRAWLERS[ats](b, path, a.cap)
            except Exception as e:
                n, note = None, f"{type(e).__name__}: {str(e)[:150]}"
            if n is None:
                r = dict(employer=emp, ats=ats, board_id=b["board_id"], postings=0, fetched=TODAY, status="failed", note=note)
            else:
                r = dict(employer=emp, ats=ats, board_id=b["board_id"], postings=n, fetched=TODAY,
                         status="capped" if "capped" in note else ("empty" if n == 0 else "ok"), note=note)
        with lock:
            idx[emp] = r
            print(f"{emp}: {r['ats']} {r['postings']} {r['status']} {r['note']}", flush=True)
            flush()

    with ThreadPoolExecutor(a.workers) as ex:
        list(ex.map(work, boards))
    with lock:
        flush()
    print("total postings:", sum(int(r["postings"]) for r in idx.values()))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest="cmd", required=True)
    d = sp.add_parser("discover")
    d.add_argument("--workers", type=int, default=16)
    d.add_argument("--redo", metavar="METHOD")
    c = sp.add_parser("crawl")
    c.add_argument("--workers", type=int, default=32)
    c.add_argument("--retry-failed", action="store_true")
    c.add_argument("--cap", type=int, default=CAP)
    for p in (d, c):
        p.add_argument("--limit", type=int)
        p.add_argument("--only")
    a = ap.parse_args()
    {"discover": cmd_discover, "crawl": cmd_crawl}[a.cmd](a)


if __name__ == "__main__":
    main()
