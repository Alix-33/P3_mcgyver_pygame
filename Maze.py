from random import randint
from mcgyver import McGyver
from item import Item
from needle import Needle
from tube import Tube
from ether import Ether
from tile import Tile
from guardian import Guardian
from lane import Lane
from wall import Wall
from constants import *
import pygame


class Maze:
    """load the maze, the window and the icon, give a random position to items,
    replaces the tiles with their image, and draw the maze"""

    def __init__(self, file_name, window, icon):
        """constructor actions: load text file (with "load_maze" method))  
        + insert items randomly (with "create_items" method from the items tuple)."""
        self.window = window
        self.data = self.load_maze(file_name)
        self.items = ("N", "T", "E")
        self.create_items()
        self.icon = pygame.display.set_icon(icon)

    def find_tile(self, tile):
        """ find a tile in the maze, if this tile is an instance of the class Tile."""
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if isinstance(self.data[i][j], tile):
                    return [i, j]
        return None

    def get_tile(self, i, j):
        """give the tile at the i,j position
            i: line
            j: colone"""
        return self.data[i][j]

    def set_tile(self, i, j, tile):
        """print the tile at the given position
            i: line
            j: colone"""
        self.data[i][j] = tile

    def load_maze(self, file_name):
        """load a list of lists of character, and replace by the tile image,
        defined in its class"""
        data = []
        with open(file_name) as f:
            # f= line list -> first loop to add each line in "data" list
            for line in f:
                # second loop to add each tile in "line_data" list, 
                # with its symbol defined in its class
                line_data = []
                for tile in line:
                    if tile == "G":
                        line_data.append(Guardian())
                    elif tile == "#":
                        line_data.append(Wall())
                    elif tile == " ":
                        line_data.append(Lane())
                    elif tile == "M":
                        line_data.append(McGyver())
                # add each line_data in data       
                data.append(line_data)
        return data

    def create_items(self):
        """get items symbol instead of its character in the text file
        (given in each class),
        for each item in the "items" tupple (given in Maze constructor),
        at the position (pos) given in get_random_empty_tile method
        pos= [line, colone]"""
        for item in self.items:
            pos = self.get_random_empty_tile()
            if item == "N":
                self.data[pos[0]][pos[1]] = Needle()
            elif item == "E":
                self.data[pos[0]][pos[1]] = Ether()
            elif item == "T":
                self.data[pos[0]][pos[1]] = Tube()

    def get_random_empty_tile(self):
        """get random position inside the maze"""
        while True:
            row = randint(0, len(self.data) - 1)
            col = randint(0, len(self.data) - 1)
            tile = self.data[row][col]
            if type(tile) == Lane:
                return [row, col]

    def draw_maze(self):
        """print the maze (loaded in load_maze)"""
        pygame.draw.rect(self.window, (0, 0, 0), (0, 0) + self.window.get_size())
        line = 0
        for row_data in self.data:
            col = 0
            for tile in row_data:
                x = col * SPRITE_SIZE
                y = line * SPRITE_SIZE
                if tile.image is not None:
                    self.window.blit(tile.image, (x, y))
                col += 1
            line += 1
        pygame.display.flip()
