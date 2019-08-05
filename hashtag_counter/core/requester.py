from typing import Tuple

from rauth import OAuth1Service

from hashtag_counter import Configuration, HashTag


class Requester:
    """
    The requester is in charge of hitting the search endpoint,
    using the values on the config file, the twitter request tokens and the provided
    hash tag instance.
    """
    def __init__(self, twitter_config_path: str, tokens_config_path: str):
        self._twitter_config = Configuration.from_yaml(twitter_config_path)

        self._twitter = OAuth1Service(**self._twitter_config.__dict__)
        self._tokens = Configuration.from_yaml(tokens_config_path)

    def do_search(self, hash_tag: HashTag) -> Tuple[str, dict]:
        """
        Performs a search of the provided hash tag using the Twitter API.
        :param hash_tag:
        :return: A tuple of (hash_tag.name, response.json)
        """
        request_token, request_token_secret = self._tokens
        session = self._twitter.get_auth_session(request_token, request_token_secret)

        search_endpoint = f'{self._twitter_config.base_url}/search/tweets.json'
        response = session.get(search_endpoint, params=hash_tag.query_params())

        return hash_tag.name, (response.json())
