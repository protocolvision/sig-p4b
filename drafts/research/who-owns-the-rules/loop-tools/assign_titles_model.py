"""Assign O*NET-SOC codes to the job titles map_occupations.py routed to method "model".

For each such title the 10 best candidate occupations are found by token overlap with the O*NET
dictionary (occupation titles, alternate titles, reported titles), and claude-haiku-5-5 picks the best
code from those 10 or answers "none". The request goes through the Message Batches API; the reply is
structured JSON constrained to the 10 candidate codes plus "none". Client and batch patterns follow
extract_tasks.py.

Input: the CSV written by map_occupations.py (columns id, title, normalised, method, ...). Only rows
with method == "model" are sent.

Usage (from loop-tools/, with the analytics venv):
  .venv/bin/python assign_titles_model.py submit MAPPED.csv --run NAME [--model claude-haiku-5-5]
  .venv/bin/python assign_titles_model.py status --run NAME
  .venv/bin/python assign_titles_model.py collect --run NAME

collect writes corpus/b-raw/extract/<NAME>/assigned.csv: id, title, normalised, onet_code, method
("model-assigned", or "model-none" when the answer is none), onet_title, candidates. State is in
batches.json and candidates.json beside it. Merge assigned.csv back over the "model" rows yourself.
"""
import argparse, csv, json, pathlib, re, sys, time

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

from map_occupations import Mapper

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "corpus" / "b-raw" / "extract"
BATCH_SIZE = 10_000
N_CAND = 10

SYSTEM = (
    "You assign one O*NET-SOC occupation code to a job-posting title. You are given the title and a numbered "
    "list of candidate occupations. Choose the single candidate whose occupation best matches the work the "
    "title describes. Choose \"none\" if no candidate is a reasonable match; do not pick the least bad one. "
    "Judge by the work, not by a shared word: \"Product Manager\" is not a designer because both say "
    "\"product\". Answer with the candidate's code exactly as listed, or \"none\"."
)


def schema(codes):
    return {
        "type": "object",
        "properties": {"code": {"type": "string", "enum": list(codes) + ["none"]}},
        "required": ["code"],
        "additionalProperties": False,
    }


def candidates(m, norm, k=N_CAND):
    """Top-k O*NET codes by token overlap with the normalised title. Per code, the best dictionary title
    counts: score = (shared tokens, share of the posting's tokens, Jaccard); ties go to the code with the most
    dictionary titles, then the lowest code (as in map_occupations)."""
    toks = set(norm.split())
    best = {}
    for n, levels in m.index.items():
        nt = set(n.split())
        shared = len(toks & nt)
        if not shared:
            continue
        score = (shared, shared / len(toks), shared / len(toks | nt))
        for d in levels.values():
            for code in d:
                if code not in best or score > best[code]:
                    best[code] = score
    ranked = sorted(best, key=lambda c: (best[c][0] * -1, -best[c][1], -best[c][2], -m.code_count[c], c))
    return ranked[:k]


def run_dir(name):
    d = OUT / name
    d.mkdir(parents=True, exist_ok=True)
    return d


def submit(a):
    client = anthropic.Anthropic()
    m = Mapper()
    d = run_dir(a.run)
    with open(a.input, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["method"] == "model"]
    # one request per distinct normalised title; custom_id = t<index>
    uniq = {}
    for r in rows:
        uniq.setdefault(r["normalised"], r["title"])
    meta, reqs = {}, []
    for i, (norm, title) in enumerate(sorted(uniq.items())):
        cands = candidates(m, norm)
        cid = f"t{i}"
        meta[cid] = {"normalised": norm, "title": title, "candidates": cands}
        if not cands:
            continue                                   # nothing overlaps: leave as model-none without a call
        listing = "\n".join(f"{n + 1}. {c}  {m.occ.get(c, '')}" for n, c in enumerate(cands))
        reqs.append(Request(
            custom_id=cid,
            params=MessageCreateParamsNonStreaming(
                model=a.model,
                max_tokens=200,
                system=[{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
                output_config={"effort": "low", "format": {"type": "json_schema", "schema": schema(cands)}},
                messages=[{"role": "user", "content": f"Title: {title}\n\nCandidates:\n{listing}"}],
            ),
        ))
    state = {"model": a.model, "input": str(pathlib.Path(a.input).resolve()), "batches": []}
    for i in range(0, len(reqs), BATCH_SIZE):
        batch = client.messages.batches.create(requests=reqs[i : i + BATCH_SIZE])
        state["batches"].append(batch.id)
        print(f"submitted {batch.id}: {len(reqs[i : i + BATCH_SIZE])} requests", file=sys.stderr)
    (d / "candidates.json").write_text(json.dumps(meta, indent=1))
    (d / "batches.json").write_text(json.dumps(state, indent=1))
    print(f"{len(rows)} model rows, {len(uniq)} distinct titles, {len(reqs)} requests", file=sys.stderr)


def status(a):
    client = anthropic.Anthropic()
    state = json.loads((run_dir(a.run) / "batches.json").read_text())
    for bid in state["batches"]:
        b = client.messages.batches.retrieve(bid)
        print(bid, b.processing_status, b.request_counts)


def collect(a):
    client = anthropic.Anthropic()
    m = Mapper()
    d = run_dir(a.run)
    state = json.loads((d / "batches.json").read_text())
    meta = json.loads((d / "candidates.json").read_text())
    for bid in state["batches"]:
        while client.messages.batches.retrieve(bid).processing_status != "ended":
            time.sleep(60)
    answer, failed = {}, []
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
            code = json.loads(text)["code"]
            if code != "none" and code not in meta[res.custom_id]["candidates"]:
                failed.append({"id": res.custom_id, "type": "code-not-in-candidates"})
                continue
            answer[res.custom_id] = code
    n = {"model-assigned": 0, "model-none": 0, "failed": len(failed)}
    with open(d / "assigned.csv", "w", newline="", encoding="utf-8") as f, \
         open(state["input"], encoding="utf-8") as fin:
        w = csv.writer(f)
        w.writerow(["id", "title", "normalised", "onet_code", "method", "onet_title", "candidates"])
        by_norm = {v["normalised"]: (k, v) for k, v in meta.items()}
        for r in csv.DictReader(fin):
            if r["method"] != "model":
                continue
            cid, v = by_norm[r["normalised"]]
            if cid in answer or not v["candidates"]:
                code = answer.get(cid, "none")
                code = "" if code == "none" else code
                method = "model-assigned" if code else "model-none"
            else:
                continue                               # request failed: row stays "model"; see report.json
            n[method] += 1
            w.writerow([r["id"], r["title"], r["normalised"], code, method, m.occ.get(code, ""),
                        " ".join(v["candidates"])])
    (d / "report.json").write_text(json.dumps({"model": state["model"], **n, "failed_detail": failed}, indent=1))
    print(json.dumps(n))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("submit"); s.add_argument("input"); s.add_argument("--run", required=True)
    s.add_argument("--model", default="claude-haiku-5-5")
    for name in ("status", "collect"):
        p = sub.add_parser(name); p.add_argument("--run", required=True)
    a = ap.parse_args()
    {"submit": submit, "status": status, "collect": collect}[a.cmd](a)


if __name__ == "__main__":
    main()
