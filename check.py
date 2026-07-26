from playwright.sync_api import sync_playwright
import time
import json

URL = "https://www.sharkvalleytramtours.com/event-calendar/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Opening calendar directly...")
    page.goto(URL, wait_until="networkidle")

    # Close popup
    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    print("Calendar loaded")

    # Select November 2026
    selects = page.locator("select")

    selects.nth(0).select_option("2026")
    time.sleep(2)

    selects.nth(1).select_option("November")
    time.sleep(5)

    print("Searching page scripts for event data...")

    scripts = page.locator("script")

    found = False

    for i in range(scripts.count()):
        txt = scripts.nth(i).inner_text()

        if "Tram Tour" in txt or "events" in txt:
            print("\nFOUND SCRIPT", i)
            print(txt[:2000])

            if "November" in txt or "2026" in txt:
                found = True
                break

    if not found:
        print("No event script found")

    browser.close()
