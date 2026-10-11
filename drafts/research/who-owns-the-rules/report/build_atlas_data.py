"""Build report/data/atlas.json for the agent controls atlas from the committed CSVs.

Every number the page draws comes from results/rerun-2026-10-10/controls-atlas/. Labels for the 14 objects, 11
enforcement points and 7 mechanisms follow taxonomy.md; the four object families and the short cluster labels on the
map are presentation only (ours). Usage: python3 build_atlas_data.py
"""
import csv, json, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE.parent / "results/rerun-2026-10-10/controls-atlas"
def rows(name): return list(csv.DictReader(open(SRC / name, encoding="utf-8")))

# objects: full name (taxonomy.md), short label, code (timeline-analysis.md), family (presentation only)
OBJ = [
    ("Harmful and off-limits content", "Harmful content", "HARM", 0),
    ("Prompt attacks and untrusted input", "Prompt attacks", "PI", 0),
    ("Sensitive data in prompts and outputs", "Sensitive data", "SENS", 0),
    ("Answer accuracy and presentation", "Answer accuracy", "ACC", 0),
    ("Agent tools and actions", "Tools and actions", "TOOL", 1),
    ("Autonomy and human handover", "Autonomy, handover", "AUTO", 1),
    ("Data and files the AI can reach", "Data it can reach", "DATA", 1),
    ("Network destinations", "Network", "NET", 1),
    ("Identity, credentials and access rights", "Identity, access", "ID", 2),
    ("Usage, spend and rate limits", "Usage and spend", "USE", 2),
    ("Model choice, routing and caching", "Model choice", "MODEL", 2),
    ("Logs, traces and audit records", "Logs and audit", "LOG", 3),
    ("Stored data: retention, training use and encryption", "Stored data", "STOR", 3),
    ("AI inventory, lifecycle and policy management", "Inventory, lifecycle", "INV", 3),
]
DEF = {  # one-line definitions, from taxonomy.md
    "HARM": "What a prompt or response says or is about, judged against safety, topic, brand or acceptable-use policy.",
    "PI": "Input that tries to override instructions or exploit the system, and the handling of untrusted text before it reaches the model.",
    "SENS": "Personal, payment, secret or confidential data in live AI traffic: prompts, responses, tool arguments, retrieved content.",
    "ACC": "Whether a response is correct, grounded, well-formed and properly presented, as distinct from whether it is harmful.",
    "TOOL": "What an agent may do in the world: tools, MCP servers, apps, API calls, commands, file edits, purchases, and the sandbox they run in.",
    "AUTO": "The agent's run as a whole: how autonomously it operates, when a person reviews or takes over, and the state of the task.",
    "DATA": "Which knowledge sources, documents, files, folders and data stores an agent or model can read or write.",
    "NET": "Where traffic may go or come from: hosts, domains, IP ranges, private endpoints and transport security.",
    "ID": "Who or what the caller is, how it proves that, and what it is entitled to use or manage.",
    "USE": "How much is used or spent: requests, tokens, money, compute, time, iterations, size and count.",
    "MODEL": "Which model or provider serves a call, where it runs, and how the call is routed, retried, cached or parameterised.",
    "LOG": "The record of activity kept for the customer's oversight, and what that record contains.",
    "STOR": "Customer content held at rest: how long it is kept, whether it may train models, how it is encrypted.",
    "INV": "The AI system or agent as a managed asset, and the management of the control policies themselves.",
}
EP = [("input", "Before the model", "Input"), ("model_call", "Inside the model call", "Model call"),
      ("output", "After the model", "Output"), ("tool_action", "Before a tool or action", "Tool or action"),
      ("data_access", "Data access", "Data access"), ("network_egress", "Network egress", "Network"),
      ("identity_permission", "Identity and permissions", "Identity"), ("spend_rate", "Spend and rate", "Spend, rate"),
      ("human_approval", "Human approval", "Human approval"), ("logging_audit", "Logging and audit", "Logging"),
      ("lifecycle", "Lifecycle: publish, version, retire", "Lifecycle")]
