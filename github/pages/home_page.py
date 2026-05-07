from config import BASE_URL
from github.locators.home_page_locators import HomePageLocators
from github.pages.base_page import BasePage


class HomePage(BasePage):

    def open(self):
        self.go_to_url(BASE_URL)

    def click_sign_in_button(self):
        self.click_element(HomePageLocators.SIGN_IN_BUTTON)

    def click_sign_in_button_mobile(self):
        self.click_element(HomePageLocators.SIGN_IN_BUTTON_MOBILE)

    def click_sign_up_button(self):
        self.click_element(HomePageLocators.SIGN_UP_BUTTON)