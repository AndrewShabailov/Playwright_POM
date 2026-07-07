from pages.base_page import BasePage
from locators import login_locators as locators
from playwright.sync_api import expect


class LoginPage(BasePage):
    page_url = 'web/login'

    def login(self, email, password):
        self.find(locators.login_input).fill(email)
        self.find(locators.password_input).fill(password)
        self.find(locators.login_button).click()

    def check_error_message_is(self, text):
        expect(self.find(locators.error_message)).to_contain_text(text)
