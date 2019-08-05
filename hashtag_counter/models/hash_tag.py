import re
from pprint import pprint
from typing import Dict

from urllib.parse import parse_qsl


class HashTag:
    """
    Represents a Twitter hash tags.
    Hash tags can not contain punctuations nor spaces.
    """

    # Hash tags can not have any punctuation nor spaces.
    invalid_tag_patter = re.compile(r'[ ._,$!"\'@]')

    def __init__(self, name):
        """
        Builds a new instance of a HasTag, if an
        invalid name is provided a ValueError will be
        thrown
        :param name: HashTag name
        """
        if HashTag.invalid_tag_patter.search(name):
            raise ValueError('Invalid hash tag!')
        self.name = name
        self.count = 0
        self.refresh_url = None

    def __str__(self):
        return f'{self.name}\nCount: {self.count}'

    def query_params(self) -> Dict[str, str]:
        """
        :return: Query params for the current hash tag
        """
        if self.refresh_url:
            return dict(parse_qsl(self.refresh_url[1:]))
        return {
            'q': f'#{self.name}',
            'result_type': 'mixed'
        }

    def update_from(self, api_result):
        """
        Updates this hash tag based on the given Twitter API
        response
        :param api_result: Response we got from the Twitter API
        :return: New Hash tag with all proper fields updated
        """
        if 'search_metadata' not in api_result:
            raise ValueError('Invalid API result!')

        metadata = api_result['search_metadata']
        refresh_url = metadata['search_metadata']['refresh_url']
        count = len(metadata['statuses'])

        new_hash_tag = HashTag(self.name)
        new_hash_tag.refresh_url = refresh_url
        new_hash_tag.count = self.count + count
        return new_hash_tag
