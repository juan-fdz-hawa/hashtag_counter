import sys
from os import path

from hashtag_counter import get_logger, process_args, read_args


def main():
    tokens_path = path.join('.', '.twitter_tokens')
    config_path = path.join('.', 'config.yaml')

    if not path.isfile(config_path):
        print('Oh noes! config.yaml file not found! Use config.yaml.template as a base for creating a config file.',
              file=sys.stderr)
        exit(1)

    if not path.isfile(tokens_path):
        print('Oh noes! Twitter Request token file not found! Please run the auth process before using the app',
              file=sys.stderr)
        exit(1)

    logger = get_logger()
    args = process_args(read_args(), logger)


if __name__ == '__main__':
    main()
