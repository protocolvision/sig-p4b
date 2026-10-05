#!/usr/bin/env bash
# Build the site, publish it to Cloudflare at protocolsforbusiness.com, and keep the old here.now address redirecting.
set -euo pipefail
cd "$(dirname "$0")"
SLUG_FILE=.herenow-slug
PUBLISH=${HERENOW_PUBLISH:-$HOME/.claude/skills/here-now/scripts/publish.sh}
# Build everything from source, and refuse to publish a non-conformant blyg.
python3 tools/build_schedule.py
python3 tools/build_site.py
python3 tools/build_blyg.py
python3 tools/build_sitemap.py
python3 tools/blyg_check.py
# 1) The site, built into dist/ and served by Cloudflare at protocolsforbusiness.com (site/wrangler.jsonc).
SITE=$(python3 -c "import json;print(json.load(open('config.json'))['site'])")
rm -rf dist && mkdir dist
rsync -a --exclude '.git' --exclude '.herenow*' --exclude 'README.md' --exclude 'CLAUDE.md' --exclude 'deploy.sh' --exclude 'tools' --exclude 'worker' --exclude 'site' --exclude 'dist' --exclude 'sources' --exclude 'ops' --exclude 'drafts' --exclude 'src' --exclude 'blyg-src' --exclude '.github' --exclude 'node_modules' ./ dist/
# Bust the CDN/browser cache for the stylesheet and script on every deploy.
V=$(date +%s)
find dist -name '*.html' -exec perl -pi -e "s|style\.css\"|style.css?v=$V\"|; s|site\.js\"|site.js?v=$V\"|" {} +
(cd site && npx wrangler deploy)

# 2) The old address, npc.here.now/protocolvision: every page redirects to the same page on the new
#    domain; calendar, feeds, data and Markdown files stay as they are so subscriptions keep working.
OUT=$(mktemp -d)
rsync -a --exclude '*.html' dist/ "$OUT/"
find dist -name '*.html' | while read -r f; do
  rel=${f#dist/}; path=${rel%index.html}; mkdir -p "$OUT/$(dirname "$rel")"
  printf '<!doctype html><meta charset="utf-8"><title>Moved</title>\n<meta http-equiv="refresh" content="0; url=%s%s">\n<link rel="canonical" href="%s%s">\n<p>This page moved to <a href="%s%s">%s%s</a>.</p>\n' "$SITE" "$path" "$SITE" "$path" "$SITE" "$path" "$SITE" "$path" > "$OUT/$rel"
done
# Only with a here.now key (local credentials file or HERENOW_API_KEY); without one, skip rather than
# publish anonymously.
if [[ -f $SLUG_FILE ]] && { [[ -n "${HERENOW_API_KEY:-}" ]] || [[ -f "$HOME/.herenow/credentials" ]]; }; then
  "$PUBLISH" "$OUT" --slug "$(cat $SLUG_FILE)" --client claude-code
else
  echo "No here.now key; the old address was not updated."
fi
echo "Live: $SITE (old address redirects: https://npc.here.now/protocolvision/)"
