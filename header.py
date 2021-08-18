from browser import Browser
from UIElement import UIElement as Element
from selenium.webdriver.common.by import By

# May 20th, 2021
# student Evgeny Abdulin

class Header:
    def __init__(self, browser):
        self.browser = browser
        self.my_account_btn = Element(browser, By.XPATH, "//a[@title='My Account']")
        self.my_account_dropdown = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']")
        self.register_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[1]")
        self.login_btn = Element(browser, By.XPATH, "//*[@class='dropdown-menu dropdown-menu-right']/li[2]")
        self.wish_list_btn = Element(browser, By.ID, "wishlist-total")
        self.shopping_list_btn = Element(browser, By.XPATH, "//a[@title='Shopping Cart']")
        self.checkout_btn = Element(browser, By.XPATH, "//a[@title='Checkout']")
        self.currency_btn = Element(browser, By.ID, "form-currency")
        # added to have it in __init__
        self.currency_option = Element(browser, By.NAME, "EUR")
        self.logo = Element(browser, By.ID, "logo")
        # changed locator
        self.search = Element(browser, By.NAME, "search")
        # added
        self.search_btn = Element(browser, By.XPATH, "//div[@id='search']/span/button")

    def verify_logo_is_visible(self):
        return self.logo.wait_until_visible()

    def open_registration_form(self):
        self.my_account_btn.click()
        self.my_account_dropdown.wait_until_visible()
        self.register_btn.click()

    def open_login_page(self):
        self.my_account_btn.click()
        self.my_account_dropdown.wait_until_visible()
        self.login_btn.click()

    def change_currency(self, new_currency):
        # options for new_currency: EUR, GBP, USD
        self.currency_btn.click()
        self.currency_option.wait_until_visible()
        self.currency_option = Element(self.browser, By.NAME, new_currency.upper())
        self.currency_option.click()

    def open_wishlist(self):
        self.wish_list_btn.click()

    def search_for(self, text):
        self.search.enter_text(text)
        self.search_btn.click()
