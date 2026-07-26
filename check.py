from playwright.sync_api import sync_playwright
import os
import requests

TARGET_DATE = "November 7, 2026"
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

    # Close popup
    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    page.wait_for_timeout(3000)

    print("Calendar loaded")

    # Navigate until November 2026
    for i in range(12):
        body = page.locator("body").inner_text()

        if "November 2026" in body:
            print("Found November 2026")
            break

        # click the right arrow only
        page.locator(".fc-text-arrow").last.click(timeout=10000)
        page.wait_for_timeout(2000)

    else:
        print("Could not reach November 2026")
        browser.close()
        exit()


    # Find all event blocks
    events = page.locator(".fc-event")

    print("Total events:", events.count())

    found = False

    for i in range(events.count()):

        event = events.nth(i)

        text = event.inner_text()

        if TARGET_TIME in text:

            print("----------------")
            print(text)

            # Look at parent day container for date
            parent = event.locator("xpath=ancestor::*[contains(@class,'fc-day')]").first

            date = parent.get_attribute("data-date")

            print("DATE:", date)

            if (
                date == "2026-11-07"
                and "Sold Out" not in text
            ):
                found = True

                message = (
                    "🚨 Shark Valley Tram Tour Available!\n\n"
                    "November 7, 2026\n"
                    "2:00 PM Tram Tour\n\n"
                    + text
                )

                print(message)
                send_discord(message)
                break


    if not found:
        print("November 7 2 PM tour still unavailable")

    browser.close()
