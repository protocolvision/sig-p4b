"""Block feature coding if coder inputs name a pattern (loop-prompts/feature-coding.md, leak check; addendum A.2).

Scans every file the coders receive (CODER_INPUTS, the same list as the prompt's Inputs section): all .md and
.csv files of instruments I1-I6 except superseded "-v1" copies, clusters/, and corpus-b/filings-*.csv.
Matches pattern and design labels only in prose: in a .csv, every cell except columns whose header contains
"title" or "occupation"; in a .md, every line, except table cells under such a header. Common occupation
names ("data scientist", "product manager", "brand manager") are not labels and are not matched.

Usage: python3 loop-tools/leak_check.py   (exit 1 and list hits if any; prints "clean" otherwise)
"""
import csv, pathlib, re, sys

RUN = pathlib.Path(__file__).resolve().parent.parent / "results" / "rerun-2026-10-10"
TERMS = re.compile(
    r"devops|\bSRE\b|site reliability|webmaster|prompt engineer|\bCISO\b|mandated officer|tool-operator"
    r"|tool operator fade|scarcity boom|boom then speciali[sz]ation|lead-industry|lead industry diffusion"
    r"|data scien(?:ce|tist) pattern|brand management pattern|product management pattern"
    r"|engineering absorption|signature", re.I)
CODER_INPUTS = [f"instruments/I{i}*.{ext}" for i in range(1, 7) for ext in ("md", "csv")] + [
    "clusters/**/*.md", "clusters/**/*.csv", "corpus-b/filings-*.csv"]
EXEMPT = re.compile(r"title|occupation", re.I)


def files():
    seen = set()
    for pat in CODER_INPUTS:
        for p in sorted(RUN.glob(pat)):
            if p.is_file() and not re.search(r"-v1\.(md|csv)$", p.name) and p not in seen:
                seen.add(p)
                yield p


def scan_csv(p):
    with open(p, newline="", errors="ignore") as fh:
        rows = csv.reader(fh)
        header = next(rows, [])
        keep = [i for i, h in enumerate(header) if not EXEMPT.search(h)]
        for i in keep:  # header cells are prose too, except exempt ones
            if TERMS.search(header[i]):
                yield 1, TERMS.search(header[i]).group(0)
        for n, row in enumerate(rows, 2):
            for i in keep:
                m = i < len(row) and TERMS.search(row[i])
                if m:
                    yield n, m.group(0)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def scan_md(p):
    lines = p.read_text(errors="ignore").splitlines()
    header = None
    for n, line in enumerate(lines, 1):
        if line.lstrip().startswith("|"):
            nxt = lines[n] if n < len(lines) else ""
            if header is None and re.match(r"^\s*\|?\s*:?-{3,}", nxt):
                header = cells(line)
            if re.match(r"^\s*\|?\s*:?-{3,}", line):
                continue
            exempt = {i for i, h in enumerate(header or []) if EXEMPT.search(h)}
            text = " | ".join(c for i, c in enumerate(cells(line)) if i not in exempt)
        else:
            header, text = None, line
        m = TERMS.search(text)
        if m:
            yield n, m.group(0)


hits = []
for p in files():
    for n, term in (scan_csv(p) if p.suffix == ".csv" else scan_md(p)):
        hits.append(f"{p.relative_to(RUN)}:{n}: {term}")
print("\n".join(hits) or "clean")
sys.exit(1 if hits else 0)
