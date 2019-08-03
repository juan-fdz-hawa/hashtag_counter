from urllib.parse import parse_qsl
import re


class HashTag:
    invalid_tag_patter = re.compile(r'[ .,$!"\']')

    def __init__(self, name):
        if HashTag.invalid_tag_patter.search(name):
            raise ValueError('Invalid hash tag!')
        self.name = name
        self.count = 0
        self.refresh_url = None
        self.callbacks = []

    def __str__(self):
        return f'{self.name}\nCount: {self.count}'

    def on_update(self, callback):
        self.callbacks.append(callback)

    def update_count(self, count):
        self.count = count
        for callback in self.callbacks:
            print('Calling callback')
            callback(self)

    @property
    def query(self):
        if self.refresh_url:
            return dict(parse_qsl(self.refresh_url))
        return {
            'url_params': self.name,
            'result_type': 'mixed'
        }
