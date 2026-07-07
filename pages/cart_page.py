from locators import cart_locators as locators
from pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    page_url = 'shop/cart/'

    def check_order_title_is(self, text):
        expect(self.find(locators.cart_overview)).to_contain_text(text)

    def check_cart_message_is(self, text):
        expect(self.find(locators.cart_message)).to_contain_text(text)

    def check_cart_step_label(self, text):
        expect(self.find(locators.cart_step_label)).to_contain_text(text)

    def check_cart_item_name(self, text):
        expect(self.find(locators.cart_item_name)).to_contain_text(text)

    def remove_item(self):
        self.find(locators.remove_item).click()
