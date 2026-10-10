#!/usr/bin/env python3
"""I1 labour-market measures, exactly as fixed in deviations.md items 14, 18, 21.
Run with loop-tools/.venv/bin/python from the study root. Writes
results/rerun-2026-10-10/instruments/I1-tables.csv, I1-lexical-flags.csv and I1-posting-level.csv.gz.

v2 (review, 10 October 2026; v1 kept as i1_labour-v1.py):
- rest20 is a 20% stratified sample (deviation 14; strata = O*NET major group of the selection-time mapping
  postings-mapped.csv x employer type). Each rest20 posting carries sampling weight N_h / n_h of its stratum;
  S1 and new-title postings weight 1. Pooled counts, shares and ratios are reported unweighted and
  sampling-weighted; the employer weighting (each employer total 1) is built on the sampling weights.
- Board workday/abbott is Abbott Laboratories (crawl-identity-check); selection.csv attributed it to Ross Stores
  (duplicate board row in boards.csv). Corrected here.
- US vs non-US rule: site-code prefixes stripped, country-region prefixes, "U.S." at end of string, and US
  places that share a name with a non-US place (Florence KY, North Wales PA, Vancouver WA, ...).
- Lexical flag validated on the 200 real posting records of the coding pool against coder A and B codes
  (AO, PE or RD = agent or AI duty). Reads corpus/b-raw/coding/record-pool-key.json for validation only
  (real vs seed); the term list is unchanged."""
import json, re, sys
from pathlib import Path
import numpy as np, pandas as pd

ROOT = Path(__file__).resolve().parent.parent
R = ROOT / "results/rerun-2026-10-10"
OUT = R / "instruments"

# ---------- lexical agent/AI duty flag (item 21) ----------
TERMS = [r"AI", r"A\.I\.", r"agentic", r"LLM", r"GenAI", r"generative AI", r"machine learning",
         r"automation", r"prompt", r"copilot", r"intelligent automation", r"RPA",
         r"AI governance", r"responsible AI", r"model risk"]
TERM_RE = re.compile(r"(?<![\w.])(?:" + "|".join(TERMS) + r")(?![\w])", re.I)
ADJ = r"(?:AI|A\.I\.|agentic|autonomous|virtual|digital)"
AGENT_RE = re.compile(r"(?<![\w.])(?:" + ADJ + r"[\s\-/]+agents?|agents?[\s\-/]+" + ADJ + r")(?![\w])", re.I)

def lex_flag(span):
    s = span or ""
    return bool(TERM_RE.search(s) or AGENT_RE.search(s))

def lex_terms(span):
    """Matched terms, lower-cased ("agent rule" for an AGENT_RE hit); for reporting which terms drive the flag."""
    s = span or ""
    out = {m.group(0).lower() for m in TERM_RE.finditer(s)}
    if AGENT_RE.search(s): out.add("agent rule")
    return out

