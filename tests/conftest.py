from uuid import uuid1
from os import path

import pytest


@pytest.fixture
def non_existent_config_file():
    return str(uuid1())


@pytest.fixture
def invalid_config_file(tmpdir):
    config_file = tmpdir.join('config.yaml')
    config_file.write("""
    request_token_url: 'https://api.twitter.com/oauth/request_token'
    authorize_url: 'https://api.twitter.com/oauth/authorize'
    access_token_url: 'https://api.twitter.com/oauth/access_token'
    base_url: 'https://api.twitter.com/1.1'
    """)
    return path.join(config_file.dirname, config_file.basename)


@pytest.fixture
def valid_config_file(tmpdir):
    config_file = tmpdir.join('config.yaml')
    config_file.write("""
    consumer_key: '<consumer key>'
    consumer_secret: '<consumer secret>'
    request_token_url: 'https://api.twitter.com/oauth/request_token'
    authorize_url: 'https://api.twitter.com/oauth/authorize'
    access_token_url: 'https://api.twitter.com/oauth/access_token'
    base_url: 'https://api.twitter.com/1.1'
    """)
    return path.join(config_file.dirname, config_file.basename)
