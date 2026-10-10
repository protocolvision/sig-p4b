#!/usr/bin/env bash
# Check that this machine can run the end-to-end rerun (RERUN.md, phase 0).
# Usage: bash drafts/research/who-owns-the-rules/loop-tools/check_setup.sh
set -u
cd "$(dirname "$0")/.." || exit 1
ok=1
need() { if command -v "$1" >/dev/null 2>&1; then echo "ok       $1"; else echo "MISSING  $1  ($2)"; ok=0; fi; }
want() { if command -v "$1" >/dev/null 2>&1; then echo "ok       $1"; else echo "optional $1  ($2)"; fi; }
need python3 "https://www.python.org/downloads/"
need yt-dlp "pip install yt-dlp  or  brew install yt-dlp"
need pdftotext "brew install poppler  or  apt install poppler-utils"
need claude "https://code.claude.com/docs (Claude Code CLI)"
want whisper "pip install openai-whisper, for podcasts with no transcript"
for u in https://www.finra.org https://web.archive.org https://www.youtube.com https://eur-lex.europa.eu; do
  code=$(curl -s -o /dev/null -m 15 -w "%{http_code}" "$u")
  if [ "$code" = "000" ]; then echo "NO NET   $u"; ok=0; else echo "ok       $u ($code)"; fi
done
python3 loop-tools/build_manifest.py
if [ "$ok" = 1 ]; then echo "Ready. Start Claude Code with the prompt in rerun-prompt.md."; else echo "Fix the items above first."; exit 1; fi
