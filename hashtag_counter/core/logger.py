from os import path
from logging import getLogger, Logger
from logging.config import fileConfig


def get_logger() -> Logger:
    """
    Creates a new Logger from the settings inside logger.ini.
    :return: New logger instance
    """
    config_path = path.join(path.dirname(__file__), 'logger.ini')
    fileConfig(config_path)
    return getLogger('HashTagLogger')
