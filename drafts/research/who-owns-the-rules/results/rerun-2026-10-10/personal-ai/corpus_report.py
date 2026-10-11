import pandas as pd, json, re, csv
D = 'results/rerun-2026-10-10/personal-ai/'
df = pd.read_pickle(D + '_hits.pkl'); raw = pd.read_csv(D + '_rawterms.csv', index_col=0)
def md(t):
    t = t.copy(); idx = t.index.name or ''
    cols = [idx] + [str(c) for c in t.columns]
    rows = ['| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
    for i, r in t.iterrows(): rows.append('| ' + ' | '.join([str(i)] + [str(v) for v in r.values]) + ' |')
    return '\n'.join(rows)
P = df[df.source == 'posting'].assign(doc=lambda x: x.id.str.rsplit(':', n=1).str[0]); F = df[df.source == 'filing']
SP = df[df.source.str.startswith('speech')]
L = []
L.append("# Personal and unsanctioned AI at work: what our corpus says (Part B, descriptive)\n")
L.append("11 October 2026. Search of posting duty statements, speech spans and filing passages already in the corpus; no new collection. Script: `corpus_search.py` (search), `corpus_code.py` (coding, quote check, tables), `corpus_report.py` (this file). Hits: `corpus-hits.csv`.\n")
L.append("## Filings and postings mention the problem mostly as a risk or a duty to use approved tools; practitioners barely mention it\n")
L.append(f"Of {len(df)} kept hits, {len(P)} are posting duty statements ({P.doc.nunique()} postings, {P.employer.nunique()} employers), {len(F)} are filing passages ({F.employer.nunique()} companies) and {len(SP)} are speech passages. Postings that name a control (discover, monitor, block, approve) are concentrated in security roles; filings mostly state the risk of employees using unapproved tools without naming a control; the speech corpus has only two spans on the topic.\n")
L.append("## Method\n")
L.append("- Sources: `postings-haiku-all.tasks.jsonl` duty spans (25,220 postings with spans, joined to `postings-input.jsonl` group and the load_postings table for employer, title and function via `function_map.py`); `consensus-dedup.jsonl` (862 speech spans); `filings-input-v3.jsonl` (2,216 passages). For speech I also searched the surrounding paragraph text (`speech-input.jsonl`, 189 chunks) and the untimestamped paragraphs (`speech-input-notime.jsonl`, 42) as supplementary sources, because spans are short extracts.")
L.append("- Search: case-insensitive regular expressions, one per term, in `corpus_search.py` (the term list is the dictionary `TERMS`). Terms that are ambiguous alone (shadow IT, unauthorized, acceptable use, AI tool approval/intake, browser extensions, data leakage, DLP) require an AI or tool word within 80 characters. Each term counts once per span or passage.")
L.append("- Reading: every hit in speech was read. For postings, hits on the broad terms (approved tools, public AI tools, approval/intake, ChatGPT, DLP, data leakage) were read only if the span contains an AI word; hits on the narrow terms (shadow, unsanctioned, unapproved, unauthorized, personal, BYOD, acceptable use, policy) were all read. For filings, hits were read if the passage contains an AI word and an employee or user word (employee, workforce, personnel, staff, personal, user, shadow, unapproved, internal use and similar); the other filing hits (about 150 passages) are generic cybersecurity or product text with no employee reference and were not coded.")
L.append("- Kept: text about employees' (or staff's) use of AI tools or agents outside sanctioned channels, or a control or sanction route for that use. Excluded: security vendors describing products to customers (Zscaler, Palo Alto Networks, AvePoint, Netskope; 'shadow AI' appears in their product text), AI security of products and agents built for customers, general AI governance duties, and BYOD or personal-computer mentions with no AI context (for example Comcast 'activating BYOD to the network').")
L.append("- Coding: who = the function the text assigns the response to (security, IT, legal/compliance, data/AI, business, HR, not stated); for postings it is the role that owns the duty. Response = discover, block, approve/sanction, monitor, train, policy, or 'none stated (risk only)' for filing risk statements that name no response. Function: postings by `function_map.py` (title rules then O*NET, with its stated error); filings by SIC description; speech by the recording's function tag. A posting duty to 'use approved AI tools' is coded approve and flagged tier 'approved-tool duty'; everything else is tier 'control or unsanctioned use'.")
L.append("- Weights: rest20 postings carry sampling weight 5. Counts below are unweighted spans unless a 'weighted' column says otherwise.")
L.append("- Quotes are 40 words or fewer, checked by script as substrings of the source text (whitespace normalised; speech timestamps removed). No personal names or emails appear in the quotes; speech is cited by recording id.\n")
L.append("## Raw hits per source and term (before reading)\n")
raw = raw.rename(columns={'speech': 'speech spans', 'speech-text': 'speech paragraphs', 'speech-notime': 'speech untimestamped paragraphs', 'filing': 'filing passages', 'posting': 'posting spans'})[['posting spans','filing passages','speech spans','speech paragraphs','speech untimestamped paragraphs']]
raw.loc['TOTAL'] = raw.sum()
L.append(md(raw) + "\n")
L.append("Most raw hits are not about personal AI use. 'public AI tools' hits are mostly 'third-party AI' or 'external AI' in product text, and the postings' 'approved tools' hits are mostly about integrating with approved systems. 'personal account(s)' in postings is 'personal accountability'.\n")
L.append("## Kept hits by source and response\n")
t = pd.crosstab(df.response, df.source.replace({'speech-text': 'speech (paragraph)', 'speech-notime': 'speech (untimestamped)', 'speech': 'speech (span)'}), margins=True, margins_name='total')
L.append(md(t) + "\n")
L.append("Speech: M065, M052 and M081 are timestamped; M067 is untimestamped and shown separately. M041, M053 and M054 gave no relevant hits. M052 and M081 come from the paragraph text, not from extracted spans.\n")
L.append("## Postings: roles that carry the duty\n")
a = P.groupby('function').agg(spans=('id', 'size'), weighted=('weight', 'sum'))
a2 = pd.crosstab(P.function, P.tier)
a = a.join(a2).sort_values('spans', ascending=False); a.loc['total'] = a.sum()
L.append(md(a.astype(int)) + "\n")
L.append("Security roles hold " + str(int(((P.function=='security')&(P.tier=='control or unsanctioned use')).sum())) + f" of the {int((P.tier=='control or unsanctioned use').sum())} control spans in postings. Outside security, the typical duty is simply to use approved AI tools (" + str(int((P.tier=='approved-tool duty').sum())) + " spans, mostly software, manufacturing, IT and finance roles at a few employers such as Micron, Amgen and Visa).\n")
L.append("## Postings and filings: who and response\n")
w = pd.crosstab(df[df.source.isin(['posting','filing'])].who, df[df.source.isin(['posting','filing'])].source, margins=True, margins_name='total')
L.append(md(w) + "\n")
r = pd.crosstab(P.response, P.tier, margins=True, margins_name='total')
L.append("Postings, response by tier:\n\n" + md(r) + "\n")
L.append("Postings: weighted spans are " + str(int(P.weight.sum())) + f" ({int(P[P.tier=='control or unsanctioned use'].weight.sum())} control, {int(P[P.tier=='approved-tool duty'].weight.sum())} approved-tool duty).\n")
L.append("## Filings: industries\n")
L.append(md(F.groupby('function').size().sort_values(ascending=False).rename('passages').to_frame()) + "\n")
L.append(f"Thirteen of {len(F)} filing passages state the risk without a response; the rest name a policy ({int((F.response=='policy').sum())}), an approval route ({int((F.response=='approve').sum())}), a prohibition ({int((F.response=='block').sum())}) or training ({int((F.response=='train').sum())}). No filing passage mentions monitoring other than Arcturus's data-exfiltration detection, which sits in the same passage coded 'approve'.\n")
L.append("## Examples\n")
ex = ['hasense_8634067002:0', 'house_onetrust_8222894:2', 'cdw_R26_00002737:0', '0001635282-25-000215_1', '0001193125-26-051382_7', '0001193125-26-088391_0', 'M065_c06:2', 'M052_c01']
L.append("Verbatim, 40 words or fewer, checked by script.\n")
n = 1
for e in ex:
    h = df[df.id.str.endswith(e)].iloc[0]
    emp = f", {h.employer}" if h.employer else ''
    L.append(f"{n}. [{h.source}, {h.function}{emp}; who: {h.who}; response: {h.response}] \"{h.quote}\"")
    n += 1
L.append("\n## Limits\n")
L.append("- Postings state what a role does, not what a company practises, so a duty to 'discover unsanctioned AI tools' shows that the function exists in the hiring plan, not how common unsanctioned use is. Filings are risk disclosures; the same company text repeats across filings (JFrog three passages, Tenable five, Upstart three), and each passage is counted once.")
L.append("- Speech has almost no coverage: the interview sample is about AI adoption and the extractor kept task spans, so the topic appears in only four passages.")
L.append("- The filings prefilter and the AI-word prefilter for postings are judgement filters; recall of the terms outside them was not checked beyond the raw table. Function labels inherit the function map's O*NET error.")
L.append("- The 'approved-tool duty' tier is a wide reading of 'controls on use'; the 'control or unsanctioned use' tier is the narrower one.")
open(D + 'corpus-findings.md', 'w').write('\n'.join(L) + '\n')
print('\n'.join(L)[:200])
