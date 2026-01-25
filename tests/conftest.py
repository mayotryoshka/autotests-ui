import pytest
from playwright.sync_api import sync_playwright, Page, Playwright


# @pytest.fixture
# def chromium_page() -> Page:
#    with sync_playwright() as playwright:
#        browser_launch = playwright.chromium.launch(headless=False)
#        yield browser_launch.new_page()
#        browser_launch.close()


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser_launch = playwright.chromium.launch(headless=False)
    yield browser_launch.new_page()
    browser_launch.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page_new = context.new_page()
    page_new.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page_new.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page_new.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page_new.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page_new.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')


@pytest.fixture(scope='function')
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    yield context.new_page()
    context.close()