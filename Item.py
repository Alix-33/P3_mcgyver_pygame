import pygame

from Tile import Tile 

class Item(Tile):
    pass

class Needle(Item):
    def __init__(self):
        self.load_image("4")

class Ether(Item):
    def __init__(self):
        self.load_image("5")

class Tube(Item):
    def __init__(self):
        self.load_image("6")
