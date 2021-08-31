from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from config_reader import ConfigReader
from pprint import pprint

remote_section_name = 'remote'
environment_section_name = 'environment'

class Browser:
    """
    This class is wrapper around Selenium driver
    """
    # Exercise  # 1
    # Add to Browser 's initialization method an exception handling that will print out
    # the executable path to the driver is incorrect
    def __init__(self, url, browser_name="", time_wait=10, scenario=""):
        # decide which browser to open, can be extended
        configs = ConfigReader("config.ini")
        # comment next 2 lines, uncomment try-except section below to read configurable values of size of browser window
        browser_width = -1
        browser_height = -1
        try:
            browser_width = configs.get_browser_width(environment_section_name)
            browser_height = configs.get_browser_height(environment_section_name)
        except Exception:
            browser_width = -1
            browser_height = -1
        try:
            if browser_name.lower() == "firefox":
                self.driver = webdriver.Firefox(executable_path='../../drivers/geckodriver')
                self.driver.maximize_window()
            elif browser_name.lower() == 'chrome':
                options = webdriver.ChromeOptions()
                # setting size of browser window if values are provided
                if (browser_width != -1) and (browser_height != -1):
                    options.add_argument("--window-size={},{}".format(browser_width, browser_height))
                # testing desired capabilities, maximization doesn't work on my Mac
                # options.add_argument("--start-maximized")
                # options.add_argument("--window-size=360,800")
                options.add_argument("--incognito")
                options.add_experimental_option("excludeSwitches", ['enable-automation'])
                self.driver = webdriver.Chrome(executable_path='../../drivers/chromedriver', options=options)
                if (browser_width == -1) or (browser_height == -1):
                    self.driver.maximize_window()
                # self.driver = webdriver.Chrome(executable_path='drivers/chromedriver', desired_capabilities={"chromeOptions": {"binary": 'mycefapp.exe'}})
            elif browser_name.lower() == 'remote':
                username = configs.get_username(remote_section_name)
                access_key = configs.get_access_key(remote_section_name)
                desired_cap = {
                    'os_version': configs.get_os_version(remote_section_name),
                    'os': configs.get_os_name(remote_section_name),
                    'browser': configs.get_browser_name(remote_section_name),
                    'browser_version': configs.get_browser_version(remote_section_name),
                    'name': scenario.name,  # test name
                    'build': configs.get_build_name(remote_section_name),  # Your tests will be organized within this build
                    'acceptSslCerts': configs.get_accept_ssl_certs(remote_section_name)
                               }
                # pprint(desired_cap)
                self.driver = webdriver.Remote(
                    command_executor='https://' + username + ':' + access_key + '@hub-cloud.browserstack.com/wd/hub',
                    desired_capabilities=desired_cap)

        except WebDriverException as err:
            print("Incorrect path to WebDriver:", err)
            raise

        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        # self.driver.maximize_window()
        self.driver.implicitly_wait(time_wait)

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()
