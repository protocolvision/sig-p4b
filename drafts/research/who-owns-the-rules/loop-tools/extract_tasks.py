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
import argparse, json, pathlib, re, statistics, sys, time

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
    # Filing prompt history. v1 (git history) asked for activities of the company, its people "or its
    # systems": precision 0.39 on the clean check. v2 (10 October 2026) added exclusions and negative
    # examples (results/rerun-2026-10-10/review/extraction-check-filings.md) but still let product
    # capability through. v3 (14 October 2026, review items C1-C2) keeps only what the company's people,
    # teams or functions do, including directing or running agents in the firm's own operations;
    # product capability is excluded rather than labelled.
    "filing": (
        "You read one passage from a company's annual or quarterly report. List every activity that THIS "
        "company's people, teams or functions have actually performed, are performing, have started or have "
        "stopped, as stated in the passage. This includes work in which they direct, configure, supervise or "
        "run agents or software in the company's own operations. Copy each one exactly, character for "
        "character (keep quotes, capitals and punctuation; never use \"...\"), one complete clause per "
        "item.\n\n"
        "Do NOT include:\n"
        "- what a product, platform or system does, can do, is designed to do, or enables customers to do "
        "(\"X enables\", \"customers can\", \"allows organizations to\"), including anything it does for "
        "customers;\n"
        "- mergers, acquisitions, divestitures, financing, capital raising and other corporate transactions;\n"
        "- actions by customers, partners, competitors, regulators, merchants, acquired companies before the "
        "acquisition, or the market, and any other party's actions;\n"
        "- forecasts, intentions and plans (expect, intend, plan, will, potential, may, could);\n"
        "- goals, priorities or commitments (focused on, committed to, our strategy is);\n"
        "- risk statements, hypotheticals, accounting definitions, and legal or non-GAAP boilerplate.\n\n"
        "Before you output an item, check that its grammatical subject is the company (we, the Company, a "
        "named subsidiary) or its people, teams or functions, and that the verb describes something done, "
        "not something possible. If none qualify, return an empty list.\n\n"
        "For each item, set performer to: person (people do the work), \"agent in own operations\" (software "
        "or agents run in the company's own operations do the work), both, or unclear.\n\n"
        "Examples of what NOT to extract:\n"
        "- \"the AI agents can operate independently to perform tasks across various business functions\" "
        "(a product capability)\n"
        "- \"The C3 AI orchestrator coordinates multiple AI agents, invokes specialized machine-learning "
        "models or mathematical tools as necessary and handles all data types and tasks\" (a product feature)\n"
        "- \"traditional and non-traditional competitors use other, new data sources and technologies\" "
        "(competitors' actions)\n"
        "- \"we are focused on expanding profitability, free cash flows and capital return\" (a goal)\n"
        "- \"We intend to continue to invest in our research and development capabilities\" (an intention)\n"
        "- \"We expect to continue to invest heavily in generative AI\" (a forecast)\n"
        "- \"remain committed to organic initiatives and a programmatic approach to growth through tuck-in "
        "acquisitions and divestitures\" (a priority and M&A)"
    ),
    # Speech prompt v1 (loop-design-v2.md section 5, stratum S7). Names no codes and none of our terms.
    "speech": (
        "You read one excerpt from a transcript of a talk or conversation. Each line starts with a "
        "[HH:MM:SS] timestamp; a header gives the speakers' names, roles and organisations. List every "
        "activity that a speaker says THEY or THEIR TEAM do, did, are doing or have started, as stated in "
        "the excerpt. This includes work in which they direct, configure, supervise or run software or "
        "agents. Copy each one exactly, character for character, from the transcript (never use \"...\"; "
        "do not copy the timestamp), one activity per item, as a complete clause.\n\n"
        "For each item give:\n"
        "- speaker: the speaker's name if you can identify who is talking from the excerpt, else \"unknown\";\n"
        "- speaker_relation: self (the speaker does it), own team (the speaker's team or organisation does "
        "it), other team (a named group other than the speaker's own does it), or general claim (a "
        "statement about what companies, teams or people in general do);\n"
        "- performer_type: person (people do the work), agent (software or an AI agent does the work), or "
        "both;\n"
        "- timestamp: the nearest preceding [HH:MM:SS] timestamp in the excerpt, written as HH:MM:SS.\n\n"
        "Do NOT include:\n"
        "- questions asked by a host or interviewer;\n"
        "- what a product or tool can do, is designed to do or will do for customers (a pitch);\n"
        "- predictions, hopes, intentions and plans (will, going to, expect, might, could);\n"
        "- opinions, advice and recommendations about what others should do.\n\n"
        "Statements about what companies in general do may be returned only with speaker_relation = "
        "general claim. If no activity qualifies, return an empty list."
    ),
}
PROMPT_VERSION = {"posting": "v1", "filing": "v3", "speech": "v1"}

