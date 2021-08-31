from components.header import Header
from components.right_menu import RightMenu
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By
from webelements.dropdown2 import Dropdown

# May 23rd, 2021
# student Evgeny Abdulin


class ReturnPage:
    def __init__(self, browser):
        self.browser = browser
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)

        self.title = Element(browser, By.XPATH, "//*[@id='content']/h1")
        self.first_name_input = Element(browser, By.NAME, "firstname")
        self.last_name_input = Element(browser, By.NAME, "lastname")
        self.email_input = Element(browser, By.NAME, "email")
        self.telephone_input = Element(browser, By.NAME, "telephone")
        self.order_id_input = Element(browser, By.NAME, "order_id")
        self.order_date_input = Element(browser, By.NAME, "date_ordered")
        self.product_name_input = Element(browser, By.NAME, "product")
        self.product_code_input = Element(browser, By.NAME, "model")
        self.quantity_input = Element(browser, By.NAME, "quantity")
        self.return_reason = None

        self.opened_yes_radiobutton = Element(browser, By.XPATH, "//input[@name='opened' and @value='1']")
        self.opened_no_radiobutton = Element(browser, By.XPATH, "//input[@name='opened' and @value='0']")
        self.submit_button = Element(browser, By.XPATH, "//input[@value='Submit']")

    def get_form_title(self):
        return self.title.get_text(wait=True)

    def enter_first_name(self, text):
        self.first_name_input.enter_text(text)

    def enter_last_name(self, text):
        self.last_name_input.enter_text(text)

    def enter_email(self, text):
        self.email_input.enter_text(text)

    def enter_telephone(self, text):
        self.telephone_input.enter_text(text)

    def enter_order_id(self, text):
        self.order_id_input.enter_text(text)

    def enter_order_date(self, text):
        self.order_date_input.enter_text(text)

    def enter_product_name(self, text):
        self.product_name_input.enter_text(text)

    def enter_product_code(self, text):
        self.product_code_input.enter_text(text)

    def enter_quantity(self, text):
        self.quantity_input.enter_text(text)

    def return_reason_click(self, text):
        self.return_reason = Element(self.browser, By.XPATH, "//label[contains(.,\'" + text + "\')]")
        self.return_reason.click()

    def opened_yes_click(self):
        self.opened_yes_radiobutton.click()

    def opened_no_click(self):
        self.opened_no_radiobutton.click()

    def submit_form(self):
        self.submit_button.submit()








