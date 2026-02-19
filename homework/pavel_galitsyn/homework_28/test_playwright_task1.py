from playwright.sync_api import Page, expect


def test_alert1(page: Page):
    page.on("dialog", lambda dialog: dialog.accept())

    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role("link", name="Click").click()

    expect(page.locator("#result-text")).to_have_text("Ok")
