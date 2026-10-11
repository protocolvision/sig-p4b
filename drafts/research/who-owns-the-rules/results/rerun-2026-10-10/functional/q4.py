"""Q4: reporting lines in AI-titled postings. AI-titled = group 'newtitle' (2,945; "agent (human)" titles excluded).
Raw text: corpus/b-raw/postings/*.jsonl, joined by doc_id = "P" + ats + "_" + board_id + "_" + id.
Phrase patterns:
  RT   reports to / reporting to / reports directly to / reports into / report to / reports functionally to / dotted line to
  PART "part of (the|our|a) <words> team|group|organization|department|function|org"  and "join(ing) the <words> team"
  WITHIN "(sits|sit|situated|housed|based) (within|in) (the) <words> (team|organization|org|department|group)"
The captured phrase (up to 14 words, cut at sentence end) is classified to a department by keyword rules (first match
in DEPT_RULES order). Phrases are NOT written to disk except the vetted examples placed in results.md; personal names are
detected by a capitalised-bigram check and such phrases are never used as examples."""
import re, glob
from common import *

T = Table()
p = load_postings()
ai = p[p.group == "newtitle"].copy()
need = set(ai.doc_id)
text = {}
for f in glob.glob(str(ROOT / "corpus/b-raw/postings/*.jsonl")):
    for line in open(f):
        r = json.loads(line)
        d = f"P{r['ats']}_{r['board_id']}_{r['id']}"
        if d in need:
            text[d] = r.get("description_text") or ""
print("joined", len(text), "of", len(need))
ai["has_text"] = ai.doc_id.isin(text)

RT = re.compile(r"\b(?:reports?|reporting|reports? directly|reporting directly|reports? functionally|reports? into|reporting into|dotted[\s-]line)\s+(?:to|into)\s+(?:the\s+|our\s+|a\s+|an\s+)?([^.;\n]{3,110})", re.I)
PART = re.compile(r"\b(?:part of|joins?|joining|member of|be on|within)\s+(?:the\s+|our\s+|a\s+|an\s+)([A-Za-z0-9&/,\- ]{2,70}?\s(?:team|group|organization|organisation|department|function|org|division))\b", re.I)

# department rules. A phrase goes to the rule whose keyword appears EARLIEST in the (trimmed) phrase; ties go to the
# rule listed first. Title words alone (manager, director, VP) do not name a department.
DEPT_RULES = [
    ("executive/strategy", r"\bCEO\b|chief executive|chief of staff|\bCOO\b|chief operating|business unit|\bGM\b|corporate strategy|\bstrategy\b"),
    ("security", r"\bCISO\b|\bCSO\b|security|cyber|trust (?:and|&) safety"),
    ("legal and compliance", r"general counsel|\blegal\b|\bcounsel\b|compliance|\brisk\b|privacy|governance"),
    ("finance and accounting", r"\bCFO\b|chief financial|finance|financial|accounting|controller|treasury"),
    ("HR", r"\bCHRO\b|\bHR\b|human resources|people (?:team|operations|ops|org)|talent|\bpeople\b"),
    ("data and AI/ML", r"chief (?:data|AI|analytics)|\bCDO\b|\bCAIO\b|data science|\bdata\b|\bAI\b|artificial intelligence|machine learning|\bML\b|analytics|research|applied science|\bscience\b|\bLLM\b"),
    ("software engineering", r"\bCTO\b|chief technology|engineering|engineer|software|developer|devops|\bSRE\b|platform|architect|\bR&D\b|technology"),
    ("IT and infrastructure", r"\bCIO\b|chief information|\bIT\b|information technology|infrastructure|enterprise (?:systems|applications)|digital transformation|business systems|\bsystems\b"),
    ("customer service/support", r"support|customer (?:success|service|experience|care|operations)|\bCX\b|service delivery|client services|professional services|customer care"),
    ("sales", r"\bCRO\b|chief revenue|sales|revenue|go[\s-]to[\s-]market|\bGTM\b|account|business development|partnerships?|alliances"),
    ("marketing", r"\bCMO\b|chief marketing|marketing|brand|communications|growth"),
    ("operations and supply chain", r"operations|\bops\b|supply chain|logistics|procurement|sourcing|fulfil+ment|planning|program management|\bPMO\b|transformation|process"),
    ("manufacturing/field", r"manufactur|plant|factory|production|field|quality|maintenance|reliability|mechanical|electrical|hardware|silicon"),
    ("product/design", r"\bCPO\b|chief product|product|\bUX\b|design"),
    ("healthcare/clinical", r"clinical|medical|health|nursing|pharmacy"),
]
DEPT_RX = [(d, re.compile(r, re.I)) for d, r in DEPT_RULES]
NONE_NAMED = "no function named"
ROLE0 = re.compile(r"(?:senior|sr|executive|vice|chief|head|director|manager|managing|associate|regional|global|group|division|department|principal|lead|leadership|vp|svp|evp|avp|cto|ceo|cio|cfo|coo|cmo|ciso|cpo|cro|president|supervisor|sales|engineering|ai|data|product|its|his|her|their|an?|the|our)$", re.I)
def classify(ph):
    best = None
    for i, (d, rx) in enumerate(DEPT_RX):
        m = rx.search(ph)
        if m and (best is None or (m.start(), i) < best[0]):
            best = ((m.start(), i), d)
    if best: return best[1]
    return NONE_NAMED

