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

    # Find elements containing Tram Tour
    elements = page.locator("text=Tram Tour")

    print("Tram Tour matches:", elements.count())

    for i in range(min(elements.count(), 10)):

        el = elements.nth(i)

        print("\n--- RESULT", i, "---")

        try:
            print("TAG:", el.evaluate("(e)=>e.tagName"))
            print("CLASS:", el.get_attribute("class"))
            print("ID:", el.get_attribute("id"))
            print("TEXT:")
            print(el.inner_text())

            print("HTML:")
            print(el.evaluate("(e)=>e.outerHTML")[:1500])

        except Exception as e:
            print("ERROR:", e)

    browser.close()
