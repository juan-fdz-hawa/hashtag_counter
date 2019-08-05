from typing import Tuple

from twython import Twython

from hashtag_counter import Configuration, HashTag


class Requester:
    """
    The requester is in charge of hitting the search endpoint,
    using the values on the config file, the twitter request tokens and the provided
    hash tag instance.
    """

    def __init__(self, config_path: str):
        config = Configuration.from_yaml(config_path)

        twitter = Twython(config.consumer_key, config.consumer_secret, oauth_version=2)
        access_token = twitter.obtain_access_token()
        self._api = Twython(config.consumer_key, access_token=access_token)

    def do_search(self, hash_tag: HashTag) -> Tuple[str, dict]:
        """
        Performs a search of the provided hash tag using the Twitter API.
        :param hash_tag:
        :return: A tuple of (hash_tag.name, response.json)
        """
        result = self._api.search(**hash_tag.query_params())
        return hash_tag.name, {'search_metadata': result}
