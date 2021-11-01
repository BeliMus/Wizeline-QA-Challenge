"""Constant variables used throughout the framework."""
from selenium import webdriver

# Drivers List
CHROME = webdriver.Chrome
FIREFOX = webdriver.Firefox
EDGE = webdriver.Edge
IE = webdriver.Ie
OPERA = webdriver.Opera

# URL List
HOME_URL = "https://www.saucedemo.com"
INVENTORY_URL = f"{HOME_URL}/inventory.html"
CART_URL = f"{HOME_URL}/cart.html"
CHECKOUT_INFORMATION_URL = f"{HOME_URL}/checkout-step-one.html"
CHECKOUT_OVERVIEW_URL = f"{HOME_URL}/checkout-step-two.html"
CHECKOUT_COMPLETE_URL = f"{HOME_URL}/checkout-complete.html"

# Titles List
INVENTORY_TITLE = "PRODUCTS"
CART_TITLE = "YOUR CART"
CHECKOUT_INFORMATION_TITLE = "CHECKOUT: YOUR INFORMATION"
CHECKOUT_OVERVIEW_TITLE = "CHECKOUT: OVERVIEW"
CHECKOUT_COMPLETE_TITLE = "CHECKOUT: COMPLETE!"
