import re
from typing import Dict

from urllib.parse import parse_qsl


class HashTag:
    """
    Represents a Twitter hash tags.
    Hash tags can not contain punctuations nor spaces.
    """

    # Hash tags can not have any punctuation nor spaces.
    invalid_tag_patter = re.compile(r'[ .,$!"\']')

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

    @property
    def query(self) -> Dict[str, str]:
        """
        Query string params of the given tag
        :return:
        """
        if self.refresh_url:
            return dict(parse_qsl(self.refresh_url))
        return {
            'url_params': self.name,
            'result_type': 'mixed'
        }
