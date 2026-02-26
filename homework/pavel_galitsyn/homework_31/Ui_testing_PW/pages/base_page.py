from playwright.sync_api import Page


class BasePage:
    base_url = "http://testshop.qa-practice.com"
    page_url: str | None = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if not self.page_url:
            raise NotImplementedError(
                "Page cannot be opened for this page class"
            )
        full_url = f"{self.base_url}{self.page_url}"
        self.page.goto(full_url)

    def find(self, selector: str):
        return self.page.locator(selector)

    def find_all(self, selector: str):
        return self.page.locator(selector)

    def wait_for_url(self, url_part: str):
        self.page.wait_for_url(f"**{url_part}**")

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")
