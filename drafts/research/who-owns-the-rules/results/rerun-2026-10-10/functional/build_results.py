"""Merge the per-question tables into tables.csv and write results.md. Run last."""
from common import *
from q5_keywords import FAMILIES

parts = [pd.read_csv(OUT / f) for f in ("tables-q1q3.csv", "tables-q4.csv", "tables-q5.csv")]
i6 = pd.read_csv(RUN / "instruments/I6-tables.csv")
i6 = i6[i6.table == "code_x_function"]
sp = pd.DataFrame(dict(question="Speech", function=i6.column, measure="I6_pooled_spans_" + i6.row, value=i6.n, low=None, high=None, n=i6.n))
tab = pd.concat(parts + [sp], ignore_index=True)
tab["measure"] = tab.measure.str.replace(r"^(all_weighted|existing_weighted|ai_titled):", r"Q5_\1:", regex=True)
tab.to_csv(OUT / "tables.csv", index=False)

def g(q, f, m, col="value"):
    r = tab[(tab.question == q) & (tab.function == f) & (tab.measure == m)]
    return float(r[col].iloc[0]) if len(r) else float("nan")
def pc(q, f, m, d=1):
    v, lo, hi = g(q, f, m), g(q, f, m, "low"), g(q, f, m, "high")
    return f"{100*v:.{d}f}% ({100*lo:.{d}f}-{100*hi:.{d}f})"
def md(df):
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "| " + " | ".join("---" for _ in cols) + " |"]
    for r in df.itertuples(index=False):
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out)

L = ["# Functional analysis: who does what with AI, by business function", "",
     "Descriptive, added at the user's request (design in `design.md`). Run on the 25,512 selected postings (`I1-posting-level.csv.gz`), "
     "305,533 extracted duty statements, 600 phase-2 coded tasks, the platform-controls P2 recode and the I6 speech counts. "
     "Functions come from one map (`function_map.py`); every figure inherits its error (see Limits). Intervals are 95%.", ""]

# ---- function map and accuracy
acc = pd.read_csv(OUT / "spotcheck-accuracy.csv")
fa = acc[(acc["map"] == "final map, fresh draw") & (acc.subset == "all 60")].iloc[0]
fb = acc[(acc["map"] == "first map, first draw") & (acc.subset == "all 60")].iloc[0]
L += ["## Function map and hand spot check", "",
      "Title keywords (security, legal, support, data/AI, sales, plus short finance, HR, marketing, software and executive lists) are applied first; "
      "otherwise the O*NET detailed code of `postings-mapped-v2.csv` is looked up by detailed code, minor group, then major group; otherwise 'other'. "
      "The full tables and keyword lists are in `function_map.py`.", "",
      f"Spot check of 60 postings (40 drawn in proportion to sampling weight, 20 from AI-titled postings), judged by me from title, employer and department (not from posting text; not an independent coder). "
      f"The first version of the map scored {fb.correct}/60 correct ({100*fb.strict:.0f}%, {fb.partial} partly defensible, {fb.wrong} wrong), mostly because 'Security Consulting Engineer' and similar titles missed the security rule, hardware engineers went to software, 'transformation' pulled AI roles into executive/strategy, and 'Solution Architect' went to sales. "
      f"I fixed those rules and drew a fresh sample of 60: **{fa.correct}/60 correct ({100*fa.strict:.0f}%, Wilson {100*fa.strict_lo:.0f}-{100*fa.strict_hi:.0f}%), {fa.partial} partly defensible, {fa.wrong} wrong**; counting partly defensible as correct, {100*fa.lenient:.0f}%. "
      "The fixed rules were tuned on the first sample, so only the fresh draw is a fair estimate. This is a check of business function (15 classes), a different target from the 83% major-group check of deviation 18, which scored the O*NET code alone. Verdicts are in `spotcheck-verdicts.csv` and `spotcheck-accuracy.csv`.", ""]
fnc = pd.read_csv(OUT / "spotcheck-sample.csv")  # unused; keep file referenced

