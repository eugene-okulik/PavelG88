def test_product_main_info_is_displayed(product_page):
    product_page.open_page()
    product_page.check_product_main_info_is_displayed()


def test_product_quantity_adds_correctly_to_cart(product_page, cart_page):
    product_page.open_page()

    product_page.check_default_quantity_is(1)

    product_page.increase_quantity(2)
    product_page.add_to_cart()

    product_page.wait_until_cart_counter_is(3)

    product_page.go_to_cart()
    cart_page.check_product_quantity_is(3)


def test_product_can_be_removed_from_cart(product_page, cart_page):
    product_page.open_page()

    product_page.add_product_to_cart()
    product_page.wait_until_cart_counter_is(1)

    product_page.go_to_cart()

    cart_page.remove_product()
    cart_page.check_cart_is_empty()
