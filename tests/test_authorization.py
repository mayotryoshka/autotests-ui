import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
        chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
        # переход на указанную страницу

        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')
        # указываем локатор для поля Email new_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        # указываем значение, которым будем заполнять поле

        password_input = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input.fill('password')
        # указываем локатор для поля Password
        # указываем значение, которым будем заполнять поле

        login_button = chromium_page.get_by_test_id('login-page-login-button')
        login_button.click()
        # указываем локатор для кнопки Login chromium_page.locator('//button[@id="login-page-login-button"]')
        # указываем клик по кнопке
        # Playwright поддерживает нативную работу с data-testid

        wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        # указываем локатор для плашки с ошибкой new_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        expect(wrong_email_or_password_alert).to_be_visible()  # проверяем, что плашка с ошибкой видимая
        expect(wrong_email_or_password_alert).to_contain_text('Wrong email or password')
        # проверяем, что плашка с ошибкой содержит нужный текст