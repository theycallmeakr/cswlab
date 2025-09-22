"""
Topic 12 — datetime, time, and time zones (basic, no tzdb deps)
"""

from datetime import datetime, timedelta, timezone

now_utc = datetime.now(timezone.utc)
ist = timezone(timedelta(hours=5, minutes=30))
now_ist = now_utc.astimezone(ist)
print("UTC:", now_utc.isoformat())
print("IST:", now_ist.isoformat())

# Mini-exercise: print the date 100 days from today
print("100 days later:", (now_ist + timedelta(days=100)).date())
