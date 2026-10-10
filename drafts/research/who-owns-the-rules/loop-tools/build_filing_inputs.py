"""Build the extraction input for SEC filings (v3): triangulation-design.md 4.2, review item C1.

Replaces the undocumented step that turned passages.jsonl into filings-input.jsonl. Steps, each counted:
  1. re-cut the +/-150-word windows from the fetched filing text (same phrases and section rules as
     edgar_fetch.py), one window per phrase match;
  2. drop amendments (10-K/A, 10-Q/A) when the original filing (same CIK, same period, base form) is present;
  3. merge overlapping windows within each filing section into one passage per merged interval;
  4. keep only business, risk_factors, mdna and controls for extraction; "other" goes to a separate file;
  5. tag each filer with its SIC code (EDGAR submissions JSON); filer_type = vendor for SIC 7370-7374 and
     3570-3579, else adopter;
  6. draw a 10% sample (seed 20261014) of the extraction input.

Standard library only. SIC lookups are cached in corpus/b-raw/filings/sic/ and stay under 5 requests/sec.

Usage (from loop-tools/): python3 build_filing_inputs.py
Outputs: corpus/b-raw/extract/filings-input-v3.jsonl, filings-input-v3-10pct.jsonl,
         corpus/b-raw/extract/filings-other-v3.jsonl, results/rerun-2026-10-10/corpus-b/filings-inputs.md
"""
import bisect
import json
import random
import re
from collections import Counter, defaultdict

import edgar_fetch as ef

ROOT, RAW = ef.ROOT, ef.RAW
EXTRACT = ROOT / "corpus" / "b-raw" / "extract"
REPORT = ef.OUT / "filings-inputs.md"
SIC_DIR = RAW / "sic"
KEEP = ("business", "risk_factors", "mdna", "controls")
SEED = 20261014
FRACTION = 0.10


def windows_for(text, form):
    """Yield (section, first_word, last_word_exclusive) for every phrase match, plus the word spans."""
    marks = ef.split_sections(text, form)
    starts = [m[0] for m in marks]
    words = [(m.start(), m.end()) for m in re.finditer(r"\S+", text)]
    wstarts = [w[0] for w in words]
    out = []
    for phrase in ef.PHRASES:
        pat = re.compile(r"(?<![A-Za-z0-9])" + r"\s+".join(map(re.escape, phrase.split())) + r"(?![A-Za-z0-9])", re.I)
        for m in pat.finditer(text):
            sec = marks[bisect.bisect_right(starts, m.start()) - 1][1]
            i = bisect.bisect_right(wstarts, m.start()) - 1
            j = bisect.bisect_right(wstarts, m.end() - 1) - 1
            out.append((sec, max(0, i - ef.WORDS), min(len(words), j + 1 + ef.WORDS)))
    return out, words


def merge(intervals):
    """Union of overlapping [a, b) intervals (touching intervals stay separate)."""
    merged = []
    for a, b in sorted(intervals):
        if merged and a < merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    return merged


def sic_for(cik):
    SIC_DIR.mkdir(parents=True, exist_ok=True)
    p = SIC_DIR / f"CIK{int(cik):010d}.json"
    if not p.exists():
        raw = ef.get(f"https://data.sec.gov/submissions/CIK{int(cik):010d}.json")  # throttled, UA set in ef
        p.write_text(raw.decode() if raw else "{}")
    d = json.loads(p.read_text() or "{}")
    sic = str(d.get("sic") or "")
    return sic, d.get("sicDescription") or ""


def is_vendor(sic):
    return sic.isdigit() and (7370 <= int(sic) <= 7374 or 3570 <= int(sic) <= 3579)


