from Tile import Tile, Lane, Guardian
from Item import Item
import pygame
from pygame.locals import *
pygame.init()

class McGyver(Tile):
    # def __repr__(self):
    #     return "⚪"
    #constructor action: when mg is out = True -> end of the game.
    def __init__(self):
        self.is_out = False
        self.load_image("3")
    
    def move2(self, maze):
        #wait for player (+ translate the input in capital letters):
        # direction = input("(Droite = D, Gauche = G, Haut = H, Bas = B, Quitter = Q) Votre choix?: ").upper()
        modifs = (0,0)
        #give the position modifications depending on the player answer:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.is_out = True
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    modifs = (0, 1)
                elif event.key == K_LEFT:
                    modifs = (0, -1)
                elif event.key == K_UP:
                    modifs = (-1, 0)
                elif event.key == K_DOWN:
                    modifs = (1, 0)
        
        self.update_position2(maze, modifs)

    #depending on the player answer: update McGyver position
    def update_position2(self, maze, modifs):
        #initial position = Mcgyver tile in maze
        #update position inside the maze
        pos = maze.find_tile2(McGyver)
        lin = pos[0] + modifs[0]
        lin = min(lin,14)
        col = pos[1] + modifs[1]
        col = min(col, 14)
        
        #if the new position (found with get_tile) is an item, print a lane (with set_tile)
        if isinstance(maze.get_tile(lin, col), Item):
            maze.set_tile(lin,col,Lane())
        #if the new position is Guardian -> check victory
        if isinstance(maze.get_tile(lin, col), Guardian):
            self.check_victory(maze)
            #mg is out = True: end of the game
            self.is_out = True
        #if the new position is a lane: replace by mg, and print lane instead of old position
        if isinstance(maze.get_tile(lin, col), Lane):
            maze.set_tile(pos[0], pos[1], Lane())
            maze.set_tile(lin,col, self)

    def check_victory(self, maze):       
        #if an item is found in maze: lost game (else, game won)
        if maze.find_tile2(Item):
            print("You're dead!")
        else:
            print("You win!")
