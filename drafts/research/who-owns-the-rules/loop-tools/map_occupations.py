"""Map job-posting titles to O*NET-SOC codes with a fixed title dictionary.

Needs Python 3.9+, standard library only, and the O*NET text files in corpus/b-raw/onet/ (see VERSION.txt).

Usage:
  python3 map_occupations.py IN.jsonl OUT.csv

IN.jsonl has one object per line with fields `id` and `title`, and optionally `department` (passed through).
OUT.csv columns: id, title, normalised, onet_code, method, onet_title, study_occupation, candidate_code,
candidate_method, department

Both sides (posting titles and O*NET titles) are singularised before lookup (Pharmacists -> pharmacist).
Lead, staff and head of are removed only as leading seniority words followed by a function noun
("Staff Software Engineer" -> software engineer; "Staff Accountant", "Lead Generation" are kept).

Order of matching (first hit wins):
  override   fixed table below, for the ten study occupations (study_occupation is filled only here)
  exact      normalised title equals a normalised O*NET occupation title
  alternate  ... equals an O*NET alternate title ("Job Titles.txt" in release 31.0)
  reported   ... equals an O*NET sample-of-reported-title
  model      EVERY other title. onet_code is empty. Dictionary hits are candidates only: `candidate_code`
             holds the best hit and `candidate_method` its level (exact, alternate, reported, fallback, or
             fallback-low when the matched title covers < 60% of the posting's tokens). assign_titles_model.py
             resolves these titles with the Message Batches API.
  unmatched  the title is empty after normalisation
Ties, at every step: most specific match first (fallback: most tokens), then the SOC code with the most
dictionary titles (the most common code), then the lowest code. Nothing is random.
"""
import csv, json, pathlib, re, sys
from collections import Counter, defaultdict

HERE = pathlib.Path(__file__).resolve().parent
ONET = HERE.parent / "corpus" / "b-raw" / "onet"

# Fixed override table for the ten study occupations, so their common variants map correctly whatever
# the O*NET dictionary says. Each row: (study occupation, O*NET-SOC code, groups). A title matches when,
# for every group, at least one alternative has all of its words present in the normalised title
# (any order). Rows are tried in order. Codes are the study's chosen O*NET home for each occupation;
# several occupations share 11-1021.00 (no closer O*NET occupation), so study_occupation is what
# separates them.
# Words that make a "controller" title something other than the finance role (C5, fix 3). The S1 walk's
# sel.py regex is not in the repo (C6 asks for it to be committed); this is the reviewer's list.
CONTROLLER_EXCLUDE_PHRASES = ["air traffic"]
CONTROLLER_EXCLUDE_WORDS = {"project", "production", "motor", "firmware", "plc", "network", "domain", "cost",
                            "credit", "quality", "inventory"}
# Head-level words accepted wherever the study occupation is an operations manager role (C5, fix 4).
HEAD = ["manager", "director", "head", "vp", "vice president", "lead"]

OVERRIDES = [
    ("controller", "11-3031.01", [["controller"]]),
    ("accounts payable specialist", "43-3031.00", [["accounts payable", "ap"], ["specialist"]]),
    ("support operations manager", "11-1021.00", [["support operations", "support ops"], HEAD]),
    ("revenue operations manager", "11-2022.00", [["revenue operations", "revenue ops", "revops"], HEAD]),
    ("procurement specialist", "13-1023.00", [["procurement"], ["specialist"]]),
    ("legal operations manager", "11-1021.00", [["legal operations", "legal ops"], HEAD]),
    ("HR operations specialist", "13-1071.00",
     [["hr", "human resource", "human resources", "people"], ["operations", "ops"], ["specialist"]]),
    ("identity and access administrator", "15-1244.00",
     [["identity access", "identity and access", "iam"], ["administrator", "admin"]]),
    ("compliance analyst", "13-1041.00", [["compliance"], ["analyst"]]),
    ("platform engineer", "15-1252.00", [["platform"], ["engineer"]]),
]

SENIORITY = {"senior", "sr", "junior", "jr", "principal", "i", "ii", "iii", "ll"}
FIELDS = ["id", "title", "normalised", "onet_code", "method", "onet_title", "study_occupation", "candidate_code",
          "candidate_method", "department"]
FALLBACK_COVER = 0.60

# "lead" and "staff" are seniority only as the first word of a title and only before a function noun.
LEAD_NEXT = {"engineer", "developer", "designer", "analyst", "scientist", "architect", "researcher",
             "programmer", "consultant", "recruiter", "administrator", "technician", "specialist", "manager",
             "software", "data", "product", "program", "project", "security", "backend", "frontend", "ml",
             "ai", "cloud", "devops", "qa", "ux", "ui"}
STAFF_NEXT = {"engineer", "developer", "designer", "scientist", "architect", "researcher", "software",
              "data", "machine", "ml", "ai", "product", "program", "security", "backend", "frontend",
              "cloud", "devops", "qa", "ux", "ui", "technical", "applied", "research"}
# words that look plural but are not
NO_SINGULAR = {"sales", "analysis", "business", "process"}


def singular(w):
    """Plain rule-based singulariser: pharmacists -> pharmacist, secretaries -> secretary, boxes -> box."""
    if len(w) <= 3 or w.endswith(("ss", "us", "is", "ics")) or w in NO_SINGULAR:
        return w
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"
    if w.endswith(("sses", "xes", "ches", "shes", "zes")):
        return w[:-2]
    if w.endswith("s"):
        return w[:-1]
    return w


