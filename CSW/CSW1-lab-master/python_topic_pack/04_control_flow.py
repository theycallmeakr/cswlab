"""
Topic 04 — Control Flow
if/elif/else, while, for, break/continue, match (3.10+).
"""

grade = 86
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
else:
    letter = "C"
print(letter)

# While loop
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print("n:", n)
    if n == 1:
        break

# match-case (requires Python 3.10+)
def vibe(x):
    match x:
        case 0:
            return "neutral"
        case 1 | 2 | 3:
            return "low-key"
        case _:
            return "max crazy"
print(vibe(3))
