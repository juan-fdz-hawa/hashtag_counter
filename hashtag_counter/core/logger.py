from os import path
from logging import getLogger
from logging.config import fileConfig


def get_logger():
    config_path = path.join(path.dirname(__file__), 'logger.ini')
    fileConfig(config_path)
    return getLogger('HashTagLogger')
