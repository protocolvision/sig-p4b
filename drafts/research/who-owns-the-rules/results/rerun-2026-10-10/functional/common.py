"""Shared loaders for the functional analysis. Run with loop-tools/.venv/bin/python from the study root."""
import json, math, pathlib, sys
import numpy as np, pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[3]
RUN = ROOT / "results" / "rerun-2026-10-10"
OUT = RUN / "functional"
sys.path.insert(0, str(OUT)); sys.path.insert(0, str(ROOT / "loop-tools"))
from function_map import FUNCTIONS, assign  # noqa: E402

KEY = ["ats", "board_id", "posting_id"]

def wilson(k, n, z=1.96):
    if n <= 0:
        return float("nan"), float("nan"), float("nan")
    k = min(max(k, 0.0), n)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(max(p * (1 - p) / n + z * z / (4 * n * n), 0))
    return p, max((c - r) / d, 0.0), min((c + r) / d, 1.0)

def kish(w):
    w = np.asarray(w, float)
    return float(w.sum() ** 2 / (w ** 2).sum()) if len(w) else 0.0

def load_postings():
    """Posting-level table (25,512 selected postings) with v2 O*NET code and two function columns:
    fn (title as written) and fn_q1 (AI terms stripped from the title)."""
    p = pd.read_csv(RUN / "instruments" / "I1-posting-level.csv.gz")
    m = pd.read_csv(ROOT / "corpus/b-raw/mapping/postings-mapped-v2.csv", usecols=KEY + ["onet_code"])
    m = m.rename(columns={"onet_code": "onet_v2"})
    p = p.merge(m, on=KEY, how="left")
    p["onet_use"] = p.onet_v2.where(p.onet_v2.notna(), p.onet_code)
    p["fn"] = [assign(t, c)[0] for t, c in zip(p.title, p.onet_use)]
    p["fn_src"] = [assign(t, c)[1] for t, c in zip(p.title, p.onet_use)]
    p["fn_q1"] = [assign(t, c, strip_ai=True)[0] for t, c in zip(p.title, p.onet_use)]
    p["sw"] = p.sw.fillna(1.0)
    return p

class Table:
    def __init__(self):
        self.rows = []
    def add(self, question, function, measure, value, low=None, high=None, n=None):
        self.rows.append(dict(question=question, function=function, measure=measure, value=value, low=low, high=high, n=n))
    def df(self):
        return pd.DataFrame(self.rows)
