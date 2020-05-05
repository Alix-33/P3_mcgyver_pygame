import pygame
from constants import IMAGE_PATH


class Tile:
    """ loads child class image """
    def __init__(self):
        """ constructor defines an image, used in the method load_image,
        and a name, given next in child class """
        self.image = None
        self.name = None

    def load_image(self, image_name):
        """ gives the way to load the child class image with the constant IMAGE_PATH
        and expects image_name given in child class """
        self.image = pygame.image.load(f"{IMAGE_PATH}{image_name}.png").convert_alpha()


