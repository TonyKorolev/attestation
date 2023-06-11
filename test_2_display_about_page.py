from testpage import BasePage
from testpage import Operations


def test_authorization_with_right_login(browser, about_page):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_password()
    page.click_login_button()
    page.click_about_button()
    assert page.get_about_page_text() == about_page
