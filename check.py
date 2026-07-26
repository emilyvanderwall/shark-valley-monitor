import os
from playwright.sync_api import sync_playwright

URL = "https://www.sharkvalleytramtours.com/event-calendar/"


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        URL,
        wait_until="networkidle",
        timeout=60000
    )

    page.wait_for_timeout(5000)

    try:
        page.locator(".pum-close").click(timeout=5000)
        page.wait_for_timeout(2000)
    except:
        pass

    for i in range(4):
        page.locator(".fc-text-arrow").nth(1).click(timeout=10000)
        page.wait_for_timeout(2000)

    events = page.locator(".fc-event")

    print("Number of events:", events.count())

    for i in range(events.count()):
        event = events.nth(i)

        if "2:00PM Tram Tour" in event.inner_text():
            print("\n--- EVENT HTML ---")
            print(event.evaluate("(el) => el.outerHTML"))
            break

    browser.close()
