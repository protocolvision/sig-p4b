#!/usr/bin/env python3
"""I1 labour-market measures, exactly as fixed in deviations.md items 14, 18, 21.
Run with loop-tools/.venv/bin/python from the study root. Writes
results/rerun-2026-10-10/instruments/I1-tables.csv and I1-lexical-flags.csv.
Does not read any *-key.json file."""
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

# ---------- US vs non-US from location text ----------
US_STATES = set("AL AK AZ AR CA CO CT DE FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY DC PR".split())
US_WORD = re.compile(r"\b(?:USA|U\.S\.A?\.?|United States(?: of America)?|US)\b")
US_STATE_NAMES = ("Alabama Alaska Arizona Arkansas California Colorado Connecticut Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota Mississippi Missouri Montana Nebraska Nevada Ohio Oklahoma Oregon Pennsylvania Tennessee Texas Utah Vermont Virginia Washington Wisconsin Wyoming New York|New Jersey|New Mexico|New Hampshire|North Carolina|South Carolina|North Dakota|South Dakota|Rhode Island|West Virginia|District of Columbia").split()
US_CITIES = ["New York","NYC","San Francisco","Chicago","San Jose","Boise","Houston","Charlotte","Atlanta","Boston","Austin","North Chicago","Seattle","Los Angeles","Dallas","Denver","Phoenix","Philadelphia","Pittsburgh","Minneapolis","Detroit","Santa Clara","Sunnyvale","Mountain View","Palo Alto","Redwood City","San Diego","San Mateo","Cupertino","Milpitas","Fremont","Menlo Park","Washington DC","Washington, D.C.","Salt Lake City","Nashville","Columbus","Cincinnati","Cleveland","St. Louis","Kansas City","Omaha","Portland","Raleigh","Richmond","Tampa","Miami","Orlando","Irvine","Plano","Irving","Memphis","Louisville","Indianapolis","Milwaukee","Baltimore","Hartford","Stamford","Cambridge","Bentonville","Springdale","Arlington","Remote - US","Remote US","Fab 10N","Fab 10X","Fab 10","Evendale","Boulder","Durham","Bellevue","Redmond","Oakland","Sacramento","Burlington","Wilmington","Newark","Jersey City","Rochester","Albany","Buffalo","Honolulu","Anchorage","Las Vegas","Tucson","Albuquerque","Oklahoma City","Tulsa","Jacksonville","New Orleans","Birmingham","Greenville","Peoria","Moline","Des Moines","Madison","Toledo","Akron","Dayton","Lexington","Knoxville","Chattanooga","Savannah","Charleston","Norfolk","Reston","McLean","Herndon","Bethesda","Rockville","Princeton","Parsippany","Bridgewater","Tarrytown","Sleepy Hollow","Niskayuna","Schenectady","Rensselaer","Grand Rapids","Longmont","Clearwater","Kalamazoo","Grand Forks","Burns Harbor","Stafford","Kohl's","AutoNation","Charles City","Bangor","Lincoln","Warren","Pennington"]
NONUS = ["India","Bangalore","Bengaluru","Hyderabad","Pune","Mumbai","Chennai","Gurgaon","Gurugram","Noida","Delhi","Kolkata","Singapore","London","United Kingdom","UK","England","Scotland","Wales","Ireland","Dublin","Seoul","Korea","Tokyo","Japan","Osaka","China","Shanghai","Beijing","Shenzhen","Hong Kong","Taiwan","Taipei","Taichung","Hsinchu","Canada","Toronto","Vancouver","Montreal","Ottawa","Calgary","Mexico","Brazil","Brasil","Argentina","Chile","Colombia","Peru","Germany","Munich","Berlin","France","Paris","Spain","Madrid","Barcelona","Italy","Milan","Florence","Rome","Netherlands","Amsterdam","Belgium","Brussels","Poland","Warsaw","Krakow","Romania","Bucharest","Bulgaria","Sofia","Hungary","Budapest","Czech","Prague","Portugal","Lisbon","Sweden","Stockholm","Norway","Denmark","Finland","Switzerland","Zurich","Austria","Vienna","Turkey","Istanbul","Israel","Tel Aviv","UAE","United Arab Emirates","Dubai","Abu Dhabi","Saudi","Riyadh","Bahrain","Egypt","Cairo","South Africa","Johannesburg","Nigeria","Kenya","Australia","Sydney","Melbourne","New Zealand","Philippines","Manila","Pasig","Malaysia","Kuala Lumpur","Penang","Thailand","Bangkok","Vietnam","Indonesia","Jakarta","Pakistan","Sri Lanka","Bangladesh","Costa Rica","Panama","Guatemala","Dominican","Puerto Rico?","EMEA","APAC","LATAM","Ukraine","Greece","Serbia","Croatia","Slovakia","Lithuania","Latvia","Estonia","Luxembourg","Morocco","Ghana","Guadalajara","Cork","Limerick","Mississauga","Quebec","Ontario","Chihuahua","Ho Chi Minh","Villeurbanne","Belfort","Nhon Trach","Ranjangaon","Sanchong","Tanauan","Quezon","Taguig","Petaling","Benalm\u00e1dena","Martillac","Nouvelle-Aquitaine","Sao Bernardo","Tbilisi","Guangzhou","Lyon","Massy","Kwidzyn","Markham","Brossard","Bromont","Canadian Head Office","Uzhhorod","Thailand","Monterrey","Tijuana","Bogota","Lima","Santiago","Buenos Aires","Sao Paulo","S\u00e3o Paulo"]
def _wb(words):
    return re.compile(r"(?<![A-Za-z])(?:" + "|".join(re.escape(w) for w in words) + r")(?![A-Za-z])", re.I)
