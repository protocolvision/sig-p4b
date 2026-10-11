"""Part B step 2-3: hand-coded keep list (after reading every prefiltered hit) -> corpus-hits.csv, quote check, tables.
Run from study root after corpus_search.py: loop-tools/.venv/bin/python results/rerun-2026-10-10/personal-ai/corpus_code.py"""
import json, re, csv, collections, sys, pathlib
sys.path.insert(0, 'results/rerun-2026-10-10/functional')
from common import load_postings
D = pathlib.Path('results/rerun-2026-10-10/personal-ai')
cand = json.load(open(D / 'candidates.json'))
APP = 'approve'; DIS = 'discover'; MON = 'monitor'; POL = 'policy'; TR = 'train'; BL = 'block'; NONE = 'none stated (risk only)'
SEC, IT, LG, DA, BU, HR, NS = 'security', 'IT', 'legal/compliance', 'data/AI', 'business', 'HR', 'not stated'
# (doc suffix, anchor (case-insens), who, response)
POST = [
 ('hasense_8634067002', 'discover unsanctioned', SEC, DIS), ('hasense_8634067002', 'Monitor DLP and AI usage logs', SEC, MON),
 ('hasense_8634067002', 'AI-specific DLP controls', SEC, MON),
 ('myhrabc_R2615880', 'shadow AI discovery', SEC, DIS), ('myhrabc_R2615880', 'shadow AI indicators', SEC, MON),
 ('myhrabc_R2615880', 'unauthorized access through RAG', SEC, POL), ('myhrabc_R2615880', 'managed and unmanaged endpoints', SEC, MON),
 ('se_coupang_8163774', 'shadow AI', SEC, POL), ('etrust_8222894', 'Shadow AI detection strategy', IT, DIS),
 ('etrust_8222894', 'discover unsanctioned', IT, DIS), ('44000143146444', 'shadow AI', SEC, POL),
 ('y_cdw_R26_00002737', 'shadow AI', SEC, APP), ('y_cdw_R26_00002737', 'unapproved AI use', SEC, APP),
 ('y_cdw_R26_00002737', 'prompt and response inspection', SEC, MON),
 ('w_R26_00002602', 'how coworkers work with AI', IT, POL), ('ington_R103321', 'acceptable use guidelines', IT, TR),
 ('orkday_kla_2641147', 'security standards for enterprise use', SEC, POL), ('orkday_kla_2640596', 'policy enforcement', IT, POL),
 ('iqvia_R1549373', 'AI security intake', SEC, APP), ('_leidos_R-00192986', 'security-approval process', SEC, APP),
 ('freddiemac_JR17387', 'AI Clearinghouse', DA, APP), ('freddiemac_JR17388', 'use case intake', DA, APP),
 ('testreet_R-799264', 'approved tools are used only', NS, POL), ('testreet_R-799264', 'governance and approval processes', NS, APP),
 ('kday_cisco_2024069', 'onboarding third-party AI tools', BU, APP), ('y_gilead_R0055678', 'intake and assessment', NS, APP),
 ('kday_ntrs_R153112', 'AI prompt and response handling', SEC, MON), ('kday_ntrs_R153112', 'AI-specific scenarios', SEC, MON),
 ('y_biibhr_REQ24327', 'guardrails for generative AI usage', SEC, BL), ('y_carrier_30217267', 'Integrate AI security controls', SEC, MON),
 ('pacificlife_R17881', 'DLP policies', IT, BL), ('rkday_cnx_R1691702', 'AI misuse or data leakage', SEC, MON),
 ('y_abbott_31159447', 'Promote responsible and secure AI use', SEC, TR), ('financial_JR2600957', 'Approved AI/Model List', SEC, APP),
]
APPR = ['alesforce_JR356841','kday_ntrs_R160852','mckesson_JR0155354','ckesson_JR0151888','_travelers_R-52663','ay_gilead_R0054109',
 'kday_citi_26999356','workday_JR-0110413','_myhrabc_R2616950','ay_avnet_JR-022116','rkday_ghr_26034383','y_visa_REF089065W',
 'networks_JR-021183','y_paypal_R0137762','_leidos_R-00193692','ay_amgen_R-251304','y_micron_JR107244','y_micron_JR110701',
 'ay_micron_JR112606','ay_micron_JR97549','y_micron_JR111590','ay_micron_JR112508','ay_micron_JR105647','ay_micron_JR113677',
 'astercard_R-291633','ay_allstate_R35231','day_cigna_26010283','y_abbott_31161904','y_danaher_R1318142','ay_abbott_31160735',
 'kday_ntrs_R162120','day_amgen_R-254776','orkday_caci_330959','orkday_spgi_330519']
