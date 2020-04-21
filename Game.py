from Maze import Maze
from Mc_Gyver import McGyver
from constants import *
import pygame


class Game:
    #load the game from text file + load class Maze + load class McGyver
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((window_side, window_side))
        self.maze = Maze(maze_file, self.window)
        self.mg = McGyver()
    
    def run(self):
        #carry out the movement several time leaving the yey pressed (400 milliseconds before continue moving, 30 mls between each movement)
        pygame.key.set_repeat(400, 30)
        #boucle while: while mg is out = False (mg is in the maze) -> reload draw maze + mg move.
        while self.mg.is_out == False:
            self.maze.draw_maze2()
            self.mg.move2(self.maze)
