from selenium.webdriver.common.by import By


class HomePageLocators:
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, '.HeaderMenu-link--sign-in')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, '.HeaderMenu-link--sign-up')
    HEADER_BURGER_BUTTON = (By.CSS_SELECTOR, '.js-header-menu-toggle')