for a in APPR: POST.append((a, r'(?:approved|authorized)', IT if a in ('_travelers_R-52663','ay_avnet_JR-022116','ay_gilead_R0054109') else NS, APP))
POST += [('y_micron_JR108610','approved AI tools',NS,TR),('rkelcorp_R0023796','approved tools, platforms, and policies',NS,POL),
 ('y_visa_REF085268W','approved AI standards',NS,POL),('y_visa_REF085268W','approved AI-enabled ways',NS,TR),
 ('evernova_R5048292','IP protection guidelines',NS,POL)]
FIL = [
 ('0000872589-26-000025_0','Employee use of unapproved AI tools',NS,NONE), ('0001032975-26-000021_0','employees using unauthorized AI tools',NS,NONE),
 ('0001193125-26-051382_7','relating to our employees',NS,POL), ('0001193125-26-214647_2','relating to our employees',NS,POL),
 ('0001193125-26-340294_3','relating to our employees',NS,POL), ('0001193125-26-088391_0','our employees may access following internal review',SEC,APP),
 ('0001193125-26-307785_2','internal AI policies and training',NS,POL), ('0001468327-26-000088_4','risks of employee non-compliance',NS,NONE),
 ('0001628280-26-015791_1','non-approved AI',NS,NONE), ('0001628280-26-021721_1','mandatory compliance training',NS,TR),
 ('0001628280-26-057139_0','unauthorized or unapproved use of generative AI',NS,NONE), ('0001628280-26-057406_1','unauthorized or unapproved use of generative AI',NS,NONE),
 ('0001628280-26-059830_1','unauthorized or unsanctioned means',NS,NONE), ('0001635282-25-000215_1','we prohibit the use of artificial intelligence',NS,BL),
 ('0001647639-26-000027_1','Our employees and contractors use generative AI',NS,POL), ('0001647639-26-000046_0','Despite policies governing their use',NS,POL),
 ('0001647639-26-000063_0','Despite policies governing their use',NS,POL), ('0001660280-25-000128_0','employee use of unvetted',NS,NONE),
 ('0001660280-26-000005_0','shadow AI',NS,NONE), ('0001660280-26-000005_2','employee use of unvetted',NS,NONE),
 ('0001660280-26-000023_0','employee use of unvetted',NS,NONE), ('0001660280-26-000035_0','employee use of third-party agentic',NS,NONE),
 ('0001628280-26-011709_0','use of unapproved AI tools',NS,NONE), ('0001437749-26-031469_6','authorized business users',NS,APP),
 ('0002055592-26-000065_0','third-party generative AI tools under enterprise agreements',NS,APP),
]
SPE = [('M065_c06:2','compliance approval process for new tools',NS,APP,'speech'),
       ('M067_p08:6','we have opened up an enterprise license for ChatGPT',NS,APP,'speech-notime'),
       ('M052_c01','allowed to use AI',SEC,POL,'speech-text'),
       ('M081_c01','Here are some rules just about keeping data private',NS,POL,'speech-text')]
def clean(t): return re.sub(r"\s+", " ", re.sub(r"\[\s?\d\d:\d\d:\d\d\s?\]", "", t)).strip()
def quote(text, anchor):
    t = clean(text); m = re.search(anchor, t, re.I)
    if not m: return None
    a = t.rfind('. ', 0, m.start()); a = 0 if a < 0 else a + 2
    b = t.find('. ', m.end()); b = len(t) if b < 0 else b + 1
    w = t[a:b].split()
    if len(w) > 40:
        pre = len(t[a:m.start()].split()); s = max(0, min(pre - 2, len(w) - 40)); w = w[s:s + 40]
    return ' '.join(w)
# source texts
src = {}
for l in open('corpus/b-raw/extract/filings-input-v3.jsonl'):
    r = json.loads(l); src[('filing', r['id'])] = r['text'].split('\n\n', 1)[-1]
for f in ('speech-input.jsonl', 'speech-input-notime.jsonl'):
    for l in open('corpus/b-raw/extract/' + f):
        r = json.loads(l); src[('speech-para', r['id'])] = r['text']
for l in open('corpus/b-raw/extract/speech-consensus/consensus-dedup.jsonl'):
    r = json.loads(l); src[('speech', r['task_id'])] = r['span']
