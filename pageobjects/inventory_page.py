from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pageobjects.base_page import BasePage
import lib.Constants as Constants


class InventoryPage(BasePage):
    URL = Constants.INVENTORY_URL
    MENU_BUTTON_ID = (By.ID, 'react-burger-menu-btn')
    LOGOUT_LINK_ID = (By.ID, 'logout_sidebar_link')
    SORT_DROPDOWN = (By.CLASS_NAME, 'product_sort_container')
    OPTION_SORT_PRICE_LOW_TO_HIGH = (By.CSS_SELECTOR, '.product_sort_container > option:nth-child(3)')
    PRODUCT_PRICES = (By.CLASS_NAME, 'inventory_item_price')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '[id^=add-to-cart]')
    PRODUCTS_QUANTITY_IN_CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    PRODUCT_DETAILS_DIV = (By.CLASS_NAME, 'inventory_item')
    ADD_TO_CART_SAUCE_LABS_ONESIE_BUTTON_ID = (By.ID, 'add-to-cart-sauce-labs-onesie')
    CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_menu_button(self):
        self.click_element(*self.MENU_BUTTON_ID)
        self.driver.implicitly_wait(10)

    def click_logout_link(self):
        self.click_element(*self.LOGOUT_LINK_ID)

    def click_sort_dropdown(self):
        self.click_element(*self.SORT_DROPDOWN)

    def click_add_to_cart(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def click_cart_link(self):
        self.click_element(*self.CART_LINK)

    def add_lab_sauce_onesie_to_cart(self):
        self.click_element(*self.ADD_TO_CART_SAUCE_LABS_ONESIE_BUTTON_ID)

    def sort_by_price_low_to_high(self):
        self.click_sort_dropdown()
        sort_option = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(self.OPTION_SORT_PRICE_LOW_TO_HIGH)
        )
        sort_option.click()

    def get_list_of_prices(self):
        prices = self.find_elements(*self.PRODUCT_PRICES)
        return [float(item.text.replace("$", "")) for item in prices]

    def get_products_quantity_in_cart(self):
        return int(self.get_element_inner_text(*self.PRODUCTS_QUANTITY_IN_CART_BADGE))

    def get_products_count(self):
        return len(self.find_elements(*self.PRODUCT_DETAILS_DIV))

    def logout_process(self):
        self.click_menu_button()
        self.click_logout_link()
