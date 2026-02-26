from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.locators.shop_product_page_locators import (
    ProductPageLocators as loc
)


class ProductPage(BasePage):
    page_url = "/shop/furn-9999-office-design-software-7?category=9"

    def check_product_main_info_is_displayed(self):
        title = self.page.locator(loc.TITLE)
        price = self.page.locator(loc.PRICE)
        button = self.page.locator(loc.ADD_TO_CART_BUTTON)

        expect(title).to_be_visible()
        expect(price).to_be_visible()
        expect(button).to_be_visible()

        assert title.inner_text().strip() != ""
        assert price.inner_text().strip() != ""

    def check_default_quantity_is(self, expected_quantity):
        quantity = self.page.locator(loc.QUANTITY_INPUT)

        expect(quantity).to_be_visible()
        assert quantity.input_value() == str(expected_quantity)

    def increase_quantity(self, times=1):
        button = self.page.locator(loc.ADD_ONE_BUTTON)

        for _ in range(times):
            button.click()

    def add_to_cart(self):
        self.page.locator(loc.ADD_TO_CART_BUTTON).click()

    def wait_until_cart_counter_is(self, expected_value):
        expect(
            self.page.locator(loc.CART_COUNTER).first
        ).to_have_text(str(expected_value))

    def go_to_cart(self):
        self.page.get_by_role("link", name="eCommerce cart").click()

    def add_product_to_cart(self):
        self.add_to_cart()
