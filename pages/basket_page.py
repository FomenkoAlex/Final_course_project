from .locators import ProductPageLocators
from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET), \
            "The product is in the basket, but should not be"

    def is_basket_empty(self):
        assert self.is_element_present(*BasePageLocators.MESSAGE_ABOUT_EMPTY_BASKET), \
            "There is no message that the basket is empty"
