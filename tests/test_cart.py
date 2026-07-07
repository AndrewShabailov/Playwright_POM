def test_cart_overview(cart_page):
    cart_page.open_page()
    cart_page.check_order_title_is('Order overview')


def test_empty_cart_message(cart_page):
    cart_page.open_page()
    cart_page.check_cart_message_is('Your cart is empty!')


def test_cart_step_label(cart_page):
    cart_page.open_page()
    cart_page.check_cart_step_label('Review Order')
