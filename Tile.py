import pygame

from constants import image_path


class Tile:
    def __init__(self):
        # for Lane, need an empty image
        self.image = None
        # for other classes: need to load their image
    def load_image(self, image_name):
        self.image = pygame.image.load(f"{image_path}{image_name}.png").convert_alpha()


class Guardian(Tile):
    def __init__(self):
        self.load_image("2")

class Wall(Tile):
    def __init__(self):
        self.load_image("1")
    

class Lane(Tile):
    def __init__(self):
        # = Tile.__init__(self) ->call parent constructor
        super().__init__()