rows = []; seen = set()
for o in cand:
    if o['source'] != 'posting': continue
    for suf, anc, who, resp in POST:
        if suf in o['id'] and re.search(anc, o['ctx'], re.I):
            # candidate ctx for postings = span itself (+-300 chars, whole span)
            k = (o['id'], anc)
            if k in seen: continue
            seen.add(k)
            rows.append(dict(id=o['id'], source='posting', function=o['function'], employer=o['employer'], who=who, response=resp,
                             text=o['ctx'], anchor=anc, weight=o['weight'], title=o['title']))
# dedupe rows per posting span (same span via several anchors -> keep first)
ded = {}
for r in rows: ded.setdefault((r['id'], r['text']), r)
rows = list(ded.values())
for fid, anc, who, resp in FIL:
    o = next(o for o in cand if o['source'] == 'filing' and o['id'] == fid)
    rows.append(dict(id=fid, source='filing', function=o['function'], employer=o['employer'], who=who, response=resp,
                     text=src[('filing', fid)], anchor=anc, weight=1, title=o['title']))
spfun = {o['id']: o['function'] for o in cand if o['source'].startswith('speech')}
spfun['M067_p08:6']='customer support/CX'
for sid, anc, who, resp, st in SPE:
    kind = 'speech' if ('speech', sid) in src else 'speech-para'
    rows.append(dict(id=sid, source=st, function=spfun[sid], employer='', who=who, response=resp, text=src[(kind, sid)],
                     anchor=anc, weight=1, title=''))
out = []; bad = []
for r in rows:
    q = quote(r['text'], r['anchor'])
    ok = q is not None and q in clean(r['text']) and len(q.split()) <= 40 and '@' not in q
    if not ok: bad.append(r['id']); continue
    r['quote'] = q; out.append(r)
print('rows', len(rows), 'quote ok', len(out), 'bad', bad)
with open(D / 'corpus-hits.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['id', 'source', 'function', 'employer', 'who', 'response', 'quote'])
    for r in out:
        w.writerow([r['id'], r['source'], r['function'], r['employer'] if r['source'] in ('posting', 'filing') else '', r['who'], r['response'], r['quote']])
json.dump(out, open(D / '_hits.json', 'w'))

# ---- tables
import pandas as pd
APPSET = set(APPR) | {'y_micron_JR108610', 'rkelcorp_R0023796', 'y_visa_REF085268W'}
def tier(r):
    if r['source'] == 'posting' and any(a in r['id'] for a in APPSET) : return 'approved-tool duty'
    return 'control or unsanctioned use'
df = pd.DataFrame(out); df['tier'] = df.apply(tier, axis=1)
UNT = ('M041', 'M053', 'M054', 'M067')
df['untimestamped'] = df.id.str[:4].isin(UNT)
pd.DataFrame(out).assign(tier=df.tier).rename(columns={'text': '_t'})[['id','source','function','employer','who','response','quote','tier']].assign(
    employer=lambda x: x.employer.where(x.source.isin(['posting','filing']), '')).to_csv(D / 'corpus-hits.csv', index=False)
df.to_pickle(D / '_hits.pkl')
raw = collections.Counter((o['source'], o['term']) for o in cand)
rawdf = pd.Series(raw).unstack(0).fillna(0).astype(int)
rawdf.to_csv(D / '_rawterms.csv'); print(rawdf.to_string())
print(df.groupby('source').agg(n=('id','size'), w=('weight','sum')))
print(df.groupby(['source', 'response']).size().unstack(0).fillna(0))
print(df.groupby(['tier','source']).size().unstack(1).fillna(0))
print(df.groupby(['who','source']).size().unstack(1).fillna(0))
print(df[df.source=='posting'].groupby('function').agg(n=('id','size'),w=('weight','sum')).sort_values('n',ascending=False))
print(df[df.source=='filing'].groupby('function').size().sort_values(ascending=False))
print(df[df.source=='posting'].assign(d=lambda x:x.id.str.rsplit(':',n=1).str[0]).groupby('tier').agg(spans=('id','size'),postings=('d','nunique'),emp=('employer','nunique'),w=('weight','sum')))
print(df[df.source=='filing'].employer.nunique())
print(df[df.source.str.startswith('speech')][['id','source','untimestamped']])
print(pd.crosstab(df[df.source=='posting'].tier, df[df.source=='posting'].response))
print(pd.crosstab(df[df.source=='posting'].function, df[df.source=='posting'].tier))
print(df[df.source=='posting'].groupby('weight').size())
