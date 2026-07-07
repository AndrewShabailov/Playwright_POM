def test_item_title(office_design_software_page):
    office_design_software_page.open_page()
    office_design_software_page.check_item_title_is('Office Design Software')


def test_item_price(office_design_software_page):
    office_design_software_page.open_page()
    office_design_software_page.check_item_price_is('280.00')


def test_item_image_is_displayed(office_design_software_page):
    office_design_software_page.open_page()
    office_design_software_page.check_item_image_is_displayed()
