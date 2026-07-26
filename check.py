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

    page.locator("select[rel='year']").select_option("2026")
    page.wait_for_timeout(2000)

    page.locator("select[rel='month']").select_option("11")
    page.wait_for_timeout(5000)

    text = page.locator("body").inner_text()

    browser.close()


print(text[:3000])

if "November 7" in text or "Nov 7" in text:
    print("Found November 7")

    if "2:00PM Tram Tour" in text:
        if "Availability: Sold Out (0)" in text:
            print("Still sold out")
        else:
            send_alert(
                "🚨 Shark Valley Tram Tour OPEN!\n\n"
                "November 7, 2026 at 2:00 PM\n"
                + URL
            )
            print("ALERT SENT")
    else:
        print("2 PM tour not found")
else:
    print("November 7 not found")
