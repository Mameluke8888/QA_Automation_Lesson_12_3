from configparser import  ConfigParser

class IniFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = ConfigParser()
            self.data.read_file(config_file)

    def get_browser(self, section_name):
        value = self.data.get(section_name, 'browser', fallback=None)
        if value is None:
            raise Exception("browser option is not present in the config file")
        return value

    # def get_browser_width(self, section_name):
    #     value = self.data.get(section_name, 'width', fallback=None)
    #     if value is None:
    #         raise Exception("width option is not present in the config file")
    #     return value
    #
    # def get_browser_height(self, section_name):
    #     value = self.data.get(section_name, 'height', fallback=None)
    #     if value is None:
    #         raise Exception("height option is not present in the config file")
    #     return value

    def get_browser_width(self, section_name):
        value = self.data.get(section_name, 'width', fallback=None)
        if value is None:
            value = -1
        return value

    def get_browser_height(self, section_name):
        value = self.data.get(section_name, 'height', fallback=None)
        if value is None:
            value = -1
        return value

    def get_wait_time(self, section_name):
        value = self.data.get(section_name, 'wait', fallback=None)
        if value is None:
            raise Exception("wait_time option is not present in the config file")
        return int(value)

    def get_url(self):
        value = self.data.get('environment', 'url', fallback=None)
        if value is None:
            raise Exception("URL option is not found in environment section")
        return value

    def get_email(self, section_name):
        value = self.data.get(section_name, "email", fallback=None)
        if value is None:
            raise Exception("email option is not found in section ", section_name)
        return value

    def get_password(self, section_name):
        value = self.data.get(section_name, "password", fallback=None)
        if value is None:
            raise Exception("password option is not found in section ", section_name)
        return value

    def get_first_name(self, section_name):
        value = self.data.get(section_name, "first_name", fallback=None)
        if value is None:
            raise Exception("first_name option is not found in section ", section_name)
        return value

    def get_last_name(self, section_name):
        value = self.data.get(section_name, "last_name", fallback=None)
        if value is None:
            raise Exception("last_name option is not found in section ", section_name)
        return value

    def get_address(self, section_name):
        value = self.data.get(section_name, "address", fallback=None)
        if value is None:
            raise Exception("address option is not found in section ", section_name)
        return value

    def get_city(self, section_name):
        value = self.data.get(section_name, "city", fallback=None)
        if value is None:
            raise Exception("city option is not found in section ", section_name)
        return value

    def get_zip(self, section_name):
        value = self.data.get(section_name, "zip", fallback=None)
        if value is None:
            raise Exception("zip option is not found in section ", section_name)
        return value

    def get_country(self, section_name):
        value = self.data.get(section_name, "country", fallback=None)
        if value is None:
            raise Exception("country option is not found in section ", section_name)
        return value

    def get_state(self, section_name):
        value = self.data.get(section_name, "state", fallback=None)
        if value is None:
            raise Exception("state option is not found in section ", section_name)
        return value

    def get_phone(self, section_name):
        value = self.data.get(section_name, "phone", fallback=None)
        if value is None:
            raise Exception("phone option is not found in section ", section_name)
        return value

    def get_order_id(self, section_name):
        value = self.data.get(section_name, "order_id", fallback=None)
        if value is None:
            raise Exception("order_id option is not found in section ", section_name)
        return value

    def get_product_name(self, section_name):
        value = self.data.get(section_name, "product_name", fallback=None)
        if value is None:
            raise Exception("product_name option is not found in section ", section_name)
        return value

    def get_product_code(self, section_name):
        value = self.data.get(section_name, "product_code", fallback=None)
        if value is None:
            raise Exception("product_code option is not found in section ", section_name)
        return value

    def get_quantity(self, section_name):
        value = self.data.get(section_name, "quantity", fallback=None)
        if value is None:
            raise Exception("quantity option is not found in section ", section_name)
        return value

    def get_order_date(self, section_name):
        value = self.data.get(section_name, "order_date", fallback=None)
        if value is None:
            raise Exception("order_date option is not found in section ", section_name)
        return value

    def get_return_reason(self, section_name):
        value = self.data.get(section_name, "reason", fallback=None)
        if value is None:
            raise Exception("reason option is not found in section ", section_name)
        return value

    def get_product_opened(self, section_name):
        value = self.data.get(section_name, "opened", fallback=None)
        if value is None:
            raise Exception("opened option is not found in section ", section_name)
        return value

    def get_subscription(self, section_name):
        value = self.data.get(section_name, "subscribe", fallback=None)
        if value is None:
            raise Exception("subscribe option is not found in section ", section_name)
        return value

    def get_section(self, section_name):
        value = self.data.get(section_name, "section", fallback=None)
        if value is None:
            raise Exception("section option is not found in section ", section_name)
        return value

    def get_subsection(self, section_name):
        value = self.data.get(section_name, "subsection", fallback=None)
        if value is None:
            raise Exception("subsection option is not found in section ", section_name)
        return value

    def get_product(self, section_name):
        value = self.data.get(section_name, "product", fallback=None)
        if value is None:
            raise Exception("product option is not found in section ", section_name)
        return value

    def get_review(self, section_name):
        value = self.data.get(section_name, "review", fallback=None)
        if value is None:
            raise Exception("review option is not found in section ", section_name)
        return value

    def get_rating(self, section_name):
        value = self.data.get(section_name, "rating", fallback=None)
        if value is None:
            raise Exception("rating option is not found in section ", section_name)
        return value

    def get_username(self, section_name):
        value = self.data.get(section_name, "username", fallback=None)
        if value is None:
            raise Exception("username option is not found in section ", section_name)
        return value

    def get_access_key(self, section_name):
        value = self.data.get(section_name, "access_key", fallback=None)
        if value is None:
            raise Exception("access_key option is not found in section ", section_name)
        return value

    def get_os_version(self, section_name):
        value = self.data.get(section_name, "os_version", fallback=None)
        if value is None:
            raise Exception("os_version option is not found in section ", section_name)
        return value

    def get_os_name(self, section_name):
        value = self.data.get(section_name, "os_name", fallback=None)
        if value is None:
            raise Exception("os_name option is not found in section ", section_name)
        return value

    def get_browser_name(self, section_name):
        value = self.data.get(section_name, "browser_name", fallback=None)
        if value is None:
            raise Exception("browser_name option is not found in section ", section_name)
        return value

    def get_browser_version(self, section_name):
        value = self.data.get(section_name, "browser_version", fallback=None)
        if value is None:
            raise Exception("browser_version option is not found in section ", section_name)
        return value

    def get_build_name(self, section_name):
        value = self.data.get(section_name, "build", fallback=None)
        if value is None:
            raise Exception("build option is not found in section ", section_name)
        return value

    def get_accept_ssl_certs(self, section_name):
        value = self.data.get(section_name, "accept_ssl_certs", fallback=None)
        if value is None:
            raise Exception("accept_ssl_certs option is not found in section ", section_name)
        return value