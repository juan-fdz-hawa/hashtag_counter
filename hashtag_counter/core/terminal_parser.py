from argparse import ArgumentParser

MAX_HASH_TAGS = 4


def process_args(args, logger):
    unq_hash_tags = set(args.hash_tags)
    if len(unq_hash_tags) < len(args.hash_tags):
        logger.info('Duplicated hash tags detected! Only taking unique values')
        args.hash_tags = list(unq_hash_tags)

    if len(args.hash_tags) > MAX_HASH_TAGS:
        logger.info('Too many hash tags! Only taking the first 4')
        args.hash_tags = args.hash_tags[:4]
    return args


def read_args():
    arg_parser = ArgumentParser(
        prog='hash_tag_counter',
        description='Given a list of tags, returns all counts'
    )

    arg_parser.add_argument(
        '-h',
        '--hash-tags',
        required=True,
        help='List of hash tags (separated by space) that will be used for the counting',
        nargs='+'
    )

    return arg_parser.parse_args()
