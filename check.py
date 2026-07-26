from playwright.sync_api import sync_playwright
import os
import requests

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

URL = "https://www.sharkvalleytramtours.com/"


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

    # Close popup
    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    print("Calendar loaded")

    page.wait_for_timeout(5000)

    # Find all calendar event elements
    events = page.locator(".fc-event")

    print("Events found:", events.count())

    found = False

    for i in range(events.count()):

        event = events.nth(i)

        text = event.inner_text()

        date = event.get_attribute("data-date")

        print("DATE:", date)
        print(text)

        if (
            date == "2026-11-07"
            and "2:00PM" in text
            and "Sold Out" not in text
        ):
            found = True

    if found:

        msg = (
            "🦈 Shark Valley Tram Tour Available!\n\n"
            "November 7, 2026\n"
            "2:00 PM Tram Tour"
        )

        print(msg)
        send_discord(msg)

    else:
        print("November 7 2 PM tour not available")

    browser.close()
