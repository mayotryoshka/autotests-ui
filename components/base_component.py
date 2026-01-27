from playwright.sync_api import Page, expect
from typing import Pattern

class BaseComponent:
    def __init__(self, page: Page):
        self.page = page


    def check_current_url(self, expected_url: Pattern[str]):
        expect(self).to_have_url(expected_url)