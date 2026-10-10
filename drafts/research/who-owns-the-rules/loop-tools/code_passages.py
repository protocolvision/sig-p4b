"""Code SEC filing passages with the fixed codebook, using the Message Batches API.

Deviation 10 (results/rerun-2026-10-10/deviations.md). The system prompt is the question text of
loop-prompts/filing-codes.md, verbatim (everything after the first '---' rule). Every yes-quote is checked
against its passage (whitespace-normalised, case-insensitive); quotes that are not verbatim are flagged.

Input: JSON Lines with id, text (plus cik, filed, section, filer_type, carried through by the analysis).

Usage (from loop-tools/, with the analytics venv):
  .venv/bin/python code_passages.py submit INPUT.jsonl --run NAME [--model claude-haiku-5-5]
  .venv/bin/python code_passages.py status --run NAME
  .venv/bin/python code_passages.py collect --run NAME
  .venv/bin/python code_passages.py agree --run-a NAME --run-b NAME

State and output go to corpus/b-raw/extract/<NAME>/: batches.json, codes.jsonl, report.json.
"""
import argparse, json, pathlib, re, sys, time

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "corpus" / "b-raw" / "extract"
CODEBOOK = HERE.parent / "loop-prompts" / "filing-codes.md"
BATCH_SIZE = 10_000
CODES = ["own_use", "product", "reorg", "body", "metric", "controls", "workforce", "rule_cited"]


def system_prompt():
    """Question text of the codebook: everything after the first horizontal rule, unchanged."""
    return CODEBOOK.read_text().split("\n---\n", 1)[1].strip()


def make_schema():
    one = {"type": "object",
           "properties": {"value": {"type": "string", "enum": ["yes", "no"]},
                          "quote": {"type": "string", "description": "exact quote from the passage; empty when no"}},
           "required": ["value", "quote"], "additionalProperties": False}
    props = {c: one for c in CODES}
    props["rule_name"] = {"type": "string", "description": "name of the law or regulator when rule_cited is yes; else empty"}
    return {"type": "object", "properties": props, "required": CODES + ["rule_name"], "additionalProperties": False}


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def run_dir(name):
    d = OUT / name
    d.mkdir(parents=True, exist_ok=True)
    return d


def load_docs(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def submit(a):
    client = anthropic.Anthropic()
    d = run_dir(a.run)
    docs = load_docs(a.input)
    bad = [x["id"] for x in docs if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", x["id"])]
    if bad:
        sys.exit(f"{len(bad)} ids are not valid batch custom_ids ([A-Za-z0-9_-], 1-64 chars), e.g. {bad[0]}")
    system, schema = system_prompt(), make_schema()
    state = {"model": a.model, "input": str(pathlib.Path(a.input).resolve()), "batches": []}
    for i in range(0, len(docs), BATCH_SIZE):
        reqs = [
            Request(
                custom_id=doc["id"],
                params=MessageCreateParamsNonStreaming(
                    model=a.model,
                    max_tokens=4000,
                    system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
                    output_config={"effort": "low", "format": {"type": "json_schema", "schema": schema}},
                    messages=[{"role": "user", "content": doc["text"]}],
                ),
            )
            for doc in docs[i : i + BATCH_SIZE]
        ]
        batch = client.messages.batches.create(requests=reqs)
        state["batches"].append(batch.id)
        print(f"submitted {batch.id}: {len(reqs)} requests", file=sys.stderr)
    (d / "batches.json").write_text(json.dumps(state, indent=1))


def status(a):
    client = anthropic.Anthropic()
    state = json.loads((run_dir(a.run) / "batches.json").read_text())
    for bid in state["batches"]:
        b = client.messages.batches.retrieve(bid)
        print(bid, b.processing_status, b.request_counts)


def collect(a):
    client = anthropic.Anthropic()
    d = run_dir(a.run)
    state = json.loads((d / "batches.json").read_text())
    for bid in state["batches"]:
        while client.messages.batches.retrieve(bid).processing_status != "ended":
            time.sleep(60)
    texts = {x["id"]: norm(x["text"]) for x in load_docs(state["input"])}
    failed, rows = [], []
    n_yes = n_verbatim = 0
    for bid in state["batches"]:
        for res in client.messages.batches.results(bid):
            if res.result.type != "succeeded":
                failed.append({"id": res.custom_id, "type": res.result.type})
                continue
            msg = res.result.message
            if msg.stop_reason != "end_turn":
                failed.append({"id": res.custom_id, "type": msg.stop_reason})
                continue
            out = json.loads(next(b.text for b in msg.content if b.type == "text"))
            row = {"doc_id": res.custom_id, "model": state["model"], "rule_name": out["rule_name"]}
            for c in CODES:
                yes = out[c]["value"] == "yes"
                q = out[c]["quote"]
                verbatim = (norm(q) in texts.get(res.custom_id, "")) if (yes and q.strip()) else None
                row[c] = {"value": out[c]["value"], "quote": q, "verbatim": verbatim}
                if yes:
                    n_yes += 1
                    n_verbatim += bool(verbatim)
            rows.append(row)
    rows.sort(key=lambda r: r["doc_id"])
    with open(d / "codes.jsonl", "w") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    report = {"model": state["model"], "docs": len(rows), "yes_codes": n_yes, "yes_verbatim": n_verbatim,
              "verbatim_rate": round(n_verbatim / n_yes, 4) if n_yes else None, "failed": failed}
    (d / "report.json").write_text(json.dumps(report, indent=1))
    print(json.dumps({k: v for k, v in report.items() if k != "failed"}), f"failed={len(failed)}")


def kappa(x, y):
    n = len(x)
    po = sum(a == b for a, b in zip(x, y)) / n
    pa, pb = sum(x) / n, sum(y) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return None if pe == 1 else (po - pe) / (1 - pe)


def agree(a):
    def load(name):
        return {r["doc_id"]: r for r in map(json.loads, open(run_dir(name) / "codes.jsonl"))}
    ra, rb = load(a.run_a), load(a.run_b)
    shared = sorted(set(ra) & set(rb))
    res = {"shared_passages": len(shared), "codes": {}}
    for c in CODES:
        x = [ra[i][c]["value"] == "yes" for i in shared]
        y = [rb[i][c]["value"] == "yes" for i in shared]
        k = kappa(x, y)
        res["codes"][c] = {"kappa": None if k is None else round(k, 3),
                           "yes_a": sum(x), "yes_b": sum(y), "both_yes": sum(p and q for p, q in zip(x, y)),
                           "prevalence_a": round(sum(x) / len(x), 3), "prevalence_b": round(sum(y) / len(y), 3),
                           "gate_0.6": k is not None and k >= 0.6}
    print(json.dumps(res, indent=1))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("submit"); s.add_argument("input"); s.add_argument("--run", required=True)
    s.add_argument("--model", default="claude-haiku-5-5")
    for name in ("status", "collect"):
        p = sub.add_parser(name); p.add_argument("--run", required=True)
    g = sub.add_parser("agree"); g.add_argument("--run-a", required=True); g.add_argument("--run-b", required=True)
    a = ap.parse_args()
    {"submit": submit, "status": status, "collect": collect, "agree": agree}[a.cmd](a)


if __name__ == "__main__":
    main()
