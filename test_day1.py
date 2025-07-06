import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    # Expect a title with 'Playwright'
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    # Click link "get started"
    page.get_by_role("link", name = "Get started").click()
    # Expect page to have heading "Installation"
    expect(page.get_by_role("heading", name = "Installation")).to_be_visible() 
