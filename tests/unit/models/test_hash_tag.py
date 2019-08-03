from hashtag_counter import HashTag


def test_refresh_url_not_set():
    hash_tag = HashTag('ice_cream')
    assert hash_tag.query == {
        'url_params': 'ice_cream',
        'result_type': 'mixed'
    }