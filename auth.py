"""
Small web app used for authorizing hashtag_counter
to use the Twitter API using the credentials provided
in config.yaml
"""

import yaml

from flask import Flask
from rauth import OAuth1Service
from os import path

from hashtag_counter import Configuration

app = Flask(__name__)

config_file = path.join('.', 'config.yaml')
config = Configuration.from_yaml(config_file)

twitter = OAuth1Service(**config.__dict__)


@app.route('/')
def home():
    """
    After hitting the home end point (/) a config file (.twitter_tokens)
    will be created with your request_token and your request_token_secrect.
    Keep this file! This file will be used later on by the Requester for
    hitting the API search end point.
    :return: twitter_auth.html template.
    """
    request_token, request_token_secret = twitter.get_request_token()
    _store_tokens(request_token, request_token_secret)
    template = _get_template(request_token)
    return template


def _get_template(request_token):
    auth_url = twitter.get_authorize_url(request_token)
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>HashTag Counter</title>
    </head>
    <body>
    <a href="{auth_url}"> Click here to authorize </a>
    </body>
    </html>
    """


def _store_tokens(request_token, request_token_secret):
    with open('.twitter_tokens', 'w') as f:
        contents = yaml.dump({
            'request_token': request_token,
            'request_token_secret': request_token_secret
        }, default_flow_style=False)
    f.write(contents)


@app.route('/callback')
def callback():
    return 'All done!, feel free to close this window'


app.run(host='localhost', port=3000)
