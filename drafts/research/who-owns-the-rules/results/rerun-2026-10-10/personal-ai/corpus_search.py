"""Part B search. Run from study root: loop-tools/.venv/bin/python results/rerun-2026-10-10/personal-ai/corpus_search.py
Case-insensitive term list (AI-context terms need an AI/tool word within 80 chars). Writes candidates.csv with context windows."""
import json, re, sys, pathlib, csv
sys.path.insert(0, 'results/rerun-2026-10-10/functional')
from common import load_postings
AI = r"(?:\bAI\b|A\.I\.|artificial intelligence|generative|genai|\bLLMs?\b|chatgpt|copilot|gemini|claude|\bagents?\b|chatbot|language model|\btools?\b|\bapps?\b|applications?|software)"
def near(t): return re.compile(r"(?:%s.{0,80}?%s|%s.{0,80}?%s)" % (t, AI, AI, t), re.I | re.S)
TERMS = {
 "shadow AI": re.compile(r"shadow[\s-]+AI|shadow[\s-]+(?:use|usage) of AI", re.I),
 "shadow IT (AI context)": near(r"shadow[\s-]+IT"),
 "unsanctioned": re.compile(r"unsanctioned", re.I),
 "unapproved": re.compile(r"unapproved|non-?approved|not[\s-]+approved", re.I),
 "unauthorized (AI/tools)": near(r"unauthori[sz]ed"),
 "personal account(s)": re.compile(r"personal\s+(?:ai\s+)?accounts?|personal\s+(?:chatgpt|ai)\s+(?:subscriptions?|licen[cs]es?)", re.I),
 "personal device(s)": re.compile(r"personal\s+(?:devices?|laptops?|phones?|computers?)", re.I),
 "BYOD": re.compile(r"\bBYOD\b", re.I),
 "bring your own": re.compile(r"bring[\s-]+your[\s-]+own|\bBYO(?:AI|T)?\b", re.I),
 "approved tools / AI tools": re.compile(r"(?:approved|sanctioned|authori[sz]ed|permitted|allowed)\s+(?:\w+\s+){0,2}(?:tools?|AI|applications?|platforms?)|(?:tools?|AI)\s+(?:that\s+)?(?:are|is)\s+(?:approved|sanctioned|authori[sz]ed)", re.I),
 "acceptable use (AI)": near(r"acceptable[\s-]+use"),
 "sanctioned AI": re.compile(r"sanctioned", re.I),
 "public AI tools": re.compile(r"(?:public|publicly[\s-]available|open|external|third[\s-]party|free)\s+(?:\w+\s+){0,2}(?:AI|generative|GenAI|LLM|chatbots?)\b", re.I),
 "consumer AI": re.compile(r"consumer[\s-]+(?:grade\s+)?(?:\w+\s+)?(?:AI|generative|chatbots?|tools?|LLM)", re.I),
 "ChatGPT (usage policy)": re.compile(r"chatgpt", re.I),
 "AI usage policy": re.compile(r"(?:AI|generative|GenAI)[\s-]+(?:\w+\s+)?(?:use|usage|user)\s+(?:polic\w+|guidelines?|standards?|rules)|polic\w+\s+(?:on|for|governing|regarding)\s+(?:the\s+)?(?:use\s+of\s+)?(?:AI|generative)|(?:AI|generative)\s+(?:policy|policies)", re.I),
 "AI tool approval/intake": near(r"(?:approval|intake|vetting|request(?:s)?\s+process|review process)\s+(?:of|for)?"),
 "browser extension(s) (AI)": near(r"browser\s+(?:extensions?|plug-?ins?)"),
 "data leakage (AI/prompts)": near(r"(?:data|information)\s+(?:leak\w*|exfiltration|loss)|leak\w*\s+(?:of\s+)?(?:data|confidential)"),
 "DLP (AI)": near(r"\bDLP\b|data[\s-]+loss[\s-]+prevention"),
}
def window(text, m, w=45):
    a, b = m.start(), m.end()
    return text[max(0, a-300):min(len(text), b+300)]
out = []
def scan(src, id_, text, meta):
    for name, rx in TERMS.items():
        for m in rx.finditer(text):
            out.append(dict(id=id_, source=src, term=name, ctx=" ".join(window(text, m).split()), **meta)); break
# postings
p = load_postings().drop_duplicates('doc_id').set_index('doc_id')
tasks = {}
for l in open('corpus/b-raw/extract/postings-haiku-all.tasks.jsonl'):
    r = json.loads(l); tasks.setdefault(r['doc_id'], []).append(r['span'])
npost = 0
for d, spans in tasks.items():
    if d not in p.index: continue
    npost += 1; row = p.loc[d]
    for i, s in enumerate(spans):
        scan('posting', d + ':' + str(i), s, dict(function=row.fn, employer=row.employer, title=row.title, weight=5 if row.group == 'rest20' else 1))
# speech
nsp = 0
for l in open('corpus/b-raw/extract/speech-consensus/consensus-dedup.jsonl'):
    r = json.loads(l); nsp += 1
    scan('speech', r['task_id'], r['span'], dict(function=r['function'], employer='', title=r['transcript_id'], weight=1))
# speech full text (supplementary: paragraphs around spans, incl. untimestamped M041/M053/M054/M067)
for fn_ in ('speech-input.jsonl','speech-input-notime.jsonl'):
    for l in open('corpus/b-raw/extract/'+fn_):
        r = json.loads(l)
        scan('speech-text' if r.get('start') not in (None,'None') else 'speech-notime', r['id'], r['text'], dict(function=r['function'], employer='', title=r['transcript_id'], weight=1))
# filings
nf = 0
for l in open('corpus/b-raw/extract/filings-input-v3.jsonl'):
    r = json.loads(l); nf += 1
    mm = re.match(r"Company: (.*?)  \(", r['text']); emp = mm.group(1) if mm else ''
    body = r['text'].split('\n\n', 1)[-1]
    scan('filing', r['id'], body, dict(function=r['sic_description'], employer=emp, title=r['section'], weight=1))
print(npost, nsp, nf, len(out))
json.dump(out, open('results/rerun-2026-10-10/personal-ai/candidates.json', 'w'))
from collections import Counter
c = Counter((o['source'], o['term']) for o in out)
for k, v in sorted(c.items()): print(k, v)
