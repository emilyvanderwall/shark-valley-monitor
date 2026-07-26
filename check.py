from playwright.sync_api import sync_playwright
import requests
import os

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

TARGET_DATE = "November 7"
TARGET_TIME = "2:00PM Tram Tour"


def send_alert(message):
    if WEBHOOK:
        requests.post(WEBHOOK, json={"content": message})


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
        page.keyboard.press("Escape")
        print("Closed popup")
    except:
        pass

    print("Homepage loaded")

    # Find visible ticket button
    links = page.locator('a[href="/event-calendar/"]')

    print("Ticket links found:", links.count())

    for i in range(links.count()):
        if links.nth(i).is_visible():
            print("Clicking visible ticket link")
            links.nth(i).click()
            break

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(5000)

    print("Calendar loaded")

    # Select November 2026
    try:
        page.locator("select").evaluate_all("""
        els => els.map(e => ({
            value:e.value,
            options:[...e.options].map(o=>o.text)
        }))
        """)
    except:
        pass

    # Set month/year using dropdowns
    selects = page.locator("select")

    for i in range(selects.count()):
        options = selects.nth(i).locator("option").all_inner_texts()

        if "2026" in options:
            selects.nth(i).select_option(label="2026")

        if "November" in options:
            selects.nth(i).select_option(label="November")

    page.wait_for_timeout(5000)


    # Get calendar text
    text = page.locator("body").inner_text()

    print("Searching for November 7 2PM")


    # Find all 2PM tours around November 7
    if TARGET_TIME in text:

        index = text.find(TARGET_TIME)

        nearby = text[index-200:index+200]

        print("FOUND:")
        print(nearby)

        if "November 7" in nearby or "7" in nearby:
            if "Sold Out (0)" not in nearby:
                msg = (
                    "🦈 Shark Valley Tram Tour Available!\n"
                    "November 7, 2026\n"
                    "2:00 PM Tram Tour"
                )

                print(msg)
                send_alert(msg)

            else:
                print("November 7 2PM sold out")

    else:
        print("No 2PM tours found")


    browser.close()
