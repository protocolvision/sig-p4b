#!/usr/bin/env bash
# Download the session sign-up list as CSV (name, email, affiliation, signed_up, source, unsubscribe_url).
# Needs the export secret at ~/.config/sig-p4b/export_secret (never commit it).
set -euo pipefail
OUT=${1:-signups-$(date +%Y-%m-%d).csv}
curl -sf https://sig-p4b-signup.rafaeldf2.workers.dev/export.csv \
  -H "X-Export-Secret: $(cat ~/.config/sig-p4b/export_secret)" -o "$OUT"
echo "$(($(wc -l < "$OUT") - 1)) sign-ups -> $OUT"
