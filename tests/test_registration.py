from playwright.sync_api import sync_playwright
import pytest

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # для сохранения данных в локал сторадже, baseURL, размер экрана, локаль и пр.
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

        context.storage_state(path='browser-state.json')  # Сохранение состояние браузера (куки и localStorage) в файл

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page_new = context.new_page()
        # page_new = browser.new_page() # без контекста

        page_new.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

        page_new.wait_for_timeout(5000)