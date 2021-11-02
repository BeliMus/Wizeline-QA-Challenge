""" POM Base class for all other Page classes. """
from selenium.webdriver.common.by import By


class BasePage(object):
    TITLE_SPAN = (By.CLASS_NAME, 'title')

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_element_inner_text(self, *locator):
        return self.driver.find_element(*locator).get_attribute("innerText")

    def get_title(self):
        return self.driver.title

    def get_title_span(self):
        return self.find_element(*self.TITLE_SPAN)

    def get_title_span_text(self):
        return self.find_element(*self.TITLE_SPAN).get_attribute("innerText")

    def get_url(self):
        return self.driver.current_url

    def open(self):
        self.driver.get(self.URL)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()
