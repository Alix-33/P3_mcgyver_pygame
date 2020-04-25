from Tile import Tile
from Item import Item

class Ether(Item):
    def __init__(self):
        self.load_image("5")
        self.name = "Ether"