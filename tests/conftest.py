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