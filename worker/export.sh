#!/usr/bin/env bash
# Download the session sign-up list as CSV
# (name, email, affiliation, website, github, discord, role, signed_up, source, updated, unsubscribe_url).
# Needs the export secret at ~/.config/sig-p4b/export_secret (never commit it).
set -euo pipefail
cd "$(dirname "$0")/.."
WORKER=$(python3 -c "import json;print(json.load(open('config.json'))['signup_worker'].rstrip('/'))")
OUT=${1:-signups-$(date +%Y-%m-%d).csv}
curl -sf "$WORKER/export.csv" -H "X-Export-Secret: $(cat ~/.config/sig-p4b/export_secret)" -o "$OUT"
echo "$(($(wc -l < "$OUT") - 1)) sign-ups -> $OUT"
