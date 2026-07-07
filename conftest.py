import pytest
from playwright.sync_api import Page, BrowserContext
from pages.cart_page import CartPage
from pages.desk_category_page import DeskPage
from pages.office_design_software_page import OfficeDesignSoftwarePage
from pages.warranty_page import WarrantyPage
from pages.base_page import BasePage
from pages.login_page import LoginPage


@pytest.fixture
def page(context: BrowserContext):
    page = context.new_page()
    return page


@pytest.fixture
def base_page(page: Page):
    return BasePage(page)


@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)


@pytest.fixture
def desk_page(page: Page):
    return DeskPage(page)


@pytest.fixture
def office_design_software_page(page: Page):
    return OfficeDesignSoftwarePage(page)


@pytest.fixture
def warranty_page(page: Page):
    return WarrantyPage(page)


@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)
