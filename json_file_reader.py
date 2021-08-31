import json


class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("browser option is not present in the config file")
        return self.data['browser']

    # def get_browser_width(self):
    #     if 'width' not in self.data.keys():
    #         raise Exception("width option is not present in the config file")
    #     return self.data['width']
    #
    # def get_browser_height(self):
    #     if 'height' not in self.data.keys():
    #         raise Exception("height option is not present in the config file")
    #     return self.data['height']

    def get_browser_width(self):
        if 'width' not in self.data.keys():
            return -1
        return self.data['width']

    def get_browser_height(self):
        if 'height' not in self.data.keys():
            return -1
        return self.data['height']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("wait_time option is not present in the config file")
        return int(self.data['wait_time'])

    def get_email(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'email' not in self.data[section_name].keys():
                raise Exception("email option is not present in the config file")
        return self.data[section_name]['email']

    def get_password(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'password' not in self.data[section_name].keys():
                raise Exception("password option is not present in the config file")
        return self.data[section_name]['password']

    def get_username(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'username' not in self.data[section_name].keys():
                raise Exception("username option is not present in the config file")
        return self.data[section_name]['username']

    def get_access_key(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'access_key' not in self.data[section_name].keys():
                raise Exception("access_key option is not present in the config file")
        return self.data[section_name]['access_key']

    def get_os_version(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'os_version' not in self.data[section_name].keys():
                raise Exception("os_version option is not present in the config file")
        return self.data[section_name]['os_version']

    def get_os_name(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'os_name' not in self.data[section_name].keys():
                raise Exception("os_name option is not present in the config file")
        return self.data[section_name]['os_name']

    def get_browser_name(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'browser_name' not in self.data[section_name].keys():
                raise Exception("browser_name option is not present in the config file")
        return self.data[section_name]['browser_name']

    def get_browser_version(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'browser_version' not in self.data[section_name].keys():
                raise Exception("browser_version option is not present in the config file")
        return self.data[section_name]['browser_version']

    def get_build_name(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'build' not in self.data[section_name].keys():
                raise Exception("build option is not present in the config file")
        return self.data[section_name]['build']

    def get_accept_ssl_certs(self, section_name):
        if section_name not in self.data.keys():
            raise Exception(section_name, " section is not present in the config file")
        else:
            if 'accept_ssl_certs' not in self.data[section_name].keys():
                raise Exception("accept_ssl_certs option is not present in the config file")
        return self.data[section_name]['accept_ssl_certs']
