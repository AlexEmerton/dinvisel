import os
import yaml


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

    @staticmethod
    def get_app_configs():
        with open("app_config.yaml", "r") as f:
            config = yaml.safe_load(f)
        return config
