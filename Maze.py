from random import randint
from Mc_Gyver import McGyver
from Item import Needle, Ether, Tube
from Tile import Guardian, Wall, Lane
from constants import *
import pygame


class Maze:
    
    #constructor actions: load text file (with "load_maze" method))  + insert items randomly (with "create_items" method from the items tupple).
    def __init__(self, file_name, window):
        self.window = window
        self.data2 = self.load_maze2(file_name)
        self.items = ("A","T","E")
        self.create_items2() 

    #find a tile in the maze, if this tile is an instance of the class Tile.
    def find_tile2(self, tile):
        for i in range(len(self.data2)):     
            for j in range(len(self.data2[i])): 
                if isinstance(self.data2[i][j], tile):
                    return [i,j]
        return None
    
    #give the tile position
    def get_tile (self, i, j):
        return self.data2[i][j]

    #print the tile at the given position
    def set_tile( self, i, j, tile):
        self.data2[i][j] = tile

    def load_maze2(self,file_name):
        data = []
        with open(file_name) as f:
            #f= line list -> first loop to add each line in "data" list
            for line in f:
                #second loop to add each tile in "line_data" list, with its symbol defined in its class
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
                #add each line_data in data       
                data.append(line_data)
        return data

    #get items symbol instead of its character in the text file (given in each class), for each item in the "items" tupple (given in Maze constructor)
    def create_items2(self):
        for item in self.items:
            pos = self.get_random_empty_tile2()
            if item == "A":
                self.data2[pos[0]][pos[1]] = Needle()
            elif item == "E":
                self.data2[pos[0]][pos[1]] = Ether()
            elif item == "T":
                self.data2[pos[0]][pos[1]] = Tube()
    
    #get random position inside the maze 
    def get_random_empty_tile2(self):
        while True:
            row = randint(0, len(self.data2)-1)
            col = randint(0, len(self.data2)-1)
            tile = self.data2[row][col]
            if type(tile) == Lane:
                return [row, col]

    #print the maze (loaded in load_maze)
    def draw_maze2(self):
        pygame.draw.rect(self.window, (0,0,0), (0,0)+ self.window.get_size())
        line = 0
        for row_data in self.data2:
            col = 0
            for tile in row_data:
                x = col * sprite_size
                y = line * sprite_size
                if tile.image is not None:
                    self.window.blit(tile.image, (x,y))         
                col += 1
            line += 1
        pygame.display.flip()