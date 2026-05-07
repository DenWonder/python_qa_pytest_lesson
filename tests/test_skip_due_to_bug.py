import pytest

pytestmark = pytest.mark.skip(reason="this scope of tests skipped cause of bug TASK-1234")

def test_first():
    assert True

def test_second(desktop_browser):
    desktop_browser.get('http://google.com')
    assert desktop_browser.title == 'Google'

@pytest.mark.desktop
@pytest.mark.parametrize("desktop_browser", [(1920, 1080)], indirect=True)
def test_third_marked(desktop_browser):
    desktop_browser.get('http://google.com')
    assert desktop_browser.title == 'Google'

