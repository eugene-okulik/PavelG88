from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_new_tab(driver):
    driver.get("http://testshop.qa-practice.com/")
    wait = WebDriverWait(driver, 10)

    link = driver.find_element(By.LINK_TEXT, "Customizable Desk")
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    wait.until(
        EC.element_to_be_clickable((By.ID, "add_to_cart"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-secondary"))
    ).click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "sup.my_cart_quantity"),
            "1"
        )
    )

    driver.close()
    driver.switch_to.window(tabs[0])

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa-shopping-cart"))
    ).click()

    cart_item = wait.until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//a[contains(@href,'customizable-desk')]/h6"
        ))
    )

    assert "Customizable Desk (Steel, White)" in cart_item.text