def main():
    filings = {a: r for a, r in ef.load_hits().items() if (RAW / f"{a}.txt").exists()}
    n = {}
    raw_w = {a: windows_for((RAW / f"{a}.txt").read_text(), r["form"]) for a, r in filings.items()}
    n["windows"] = sum(len(w[0]) for w in raw_w.values())
    n["windows_by_section"] = Counter(s for w, _ in raw_w.values() for s, _, _ in w)
    n["filings"] = len(filings)

    # 2. amendments
    originals = {(r["cik"], r["period"], r["form"]) for r in filings.values() if not r["form"].endswith("/A")}
    drop = {a for a, r in filings.items() if r["form"].endswith("/A") and (r["cik"], r["period"], r["form"][:-2]) in originals}
    n["amend_filings_total"] = sum(r["form"].endswith("/A") for r in filings.values())
    n["amend_filings_dropped"] = len(drop)
    n["windows_after_amend"] = sum(len(raw_w[a][0]) for a in filings if a not in drop)

    # 3. merge within section
    passages = []
    for a in sorted(filings):
        if a in drop:
            continue
        r = filings[a]
        wins, words = raw_w[a]
        text = (RAW / f"{a}.txt").read_text()
        by_sec = defaultdict(list)
        for sec, i, j in wins:
            by_sec[sec].append((i, j))
        k = 0
        for sec in sorted(by_sec):
            for i, j in merge(by_sec[sec]):
                body = text[words[i][0]:words[j - 1][1]].replace("\n", " ")
                head = f"Company: {r['company']}. Form {r['form']}, filed {r['filed']}. Section: {sec}.\n\n"
                passages.append({"id": f"{a}_{k}", "kind": "filing", "text": head + body, "cik": r["cik"],
                                 "filed": r["filed"], "section": sec})
                k += 1
    n["merged"] = len(passages)
    n["merged_by_section"] = Counter(p["section"] for p in passages)

    # 4. sections
    kept = [p for p in passages if p["section"] in KEEP]
    other = [p for p in passages if p["section"] not in KEEP]

    # 5. SIC
    ciks = sorted({p["cik"] for p in passages})
    sic = {}
    for c in ciks:
        try:
            sic[c] = sic_for(c)
        except Exception as e:  # leave untagged rather than guess
            print(f"SIC lookup failed for {c}: {e}")
            sic[c] = ("", "")
    for p in kept + other:
        s, desc = sic[p["cik"]]
        p.update(sic=s, sic_description=desc, filer_type="vendor" if is_vendor(s) else "adopter")
    n["no_sic"] = sum(1 for c in ciks if not sic[c][0])

    def write(path, rows):
        with open(path, "w") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")

    EXTRACT.mkdir(parents=True, exist_ok=True)
    write(EXTRACT / "filings-input-v3.jsonl", kept)
    write(EXTRACT / "filings-other-v3.jsonl", other)
    ids = sorted(p["id"] for p in kept)
    pick = set(random.Random(SEED).sample(ids, round(FRACTION * len(ids))))
    sample = [p for p in kept if p["id"] in pick]
    write(EXTRACT / "filings-input-v3-10pct.jsonl", sample)

    ft = Counter(p["filer_type"] for p in kept)
    fc = {t: len({p["cik"] for p in kept if p["filer_type"] == t}) for t in ("vendor", "adopter")}
    st = Counter(p["filer_type"] for p in sample)
    old = ef.ROOT / "corpus" / "b-raw" / "extract" / "filings-input.jsonl"
    n_old = sum(1 for _ in open(old)) if old.exists() else "n/a"
    L = ["# Filing inputs v3: counts per step", "",
         "Built by `loop-tools/build_filing_inputs.py` (design 4.2; review item C1). Windows are +/-150 words around each phrase match.", "",
         "| Step | Filings | Passages |", "|---|---|---|",
         f"| Old `filings-input.jsonl` (undocumented step, from 5,319 windows) | | {n_old} |",
         f"| 1. Windows re-cut from fetched filings | {n['filings']} | {n['windows']} |",
         f"| 2. Drop amendments with original present ({n['amend_filings_dropped']} of {n['amend_filings_total']} amendments) | {n['filings'] - len(drop)} | {n['windows_after_amend']} |",
         f"| 3. Merge overlapping windows within section | {len({p['id'].rsplit('_', 1)[0] for p in passages})} | {n['merged']} |",
         f"| 4a. Keep business, risk_factors, mdna, controls (extraction input) | {len({p['id'].rsplit('_', 1)[0] for p in kept})} | {len(kept)} |",
         f"| 4b. `other` (stored separately, not extracted) | | {len(other)} |",
         f"| 6. 10% sample, seed {SEED} | | {len(sample)} |", "",
         "## Passages by section", "", "| Section | Windows (step 1) | Merged (step 3) |", "|---|---|---|"]
    for s in sorted(set(n["windows_by_section"]) | set(n["merged_by_section"])):
        L.append(f"| {s} | {n['windows_by_section'][s]} | {n['merged_by_section'][s]} |")
    L += ["", "## Vendor / adopter split (SIC 7370-7374 and 3570-3579 = vendor)", "",
          "| Set | Vendor | Adopter | Vendor share |", "|---|---|---|---|"]
    L.append(f"| Passages in v3 input | {ft['vendor']} | {ft['adopter']} | {ft['vendor'] / len(kept):.1%} |")
    L.append(f"| Filers (CIKs) | {fc['vendor']} | {fc['adopter']} | {fc['vendor'] / (fc['vendor'] + fc['adopter']):.1%} |")
    L.append(f"| 10% sample passages | {st['vendor']} | {st['adopter']} | {st['vendor'] / len(sample):.1%} |")
    L += ["", f"Filers with no SIC in EDGAR (counted as adopter): {n['no_sic']} of {len(ciks)}.", ""]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(L))
    print("\n".join(L))


if __name__ == "__main__":
    main()
