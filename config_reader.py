from json_file_reader import JsonFileReader
from ini_file_reader import IniFileReader


class ConfigReader:
    def __init__(self, filename):
        self.reader = None

        if filename.endswith(".json"):
            self.reader = JsonFileReader(filename)
        elif filename.endswith(".ini"):
            self.reader = IniFileReader(filename)
        else:
            raise Exception("File format is not supported")

    def get_browser(self, section_name):
        return self.reader.get_browser(section_name)

    def get_browser_width(self, section_name):
        return self.reader.get_browser_width(section_name)

    def get_browser_height(self, section_name):
        return self.reader.get_browser_height(section_name)

    def get_wait_time(self, section_name):
        return self.reader.get_wait_time(section_name)

    def get_url(self):
        return self.reader.get_url()

    def get_email(self, section_name):
        return self.reader.get_email(section_name)

    def get_password(self, section_name):
        return self.reader.get_password(section_name)

    def get_first_name(self, section_name):
        return self.reader.get_first_name(section_name)

    def get_last_name(self, section_name):
        return self.reader.get_last_name(section_name)

    def get_address(self, section_name):
        return self.reader.get_address(section_name)

    def get_city(self, section_name):
        return self.reader.get_city(section_name)

    def get_zip(self, section_name):
        return self.reader.get_zip(section_name)

    def get_country(self, section_name):
        return self.reader.get_country(section_name)

    def get_state(self, section_name):
        return self.reader.get_state(section_name)

    def get_phone(self, section_name):
        return self.reader.get_phone(section_name)

    def get_order_id(self, section_name):
        return self.reader.get_order_id(section_name)

    def get_product_name(self, section_name):
        return self.reader.get_product_name(section_name)

    def get_product_code(self, section_name):
        return self.reader.get_product_code(section_name)

    def get_quantity(self, section_name):
        return self.reader.get_quantity(section_name)

    def get_order_date(self, section_name):
        return self.reader.get_order_date(section_name)

    def get_return_reason(self, section_name):
        return self.reader.get_return_reason(section_name)

    def get_product_opened(self, section_name):
        return self.reader.get_product_opened(section_name)

    def get_subscription(self, section_name):
        return self.reader.get_subscription(section_name)

    # for product review
    def get_section(self, section_name):
        return self.reader.get_section(section_name)

    def get_subsection(self, section_name):
        return self.reader.get_subsection(section_name)

    def get_product(self, section_name):
        return self.reader.get_product(section_name)

    def get_review(self, section_name):
        return self.reader.get_review(section_name)

    def get_rating(self, section_name):
        return self.reader.get_rating(section_name)

    # for remote browser configuration like BrowserStack
    def get_username(self, section_name):
        return self.reader.get_username(section_name)

    def get_access_key(self, section_name):
        return self.reader.get_access_key(section_name)

    def get_os_version(self, section_name):
        return self.reader.get_os_version(section_name)

    def get_os_name(self, section_name):
        return self.reader.get_os_name(section_name)

    def get_browser_version(self, section_name):
        return self.reader.get_browser_version(section_name)

    def get_browser_name(self, section_name):
        return self.reader.get_browser_name(section_name)

    def get_build_name(self, section_name):
        return self.reader.get_build_name(section_name)

    def get_accept_ssl_certs(self, section_name):
        return self.reader.get_accept_ssl_certs(section_name)
