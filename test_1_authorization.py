from testpage import BasePage
from testpage import Operations


def test_authorization_with_right_login(browser, hello_user):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_password()
    page.click_login_button()
    assert page.get_hello_user() == hello_user
