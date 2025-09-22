"""
Topic 11 — JSON, CSV, and Pickle
"""

import json, csv, pickle, io

data = {"name":"Boss","score":100}
s = json.dumps(data)
print("json:", s)
print(json.loads(s))

csv_buf = io.StringIO()
writer = csv.DictWriter(csv_buf, fieldnames=["name","score"])
writer.writeheader(); writer.writerow(data)
print("csv:\n", csv_buf.getvalue())

blob = pickle.dumps(data)
print("pickle bytes length:", len(blob))
print(pickle.loads(blob))
