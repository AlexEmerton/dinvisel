import os


class ConfigParser:

    @staticmethod
    def get_token():
        return os.environ['TOKEN']

    @staticmethod
    def get_port():
        return int(os.environ.get('PORT', '8443'))

    @staticmethod
    def get_app_name():
        return 'https://dinvisel.herokuapp.com/'
