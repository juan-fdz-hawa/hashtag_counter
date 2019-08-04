from tkinter import Frame, Label, StringVar
from typing import List

from hashtag_counter.hash_tag_store import HashTagStore


class UI(Frame):
    def __init__(self, master=None, hash_tags=List[str]):
        super().__init__(master)

        self._labels = {h: StringVar() for h in hash_tags}

        store = HashTagStore(hash_tags)
        store.on_update(lambda x: self._labels[x.name].set(str(x)))

        self.display()

    def display(self):
        # Header
        Label(
            self,
            text='HashTagCounter',
            font=('Helvetica', 24),
            height=4
        ).pack()

        # HashTags
        for _, var in self._labels:
            label = Label(
                self,
                textvariable=var,
                font=('Helvetica', 20),
            )
            label.pack()
