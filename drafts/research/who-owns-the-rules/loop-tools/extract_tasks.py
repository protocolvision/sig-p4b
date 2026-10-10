"""Extract verbatim task statements from Corpus B documents with the Message Batches API.

triangulation-design.md, section 5. The prompt names no codes and none of our terms, so extraction stays
blind to the codebook. Every returned span is checked against its source text; spans that are not verbatim
are kept but flagged, and their rate is reported.

Input: a JSON Lines file, one document per line, with fields id, kind ("posting" or "filing") and text.

Usage (from loop-tools/, with the analytics venv):
  .venv/bin/python extract_tasks.py submit INPUT.jsonl --run NAME [--model claude-haiku-5-5]
  .venv/bin/python extract_tasks.py status --run NAME
  .venv/bin/python extract_tasks.py collect --run NAME
  .venv/bin/python extract_tasks.py agree --run-a NAME --run-b NAME

State and output go to corpus/b-raw/extract/<NAME>/ (ignored by git): batches.json, tasks.jsonl, report.json.
"""
import argparse, json, pathlib, re, sys, time

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "corpus" / "b-raw" / "extract"
BATCH_SIZE = 10_000

PROMPTS = {
    "posting": (
        "You read one job posting. List every task, duty or responsibility the person hired will perform. "
        "Copy each one exactly as written in the posting, one task per item; split a sentence only where it "
        "lists separate tasks, and then copy each part exactly. Leave out qualifications, required skills, "
        "education, benefits, pay, and descriptions of the company or team. If the posting lists no tasks, "
        "return an empty list."
    ),
    "filing": (
        "You read one passage from a company's annual or quarterly report. List every activity the passage "
        "says the company, its people or its systems perform, have started, or have stopped. Copy each one "
        "exactly as written, one activity per item. Leave out forecasts, general risk statements that name "
        "no activity, and legal boilerplate. If there are none, return an empty list."
    ),
}

SCHEMA = {
    "type": "object",
    "properties": {
        "tasks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "span": {"type": "string", "description": "the task, copied exactly from the text"},
                    "performer": {"type": "string", "enum": ["person", "software or agent", "both", "unclear"]},
                },
                "required": ["span", "performer"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["tasks"],
    "additionalProperties": False,
}


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
    state = {"model": a.model, "input": str(pathlib.Path(a.input).resolve()), "batches": []}
    for i in range(0, len(docs), BATCH_SIZE):
        chunk = docs[i : i + BATCH_SIZE]
        reqs = [
            Request(
                custom_id=doc["id"],
                params=MessageCreateParamsNonStreaming(
                    model=a.model,
                    max_tokens=8000,
                    system=[{"type": "text", "text": PROMPTS[doc["kind"]], "cache_control": {"type": "ephemeral"}}],
                    output_config={"effort": "low", "format": {"type": "json_schema", "schema": SCHEMA}},
                    messages=[{"role": "user", "content": doc["text"]}],
                ),
            )
            for doc in chunk
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
    texts = {doc["id"]: norm(doc["text"]) for doc in load_docs(state["input"])}
    n_docs = n_tasks = n_verbatim = 0
    failed = []
    with open(d / "tasks.jsonl", "w") as out:
        for bid in state["batches"]:
            for res in client.messages.batches.results(bid):
                if res.result.type != "succeeded":
                    failed.append({"id": res.custom_id, "type": res.result.type})
                    continue
                msg = res.result.message
                if msg.stop_reason != "end_turn":
                    failed.append({"id": res.custom_id, "type": msg.stop_reason})
                    continue
                text = next(b.text for b in msg.content if b.type == "text")
                n_docs += 1
                for k, t in enumerate(json.loads(text)["tasks"]):
                    verbatim = norm(t["span"]) in texts.get(res.custom_id, "")
                    n_tasks += 1
                    n_verbatim += verbatim
                    out.write(json.dumps({"doc_id": res.custom_id, "task_id": f"{res.custom_id}:{k}",
                                          "span": t["span"], "performer": t["performer"],
                                          "verbatim": verbatim, "model": state["model"]}) + "\n")
    report = {"model": state["model"], "docs": n_docs, "tasks": n_tasks,
              "verbatim_rate": round(n_verbatim / n_tasks, 4) if n_tasks else None, "failed": failed}
    (d / "report.json").write_text(json.dumps(report, indent=1))
    print(json.dumps({k: v for k, v in report.items() if k != "failed"}), f"failed={len(failed)}")


def agree(a):
    """Span-level F1 between two runs on the documents both extracted (normalised exact match)."""
    def spans(name):
        by_doc = {}
        for line in open(run_dir(name) / "tasks.jsonl"):
            r = json.loads(line)
            by_doc.setdefault(r["doc_id"], set()).add(norm(r["span"]))
        return by_doc
    sa, sb = spans(a.run_a), spans(a.run_b)
    tp = fa = fb = 0
    for doc in sa.keys() & sb.keys():
        tp += len(sa[doc] & sb[doc])
        fa += len(sa[doc] - sb[doc])
        fb += len(sb[doc] - sa[doc])
    p, r = tp / ((tp + fa) or 1), tp / ((tp + fb) or 1)
    f1 = 2 * p * r / ((p + r) or 1)
    print(json.dumps({"docs": len(sa.keys() & sb.keys()), "precision_a_vs_b": round(p, 3),
                      "recall_a_vs_b": round(r, 3), "span_f1": round(f1, 3)}))


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
