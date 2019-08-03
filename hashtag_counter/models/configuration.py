import yaml

from os import path
from typing import Dict
from .required_fields import required_fields


class Configuration:

    @staticmethod
    def _config_is_valid(config_path: str, config: Dict[str, str]) -> bool:
        required = required_fields[path.basename(config_path)]
        config_fields = set(config.keys())
        return config_fields.issuperset(required)

    @classmethod
    def from_yaml(cls, config_path: str):
        if not path.isfile(config_path):
            raise ValueError('Invalid config path')
        with open(config_path, 'r') as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
            if cls._config_is_valid(config_path, config):
                return cls(**config)
            raise ValueError('Invalid config file')

    def __init__(self, **kwargs):
        for prop, val in kwargs.items():
            setattr(self, prop, val)
