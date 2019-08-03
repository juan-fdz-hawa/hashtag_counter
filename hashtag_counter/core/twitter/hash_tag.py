from urllib.parse import parse_qsl


class HashTag:
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.refresh_url = None

    @property
    def query(self):
        if self.refresh_url:
            return dict(parse_qsl(self.refresh_url))
        return {
            'url_params': self.name,
            'result_type': 'mixed'
        }
