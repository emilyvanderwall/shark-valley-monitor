from playwright.sync_api import sync_playwright
import requests
import os
import re

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

TARGET_DATE = "November 7"
TARGET_TIME = "2:00PM Tram Tour"


def send_alert(message):
    if WEBHOOK:
        requests.post(WEBHOOK, json={"content": message})


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Opening calendar directly...")

    page.goto(
        "https://www.sharkvalleytramtours.com/event-calendar/",
        wait_until="networkidle",
        timeout=60000
    )

    page.wait_for_timeout(5000)

    # Close popup if present
    try:
        page.locator(".pum-close").click(timeout=3000)
        print("Closed popup")
    except:
        try:
            page.keyboard.press("Escape")
            print("Closed popup with escape")
        except:
            pass

    print("Calendar loaded")


    # Find dropdowns
    selects = page.locator("select")

    print("Dropdown count:", selects.count())

    for i in range(selects.count()):
        options = selects.nth(i).locator("option").all_inner_texts()
        print(i, options[:5], "...")

        if "2026" in options:
            print("Selecting year 2026")
            selects.nth(i).select_option(label="2026")

        if "November" in options:
            print("Selecting November")
            selects.nth(i).select_option(label="November")


    page.wait_for_timeout(5000)


    # Grab calendar text
    body = page.locator("body").inner_text()

    print("Looking for November 7...")


    # Print any area containing 2PM tours
    matches = [
        m.start()
        for m in re.finditer("2:00PM Tram Tour", body)
    ]

    print("2PM matches:", len(matches))


    found = False

    for index in matches:

        section = body[index-300:index+300]

        print("--------------------")
        print(section)

        if "Sold Out (0)" not in section:

            if "7" in section:

                found = True

                message = (
                    "🦈 Shark Valley Tram Tour Available!\n\n"
                    "Date: November 7, 2026\n"
                    "Time: 2:00 PM"
                )

                print(message)
                send_alert(message)
                break


    if not found:
        print("November 7 2PM tour not available")


    browser.close()
