"""
Topic 07 — Iterators & Context Managers
__iter__, __next__, contextlib.contextmanager
"""

class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n + 1

for i in Countdown(3):
    print(i)

from contextlib import contextmanager
@contextmanager
def suppress(exc):
    try:
        yield
    except exc:
        print(f"Suppressed {exc.__name__}")

with suppress(ZeroDivisionError):
    1/0
