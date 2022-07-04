from .locators import LoginPageLocators
from .base_page import BasePage
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It`s not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        enter_email = self.browser.find_element(*LoginPageLocators.ENTER_EMAIL)
        enter_email.send_keys(email)
        password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password.send_keys("12345678Qw")
        repeat_password = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD)
        repeat_password.send_keys("12345678Qw")
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
