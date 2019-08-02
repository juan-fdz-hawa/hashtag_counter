import pytest

from hastag_counter import Configuration


def test_configuration_with_non_existent_file(non_existent_config_file):
    with pytest.raises(ValueError) as e:
        assert Configuration.from_yaml(non_existent_config_file)
        assert str(e.value) == 'Invalid config path'


def test_configuration_with_invalid_file(invalid_config_file):
    with pytest.raises(ValueError) as e:
        assert Configuration.from_yaml(invalid_config_file)
        assert str(e.value) == 'Invalid config file'


def test_configuration_with_valid_file(valid_config_file):
    result = Configuration.from_yaml(valid_config_file)
    print(result)
    assert result.base_url == 'https://api.twitter.com/1.1'
