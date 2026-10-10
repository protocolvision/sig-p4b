"""Assign O*NET-SOC codes to the job titles map_occupations.py routed to method "model".

For each such title the 10 best candidate occupations are found by token overlap with the O*NET
dictionary (occupation titles, alternate titles, reported titles), and claude-haiku-5-5 picks the best
code from those 10 or answers "none". The request goes through the Message Batches API; the reply is
structured JSON constrained to the 10 candidate codes plus "none". Client and batch patterns follow
extract_tasks.py.

Input: the CSV written by map_occupations.py (columns id, title, normalised, method, candidate_code, department, ...). The
candidate_code (best dictionary hit) is always among the 10 offered; department, if present, is shown as context. Only rows
with method == "model" are sent.

Usage (from loop-tools/, with the analytics venv):
  .venv/bin/python assign_titles_model.py submit MAPPED.csv --run NAME [--model claude-haiku-5-5]
  .venv/bin/python assign_titles_model.py status --run NAME
  .venv/bin/python assign_titles_model.py collect --run NAME

Two-stage version (replaces the top-10 candidate list, which often missed the right code):
  .venv/bin/python assign_titles_model.py submit2 MAPPED.csv --run NAME [--model claude-haiku-5-5]
  .venv/bin/python assign_titles_model.py collect2 --run NAME
Stage 1 picks the O*NET-SOC major group (first two digits) or none from the full numbered group list
(one fixed schema, an integer 0..N). Stage 2 picks the occupation from ALL occupations in that group
(one schema per group, an integer enum 0..n, so at most 23 schemas; batches are submitted group by group).
collect2 waits for stage 1, submits stage 2, waits, retries failed requests once with a larger max_tokens,
and writes assigned.csv (same columns as collect plus major_group; `candidates` is empty). It can be re-run
after an interruption: state is kept in stage1.json and stage2.json beside the output.

collect writes corpus/b-raw/extract/<NAME>/assigned.csv: id, title, normalised, onet_code, method
("model-assigned", or "model-none" when the answer is none), onet_title, candidates. State is in
batches.json and candidates.json beside it. Merge assigned.csv back over the "model" rows yourself.
"""
import argparse, csv, json, pathlib, re, sys, time

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

from map_occupations import Mapper, read_tsv

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "corpus" / "b-raw" / "extract"
BATCH_SIZE = 10_000
N_CAND = 10

SYSTEM = (
    "You assign one O*NET-SOC occupation code to a job-posting title. You are given the title and a numbered "
    "list of candidate occupations. Choose the single candidate whose occupation best matches the work the "
    "title describes. Choose \"none\" if no candidate is a reasonable match; do not pick the least bad one. "
    "A department may be given as context. Judge by the work, not by a shared word: \"Product Manager\" is not a designer because both say "
    "\"product\". Answer with the NUMBER of the best candidate (1-10) as listed, or 0 if none fits."
)


# One fixed schema for every request: per-request enums each need a grammar compilation, and the API
# allows 50 compilations per minute (first run: about 85% of requests errored on that limit).
SCHEMA = {
    "type": "object",
    "properties": {"choice": {"type": "integer", "enum": list(range(0, 11))}},
    "required": ["choice"],
    "additionalProperties": False,
}


def schema(codes):
    return SCHEMA


