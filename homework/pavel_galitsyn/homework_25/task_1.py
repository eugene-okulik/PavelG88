from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver



def test_text_check(driver):
    input_data = "testword"

    driver.get("https://www.qa-practice.com/elements/input/simple")

    text_string = driver.find_element(By.ID, "id_text_string")
    text_string.send_keys(input_data)
    text_string.send_keys(Keys.ENTER)

    result_text = driver.find_element(By.CLASS_NAME, "result-text")
    print(result_text.text)