# ---- Q1
rows = []
for f in FUNCTIONS + ["ALL"]:
    rows.append({"function": f, "sampled postings": int(g("Q1", f, "weighted_postings") and tab[(tab.question == "Q1") & (tab.function == f) & (tab.measure == "ai_title_share")].n.iloc[0]),
                 "AI-titled (n)": int(g("Q1", f, "ai_title_postings_n")), "AI-title share": pc("Q1", f, "ai_title_share"),
                 "AI/ML terms": f"{100*g('Q1', f, 'ai_ml_title_share'):.1f}%", "automation": f"{100*g('Q1', f, 'automation_title_share'):.1f}%",
                 "agent/agentic": f"{100*g('Q1', f, 'agent_title_share'):.1f}%",
                 "census check": f"{100*g('Q1', f, 'census_ai_title_share'):.1f}%",
                 "share of all AI-titled": "" if f == "ALL" else f"{100*g('Q1', f, 'share_of_all_ai_titled'):.0f}%"})
q1 = pd.DataFrame(rows).sort_values("AI-titled (n)", ascending=False)
L += ["## Q1. AI-titled postings are concentrated in data/AI, software, IT and security, with automation titles carrying manufacturing", "",
      "Share of each function's postings with an AI, ML, automation or agentic term in the title (deviation 14 list, human-agent titles excluded), weighted by the rest20 sampling weight. "
      "Function is assigned with the AI term stripped from the title so the term does not define the function. Interval: Wilson on the Kish effective sample size. "
      "'Census check' is the same share over all 110,715 titles of `postings-mapped-v2.csv` (non-excluded boards), with no weighting.", "", md(q1), "",
      f"Across all postings {pc('Q1','ALL','ai_title_share')} carry an AI-capability title (census {100*g('Q1','ALL','census_ai_title_share'):.1f}%). "
      f"Data and AI/ML leads at {pc('Q1','data and AI/ML','ai_title_share')}, then software engineering {pc('Q1','software engineering','ai_title_share')}, IT and infrastructure {pc('Q1','IT and infrastructure','ai_title_share')} and security {pc('Q1','security','ai_title_share')}. "
      f"Executive/strategy ({pc('Q1','executive/strategy','ai_title_share')}) and marketing ({pc('Q1','marketing','ai_title_share')}) are next; sales, customer service, finance, HR, legal and healthcare are all below 1%. "
      f"Software engineering ({100*g('Q1','software engineering','share_of_all_ai_titled'):.0f}% of all AI-titled postings), IT ({100*g('Q1','IT and infrastructure','share_of_all_ai_titled'):.0f}%) and data/AI ({100*g('Q1','data and AI/ML','share_of_all_ai_titled'):.0f}%) hold most of them; manufacturing/field holds {100*g('Q1','manufacturing/field','share_of_all_ai_titled'):.0f}% because its base is large, and its {100*g('Q1','manufacturing/field','ai_title_share'):.1f}% rate is almost entirely 'automation' titles ({100*g('Q1','manufacturing/field','automation_title_share'):.1f}%), not AI or agent terms. "
      "Agent or agentic titles are rare everywhere (0.1% overall).", ""]

# ---- Q2
rows = []
for f in FUNCTIONS + ["ALL"]:
    rows.append({"function": f, "existing postings (sampled)": int(tab[(tab.question == "Q2") & (tab.function == f) & (tab.measure == "flagged_share_existing")].n.iloc[0]),
                 "flagged by lexical screen": pc("Q2", f, "flagged_share_existing"),
                 "confirmed agent duty (two-phase est.)": pc("Q2", f, "confirmed_agent_duty_share_existing"),
                 "phase-2 tasks confirmed": f"{100*g('Q2', f, 'phase2_task_confirmation_rate_existing'):.0f}% of {int(tab[(tab.question == 'Q2') & (tab.function == f) & (tab.measure == 'phase2_task_confirmation_rate_existing')].n.iloc[0])}"})
