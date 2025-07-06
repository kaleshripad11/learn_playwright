from playwright.sync_api import Page, expect

def test_login_to_orange_hrm(page: Page):
    # Navigate to orange hrm url
    page.goto("https://opensource-demo.orangehrmlive.com/")
    # Locate username & password field
    page.get_by_role("textbox", name = "username").fill("Admin")
    page.get_by_role("textbox", name = "password").fill("admin123")
    page.get_by_role("button", name = "Login")
    expect(page.get_by_role("heading", name = "Dashboard")).to_be_visible()