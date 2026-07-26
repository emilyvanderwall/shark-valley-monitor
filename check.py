from playwright.sync_api import sync_playwright
import os
import requests

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

URL = "https://www.sharkvalleytramtours.com/"

TARGET_DATE = "2026-11-07"
TARGET_TIME = "2:00PM"


def send_discord(message):
    if WEBHOOK:
        requests.post(
            WEBHOOK,
            json={"content": message},
            timeout=10
        )


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)

    # Close popup if present
    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    print("Calendar loaded")

    # wait for calendar text
    page.wait_for_timeout(5000)

    # Extract all calendar event text
    body = page.locator("body").inner_text()

    found = False

    lines = body.splitlines()

    for i, line in enumerate(lines):

        if TARGET_TIME in line:
            block = "\n".join(lines[i:i+3])

            print(block)

            if "high" in block.lower():
                found = True
                break

    if found:
        message = (
            "🦈 Shark Valley Tram Tour Available!\n\n"
            "Date: November 7, 2026\n"
            "Time: 2:00 PM\n"
            "Availability found"
        )

        print(message)
        send_discord(message)

    else:
        print("November 7 2 PM tour not available")

    browser.close()
