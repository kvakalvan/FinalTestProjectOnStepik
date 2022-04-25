from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import Basket

class BasketPage(BasePage):
    def should_not_be_success_message_in_basket(self):
        assert self.is_not_element_present(*Basket.PRODUCT_BASKET), \
            "Присутствует товар в корзине"

    def should_text_to_empty_basket(self):
        assert self.is_element_present(*Basket.BASKET_MESSAGE), \
            "Текста о пустой корзине нет"