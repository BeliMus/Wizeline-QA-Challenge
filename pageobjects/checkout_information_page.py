from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
import lib.Constants as Constants


class CheckoutInformationPage(BasePage):
    URL = Constants.CHECKOUT_INFORMATION_URL
    FIRST_NAME_ID = (By.ID, 'first-name')
    LAST_NAME_ID = (By.ID, 'last-name')
    ZIPCODE_ID = (By.ID, 'postal-code')
    CONTINUE_BUTTON_ID = (By.ID, 'continue')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_cart_products_name(self):
        return [item.text for item in self.find_elements(*self.CART_PRODUCT_NAME)]

    def click_checkout_button(self):
        self.click_element(*self.CHECKOUT_BUTTON)

    def set_first_name(self, firstname):
        self.find_element(*self.FIRST_NAME_ID).send_keys(firstname)

    def set_last_name(self, lastname):
        self.find_element(*self.LAST_NAME_ID).send_keys(lastname)

    def set_zipcode(self, zipcode):
        self.find_element(*self.ZIPCODE_ID).send_keys(zipcode)

    def click_continue(self):
        self.click_element(*self.CONTINUE_BUTTON_ID)
