import re

from playwright.sync_api import Page, expect


def test_dynamic(page: Page):
    page.goto("https://demoqa.com/")
    page.get_by_role('heading', name='Elements').click()
    page.get_by_text('Dynamic Properties').click()

    page.wait_for_load_state("networkidle")

    button = page.locator("#colorChange")

    expect(button).to_have_attribute(
        "class",
        re.compile(r"\btext-danger\b")
    )
    button.click()