# ---------- US vs non-US from location text ----------
US_STATES = set("AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC PR".split())
US_WORD = re.compile(r"(?<![A-Za-z])(?:USA|U\.S\.(?:A\.?)?|United States(?: of America)?|US)(?![A-Za-z])")
US_STATE_NAMES = ("Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota Mississippi Missouri Montana Nebraska Nevada Ohio Oklahoma Oregon Pennsylvania Tennessee Texas Utah Vermont Virginia Washington Wisconsin Wyoming New York|New Jersey|New Mexico|New Hampshire|North Carolina|South Carolina|North Dakota|South Dakota|Rhode Island|West Virginia|District of Columbia").split()
US_CITIES = ["New York","NYC","San Francisco","Chicago","San Jose","Boise","Houston","Charlotte","Atlanta","Boston","Austin","North Chicago","Seattle","Los Angeles","Dallas","Denver","Phoenix","Philadelphia","Pittsburgh","Minneapolis","Detroit","Santa Clara","Sunnyvale","Mountain View","Palo Alto","Redwood City","San Diego","San Mateo","Cupertino","Milpitas","Fremont","Menlo Park","Washington DC","Washington, D.C.","Salt Lake City","Nashville","Columbus","Cincinnati","Cleveland","St. Louis","Kansas City","Omaha","Portland","Raleigh","Richmond","Tampa","Miami","Orlando","Irvine","Plano","Irving","Memphis","Louisville","Indianapolis","Milwaukee","Baltimore","Hartford","Stamford","Cambridge","Bentonville","Springdale","Arlington","Remote - US","Remote US","Fab 10N","Fab 10X","Fab 10","Evendale","Boulder","Durham","Bellevue","Redmond","Oakland","Sacramento","Burlington","Wilmington","Newark","Jersey City","Rochester","Albany","Buffalo","Honolulu","Anchorage","Las Vegas","Tucson","Albuquerque","Oklahoma City","Tulsa","Jacksonville","New Orleans","Birmingham","Greenville","Peoria","Moline","Des Moines","Madison","Toledo","Akron","Dayton","Lexington","Knoxville","Chattanooga","Savannah","Charleston","Norfolk","Reston","McLean","Herndon","Bethesda","Rockville","Princeton","Parsippany","Bridgewater","Tarrytown","Sleepy Hollow","Niskayuna","Schenectady","Rensselaer","Grand Rapids","Longmont","Clearwater","Kalamazoo","Grand Forks","Burns Harbor","Stafford","Kohl's","AutoNation","Charles City","Bangor","Lincoln","Warren","Pennington"]
NONUS = ["India","Bangalore","Bengaluru","Hyderabad","Pune","Mumbai","Chennai","Gurgaon","Gurugram","Noida","Delhi","Kolkata","Singapore","London","United Kingdom","UK","England","Scotland","Wales","Ireland","Dublin","Seoul","Korea","Tokyo","Japan","Osaka","China","Shanghai","Beijing","Shenzhen","Hong Kong","Taiwan","Taipei","Taichung","Hsinchu","Canada","Toronto","Vancouver","Montreal","Ottawa","Calgary","Mexico","Brazil","Brasil","Argentina","Chile","Colombia","Peru","Germany","Munich","Berlin","France","Paris","Spain","Madrid","Barcelona","Italy","Milan","Florence","Rome","Netherlands","Amsterdam","Belgium","Brussels","Poland","Warsaw","Krakow","Romania","Bucharest","Bulgaria","Sofia","Hungary","Budapest","Czech","Prague","Portugal","Lisbon","Sweden","Stockholm","Norway","Denmark","Finland","Switzerland","Zurich","Austria","Vienna","Turkey","Istanbul","Israel","Tel Aviv","UAE","United Arab Emirates","Dubai","Abu Dhabi","Saudi","Riyadh","Bahrain","Egypt","Cairo","South Africa","Johannesburg","Nigeria","Kenya","Australia","Sydney","Melbourne","New Zealand","Philippines","Manila","Pasig","Malaysia","Kuala Lumpur","Penang","Thailand","Bangkok","Vietnam","Indonesia","Jakarta","Pakistan","Sri Lanka","Bangladesh","Costa Rica","Panama","Guatemala","Dominican","Puerto Rico?","EMEA","APAC","LATAM","Ukraine","Greece","Serbia","Croatia","Slovakia","Lithuania","Latvia","Estonia","Luxembourg","Morocco","Ghana","Guadalajara","Cork","Limerick","Mississauga","Quebec","Ontario","Chihuahua","Ho Chi Minh","Villeurbanne","Belfort","Nhon Trach","Ranjangaon","Sanchong","Tanauan","Quezon","Taguig","Petaling","Benalm\u00e1dena","Martillac","Nouvelle-Aquitaine","Sao Bernardo","Tbilisi","Guangzhou","Lyon","Massy","Kwidzyn","Markham","Brossard","Bromont","Canadian Head Office","Uzhhorod","Thailand","Monterrey","Tijuana","Bogota","Lima","Santiago","Buenos Aires","Sao Paulo","S\u00e3o Paulo","T\u00fcrkiye","Turkiye","Jordan","Amman"]
def _wb(words):
    return re.compile(r"(?<![A-Za-z])(?:" + "|".join(re.escape(w) for w in words) + r")(?![A-Za-z])", re.I)
NONUS_RE = _wb([w for w in NONUS if not w.endswith("?")])
US_CITY_RE = _wb(US_CITIES)
US_STATE_NAME_RE_V1 = _wb([x for part in US_STATE_NAMES for x in part.split("|")])  # v1 bug: splits "New York" into "New", "York", and matches "of", "North", "West"
# v2: single-word names split on spaces, multi-word names (joined by "|") kept whole
_SN = " ".join(US_STATE_NAMES).split(" New York|")[0].split() + ("New York|" + " ".join(US_STATE_NAMES).split(" New York|")[1]).split("|")
US_STATE_NAME_RE = _wb(_SN)
STATE_TOKEN = re.compile(r"(?:,\s*|\s-\s*|\s)(" + "|".join(sorted(US_STATES)) + r")(?=$|[\s,\-/;0-9])")
STATE_TOKEN_FIRST = re.compile(r"^(" + "|".join(sorted(US_STATES)) + r")\s*[-,/]\s")

ISO3 = re.compile(r"^(?:CAN|BRA|VNM|ESP|PHL|MYS|MEX|IND|CHN|JPN|KOR|GBR|DEU|FRA|ITA|NLD|POL|ROU|HUN|SGP|TWN|THA|IDN|IRL|CA-[A-Z]{2}|PH-[A-Z]+|BR-[A-Z]{2}|MX-[A-Z]+|PL-[0-9A-Z]+|GEO|TUN)(?![A-Za-z])")
REMOTE_ST = re.compile(r"^Remote\s*[-,(]\s*(?:Any State|(" + "|".join(sorted(US_STATES)) + r"))\b")

# v2: non-US place names that are also US places. A hit on one of these alone does not make a location non-US
# when a US state token, state name or US word is also present (Florence, KY; USA - Pennsylvania - North Wales).
AMBIG_NONUS = _wb(["Florence","Vancouver","Melbourne","Dublin","Vienna","Amsterdam","Lima","Rome","Wales",
                   "Paris","Berlin","Panama","Cairo","Milan","Peru","Delhi","Ontario","London",
                   "Sydney","Warsaw","Lyon","Jordan","Santiago"])
