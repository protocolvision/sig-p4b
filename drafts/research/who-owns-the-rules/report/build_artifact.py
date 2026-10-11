"""Build the claude.ai artifact version: inline data/map.json, keep the artifact-only link, drop the website-only form."""
import pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
s = (HERE / "interactive-src.html").read_text()
s = re.sub(r"<!--SITE-->.*?<!--/SITE-->", "", s, flags=re.S).replace("<!--ARTIFACT-->", "").replace("<!--/ARTIFACT-->", "")
(HERE / "who-owns-the-rules-interactive.html").write_text(s.replace("/*MAP*/", (HERE / "data/map.json").read_text()))
print("wrote who-owns-the-rules-interactive.html")
