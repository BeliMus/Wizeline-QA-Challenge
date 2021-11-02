from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
import lib.Constants as Constants


class CheckoutOverviewPage(BasePage):
    URL = Constants.CHECKOUT_OVERVIEW_URL
    FINISH_BUTTON_ID = (By.ID, 'finish')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_finish(self):
        self.click_element(*self.FINISH_BUTTON_ID)
