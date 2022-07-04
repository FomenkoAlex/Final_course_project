from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    ENTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main p.price_color")
    MESSAGE_WITH_PRICE_OF_BASKET = (By.CSS_SELECTOR, ".alert-info strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET = (By.CSS_SELECTOR, ".basket-mini a")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
