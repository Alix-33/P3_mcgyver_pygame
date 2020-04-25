import pygame

from constants import IMAGE_PATH


class Tile:
    def __init__(self):
        # for Lane, need an empty image
        self.image = None
        self.name = None
        # for other classes: need to load their image
    def load_image(self, image_name):
        self.image = pygame.image.load(f"{IMAGE_PATH}{image_name}.png").convert_alpha()