MECH = [("Allow-list or grant", "The item proceeds only if named, granted or within a boundary."),
        ("Block or switch off", "The item does not proceed: deny-lists, refusals, kill and off switches."),
        ("Cap a quantity", "The item proceeds up to a number: rate, token, money, count, size or time."),
        ("Require a human", "The item waits for, or is handed to, a person."),
        ("Transform or steer", "The item proceeds, changed (masked, redacted) or directed (routing, parameters, settings)."),
        ("Detect and flag", "The rule produces a verdict, score or alert and does not itself stop the item."),
        ("Record and report", "The rule produces a durable record or report.")]
GROUPS = {"A": "Business agent platforms", "B": "Cloud agent runtimes", "C": "Model providers", "D": "Coding and desktop agents",
          "E": "Guardrail frameworks", "F": "AI and MCP gateways", "G": "Identity and governance", "H": "Agent protocols"}
CLUSTER_LABELS = {  # short names for embedding clusters, read off embed-clusters.md (presentation only)
    1: "Rate and spend limits", 6: "Audit logs", 14: "MCP server rules", 17: "Content filters", 26: "Connector sign-in",
    30: "Escalation, instructions", 12: "Injection detection", 18: "PII filters", 8: "Retention", 23: "Sandbox file rules",
    24: "Network domain lists", 27: "Payment mandates", 22: "Command approval", 32: "AI Control Tower", 35: "Who may use an agent",
    31: "Tests before release", 5: "Managed settings", 0: "Hooks", 20: "Guardrail actions", 3: "Model allow-lists"}

oi = {o[0]: i for i, o in enumerate(OBJ)}
code_i = {o[2]: i for i, o in enumerate(OBJ)}
ei = {e[0]: i for i, e in enumerate(EP)}
mi = {m[0]: i for i, m in enumerate(MECH)}

coded = rows("coded-all.csv")
inv = {r["control_id"]: r for r in rows("inventory-all.csv")}
emb = {r["control_id"]: r for r in rows("embed-clusters.csv")}
products = sorted({(r["group"], r["product"]) for r in coded})
pi = {p[1]: i for i, p in enumerate(products)}

C = []
for r in coded:
    v, e = inv[r["control_id"]], emb[r["control_id"]]
    src = 1 if r["source"] != "single coder" else 0
    C.append([r["control_id"], pi[r["product"]], oi[r["object"]], mi[r["mechanism"]], ei[r["enforcement_point"]],
              round(float(e["x"]), 4), round(float(e["y"]), 4), 1 if r["is_gap"] == "yes" else 0, src,
              v["control_name"].strip(), v["quote"].strip(), int(e["cluster"])])

