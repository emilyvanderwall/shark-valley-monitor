from playwright.sync_api import sync_playwright
import os
import requests

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

    # Navigate to November 2026
    for i in range(12):

        body = page.locator("body").inner_text()

        if "November 2026" in body:
            print("Found November 2026")
            break

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
            browser.close()
            exit()

        page.wait_for_timeout(2000)

    else:
        print("Could not reach November 2026")
        browser.close()
        exit()


    print("Checking November 7, 2026 2 PM Tram Tour")

    events = page.locator(".fc-event")

    found = False

    for i in range(events.count()):

        event = events.nth(i)

        text = event.inner_text()

        if "2:00PM Tram Tour" in text:

            print(text)

            if "Sold Out" not in text:

                found = True

                message = (
                    "🚨 Shark Valley Tram Tour Available!\n\n"
                    "Date: November 7, 2026\n"
                    "Time: 2:00 PM Tram Tour\n\n"
                    f"{text}"
                )

                print(message)
                send_discord(message)

                break


    if not found:
        print("November 7, 2026 2 PM Tram Tour still unavailable")

    browser.close()
