from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
import lib.Constants as Constants


class CartPage(BasePage):
    URL = Constants.CART_URL
    MENU_BUTTON_ID = (By.ID, 'react-burger-menu-btn')
    LOGOUT_LINK_ID = (By.ID, 'logout_sidebar_link')
    CART_PRODUCT_NAME = (By.CLASS_NAME, 'inventory_item_name')
    CHECKOUT_BUTTON_ID = (By.ID, 'checkout')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_cart_products_name(self):
        return [item.text for item in self.find_elements(*self.CART_PRODUCT_NAME)]

    def click_checkout_button(self):
        self.click_element(*self.CHECKOUT_BUTTON_ID)
        self.driver.implicitly_wait(10)