STATE_COMMA = re.compile(r",\s*(" + "|".join(sorted(US_STATES)) + r")(?=$|[\s,\-/;0-9])")
SITE_CODE = re.compile(r"^(?!USA:)[A-Z]{3}[A-Z0-9]*:\s*")          # e.g. CAN05:, CAFLO:, LOC5028:, CHE4442:
CC_REGION = re.compile(r"^(?!US-|NA-US-|XX-)([A-Z]{2})-[A-Z]{2,3}-")      # e.g. DE-BY-NORDLINGEN, IN-KA-BANGALORE
# e.g. TX-GRAND PRAIRIE; DE, ID and CO excluded (also Germany, Indonesia, Colombia country codes in this crawl)
ST_DASH_FIRST = re.compile(r"^(" + "|".join(sorted(US_STATES - {"DE", "ID", "CO"})) + r")-\s*[A-Za-z]")
CA_PROVINCE = re.compile(r"(?:,\s*|\s-\s*|^)(?:BC|QC|AB|MB|SK|NS|NB|NL|PE)(?=$|[\s,\-])|"
                         r"(?<![A-Za-z])(?:British Columbia|Alberta|Manitoba|Saskatchewan|Nova Scotia)(?![A-Za-z])|"
                         r"^CA\s*-\s*Ontario\b")

def _nonus_hit(s):
    """True if s names a non-US place other than an ambiguous US-namesake."""
    return bool(NONUS_RE.search(AMBIG_NONUS.sub("", re.sub(r"New Mexico", "", s, flags=re.I))))

def us_class(loc):
    """Return 'us', 'non-us' or 'unknown'. Multi-location strings use the first listed location."""
    if not isinstance(loc, str) or not loc.strip():
        return "unknown"
    s = re.split(r";|\||\bor\b|\band\b(?= [A-Z])", loc)[0].strip() or loc
    s = s.replace("\xa0", " ").strip()
    # site codes such as "CAN05:" (Carrier US sites) are not reliable country codes: classify the rest of the
    # string, and fall back to the code's ISO3 prefix (except CAN+digits, used for US sites) only if unknown
    m = SITE_CODE.match(s)
    if m:
        c = _us_class_core(s[m.end():])
        if c != "unknown" or re.match(r"^CAN\d", s):
            return c
        return "non-us" if ISO3.search(s) else "unknown"
    return _us_class_core(s)

def _us_class_core(s):
    if CA_PROVINCE.search(s) and not US_WORD.search(s): return "non-us"
    if ISO3.search(s.strip()): return "non-us"
    if CC_REGION.match(s): return "non-us"
    if s.startswith("US-"): return "us"
    if REMOTE_ST.search(s.strip()): return "us"
    us_state = bool(STATE_TOKEN.search(s) or STATE_TOKEN_FIRST.search(s) or ST_DASH_FIRST.search(s)
                    or US_STATE_NAME_RE.search(s))
    # strict US evidence (comma-separated state code, leading state code, state name): used to override an
    # ambiguous place name; a bare all-caps token such as "LA" in "PARIS LA DEFENSE" does not count
    us_strict = bool(STATE_COMMA.search(s) or STATE_TOKEN_FIRST.search(s) or ST_DASH_FIRST.search(s)
                     or US_STATE_NAME_RE.search(s))
    # explicit US words win over city lists
    if US_WORD.search(s) and not _nonus_hit(US_WORD.sub("", s)):
        return "us"
    if _nonus_hit(s):
        return "non-us"
    if (AMBIG_NONUS.search(s) or re.search(r"(?<![A-Za-z])Mexico(?![A-Za-z])", re.sub(r"New Mexico", "", s, flags=re.I))) and not us_strict:
        return "non-us"
    if us_state or US_CITY_RE.search(s):
        return "us"
    return "unknown"

def us_class_v1(loc):
    """The v1 rule, kept for the accuracy comparison."""
    if not isinstance(loc, str) or not loc.strip():
        return "unknown"
    s = re.split(r";|\||\bor\b|\band\b(?= [A-Z])", loc)[0].strip() or loc
    if ISO3.search(s.strip()): return "non-us"
    if REMOTE_ST.search(s.strip()): return "us"
    if US_WORD_V1.search(s) and not NONUS_V1_RE.search(US_WORD_V1.sub("", s)):
        return "us"
    if NONUS_V1_RE.search(s):
        return "non-us"
    if STATE_TOKEN.search(s) or STATE_TOKEN_FIRST.search(s) or US_STATE_NAME_RE_V1.search(s) or US_CITY_RE.search(s):
        return "us"
    return "unknown"
US_WORD_V1 = re.compile(r"\b(?:USA|U\.S\.A?\.?|United States(?: of America)?|US)\b")
NONUS_V1_RE = _wb([w for w in NONUS if not w.endswith("?") and w not in ("T\u00fcrkiye","Turkiye","Jordan","Amman")])

