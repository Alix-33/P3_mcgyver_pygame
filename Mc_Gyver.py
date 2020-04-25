import pygame
from Tile import Tile
from Lane import Lane
from Guardian import Guardian
from Item import Item



class McGyver(Tile):
    #constructor action: when mg is out = True -> end of the game.
    def __init__(self):
        self.is_out = False
        self.load_image("3")
        self.inventory = []
        self.message = None

    def get_message(self):
        if self.message is None:
            return f"McGyver game_inventory:{self.inventory}"
        else:
            return self.message

    #depending on the player answer: update McGyver position
    def update_position(self, maze, modifs):
        if self.is_out:
            return
        #initial position = Mcgyver tile in maze
        #update position inside the maze
        pos = maze.find_tile(McGyver)
        lin = pos[0] + modifs[0]
        lin = min(lin, 14)
        lin = max(0, lin)
        col = pos[1] + modifs[1]
        col = min(col, 14)
        col = max(0, col)
        
        #if the new position (found with get_tile) is an item, print a lane (with set_tile)
        tile = maze.get_tile(lin, col)
        if isinstance(tile, Item):
            self.inventory.append(tile.name)
            maze.set_tile(lin, col, Lane())

        #if the new position is Guardian -> check victory
        if isinstance(maze.get_tile(lin, col), Guardian):
            self.check_victory(maze)
        #if the new position is a lane: replace by mg, and print lane instead of old position
        if isinstance(maze.get_tile(lin, col), Lane):
            maze.set_tile(pos[0], pos[1], Lane())
            maze.set_tile(lin, col, self)

    def check_victory(self, maze):
        self.is_out = True
        #if an item is found in maze: lost game (else, game won)
        if maze.find_tile(Item):
            self.message = "You're dead! Press F1 to reload"
        else:
            self.message = "You win! Press F1 to reload"
