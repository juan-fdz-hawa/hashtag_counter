import pytest
from unittest.mock import Mock

from hashtag_counter import HashTag


def test_name_must_not_have_spaces_nor_punctuation(bad_hash_tags, good_hash_tags):
    with pytest.raises(ValueError) as e:
        assert [HashTag(tag) for tag in bad_hash_tags]
    assert str(e.value) == 'Invalid hash tag!'
    assert [HashTag(tag) for tag in good_hash_tags]


def test_refresh_url_not_set():
    hash_tag = HashTag('ice_cream')
    assert hash_tag.query == {
        'url_params': 'ice_cream',
        'result_type': 'mixed'
    }


def test_to_str():
    hash_tag = HashTag('food')
    hash_tag.count = 100
    assert str(hash_tag) == f'{hash_tag.name}\nCount: {hash_tag.count}'
