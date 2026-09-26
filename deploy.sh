#!/usr/bin/env bash
# Publish the site to here.now and mount it at npc.here.now/protocolvision.
set -euo pipefail
cd "$(dirname "$0")"
SLUG_FILE=.herenow-slug
PUBLISH=~/.claude/skills/here-now/scripts/publish.sh
OUT=$(mktemp -d)
rsync -a --exclude '.git' --exclude '.herenow*' --exclude 'README.md' --exclude 'CLAUDE.md' --exclude 'deploy.sh' --exclude 'tools' --exclude 'worker' --exclude 'sources' --exclude 'src' ./ "$OUT/"
# Bust the CDN/browser cache for the stylesheet on every deploy.
V=$(date +%s)
find "$OUT" -name '*.html' -exec sed -i '' -e "s|style.css\"|style.css?v=$V\"|" -e "s|site.js\"|site.js?v=$V\"|" {} +
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