q2 = pd.DataFrame(rows)
L += ["## Q2. Confirmed agent duties in existing-title postings sit mainly in data/AI, software, security and IT", "",
      "Existing-title postings only (S1 study occupations plus the rest20 sample), sampling-weighted. 'Confirmed' uses the two-phase logic of `i1_twophase.py`: a posting with k lexically flagged tasks has probability 1-(1-p)^k of at least one confirmed (AO, PE or RD) task, "
      "with p the phase-2 confirmation rate of its sampling group. The estimate reproduces `I1-twophase.md` (S1 189, rest20 2,340 postings). Interval for the two-phase column: percentile bootstrap (2,000 resamples) over postings within group and over the phase-2 sample "
      "(it does not include lexical-recall error). The last column is the direct confirmation rate of the sampled flagged tasks in that function (Wilson intervals in `tables.csv`); it rests on very few tasks outside data/AI, software, security and manufacturing.", "", md(q2), "",
      f"About {pc('Q2','ALL','confirmed_agent_duty_share_existing')} of existing-title postings carry a confirmed agent duty. By function the estimate is highest in data and AI/ML ({pc('Q2','data and AI/ML','confirmed_agent_duty_share_existing')}), "
      f"software engineering ({pc('Q2','software engineering','confirmed_agent_duty_share_existing')}), security ({pc('Q2','security','confirmed_agent_duty_share_existing')}) and IT ({pc('Q2','IT and infrastructure','confirmed_agent_duty_share_existing')}), "
      f"then marketing ({pc('Q2','marketing','confirmed_agent_duty_share_existing')}), executive/strategy and legal; it is under 1% in sales, healthcare and 'other'. "
      "These figures apply each sampling group's confirmation rate to every function in it; the direct function-level rates in the last column show the assumption is loose (IT and manufacturing/field confirm less often than the group rate, data/AI and security more), so the IT and manufacturing/field estimates are probably too high. "
      "Functions with fewer than 15 sampled tasks (HR, support, finance, healthcare, legal, executive, 'other') should be read as 'not distinguishable from zero or from the average'.", ""]

# ---- Q3
rows = []
for f in FUNCTIONS + ["ALL"]:
    r = {"function": f, "tasks sampled": int(g("Q3", f, "phase2_tasks_sampled_all"))}
    for c in ("AO", "PE", "PV", "RD"):
        r[c] = int(g("Q3", f, f"{c}_count_all"))
    r["AO existing / new-title"] = f"{int(g('Q3', f, 'AO_count_existing'))} / {int(g('Q3', f, 'AO_count_newtitle'))}"
    r["PE existing / new-title"] = f"{int(g('Q3', f, 'PE_count_existing'))} / {int(g('Q3', f, 'PE_count_newtitle'))}"
    rows.append(r)
q3 = pd.DataFrame(rows)
rows = []
for f in FUNCTIONS + ["ALL"]:
    if np.isnan(g("Q3", f, "p2_decision_count")): continue
    rows.append({"function": f, "tool_change": int(g("Q3", f, "p2_tool_change_count")), "decision": int(g("Q3", f, "p2_decision_count")), "neither": int(g("Q3", f, "p2_neither_count"))})
q3b = pd.DataFrame(rows)
L += ["## Q3. Running agents (AO) is the common activity; setting limits (PE) is rarer and sits in data/AI, security, IT and software", "",
      "Counts of phase-2 coded tasks by the function of the posting they come from. Final code = coders' agreed code, else the blind adjudication; a task with two codes counts under each. "
      "The 600 tasks are a stratified sample of lexically flagged tasks (150 S1, 300 rest20, 150 new-title), so counts are unweighted sample counts, not population rates. No task has a final RD code.", "", md(q3), "",
      "Platform-controls P2 recode (`p2-final.csv`), posting items only (117 of the 288 items; the rest are speech spans): whether the text is about changing a setting in a tool (tool_change), deciding or approving what an agent may do (decision), or neither.", "", md(q3b), "",
      f"Of 600 tasks, {int(g('Q3','ALL','AO_count_all'))} carry AO, {int(g('Q3','ALL','PE_count_all'))} PE, {int(g('Q3','ALL','PV_count_all'))} PV and none RD. "
      f"Data and AI/ML ({int(g('Q3','data and AI/ML','AO_count_all'))}) and software engineering ({int(g('Q3','software engineering','AO_count_all'))}) hold {100*(g('Q3','data and AI/ML','AO_count_all')+g('Q3','software engineering','AO_count_all'))/g('Q3','ALL','AO_count_all'):.0f}% of the AO tasks. "
      f"PE is spread over data/AI ({int(g('Q3','data and AI/ML','PE_count_all'))}), security ({int(g('Q3','security','PE_count_all'))}), software ({int(g('Q3','software engineering','PE_count_all'))}), IT ({int(g('Q3','IT and infrastructure','PE_count_all'))}) and operations ({int(g('Q3','operations and supply chain','PE_count_all'))}); "
      "PE tasks split almost evenly between existing-title (18) and new-title (15) postings although new-title tasks are a quarter of the sample, and AO tasks are 58 existing to 30 new-title. The two PV tasks are one security and one data/AI posting. "
      "In the P2 recode, 10 of 117 posting items describe a decision and 1 a tool change; the decisions sit in data/AI (5), IT (2), security (2) and software (1). Business functions outside technology and security contribute almost no confirmed AO or PE tasks in this sample.", ""]

