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

    # Find visible Buy Tickets link
    links = page.locator('a[href*="event-calendar"]')

    print("Ticket links found:", links.count())

    for i in range(links.count()):
        visible = links.nth(i).is_visible()
        print(i, "visible:", visible)

        if visible:
            print("Clicking visible ticket link")
            links.nth(i).click(timeout=15000)
            break

    page.wait_for_load_state("networkidle", timeout=60000)

    print("URL:")
    print(page.url)

    page.wait_for_timeout(5000)

    text = page.locator("body").inner_text()

    print(text[:5000])

    browser.close()
