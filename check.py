from playwright.sync_api import sync_playwright

URL = "https://www.sharkvalleytramtours.com/"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)

    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    print("Homepage loaded")

    # Click Buy Tickets
    page.get_by_text("Buy Tickets", exact=True).click(timeout=15000)

    print("Clicked Buy Tickets")

    page.wait_for_timeout(10000)

    print("URL:")
    print(page.url)

    text = page.locator("body").inner_text()

    print(text[:3000])

    browser.close()
