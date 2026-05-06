from github.locators.sign_in_page_locators import SignInPageLocators
from github.pages.base_page import BasePage


class SignInPage(BasePage):

    def click_sign_in_button(self):
        self.wait_until_visible(SignInPageLocators.SIGN_IN_BUTTON)
        self.click_element(SignInPageLocators.SIGN_IN_BUTTON)

    def fill_sign_in_login_input_field(self, value):
        self.wait_until_visible(SignInPageLocators.USERNAME_INPUT_FIELD)
        self.fill_input(SignInPageLocators.USERNAME_INPUT_FIELD, value)

    def fill_sign_in_password_input_field(self, value):
        self.wait_until_visible(SignInPageLocators.PASSWORD_INPUT_FIELD)
        self.fill_input(SignInPageLocators.PASSWORD_INPUT_FIELD, value)

    def click_forgot_password_link(self):
        self.wait_until_visible(SignInPageLocators.FORGOT_PASSWORD_BUTTON)
        self.click_element(SignInPageLocators.FORGOT_PASSWORD_BUTTON)

    def click_create_an_account_link(self):
        self.wait_until_visible(SignInPageLocators.CREATE_ACCOUNT_BUTTON)
        self.click_element(SignInPageLocators.CREATE_ACCOUNT_BUTTON)