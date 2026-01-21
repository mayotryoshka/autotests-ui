from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
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

        context.storage_state(path='browser-state-new.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state-new.json')
        page_new = context.new_page()

        page_new.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        title = page_new.get_by_test_id('courses-list-toolbar-title-text')
        expect(title).to_be_visible()
        expect(title).to_have_text('Courses')

        empty_result_header = page_new.get_by_test_id('courses-list-empty-view-title-text')
        expect(empty_result_header).to_be_visible()
        expect(empty_result_header).to_have_text('There is no results')

        empty_result_icon = page_new.get_by_test_id('courses-list-empty-view-icon')
        expect(empty_result_icon).to_be_visible()

        empty_result_text = page_new.get_by_test_id('courses-list-empty-view-description-text')
        expect(empty_result_text).to_be_visible()
        expect(empty_result_text).to_have_text('Results from the load test pipeline will be displayed here')