from playwright.sync_api import sync_playwright
import time

URL = "https://www.sharkvalleytramtours.com/event-calendar/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    print("Opening calendar directly...")
    page.goto(URL, wait_until="networkidle")

    # close popup
    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    print("Calendar loaded")

    # Select year 2026
    selects = page.locator("select")

    print("Dropdown count:", selects.count())

    for i in range(selects.count()):
        vals = selects.nth(i).locator("option").all_inner_texts()
        print(i, vals[:5])

    selects.nth(0).select_option("2026")
    time.sleep(2)

    # Select November
    selects.nth(1).select_option("11")
    time.sleep(3)

    print("Looking for November 7...")

    # Find day cell containing 7
    days = page.locator(".fc-day")

    found = False

    for i in range(days.count()):
        cell = days.nth(i)

        txt = cell.inner_text()

        if txt.strip().startswith("7"):

            print("FOUND DAY CELL:")
            print(txt)

            if "2:00PM Tram Tour" in txt:

                print("FOUND NOVEMBER 7 2PM!")

                if "Sold Out" in txt:
                    print("Status: SOLD OUT")
                elif "high" in txt:
                    print("Status: AVAILABLE")
                else:
                    print(txt)

                found = True
                break

    if not found:
        print("November 7 2PM tour not available")

    browser.close()
