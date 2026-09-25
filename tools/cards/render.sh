#!/usr/bin/env bash
# Re-render the 1200x630 social cards into assets/cards/ (edit the .html files to change copy).
set -euo pipefail
cd "$(dirname "$0")"
C="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for k in home syllabus observations case-studies; do
  "$C" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=5000 --window-size=1200,630 --screenshot="/tmp/$k.png" "file://$PWD/$k.html" 2>/dev/null
  python3 -c "from PIL import Image; Image.open('/tmp/$k.png').convert('RGB').save('../../assets/cards/$k.jpg', quality=88, optimize=True)"
done
echo "cards -> assets/cards/"
