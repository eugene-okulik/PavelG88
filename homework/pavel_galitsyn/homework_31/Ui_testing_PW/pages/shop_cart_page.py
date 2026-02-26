from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators.shop_cart_locators import ShopCartLocators as loc


class ShopCartPage(BasePage):
    page_url = "/shop/cart"

    def check_title_is(self, expected_text):
        title = self.page.locator(loc.TITLE)
        expect(title).to_be_visible()
        expect(title).to_have_text(expected_text)

    def check_cart_is_empty(self):
        empty_message = self.page.locator(loc.EMPTY_CART_MESSAGE)
        expect(empty_message).to_be_visible()
        expect(empty_message).to_have_text("Your cart is empty!")

    def check_checkout_steps_are_visible(self):
        container = self.page.locator(
            (
                "div.d-flex.flex-column.flex-md-row."
                "align-items-end.align-items-md-start."
                "justify-content-center"
            )
        )

        expected_steps = ["Review Order", "Shipping", "Payment"]

        for step in expected_steps:
            expect(
                container.locator(f"p:has-text('{step}')")
            ).to_be_visible()

    def check_product_quantity_is(self, expected_quantity):
        quantity = self.page.locator(".js_quantity")
        expect(quantity).to_be_visible()
        expect(quantity).to_have_value(str(expected_quantity))

    def remove_product(self):
        product_row = self.page.locator(loc.PRODUCT_ROW)

        expect(product_row).to_be_visible()

        self.page.locator(loc.REMOVE_ONE_BUTTON).click()

        expect(product_row).not_to_be_attached()
