from typing import Tuple, Callable, List

from hashtag_counter import HashTag


class HashTagStore:
    """
    Keep tracks of all hash tags. Updating all listeners
    whenever the counts are updated.
    """
    def __init__(self, hash_tags_names: List[str]):
        self._hash_tags = {h: HashTag(h) for h in hash_tags_names}
        self._callbacks = []

    def on_update(self, callback: Callable[[HashTag], None]) -> None:
        """
        Registers a new listener
        :param callback: Func to call when a new count is posted
        :return: None
        """
        self._callbacks.append(callback)

    def update(self, results: List[Tuple[str, int]]) -> None:
        """
        Updates all hash tags based on the contents of results.
        Results is a list of hash tag names count pairs. Hash tags
        are indexed based on their names and if any match is found
        its count is updated, after all this, all registered listeners
        will be notified.
        :param results: List of (hash tag names, count)
        :return: None
        """
        pass
