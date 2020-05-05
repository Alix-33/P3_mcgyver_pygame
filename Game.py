from pygame.constants import QUIT, KEYDOWN
from maze import Maze
from mcgyver import McGyver
import pygame
from pygame.locals import *
from constants import *


class Game:
    """ loads the game from text file (given in the constants file)
    + loads class Maze + loads class McGyver, and makes McGyver move. """

    def __init__(self):
        """ defines the window size, gives the icon image,
        defines the boolean needed in the main loop, and loads the game. """
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE))
        self.icon = pygame.image.load(WINDOW_ICON)
        self.quit = False
        self.load_game()

    def load_game(self):
        self.mg = McGyver()
        self.maze = Maze(MAZE_FILE, self.window, self.icon)

    def run(self):
        """ contains the main loop: while self.quit = False (mg is in the maze),
        reload draw maze + mg move """
        # carry out the movement several time leaving the key pressed
        # (400 milliseconds before continue moving, 30 mls between each movement)
        pygame.key.set_repeat(400, 30)
        while self.quit == False:
            pygame.display.set_caption(self.mg.get_message())
            self.maze.draw_maze()
            self.move(self.maze)
        pygame.quit()

    def move(self, maze):
        """ gets the keyboard event to make McGyver move, to quit or reload """
        modifs = (0, 0)
        # give the position modifications depending on the player answer:
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
