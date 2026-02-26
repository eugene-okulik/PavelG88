import pytest

from pages.shop_cart_page import ShopCartPage
from pages.shop_desk_page import ShopDeskPage
from pages.product_page import ProductPage


@pytest.fixture
def cart_page(page):
    return ShopCartPage(page)


@pytest.fixture
def desk_page(page):
    return ShopDeskPage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)