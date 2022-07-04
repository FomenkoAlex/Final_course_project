from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators
from .base_page import BasePage
import math


class ProductPage(BasePage):
    def should_add_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_message_about_add_to_basket()
        self.product_name_matching()
        self.should_be_message_with_price_of_basket()
        self.product_price_matching()

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_about_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET), "Message about add to " \
                                                                                          "basket is not presented"

    def product_name_matching(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product_name.text == product_name_in_message.text, "Product name does not match"

    def should_be_message_with_price_of_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRICE_OF_BASKET), "Message with price of " \
                                                                                           "basket is not presented"

    def product_price_matching(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        message_with_price_of_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRICE_OF_BASKET)
        assert price_product.text == message_with_price_of_basket.text, "The price of the cart does not match the " \
                                                                        "price of the product"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_message_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"
