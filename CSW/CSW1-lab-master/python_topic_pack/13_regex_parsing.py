"""
Topic 13 — Regular Expressions
findall, search, groups, named groups.
"""

import re
text = "Emails: a@x.com, b.y@z.co.in — Phone: +91-98765-43210"
emails = re.findall(r"[\w.]+@[\w.]+", text)
print("emails:", emails)

m = re.search(r"\+91-(?P<first>\d{5})-(?P<second>\d{5})", text)
print("phone groups:", m.groupdict() if m else None)
