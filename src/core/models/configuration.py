from os import path
from typing import Dict

import yaml


class Configuration:

    @staticmethod
    def _config_is_valid(config: Dict[str, str]) -> bool:
        required_fields = {'consumer_key', 'consumer_secret', 'request_token_url', 'authorize_url', 'access_token_url',
                           'api_version', 'search_endpoint'}
        config_fields = {k for k in config.keys()}
        return config_fields.issuperset(required_fields)

    @classmethod
    def from_yaml(cls, config_path):
        if path.isfile(config_path):
            with open(config_path, 'r') as f:
                config = yaml.load(f)
                if cls._config_is_valid(config):
                    return cls(**config)
                raise ValueError('Invalid config file')
        raise ValueError('Invalid config path')

    def __init__(self, **kwargs):
        for prop, val in kwargs.items():
            setattr(self, prop, val)
