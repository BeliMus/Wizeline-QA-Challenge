import pytest
import lib.LoginCredentials as Credentials
import lib.FillTestData as FillTestData
from lib.Constants import INVENTORY_URL, INVENTORY_TITLE, HOME_URL, INVALID_CREDENTIALS
from assertpy import assert_that
from pageobjects.login_page import LoginPage
from pageobjects.inventory_page import InventoryPage

testData = FillTestData.fill_data([Credentials.STANDARD_USER, Credentials.STANDARD_PASSWORD])


@pytest.mark.parametrize(
    "browser, username, password", testData
)
@pytest.mark.login
@pytest.mark.login_success
def test_successful_login(driver, username, password):
    login = LoginPage(driver)
    login.login_process(username, password)

    assert_that(login.get_url()).is_equal_to(INVENTORY_URL)
    assert_that(login.get_title_span()).is_not_none()
    assert_that(login.get_title_span_text()).is_equal_to(INVENTORY_TITLE)


@pytest.mark.parametrize(
    "browser, username, password", testData
)
@pytest.mark.login
@pytest.mark.login_logout
def test_logout(driver, username, password):
    login = LoginPage(driver)
    login.login_process(username, password)

    assert_that(login.get_url()).is_equal_to(INVENTORY_URL)
    assert_that(login.get_title_span()).is_not_none()
    assert_that(login.get_title_span_text()).is_equal_to(INVENTORY_TITLE)
    inventory = InventoryPage(driver)
    inventory.logout_process()

    assert_that(login.get_url()).is_equal_to(HOME_URL)


testData = FillTestData.fill_data([Credentials.INVALID_USER, Credentials.STANDARD_PASSWORD])


@pytest.mark.parametrize(
    "browser, username, password", testData
)
@pytest.mark.login
@pytest.mark.login_invalid
def test_invalid_login(driver, username, password):
    login = LoginPage(driver)
    login.login_process(username, password)

    assert_that(login.get_url()).is_equal_to(HOME_URL)
    assert_that(login.get_error()).is_equal_to(INVALID_CREDENTIALS)
