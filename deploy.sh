#!/usr/bin/env bash
# hype branch: a local parody, never published
echo "This is the local hype copy; it is never deployed." >&2; exit 1
# Publish the site to here.now and mount it at npc.here.now/protocolvision.
set -euo pipefail
cd "$(dirname "$0")"
SLUG_FILE=.herenow-slug
PUBLISH=${HERENOW_PUBLISH:-$HOME/.claude/skills/here-now/scripts/publish.sh}
# Build everything from source, and refuse to publish a non-conformant blyg.
python3 tools/build_schedule.py
python3 tools/build_site.py
python3 tools/build_blyg.py
python3 tools/blyg_check.py
OUT=$(mktemp -d)
rsync -a --exclude '.git' --exclude '.herenow*' --exclude 'README.md' --exclude 'CLAUDE.md' --exclude 'deploy.sh' --exclude 'tools' --exclude 'worker' --exclude 'sources' --exclude 'drafts' --exclude 'src' --exclude 'blyg-src' --exclude '.github' ./ "$OUT/"
# Bust the CDN/browser cache for the stylesheet on every deploy.
V=$(date +%s)
find "$OUT" -name '*.html' -exec perl -pi -e "s|style\.css\"|style.css?v=$V\"|; s|site\.js\"|site.js?v=$V\"|" {} +
if [[ -f $SLUG_FILE ]]; then
  "$PUBLISH" "$OUT" --slug "$(cat $SLUG_FILE)" --client claude-code
else
  URL=$("$PUBLISH" "$OUT" --client claude-code | tail -1)
  SLUG=$(echo "$URL" | sed -E 's#https://([^.]+)\.here\.now/?#\1#')
  echo "$SLUG" > $SLUG_FILE
  curl -sS https://here.now/api/v1/links -H "Authorization: Bearer $(cat ~/.herenow/credentials)" \
    -H "Content-Type: application/json" -d "{\"location\":\"protocolvision\",\"slug\":\"$SLUG\"}"
  echo
fi
echo "Live: https://npc.here.now/protocolvision/"
