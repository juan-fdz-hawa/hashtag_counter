import yaml

from os import path
from typing import Dict
from .required_fields import required_fields


class Configuration:
    """
    Represents a configuration file.
    A configuration file can be build from many sources
    (right now only yaml file is supported) and a configuration
    file has a series of required properties (checked by the
    _config_is_valid method).
    """

    @staticmethod
    def _config_is_valid(config_path: str, config: Dict[str, str]) -> bool:
        """
        Based on the rules contained inside rquired_fileds[config_path],
        check that the provided config contains all required files.
        :param config_path: filepath of the config file loaded
        :param config: config fields loaded
        :return: Whether provided config is valid or not
        """
        required = required_fields[path.basename(config_path)]
        config_fields = set(config.keys())
        return config_fields.issuperset(required)

    @classmethod
    def from_yaml(cls, config_path: str):
        """
        Parses and loads the YAML config file based
        on the provided file path
        :param config_path: Config file path
        :return: Configuration object if file exists and
        if file contains all required fields, otherwise
        raises ValueError
        """
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
