"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import random
from time import sleep

import pytest

from conftest import chrome_only
from github.pages.home_page import HomePage

@pytest.mark.parametrize("desktop_browser", [(1280, 720), (1720, 1080)], indirect=True)
def test_github_desktop_different_size(desktop_browser):
    home_page = HomePage(desktop_browser)
    home_page.open()
    sleep(5)
    home_page.click_sign_in_button()
    sleep(5)


@chrome_only
@pytest.mark.parametrize("desktop_browser", [(1280, 720), (1920, 1080)], indirect=True)
def test_chrome_desktop_different_size(browser, desktop_browser):
    home_page = HomePage(browser)
    home_page.open()
    sleep(2)
    home_page.click_sign_in_button()

@pytest.mark.parametrize("mobile_browser", [(480, 800), (300, 600)], indirect=True)
def test_github_mobile(mobile_browser):
    pass

@pytest.mark.xfail(reason='Мы знаем, что этот тест упадёт')
def test_failed():
    user1 = random.randint(0, 100)
    user2 = random.randint(0, 100)
    assert user1 == user2

# Better way to use xfail:
def test_failed_2():
    user1 = random.randint(0, 100)
    user2 = random.randint(0, 100)
    try:
        assert user1 == user2
    except AssertionError:
        pytest.xfail(reason='Мы знаем, что этот тест упадёт')