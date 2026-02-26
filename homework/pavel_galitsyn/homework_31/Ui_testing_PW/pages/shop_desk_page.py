from playwright.sync_api import expect
import re

from pages.base_page import BasePage
from pages.locators.shop_desk_locators import ShopDeskLocators as loc


class ShopDeskPage(BasePage):
    page_url = "/shop/category/desks-1"

    def apply_sorting_by_price_low_to_high(self):
        self.page.locator(loc.SORT_DROPDOWN).click()
        self.page.locator(loc.SORT_LOW_TO_HIGH).click()

    def check_products_are_sorted_by_price_low_to_high(self):
        prices = self.page.locator(loc.PRODUCT_PRICES)

        expect(prices.first).to_be_visible()

        price_values = [
            float(price.replace("$", "").replace(",", "").strip())
            for price in prices.all_inner_texts()
        ]

        assert price_values == sorted(price_values)

    def check_all_products_have_price(self):
        products = self.page.locator(loc.PRODUCTS)

        count = products.count()
        assert count > 0

        for i in range(count):
            product = products.nth(i)
            price = product.locator(loc.PRODUCT_PRICE)

            expect(price).to_be_visible()
            assert price.inner_text().strip() != ""

    def apply_steel_filter(self):
        expect(
            self.page.locator(loc.PRICE_SLIDER_READY).first
        ).to_be_visible()

        self.page.get_by_role("checkbox", name="Steel").click()

        expect(self.page).to_have_url(
            re.compile(r"attrib=1-1")
        )

    def get_products_count(self):
        products = self.page.locator(loc.PRODUCTS)
        expect(products.first).to_be_visible()
        return products.count()

    def check_products_count_changed(self, old_count):
        new_count = self.page.locator(loc.PRODUCTS).count()
        assert new_count != old_count
