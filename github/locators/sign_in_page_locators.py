from selenium.webdriver.common.by import By


class SignInPageLocators:
    USERNAME_INPUT_FIELD = (By.CSS_SELECTOR, '#login_field')
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, '#password')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a[id="forgot-password"]')
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'div.authentication-login-footer-links a')