# ---------- helpers ----------
def sector_of(sic, etype, has_cik):
    if etype != "fortune500":
        return "VC software (not SEC filers)"
    if not has_cik:
        return "Mutuals and private (no SEC filing)"
    try: n = int(sic)
    except Exception: return "Unclassified"
    if 3570 <= n <= 3579 or 3670 <= n <= 3679 or 7370 <= n <= 7379: return "Tech (SIC 357x, 367x, 737x)"
    if 100 <= n <= 1799: return "Mining, construction, agriculture"
    if 2000 <= n <= 3999: return "Manufacturing"
    if 4000 <= n <= 4899: return "Transport and telecom"
    if 4900 <= n <= 4999: return "Utilities"
    if 5000 <= n <= 5999: return "Retail and wholesale"
    if 6000 <= n <= 6799: return "Finance, insurance, real estate"
    if 7000 <= n <= 8999: return "Services (other)"
    return "Unclassified"

rows = []
FLAG_NOTE = {"value": ""}   # set by validate(): measured precision of the lexical flag, attached to every flag row
def add(measure, slice_, value, n, weighting, flag=False):
    rows.append(dict(measure=measure, slice=slice_, value=value, n=n, weighting=weighting,
                     flag_precision=FLAG_NOTE["value"] if flag else ""))

# board workday/abbott is Abbott Laboratories (review/crawl-identity-check.md); boards.csv lists it twice and
# selection.csv took the Ross Stores row
EMPLOYER_FIX = {("workday", "abbott"): "Abbott Laboratories"}
GROUPS_FULL = ("S1", "newtitle", "newtitle-agent-human")   # fully enumerated (deviation 14)

def sampling_weights(sel):
    """Inverse sampling fraction per rest20 stratum (O*NET major group of the selection-time mapping x employer
    type). Universe: all titled postings of postings-mapped.csv (the mapping whose codes selection.csv carries)
    on non-excluded boards, minus the fully enumerated groups."""
    key = ["ats", "board_id", "posting_id"]
    u = pd.read_csv(ROOT / "corpus/b-raw/mapping/postings-mapped.csv", usecols=key + ["onet_code"])
    b = pd.read_csv(R / "corpus-b/boards.csv")
    b = b[b.status == "found"].drop_duplicates(["ats", "board_id"])[["ats", "board_id", "type"]]
    ex = {l.strip() for l in open(R / "corpus-b/exclude-boards.txt") if l.strip() and not l.startswith("#")}
    u = u.merge(b, on=["ats", "board_id"], how="left")
    u = u[~(u.ats + "-" + u.board_id.astype(str)).isin(ex)]
    assert u.type.notna().all() and not u.duplicated(key).any()
    u = u.merge(sel[key + ["group"]], on=key, how="left")
    assert u.group.notna().sum() == len(sel), "selection not contained in the mapping universe"
    rest = u[~u.group.isin(GROUPS_FULL)].copy()
    rest["stratum"] = rest.onet_code.astype(str).str[:2].where(rest.onet_code.notna(), "none") + "|" + rest.type
    st = rest.groupby("stratum").group.agg(N="size", n=lambda g: int((g == "rest20").sum()))
    st["fraction"] = st.n / st.N
    st["weight"] = st.N / st.n
    sel_st = sel.onet_code.astype(str).str[:2].where(sel.onet_code.notna(), "none") + "|" + sel.employer_type
    w = np.where(sel.group == "rest20", sel_st.map(st.weight), 1.0)
    assert not np.isnan(w).any()
    return w, st, len(u)

def wsum(x, w):
    return float((np.asarray(x, dtype=float) * np.asarray(w, dtype=float)).sum())

