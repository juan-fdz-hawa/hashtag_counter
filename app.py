import sys
from os import path
from tkinter import Tk

from hashtag_counter import get_logger, process_args, read_args, HashTagStore, UI, Requester, Runner


def main():
    config_path = path.join('.', 'config.yaml')

    _check_config_files(config_path)

    logger = get_logger()
    args = process_args(read_args(), logger)

    requester = Requester(config_path)
    runner = Runner(
        on_success=lambda results: store.update_all(results),
        on_error=on_error,
        on_complete=on_complete
    )

    store = HashTagStore(args.hash_tags)
    fetcher = fetcher_of_counts(runner, requester, store)
    launch_ui(fetcher, store)


def launch_ui(fetcher, store):
    tk_root = Tk()
    ui = UI(
        master=tk_root,
        store=store,
        on_update_btn_click=fetcher
    )
    ui.master.title('Hash Tag Counter')
    ui.master.geometry('400x700+100+100')
    ui.mainloop()


def _check_config_files(config_path):
    if not path.isfile(config_path):
        print('Oh noes! config.yaml file not found! Use config.yaml.template as a base for creating a config file.',
              file=sys.stderr)
        exit(1)


def fetcher_of_counts(runner, requester, store):
    return lambda: runner.execute(requester.do_search, list(store))


def on_error(error):
    print(f'Opsy daisy, something went wrong {error}')


def on_complete():
    pass


if __name__ == '__main__':
    main()
