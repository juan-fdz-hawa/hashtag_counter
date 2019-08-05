from tkinter import Frame, Label, StringVar, Button
from typing import List

from hashtag_counter import HashTagStore, HashTag


class UI(Frame):
    def __init__(self, master=None, store=HashTagStore, on_update_btn_click=None):
        super().__init__(master)

        self._labels = {hash_tag.name: StringVar(value=str(hash_tag)) for hash_tag in store}
        store.on_update(lambda hash_tags: self._update_labels(hash_tags))

        self._on_update_btn_click = on_update_btn_click

        self.display()

    def _update_labels(self, hash_tags: List[HashTag]):
        for hash_tag in hash_tags:
            self._labels[hash_tag.name].set(str(hash_tag))

    def _fetch_counts(self):
        pass

    def display(self):
        # Header
        Label(
            self,
            text='Hash Tag Counter',
            font=('Helvetica', 24),
            height=4
        ).pack()

        # HashTags
        for var in self._labels.values():
            label = Label(
                self,
                textvariable=var,
                font=('Helvetica', 20),
            )
            label.pack()

        # Update btn
        Button(
            self,
            text='Update',
            command=self._on_update_btn_click
        ).pack(side='bottom')

        self.pack()
