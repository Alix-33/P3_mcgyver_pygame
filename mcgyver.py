import pygame
from tile import Tile
from lane import Lane
from guardian import Guardian
from item import Item


class McGyver(Tile):
    """ this class, Tile child class, works while McGyver is in the game,
    load the McGyver image,
    and defines the window title message, with an updated inventory. """
    
    def __init__(self):
        """ constructor action: while McGyver is-out is False, the game continues.
        inventory: empty list fulfilled by McGyver when goes on an item
        message: window title """
        self.is_out = False
        self.load_image("3")
        self.inventory = []
        self.message = None

    def get_message(self):
        """print a message in the window title,
        and the inventory list,
        updated at each item picked up"""
        if self.message is None:
            return f"McGyver game_inventory:{self.inventory}"
        else:
            return self.message

    def update_position(self, maze, modifs):
        """depending on the player answer:
        gives the conditions to update McGyver's position inside the maze.
        modifs: given by the player in the move method of class Game
        return: None if McGyver is out = True and stop reading this method"""
        if self.is_out:
            return
        # initial position = Mcgyver tile in maze
        # update position inside the maze
        pos = maze.find_tile(McGyver)
        lin = pos[0] + modifs[0]
        lin = min(lin, 14)
        lin = max(0, lin)
        col = pos[1] + modifs[1]
        col = min(col, 14)
        col = max(0, col)
        
        # if the new position (found with get_tile) is an item,
        # print a lane (with set_tile)
        tile = maze.get_tile(lin, col)
        if isinstance(tile, Item):
            self.inventory.append(tile.name)
            maze.set_tile(lin, col, Lane())

        # if the new position is Guardian -> check victory
        if isinstance(maze.get_tile(lin, col), Guardian):
            self.check_victory(maze)
        # if the new position is a lane: replace by mg, 
        # and print lane instead of old position
        if isinstance(maze.get_tile(lin, col), Lane):
            maze.set_tile(pos[0], pos[1], Lane())
            maze.set_tile(lin, col, self)

    def check_victory(self, maze):
        """if McGyver position = Guardian position: stop the game, check if
        you win or loose, and offers to reload the game"""
        self.is_out = True
        # if an item is found in maze: lost game (else, game won)
        if maze.find_tile(Item):
            self.message = "You're dead! Press F1 to reload"
        else:
            self.message = "You win! Press F1 to reload"