NONUS_RE = _wb([w for w in NONUS if not w.endswith("?")])
US_CITY_RE = _wb(US_CITIES)
US_STATE_NAME_RE = _wb([x for part in US_STATE_NAMES for x in part.split("|")])
STATE_TOKEN = re.compile(r"(?:,\s*|\s-\s*|\s)(" + "|".join(sorted(US_STATES)) + r")(?=$|[\s,\-/;0-9])")
STATE_TOKEN_FIRST = re.compile(r"^(" + "|".join(sorted(US_STATES)) + r")\s*[-,/]\s")

ISO3 = re.compile(r"^(?:CAN|BRA|VNM|ESP|PHL|MYS|MEX|IND|CHN|JPN|KOR|GBR|DEU|FRA|ITA|NLD|POL|ROU|HUN|SGP|TWN|THA|IDN|IRL|CA-[A-Z]{2}|PH-[A-Z]+|BR-[A-Z]{2}|MX-[A-Z]+|PL-[0-9A-Z]+|GEO|TUN)(?![A-Za-z])")
REMOTE_ST = re.compile(r"^Remote\s*[-,(]\s*(?:Any State|(" + "|".join(sorted(US_STATES)) + r"))\b")

def us_class(loc):
    """Return 'us', 'non-us' or 'unknown'. Multi-location strings use the first listed location."""
    if not isinstance(loc, str) or not loc.strip():
        return "unknown"
    s = re.split(r";|\||\bor\b|\band\b(?= [A-Z])", loc)[0].strip() or loc
    if ISO3.search(s.strip()): return "non-us"
    if REMOTE_ST.search(s.strip()): return "us"
    # explicit US words win over city lists
    if US_WORD.search(s) and not NONUS_RE.search(US_WORD.sub("", s)):
        return "us"
    if NONUS_RE.search(s):
        return "non-us"
    if STATE_TOKEN.search(s) or STATE_TOKEN_FIRST.search(s) or US_STATE_NAME_RE.search(s) or US_CITY_RE.search(s):
        return "us"
    return "unknown"

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
def add(measure, slice_, value, n, weighting):
    rows.append(dict(measure=measure, slice=slice_, value=value, n=n, weighting=weighting))

