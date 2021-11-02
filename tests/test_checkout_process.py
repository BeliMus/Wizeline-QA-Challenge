import pytest
from assertpy import assert_that
import lib.LoginCredentials as Credentials
import lib.FillTestData as FillTestData
from pageobjects.login_page import LoginPage
from pageobjects.inventory_page import InventoryPage
from pageobjects.cart_page import CartPage
from pageobjects.checkout_information_page import CheckoutInformationPage
from pageobjects.checkout_overview_page import CheckoutOverviewPage
import lib.Constants as Constants

testData = FillTestData.fill_data([Credentials.STANDARD_USER, Credentials.STANDARD_PASSWORD, Constants.FIRST_NAME,
                                   Constants.LAST_NAME, Constants.ZIP_CODE])


@pytest.mark.parametrize(
    "browser, username, password, firstname, lastname, zipcode", testData
)
@pytest.mark.checkout
def test_checkout_process_success(driver, username, password, firstname, lastname, zipcode):
    login = LoginPage(driver)
    login.login_process(username, password)
    inventory = InventoryPage(driver)
    for i in range(1, inventory.get_products_count()):
        inventory.click_add_to_cart()
    inventory.click_cart_link()
    cart = CartPage(driver)
    cart.click_checkout_button()

    assert_that(cart.get_url()).is_equal_to(Constants.CHECKOUT_INFORMATION_URL)
    assert_that(login.get_title_span()).is_not_none()
    assert_that(login.get_title_span_text()).is_equal_to(Constants.CHECKOUT_INFORMATION_TITLE)

    checkout_information = CheckoutInformationPage(driver)
    checkout_information.set_first_name(firstname)
    checkout_information.set_last_name(lastname)
    checkout_information.set_zipcode(zipcode)
    checkout_information.click_continue()

    assert_that(cart.get_url()).is_equal_to(Constants.CHECKOUT_OVERVIEW_URL)
    assert_that(login.get_title_span()).is_not_none()
    assert_that(login.get_title_span_text()).is_equal_to(Constants.CHECKOUT_OVERVIEW_TITLE)

    checkout_overview = CheckoutOverviewPage(driver)
    checkout_overview.click_finish()

    assert_that(cart.get_url()).is_equal_to(Constants.CHECKOUT_COMPLETE_URL)
    assert_that(login.get_title_span()).is_not_none()
    assert_that(login.get_title_span_text()).is_equal_to(Constants.CHECKOUT_COMPLETE_TITLE)



