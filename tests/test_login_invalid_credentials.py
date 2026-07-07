def test_login_invalid_credentials(login_page):
    login_page.open_page()
    login_page.login('wrong@example.com', 'wrongpassword')
    login_page.check_error_message_is('Wrong login/password')