def main():
    sel = pd.read_csv(ROOT / "corpus/b-raw/mapping/selection.csv")
    sel["doc_id"] = "P" + sel.ats + "_" + sel.board_id.astype(str) + "_" + sel.posting_id.astype(str)
    mp = pd.read_csv(ROOT / "corpus/b-raw/mapping/postings-mapped-v2.csv")
    sel = sel.merge(mp[["ats","board_id","posting_id","major_group","location","department"]],
                    on=["ats","board_id","posting_id"], how="left")
    sel["us"] = sel.location.map(us_class)
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
    pflag = tasks.groupby("doc_id").flag.any()
    sel["n_tasks"] = sel.doc_id.map(tasks.groupby("doc_id").size()).fillna(0).astype(int)
    sel["ai_duty"] = sel.doc_id.map(pflag).fillna(False).astype(bool)

    # cluster assignments / labels
    a = pd.read_csv(R / "clusters/leaf/assignments.csv.gz")
    lab = pd.read_csv(R / "clusters/leaf/labels.csv")
    artefacts = artefact_rule()
    lab["artefact"] = lab.cluster_id.isin(artefacts)
    a["doc_id"] = "P" + a.ats + "_" + a.board_id.astype(str) + "_" + a.posting_id.astype(str)
    a = a.merge(lab[["cluster_id","function_family","business_or_technical","found","artefact"]], on="cluster_id", how="left")
    PRIMARY = {2, 19, 43, 67, 69, 76, 83, 111}
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
    sel["has_prim"] = sel.doc_id.isin(base_prim); sel["cross_prim"] = sel.doc_id.map(prim).fillna(False).astype(bool)
    sel["has_sec"] = sel.doc_id.isin(base_sec); sel["cross_sec"] = sel.doc_id.map(sec).fillna(False).astype(bool)

    sel["cat"] = np.select([sel.group == "newtitle", sel.group == "newtitle-agent-human", sel.group == "S1"],
                           ["new_title", "new_title_human_agent", "study_occupation"], "rest_sample")
    sel["existing_all"] = sel.group.isin(["S1", "rest20"])   # all non-new-title postings
    sel["existing_s1"] = sel.group == "S1"
    sel["w_emp"] = 1.0 / sel.groupby("employer").doc_id.transform("count")   # each employer weight 1

    ARTIFACT_NOTE = ",".join(map(str, sorted(artefacts)))
    add("language_artefact_clusters", ARTIFACT_NOTE, len(artefacts), len(lab), "none")
    add("selected_postings", "all", len(sel), len(sel), "none")
    for g, d in sel.groupby("group"): add("selected_postings", f"group={g}", len(d), len(d), "none")
    add("postings_with_extracted_tasks", "all", int((sel.n_tasks > 0).sum()), len(sel), "none")
    add("us_class_postings", "all", int((sel.us == "us").sum()), len(sel), "none")
    for k in ("us","non-us","unknown"): add("us_class_postings", k, int((sel.us == k).sum()), len(sel), "none")

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
        for lab_, mask in (("study_occupation", d.existing_s1), ("all_non_new_title", d.existing_all)):
            e = d[mask]
            nflag_u = int(e.ai_duty.sum()); nflag_w = float(e.w_emp[e.ai_duty].sum())
            new = d[d.group == "newtitle"]
            nnew_u = len(new); nnew_w = float(new.w_emp.sum())
            add(f"existing_with_ai_duty[{lab_}]", name, nflag_u, len(e), "unweighted")
            add(f"existing_with_ai_duty[{lab_}]", name, round(nflag_w, 4), len(e), "employer-weighted")
            add("new_title_postings", name, nnew_u, nnew_u, "unweighted")
            add("new_title_postings", name, round(nnew_w, 4), nnew_u, "employer-weighted")
            add(f"absorption_ratio[{lab_}]", name, round(nflag_u / nnew_u, 4) if nnew_u else np.nan, nnew_u, "unweighted")
            add(f"absorption_ratio[{lab_}]", name, round(nflag_w / nnew_w, 4) if nnew_w else np.nan, nnew_u, "employer-weighted")
            add(f"share_existing_with_ai_duty[{lab_}]", name, round(nflag_u / len(e), 4) if len(e) else np.nan, len(e), "unweighted")
            add(f"share_existing_with_ai_duty[{lab_}]", name, round(nflag_w / e.w_emp.sum(), 4) if len(e) else np.nan, len(e), "employer-weighted")
    add("share_new_title_with_ai_duty", "all", round(sel[sel.group=="newtitle"].ai_duty.mean(), 4), int((sel.group=="newtitle").sum()), "unweighted")
    add("share_new_title_human_agent_with_ai_duty", "all", round(sel[sel.group=="newtitle-agent-human"].ai_duty.mean(), 4), int((sel.group=="newtitle-agent-human").sum()), "unweighted")
    # employers with >=1
    for lab_, mask in (("study_occupation", sel.existing_s1), ("all_non_new_title", sel.existing_all)):
        add(f"employers_with_ai_duty_existing[{lab_}]", "all", int(sel[mask & sel.ai_duty].employer.nunique()), int(sel.employer.nunique()), "employer")
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
                w = d.w_emp
                add(f"cross_function_share[{lvl}]", cn, round(float((d[cr] * w).sum() / w.sum()), 4), len(d), "employer-weighted")
            add(f"cross_function_count[{lvl}]", cn, int(d[cr].sum()) if len(d) else 0, len(d), "unweighted")
            add(f"postings_in_{lvl}_clusters", cn, int((cm & sel[has]).sum()), int(cm.sum()), "unweighted")
        for t, d0 in sel.groupby("employer_type"):
            for cn in ("new_title","other_postings"):
                d = d0[cats[cn].loc[d0.index] & d0[has]]
                add(f"cross_function_share[{lvl}]", f"{cn}|type={t}", round(d[cr].mean(), 4) if len(d) else np.nan, len(d), "unweighted")
    add("postings_with_pooled_tasks", "all", int(sel.in_pool.sum()), len(sel), "none")

    # ---- new-title spread
    def spread(key):
        for k, d in sel.groupby(key):
            emp = d.groupby("employer").agg(nt=("group", lambda x: int((x == "newtitle").sum())), n=("group", "size"))
            add("employers", f"{key}={k}", len(emp), len(emp), "employer")
            add("new_title_postings_per_employer_mean", f"{key}={k}", round(emp.nt.mean(), 4), len(emp), "employer")
            add("new_title_postings_per_employer_median", f"{key}={k}", float(emp.nt.median()), len(emp), "employer")
            add("employers_with_ge1_new_title", f"{key}={k}", int((emp.nt > 0).sum()), len(emp), "employer")
            add("share_employers_with_ge1_new_title", f"{key}={k}", round(float((emp.nt > 0).mean()), 4), len(emp), "employer")
            add("new_title_postings_total", f"{key}={k}", int(emp.nt.sum()), int(emp.n.sum()), "none")
            add("new_title_share_of_selected_postings", f"{key}={k}", round(emp.nt.sum() / emp.n.sum(), 4), int(emp.n.sum()), "none")
    spread("employer_type"); spread("sector")
    add("employers", "all", int(sel.employer.nunique()), int(sel.employer.nunique()), "employer")
    emp = sel.groupby("employer").group.apply(lambda x: int((x == "newtitle").sum()))
    add("employers_with_ge1_new_title", "all", int((emp > 0).sum()), len(emp), "employer")
    add("share_employers_with_ge1_new_title", "all", round(float((emp > 0).mean()), 4), len(emp), "employer")
    add("new_title_postings_per_employer_mean", "all", round(emp.mean(), 4), len(emp), "employer")
    add("new_title_postings_per_employer_median", "all", float(emp.median()), len(emp), "employer")
    add("new_title_postings_per_employer_max", "all", int(emp.max()), len(emp), "employer")
    for k in ("employer_type","sector"):
        for (kv, t), d in sel[sel.group == "newtitle"].groupby([k, "term"]):
            add("new_title_postings_by_term", f"{k}={kv}|term={t}", len(d), len(d), "none")

    # ---- major groups (descriptive; ~83% accurate per item 18)
    for cat, d in (("new_title", sel[sel.group=="newtitle"]), ("study_occupation", sel[sel.group=="S1"]), ("rest_sample", sel[sel.group=="rest20"])):
        vc = d.major_group.dropna().astype(int).astype(str).str.zfill(2).value_counts()
        for g, v in vc.items():
            add("major_group_share[descriptive; major group correct ~83%]", f"{cat}|major_group={g}", round(v / vc.sum(), 4), int(v), "unweighted")
    d = sel[(sel.group == "newtitle")]
    for g, dd in d.groupby("major_group"):
        if len(dd): add("major_group_new_title_ai_duty_share[descriptive; ~83%]", f"major_group={int(g):02d}", round(dd.ai_duty.mean(), 4), len(dd), "unweighted")

    pd.DataFrame(rows).to_csv(OUT / "I1-tables.csv", index=False)
    sel.drop(columns=["w_emp"]).to_csv(OUT / "I1-posting-level.csv.gz", index=False)
    unknown = sel[sel.us == "unknown"].location.value_counts().head(40)
    print("unknown-location top:", unknown.to_dict())
    print("artefacts:", sorted(artefacts))
    validate()

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

def validate():
    """Lexical flag on real posting records of the coding pool (id, flag). Real = span equals a Haiku task span."""
    tasks = pd.read_json(ROOT / "corpus/b-raw/extract/postings-haiku-all.tasks.jsonl", lines=True)
    real = set(tasks.span.str.strip())
    pool = [json.loads(l) for l in open(ROOT / "corpus/b-raw/coding/record-pool.jsonl")]
    rec = [r for r in pool if r["kind"] == "posting"]
    out = pd.DataFrame([{"id": r["id"], "flag": int(lex_flag(r["span"])), "real": r["span"].strip() in real} for r in rec])
    print("posting records:", len(out), "real:", int(out.real.sum()), "flagged real:", int(out[out.real].flag.sum()), "flagged non-real:", int(out[~out.real].flag.sum()))
    out[out.real][["id", "flag"]].to_csv(OUT / "I1-lexical-flags.csv", index=False)

if __name__ == "__main__":
    main()
