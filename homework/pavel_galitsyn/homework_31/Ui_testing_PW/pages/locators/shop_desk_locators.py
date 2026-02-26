class ShopDeskLocators:
    SORT_DROPDOWN = (
        "//div[contains(@class,'o_sortby_dropdown')]"
        "//a[@data-bs-toggle='dropdown']"
    )

    SORT_LOW_TO_HIGH = (
        "//span[normalize-space()='Price - Low to High']"
    )

    PRODUCT_PRICES = ".oe_currency_value"

    PRICE_SLIDER_READY = "input.ghost.multirange"

    PRODUCTS = ".oe_product_cart"

    PRODUCT_PRICE = ".oe_currency_value"

    STEEL_FILTER = "//label[contains(text(),'Steel')]"
