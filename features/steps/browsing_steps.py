from behave import given, when, then
import time

from webelements.browser2 import Browser
from components.header import Header
from config_reader import ConfigReader
from pages.login_page import LoginPage
from components.right_menu import RightMenu
from components.navigation_bar import NavigationBar
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By

URL = "https://techskillacademy.net/brainbucket/index.php"
configs = ConfigReader("config.ini")


@given("user has navigation bar available on home page")
def launch_home_page(context):
    browser = context.browser
    navigation_bar = NavigationBar(browser)
    context.navigation_bar = navigation_bar
    # check that navigation bar is visible and basic content check
    navigation_bar.desktops.wait_until_visible()
    assert navigation_bar.desktops.get_text() == 'Desktops'


@when('user moves to "{section}" in navigation bar')
def open_section_page(context, section):
    navigation_bar = context.navigation_bar
    if section == 'Desktops':
        navigation_bar.move_to_desktops()
    elif section == 'Phones & PDAs':
        navigation_bar.move_to_phones_and_pdas()
    elif section == 'Components':
        navigation_bar.move_to_components()


@when('user clicks on "{option}" of a dropdown menu')
def open_option_page(context, option):
    navigation_bar = context.navigation_bar
    if option == 'Macs':
        navigation_bar.select_mac_desktops()
    elif option == 'PC':
        navigation_bar.select_pcs()
    elif option == 'Phones':
        navigation_bar.select_phones()
    elif option == 'Show All Components':
        navigation_bar.select_all_components()


@then('page with "{product}" is open')
def check_product_page_open(context, product):
    browser = context.browser
    # product page title on a product page
    product_page_title = Element(browser, By.XPATH, "//h2")
    if product == 'Mac desktops':
        assert product_page_title.get_text() == 'Mac'
    elif product == 'PC desktops':
        assert product_page_title.get_text() == 'PC'
    elif product == 'Phones':
        assert product_page_title.get_text() == 'Phones'
    elif product == 'Components':
        assert product_page_title.get_text() == 'Components'
