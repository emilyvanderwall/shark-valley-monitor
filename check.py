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

    page.wait_for_timeout(5000)

    # The calendar opens on July 2026.
    # Click next month 4 times to reach November 2026.
    for i in range(4):
        page.locator("text=›").first.click()
        page.wait_for_timeout(2000)

    text = page.locator("body").inner_text()

    browser.close()


print("Calendar loaded")
print(text[:3000])


# Confirm we reached November
if "November 2026" in text:

    print("Found November 2026")

    # Look for November 7 and the 2 PM tour
    if "November 7" in text or "Nov 7" in text:

        print("Found November 7")

        if "2:00PM Tram Tour" in text:

            print("Found 2:00 PM tour")

            if "Availability: Sold Out (0)" in text:
                print("Still sold out")

            else:
                send_alert(
                    "🚨 Shark Valley Tram Tour OPEN!\n\n"
                    "November 7, 2026 at 2:00 PM\n\n"
                    + URL
                )

                print("ALERT SENT")

        else:
            print("2:00 PM tour not found")

    else:
        print("November 7 not found")

else:
    print("Could not move to November 2026")
