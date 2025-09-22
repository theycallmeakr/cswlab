"""
Topic 02 — Strings
Slicing, methods, immutability, join/split, f-strings.
"""

s = "Pythonista"
print(s[0], s[-1], s[2:6], s[::-1])
print(s.lower(), s.upper(), s.title(), s.replace("ista", " enjoyer"))

words = ["law", "logic", "lucidity"]
joined = ", ".join(words)
print(joined)
print(joined.split(", "))

# Mini-exercise: define slugify(title) -> 'kebab-case'