# ---- Q4
n_ai = int(g("Q4", "ALL", "ai_titled_postings"))
first = tab[(tab.question == "Q4") & (tab.function == "ALL") & tab.measure.str.startswith("reports_to_dept:")]
rows = []
for r in first.sort_values("value", ascending=False).itertuples():
    d = r.measure.split(":", 1)[1]
    rows.append({"reports to (department of the named manager or leader)": d, "postings": int(r.value), "share of postings with a reporting phrase": pc("Q4", "ALL", f"reports_to_dept_share:{d}")})
q4a = pd.DataFrame(rows)
rows = []
for f in FUNCTIONS:
    n = tab[(tab.question == "Q4") & (tab.function == f) & (tab.measure == "share_with_reports_to_phrase")].n
    if not len(n): continue
    rows.append({"posting function": f, "AI-titled postings": int(n.iloc[0]), "with a reports-to phrase": pc("Q4", f, "share_with_reports_to_phrase", 0),
                 "reports to own function": ("" if np.isnan(g("Q4", f, "reports_to_own_function_share")) else f"{100*g('Q4', f, 'reports_to_own_function_share'):.0f}% of {int(tab[(tab.question=='Q4')&(tab.function==f)&(tab.measure=='reports_to_own_function_share')].n.iloc[0])}")})
q4b = pd.DataFrame(rows).sort_values("AI-titled postings", ascending=False)
part = tab[(tab.question == "Q4") & (tab.function == "ALL") & tab.measure.str.startswith("part_of_team_dept:")].sort_values("value", ascending=False)
q4c = pd.DataFrame([{"team named": r.measure.split(":", 1)[1], "postings": int(r.value)} for r in part.itertuples()])
ex = pd.read_csv(OUT / "q4-examples.csv")
exl = []
for r in ex.itertuples():
    exl.append(f"- ({r.kind.replace('_', ' ')}; classified {r.dept}; posting `{r.posting_id}`) \"{r.text}\"")
