from playwright.sync_api import sync_playwright
import os
import requests
import re

TARGET_DATE = "2026-11-07"
TARGET_TIME = "2:00PM Tram Tour"

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def send_discord(message):
    if DISCORD_WEBHOOK:
        requests.post(
            DISCORD_WEBHOOK,
            json={"content": message}
        )

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(
        "https://www.sharkvalleytramtours.com/",
        wait_until="networkidle",
        timeout=60000
    )

    # Close popup if present
    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    # Open calendar if needed
    try:
        page.get_by_text("Tram Tours").first.click(timeout=5000)
    except:
        pass

    page.wait_for_timeout(5000)

    print("Calendar loaded")

    # Navigate calendar to November 2026
    while True:
        month = page.locator(".fc-center h2").inner_text()

        print("Current month:", month)

        if "November 2026" in month:
            break

        page.locator(".fc-next-button").click()
        page.wait_for_timeout(1000)

    print("November 2026 found")

    # Grab all calendar events
    events = page.locator(".fc-event")

    found = False

    print("Checking events...")

    for i in range(events.count()):
        event = events.nth(i)

        text = event.inner_text()

        # Get date from FullCalendar attributes
        attrs = [
            event.get_attribute("data-date"),
            event.get_attribute("data-start"),
            event.get_attribute("href")
        ]

        date_string = " ".join(
            [x for x in attrs if x]
        )

        print("----------------")
        print(text)
        print("ATTR:", date_string)

        if (
            "2:00PM Tram Tour" in text
            and "2026-11-07" in date_string
            and "Sold Out" not in text
        ):
            found = True

            message = (
                "🚨 Shark Valley Tram Tour Available!\n\n"
                "Date: November 7, 2026\n"
                "Time: 2:00 PM\n\n"
                f"{text}"
            )

            print(message)
            send_discord(message)

            break

    if not found:
        print("November 7 2026 2 PM tour still unavailable")

    browser.close()
