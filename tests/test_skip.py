import time

import pytest
import platform

from conftest import desktop_only

@pytest.mark.desktop
def test_only_desktop(is_mobile):
    if is_mobile:
        pytest.skip("skipped, cause this test is only for desktop")
    pass

@pytest.mark.mobile
def test_only_mobile(is_mobile):
    if not is_mobile:
        pytest.skip("skipped, cause this test is only for mobile")
    pass

@pytest.mark.desktop
@desktop_only
def test_only_windows_desktop(is_windows, desktop_browser):
    if not is_windows:
        pytest.skip("skipped, cause this test is only for windows")
    pass

@pytest.mark.mobile
def test_only_mobile_ios(is_mobile, is_ios):
    if not is_mobile:
        pytest.skip("skipped, cause this test is only for mobile")
    if not is_ios:
        pytest.skip("skipped, cause this test is only for ios")
    pass


@pytest.mark.skip(reason="TASK-1234 Тест нестабильный потому что время от времени не хватает таймаута")
def test_first(browser):
    time.sleep(1)

@pytest.fixture()
def is_macos():
    return platform.system() == 'Darwin'

@pytest.fixture()
def is_windows():
    return platform.system() == 'Windows'

@pytest.fixture()
def is_linux():
    return platform.system() == 'Linux'

@pytest.fixture()
def is_android():
    return platform.system() == 'Android'

@pytest.fixture()
def is_ios():
    return platform.system() == 'iOS'