def normalise(t, strip_lead=True):
    """Lower-case, drop location/brackets/punctuation/seniority, singularise. With strip_lead=False the
    words lead, staff and head of are kept (used by the override table, which wants head-level words)."""
    t = t.lower().split("|")[0]                      # "Title | Location" -> title
    for _ in range(3):                               # bracketed text, nested or stray
        t = re.sub(r"\([^()]*\)|\[[^\[\]]*\]|\{[^{}]*\}", " ", t)
    t = t.replace("&", " and ")
    t = re.sub(r"[^a-z0-9]+", " ", t)                # punctuation (incl. en/em dashes)
    toks = [singular(w) for w in t.split() if w not in SENIORITY]
    if strip_lead:
        # drop seniority words anywhere only if leading (after any other seniority word was removed)
        if toks[:2] == ["head", "of"] and len(toks) > 2:
            toks = toks[2:]
        elif len(toks) > 1 and toks[0] == "lead" and toks[1] in LEAD_NEXT:
            toks = toks[1:]
        elif len(toks) > 1 and toks[0] == "staff" and toks[1] in STAFF_NEXT:
            toks = toks[1:]
    return " ".join(toks)


def read_tsv(name):
    with open(ONET / name, encoding="utf-8") as f:
        rd = csv.reader(f, delimiter="\t")
        next(rd)
        return [r for r in rd if r]


def build():
    """Return (index, code_titles, onet_title_of_code). index: normalised title -> {level: {code: raw title}}."""
    occ = {r[0]: r[1] for r in read_tsv("Occupation Data.txt")}
    index = defaultdict(lambda: defaultdict(dict))
    sources = [("exact", [(c, t) for c, t in occ.items()]),
               ("alternate", [(r[0], r[1]) for r in read_tsv("Job Titles.txt")]),
               ("reported", [(r[0], r[1]) for r in read_tsv("Sample of Reported Titles.txt")])]
    for level, rows in sources:
        for code, raw in rows:
            n = normalise(raw)
            if n:
                index[n][level].setdefault(code, raw)
    code_count = Counter(c for lv in index.values() for d in lv.values() for c in d)
    return index, code_count, occ


def pick(cands, code_count):
    return sorted(cands, key=lambda c: (-code_count[c], c))[0]


class Mapper:
    def __init__(self):
        self.index, self.code_count, self.occ = build()
        self.df = Counter(w for n in self.index for w in set(n.split()))
        self.by_key = defaultdict(list)              # rarest token -> multi-token dictionary titles
        for n in self.index:
            toks = n.split()
            if len(toks) >= 2:
                self.by_key[min(set(toks), key=lambda w: (self.df[w], w))].append((n, frozenset(toks)))

    def override(self, norm):
        padded = f" {norm} "
        for study, code, groups in OVERRIDES:
            if study == "controller" and (any(f" {p} " in padded for p in CONTROLLER_EXCLUDE_PHRASES)
                                          or CONTROLLER_EXCLUDE_WORDS & set(norm.split())):
                continue
            if all(any(all(f" {w} " in padded for w in a.split())
                       for a in (normalise(x, False) for x in g)) for g in groups):
                return study, code
        return None

    def map(self, title):
        """Return (normalised, code, method, onet_title, study_occupation, candidate_code, candidate_method).
        Only the study-occupation override table assigns a code. Every other title gets method "model"; the
        best dictionary hit (exact, alternate, reported or fallback) is kept as candidate_code/candidate_method."""
        raw_norm = normalise(title, strip_lead=False)
        norm = normalise(title)
        if not norm:
            return norm, "", "unmatched", "", "", "", ""
        ov = self.override(raw_norm)
        if ov:
            return norm, ov[1], "override", self.occ.get(ov[1], ""), ov[0], "", ""
        hit = self.index.get(norm)
        if hit:
            for level in ("exact", "alternate", "reported"):
                if level in hit:
                    return norm, "", "model", "", "", pick(hit[level], self.code_count), level
        toks = set(norm.split())
        best = None
        for w in toks:
            for n, ts in self.by_key.get(w, ()):
                if ts <= toks:
                    codes = {c for d in self.index[n].values() for c in d}
                    c = pick(codes, self.code_count)
                    key = (-len(ts), -self.code_count[c], c)
                    if best is None or key < best[0]:
                        best = (key, c)
        if best:
            cover = -best[0][0] / len(toks)
            return norm, "", "model", "", "", best[1], "fallback" if cover >= FALLBACK_COVER else "fallback-low"
        return norm, "", "model", "", "", "", ""


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    m = Mapper()
    n = Counter()
    with open(sys.argv[1], encoding="utf-8") as fin, open(sys.argv[2], "w", newline="", encoding="utf-8") as fout:
        w = csv.writer(fout)
        w.writerow(FIELDS)
        for line in fin:
            if not line.strip():
                continue
            r = json.loads(line)
            norm, code, method, otitle, study, cand, cmeth = m.map(r["title"])
            n[method] += 1
            w.writerow([r["id"], r["title"], norm, code, method, otitle, study, cand, cmeth, r.get("department", "")])
    print(f"dictionary: {len(m.index)} normalised titles, {len(m.code_count)} codes", file=sys.stderr)
    print("; ".join(f"{k} {v}" for k, v in n.most_common()), file=sys.stderr)


if __name__ == "__main__":
    main()
