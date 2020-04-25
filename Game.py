from pygame.constants import QUIT, KEYDOWN

from Maze import Maze
from Mc_Gyver import McGyver
import pygame
from pygame.locals import *

from constants import *


class Game:
    #load the game from text file + load class Maze + load class McGyver
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
        self.icon = pygame.image.load(WINDOW_ICON)
        self.quit = False
        self.load_game()

    def load_game(self):
        self.mg = McGyver()
        self.maze = Maze(MAZE_FILE, self.window, self.icon)

    def run(self):
        #carry out the movement several time leaving the yey pressed (400 milliseconds before continue moving, 30 mls between each movement)
        pygame.key.set_repeat(400, 30)
        #boucle while: while mg is out = False (mg is in the maze) -> reload draw maze + mg move.
        while self.quit == False:
            pygame.display.set_caption(self.mg.get_message())
            self.maze.draw_maze()
            self.move(self.maze)
        pygame.quit()
    
    def move(self, maze):
    #wait for player (+ translate the input in capital letters):
    # direction = input("(Droite = D, Gauche = G, Haut = H, Bas = B, Quitter = Q) Votre choix?: ").upper()
        modifs = (0,0)
        #give the position modifications depending on the player answer:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.quit = True
            if event.type == KEYDOWN and event.key == K_F1:
                self.load_game()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    modifs = (0, 1)
                elif event.key == K_LEFT:
                    modifs = (0, -1)
                elif event.key == K_UP:
                    modifs = (-1, 0)
                elif event.key == K_DOWN:
                    modifs = (1, 0)
        
        self.mg.update_position(maze, modifs)
