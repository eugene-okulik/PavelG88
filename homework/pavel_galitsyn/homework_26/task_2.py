from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_move_to(driver):
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    driver.get('http://testshop.qa-practice.com/')

    product_card = wait.until(
        EC.visibility_of_element_located((
            By.XPATH, "//img[@alt='Customizable Desk']"
        ))
    )

    actions.move_to_element(product_card).perform()

    add_to_cart_btn = wait.until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//a[contains(@class,'btn-primary') and @aria-label='Shopping cart']"
        ))
    )

    add_to_cart_btn.click()

    expected_product_name = "Customizable Desk (Steel, White)"

    popup_product = wait.until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, "strong.product-name.product_display_name"
        ))
    )

    assert expected_product_name in popup_product.text
