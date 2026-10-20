#!/usr/bin/env bash
# List pending requests to join the Feed's community, or mark one handled:
#   worker/listings.sh                 print pending requests
#   worker/listings.sh done <key>      remove a request after adding or declining it
# Needs the export secret at ~/.config/sig-p4b/export_secret. Requests hold personal data: never save them in the repo.
set -euo pipefail
cd "$(dirname "$0")/.."
WORKER=$(python3 -c "import json;print(json.load(open('config.json'))['signup_worker'].rstrip('/'))")
H="X-Export-Secret: $(cat ~/.config/sig-p4b/export_secret)"
if [ "${1:-}" = done ]; then
  curl -sf -X POST "$WORKER/listings/done?key=$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$2")" -H "$H"; echo
else
  curl -sf "$WORKER/listings.json" -H "$H" | python3 -c "
import json,sys
L=json.load(sys.stdin)
print(len(L),'pending')
for r in L: print(f\"{r['ts'][:16]}  {r['kind']:4}  {r['title'] or r['site']}  {r['site']}  feed {r['feed']}  from {r['name']}  key {r['key']}\")"
fi
