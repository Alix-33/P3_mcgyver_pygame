from tile import Tile
from item import Item


class Needle(Item):
    def __init__(self):
        self.load_image("4")
        self.name = "Needle"
