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

    # Close popup
    try:
        page.locator(".pum-close").click(timeout=5000)
        page.wait_for_timeout(2000)
    except:
        pass

    # Move July -> November
    for i in range(4):
        page.locator(".fc-text-arrow").nth(1).click(timeout=10000)
        page.wait_for_timeout(3000)

    # Extract calendar event information
    events = page.locator(".fc-event")

    found = False

    for i in range(events.count()):
        event = events.nth(i).inner_text()

        if "2:00PM Tram Tour" in event:
            print(event)

            # Get date from event element
            date = events.nth(i).get_attribute("data-date")

            print("DATE:", date)

            if date == "2026-11-07":

                found = True

                if "Sold Out (0)" in event:
                    print("November 7 2 PM still sold out")
                else:
                    send_alert(
                        "🚨 Shark Valley Tram Tour OPEN!\n\n"
                        "November 7, 2026 at 2:00 PM\n\n"
                        + URL
                    )

                break

    browser.close()


if not found:
    print("November 7 2 PM event not found")
