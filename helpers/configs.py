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
    def get_aws_access_key_id():
        return os.environ['AWS_ACCESS_KEY_ID']

    @staticmethod
    def get_aws_secret_access_key():
        return os.environ['AWS_ACCESS_KEY']

    @staticmethod
    def get_app_configs():
        with open("app_config.yaml", "r") as f:
            config = yaml.safe_load(f)
        return config