# cluster label anchors: median position of each labelled cluster
cl = collections.defaultdict(list)
for c in C: cl[c[11]].append((c[5], c[6]))
def med(a): a = sorted(a); return a[len(a) // 2]
CL = [[k, lab, round(med([p[0] for p in cl[k]]), 4), round(med([p[1] for p in cl[k]]), 4), len(cl[k])] for k, lab in CLUSTER_LABELS.items()]

# coverage per object (non-gap controls), matches coverage.md
cov = []
for i, o in enumerate(OBJ):
    sub = [c for c in C if c[2] == i and not c[7]]
    cov.append([len(sub), len({c[1] for c in sub}), len({products[c[1]][0] for c in sub})])

# vendors: the 46 products belong to 31 vendors (GitHub counted with Microsoft; each protocol is its own vendor)
VENDOR = {"Google Gemini Enterprise": "Google", "Google Vertex AI": "Google", "Gemini API": "Google", "Gemini Code Assist": "Google",
          "Microsoft Copilot Studio": "Microsoft", "Azure AI Foundry": "Microsoft", "Azure API Management (MCP and LLM policies)": "Microsoft",
          "Microsoft Entra Agent ID / Conditional Access": "Microsoft", "Microsoft Purview (DSPM for AI, DLP)": "Microsoft", "GitHub Copilot": "Microsoft",
          "AWS Bedrock AgentCore": "AWS", "AWS Bedrock Agents": "AWS", "AWS Bedrock Guardrails": "AWS", "Amazon Q Developer": "AWS",
          "Anthropic": "Anthropic", "Claude Code": "Anthropic", "ChatGPT Enterprise/Edu/Business": "OpenAI", "OpenAI API": "OpenAI",
          "OpenAI Codex": "OpenAI", "ServiceNow AI Agents": "ServiceNow", "ServiceNow AI Control Tower": "ServiceNow"}
def vendor(p): return VENDOR.get(p, p)
NV = len({vendor(p) for _, p in products})
for i in range(len(OBJ)):
    cov[i].append(len({vendor(products[c[1]][1]) for c in C if c[2] == i and not c[7]}))

# comparison
DOM = ["algorithmic trading", "card payments and spend management", "cloud identity and infrastructure", "email and DLP",
       "IT change management", "industrial safety", "application access control", "ERP segregation of duties",
       "robotic process automation", "API gateway and WAF", "feature flags and release controls"]
DOM_S = ["Trading", "Payments", "Cloud", "Email, DLP", "IT change", "Industrial safety", "App access", "ERP SoD", "RPA",
         "API gateway, WAF", "Feature flags"]
di = {d: i for i, d in enumerate(DOM)}
fwd = [[None] * len(DOM) for _ in OBJ]
for r in rows("map-forward.csv"):
    fwd[oi[r["agent_category"]]][di[r["domain"]]] = [{"direct": 2, "partial": 1, "none": 0}[r["match"]], r["analogue"], r["reason"], r["source_flag"]]
REQ = {"law": 0, "regulator guidance": 1, "standard": 2, "product feature": 3}
rev = [[di[r["domain"]], r["control_type"], REQ[r["required_by"]], r["agent_equivalent"], r["closest_agent_controls"], r["note"]]
       for r in rows("map-reverse.csv")]
reach = [[oi[r["agent_category"]], r["determinism"], r["position"], r["reach"], r["failure_modes"]] for r in rows("reach.csv")]
conv = collections.OrderedDict()
for r in rows("conventional-sources.csv"):
    d = conv.setdefault(r["domain"], {"n": 0, "det": collections.Counter(), "pos": collections.Counter(), "reach": collections.Counter()})
    d["n"] += 1; d["det"][r["determinism"]] += 1; d["pos"][r["position"]] += 1; d["reach"][r["reach"]] += 1
conv = [[di[k], v["n"], dict(v["det"]), dict(v["pos"]), dict(v["reach"])] for k, v in conv.items()]

# timeline
TQ_COLS = ["quarter", "new_events", "new_types", "cum_types_vendor_object_soph", "objects_covered", "vendors_cum",
           "median_vendors_per_object", "max_soph_new", "median_soph_new", "share_45_new"]
tq = {"all": [], "primary": []}
for r in rows("timeline-quarterly.csv"):
    k = "all" if r["variant"].startswith("all") else "primary"
    tq[k].append([r["quarter"]] + [float(r[c]) if r[c] not in ("",) else None for c in TQ_COLS[1:]])
tall = {r["event_id"]: r for r in rows("timeline-all.csv")}
ev = []
for r in rows("timeline-final.csv"):
    a = tall[r["event_id"]]
    ev.append([r["event_id"], r["date"], r["vendor"], r["product"], code_i[{v[0]: v[2] for v in OBJ}[r["object"]]],
               int(r["sophistication"]), 1 if r["is_availability"] == "yes" else 0, r["evidence"], r["stage"], a["control_description"]])

lin = [[int(r["id"]), r["domain"], r["date"], int(r["stage_final"]), r["status"], r["milestone"], r["source"]] for r in rows("lineage-final.csv")]

out = {"objects": [[o[0], o[1], o[2], o[3], DEF[o[2]]] + cov[i] for i, o in enumerate(OBJ)],
       "eps": [[e[0], e[1], e[2]] for e in EP], "mechs": MECH, "groups": GROUPS,
       "products": [[g, p] for g, p in products], "nvendors": NV, "controls": C, "clusters": CL,
       "domains": [DOM, DOM_S], "fwd": fwd, "rev": rev, "reach": reach, "conv": conv,
       "tq_cols": TQ_COLS, "tq": tq, "events": ev, "lineage": lin}
(HERE / "data").mkdir(exist_ok=True)
s = json.dumps(out, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
(HERE / "data/atlas.json").write_text(s, encoding="utf-8")
ng = [c for c in C if not c[7]]
assert NV == 31, NV
print(f"vendors {NV}; controls {len(C)} (documented {len(ng)}, gaps {len(C) - len(ng)}), products {len(products)}, events {len(ev)}, "
      f"lineage {len(lin)}, reverse gaps {len(rev)}; {len(s) // 1024} KB")
