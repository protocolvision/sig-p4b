"""Build the agent controls atlas page: inline data/atlas.json into atlas-src.html at /*ATLAS*/.
Writes agent-controls-atlas.html (artifact page contract: no doctype, starts with <title>). Usage: python3 build_atlas.py"""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent
src = (HERE / "atlas-src.html").read_text(encoding="utf-8")
assert src.count("/*ATLAS*/") == 1, "placeholder /*ATLAS*/ must appear once"
(HERE / "agent-controls-atlas.html").write_text(src.replace("/*ATLAS*/", (HERE / "data/atlas.json").read_text(encoding="utf-8")), encoding="utf-8")
print("wrote agent-controls-atlas.html")
