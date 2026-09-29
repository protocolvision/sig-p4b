#!/usr/bin/env bash
# Build this hype copy and export it into the main site as hype/ (served at npc.here.now/protocolvision/hype/).
# The main repo's ./deploy.sh then publishes it. Blyg, llms.txt and the calendar stay on the main site only.
set -euo pipefail
cd "$(dirname "$0")/.."
DEST=${1:-../sig-p4b/hype}
python3 tools/build_schedule.py >/dev/null
python3 tools/build_site.py >/dev/null
rsync -a --delete --exclude '.git' --exclude '.herenow*' --exclude 'README.md' --exclude 'CLAUDE.md' --exclude 'deploy.sh' \
  --exclude 'tools' --exclude 'worker' --exclude 'sources' --exclude 'drafts' --exclude 'src' --exclude 'blyg-src' --exclude '.github' \
  --exclude 'blyg' --exclude 'llms.txt' --exclude 'sig-p4b.ics' --exclude 'config.json' ./ "$DEST/"
# hype/ sits one level deeper, so point blyg and llms.txt links at the main site's copies
find "$DEST" -name '*.html' -exec perl -pi -e 's#href="((?:\.\./)*)(blyg/|llms\.txt)#href="$1../$2#g' {} +
echo "Exported to $DEST"
