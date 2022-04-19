from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    CORRECT_URL ="https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    CORRECT_LOGIN_FORM = (By.ID, "login_form")
    CORRECT_REGISTER_FORM = (By.ID, "register_form")