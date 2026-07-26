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

    print("Calendar loaded")

    page.wait_for_timeout(5000)

    print("\nFRAMES:")
    for i, frame in enumerate(page.frames):
        print(i, frame.url)

        try:
            text = frame.locator("body").inner_text(timeout=5000)

            if "2:00" in text or "Tram Tour" in text:
                print("\nFOUND CALENDAR IN FRAME", i)
                print(text[:2000])

        except:
            pass

    browser.close()