L += ["## Q4. Few AI-titled postings state who the role reports to; where they do, it is mostly the data/AI or engineering line", "",
      f"Population: the {n_ai:,} AI-titled (new-title, non-human-agent) postings; raw text joined to the analysis table by doc_id = P + ats + _ + board_id + _ + id (all {int(g('Q4','ALL','ai_titled_with_text')):,} joined). "
      "Patterns: 'reports/reporting (directly/functionally) to/into ...' and 'part of / join the ... team|group|organization|department'. The phrase after the cue (up to 9 words, cut at clause breaks) is classified by keyword to the department whose keyword appears earliest; "
      "title words (manager, director, VP) do not name a department. One phrase per posting (the first). Keyword rules are in `q4.py`. Posting-level classes are in `q4-phrase-classes.csv` (no phrase text).", "",
      f"{pc('Q4','ALL','share_with_reports_to_phrase')} of AI-titled postings name a reporting line ({int(first.value.sum())} postings); {pc('Q4','ALL','share_with_part_of_team_phrase')} use a 'part of the ... team' phrase.", "", md(q4a), "",
      "By the function of the posting itself (function from the title as written, so counts differ from Q1, which strips the AI term):", "", md(q4b), "", "'Part of the ... team' phrases, by team named (generic phrases such as 'winning team' or an employer's name carry no function):", "", md(q4c), "",
      f"Of postings with a reporting line, {pc('Q4','ALL','reports_to_dept_share:data and AI/ML',0)} report to a data/AI leader and {pc('Q4','ALL','reports_to_dept_share:software engineering',0)} to engineering; security ({int(g('Q4','ALL','reports_to_dept:security'))}), "
      f"legal and compliance ({int(g('Q4','ALL','reports_to_dept:legal and compliance'))}), HR ({int(g('Q4','ALL','reports_to_dept:HR'))}) and finance ({int(g('Q4','ALL','reports_to_dept:finance and accounting'))}) together account for about {100*(g('Q4','ALL','reports_to_dept:security')+g('Q4','ALL','reports_to_dept:legal and compliance')+g('Q4','ALL','reports_to_dept:HR')+g('Q4','ALL','reports_to_dept:finance and accounting'))/first.value.sum():.0f}%. "
      "Postings in data/AI report to their own function about half the time; IT-, manufacturing- and finance-function postings report outside it more often than inside (small n; the function of the posting is itself a title-based label, and AI terms in the reporting phrase pull the classifier toward data/AI). "
      "The 'manufacturing/field' reporting lines include phrases such as 'Field AI Strategy', i.e. keyword noise in a small cell. Part-of-team phrases mostly name no function (58%) or a data/AI or engineering team.", "",
      "Verbatim examples (one sentence, at most 40 words, names, emails and links removed; screened for personal names by a capitalised-bigram rule and read by me):", ""] + exl + [""]

# ---- Q5
fam_rows = {}
def q5table(pop):
    rows = []
    for f in FUNCTIONS + ["ALL"]:
        r = {"function": f}
        n = tab[(tab.question == "Q5") & (tab.function == f) & (tab.measure == f"Q5_{pop}:security_review_per_1000_duties")].n
        if not len(n): continue
        r["duty statements"] = int(n.iloc[0])
        for fam in FAMILIES:
            m = f"Q5_{pop}:{fam}_per_1000_duties"
            r[fam.replace("_", " ")] = f"{g('Q5', f, m):.1f} ({g('Q5', f, m, 'low'):.1f}-{g('Q5', f, m, 'high'):.1f})"
        rows.append(r)
    return pd.DataFrame(rows)
kw = []
for fam, words in FAMILIES.items():
    kw.append(f"- **{fam.replace('_', ' ')}**: " + "; ".join(words))
A = lambda f, fam, pop="all_weighted": g("Q5", f, f"Q5_{pop}:{fam}_per_1000_duties")
L += ["## Q5. Security review sits in security and IT, AI governance in data/AI, guardrail and permission work in security, and service management in support and IT", "",
      "Rate per 1,000 duty statements (305,533 statements from 25,220 postings), weighted by the posting's sampling weight; interval = percentile bootstrap over postings within sampling group (duties cluster in postings, so Wilson on statements would be too narrow). "
      "Function is the posting's function from the map, so the 'security' row is partly defined by 'security' in the title: its high security-review rate is partly built in.", "",
      "Keyword families (case-insensitive, whole-word start, stems match; short acronyms matched in capitals only):", ""] + kw + ["",
      "All postings, weighted:", "", md(q5table("all_weighted")), "", "AI-titled postings only (unweighted; small cells are wide):", "", md(q5table("ai_titled")), "",
      f"Security review: {A('security','security_review'):.0f} per 1,000 duties in security postings against {A('ALL','security_review'):.0f} overall; IT ({A('IT and infrastructure','security_review'):.0f}), software ({A('software engineering','security_review'):.0f}) and data/AI ({A('data and AI/ML','security_review'):.0f}) follow. "
      f"AI governance is the clearest data/AI signal ({A('data and AI/ML','ai_governance'):.1f} per 1,000, against {A('ALL','ai_governance'):.1f} overall), with security ({A('security','ai_governance'):.1f}) and IT ({A('IT and infrastructure','ai_governance'):.1f}) next; in AI-titled postings the rate is {A('ALL','ai_governance','ai_titled'):.0f} per 1,000 and the legal, finance and operations cells are high but rest on 15 to 53 postings. "
      f"Guardrail and permission duties peak in security ({A('security','guardrail_permission'):.0f}), with IT ({A('IT and infrastructure','guardrail_permission'):.0f}) and data/AI ({A('data and AI/ML','guardrail_permission'):.0f}) at about a quarter of that. "
      f"Service management is the one family that leaves technology: customer service/support ({A('customer service/support','service_management'):.0f}) matches IT ({A('IT and infrastructure','service_management'):.0f}), then software ({A('software engineering','service_management'):.0f}) and security ({A('security','service_management'):.0f}); business functions are 3 to 7 per 1,000. "
      "The rates for governance, guardrail and permission duties outside technology and security are close to zero in the whole posting set.", ""]

