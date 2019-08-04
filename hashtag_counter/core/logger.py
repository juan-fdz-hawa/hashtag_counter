from os import path
from logging import getLogger, Logger
from logging.config import fileConfig


def get_logger() -> Logger:
    """
    Based on settings inside logger.ini, returns a new Logger instance
    :return: New logger instance
    """
    config_path = path.join(path.dirname(__file__), 'logger.ini')
    fileConfig(config_path)
    return getLogger('HashTagLogger')
