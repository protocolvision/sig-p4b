import json,csv,re,random,collections
B='corpus/b-raw/'
sel={}
for r in csv.DictReader(open(B+'mapping/selection.csv',encoding='utf-8')):
    sel[(r['ats'],r['board_id'],r['posting_id'])]=r
inp={}
for l in open(B+'extract/postings-input.jsonl',encoding='utf-8'):
    d=json.loads(l); inp[d['id']]=(d['ats'],d['board_id'],d['posting_id'],d.get('group'))
S=r'[\s\-]*'
DOM={
'AGT':[r'agents?',r'agentic',r'co-?pilots?',r'chat-?bots?',r'virtual assistants?',r'AI assistants?'],
'CRD':[r'credit polic(?:y|ies)',r'underwriting',r'credit risk',r'lending criteria'],
'PRC':[r'pricing',r'discounts?|discounting',r'deal desk',r'price exceptions?'],
'FRD':[r'fraud',r'AML',r'transaction monitoring',r'sanctions? screening'],
'CHG':[r'change advisory boards?',r'CAB',r'change management',r'release approvals?'],
'ACC':[r'access polic(?:y|ies)',r'entitlements?',r'identity governance',r'role-based access',r'privileged access'],
'TRD':[r'trading limits?',r'risk limits?',r'position limits?',r'kill[\s-]?switch(?:es)?',r'pre-?trade'],
'CLN':[r'clinical protocols?',r'formular(?:y|ies)',r'order sets?',r'clinical guidelines?',r'care pathways?'],
'PRO':[r'approval thresholds?',r'delegations? of authority',r'procurement polic(?:y|ies)',r'spend approvals?'],
}
CASE_SENS={'CAB','AML'}
RULE=r'rules?|polic(?:y|ies)|limits?|thresholds?|criteria|guidelines?|protocols?|guardrails?|standards?|controls?|approvals?|exceptions?|parameters?|configurations?'
rule_re=re.compile(r'\b(?:%s)\b'%RULE,re.I)
AI_CTX=re.compile(r'\b(?:AI|LLMs?|models?|co-?pilots?|chat-?bots?|automation|agentic)\b',re.I)
term_re={d:[(t,re.compile(r'\b(?:%s)\b'%t,0 if t in CASE_SENS else re.I)) for t in ts] for d,ts in DOM.items()}
def first_pos(d,s):
    best=None
    for t,rx in term_re[d]:
        for m in rx.finditer(s):
            if d=='AGT' and t=='agents?' and not AI_CTX.search(s): continue
            if best is None or m.start()<best: best=m.start()
            break
    return best
def norm(s): return re.sub(r'\W+',' ',s.lower()).strip()
raw=collections.defaultdict(list); multi=collections.Counter(); n=0; unj=0
for l in open(B+'extract/postings-haiku-all.tasks.jsonl',encoding='utf-8'):
    t=json.loads(l); n+=1; s=t['span']
    if not rule_re.search(s): continue
    pos={d:first_pos(d,s) for d in DOM}; pos={d:p for d,p in pos.items() if p is not None}
    if not pos: continue
    order=sorted(pos,key=pos.get)
    if len(order)>1: multi['+'.join(sorted(order))]+=1
    key=inp.get(t['doc_id'])
    if not key: unj+=1; continue
    r=sel.get(key[:3])
    if not r: unj+=1; continue
    grp=r['group'] or key[3]
    w=5 if (key[3]=='rest20' or r['group']=='rest20') else 1
    raw[order[0]].append(dict(task_id=t['task_id'],domain=order[0],span=s,employer=r['employer'],title=r['title'],group=grp,weight=w,doc_id=t['doc_id'],multi=len(order)>1))
rng=random.Random(20261012)
out=[];rows=[]
for d in DOM:
    L=raw[d]; seen=set(); dd=[]
    for x in L:
        k=(x['employer'],norm(x['span']))
        if k in seen: continue
        seen.add(k); dd.append(x)
    dd.sort(key=lambda x:x['task_id'])
    k=min(60,len(dd)); smp=rng.sample(dd,k)
    for x in smp: out.append({c:x[c] for c in ['task_id','domain','span','employer','title','group','weight']})
    rows.append((d,len(L),sum(x['weight'] for x in L),len({x['doc_id'] for x in L}),len({x['employer'] for x in L}),len(dd),sum(x['weight'] for x in dd),len({x['doc_id'] for x in dd}),k,sum(x['multi'] for x in L)))
with open(B+'coding/dr-sample.jsonl','w',encoding='utf-8') as f:
    for o in out: f.write(json.dumps(o,ensure_ascii=False)+'\n')
P=lambda *a:a
md=['# Decision rights Part 1: sample','',f'Script: results/rerun-2026-10-10/decision-rights/build_sample.py. Statements scanned: {n}; matched but not joinable to selection.csv: {unj}.','',
'## Matching','','A statement matches a domain if it contains one of the domain terms and one rule word (word-boundary, case-insensitive; CAB and AML case-sensitive). Domain assignment: the domain whose term appears earliest in the statement. Plurals allowed.','',
'Rule word regex: `\\b(?:%s)\\b`'%RULE,'','AGT: bare "agent(s)" counts only if the statement also matches `\\b(?:AI|LLMs?|models?|co-?pilots?|chat-?bots?|automation|agentic)\\b`. The other AGT terms need no context word.','','Domain term regexes (each wrapped in `\\b(?:...)\\b`):','']
for d,ts in DOM.items(): md.append(f'- {d}: '+'; '.join(f'`{t}`' for t in ts))
md+=['','## Counts','','Raw = matched statements assigned to domain; weighted = rest20 statements x5. Dedupe = identical normalized text within the same employer removed (first kept by task_id order). Postings are distinct postings in the raw match.','',
'| Domain | Raw | Weighted | Postings | Employers | After dedupe (raw) | After dedupe (weighted) | Postings after dedupe | Sample n | Multi-domain matches in raw |','|---|---|---|---|---|---|---|---|---|---|']
for r in rows: md.append('| '+' | '.join(map(str,r))+' |')
md+=['','## Multi-domain matches (all statements, by domain set)','']
for k,v in multi.most_common(): md.append(f'- {k}: {v}')
md+=['','## Sampling notes','','- random.Random(20261012); per domain, pool sorted by task_id, then rng.sample of up to 60; domains processed in table order.','- Sample is unweighted within the deduped pool; weight field is carried for later estimates.','- Employer, title, group come from selection.csv (group falls back to postings-input if blank).','- No coding done; no seed items created. Seed statements (30) still to be added separately.']
open('results/rerun-2026-10-10/decision-rights/sample.md','w').write('\n'.join(md)+'\n')
print('\n'.join(md[md.index('## Counts'):]))
