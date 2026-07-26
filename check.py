import os
import requests
from playwright.sync_api import sync_playwright

WEBHOOK = os.environ["DISCORD_WEBHOOK"]

URL = "https://www.sharkvalleytramtours.com/event-calendar/"

def send_alert(message):
    requests.post(
        WEBHOOK,
        json={"content": message},
        timeout=30
    )

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        URL,
        wait_until="networkidle",
        timeout=60000
    )

    # Allow calendar widgets to load
    page.wait_for_timeout(8000)

    page_text = page.locator("body").inner_text()

    browser.close()


print("Page loaded")
print(page_text[:3000])


# Search for November 7 + 2 PM
date_found = "November 7" in page_text
time_found = "2:00" in page_text or "2:00 PM" in page_text

sold_out = (
    "Sold Out" in page_text
    or "Sold out" in page_text
    or "sold out" in page_text
)


if date_found and time_found:
    if not sold_out:
        send_alert(
            "🚨 Shark Valley Tram Tour may have opened!\n\n"
            "November 7 at 2:00 PM\n"
            + URL
        )
        print("ALERT SENT")
    else:
        print("November 7 2:00 PM still sold out")
else:
    print("Could not find target date/time")
