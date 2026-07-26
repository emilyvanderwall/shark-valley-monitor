from playwright.sync_api import sync_playwright
import time

URL = "https://www.sharkvalleytramtours.com/event-calendar/"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    def log_response(response):
        url = response.url

        if "ajax" in url.lower() or "calendar" in url.lower() or "event" in url.lower():
            print("\nPOSSIBLE EVENT REQUEST:")
            print(url)

            try:
                text = response.text()
                print(text[:1000])
            except:
                pass

    page.on("response", log_response)

    print("Opening calendar...")
    page.goto(URL, wait_until="networkidle")

    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    print("Calendar loaded")

    # Change to November 2026
    selects = page.locator("select")

    selects.nth(0).select_option("2026")
    time.sleep(2)

    selects.nth(1).select_option("November")
    time.sleep(5)

    print("Finished waiting for calendar data")

    browser.close()