def main():
    validate()   # sets FLAG_NOTE before any flag-based figure is written
    sel = pd.read_csv(ROOT / "corpus/b-raw/mapping/selection.csv")
    for (ats, bid), emp in EMPLOYER_FIX.items():
        sel.loc[(sel.ats == ats) & (sel.board_id == bid), "employer"] = emp
    sel["doc_id"] = "P" + sel.ats + "_" + sel.board_id.astype(str) + "_" + sel.posting_id.astype(str)
    sel["sw"], strata, n_universe = sampling_weights(sel)
    strata.to_csv(OUT / "I1-strata.csv")
    mp = pd.read_csv(ROOT / "corpus/b-raw/mapping/postings-mapped-v2.csv")
    sel = sel.merge(mp[["ats","board_id","posting_id","major_group","location","department"]],
                    on=["ats","board_id","posting_id"], how="left")
    sel["us"] = sel.location.map(us_class)
    sel["us_v1"] = sel.location.map(us_class_v1)
    cik = pd.read_csv(R / "corpus-b/frame-cik.csv", dtype={"cik": str})
    sic = {}
    for _, r in cik.iterrows():
        if isinstance(r.cik, str) and r.cik.strip() and r.cik != "nan":
            p = ROOT / f"corpus/b-raw/filings/sic/CIK{int(float(r.cik)):010d}.json"
            if p.exists():
                sic[r.employer] = json.load(open(p)).get("sic")
    has_cik = set(cik.dropna(subset=["cik"]).employer)
    sel["sector"] = [sector_of(sic.get(e), t, e in has_cik) for e, t in zip(sel.employer, sel.employer_type)]

    # tasks -> posting flag
    tasks = pd.read_json(ROOT / "corpus/b-raw/extract/postings-haiku-all.tasks.jsonl", lines=True)
    tasks["flag"] = tasks.span.map(lex_flag)
    tasks["terms"] = tasks.span.map(lex_terms)
    pflag = tasks.groupby("doc_id").flag.any()
    sel["n_tasks"] = sel.doc_id.map(tasks.groupby("doc_id").size()).fillna(0).astype(int)
    sel["ai_duty"] = sel.doc_id.map(pflag).eq(True)
    pterms = tasks[tasks.flag].groupby("doc_id").terms.apply(lambda s: set().union(*s))
    sel["flag_terms"] = sel.doc_id.map(pterms).map(lambda x: "|".join(sorted(x)) if isinstance(x, set) else "")

    # cluster assignments / labels
    a = pd.read_csv(R / "clusters/leaf/assignments.csv.gz")
    lab = pd.read_csv(R / "clusters/leaf/labels.csv")
    artefacts = artefact_rule()
    lab["artefact"] = lab.cluster_id.isin(artefacts)
    a["doc_id"] = "P" + a.ats + "_" + a.board_id.astype(str) + "_" + a.posting_id.astype(str)
    a = a.merge(lab[["cluster_id","function_family","business_or_technical","found","artefact"]], on="cluster_id", how="left")
    PRIMARY = set(lab[lab.found.astype(bool) & ~lab.artefact].cluster_id)   # found, non-artefact (deviation 20)
    assert PRIMARY == {2, 19, 43, 67, 69, 76, 83, 111}, PRIMARY
    def cross(df, clusters_ok):
        d = df[df.cluster_id.isin(clusters_ok)]
        out = {}
        for doc, g in d.groupby("doc_id"):
            fams = set(g.function_family)
            out[doc] = (len(fams) >= 2 and "business" in set(g.business_or_technical) and "technical" in set(g.business_or_technical))
        return pd.Series(out, dtype=bool)
    prim = cross(a, PRIMARY)
    sec_ok = set(lab[~lab.artefact].cluster_id) - {-1}
    sec = cross(a, sec_ok)
    base_prim = set(a[a.cluster_id.isin(PRIMARY)].doc_id)
    base_sec = set(a[a.cluster_id.isin(sec_ok)].doc_id)
    pooled = set(a.doc_id)
    sel["in_pool"] = sel.doc_id.isin(pooled)
    sel["has_prim"] = sel.doc_id.isin(base_prim); sel["cross_prim"] = sel.doc_id.map(prim).eq(True)
    sel["has_sec"] = sel.doc_id.isin(base_sec); sel["cross_sec"] = sel.doc_id.map(sec).eq(True)

    sel["cat"] = np.select([sel.group == "newtitle", sel.group == "newtitle-agent-human", sel.group == "S1"],
                           ["new_title", "new_title_human_agent", "study_occupation"], "rest_sample")
    sel["existing_all"] = sel.group.isin(["S1", "rest20"])   # all non-new-title postings
    sel["existing_s1"] = sel.group == "S1"
    # employer weighting (each employer weight 1) over the employer's estimated postings: sampling weight / employer total
    sel["w_emp"] = sel.sw / sel.groupby("employer").sw.transform("sum")
    sel["w_emp_v1"] = 1.0 / sel.groupby("employer").doc_id.transform("count")

    ARTIFACT_NOTE = ",".join(map(str, sorted(artefacts)))
    add("language_artefact_clusters", ARTIFACT_NOTE, len(artefacts), len(lab), "none")
    add("rest20_strata", "all", len(strata), int(strata.N.sum()), "none")
    add("rest20_sampling_fraction", "min", round(float(strata.fraction.min()), 4), int(strata.n.sum()), "none")
    add("rest20_sampling_fraction", "max", round(float(strata.fraction.max()), 4), int(strata.n.sum()), "none")
    add("rest20_sampling_fraction", "overall", round(float(strata.n.sum() / strata.N.sum()), 4), int(strata.N.sum()), "none")
    add("rest20_weight", "mean", round(float(sel.sw[sel.group == "rest20"].mean()), 4), int((sel.group == "rest20").sum()), "none")
    add("titled_postings_in_mapping_universe", "all", n_universe, n_universe, "none")
    add("selected_postings", "all", len(sel), len(sel), "unweighted")
    add("selected_postings", "all", round(float(sel.sw.sum()), 1), len(sel), "sampling-weighted")
    for g, d in sel.groupby("group"):
        add("selected_postings", f"group={g}", len(d), len(d), "unweighted")
        add("selected_postings", f"group={g}", round(float(d.sw.sum()), 1), len(d), "sampling-weighted")
    add("postings_with_extracted_tasks", "all", int((sel.n_tasks > 0).sum()), len(sel), "unweighted")
    for k in ("us","non-us","unknown"):
        add("us_class_postings", k, int((sel.us == k).sum()), len(sel), "unweighted")
        add("us_class_postings", k, round(float(sel.sw[sel.us == k].sum()), 1), len(sel), "sampling-weighted")
        add("us_class_postings_v1_rule", k, int((sel.us_v1 == k).sum()), len(sel), "unweighted")

    # ---- new-title by term
    nt = sel[sel.group.isin(["newtitle", "newtitle-agent-human"])]
    for t, d in nt.groupby(["group","term"]): add("newtitle_postings_by_term", f"{t[0]}|{t[1]}", len(d), len(d), "none")

    # ---- AI-duty prevalence and absorption
    def slices():
        yield "all", sel
        for k, d in sel.groupby("employer_type"): yield f"type={k}", d
        for k, d in sel[sel.us != "unknown"].groupby("us"): yield f"us={k}", d
        for (t, u), d in sel[sel.us != "unknown"].groupby(["employer_type","us"]): yield f"type={t}|us={u}", d
    for name, d in slices():
        new = d[d.group == "newtitle"]
        nnew_u = len(new); nnew_w = float(new.w_emp.sum())
        add("new_title_postings", name, nnew_u, nnew_u, "unweighted")
        add("new_title_postings", name, round(nnew_w, 4), nnew_u, "employer-weighted")
        for lab_, mask in (("study_occupation", d.existing_s1), ("all_non_new_title", d.existing_all)):
            e = d[mask]
            nflag_u = int(e.ai_duty.sum()); nflag_s = wsum(e.ai_duty, e.sw); nflag_e = wsum(e.ai_duty, e.w_emp)
            add(f"existing_with_ai_duty[{lab_}]", name, nflag_u, len(e), "unweighted", flag=True)
            add(f"existing_with_ai_duty[{lab_}]", name, round(nflag_s, 1), len(e), "sampling-weighted", flag=True)
            add(f"existing_with_ai_duty[{lab_}]", name, round(nflag_e, 4), len(e), "employer-weighted", flag=True)
            add(f"existing_postings[{lab_}]", name, round(float(e.sw.sum()), 1), len(e), "sampling-weighted")
            add(f"absorption_ratio[{lab_}]", name, round(nflag_u / nnew_u, 4) if nnew_u else np.nan, nnew_u, "unweighted", flag=True)
            add(f"absorption_ratio[{lab_}]", name, round(nflag_s / nnew_u, 4) if nnew_u else np.nan, nnew_u, "sampling-weighted", flag=True)
            add(f"absorption_ratio[{lab_}]", name, round(nflag_e / nnew_w, 4) if nnew_w else np.nan, nnew_u, "employer-weighted", flag=True)
            add(f"share_existing_with_ai_duty[{lab_}]", name, round(nflag_u / len(e), 4) if len(e) else np.nan, len(e), "unweighted", flag=True)
            add(f"share_existing_with_ai_duty[{lab_}]", name, round(nflag_s / e.sw.sum(), 4) if len(e) else np.nan, len(e), "sampling-weighted", flag=True)
            add(f"share_existing_with_ai_duty[{lab_}]", name, round(nflag_e / e.w_emp.sum(), 4) if len(e) else np.nan, len(e), "employer-weighted", flag=True)
    for g in ("newtitle", "newtitle-agent-human", "S1", "rest20"):
        d = sel[sel.group == g]
        add("share_with_ai_duty", f"group={g}", round(d.ai_duty.mean(), 4), len(d), "unweighted", flag=True)
    # which terms carry the posting flag among existing postings (sampling-weighted)
    e = sel[sel.existing_all & sel.ai_duty]
    for t in sorted({x for v in e.flag_terms for x in v.split("|") if x}):
        has = e.flag_terms.str.split("|").map(lambda v: t in v)
        only = e.flag_terms == t
        add("existing_flagged_with_term[all_non_new_title]", f"term={t}", round(wsum(has, e.sw), 1), len(e), "sampling-weighted", flag=True)
        add("existing_flagged_only_by_term[all_non_new_title]", f"term={t}", round(wsum(only, e.sw), 1), len(e), "sampling-weighted", flag=True)
    # employers with >=1 (rest20 is a sample, so employer counts for (b) are lower bounds)
    for lab_, mask in (("study_occupation", sel.existing_s1), ("all_non_new_title", sel.existing_all)):
        add(f"employers_with_ai_duty_existing[{lab_}]", "all", int(sel[mask & sel.ai_duty].employer.nunique()), int(sel.employer.nunique()), "employer", flag=True)
    add("employers_with_new_title", "all", int(sel[sel.group=="newtitle"].employer.nunique()), int(sel.employer.nunique()), "employer")

    # ---- cross-function
    for lvl, has, cr in (("primary", "has_prim", "cross_prim"), ("secondary", "has_sec", "cross_sec")):
        cats = {"new_title": sel.group == "newtitle", "other_postings": sel.group != "newtitle",
                "other_study_occupation": sel.group == "S1", "other_rest_sample": sel.group == "rest20",
                "new_title_human_agent": sel.group == "newtitle-agent-human"}
        for cn, cm in cats.items():
            d = sel[cm & sel[has]]
            add(f"cross_function_share[{lvl}]", cn, round(d[cr].mean(), 4) if len(d) else np.nan, len(d), "unweighted")
            if len(d):
                add(f"cross_function_share[{lvl}]", cn, round(wsum(d[cr], d.sw) / d.sw.sum(), 4), len(d), "sampling-weighted")
                add(f"cross_function_share[{lvl}]", cn, round(wsum(d[cr], d.w_emp) / d.w_emp.sum(), 4), len(d), "employer-weighted")
            add(f"cross_function_count[{lvl}]", cn, int(d[cr].sum()) if len(d) else 0, len(d), "unweighted")
            add(f"cross_function_count[{lvl}]", cn, round(wsum(d[cr], d.sw), 1) if len(d) else 0, len(d), "sampling-weighted")
            add(f"postings_in_{lvl}_clusters", cn, int((cm & sel[has]).sum()), int(cm.sum()), "unweighted")
            add(f"postings_in_{lvl}_clusters", cn, round(float(sel.sw[cm & sel[has]].sum()), 1), int(cm.sum()), "sampling-weighted")
        for t, d0 in sel.groupby("employer_type"):
            for cn in ("new_title","other_postings"):
                d = d0[cats[cn].loc[d0.index] & d0[has]]
                add(f"cross_function_share[{lvl}]", f"{cn}|type={t}", round(d[cr].mean(), 4) if len(d) else np.nan, len(d), "unweighted")
                if len(d):
                    add(f"cross_function_share[{lvl}]", f"{cn}|type={t}", round(wsum(d[cr], d.sw) / d.sw.sum(), 4), len(d), "sampling-weighted")
    add("postings_with_pooled_tasks", "all", int(sel.in_pool.sum()), len(sel), "unweighted")

    # ---- new-title spread (new-title postings are fully enumerated; only the share of postings uses weights)
    def spread(key):
        for k, d in sel.groupby(key):
            emp = d.groupby("employer").agg(nt=("group", lambda x: int((x == "newtitle").sum())), n=("group", "size"), nw=("sw", "sum"))
            add("employers", f"{key}={k}", len(emp), len(emp), "employer")
            add("new_title_postings_per_employer_mean", f"{key}={k}", round(emp.nt.mean(), 4), len(emp), "employer")
            add("new_title_postings_per_employer_median", f"{key}={k}", float(emp.nt.median()), len(emp), "employer")
            add("employers_with_ge1_new_title", f"{key}={k}", int((emp.nt > 0).sum()), len(emp), "employer")
            add("share_employers_with_ge1_new_title", f"{key}={k}", round(float((emp.nt > 0).mean()), 4), len(emp), "employer")
            add("new_title_postings_total", f"{key}={k}", int(emp.nt.sum()), int(emp.n.sum()), "none")
            add("new_title_share_of_postings", f"{key}={k}", round(emp.nt.sum() / emp.n.sum(), 4), int(emp.n.sum()), "unweighted")
            add("new_title_share_of_postings", f"{key}={k}", round(emp.nt.sum() / emp.nw.sum(), 4), int(emp.n.sum()), "sampling-weighted")
    spread("employer_type"); spread("sector")
    add("employers", "all", int(sel.employer.nunique()), int(sel.employer.nunique()), "employer")
    emp = sel.groupby("employer").group.apply(lambda x: int((x == "newtitle").sum()))
    add("employers_with_ge1_new_title", "all", int((emp > 0).sum()), len(emp), "employer")
    add("share_employers_with_ge1_new_title", "all", round(float((emp > 0).mean()), 4), len(emp), "employer")
    add("new_title_postings_per_employer_mean", "all", round(emp.mean(), 4), len(emp), "employer")
    add("new_title_postings_per_employer_median", "all", float(emp.median()), len(emp), "employer")
    add("new_title_postings_per_employer_max", "all", int(emp.max()), len(emp), "employer")
    add("new_title_share_of_postings", "all", round((sel.group == "newtitle").sum() / len(sel), 4), len(sel), "unweighted")
    add("new_title_share_of_postings", "all", round((sel.group == "newtitle").sum() / sel.sw.sum(), 4), len(sel), "sampling-weighted")
    for k in ("employer_type","sector"):
        for (kv, t), d in sel[sel.group == "newtitle"].groupby([k, "term"]):
            add("new_title_postings_by_term", f"{k}={kv}|term={t}", len(d), len(d), "none")

    # ---- major groups (descriptive; ~83% accurate per item 18)
    for cat, d in (("new_title", sel[sel.group=="newtitle"]), ("study_occupation", sel[sel.group=="S1"]), ("rest_sample", sel[sel.group=="rest20"])):
        d = d[d.major_group.notna()]
        mg = d.major_group.astype(int).astype(str).str.zfill(2)
        for g in sorted(mg.unique()):
            m_ = mg == g
            add("major_group_share[descriptive; major group correct ~83%]", f"{cat}|major_group={g}", round(m_.mean(), 4), int(m_.sum()), "unweighted")
            if cat == "rest_sample":
                add("major_group_share[descriptive; major group correct ~83%]", f"{cat}|major_group={g}", round(wsum(m_, d.sw) / d.sw.sum(), 4), int(m_.sum()), "sampling-weighted")
    d = sel[(sel.group == "newtitle")]
    for g, dd in d.groupby("major_group"):
        if len(dd): add("major_group_new_title_ai_duty_share[descriptive; ~83%]", f"major_group={int(g):02d}", round(dd.ai_duty.mean(), 4), len(dd), "unweighted", flag=True)

    pd.DataFrame(rows).to_csv(OUT / "I1-tables.csv", index=False)
    sel.drop(columns=["w_emp_v1"]).to_csv(OUT / "I1-posting-level.csv.gz", index=False)
    unknown = sel[sel.us == "unknown"].location.value_counts().head(40)
    print("unknown-location top:", unknown.to_dict())
    print("artefacts:", sorted(artefacts))

