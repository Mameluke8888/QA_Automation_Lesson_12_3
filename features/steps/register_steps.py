from behave import given, when, then
import time

from webelements.browser2 import Browser
from components.header import Header
from config_reader import ConfigReader
from pages.registration_page import RegistrationPage
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By


URL = "https://techskillacademy.net/brainbucket/index.php"
configs = ConfigReader("config.ini")
user_section_name = 'user2'


@given("an unregistered user is on home page")
def launch_login_page(context):
    header = context.header
    header.open_my_account_dropdown()
    # checking that the user is not registered - not logged in - if the user is, the first item in the dropdown changes
    assert header.get_my_account_first_item() == 'Register'


@when("user clicks on Register option of dropdown menu from My Account option in the header")
def open_register_page(context):
    header = context.header
    header.open_registration_form_opened_dropdown()


@when("user fills all fields with personal information")
def enter_register_fields(context):
    # setting up return page
    registration_page = RegistrationPage(context.browser)
    context.registration_page = registration_page

    # filling user info
    registration_page.enter_first_name(configs.get_first_name(user_section_name))
    registration_page.enter_last_name(configs.get_last_name(user_section_name))
    registration_page.enter_email(configs.get_email(user_section_name))
    registration_page.enter_telephone(configs.get_phone(user_section_name))

    registration_page.enter_first_line_address(configs.get_address(user_section_name))
    registration_page.enter_city(configs.get_city(user_section_name))
    registration_page.enter_postcode(configs.get_zip(user_section_name))
    registration_page.select_country(configs.get_country(user_section_name))
    registration_page.select_state(configs.get_state(user_section_name))

    registration_page.enter_password(configs.get_password(user_section_name))
    registration_page.confirm_password(configs.get_password(user_section_name))


@when("user checks Yes/No radiobutton for subscription to the newsletter")
def click_subscription_radiobutton(context):
    registration_page = context.registration_page
    if configs.get_subscription(user_section_name).lower() == "yes":
        registration_page.subscribe_btn.click()
    elif configs.get_subscription(user_section_name).lower() == "no":
        registration_page.unsubscribe_btn.click()


@when("user checks I have read and agree to the Privacy Policy checkbox")
def click_policy_radiobutton(context):
    registration_page = context.registration_page
    registration_page.agree_to_privacy_policy()


@when("user clicks Continue button")
def click_submit_button(context):
    time.sleep(2)
    registration_page = context.registration_page
    registration_page.submit_form()


@then("message \"Your Account Has Been Created!\" or \"E-Mail Address is already registered\" appears")
def check_return_result_page(context):
    browser = context.browser
    registration_confirmation = Element(browser, By.XPATH, '//h1').get_text()
    # # assertion that the message appears that the account is successfully created
    # assert registration_confirmation == 'Your Account Has Been Created!'
    registration_message = Element(browser, By.XPATH, "//*[@class='alert alert-danger' and contains(text(), 'Warning')]").get_text()
    # assertion that the message appears that the account is successfully created or the account has been registered
    print("confirmation:" + registration_confirmation)
    print("message:" + registration_message)
    if 'already' in registration_message:
        assert registration_message == 'Warning: E-Mail Address is already registered!'
    else:
        assert registration_confirmation == 'Your Account Has Been Created!'

