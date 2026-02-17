from playwright.sync_api import Page


def test_demo1(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role('link', name="Form Authentication").click()
    username = page.get_by_role('textbox', name="Username")
    username.fill('username1')
    password = page.get_by_role('textbox', name="Password")
    password.fill('password1')
    page.get_by_role('button', name="Login").click()


def test_demo2(page: Page):
    page.goto("https://demoqa.com/")
    page.get_by_text('Forms').click()
    page.get_by_text('Practice Form').click()
    page.get_by_placeholder('First Name').fill('Petr')
    page.get_by_placeholder('Last Name').fill('Petrovich')
    page.get_by_placeholder('name@example.com').fill('blabla@gmail.com')
    page.locator('#gender-radio-1').click()
    page.get_by_role('textbox', name="Mobile Number").fill('1234567890')
    page.locator('#dateOfBirthInput').fill('17 May 1997')
    subject = page.locator("#subjectsInput")
    subject.fill('Hindi')
    subject.press('Enter')
    page.get_by_label('Sports').click()
    page.get_by_placeholder('Current Address').fill('address1')
    page.locator("#state").click()
    page.get_by_text("NCR").click()
    page.locator("#city").click()
    page.get_by_text("Delhi").click()
    page.get_by_role('button', name='Submit').click()