ABBR = re.compile(r"\b(Sr|Jr|Mr|Ms|Mrs|Dr|Inc|Ltd|Co|vs|St|U\.S|U\.K|No)\.", re.I)
CUT = re.compile(r"[.;:()|\n]|,\s*(?:you|this|the|who|and|where|which|while|he|she|they|our|we|a)\b|\s(?:you|and (?:work|will|is|has|be|serve|partner|collaborate)|who|where|which|while|"
                 r"based|in order|by|in the (?:US|United|UK|EU)|at the|for the|with the|on a)\b|\s[-\u2013\u2014]\s|\s(?:to|in|from)\s(?=[a-z])", re.I)

rows = []
for r in ai.itertuples():
    t = text.get(r.doc_id, "")
    t1 = ABBR.sub(lambda x: x.group(1), re.sub(r"\s+", " ", t))
    for kind, rx in (("reports_to", RT), ("part_of_team", PART)):
        for m in rx.finditer(t1):
            ph = m.group(1).strip()
            ph = CUT.split(ph)[0].strip(" ,")
            ph = " ".join(ph.split()[:9])
            if len(ph) < 3: continue
            w0 = ph.split()[0]
            if w0[0].islower() and kind == "reports_to" and not ROLE0.match(w0): continue   # "reports to monitor ..." (verb), not a reporting line
            a0 = t1.rfind(". ", 0, m.start()) + 2
            b0 = t1.find(". ", m.end())
            sent = t1[a0 if a0 > 1 else 0: (b0 + 1) if b0 > 0 else len(t1)]
            rows.append(dict(doc_id=r.doc_id, fn=r.fn, kind=kind, dept=classify(ph), phrase=ph, sent=sent))
ph = pd.DataFrame(rows)
print(ph.groupby("kind").doc_id.nunique(), ph.groupby(["kind", "dept"]).size().unstack(0))

# ---- tables ----
n_ai = len(ai)
T.add("Q4", "ALL", "ai_titled_postings", n_ai, None, None, n_ai)
T.add("Q4", "ALL", "ai_titled_with_text", int(ai.has_text.sum()), None, None, n_ai)
for kind in ("reports_to", "part_of_team"):
    k = ph[ph.kind == kind].doc_id.nunique()
    pr, lo, hi = wilson(k, n_ai)
    T.add("Q4", "ALL", f"share_with_{kind}_phrase", pr, lo, hi, n_ai)
    first = ph[ph.kind == kind].drop_duplicates("doc_id")          # one phrase per posting (the first one)
    for d, c in first.dept.value_counts().items():
        pr, lo, hi = wilson(int(c), len(first))
        T.add("Q4", "ALL", f"{kind}_dept:{d}", int(c), None, None, len(first))
        T.add("Q4", "ALL", f"{kind}_dept_share:{d}", pr, lo, hi, len(first))
    for f in FUNCTIONS:
        base = ai[ai.fn == f]
        sub = first[first.fn == f]
        if not len(base): continue
        pr, lo, hi = wilson(len(sub), len(base))
        T.add("Q4", f, f"share_with_{kind}_phrase", pr, lo, hi, len(base))
        for d, c in sub.dept.value_counts().items():
            T.add("Q4", f, f"{kind}_dept:{d}", int(c), None, None, len(sub))
