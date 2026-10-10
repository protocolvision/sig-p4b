"""Block feature coding if coder inputs name a pattern (loop-prompts/feature-coding.md, leak check)."""
import pathlib, re, sys

RUN = pathlib.Path(__file__).resolve().parent.parent / "results" / "rerun-2026-10-10"
TERMS = re.compile(r"devops|\bSRE\b|site reliability|data scientist|webmaster|prompt engineer|\bCISO\b|brand manag"
                   r"|product manag|mandated officer|tool-operator|scarcity boom|lead-industry|engineering absorption"
                   r"|H-DevOps|signature", re.I)
INPUTS = ["instruments/I1*", "instruments/I2*", "instruments/I3*.md", "instruments/I4*", "instruments/I5*",
          "instruments/I6*", "clusters/*", "corpus-b/filings-*.csv"]

hits = []
for pat in INPUTS:
    for p in RUN.glob(pat):
        if p.is_file():
            for n, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
                m = TERMS.search(line)
                if m:
                    hits.append(f"{p.relative_to(RUN)}:{n}: {m.group(0)}")
print("\n".join(hits) or "clean")
sys.exit(1 if hits else 0)
