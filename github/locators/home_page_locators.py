from selenium.webdriver.common.by import By


class HomePageLocators:
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.HeaderMenu-link--sign-in')
    SIGN_IN_BUTTON_MOBILE = (By.CSS_SELECTOR, 'div.flex-1 a.HeaderMenu-link')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, '.HeaderMenu-link--sign-up')
    SIGN_UP_BUTTON_MOBILE = (By.CSS_SELECTOR, '.HeaderMenu-link--sign-up')
    HEADER_BURGER_BUTTON = (By.CSS_SELECTOR, '.js-header-menu-toggle')