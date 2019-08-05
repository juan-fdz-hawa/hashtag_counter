from collections import namedtuple
from uuid import uuid1
from os import path

import pytest


class Args:
    def __init__(self, hash_tags):
        self.hash_tags = hash_tags


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


@pytest.fixture
def args_with_many_hash_tags():
    return Args(hash_tags=['1', '2', '3', '4', '5'])


@pytest.fixture
def args_with_duplicated_hash_tags():
    return Args(hash_tags=['1', '2', '2', '2'])


@pytest.fixture
def bad_hash_tags():
    return ['bad one', 'bad.two', 'bad!three', '@badfour', '#bad.six', 'bad_seven']


@pytest.fixture
def good_hash_tags():
    return ['goodone', 'AnotherExample']


@pytest.fixture
def invalid_api_result():
    return {
        'something random': ''
    }


@pytest.fixture
def valid_api_result():
    return {
        'search_metadata': {
            'search_metadata': {
                'refresh_url': 'something',
            },
            'statuses': ['status_1', 'status_2']
        }
    }
