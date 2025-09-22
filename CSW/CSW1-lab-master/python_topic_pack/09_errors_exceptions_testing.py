"""
Topic 09 — Errors, Exceptions, and Basic Testing
try/except/else/finally, raising, asserts, doctest.
"""

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero")
    return a / b

try:
    divide(4, 0)
except ValueError as e:
    print("Caught:", e)

def add(a, b):
    """Add two numbers.
    >>> add(2, 3)
    5
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    assert add(2,3) == 5
    print("doctest/assert ✅")
