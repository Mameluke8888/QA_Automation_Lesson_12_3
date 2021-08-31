from components.header import Header
from components.right_menu import RightMenu
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")
        self.new_customer_title = Element(browser, By.XPATH, "//h2[contains(text(), 'New Customer')]")
        self.returning_customer_title = Element(browser, By.XPATH, "//h2[contains(text(), 'Returning Customer')]")
        self.email_input = Element(browser, By.ID, "input-email")
        self.password_input = Element(browser, By.ID, "input-password")
        self.login_button = Element(browser, By.XPATH, "//input[@value='Login']")

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()

    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()

    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()

    def get_new_customer_title(self):
        return self.new_customer_title.get_text()

    def get_returning_customer_title(self):
        return self.returning_customer_title.get_text()

    def enter_email(self, email):
        self.email_input.enter_text(email)

    def enter_password(self, password):
        self.password_input.enter_text(password)

    def click_login_button(self):
        self.login_button.click()

        