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
    request_token, request_token_secret = twitter.get_request_token()

    # Store request token for later use
    with open('.twitter_tokens', 'w') as f:
        contents = yaml.dump({
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
