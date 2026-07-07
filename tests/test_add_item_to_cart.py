def test_add_item_to_cart(warranty_page, cart_page):
    warranty_page.open_page()
    warranty_page.add_warranty()
    cart_page.open_page()
    cart_page.check_cart_item_name('Warranty (1 year)')
