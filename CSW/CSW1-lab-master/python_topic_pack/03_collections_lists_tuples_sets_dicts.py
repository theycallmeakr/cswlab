"""
Topic 03 — Collections: list, tuple, set, dict
Mutability basics, common methods, iteration.
"""

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[1] = "blueberry"
print(fruits)

coords = (28.6139, 77.2090)  # tuple (immutable)
seen = {"apple", "banana", "apple"}  # duplicates vanish
print(coords, seen)

student = {"name": "Boss", "exam": "CLAT", "year": 2025}
student["score"] = 99
print(student)

# Iterating
for k, v in student.items():
    print(k, "->", v)

# Mini-exercise: invert a dict {k:v} -> {v:k}
def invert(d: dict) -> dict:
    return {v:k for k, v in d.items()}

assert invert({"a":1,"b":2}) == {1:"a", 2:"b"}
print("invert ✅")
