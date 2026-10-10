"""Calibration coding of historical recordings (loop-design-v2.md section 8, items 1 and 4).

Two independent coders (Message Batches API, same pattern as extract_tasks.py):
  A = claude-sonnet-5-5, B = claude-haiku-5-5.
Each reads one H-frame transcript and codes ONLY what the recording says:
  (a) activity bundle of the role, (b) authority arrangement, (c) use of the role's title,
with timestamps and quotes of 40 words or fewer. The prompt forbids any statement on whether the role lasted
(section 8.4). The frame supplies the role name and the recording date; nothing else about the role's history.
A quote counts only if it is verbatim in the transcript and at most 40 words; an item is "present" in the
effective code only if the coder said present AND at least one such quote supports it.

Usage (from loop-tools/):
  .venv/bin/python calibration_code.py submit
  .venv/bin/python calibration_code.py collect     # waits for the batches, writes raw + csv
  .venv/bin/python calibration_code.py kappa       # prints kappa per item
Output: ../results/rerun-2026-10-10/calibration-codes.csv ; raw state in ../corpus/b-raw/calibration/ (git-ignored).
"""
import argparse, csv, json, pathlib, re, sys, time

import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
TR = ROOT / "sources-v2" / "transcripts"
FRAME = ROOT / "sources-v2" / "media-historical.csv"
RAW = ROOT / "corpus" / "b-raw" / "calibration"
OUTCSV = ROOT / "results" / "rerun-2026-10-10" / "calibration-codes.csv"
CODERS = {"A": "claude-sonnet-5-5", "B": "claude-haiku-5-5"}
ITEMS = ["a_bundle", "b_authority", "c_title"]

ROLE_INFO = {
    "Site reliability engineering": ("site reliability engineer / site reliability engineering / SRE",
        "engineers who keep production services reliable using software-engineering methods: monitoring, incident response, capacity, automating operations work"),
    "DevOps": ("DevOps / devops engineer",
        "development and operations people working together: frequent deployment, automation of releases and infrastructure, shared work on running the systems"),
    "Chief information security officer": ("chief information security officer / CISO (or an equivalent named head of security)",
        "a senior officer who runs an organisation's information-security programme"),
    "Data scientist": ("data scientist",
        "extracting findings and building data products from large data with statistics and programming"),
    "Prompt engineer": ("prompt engineer / prompt engineering",
        "writing, testing and refining the inputs given to generative AI models to get the outputs wanted"),
    "Chief knowledge officer": ("chief knowledge officer / CKO / knowledge management lead",
        "leading an organisation's work to capture, share and use what its people know"),
    "Webmaster": ("webmaster",
        "running an organisation's web site: content, servers, production, staff"),
    "Social media manager / social customer care": ("social media manager / head of social media / social customer care",
        "running an organisation's presence and conversations on social platforms and serving customers there"),
}

PROMPT = """You code one recording (a transcript, or the text of a talk or interview) for a research study. Use ONLY what this recording says. Do not use outside knowledge about the person, the organisation, the role or what happened later. Do not say, guess or hint whether the role, title or practice lasted, spread, faded, succeeded or failed, and do not comment on history after the recording date. Transcripts come from speech recognition and contain errors (misspelled names and terms); read through them, but quote exactly what the text says.

The frame gives you the role to code for, the title forms to look for, and the recording date.

Code three items.

(a) bundle: Does the speaker describe the activities of this role (the activity bundle given in the frame)? Present only if the speaker describes what people in the role actually do or are meant to do, in some detail, in the first person or about named people or teams. A passing mention is not enough.

(b) authority: Does the speaker describe the authority arrangement of the role? That means one or more of: an agreement between parties about a trade-off (for example how much reliability against how fast change, or security against business speed); a mandate that says who may decide, stop, approve or override; a budget the role controls or is bound by; a number the role owns or is held to (a target, threshold, ratio, rate). It must be stated in the recording. Responsibility in general ("I am responsible for security", "we work together") is NOT enough on its own; there must be a described agreement, mandate, budget or owned number. Say "no" if it is not there.

(c) title: Does the speaker (or the text, for a heading or introduction that is part of the recording) use the role's title, in any of the forms listed in the frame, to name a job, team or person? Describing the work without the title is "no".

For each item return present (true/false) and up to 3 evidence entries, each with a timestamp and a quote. Timestamp: the [hh:mm:ss] marker of the line where the quote starts; if the text has no timestamps, write "none". Quote: copied exactly, character for character, from the text, at most 40 words; do not use "..." and do not join separate passages. If present is false, return an empty evidence list. For (b), if present, name the kind in "kind": trade-off agreement, mandate, budget, owned number, or none.

Also return recording_date: the date given in the frame, as YYYY, YYYY-MM or YYYY-MM-DD (the most precise the frame gives).

Return only the JSON."""

EV = {"type": "object", "properties": {"timestamp": {"type": "string"}, "quote": {"type": "string"}},
      "required": ["timestamp", "quote"], "additionalProperties": False}


