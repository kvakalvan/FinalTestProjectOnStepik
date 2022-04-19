from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
         # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, 'неправильный url адрес '

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.CORRECT_LOGIN_FORM), "Не найдена форма для входа в аккаунт"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.CORRECT_REGISTER_FORM), " Не найдена форма регистрации"