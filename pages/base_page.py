from playwright.sync_api import Page, expect, Locator


class BasePage:
    base_url = 'http://testshop.qa-practice.com/'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}', wait_until='networkidle')
        else:
            raise NotImplementedError('Page not opened')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def assert_element_text(self, locator: tuple, expected_text: str):
        expect(self.find(locator)).to_have_text(expected_text)
