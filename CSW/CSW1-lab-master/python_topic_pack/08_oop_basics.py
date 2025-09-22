"""
Topic 08 — OOP Basics
Classes, __init__, methods, classmethod, staticmethod, __repr__.
"""

class Student:
    def __init__(self, name, target_exam):
        self.name = name
        self.target_exam = target_exam
        self._xp = 0

    def study(self, hours):
        self._xp += hours * 10
        return self

    def level(self):
        return "Pro" if self._xp >= 200 else "Grind-mode"

    def __repr__(self):
        return f"Student(name={self.name!r}, exam={self.target_exam!r}, xp={self._xp})"

    @classmethod
    def from_dict(cls, d): return cls(d['name'], d['exam'])
    @staticmethod
    def motivate(): return "Consistency > motivation."

boss = Student("Boss", "CLAT").study(8)
print(boss, boss.level(), Student.motivate())