def item_schema(with_kind=False):
    props = {"present": {"type": "boolean"}, "evidence": {"type": "array", "items": EV}}
    req = ["present", "evidence"]
    if with_kind:
        props["kind"] = {"type": "string", "enum": ["trade-off agreement", "mandate", "budget", "owned number", "none"]}
        req.append("kind")
    return {"type": "object", "properties": props, "required": req, "additionalProperties": False}


SCHEMA = {"type": "object",
          "properties": {"recording_date": {"type": "string"}, "a_bundle": item_schema(),
                         "b_authority": item_schema(True), "c_title": item_schema()},
          "required": ["recording_date", "a_bundle", "b_authority", "c_title"], "additionalProperties": False}


def frame_rows():
    with open(FRAME, newline="") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def available():
    return sorted(p.stem for p in TR.glob("H*.txt"))


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def clean_text(t):
    return norm(re.sub(r"^\[\d\d:\d\d:\d\d\]\s*", "", t, flags=re.M))


def message(hid, fr):
    titles, bundle = ROLE_INFO[fr["role"]]
    text = (TR / f"{hid}.txt").read_text()
    head = (f"FRAME\nrole: {fr['role']}\ntitle forms to look for: {titles}\nactivity bundle: {bundle}\n"
            f"recording date (from the frame): {fr['date']}\nrecording title: {fr['title']}\n"
            f"speakers: {fr['speakers']}\n\nRECORDING TEXT\n")
    return head + text


def submit(a):
    client = anthropic.Anthropic()
    RAW.mkdir(parents=True, exist_ok=True)
    fr = frame_rows()
    ids = available()
    state = {}
    for c, model in CODERS.items():
        reqs = [Request(custom_id=h, params=MessageCreateParamsNonStreaming(
            model=model, max_tokens=6000,
            system=[{"type": "text", "text": PROMPT, "cache_control": {"type": "ephemeral"}}],
            output_config={"format": {"type": "json_schema", "schema": SCHEMA}},
            messages=[{"role": "user", "content": message(h, fr[h])}])) for h in ids]
        b = client.messages.batches.create(requests=reqs)
        state[c] = {"model": model, "batch": b.id, "ids": ids}
        print(f"coder {c} {model}: {b.id}, {len(reqs)} requests", file=sys.stderr)
    (RAW / "batches.json").write_text(json.dumps(state, indent=1))


def collect(a):
    client = anthropic.Anthropic()
    state = json.loads((RAW / "batches.json").read_text())
    fr = frame_rows()
    rows, failed = [], []
    for c, s in state.items():
        while client.messages.batches.retrieve(s["batch"]).processing_status != "ended":
            time.sleep(30)
        for res in client.messages.batches.results(s["batch"]):
            h = res.custom_id
            if res.result.type != "succeeded" or res.result.message.stop_reason != "end_turn":
                failed.append((c, h, res.result.type))
                continue
            msg = res.result.message
            d = json.loads(next(b.text for b in msg.content if b.type == "text"))
            (RAW / f"{c}-{h}.json").write_text(json.dumps(d, indent=1))
            src = clean_text((TR / f"{h}.txt").read_text())
            row = {"id": h, "role": fr[h]["role"], "frame_date": fr[h]["date"], "coder": c, "model": s["model"],
                   "recording_date": d["recording_date"]}
            for it in ITEMS:
                ev = d[it]["evidence"]
                good = [e for e in ev if len(e["quote"].split()) <= 40 and norm(e["quote"]) in src]
                row[it + "_said"] = int(d[it]["present"])
                row[it] = int(d[it]["present"] and len(good) > 0)
                row[it + "_n_quotes"] = len(ev)
                row[it + "_n_verbatim"] = len(good)
                row[it + "_first_ts"] = good[0]["timestamp"] if good else ""
                row[it + "_quote"] = good[0]["quote"] if good else ""
            row["b_kind"] = d["b_authority"].get("kind", "")
            rows.append(row)
    rows.sort(key=lambda r: (r["id"], r["coder"]))
    OUTCSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTCSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows to {OUTCSV}; failed={failed}")


def kappa(x, y):
    n = len(x)
    po = sum(a == b for a, b in zip(x, y)) / n
    pa, pb = sum(x) / n, sum(y) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return po, (None if pe == 1 else (po - pe) / (1 - pe))


def report(a):
    rows = list(csv.DictReader(open(OUTCSV)))
    by = {}
    for r in rows:
        by.setdefault(r["id"], {})[r["coder"]] = r
    ids = [h for h, v in by.items() if len(v) == 2]
    print(f"n = {len(ids)} recordings")
    for col in ("", "_said"):
        for it in ITEMS:
            x = [int(by[h]["A"][it + col]) for h in ids]
            y = [int(by[h]["B"][it + col]) for h in ids]
            po, k = kappa(x, y)
            print(f"{it}{col or ' (effective)'}: agree={po:.2f} kappa={'undefined' if k is None else f'{k:.2f}'} "
                  f"A_yes={sum(x)} B_yes={sum(y)}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    for n, f in (("submit", submit), ("collect", collect), ("kappa", report)):
        sub.add_parser(n).set_defaults(fn=f)
    a = p.parse_args()
    a.fn(a)
