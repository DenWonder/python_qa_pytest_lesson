from time import sleep

import pytest

from github.pages.home_page import HomePage

@pytest.mark.desktop
def test_github_desktop(desktop_browser):
    home_page = HomePage(desktop_browser)
    home_page.open()
    sleep(5)
    home_page.click_sign_in_button()
    sleep(5)

@pytest.mark.mobile
def test_github_mobile(mobile_browser):
    home_page = HomePage(mobile_browser)
    home_page.open()
    sleep(5)
    home_page.click_sign_in_button_mobile()
    sleep(5)