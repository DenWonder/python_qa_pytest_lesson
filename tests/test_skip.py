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

def is_role_can_perform_operation(operation, role):
    if role == 'reader':
        if operation == 'read':
            return True
        return False
    elif role == 'editor':
        if operation == 'read' or operation == 'update':
            return True
        return False
    elif role == 'admin':
        return True
    else:
        return False


@pytest.mark.parametrize("operation", ["create", "read", "update", "delete"])
@pytest.mark.parametrize("user_role", ["reader", "editor", "admin"])
def test_operation(operation, user_role):
    if not is_role_can_perform_operation(operation, user_role):
        pytest.skip(f"skipped, cause operation {operation} is not available for {user_role}")
    assert operation in ["create", "read", "update", "delete"]
    assert user_role in ["reader", "editor", "admin"]

@pytest.mark.parametrize("browser",
                         [pytest.param("chrome", id="Chrome"),
                          pytest.param("firefox", marks=[pytest.mark.slow], id="Firefox"),
                          pytest.param("safari", marks=[pytest.mark.xfail(reason='TASK-1234 safari problem')], id="Safari")])
def test_browser(browser):
    time.sleep(1)
    pass