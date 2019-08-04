from concurrent.futures.process import ProcessPoolExecutor
from typing import List, Callable
from functools import reduce

from hashtag_counter import HashTag


class Runner:
    def __init__(self, on_success, on_error, on_complete):
        self.on_success = on_success
        self.on_error = on_error
        self.on_complete = on_complete

    def execute(self, requester: Callable[[HashTag], (str, int)], payloads: List[HashTag]):
        """
        Executes the given requester func (HashTag -> [(str, int)]) in parallel
        creating a new process for each payload.
        :param requester: Function used for loading the count of a hash tag
        :param payloads: List of hash tags to past to the requester func
        :return: None
        """
        with ProcessPoolExecutor() as executor:
            reduce(
                lambda a, c: a.merge(c),
                executor.map(requester, payloads)
            ).subscribe(
                self.on_success,
                self.on_error,
                self.on_complete
            )
