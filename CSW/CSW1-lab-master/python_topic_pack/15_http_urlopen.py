"""
Topic 15 — Simple HTTP without external deps (urllib)
Note: Works only with internet access allowed.
"""

from urllib.request import urlopen
import json

URL = "https://api.github.com/rate_limit"
try:
    with urlopen(URL, timeout=10) as r:
        payload = json.loads(r.read().decode())
        print("GitHub core remaining:", payload["resources"]["core"]["remaining"])
except Exception as e:
    print("Network call failed (sandbox?), but code is fine:", e)
