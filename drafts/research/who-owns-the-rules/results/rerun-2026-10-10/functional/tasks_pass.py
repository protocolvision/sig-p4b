"""One pass over the 305,533 duty statements: per posting, the number of duty statements, the number flagged by the
I1 lexical screen (lex_flag), and the number matching each Q5 keyword family. Writes doc-duty-counts.csv.gz (no text)."""
from common import *
from i1_labour import lex_flag
from q5_keywords import hits, FAMILIES
rows = {}
ex = {}
for line in open(ROOT / "corpus/b-raw/extract/postings-haiku-all.tasks.jsonl"):
    r = json.loads(line)
    d = rows.setdefault(r["doc_id"], dict(n_duty=0, k_flag=0, **{f: 0 for f in FAMILIES}))
    d["n_duty"] += 1
    d["k_flag"] += lex_flag(r["span"])
    for f in hits(r["span"]):
        d[f] += 1
df = pd.DataFrame.from_dict(rows, orient="index").rename_axis("doc_id").reset_index()
df.to_csv(OUT / "doc-duty-counts.csv.gz", index=False)
print(df.shape, df[["n_duty", "k_flag"] + list(FAMILIES)].sum().to_dict())
