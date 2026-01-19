import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_lang(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    wait = WebDriverWait(driver, 10)

    select = Select(
        wait.until(
            EC.visibility_of_element_located((By.ID, "id_choose_language"))
        )
    )
    select.select_by_visible_text("Python")

    selected_value = select.first_selected_option.text

    # close select dropdown
    wait.until(
        EC.element_to_be_clickable((By.ID, "id_choose_language"))
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.ID, "submit-id-submit"))
    ).click()

    result = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "result-text"))
    )

    assert result.text == selected_value


def test_dynamic_button(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 10)

    start_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
    )
    start_button.click()

    finish = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    assert finish.text == "Hello World!"
