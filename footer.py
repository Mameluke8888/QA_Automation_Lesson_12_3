from UIElement import UIElement as Element
from selenium.webdriver.common.by import By

# May 23rd, 2021
# student Evgeny Abdulin


class Footer:
    def __init__(self, browser):
        self.extras_title = Element(browser, By.XPATH, "// h5[contains(., 'Information')]")
        self.about_us = Element(browser, By.XPATH, "//a[contains(text(),'About Us')]")
        self.delivery_info = Element(browser, By.XPATH, "//a[contains(text(),'Delivery Information')]")
        self.privacy_policy = Element(browser, By.XPATH, "//a[contains(text(),'Privacy Policy')]")
        self.terms_conditions = Element(browser, By.XPATH, "//a[contains(text(),'Terms & Conditions')]")

        self.extras_title = Element(browser, By.XPATH, "// h5[contains(., 'Customer Service')]")
        self.contact_us = Element(browser, By.XPATH, "//a[contains(text(),'Contact Us')]")
        self.returns = Element(browser, By.XPATH, "//a[contains(text(),'Returns')]")
        self.site_map = Element(browser, By.XPATH, "//a[contains(text(),'Site Map')]")

        self.extras_title = Element(browser, By.XPATH, "// h5[contains(., 'Extras')]")
        self.brands = Element(browser, By.XPATH, "//a[contains(text(),'Brands')]")
        self.gift_certificates = Element(browser, By.XPATH, "//a[contains(text(),'Gift Certificates')]")
        self.affiliates = Element(browser, By.XPATH, "//a[contains(text(),'Affiliates')]")

        self.extras_title = Element(browser, By.XPATH, "// h5[contains(., 'My Account')]")
        self.my_account = Element(browser, By.XPATH, "//a[contains(text(),'My Account')]")
        self.order_history = Element(browser, By.XPATH, "//a[contains(text(),'Order History')]")
        self.wish_list = Element(browser, By.XPATH, "//a[contains(text(),'Wish List')]")
        self.newsletter = Element(browser, By.XPATH, "//a[contains(text(),'Newsletter')]")

        self.opencart_ext_link = Element(browser, By.XPATH, "//a[contains(text(),'OpenCart')]")

    def click_about_us(self):
        self.about_us.click()

    def click_delivery_info (self):
        self.delivery_info .click()

    def click_privacy_policy(self):
        self.privacy_policy.click()

    def click_terms_conditions(self):
        self.terms_conditions.click()

    def click_contact_us(self):
        self.contact_us.click()

    def click_returns(self):
        self.returns.click()

    def click_site_map(self):
        self.site_map.click()

    def click_brands(self):
        self.brands.click()

    def click_gift_certificates(self):
        self.gift_certificates.click()

    def click_my_account(self):
        self.my_account.click()

    def click_order_history(self):
        self.order_history.click()

    def click_wish_list(self):
        self.wish_list.click()

    def click_newsletter(self):
        self.newsletter.click()

    def click_opencart_ext_link(self):
        self.opencart_ext_link.click()
