def test_remove_item_from_cart(warranty_page, cart_page):
    warranty_page.open_page()
    warranty_page.add_warranty()
    cart_page.open_page()
    cart_page.remove_item()
    cart_page.check_cart_message_is('Your cart is empty!')
