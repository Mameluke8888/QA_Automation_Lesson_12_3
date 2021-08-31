from behave import given, when, then
import time

from webelements.browser2 import Browser
from components.header import Header
from config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from components.right_menu import RightMenu
from components.navigation_bar import NavigationBar
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By

user_section_name = 'user2'
review_section_name = 'review2'


@given('from home page user selects product(s) to leave a review for using navigation bar and dropdown menus')
def select_product(context):
    configs = context.configs
    context.execute_steps(
        '''
        Given user has navigation bar available on home page
        When user moves to "''' + configs.get_section(review_section_name) + '''" in navigation bar
        When user clicks on "''' + configs.get_subsection(review_section_name) + '''" of a dropdown menu
        '''
    )


@given('user opens a page with the product(s) to leave a review for')
def open_product_page(context):
    browser = context.browser
    configs = context.configs
    # product on the page
    product = Element(browser, By.XPATH, "//a[contains(text(),'" + configs.get_product(review_section_name) + "')]")
    product.wait_until_visible()
    product.click()


@when('user clicks on Review tab')
def open_review_tab(context):
    browser = context.browser
    product_page = ProductPage(browser)
    context.product_page = product_page
    product_page.click_review_link()


@when('user enters his/her name in a corresponding field')
def enter_name(context):
    product_page = context.product_page
    configs = context.configs
    product_page.enter_review_name("{} {}".format(configs.get_first_name(user_section_name),
                                                  configs.get_last_name(user_section_name)))


@when('user types in a text from 25 to 1000 characters long of a review in a corresponding field')
def enter_review(context):
    product_page = context.product_page
    configs = context.configs
    product_page.enter_review_text(configs.get_review(review_section_name))


@when('user rates the product Bad...Good by clicking corresponding radiobutton')
def click_rate_radiobutton(context):
    product_page = context.product_page
    configs = context.configs
    product_page.check_rating_radiobutton(configs.get_rating(review_section_name))


@when('user submits the review by clicking Continue button')
def click_continue_button(context):
    product_page = context.product_page
    time.sleep(2)
    product_page.click_continue_button()


@then('message \"Thank you for your review. It has been submitted to the webmaster for approval\" appears')
def check_review_message(context):
    browser = context.browser
    product_page = context.product_page
    # review_message = product_page.review_message.get_text()
    # review_message = Element(browser, By.XPATH, "//form[@id='form-review']/div[2]").get_text()
    review_message = Element(browser, By.XPATH, "//div[@class='alert alert-success']").get_text()
    print(review_message)
    assert review_message == "Thank you for your review. It has been submitted to the webmaster for approval."

