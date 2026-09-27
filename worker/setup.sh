#!/usr/bin/env bash
# Stand up the sign-up Worker on YOUR Cloudflare account (for a new maintainer).
#
#   cd worker && ./setup.sh
#
# What it does, in order:
#   1. checks you're logged in to Cloudflare (npx wrangler login)
#   2. creates a KV namespace and writes its id into wrangler.jsonc
#   3. generates an export secret in ~/.config/sig-p4b/export_secret and uploads it
#   4. deploys the Worker and writes its URL into ../config.json
# Afterwards: rebuild and deploy the site (../deploy.sh) so the form posts to the new Worker,
# and optionally move the member list over with import.py (see README.md).
set -euo pipefail
cd "$(dirname "$0")"

echo "1/4 Cloudflare login"
if ! npx wrangler whoami >/dev/null 2>&1; then npx wrangler login; fi
npx wrangler whoami | grep -E "email|Account" | head -3

echo "2/4 KV namespace"
KV_JSON=$(npx wrangler kv namespace create sig-p4b-signups 2>&1)
KV_ID=$(echo "$KV_JSON" | grep -oE '"id": *"[0-9a-f]{32}"' | grep -oE '[0-9a-f]{32}' | head -1)
[ -n "$KV_ID" ] || { echo "Could not read the new namespace id:"; echo "$KV_JSON"; exit 1; }
python3 - "$KV_ID" <<'PY'
import re, sys
p = "wrangler.jsonc"; s = open(p).read()
s = re.sub(r'("binding": "SIGNUPS", "id": ")[0-9a-f]{32}(")', r'\g<1>' + sys.argv[1] + r'\2', s)
open(p, "w").write(s)
PY
echo "   SIGNUPS -> $KV_ID"

echo "3/4 Export secret"
mkdir -p ~/.config/sig-p4b && chmod 700 ~/.config/sig-p4b
[ -f ~/.config/sig-p4b/export_secret ] || openssl rand -hex 24 > ~/.config/sig-p4b/export_secret
chmod 600 ~/.config/sig-p4b/export_secret
npx wrangler secret put EXPORT_SECRET < ~/.config/sig-p4b/export_secret

echo "4/4 Deploy"
OUT=$(npx wrangler deploy 2>&1); echo "$OUT" | tail -3
URL=$(echo "$OUT" | grep -oE 'https://[a-z0-9.-]+\.workers\.dev' | head -1)
[ -n "$URL" ] || { echo "Deployed, but could not read the workers.dev URL. Put it in ../config.json by hand."; exit 0; }
python3 - "$URL" <<'PY'
import json, sys
p = "../config.json"; c = json.load(open(p)); c["signup_worker"] = sys.argv[1]
open(p, "w").write(json.dumps(c, indent=2) + "\n")
PY
echo
echo "Done. Worker: $URL"
echo "Next: (cd .. && ./deploy.sh) to point the site at it, then commit wrangler.jsonc and config.json."
echo "If the site lives somewhere new, update SITE and ALLOWED_ORIGINS in wrangler.jsonc and redeploy."
