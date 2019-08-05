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

    def __iter__(self):
        return self._hash_tags.items().__iter__()

    def on_update(self, callback: Callable[[List[HashTag]], None]) -> None:
        """
        Registers a new listener
        :param callback: Func to call when a new count is posted
        :return: None
        """
        self._callbacks.append(callback)

    def update_all(self, results: List[Tuple[str, object]]) -> None:
        """
        Updates all hash tags based on the contents of results.
        Results will be filled from results of the requester.get_count,
        the first part of a result is the hash tag name, the second part
        is the response we got from the twitter api.
        After updating all hash tags, all listeners will be notified.
        :param results: List of (hash tag names, results)
        :return: None
        """
        for tag_name, result in results:
            notify = False
            hash_tag = self._hash_tags.get(tag_name)

            if hash_tag:
                self._hash_tags.update({tag_name: hash_tag.update(result)})
                notify = True

            if notify:
                for callback in self._callbacks:
                    callback(self._hash_tags.values())
