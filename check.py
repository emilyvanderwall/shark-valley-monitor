from playwright.sync_api import sync_playwright
import time

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
        print("No popup")

    print("Calendar loaded")

    # Select year and month
    selects = page.locator("select")

    print("Dropdown count:", selects.count())

    for i in range(selects.count()):
        print(i, selects.nth(i).locator("option").all_inner_texts()[:5])

    selects.nth(0).select_option("2026")
    time.sleep(2)

    selects.nth(1).select_option("November")
    time.sleep(3)

    print("Looking for November 7 events...")

    days = page.locator(".fc-day")

    found_day = False
    found_2pm = False

    for i in range(days.count()):

        cell = days.nth(i)

        try:
            date_text = cell.locator(".fc-day-number").inner_text(timeout=1000)
        except:
            continue

        if date_text.strip() == "7":

            found_day = True

            print("\nFOUND NOVEMBER 7 CELL")

            events = cell.locator(".fc-event")

            print("Events in cell:", events.count())

            for j in range(events.count()):

                event_text = events.nth(j).inner_text()

                print("---")
                print(event_text)

                if "2:00PM Tram Tour" in event_text:
                    found_2pm = True

                    if "Sold Out" in event_text:
                        print("RESULT: November 7 2PM SOLD OUT")

                    elif "Availability: high" in event_text or "Availability: medium" in event_text:
                        print("RESULT: November 7 2PM AVAILABLE")

                    else:
                        print("RESULT:")
                        print(event_text)

            break

    if not found_day:
        print("Could not find November 7")

    if found_day and not found_2pm:
        print("November 7 2PM tour not found")

    browser.close()
