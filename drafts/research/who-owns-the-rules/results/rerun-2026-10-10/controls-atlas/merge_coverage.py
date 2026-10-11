"""Merge all taxonomy codes (reconciled sample, held-out set coded by Sonnet, single-coder rest) and compute coverage
by product, excluding rows that document a gap rather than a control. Writes coded-all.csv and coverage.md."""
import json, pathlib, re
import pandas as pd
D = pathlib.Path(__file__).resolve().parent
ROOT = D.parents[2]
inv = pd.read_csv(D / "inventory-all.csv").fillna("")
smp = pd.read_csv(D / "taxonomy-sample.csv").merge(inv[["control_id", "enforcement_point"]], on="control_id")
smp["is_gap"] = "no"; smp["source"] = "reconciled sample"
key = json.load(open(ROOT / "corpus/b-raw/coding/atlas-key.json"))
vs = pd.read_csv(D / "verify-S.csv")
vs = vs[vs.id.map(lambda i: key[i]["src"] == "real")].copy()
vs["control_id"] = vs.id.map(lambda i: key[i]["orig"])
hold = vs[["control_id", "object", "mechanism", "enforcement_point"]].copy(); hold["is_gap"] = "no"; hold["source"] = "held-out (Sonnet code)"
rest = pd.concat([pd.read_csv(D / "coded-rest-1.csv"), pd.read_csv(D / "coded-rest-2.csv")]); rest["source"] = "single coder"
allc = pd.concat([smp[["control_id", "object", "mechanism", "enforcement_point", "is_gap", "source"]], hold, rest], ignore_index=True)
tax = open(D / "taxonomy.md").read()
m = re.search(r"(?is)documented gap.*", tax)
gapids = set(re.findall(r"\b(?:AH|BF|CD|EG)-\d{3,4}\b", m.group(0)[:4000])) if m else set()
allc.loc[allc.control_id.isin(gapids) & (allc.source == "reconciled sample"), "is_gap"] = "yes"
full = inv[["control_id", "product", "group"]].merge(allc, on="control_id", how="left")
assert full.object.notna().all(), full.object.isna().sum()
full.to_csv(D / "coded-all.csv", index=False)
ctl = full[full.is_gap != "yes"]
obj = ctl.groupby("object").agg(controls=("control_id", "count"), products=("product", "nunique"), groups=("group", "nunique")).sort_values("products", ascending=False)
mech = ctl.groupby("mechanism").agg(controls=("control_id", "count"), products=("product", "nunique")).sort_values("products", ascending=False)
ep = ctl.groupby("enforcement_point").agg(controls=("control_id", "count"), products=("product", "nunique")).sort_values("products", ascending=False)
grp = pd.crosstab(ctl.object, ctl.group, values=ctl["product"], aggfunc="nunique").fillna(0).astype(int)
md = ["# Coverage (all coded controls, documented gaps excluded)", "",
      f"{len(ctl)} controls ({(full.is_gap == 'yes').sum()} gap rows excluded), {ctl['product'].nunique()} products and protocols.", "",
      "## By object (products documenting at least one control)", "", obj.to_markdown(), "", "## By mechanism", "", mech.to_markdown(), "",
      "## By enforcement point", "", ep.to_markdown(), "",
      "## Products per object by group (A business platforms, B cloud runtimes, C model providers, D coding agents, E guardrails, F gateways, G identity/governance, H protocols)", "", grp.to_markdown()]
(D / "coverage.md").write_text("\n".join(md) + "\n")
print("\n".join(md[:30]))
