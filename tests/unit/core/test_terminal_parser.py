from unittest.mock import Mock

from hashtag_counter.core.terminal_parser import process_args


def test_process_args_with_duplicate_hash_tags(args_with_duplicated_hash_tags):
    logger = Mock()
    result = process_args(args_with_duplicated_hash_tags, logger)

    logger.info.assert_called_once_with('Duplicated hash tags detected! Only taking unique values')
    assert list({k for k in args_with_duplicated_hash_tags.hash_tags}) == result.hash_tags


def test_process_args_with_many_hash_tags(args_with_many_hash_tags):
    logger = Mock()
    result = process_args(args_with_many_hash_tags, logger)

    logger.info.assert_called_once_with('Too many hash tags! Only taking the first 4')
    assert args_with_many_hash_tags.hash_tags[:4] == result.hash_tags
