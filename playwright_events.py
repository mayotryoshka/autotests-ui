from playwright.sync_api import sync_playwright, Request, Response

def log_request(request: Request):
    print(f'Request: {request.url}')

def log_response(response: Response):
    print(f'Response: {response.url}, {response.status}, {response.body()}')

# Если нужно логировать только определённые запросы, используется фильтрация
# def log_specific_requests(request):
#    if "googleapis.com" in request.url:
#        print(f"Filtered request: {request.url}")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.on('request', log_request) # перехват запроса с передачей функции в аргументе (не вызова, т.е. без ())
    # page.remove_listener('request', log_request)
    page.on('response', log_response) # перехват ответа, аналогично
    # page.on("request", log_specific_requests)

    page.wait_for_timeout(5000)