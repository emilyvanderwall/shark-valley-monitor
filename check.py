    print("Looking for November 7 events...")

    days = page.locator(".fc-day")

    found = False

    for i in range(days.count()):
        cell = days.nth(i)

        date_text = cell.locator(".fc-day-number").inner_text(timeout=2000)

        if date_text.strip() == "7":

            print("\nFOUND NOVEMBER 7 CELL")

            events = cell.locator(".fc-event")

            print("Events in cell:", events.count())

            for j in range(events.count()):
                event_text = events.nth(j).inner_text()
                print("---")
                print(event_text)

                if "2:00PM Tram Tour" in event_text:
                    found = True

                    if "Sold Out" in event_text:
                        print("RESULT: November 7 2PM SOLD OUT")
                    elif "high" in event_text or "medium" in event_text:
                        print("RESULT: November 7 2PM AVAILABLE")
                    else:
                        print("RESULT:")
                        print(event_text)

            break

    if not found:
        print("November 7 2PM tour not available")
