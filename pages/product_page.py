from selenium.webdriver.common.by import By
from .locators import Basket, ProductPageLocators
from .base_page import BasePage


class PageObject(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        basket.click()

    def should_be_added_to_basket(self):
        name = self.browser.find_element(By.XPATH,'//*[@id="messages"]/div[1]/div/strong').text
        name2 = self.browser.find_element(*Basket.NAME_PRODUCT).text
        assert name == name2, "Товар не найден"

    def should_be_price_product(self):
        price = self.browser.find_element(By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong').text
        price2 = self.browser.find_element(*Basket.PRICE_PRODUCT).text
        assert price == price2, "Цена не соответствует"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"