# ---- Speech
sp_t = tab[tab.question == "Speech"].pivot(index="function", columns="measure", values="value").fillna(0).astype(int)
sp_t.columns = [c.replace("I6_pooled_spans_", "") for c in sp_t.columns]
sp_t = sp_t[["AO", "PE", "PV", "OT"]].reset_index().rename(columns={"index": "function"})
sp_t["AO+PE share of spans"] = [f"{100*(a+p)/(a+p+v+o):.0f}%" for a, p, v, o in zip(sp_t.AO, sp_t.PE, sp_t.PV, sp_t.OT)]
L += ["## Speech cross-check (I6, pooled spans)", "",
      "From `I6-tables.csv` (code by function). These are pooled spans from 34 transcripts, one to seven transcripts per function, extraction recall about 0.5; the function is the speaker's, not a posting's, and the I6 function list differs from the posting map. Totals reflect how many and how long the transcripts are; they are not rates.", "",
      md(sp_t), "",
      "Agent-operations spans are dense in sales/RevOps/go-to-market (89 of 170) and customer support/CX (26), finance (17) and IT/identity/security (11); setting-limits spans are few everywhere (24 in all: IT/security 5, engineering 4, risk and compliance 4, HR 3). "
      "Postings put running and limit-setting duties mainly in data/AI, software and security, while speakers describing their own work report running agents mostly in go-to-market and support. The two sources do not measure the same thing (posting duties versus self-described practice), so the difference is a contrast, not a contradiction.", ""]

L += ["## Limits", "",
      "- Function comes from title keywords and model-assigned O*NET codes; the O*NET major group is about 83% right (deviation 18) and my 60-posting check of the final 15-class map found "
      f"{100*fa.strict:.0f}% fully right. Small functions (HR, legal, support, healthcare, finance) have few postings or tasks in the AI and agent subsets, so their cells are wide or empty.",
      "- Q1 and Q4 define 'AI-titled' by title terms, so they measure titles, not work; 'automation' titles in manufacturing/field are mostly industrial automation. Strip-and-remap removes the circularity for Q1 but not for Q2 to Q5, where function is assigned from the title as written.",
      "- Q2 applies group-level confirmation rates to all functions and treats tasks within a posting as independent; the lexical screen misses postings that describe agent duties without the listed terms. Function-level confirmation rates are shown but rest on small counts.",
      "- Q3 counts a stratified task sample; the sample was drawn before function was known, so function counts are not controlled. RD never occurs in the final codes.",
      "- Q4 finds a reporting line in under 10% of AI-titled postings; those are not a random subset (named leaders appear mostly in senior or new-team roles). Department classification is keyword-based and uses the earliest keyword, so AI words in a leader's title pull the class toward data/AI; no precision check against hand coding was run.",
      "- Q5 keyword families are lexical: 'permission', 'entitlement' and 'on-call' have non-IT senses, and 'service level' and 'SLA' occur in commercial contracts. No precision check was run beyond reading the most frequent matches, which led me to drop bare 'authorization', 'escalation', 'root cause analysis', 'change management' and 'risk assessment'.",
      "- Sampling: employers are Fortune 500 and VC-software boards, US and non-US pooled; weights correct for the rest20 sampling only, not for employer selection.",
      "- No personal data is stored: Q4 tables hold department classes only, and the quoted examples were scrubbed of emails, links and phone numbers and screened for names.", ""]
(OUT / "results.md").write_text("\n".join(L))
print("ok", len(tab))
