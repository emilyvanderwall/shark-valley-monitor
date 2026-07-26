from playwright.sync_api import sync_playwright
import os
import requests
import re

URL = "https://www.sharkvalleytramtours.com/reservations/"

TARGET_DATE = "November 7"
TARGET_TIME = "2:00PM Tram Tour"

DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")


def send_alert(message):
    if DISCORD_WEBHOOK:
        requests.post(DISCORD_WEBHOOK, json={"content": message})


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)

    # Close popup if it appears
    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    # Wait for calendar
    page.wait_for_timeout(5000)
    print("Calendar loaded")

    # Jump directly to November 2026 if FullCalendar API exists
    page.evaluate("""
    () => {
        let calendar = document.querySelector('.fc').__fullCalendar;
        if (calendar) {
            calendar.gotoDate('2026-11-01');
        }
    }
    """)

    page.wait_for_timeout(5000)

    # Fallback: click next until November 2026 appears
    for i in range(12):
        text = page.locator("body").inner_text()

        if "November 2026" in text:
            break

        try:
            page.locator(".fc-next-button").click(timeout=3000)
        except:
            try:
                page.locator(".fc-button-next").click(timeout=3000)
            except:
                print("Could not find next month button")
                break

        page.wait_for_timeout(2000)

    text = page.locator("body").inner_text()

    if "November 2026" not in text:
        print("November 2026 not found")
        browser.close()
        exit()

    print("Found November 2026")

    # Find only 2PM events
    events = page.locator(".fc-event")

    found = False

    for i in range(events.count()):
        event = events.nth(i)
        event_text = event.inner_text()

        if "2:00PM Tram Tour" in event_text:

            print(event_text)

            # Get parent day cell
            day = event.locator("xpath=ancestor::td").get_attribute("data-date")

            print("DATE:", day)

            if day == "2026-11-07":

                if "Sold Out" not in event_text:

                    found = True
                    print("AVAILABLE: November 7 at 2 PM")

                    send_alert(
                        "🚨 Shark Valley Tram Tour available!\n"
                        "November 7, 2026 at 2:00 PM"
                    )

                else:
                    print("November 7 2 PM is sold out")

    if not found:
        print("November 7 2 PM event not available")

    browser.close()
