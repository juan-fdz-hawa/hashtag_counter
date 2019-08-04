"""
Small web app used for authorizing hashtag_counter
to use the Twitter API using the credentials provided
in config.yaml
"""

import yaml

from flask import Flask, render_template
from rauth import OAuth1Service
from os import path

from hashtag_counter import Configuration

app = Flask(__name__, template_folder='.')

auth_dir = path.dirname(path.abspath(__file__))
base_dir = path.join(auth_dir, '..', '..')

config_file = path.join(base_dir, 'config.yaml')
config = Configuration.from_yaml(config_file)

twitter = OAuth1Service(**config.__dict__)


@app.route('/')
def home():
    """
    After hitting the home end point (/) a config file (.twitter_tokens)
    will be created with your request_token and your request_token_secrect.
    Keep this file! This file is used for other parts of the app (you can always
    create it by going to the home endpoint).
    :return: twitter_auth.html template.
    """
    request_token, request_token_secret = twitter.get_request_token()

    # Store request token for later use
    with open('.twitter_tokens', 'w') as f: contents = yaml.dump({
        'request_token': request_token,
        'request_token_secret': request_token_secret
    }, default_flow_style=False)
    f.write(contents)

    auth_url = twitter.get_authorize_url(request_token)
    return render_template('twitter_auth.html', link=auth_url)


@app.route('/callback')
def callback():
    return 'All done!, feel free to close this window'


app.run(host='localhost', port=3000)
