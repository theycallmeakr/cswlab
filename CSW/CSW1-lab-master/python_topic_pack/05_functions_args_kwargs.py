"""
Topic 05 — Functions, *args, **kwargs, scope, annotations.
"""

def power(base: float, exp: float = 2, /, *, verbose: bool = False) -> float:
    """Raise base**exp. Pos-only + kw-only parameters demo."""
    val = base ** exp
    if verbose:
        print(f"{base=}, {exp=}, {val=}")
    return val

print(power(3))
print(power(3, 3, verbose=True))

# *args **kwargs
def demo(a, *args, **kwargs):
    print("a:", a, "args:", args, "kwargs:", kwargs)

demo(1, 2, 3, x=4, y=5)

# Mini-exercise: write a decorator timeit(fn) that prints runtime.
import time, functools
def timeit(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return fn(*args, **kwargs)
        finally:
            dt = (time.perf_counter() - t0)*1000
            print(f"{fn.__name__} took {dt:.2f} ms")
    return wrapper

@timeit
def slow():
    sum(i*i for i in range(100000))
slow()
