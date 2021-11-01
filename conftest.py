"""Test configuration for pytest"""
import time
import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from selenium.webdriver import Ie
from selenium.webdriver import Opera


@pytest.fixture
def driver(request, browser):
    """Test fixtures for pytest."""
    if browser == webdriver.Chrome:
        web_driver = Chrome()
    elif browser == webdriver.Firefox:
        web_driver = Firefox()
    elif browser == webdriver.Edge:
        web_driver = Edge()
    elif browser == webdriver.Ie:
        web_driver = Ie()
    elif browser == webdriver.Opera:
        web_driver = Opera()
    else:
        raise NameError("Unsupported browser: %s" % browser)

    web_driver.delete_all_cookies()

    # Close/quit browser after the test is completed.
    request.addfinalizer(lambda *args: finalizer(web_driver))
    return web_driver


def finalizer(web_driver):
    """Close/quit browser after the test is completed."""
    web_driver.close()
    web_driver.quit()
    time.sleep(2)
