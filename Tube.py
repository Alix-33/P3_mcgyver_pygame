from tile import Tile
from item import Item


class Tube(Item):
    def __init__(self):
        self.load_image("6")
        self.name = "Tube"
