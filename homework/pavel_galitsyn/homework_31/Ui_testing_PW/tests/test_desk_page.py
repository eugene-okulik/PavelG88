def test_products_sorted_by_price(desk_page):
    desk_page.open_page()

    desk_page.apply_sorting_by_price_low_to_high()
    desk_page.check_products_are_sorted_by_price_low_to_high()


def test_all_products_have_price(desk_page):
    desk_page.open_page()

    desk_page.check_all_products_have_price()


def test_steel_filter_changes_products(desk_page):
    desk_page.open_page()

    old_count = desk_page.get_products_count()

    desk_page.apply_steel_filter()
    desk_page.check_products_count_changed(old_count)
