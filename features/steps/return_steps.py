from behave import given, when, then
import time

from webelements.browser2 import Browser
from components.header import Header
from components.footer import Footer
from config_reader import ConfigReader
from pages.return_page import ReturnPage
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By


URL = "https://techskillacademy.net/brainbucket/index.php"
configs = ConfigReader("config.ini")
user_section_name = 'user2'
order_section_name = 'order2'


@given("user opens return request form by clicking on Returns option in the footer")
def open_return_page(context):
    footer = Footer(context.browser)
    context.footer = footer
    footer.click_returns()


@when("user fills all fields with order and product information")
def enter_return_fields(context):
    # setting up return page
    return_page = ReturnPage(context.browser)
    context.return_page = return_page

    # filling user info
    return_page.enter_first_name(configs.get_first_name(user_section_name))
    return_page.enter_last_name(configs.get_last_name(user_section_name))
    return_page.enter_email(configs.get_email(user_section_name))
    return_page.enter_telephone(configs.get_phone(user_section_name))

    # filling order info
    return_page.enter_order_id(configs.get_order_id(order_section_name))
    return_page.enter_product_name(configs.get_product_name(order_section_name))
    return_page.enter_product_code(configs.get_product_code(order_section_name))
    return_page.enter_quantity(configs.get_quantity(order_section_name))
    return_page.enter_order_date(configs.get_order_date(order_section_name))


@when("user indicates a reason for return by clicking a corresponding radiobutton in Reason for Return section")
def click_reason_radiobutton(context):
    return_page = context.return_page
    return_page.return_reason_click(configs.get_return_reason(order_section_name))


@when("user indicates whether the product was opened by clicking a corresponding radiobutton")
def click_opened_radiobutton(context):
    return_page = context.return_page
    if configs.get_product_opened(order_section_name).lower() == "yes":
        return_page.opened_yes_click()
    elif configs.get_product_opened(order_section_name).lower() == "no":
        return_page.opened_no_click()


@when("user clicks Submit button")
def click_submit_button(context):
    time.sleep(2)
    return_page = context.return_page
    return_page.submit_form()


@then("message \"Thank you for submitting your return request...\" appears")
def check_return_result_page(context):
    browser = context.browser
    return_request_message = Element(browser, By.XPATH, "//div[@id='content']/p[2]")
    # assertion that the message appears that the return request is successfully sent
    assert return_request_message.get_text() == 'You will be notified via e-mail as to the status of your request.'
