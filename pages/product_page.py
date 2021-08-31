from components.header import Header
from components.right_menu import RightMenu
from webelements.UIElement3 import UIElement as Element
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, browser):
        self.browser = browser
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.product_name = Element(browser, By.XPATH, "//h1")
        self.description_tab = Element(browser, By.XPATH, "//a[contains(text(),'Description')]")
        self.review_tab = Element(browser, By.XPATH, "//a[contains(text(),'Reviews')]")
        self.review_link = Element(browser, By.XPATH, "//a[contains(text(),'Write a review')]")
        self.add_to_cart_button = Element(browser, By.ID, "button-cart")
        self.quantity = Element(browser, By.ID, "input-quantity")
        self.add_to_wishlist_button = Element(browser, By.XPATH, "(//button[@type='button'])[9]")
        self.compare_button = Element(browser, By.XPATH, "(//button[@type='button'])[10]")
        self.review_name = Element(browser, By.ID, "input-name")
        self.review_text = Element(browser, By.ID, "input-review")
        self.review_continue_button = Element(browser, By.ID, "button-review")
        self.review_rating_radiobutton = Element(browser, By.XPATH, "(//input[@ name='rating'])[1]")
        self.review_message = Element(browser, By.XPATH, "//form[@id='form-review']/div[2]")
        self.price = Element(browser, By.XPATH, "//li/h2")
        self.stars_rating = Element(browser, By.XPATH, "(//i[@class='fa fa-star-o fa-stack-1x'])[1]")
        self.image = Element(browser, By.XPATH, "(//img[@alt='" + self.product_name.get_text() + "'])[1]")

    def get_product_name(self):
        return self.product_name

    def click_description_tab(self):
        self.description_tab.click()

    def click_review_tab(self):
        self.review_tab.click()

    def click_review_link(self):
        self.review_link.click()

    def click_add_to_cart_button(self):
        self.add_to_cart_button.click()

    def click_continue_button(self):
        self.review_continue_button.click()

    def enter_quantity(self, text):
        self.quantity.enter_text(text)

    def enter_review_name(self, text):
        self.review_name.enter_text(text)

    def enter_review_text(self, text):
        self.review_text.enter_text(text)

    def check_rating_radiobutton(self, rating):
        # rating is an integer from 1 to 5, 1 = bad, 5 = good
        self.review_rating_radiobutton = Element(self.browser, By.XPATH,
                                                 "(//input[@ name='rating'])[" + str(rating) + "]")
        self.review_rating_radiobutton.click()

    def get_rating_star(self, star_number):
        # star is an integer from 1 to 5 to get
        # stars rating is for indication only, non-clickable in the current version of the website
        self.stars_rating = Element(self.browser, By.XPATH,
                                    "(//i[@class='fa fa-star-o fa-stack-1x'])[" + str(star_number) + "]")
        # returning a link to a star object for further processing like checks how many stars are checked etc.
        return self.stars_rating

    def get_image(self, image_number):
        self.image = Element(self.browser, By.XPATH,
                             "(//img[@alt='" + self.product_name.get_text() +
                             "'])[" + str(image_number) + "]")
        return self.image

    def click_image(self, image_number):
        self.get_image(image_number).click()
