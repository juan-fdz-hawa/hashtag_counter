from argparse import ArgumentParser


def process_args(args, logger, max_hash_tags=4):
    """
    Validates hash tags read from CLI, logging any data constraints violations:
    1 - If there are duplicated hash tags, those will be removed.
    2 - If user types more than 'max_hash_tags' unique hash, just take the first 'max_hash_tags'
    :param max_hash_tags: Max number of unique hash tags allowed
    :param args: Args read from CLI
    :param logger: Logger used for logging
    :return: Arguments processed
    """
    unq_hash_tags = set(args.hash_tags)
    if len(unq_hash_tags) < len(args.hash_tags):
        logger.info('Duplicated hash tags detected! Only taking unique values')
        args.hash_tags = list(unq_hash_tags)

    if len(args.hash_tags) > max_hash_tags:
        logger.info('Too many hash tags! Only taking the first 4')
        args.hash_tags = args.hash_tags[:4]
    return args


def read_args():
    """
    Reads the hash tags (separated by a single space) from the
    user terminal
    :return: All hash tag read
    """
    arg_parser = ArgumentParser(
        prog='hashtag_counter',
        description='Given a list of tags, returns all counts'
    )

    arg_parser.add_argument(
        '-t',
        '--tags',
        required=True,
        dest='hash_tags',
        help='List of hash tags (separated by space)',
        nargs='+'
    )

    return arg_parser.parse_args()
