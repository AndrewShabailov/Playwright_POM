from pages.base_page import BasePage
from locators import office_design_software_locators as locators
from playwright.sync_api import expect


class OfficeDesignSoftwarePage(BasePage):
    page_url = 'shop/furn-9999-office-design-software-7?category=9'

    def check_item_title_is(self, text):
        expect(self.find(locators.item_title)).to_contain_text(text)

    def check_item_price_is(self, text):
        expect(self.find(locators.item_price)).to_contain_text(text)

    def check_item_image_is_displayed(self):
        item_image = self.find(locators.item_image)
        expect(item_image).to_be_visible()
