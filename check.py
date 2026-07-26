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

    # Look for anything containing 2:00PM
    matches = page.locator("text=2:00PM")

    print("2PM matches:", matches.count())

    for i in range(matches.count()):

        el = matches.nth(i)

        print("\n--- MATCH", i, "---")
        print(el.inner_text())

        try:
            print("TAG:", el.evaluate("(e)=>e.tagName"))
            print("CLASS:", el.get_attribute("class"))
            print("HTML:")
            print(el.evaluate("(e)=>e.outerHTML")[:1000])
        except Exception as e:
            print(e)


    browser.close()
