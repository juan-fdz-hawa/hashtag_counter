from tkinter import Frame, Label, StringVar
from typing import List

from hashtag_counter.models.hash_tag import HashTag


class Application(Frame):
    def __init__(self, master=None, hash_tags=List[HashTag]):
        super().__init__(master)

        self._listen_to_hash_tag_changes(hash_tags)

        self.display()

    def _listen_to_hash_tag_changes(self, hash_tags):
        self._hash_tag_labels = {
            h.name: StringVar() for h in hash_tags
        }
        for hash_tag in hash_tags:
            hash_tag.on_update(lambda x: self._update_hash_tag_label(x))

    def display(self):
        # Header
        Label(
            self,
            text='HashTagCounter',
            font=('Helvetica', 24),
            height=4
        ).pack()

        # HashTags
        for _, var in self._hash_tag_labels:
            label = Label(
                self,
                textvariable=var,
                font=('Helvetica', 20),
            )
            label.pack()

    def _update_hash_tag_label(self, hash_tag):
        self._hash_tag_labels[hash_tag.name].set(str(hash_tag))
