import pytest
from assertpy import assert_that
import lib.LoginCredentials as Credentials
import lib.FillTestData as FillTestData
from pageobjects.login_page import LoginPage
from pageobjects.inventory_page import InventoryPage
from pageobjects.cart_page import CartPage
from lib.Constants import SAUCE_LABS_ONESIE, CART_URL, CART_TITLE

testData = FillTestData.fill_data([Credentials.STANDARD_USER, Credentials.STANDARD_PASSWORD])


@pytest.mark.parametrize(
    "browser, username, password", testData
)
@pytest.mark.inventory
@pytest.mark.inventory_sort_price_low_high
def test_sort_price_low_high_success(driver, username, password):
    login = LoginPage(driver)
    login.login_process(username, password)
    inventory = InventoryPage(driver)
    inventory.sort_by_price_low_to_high()
    prices = inventory.get_list_of_prices()
    for i in range(len(prices) - 1):
        assert_that(prices[i]).is_less_than_or_equal_to(prices[i + 1])


@pytest.mark.parametrize(
    "browser, username, password", testData
)
@pytest.mark.inventory
@pytest.mark.inventory_add_multiple_items
def test_add_multiple_items_success(driver, username, password):
    login = LoginPage(driver)
    login.login_process(username, password)
    inventory = InventoryPage(driver)
    for i in range(1, inventory.get_products_count()):
        inventory.click_add_to_cart()
        assert_that(inventory.get_products_quantity_in_cart()).is_equal_to(i)


@pytest.mark.parametrize(
    "browser, username, password", testData
)
@pytest.mark.inventory
@pytest.mark.inventory_add_sauce_labs_onesie
def test_add_sauce_labs_onesie_success(driver, username, password):
    login = LoginPage(driver)
    login.login_process(username, password)
    inventory = InventoryPage(driver)
    inventory.add_lab_sauce_onesie_to_cart()
    inventory.click_cart_link()
    assert_that(login.get_url()).is_equal_to(CART_URL)
    assert_that(login.get_title_span()).is_not_none()
    assert_that(login.get_title_span_text()).is_equal_to(CART_TITLE)
    cart = CartPage(driver)
    products_in_cart = cart.get_cart_products_name()
    assert_that(SAUCE_LABS_ONESIE).is_in(*products_in_cart)
