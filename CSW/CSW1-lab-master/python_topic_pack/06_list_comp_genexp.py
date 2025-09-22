"""
Topic 06 — Comprehensions & Generator Expressions
"""

nums = list(range(10))
squares = [n*n for n in nums if n % 2 == 0]
print(squares)

# generator: lazy
gen = (n*n for n in range(3))
for x in gen:
    print("gen:", x)

# Mini-exercise: flatten a 2D list using a comprehension
matrix = [[1,2],[3,4],[5,6]]
flat = [x for row in matrix for x in row]
assert flat == [1,2,3,4,5,6]
print("flatten ✅")
