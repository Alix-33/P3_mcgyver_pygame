from Tile import Tile
from Item import Item

class Needle(Item):
    def __init__(self):
        self.load_image("4")
        self.name = "Needle"