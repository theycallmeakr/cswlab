"""
Topic 17 — SQLite intro with sqlite3
"""

import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE students(id INTEGER PRIMARY KEY, name TEXT)")
cur.executemany("INSERT INTO students(name) VALUES (?)", [("Boss",),("Aklavya",)])
conn.commit()
for row in cur.execute("SELECT * FROM students"):
    print(row)
conn.close()