# reports-to the same function as the posting's own, by function
SAME = {"data and AI/ML": "data and AI/ML", "software engineering": "software engineering", "security": "security",
        "IT and infrastructure": "IT and infrastructure", "sales": "sales", "marketing": "marketing", "legal and compliance": "legal and compliance",
        "finance and accounting": "finance and accounting", "HR": "HR", "customer service/support": "customer service/support",
        "operations and supply chain": "operations and supply chain", "manufacturing/field": "manufacturing/field"}
first = ph[ph.kind == "reports_to"].drop_duplicates("doc_id")
for f in FUNCTIONS:
    sub = first[first.fn == f]
    if len(sub):
        k = int((sub.dept == f).sum()); pr, lo, hi = wilson(k, len(sub))
        T.add("Q4", f, "reports_to_own_function_share", pr, lo, hi, len(sub))
T.df().to_csv(OUT / "tables-q4.csv", index=False)
# posting-level class file without phrase text
ph.drop(columns=["phrase", "sent"]).to_csv(OUT / "q4-phrase-classes.csv", index=False)
ph.to_pickle("/private/tmp/claude-501/-Users-rafa-Documents-protocolvision/cd04e152-b645-4bd3-a751-c964607667c6/scratchpad/q4-phrases.pkl")

# ---- verbatim examples: one sentence, <= 40 words, scrubbed, no personal names (capitalised-bigram screen + manual read) ----
SCRUB = [(re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "[email]"), (re.compile(r"https?://\S+|www\.\S+"), "[link]"),
         (re.compile(r"\+?\d[\d\s().-]{8,}\d"), "[phone]")]
SAFE = set(w.lower() for d, r_ in DEPT_RULES for w in re.findall(r"[A-Za-z]{3,}", r_)) | set("""senior director vice president head global
 team group organization department manager lead leader leadership chief officer technology software engineering product data science
 research platform operations security legal finance sales marketing customer success support strategy transformation digital enterprise
 applied generative agentic intelligence machine learning automation engineer engineers principal staff associate regional americas emea
 apac north america europe united states you will report reports reporting directly the our this role position part join joining
 new innovation business corporate technical solutions services program programs office executive""".split())
def name_safe(sent):
    toks = re.findall(r"\b[A-Z][a-z]+\b", sent)
    caps = [m for m in re.finditer(r"(?<![.!?]\s)\b([A-Z][a-z]+) ([A-Z][a-z]+)\b", sent)]
    for m in caps:
        if m.group(1).lower() not in SAFE and m.group(2).lower() not in SAFE:
            return False
    return not re.search(r"\b(?:Mr|Ms|Mrs|Dr)\b|@|\bcontact\b", sent)
EXCLUDE = {"Pworkday_myhrabc_R2615880"}   # multi-line report (solid + dotted); the classifier took the second line
ex = []
for kind, depts in (("reports_to", ["data and AI/ML", "software engineering", "security", "executive/strategy", "sales", "finance and accounting",
                                     "legal and compliance", "IT and infrastructure", "marketing", "operations and supply chain", "HR"]),
                    ("part_of_team", ["data and AI/ML", "security", "software engineering"])):
    for d in depts:
        c = ph[(ph.kind == kind) & (ph.dept == d)].sample(frac=1, random_state=7)
        for r in c.itertuples():
            if r.doc_id in EXCLUDE: continue
            sent = r.sent
            for rx, rep in SCRUB: sent = rx.sub(rep, sent)
            if len(sent.split()) <= 40 and name_safe(sent) and len(sent.split()) >= 8:
                ex.append(dict(kind=kind, dept=d, posting_id=r.doc_id, function_of_posting=r.fn, text=sent)); break
pd.DataFrame(ex).to_csv(OUT / "q4-examples.csv", index=False)
print(pd.DataFrame(ex)[["kind", "dept", "posting_id", "text"]].to_string())
