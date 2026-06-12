import dataclasses
import json
from typing import List

@dataclasses.dataclass
class Image:
    data: bytes
    width: int
    height: int

class ImageEditor:
    def __init__(self, image: Image):
        self.image = image
        self.undo_stack = []
        self.redo_stack = []

    def crop(self, x: int, y: int, width: int, height: int):
        self.undo_stack.append(self.image)
        self.image = Image(self.image.data, width, height)
        self.redo_stack = []

    def rotate(self, degrees: int):
        self.undo_stack.append(self.image)
        # Simulate rotation by changing width and height
        if degrees == 90 or degrees == 270:
            self.image = Image(self.image.data, self.image.height, self.image.width)
        self.redo_stack = []

    def flip(self, horizontal: bool):
        self.undo_stack.append(self.image)
        # Simulate flip by changing width or height
        if horizontal:
            self.image = Image(self.image.data, self.image.width, self.image.height)
        else:
            self.image = Image(self.image.data, self.image.width, self.image.height)
        self.redo_stack = []

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.image)
            self.image = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.image)
            self.image = self.redo_stack.pop()

    def get_image(self):
        return self.image
