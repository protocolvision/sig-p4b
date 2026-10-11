"""Business-function map, defined once (functional analysis, descriptive; see design.md).

Assignment order for a posting:
  1. title keyword rules, first match wins, in the order SECURITY, LEGAL, SUPPORT, DATA_AI, SALES, then
     SOFTWARE (short list) and EXEC (chiefs, strategy);
  2. otherwise the O*NET detailed code (postings-mapped-v2.csv) by longest-prefix lookup in ONET_RULES
     (detailed 7-character code, then minor group "dd-d", then major group "dd");
  3. otherwise "other".
O*NET codes are model-assigned from titles with about 83% major-group accuracy (deviation 18); the
function map inherits that error. strip_ai=True removes AI/ML/automation/agent terms from the title before the
keyword step, so the AI term in the title does not itself decide the function (used for Q1).
"""
import re

FUNCTIONS = ["sales", "customer service/support", "marketing", "finance and accounting", "HR",
             "legal and compliance", "IT and infrastructure", "security", "software engineering",
             "data and AI/ML", "operations and supply chain", "manufacturing/field",
             "healthcare/clinical", "executive/strategy", "other"]

S, CS, MK, FI, HR, LG, IT, SE, SW, DA, OP, MF, HC, EX, OT = FUNCTIONS

# AI terms stripped from titles for Q1 (same list as deviation 14)
AI_TERM_RE = re.compile(r"(?<![\w.])(?:A\.I\.|AI|agentic|agents?|LLMs?|GenAI|generative AI|machine learning|"
                        r"automation|prompt|copilot|intelligent automation|RPA|responsible AI|model risk)(?![\w])", re.I)

def _re(words):
    return re.compile(r"(?<![A-Za-z])(?:" + "|".join(words) + r")(?![A-Za-z])", re.I)

TITLE_RULES = [
    (SE, _re([r"(?<!social )security\b(?! guard| officer| agent| supervisor| patrol)",
              r"cyber\w*", r"infosec", r"information security", r"appsec", r"application security", r"cloud security",
              r"product security", r"SOC (?:analyst|engineer)", r"threat \w+", r"vulnerabilit\w+", r"penetration test\w*",
              r"red team", r"detection (?:and|&) response", r"CISO", r"IAM", r"identity (?:and|&) access",
              r"trust (?:and|&) safety", r"fraud (?:analyst|investigator|operations)", r"abuse investigator",
              r"malware", r"DevSecOps", r"forensic\w*"])),
    (LG, _re([r"counsel", r"attorney", r"lawyer", r"legal", r"paralegal", r"litigation", r"privacy",
              r"compliance", r"regulatory affairs", r"contracts? (?:manager|administrator|specialist)", r"ethics"])),
    (CS, _re([r"customer (?:support|service|care|success|experience|operations|advocate|happiness)",
              r"(?:technical|product|premier|enterprise|application|IT) support", r"support (?:engineer|specialist|agent|"
              r"representative|rep|associate|analyst|manager|operations|lead)", r"help ?desk", r"service desk",
              r"contact cent(?:er|re)", r"call cent(?:er|re)", r"client (?:support|service|care)", r"member services?",
              r"customer service", r"care (?:advocate|agent)", r"technical account manager"])),
    (DA, _re([r"data scien\w+", r"data engineer\w*", r"data analy\w+", r"data architect\w*", r"data platform",
              r"data governance", r"data analytics", r"analytics", r"business intelligence", r"BI (?:analyst|developer|engineer)",
              r"machine learning", r"ML(?:Ops)?(?: engineer| scientist| researcher)?", r"MLOps", r"deep learning",
              r"applied scientist", r"research scientist", r"research engineer", r"AI (?:engineer|scientist|researcher|"
              r"architect|product|platform|lead|specialist|developer|solutions?)", r"NLP", r"computer vision", r"LLM\w*",
              r"data (?:and|&) AI", r"statistician", r"data modeler"])),
    (S, _re([r"sales", r"account (?:executive|manager|director|representative|rep)", r"business development",
             r"\bBDR\b", r"\bSDR\b", r"sales development", r"solutions? (?:engineer|consultant)",
             r"pre-?sales", r"partner(?:ship)?s? (?:manager|lead|director)", r"channel (?:manager|partner|\w+ engineer)",
             r"revenue (?:operations|enablement)", r"inside sales", r"territory", r"customer executive", r"go-to-market"])),
    (FI, _re([r"accounting", r"finance", r"financial (?:analyst|reporting|planning|controller|operations)", r"treasury",
              r"auditor", r"audit (?:manager|director|lead)", r"\btax\b", r"payroll", r"controller", r"FP&A",
              r"accounts? (?:payable|receivable)", r"actuar\w+", r"underwrit\w+"])),
    (HR, _re([r"recruit\w*", r"talent (?:acquisition|partner|management)", r"human resources", r"\bHR\b",
              r"people (?:partner|operations|business partner|analytics|experience)", r"compensation", r"benefits (?:manager|specialist|analyst)",
              r"learning (?:and|&) development"])),
    (MK, _re([r"marketing", r"brand\b", r"communications?", r"social media", r"\bSEO\b", r"demand gen\w*",
              r"content (?:marketing|strategist|creator|writer)", r"videograph\w+", r"public relations", r"creative (?:director|strategist)"])),
    (SW, _re([r"software", r"devops", r"site reliability", r"\bSRE\b", r"full[\s-]?stack", r"front[\s-]?end",
              r"back[\s-]?end", r"mobile (?:engineer|developer)", r"web developer", r"firmware", r"embedded software",
              r"platform engineer\w*", r"QA (?:engineer|automation)", r"test automation", r"SDET", r"developer",
              r"programmer", r"engineering manager"])),
    (EX, _re([r"chief", r"CEO", r"CTO", r"CIO", r"CFO", r"COO", r"president", r"chief of staff", r"strateg\w+",
              r"corporate development", r"general manager"])),
]

