from pages.base_page import BasePage
from locators import warranty_locators
from playwright.sync_api import expect


class WarrantyPage(BasePage):
    page_url = 'shop/warranty-33'

    def check_item_title_is(self, text):
        expect(self.find(warranty_locators.item_title)).to_contain_text(text)

    def add_warranty(self):
        with self.page.expect_response(lambda response: 'cart/update_json' in response.url):
            self.find(warranty_locators.add_to_cart).click()
