from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser_launch = playwright.chromium.launch(headless=False)
    page_new = browser_launch.new_page()

    page_new.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page_new.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page_new.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page_new.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page_new.get_by_test_id('registration-page-registration-button')
    registration_button.click()
    expect(page_new).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    title = page_new.get_by_test_id('dashboard-toolbar-title-text')
    expect(title).to_have_text('Dashboard')

