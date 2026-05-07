import pytest
from selenium import webdriver

@pytest.fixture(params=["Chrome", "Firefox"], scope="function")
def browser(request):
    driver = webdriver.Chrome() if request.param == "Chrome" else webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(params=[(1920, 1080), (1280, 720)])
def desktop_browser(request, browser):
    width, height = request.param
    browser.set_window_size(width, height)
    yield browser

@pytest.fixture(params=[(480, 800), (300, 500)])
def mobile_browser(request):
    width, height = request.param
    driver = webdriver.Chrome()
    driver.set_window_size(width, height)
    yield driver
    driver.quit()

@pytest.fixture(params=[(1920, 1080), (1280, 720), (480, 800), (300, 500)])
def is_mobile(request):
    width, height = request.param
    if width > height:
        return False
    else:
        return True

desktop_only = pytest.mark.parametrize("desktop_browser", [(1920, 1080), (1280, 720)], indirect=True)
chrome_only = pytest.mark.parametrize("browser", ["Chrome"], indirect=True)