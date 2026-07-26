import requests
import re
import time
from datetime import datetime

session = requests.Session()

calendar_url = "https://www.sharkvalleytramtours.com/event-calendar/"

print("Loading calendar page...")

html = session.get(calendar_url).text

# Find the qscal ajax URL embedded in page scripts
match = re.search(
    r'admin-ajax\.php\?action=qscal[^"\']+',
    html
)

if not match:
    print("Could not find calendar API URL")
    exit()

api_path = match.group(0)

print("Found API:")
print(api_path)


# Extract v token
v_match = re.search(r'v=([^&"\']+)', api_path)

if not v_match:
    print("Could not find v token")
    exit()

v = v_match.group(1)

print("Token:", v)


params = {
    "action": "qscal",
    "t": str(time.time()),
    "v": v,
    "start": int(datetime(2026,11,1).timestamp()),
    "end": int(datetime(2026,12,1).timestamp())
}


print("Requesting events...")

response = session.get(
    "https://www.sharkvalleytramtours.com/wp-admin/admin-ajax.php",
    params=params
)

print("Response:", response.text[:200])


events = response.json()

if not isinstance(events, list):
    print("Unexpected response:")
    print(events)
    exit()


print("Events:", len(events))

found=False

for e in events:
    if e.get("start","").startswith("2026-11-07"):
        print("----------------")
        print(e["title"])
        print(e["start"])
        print("Available:", e["available"])
        print(e["avail-words"])

        if e["title"] == "2:00PM Tram Tour" and e["available"] > 0:
            found=True


if found:
    print("🎉 November 7 2PM AVAILABLE")
else:
    print("November 7 2PM not available")
