from playwright.sync_api import Page, Route, expect
import json


def test_product_name_override(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        response_data = response.json()

        for item in response_data["body"]["digitalMat"]:
            for family in item["familyTypes"]:
                family["productName"] = "яблокофон 17 про"

        response_data = json.dumps(response_data)
        route.fulfill(body=response_data)

    page.route("**/step0_iphone/**", handle_route)

    page.goto("https://www.apple.com/shop/buy-iphone")

    page.get_by_role(
        'heading',
        name='iPhone 17 Pro & iPhone 17 Pro Max'
    ).click()

    product_name = page.locator(
        '[data-autom="DigitalMat-overlay-header-0-0"]'
    )

    expect(product_name).to_have_text("яблокофон 17 про")
