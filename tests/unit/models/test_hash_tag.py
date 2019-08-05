import pytest

from hashtag_counter import HashTag


def test_name_must_not_have_spaces_nor_punctuation(bad_hash_tags, good_hash_tags):
    for tag in bad_hash_tags:
        with pytest.raises(ValueError) as e:
            assert HashTag(tag)
        assert str(e.value) == 'Invalid hash tag!'
    for tag in good_hash_tags:
        assert HashTag(tag)


def test_query_params_refresh_url_not_set():
    hash_tag = HashTag('coffee')
    assert hash_tag.query_params() == {
        'q': '#coffee',
        'result_type': 'mixed'
    }


def test_query_params_refresh_url_set():
    hash_tag = HashTag('coffee')
    hash_tag.refresh_url = '?since_id=963341767532834817&q=%23coffee&result_type=mixed&include_entities=1'
    assert hash_tag.query_params() == {
        'since_id': '963341767532834817',
        'q': '#coffee',
        'result_type': 'mixed',
        'include_entities': '1'
    }


def test_to_str():
    hash_tag = HashTag('food')
    hash_tag.count = 100
    assert str(hash_tag) == f'{hash_tag.name}\nCount: {hash_tag.count}'


def test_update_from_result_invalid_api_result(invalid_api_result):
    hash_tag = HashTag('milk')

    with pytest.raises(ValueError) as ex:
        hash_tag.update_from(invalid_api_result)
    assert str(ex.value) == 'Invalid API result!'


def test_update_from_result_valid_api_result(valid_api_result):
    hash_tag = HashTag('milk')
    result = hash_tag.update_from(valid_api_result)

    assert result.name == 'milk'
    assert result.refresh_url == valid_api_result['search_metadata']['search_metadata']['refresh_url']
    assert result.count == len(valid_api_result['search_metadata']['statuses'])
