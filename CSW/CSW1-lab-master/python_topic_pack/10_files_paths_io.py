"""
Topic 10 — Files, Paths, and I/O
with open(), text vs bytes, pathlib.
"""

from pathlib import Path
p = Path("sample.txt")
p.write_text("Hello file!\n", encoding="utf-8")
print("Read back:", p.read_text())

# Mini-exercise: append a second line and read all lines.
with p.open("a", encoding="utf-8") as f:
    f.write("Second line\n")
print(p.read_text())
