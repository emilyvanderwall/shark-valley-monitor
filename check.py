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

events = response.json()

print("Events returned:", len(events))

found = False

for event in events:
    start = event.get("start", "")
    
    if start.startswith("2026-11-07"):
        print("----------------------")
        print(event["title"])
        print("Time:", start)
        print("Availability:", event["available"])
        print("Status:", event["avail-words"])
        print("URL:", event["url"])

        if event["title"] == "2:00PM Tram Tour" and event["available"] > 0:
            found = True


print("----------------------")

if found:
    print("🎉 November 7 2PM tram tour AVAILABLE!")
else:
    print("November 7 2PM tour not available")
