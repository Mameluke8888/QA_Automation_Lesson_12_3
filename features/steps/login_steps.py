from behave import given, when, then
import time

from webelements.browser2 import Browser
from components.header import Header
from config_reader import ConfigReader
from pages.login_page import LoginPage
from components.right_menu import RightMenu
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By


URL = "https://techskillacademy.net/brainbucket/index.php"
configs = ConfigReader("config.ini")
user_section_name = 'user2'


@given("registered user who is not logged in has home page opened in a browser")
def launch_login_page(context):
    header = context.header
    header.open_my_account_dropdown()
    login_page = LoginPage(context.browser)
    context.login_page = login_page
    # checking that the user is  not logged in - if the user is, the first item in the dropdown changes
    assert header.get_my_account_first_item() == 'Register'


@given("user clicks on Login option of My Account dropdown menu in the header")
def open_login_page(context):
    header = context.header
    header.open_login_page_opened_dropdown()


@given("user clicks on Register option of My Account dropdown menu in the header")
def enter_register_page(context):
    header = context.header
    header.open_registration_form_opened_dropdown()


@given("user clicks on Login option in the right menu")
def open_login_page_right_menu(context):
    right_menu = RightMenu(context.browser)
    context.right_menu = right_menu
    right_menu.click_login()


@when("user enters correct both email address and password in the corresponding fields")
def enter_correct_both_email_password(context):
    login_page = context.login_page
    login_page.enter_email(configs.get_email(user_section_name))
    login_page.enter_password(configs.get_password(user_section_name))


@when("user enters incorrect email address and correct password in the corresponding fields")
def enter_incorrect_email_correct_password(context):
    login_page = context.login_page
    login_page.enter_email("1" + configs.get_email(user_section_name))
    login_page.enter_password(configs.get_password(user_section_name))


@when("user enters registered email address but incorrect password in the corresponding fields")
def enter_correct_email_incorrect_password(context):
    login_page = context.login_page
    login_page.enter_email(configs.get_email(user_section_name))
    login_page.enter_password("1" + configs.get_password(user_section_name))


@when("user clicks Login button")
def enter_correct_both_email_password(context):
    login_page = context.login_page
    login_page.click_login_button()


@then("user account page is open")
def check_account_page_open(context):
    browser = context.browser
    login_message = Element(browser, By.XPATH, "//h2[contains(text(), 'My Account')]")
    # assertion that the message appears that the return request is successfully sent
    login_message.wait_until_visible()


@then("message \"Warning: No match for E-Mail Address and/or Password.\" appears")
def check_warning_message(context):
    browser = context.browser
    login_message = Element(browser, By.XPATH, "//*[@class='alert alert-danger' and contains(text(), 'Warning')]")
    # assertion that the message appears that typed in credentials are not match with the registered data
    assert login_message.get_text() == 'Warning: No match for E-Mail Address and/or Password.'

