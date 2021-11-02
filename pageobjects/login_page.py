from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
import lib.Constants as Constants


class LoginPage(BasePage):
    URL = Constants.HOME_URL
    USERNAME_ID = (By.ID, 'user-name')
    PASSWORD_ID = (By.ID, 'password')
    LOGIN_BUTTON_ID = (By.ID, 'login-button')
    H3_ERROR = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.open()

    def set_username(self, username):
        self.find_element(*self.USERNAME_ID).send_keys(username)

    def set_password(self, password):
        self.find_element(*self.PASSWORD_ID).send_keys(password)

    def click_login_button(self):
        self.click_element(*self.LOGIN_BUTTON_ID)

    def get_username(self):
        return self.find_element(*self.USERNAME_ID).get_attribute("value")

    def get_password(self):
        return self.find_element(*self.PASSWORD_ID).get_attribute("value")

    def get_error(self):
        return self.get_element_inner_text(*self.H3_ERROR)

    def login_process(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
