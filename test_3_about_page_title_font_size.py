from testpage import BasePage
from testpage import Operations


def test_about_page_title_font_size(browser, font_size):
    site = BasePage(browser)
    site.go_to_site()
    page = Operations(browser)
    page.enter_good_login()
    page.enter_good_password()
    page.click_login_button()
    page.click_about_button()
    assert page.get_about_page_title_font_size() == font_size, \
        f'About Page title font size is not equal to {font_size}'
