#!/usr/bin/env python3
"""Create a new blyg item with a permanent id.

  python3 tools/blyg_new.py fragment my-short-note [--author "Your Name"]
  python3 tools/blyg_new.py thread session-2026-11-02 [--author "Your Name"]

Writes blyg-src/{fragments|threads}/<slug>.md. Nothing is published until you commit it;
each later commit that changes the text publishes a new version.
"""
import argparse, secrets, sys
from pathlib import Path

ALPHABET = "0123456789abcdefghjkmnpqrstvwxyz"  # Crockford base32, lowercase

def new_id():
    n = int.from_bytes(secrets.token_bytes(16), "big")  # 128 random bits
    out = []
    for _ in range(26):
        out.append(ALPHABET[n & 31]); n >>= 5
    return "".join(reversed(out))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["fragment", "thread"])
    ap.add_argument("slug")
    ap.add_argument("--author", default="")
    a = ap.parse_args()
    folder = Path(__file__).resolve().parent.parent / "blyg-src" / ("fragments" if a.kind == "fragment" else "threads")
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{a.slug}.md"
    if path.exists():
        sys.exit(f"{path} already exists")
    front = [f"id: {new_id()}"] + ([f"author: {a.author}"] if a.author else [])
    body = ("Write a short note here (keep fragments under 2,000 characters).\n" if a.kind == "fragment"
            else "# Title\n\nWrite here. To quote one of this blyg's fragments, put ![[<fragment id>]] on its own line.\n")
    path.write_text("---\n" + "\n".join(front) + "\n---\n" + body)
    print(path)

if __name__ == "__main__":
    main()