def candidates(m, norm, k=N_CAND, must=""):
    """Top-k O*NET codes by token overlap with the normalised title. Per code, the best dictionary title
    counts: score = (shared tokens, share of the posting's tokens, Jaccard); ties go to the code with the most
    dictionary titles, then the lowest code (as in map_occupations)."""
    toks = set(norm.split())
    if not hasattr(m, "_inv"):                     # inverted index token -> dictionary titles, built once
        m._inv = {}
        for n in m.index:
            for t in set(n.split()):
                m._inv.setdefault(t, []).append(n)
    pool = set()
    for t in toks:
        pool.update(m._inv.get(t, ()))
    best = {}
    for n in pool:
        levels = m.index[n]
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
    if must:                                       # a dictionary hit is always offered
        ranked = [must] + [c for c in ranked if c != must]
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
        uniq.setdefault((r["normalised"], r.get("department", ""), r.get("candidate_code", "")), r["title"])
    meta, reqs = {}, []
    for i, ((norm, dept, must), title) in enumerate(sorted(uniq.items())):
        cands = candidates(m, norm, must=must)
        cid = f"t{i}"
        meta[cid] = {"normalised": norm, "department": dept, "must": must, "title": title, "candidates": cands}
        if not cands:
            continue                                   # nothing overlaps: leave as model-none without a call
        listing = "\n".join(f"{n + 1}. {c}  {m.occ.get(c, '')}" for n, c in enumerate(cands))
        reqs.append(Request(
            custom_id=cid,
            params=MessageCreateParamsNonStreaming(
                model=a.model,
                max_tokens=2000,  # Haiku 5.5 thinks before answering; 200 truncated about 7% of answers
                system=[{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}],
                output_config={"effort": "low", "format": {"type": "json_schema", "schema": schema(cands)}},
                messages=[{"role": "user", "content": f"Title: {title}\n" + (f"Department: {dept}\n" if dept else "") + f"\nCandidates:\n{listing}"}],
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
            choice = json.loads(text)["choice"]
            cands = meta[res.custom_id]["candidates"]
            code = "none" if choice == 0 else (cands[choice - 1] if choice <= len(cands) else None)
            if code is None:
                failed.append({"id": res.custom_id, "type": "code-not-in-candidates"})
                continue
            answer[res.custom_id] = code
    n = {"model-assigned": 0, "model-none": 0, "failed": len(failed)}
    with open(d / "assigned.csv", "w", newline="", encoding="utf-8") as f, \
         open(state["input"], encoding="utf-8") as fin:
        w = csv.writer(f)
        w.writerow(["id", "title", "normalised", "onet_code", "method", "onet_title", "candidates"])
        by_norm = {(v["normalised"], v["department"], v["must"]): (k, v) for k, v in meta.items()}
        for r in csv.DictReader(fin):
            if r["method"] != "model":
                continue
            cid, v = by_norm[(r["normalised"], r.get("department", ""), r.get("candidate_code", ""))]
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


# ---------------------------------------------------------------- two-stage assignment
SOC_MAJOR = {
    "11": "Management", "13": "Business and Financial Operations", "15": "Computer and Mathematical",
    "17": "Architecture and Engineering", "19": "Life, Physical, and Social Science",
    "21": "Community and Social Service", "23": "Legal", "25": "Educational Instruction and Library",
    "27": "Arts, Design, Entertainment, Sports, and Media", "29": "Healthcare Practitioners and Technical",
    "31": "Healthcare Support", "33": "Protective Service", "35": "Food Preparation and Serving Related",
    "37": "Building and Grounds Cleaning and Maintenance", "39": "Personal Care and Service",
    "41": "Sales and Related", "43": "Office and Administrative Support",
    "45": "Farming, Fishing, and Forestry", "47": "Construction and Extraction",
    "49": "Installation, Maintenance, and Repair", "51": "Production", "53": "Transportation and Material Moving",
    "55": "Military Specific",
}
STAGE1_SYSTEM = (
    "You classify a job-posting title into one major occupational group of the O*NET-SOC taxonomy. You are given "
    "the title, sometimes the employing department, and a numbered list of major groups. Choose the group whose "
    "work the title describes. Answer 0 if the text is not a job title (for example \"General Application\", "
    "\"Talent Community\", \"Internship Programme\" with no function) or if you cannot tell the work. "
    "Judge by the work, not by a shared word. Answer with the NUMBER of the group as listed, or 0."
)
STAGE2_SYSTEM = (
    "You assign one O*NET-SOC occupation to a job-posting title. The title has already been placed in the major "
    "group \"{group}\". You are given the title, sometimes the employing department, and the numbered list of ALL "
    "occupations in that group. Choose the single occupation whose work best matches the title; if the title is "
    "a general or senior version, choose the closest broad occupation (including \"All Other\" entries). "
    "Answer 0 only if no occupation in the list is a reasonable match. Answer with the NUMBER as listed, or 0."
)


def schema_n(n):
    return {"type": "object", "properties": {"choice": {"type": "integer", "enum": list(range(0, n + 1))}},
            "required": ["choice"], "additionalProperties": False}


def taxonomy():
    occ = {r[0]: r[1] for r in read_tsv("Occupation Data.txt")}
    groups = {}
    for code in sorted(occ):
        groups.setdefault(code[:2], []).append(code)
    missing = [g for g in groups if g not in SOC_MAJOR]
    if missing:
        sys.exit(f"no name for major group(s) {missing}")
    return occ, dict(sorted(groups.items()))


def user_msg(title, dept):
    return f"Title: {title}\n" + (f"Department: {dept}\n" if dept else "")


def make_req(cid, model, system, schema_, title, dept, max_tokens=2000):
    return Request(custom_id=cid, params=MessageCreateParamsNonStreaming(
        model=model, max_tokens=max_tokens,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        output_config={"effort": "low", "format": {"type": "json_schema", "schema": schema_}},
        messages=[{"role": "user", "content": user_msg(title, dept)}]))


def send_batches(client, reqs, tag, state, state_path):
    """Submit reqs in chunks of BATCH_SIZE without waiting; state[tag] keeps the batch ids (saved after each
    batch), so a re-run resumes instead of resubmitting."""
    if tag in state:
        return
    ids = []
    for i in range(0, len(reqs), BATCH_SIZE):
        b = client.messages.batches.create(requests=reqs[i : i + BATCH_SIZE])
        ids.append(b.id)
        state[tag] = ids
        state_path.write_text(json.dumps(state, indent=1))
        print(f"{tag}: submitted {b.id} ({len(reqs[i : i + BATCH_SIZE])})", file=sys.stderr)


def gather(client, tag, state):
    """Wait for state[tag] and return ({custom_id: choice}, [failed custom_ids])."""
    answers, failed = {}, []
    for bid in state[tag]:
        while client.messages.batches.retrieve(bid).processing_status != "ended":
            time.sleep(60)
        for res in client.messages.batches.results(bid):
            if res.result.type != "succeeded" or res.result.message.stop_reason != "end_turn":
                failed.append(res.custom_id)
                continue
            text = next(b.text for b in res.result.message.content if b.type == "text")
            answers[res.custom_id] = json.loads(text)["choice"]
    return answers, failed


def submit2(a):
    client = anthropic.Anthropic()
    occ, groups = taxonomy()
    d = run_dir(a.run)
    with open(a.input, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["method"] == "model"]
    uniq = {}
    for r in rows:
        uniq.setdefault((r["normalised"], r.get("department", "")), r["title"])
    meta = {f"t{i}": {"normalised": n, "department": dp, "title": t}
            for i, ((n, dp), t) in enumerate(sorted(uniq.items()))}
    (d / "titles.json").write_text(json.dumps(meta))
    listing = "\n".join(f"{i + 1}. {g}  {SOC_MAJOR[g]}" for i, g in enumerate(groups))
    system = STAGE1_SYSTEM + "\n\nMajor groups:\n" + listing
    reqs = [make_req(cid, a.model, system, schema_n(len(groups)), v["title"], v["department"]) for cid, v in meta.items()]
    state = {"model": a.model, "input": str(pathlib.Path(a.input).resolve()), "groups": list(groups)}
    send_batches(client, reqs, "stage1", state, d / "stage1.json")
    print(f"{len(rows)} model rows, {len(uniq)} distinct (title, department), {len(reqs)} stage-1 requests", file=sys.stderr)


def collect2(a):
    client = anthropic.Anthropic()
    occ, groups = taxonomy()
    glist = list(groups)
    d = run_dir(a.run)
    s1 = json.loads((d / "stage1.json").read_text())
    meta = json.loads((d / "titles.json").read_text())
    model = s1["model"]
    # ---- stage 1
    ans1, bad = gather(client, "stage1", s1)
    if bad:                                            # retry once with more room
        retry = {}
        listing = "\n".join(f"{i + 1}. {g}  {SOC_MAJOR[g]}" for i, g in enumerate(glist))
        system = STAGE1_SYSTEM + "\n\nMajor groups:\n" + listing
        reqs = [make_req(c, model, system, schema_n(len(glist)), meta[c]["title"], meta[c]["department"], 4000) for c in bad]
        send_batches(client, reqs, "stage1-retry", s1, d / "stage1.json")
        more, bad = gather(client, "stage1-retry", s1)
        ans1.update(more)
    group_of = {c: (glist[v - 1] if 1 <= v <= len(glist) else None) for c, v in ans1.items()}
    # ---- stage 2, one schema (and one cached system prompt) per major group
    s2p = d / "stage2.json"
    s2 = json.loads(s2p.read_text()) if s2p.exists() else {"model": model}
    ans2, failed2 = {}, []
    plan = {}
    for g in glist:                                    # submit every group first, then wait for all
        cids = [c for c, gg in group_of.items() if gg == g]
        if not cids:
            continue
        codes = groups[g]
        system = STAGE2_SYSTEM.format(group=f"{g} {SOC_MAJOR[g]}") + "\n\nOccupations:\n" + \
            "\n".join(f"{i + 1}. {c}  {occ[c]}" for i, c in enumerate(codes))
        plan[g] = (cids, codes, system, schema_n(len(codes)))
        send_batches(client, [make_req(c, model, system, plan[g][3], meta[c]["title"], meta[c]["department"]) for c in cids],
                     f"g{g}", s2, s2p)
    for g, (cids, codes, system, sch) in plan.items():
        got, bad = gather(client, f"g{g}", s2)
        if bad:
            send_batches(client, [make_req(c, model, system, sch, meta[c]["title"], meta[c]["department"], 4000) for c in bad],
                         f"g{g}-retry", s2, s2p)
            more, bad = gather(client, f"g{g}-retry", s2)
            got.update(more)
        for c, v in got.items():
            ans2[c] = codes[v - 1] if 1 <= v <= len(codes) else "none"
        failed2 += bad
        print(f"group {g}: {len(cids)} titles, {len(bad)} failed", file=sys.stderr)
    n = {"model-assigned": 0, "model-none": 0, "stage1-none": 0, "unresolved": 0}
    by_key = {(v["normalised"], v["department"]): c for c, v in meta.items()}
    by_group = {}
    with open(d / "assigned.csv", "w", newline="", encoding="utf-8") as f, open(s1["input"], encoding="utf-8") as fin:
        w = csv.writer(f)
        w.writerow(["id", "title", "normalised", "onet_code", "method", "onet_title", "candidates", "major_group"])
        for r in csv.DictReader(fin):
            if r["method"] != "model":
                continue
            c = by_key[(r["normalised"], r.get("department", ""))]
            if c not in ans1:
                n["unresolved"] += 1
                continue                               # failed twice: stays "model"
            g = group_of[c]
            if g is None:
                n["stage1-none"] += 1
                n["model-none"] += 1
                w.writerow([r["id"], r["title"], r["normalised"], "", "model-none", "", "", ""])
                continue
            if c not in ans2:
                n["unresolved"] += 1
                continue
            code = ans2[c]
            code = "" if code == "none" else code
            n["model-assigned" if code else "model-none"] += 1
            if code:
                by_group[g] = by_group.get(g, 0) + 1
            w.writerow([r["id"], r["title"], r["normalised"], code, "model-assigned" if code else "model-none",
                        occ.get(code, ""), "", g])
    (d / "report.json").write_text(json.dumps({"model": model, **n, "assigned_by_major_group": dict(sorted(by_group.items())),
                                               "failed_stage2": failed2}, indent=1))
    print(json.dumps(n))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("submit"); s.add_argument("input"); s.add_argument("--run", required=True)
    s.add_argument("--model", default="claude-haiku-5-5")
    for name in ("status", "collect"):
        p = sub.add_parser(name); p.add_argument("--run", required=True)
    s2 = sub.add_parser("submit2"); s2.add_argument("input"); s2.add_argument("--run", required=True)
    s2.add_argument("--model", default="claude-haiku-5-5")
    c2 = sub.add_parser("collect2"); c2.add_argument("--run", required=True)
    a = ap.parse_args()
    {"submit": submit, "status": status, "collect": collect, "submit2": submit2, "collect2": collect2}[a.cmd](a)


if __name__ == "__main__":
    main()