# O*NET lookups; longest prefix wins.
ONET_RULES = {
    # 11 management
    "11-1": EX, "11-1021": OP, "11-2": MK, "11-2022": S, "11-2023": S, "11-2031": MK, "11-2032": MK,
    "11-3": OP, "11-3012": OT, "11-3013": OP, "11-3021": IT, "11-3031": FI, "11-3051": MF, "11-3061": OP, "11-3071": OP,
    "11-3111": HR, "11-3121": HR, "11-3131": HR, "11-9": OT, "11-9021": MF, "11-9041": MF, "11-9111": HC, "11-9121": OT,
    "11-9141": OP, "11-9199": OP, "11-9151": OT, "11-9051": OT, "11-9072": OT,
    # 13 business and financial
    "13-1": OP, "13-1041": LG, "13-1071": HR, "13-1075": HR, "13-1081": OP, "13-1111": EX, "13-1141": HR, "13-1151": HR,
    "13-1161": MK, "13-1199": OP, "13-1031": FI, "13-1032": FI, "13-1131": OT, "13-1121": OP, "13-1082": OP,
    "13-1051": FI, "13-2": FI,
    # 15 computer and mathematical
    "15-1": IT, "15-1211": IT, "15-1212": SE, "15-1221": DA, "15-1231": IT, "15-1232": CS, "15-1241": IT, "15-1242": IT,
    "15-1243": DA, "15-1244": IT, "15-1251": SW, "15-1252": SW, "15-1253": SW, "15-1254": SW, "15-1255": MK,
    "15-1299": IT, "15-2": DA, "15-2031": OP,
    # 17 engineering
    "17": MF,
    # 19 science
    "19": OT, "19-4": MF, "19-5": MF,
    # 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55
    "21": OT, "23": LG, "25": OT, "27": OT, "27-1024": MK, "27-3": MK, "27-1": MK, "27-2": OT, "27-4": MK,
    "29": HC, "31": HC, "33": OT, "35": OT, "37": OT, "39": OT, "41": S, "41-9": S,
    "43": OT, "43-1": OT, "43-3": FI, "43-4": CS, "43-4161": HR, "43-4171": OT, "43-5": OP, "43-6": OT, "43-9": OT,
    "43-9061": OT, "43-3031": FI,
    "45": MF, "47": MF, "49": MF, "51": MF, "53": OP, "55": OT,
}

def _onet_function(code):
    if not isinstance(code, str) or len(code) < 2:
        return None
    for n in (7, 6, 4, 3, 2):
        f = ONET_RULES.get(code[:n])
        if f:
            return f
    return None

def assign(title, onet_code=None, strip_ai=False):
    """Return (function, source) where source is 'title', 'onet' or 'default'."""
    t = title or ""
    if strip_ai:
        t = AI_TERM_RE.sub(" ", t)
    for f, rx in TITLE_RULES:
        if rx.search(t):
            return f, "title"
    f = _onet_function(onet_code)
    if f:
        return f, "onet"
    return OT, "default"

def function_of(title, onet_code=None, strip_ai=False):
    return assign(title, onet_code, strip_ai)[0]
