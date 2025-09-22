"""
Topic 01 — Numbers, Booleans, and Operators
Covers ints, floats, round(), //, %, **, comparison, truthiness.
"""

a, b = 10, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Floating point gotcha
x = 0.1 + 0.2
print("0.1 + 0.2 =", x, "≈", round(x, 10))

# Booleans & comparisons
is_adult = (18 >= 18)
print(is_adult, a > b, a == b, a != b)

# Truthiness
for value in [0, 1, "", "hi", [], [1], None]:
    print(value, "is truthy?" , bool(value))

# Mini-exercise: write a function is_even(n) returning True/False.
def is_even(n: int) -> bool:
    return n % 2 == 0

assert is_even(4) is True and is_even(5) is False
print("is_even ✅")
