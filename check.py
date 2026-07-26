from playwright.sync_api import sync_playwright
import os
import requests
import time

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")


def send_discord(message):
    if DISCORD_WEBHOOK:
        requests.post(
            DISCORD_WEBHOOK,
            json={"content": message}
        )


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(
        "https://www.sharkvalleytramtours.com/",
        wait_until="networkidle",
        timeout=60000
    )

    # Close popup
    try:
        page.locator(".pum-close").click(timeout=5000)
        print("Closed popup")
    except:
        pass

    page.wait_for_timeout(5000)

    print("Calendar loaded")

    # Move to November 2026
    for i in range(12):

        body = page.locator("body").inner_text()

        if "November 2026" in body:
            print("Found November 2026")
            break

        print("Moving forward one month")

        # Use JS click on the calendar next arrow
        clicked = page.evaluate("""
        () => {
            let arrows = document.querySelectorAll('.fc-text-arrow');
            if (arrows.length > 1) {
                arrows[1].click();
                return true;
            }

            let buttons = document.querySelectorAll('button');
            for (let b of buttons) {
                if (b.innerText.includes('›')) {
                    b.click();
                    return true;
                }
            }

            return false;
        }
        """)

        if not clicked:
            print("Could not find next month button")
            break

        page.wait_for_timeout(2000)


    print("Searching events")

    events = page.locator(".fc-event")

    print("Event count:", events.count())

    found = False

    for i in range(events.count()):

        event = events.nth(i)

        text = event.inner_text()

        if "2:00PM Tram Tour" in text:

            print("----------------")
            print(text)

            # print HTML so we can see where the date lives
            html = event.evaluate("(e)=>e.outerHTML")

            print(html[:500])

            if (
                "Sold Out" not in text
                and "November 7" in text
            ):
                found = True

                msg = (
                    "🚨 Shark Valley Tram Tour Available!\n"
                    "November 7, 2026 at 2:00 PM\n\n"
                    + text
                )

                print(msg)
                send_discord(msg)
                break


    if not found:
        print("November 7 2 PM tour still unavailable")

    browser.close()
