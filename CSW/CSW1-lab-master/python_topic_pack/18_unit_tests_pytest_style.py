"""
Topic 18 — Unit test style (without pytest dependency)
Using built-in unittest for portability.
Run: python -m unittest 18_unit_tests_pytest_style.py
"""

import unittest

def add(a, b): return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3), 5)

if __name__ == "__main__":
    unittest.main()