def make_schema(performers):
    return {
        "type": "object",
        "properties": {
            "tasks": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "span": {"type": "string", "description": "the task, copied exactly from the text"},
                        "performer": {"type": "string", "enum": performers},
                    },
                    "required": ["span", "performer"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["tasks"],
        "additionalProperties": False,
    }


# Postings keep the original performer values; the filing schema (v3) drops product capability.
def make_speech_schema():
    s = make_schema(["person", "agent", "both"])
    item = s["properties"]["tasks"]["items"]
    item["properties"].pop("performer")
    item["properties"]["speaker"] = {"type": "string"}
    item["properties"]["speaker_relation"] = {"type": "string", "enum": ["self", "own team", "other team", "general claim"]}
    item["properties"]["performer_type"] = {"type": "string", "enum": ["person", "agent", "both"]}
    item["properties"]["timestamp"] = {"type": "string", "description": "HH:MM:SS"}
    item["required"] = ["span", "speaker", "speaker_relation", "performer_type", "timestamp"]
    return s


SCHEMAS = {"speech": make_speech_schema(), "posting": make_schema(["person", "software or agent", "both", "unclear"]),
           "filing": make_schema(["person", "agent in own operations", "both", "unclear"])}


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
    bad = [doc["id"] for doc in docs if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", doc["id"])]
    if bad:
        sys.exit(f"{len(bad)} ids are not valid batch custom_ids ([A-Za-z0-9_-], 1-64 chars), e.g. {bad[0]}")
    state = {"model": a.model, "input": str(pathlib.Path(a.input).resolve()), "batches": [],
             "prompt_version": PROMPT_VERSION}
    for i in range(0, len(docs), BATCH_SIZE):
        chunk = docs[i : i + BATCH_SIZE]
        reqs = [
            Request(
                custom_id=doc["id"],
                params=MessageCreateParamsNonStreaming(
                    model=a.model,
                    max_tokens=8000,
                    system=[{"type": "text", "text": PROMPTS[doc["kind"]], "cache_control": {"type": "ephemeral"}}],
                    output_config={"effort": "low", "format": {"type": "json_schema", "schema": SCHEMAS[doc["kind"]]}},
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
    docs = {doc["id"]: doc for doc in load_docs(state["input"])}
    # Speech: clauses run across transcript lines, so timestamps are removed before the verbatim check.
    texts = {i: norm(re.sub(r"\[\d\d:\d\d:\d\d\]\s*", "", doc["text"]) if doc.get("kind") == "speech" else doc["text"])
             for i, doc in docs.items()}
    n_docs = n_tasks = n_verbatim = 0
    failed, rows = [], []
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
                row = {"doc_id": res.custom_id, "task_id": f"{res.custom_id}:{k}",
                       "span": t["span"], "performer": t.get("performer"),
                       "verbatim": verbatim, "model": state["model"],
                       "prompt_version": state.get("prompt_version")}
                # Speech schema carries extra fields (speaker, speaker_relation, performer_type, timestamp).
                row.update({f: v for f, v in t.items() if f not in ("span", "performer")})
                if docs.get(res.custom_id, {}).get("kind") == "speech":
                    row.pop("performer")
                rows.append(row)
    # Undeduplicated spans, one row per extraction: used by agree().
    with open(d / "tasks-raw.jsonl", "w") as out:
        for r in rows:
            out.write(json.dumps(r) + "\n")
    rows, n_dedup = dedupe_filings(rows, docs)
    with open(d / "tasks.jsonl", "w") as out:
        for r in rows:
            out.write(json.dumps(r) + "\n")
    report = {"model": state["model"], "docs": n_docs, "tasks": n_tasks, "tasks_after_dedupe": len(rows),
              "filing_spans_merged_as_repeats": n_dedup,
              "verbatim_rate": round(n_verbatim / n_tasks, 4) if n_tasks else None, "failed": failed}
    (d / "report.json").write_text(json.dumps(report, indent=1))
    print(json.dumps({k: v for k, v in report.items() if k != "failed"}), f"failed={len(failed)}")


def dedupe_filings(rows, docs):
    """Filings only: one row per (cik, normalised span), from the company's earliest filing.

    Adds n_repeats (occurrences across the company's passages) and filed_dates (sorted filing date of each
    occurrence) to the kept row. Postings pass through unchanged. Review item C1, fix 2.
    """
    keep, groups = [], {}
    for r in rows:
        doc = docs.get(r["doc_id"], {})
        if doc.get("kind") != "filing":
            keep.append(r)
            continue
        groups.setdefault((doc.get("cik"), norm(r["span"])), []).append((doc.get("filed") or "", r["doc_id"], r))
    for occ in groups.values():
        occ.sort(key=lambda x: (x[0], x[1], x[2]["task_id"]))
        first = dict(occ[0][2])
        first["cik"] = docs[occ[0][1]].get("cik")
        first["filed"] = occ[0][0]
        first["n_repeats"] = len(occ)
        first["filed_dates"] = [o[0] for o in occ]
        keep.append(first)
    n_merged = sum(len(o) - 1 for o in groups.values())
    return keep, n_merged


def agree(a):
    """Agreement gate between two runs on the documents both extracted (design section 5, review item C3).

    Matching rule (fixed in log.md): one-to-one greedy matching on word-set Jaccard >= 0.5, highest
    similarity first. Reports P, R, F1 for run A against run B, unmatched spans in both directions,
    documents where exactly one run returned nothing (counted as misses: their spans are all unmatched),
    exact-match F1 (diagnostic only) and the median per-document count ratio A/B (gate: [0.8, 1.25]).
    Uses tasks-raw.jsonl (before per-company dedupe) when present.
    """
    def spans(name):
        f = run_dir(name) / "tasks-raw.jsonl"
        f = f if f.exists() else run_dir(name) / "tasks.jsonl"
        by_doc = {}
        for line in open(f):
            r = json.loads(line)
            by_doc.setdefault(r["doc_id"], []).append(norm(r["span"]))
        return by_doc

    def words(x):
        return frozenset(re.findall(r"\w+", x))

    def match(xs, ys):
        wx, wy = [words(x) for x in xs], [words(y) for y in ys]
        cand = []
        for i, p in enumerate(wx):
            for j, q in enumerate(wy):
                u = len(p | q)
                if u and len(p & q) / u >= 0.5:
                    cand.append((-len(p & q) / u, i, j))
        cand.sort()
        ui, uj, n = set(), set(), 0
        for _, i, j in cand:
            if i not in ui and j not in uj:
                ui.add(i); uj.add(j); n += 1
        return n

    def prf(tp, na, nb):
        p, r = tp / (na or 1), tp / (nb or 1)
        return p, r, 2 * p * r / ((p + r) or 1)

    sa, sb = spans(a.run_a), spans(a.run_b)
    def universe(name):
        """Documents the run was asked to extract and returned a result for (failed requests excluded)."""
        d = run_dir(name)
        ids = {doc["id"] for doc in load_docs(json.loads((d / "batches.json").read_text())["input"])}
        return ids - {f["id"] for f in json.loads((d / "report.json").read_text())["failed"]}

    docs = universe(a.run_a) & universe(a.run_b)
    tp = exact = na = nb = missed_docs = 0
    ratios = []
    for doc in docs:
        xa, xb = sa.get(doc, []), sb.get(doc, [])
        if not (xa or xb):
            continue
        na += len(xa); nb += len(xb)
        tp += match(xa, xb)
        exact += len(set(xa) & set(xb))
        if bool(xa) != bool(xb):
            missed_docs += 1
        if xa and xb:
            ratios.append(len(xa) / len(xb))
        else:
            ratios.append(0.0 if xb else float("inf"))
    p, r, f1 = prf(tp, na, nb)
    _, _, f1e = prf(exact, na, nb)
    ratio = statistics.median(ratios) if ratios else None
    print(json.dumps({
        "docs_in_both_runs": len(docs), "docs_with_spans": len(ratios), "docs_one_model_empty": missed_docs,
        "spans_a": na, "spans_b": nb, "matched": tp,
        "unmatched_a": na - tp, "unmatched_b": nb - tp,
        "precision_a_vs_b": round(p, 3), "recall_a_vs_b": round(r, 3), "jaccard_f1": round(f1, 3),
        "exact_f1_diagnostic": round(f1e, 3),
        "median_count_ratio_a_over_b": round(ratio, 3) if ratio is not None else None,
        "count_ratio_gate_0.8_1.25": ratio is not None and 0.8 <= ratio <= 1.25,
    }))


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
