from playwright.sync_api import sync_playwright, expect

# sync_playwright — функция для запуска Playwright в синхронном режиме
# expect — функция из Playwright, которая позволяет писать ассерты

# sync_playwright() — запускает Playwright для использования его API в управлении браузерами
# with — блок гарантирует, что браузер автоматически закроется
# после завершения работы (без необходимости вручную его закрывать)

with sync_playwright() as playwright:
    browser_launch = playwright.chromium.launch(headless=False) # запуск браузера в видимом режиме (headless=False)
    new_page = browser_launch.new_page() # создание новой страницы в браузере, т.е. у chromium_launch

    new_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    # переход на указанную страницу

    email_input = new_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')
    # указываем локатор для поля Email new_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    # указываем значение, которым будем заполнять поле

    password_input = new_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill('password')
    # указываем локатор для поля Password
    # указываем значение, которым будем заполнять поле

    login_button = new_page.get_by_test_id('login-page-login-button')
    login_button.click()
    # указываем локатор для кнопки Login new_page.locator('//button[@id="login-page-login-button"]')
    # указываем клик по кнопке
    # Playwright поддерживает нативную работу с data-testid

    wrong_email_or_password_alert = new_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # указываем локатор для плашки с ошибкой new_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(wrong_email_or_password_alert).to_be_visible() # проверяем, что плашка с ошибкой видимая
    expect(wrong_email_or_password_alert).to_contain_text('Wrong email or password')
    # проверяем, что плашка с ошибкой содержит нужный текст

    new_page.wait_for_timeout(5000)
    # таймаут в реальных проектах не нужно использовать, потому что:
    # 1. заставляем ждать фиксированное количество времени, а элементы могут грузиться быстрее или медленнее
    # 2. замедляем тесты
    # 3. фиксированное время делает тест негибким
    # лучше выбирать явные ожидания, например, пока элемент не появится, будет доступен для клика, изменит текст и др.