def artefact_rule():
    """Deviation 20: >50% of 20 central spans mostly non-Latin script, or <30% contain common English function words."""
    cl = pd.read_csv(R / "clusters/leaf/clusters.csv")
    fw = re.compile(r"\b(?:the|and|to|of|with|for)\b", re.I)
    out = set()
    for _, r in cl.iterrows():
        spans = [s.strip() for s in str(r.top20_central_spans).split(" | ") if s.strip()]
        if not spans: continue
        def nonlatin(s):
            letters = [c for c in s if c.isalpha()]
            if not letters: return False
            return sum(1 for c in letters if ord(c) > 0x024F) / len(letters) > 0.5
        a = np.mean([nonlatin(s) for s in spans]) > 0.5
        b = np.mean([bool(fw.search(s)) for s in spans]) < 0.30
        if a or b: out.add(int(r.cluster_id))
    return out

AGENT_CODES = {"AO", "PE", "RD"}

def validate():
    """Item 21 validation: lexical flag vs coder A and B on the 200 real posting records of the coding pool.
    A coder says "agent or AI duty" when code1 or code2 is AO, PE or RD. The record-pool key is read only here,
    to keep real records (and their task ids) apart from seeds."""
    key = pd.DataFrame(json.load(open(ROOT / "corpus/b-raw/coding/record-pool-key.json")))
    pool = pd.read_json(ROOT / "corpus/b-raw/coding/record-pool.jsonl", lines=True)
    d = pool.merge(key, on="id")
    d = d[(d.kind == "posting") & (d._src == "real")].copy()
    tasks = pd.read_json(ROOT / "corpus/b-raw/extract/postings-haiku-all.tasks.jsonl", lines=True).set_index("task_id")
    assert d._task.isin(tasks.index).all()
    assert (d._task.map(tasks.span).str.strip() == d.span.str.strip()).all()
    d["flag"] = d.span.map(lex_flag).astype(int)
    d["terms"] = d.span.map(lambda s: "|".join(sorted(lex_terms(s))))
    prec = {}
    for c in ("A", "B"):
        X = pd.read_csv(R / f"coding/coder{c}-records.csv").set_index("id")
        d[f"coder{c}_codes"] = d.id.map(X.code1.fillna("") + "/" + X.code2.fillna("")).str.strip("/")
        d[f"coder{c}_agent_duty"] = d.id.map(X.code1.isin(AGENT_CODES) | X.code2.isin(AGENT_CODES)).astype(int)
    d["either_agent_duty"] = d[["coderA_agent_duty", "coderB_agent_duty"]].max(axis=1)
    d["both_agent_duty"] = d[["coderA_agent_duty", "coderB_agent_duty"]].min(axis=1)
    for ref in ("coderA_agent_duty", "coderB_agent_duty", "both_agent_duty", "either_agent_duty"):
        y = d[ref]; f = d.flag
        tp, fp = int(((f == 1) & (y == 1)).sum()), int(((f == 1) & (y == 0)).sum())
        fn, tn = int(((f == 0) & (y == 1)).sum()), int(((f == 0) & (y == 0)).sum())
        p = tp / (tp + fp) if tp + fp else np.nan; r = tp / (tp + fn) if tp + fn else np.nan
        name = ref.replace("_agent_duty", "")
        for k, v in (("tp", tp), ("fp", fp), ("fn", fn), ("tn", tn)):
            add("lexical_flag_validation_count", f"ref={name}|{k}", v, len(d), "none")
        add("lexical_flag_validation_precision", f"ref={name}", round(p, 4), tp + fp, "none")
        add("lexical_flag_validation_recall", f"ref={name}", round(r, 4), tp + fn, "none")
        prec[name] = p
    add("coder_agreement_agent_duty", "A_vs_B", round(float((d.coderA_agent_duty == d.coderB_agent_duty).mean()), 4), len(d), "none")
    fpd = d[(d.flag == 1) & (d.either_agent_duty == 0)]
    for t in sorted({x for v in d.terms for x in v.split("|") if x}):
        add("lexical_flag_false_positives_with_term", f"term={t}", int(fpd.terms.str.split("|").map(lambda v: t in v).sum()), len(fpd), "none")
        add("lexical_flag_flagged_records_with_term", f"term={t}", int(d[d.flag == 1].terms.str.split("|").map(lambda v: t in v).sum()), int(d.flag.sum()), "none")
    FLAG_NOTE["value"] = (f"task-level precision {prec['coderA']:.2f} vs coder A, {prec['coderB']:.2f} vs coder B "
                          f"(200 real posting records)")
    d[["id", "flag", "terms", "coderA_codes", "coderB_codes", "coderA_agent_duty", "coderB_agent_duty"]] \
        .to_csv(OUT / "I1-lexical-flags.csv", index=False)
    print("validation:", FLAG_NOTE["value"])

if __name__ == "__main__":
    main()
