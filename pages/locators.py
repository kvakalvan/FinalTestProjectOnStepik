from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    CORRECT_LOGIN_FORM = (By.ID, "login_form")
    CORRECT_REGISTER_FORM = (By.ID, "register_form")


class Basket():
    NAME_PRODUCT = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    PRICE_PRODUCT = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    PRODUCT_BASKET = (By.CLASS_NAME, "basket-title")
    BASKET_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

