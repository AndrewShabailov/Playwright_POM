from locators import desk_locators as locators
from pages.base_page import BasePage
from playwright.sync_api import expect


class DeskPage(BasePage):
    page_url = 'shop/category/desk-1'

    def check_presence_of_customizable_desk_on_page(self, text):
        expect(self.find(locators.customizable_desk)).to_contain_text(text)

    def check_presence_of_corner_desk_left_sit_on_page(self, text):
        expect(self.find(locators.corner_desk_left_sit)).to_contain_text(text)

    def check_presence_of_acoustic_bloc_screens_on_page(self, text):
        expect(self.find(locators.acoustic_bloc_screens)).to_contain_text(text)
