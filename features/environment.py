import time

import sys
from os.path import abspath
sys.path.append(abspath('../'))

from config_reader import ConfigReader
from webelements.browser2 import Browser
from webelements.UIElement3 import UIElement as Element
from components.header import Header
from selenium.webdriver.common.by import By


def before_all(context):
    configs = ConfigReader("config.ini")
    context.configs = configs


def before_scenario(context, scenario):
    section = 'environment'
    configs = context.configs
    browser = Browser(configs.get_url(), configs.get_browser(section), configs.get_wait_time(section), scenario)
    context.browser = browser
    header = Header(context.browser)
    context.header = header
    # checking the user is on Brainbucket website, the logo is visible
    header.logo.wait_until_visible()
    # checking the user is on home page, the slideshow is visible
    slideshow = Element(browser, By.ID, "slideshow0")
    slideshow.wait_until_visible()


def after_scenario(context, scenario):
    browser = context.browser
    time.sleep(2)
    browser.shutdown()

