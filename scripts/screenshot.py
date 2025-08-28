from playwright.sync_api import sync_playwright
import sys, os

script_path = sys.path[0]
parent_dir = os.path.dirname(script_path)

html_file = os.path.join(parent_dir, "index.html")
full_html_file = "file://" + html_file

with sync_playwright() as p:
    browser = p.firefox.launch()
    context = browser.new_context(
      viewport = { 'width': 2880, 'height': 1800 },
      device_scale_factor = 2,
    )
    page = context.new_page()
    page.goto(full_html_file)
    page.locator("#web_resume").screenshot(path = "screenshot.png", scale = "device")
    browser.close()

