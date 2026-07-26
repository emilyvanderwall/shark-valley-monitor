import requests
from datetime import datetime
import time

print("Checking Shark Valley availability...")

url = "https://www.sharkvalleytramtours.com/wp-admin/admin-ajax.php"

params = {
    "action": "qscal",
    "t": str(time.time()),
    "v": "9ff15798a708d16fde95b7e7d8aaef47",
    "start": int(datetime(2026, 11, 1).timestamp()),
    "end": int(datetime(2026, 12, 1).timestamp())
}

response = requests.get(url, params=params)

print("Status:", response.status_code)
print("Raw response:")
print(response.text[:500])

try:
    events = response.json()
except Exception:
    print("Not JSON response")
    exit()

print("Returned type:", type(events))

if isinstance(events, list):
    print("Events returned:", len(events))

    for event in events:
        if event.get("start", "").startswith("2026-11-07"):
            print("----------------------")
            print(event["title"])
            print("Time:", event["start"])
            print("Availability:", event["available"])
            print("Status:", event["avail-words"])
            print("URL:", event["url"])

else:
    print("Unexpected API response:")
    print(events)
