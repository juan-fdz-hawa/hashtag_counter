from concurrent.futures.process import ProcessPoolExecutor
from typing import List, Callable, Tuple

from rx import from_future, merge

from hashtag_counter import HashTag


class Runner:
    def __init__(self, on_success, on_error, on_complete):
        self.on_success = on_success
        self.on_error = on_error
        self.on_complete = on_complete

    def execute(self, requester: Callable[[HashTag], Tuple[str, dict]], payloads: List[HashTag]):
        """
        Executes the given requester func (HashTag -> [(str, dict)]) in parallel
        creating a new process for each request.
        :param requester: Function used for performing the API request.
        :param payloads: List of hash tags to past to the requester func
        :return: None
        """
        observables = []
        with ProcessPoolExecutor() as executor:
            for payload in payloads:
                _future = executor.submit(requester, payload)
                observables.append(from_future(_future))
        merge(*observables).subscribe(self.on_success, self.on_error, self.on_complete)
