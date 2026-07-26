Traceback (most recent call last):
  File "/home/runner/work/shark-valley-monitor/shark-valley-monitor/check.py", line 43, in <module>
Closed popup
    links.nth(i).click()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/playwright/sync_api/_generated.py", line 17672, in click
Homepage loaded
Ticket links found: 3
Clicking visible ticket link
    self._sync(
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/playwright/_impl/_sync_base.py", line 115, in _sync
    return task.result()
           ^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/playwright/_impl/_locator.py", line 163, in click
    return await self._frame._click(self._selector, strict=True, **params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/playwright/_impl/_frame.py", line 591, in _click
    await self._channel.send("click", self._timeout, locals_to_params(locals()))
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/playwright/_impl/_connection.py", line 69, in send
    return await self._connection.wrap_api_call(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/site-packages/playwright/_impl/_connection.py", line 563, in wrap_api_call
    raise rewrite_error(error, f"{parsed_st['apiName']}: {error}") from None
playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.
Call log:
  - waiting for locator("a[href=\"/event-calendar/\"]").nth(1)
    - locator resolved to <a class="icon-tickets" href="/event-calendar/">Buy Tickets</a>
  - attempting click action
    2 × waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <div role="dialog" id="pum-147007" aria-modal="true" class="pum pum-overlay pum-theme-146997 pum-theme-default-theme popmake-overlay auto_open click_open pum-active" data-popmake="{"id":147007,"slug":"alert-popup","theme_id":146997,"cookies":[{"event":"on_popup_close","settings":{"name":"pum-147007","time":"1 month","session":false,"path":"1","key":""}}],"triggers":[{"type":"auto_open","settings":{"delay":500,"cookie_name":["pum-147007"]}},{"type":"click_open","settings":{"extra_selectors":"","cook…>…</div> intercepts pointer events
    - retrying click action
    - waiting 20ms
    2 × waiting for element to be visible, enabled and stable
      - element is visible, enabled and stable
      - scrolling into view if needed
      - done scrolling
      - <div role="dialog" id="pum-147007" aria-modal="true" class="pum pum-overlay pum-theme-146997 pum-theme-default-theme popmake-overlay auto_open click_open pum-active" data-popmake="{"id":147007,"slug":"alert-popup","theme_id":146997,"cookies":[{"event":"on_popup_close","settings":{"name":"pum-147007","time":"1 month","session":false,"path":"1","key":""}}],"triggers":[{"type":"auto_open","settings":{"delay":500,"cookie_name":["pum-147007"]}},{"type":"click_open","settings":{"extra_selectors":"","cook…>…</div> intercepts pointer events
    - retrying click action
      - waiting 100ms
    58 × waiting for element to be visible, enabled and stable
       - element is visible, enabled and stable
       - scrolling into view if needed
       - done scrolling
       - <div role="dialog" id="pum-147007" aria-modal="true" class="pum pum-overlay pum-theme-146997 pum-theme-default-theme popmake-overlay auto_open click_open pum-active" data-popmake="{"id":147007,"slug":"alert-popup","theme_id":146997,"cookies":[{"event":"on_popup_close","settings":{"name":"pum-147007","time":"1 month","session":false,"path":"1","key":""}}],"triggers":[{"type":"auto_open","settings":{"delay":500,"cookie_name":["pum-147007"]}},{"type":"click_open","settings":{"extra_selectors":"","cook…>…</div> intercepts pointer events
     - retrying click action
       - waiting 500ms

Error: Process completed with exit code 1.
