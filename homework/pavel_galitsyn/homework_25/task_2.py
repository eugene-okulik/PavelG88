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


def test_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("Fedor")
    wait.until(EC.visibility_of_element_located((By.ID, "lastName"))).send_keys("Petrov")
    wait.until(
        EC.visibility_of_element_located((By.ID, "userEmail"))
    ).send_keys("mailfedora@example.com")

    # Gender
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Male']"))
    ).click()

    # Number
    wait.until(
        EC.visibility_of_element_located((By.ID, "userNumber"))
    ).send_keys("1234567890")

    # Date of Birth
    wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))).click()

    Select(
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "react-datepicker__month-select")
            )
        )
    ).select_by_visible_text("December")

    Select(
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "react-datepicker__year-select")
            )
        )
    ).select_by_visible_text("1990")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@aria-label='Choose Tuesday, December 11th, 1990']")
        )
    ).click()

    # Subjects
    subjects = ["Maths", "Arts"]

    container = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".subjects-auto-complete__value-container")
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});", container
    )

    wait.until(EC.element_to_be_clickable(container)).click()

    input_ = wait.until(EC.visibility_of_element_located((By.ID, "subjectsInput")))

    for subject in subjects:
        input_.send_keys(subject[:2])

        option = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//div[contains(@class,'subjects-auto-complete__option') "
                    f"and normalize-space()='{subject}']",
                )
            )
        )
        option.click()

    # Hobbies
    hobbies = ["Sports", "Reading"]

    for hobby in hobbies:
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//label[normalize-space()='{hobby}']")
            )
        ).click()

    # Current Address
    wait.until(
        EC.visibility_of_element_located((By.ID, "currentAddress"))
    ).send_keys("m-on 3 dom 28 kv 20")

    # State and City
    wait.until(EC.element_to_be_clickable((By.ID, "state"))).click()

    state_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']"))
    )
    state_option.click()

    wait.until(EC.element_to_be_clickable((By.ID, "city"))).click()

    city_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']"))
    )
    city_option.click()

    # Submit
    wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()

    # Modal popup
    modal = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-content"))
    )

    rows = modal.find_elements(By.CSS_SELECTOR, "tbody tr")

    print("\nSubmitted form data:")

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        print(f"{cells[0].text}: {cells[1].text}")
