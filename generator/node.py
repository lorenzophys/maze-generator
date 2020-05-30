from settings import *
import pygame, random


class Node:
    def __init__(self, row, col, window):
        self.row = row
        self.col = col
        self.window = window
        self.visited = False
        self.wall = {"top":True, "right":True, "bottom":True, "left":True}
        self.neighbors = []


    def draw(self):
        x, y = self.col*SPACING, self.row*SPACING

        if self.visited:
            pygame.draw.rect(self.window, (self.row*2,self.col*2,(self.row+self.col)*3), (x,y,SPACING,SPACING))
        if self.wall["top"]:
            pygame.draw.line(self.window, WHITE, (x,y), (x+SPACING, y), 1)
        if self.wall["right"]:
            pygame.draw.line(self.window, WHITE, (x+SPACING,y), (x+SPACING, y+SPACING), 1)
        if self.wall["bottom"]:
            pygame.draw.line(self.window, WHITE, (x,y+SPACING), (x+SPACING, y+SPACING), 1)
        if self.wall["left"]:
            pygame.draw.line(self.window, WHITE, (x,y), (x, y+SPACING), 1)


    def get_neighbors(self, grid):
        self.neighbors = []
        row = self.row
        col = self.col

        if row+1 < N:
            right = grid[col][row+1]
            if not(right.visited):
                self.neighbors.append(right)
        if row > 0:
            left = grid[col][row-1]
            if not(left.visited):
                self.neighbors.append(left)
        if col+1 < N:
            up = grid[col+1][row]
            if not(up.visited):
                self.neighbors.append(up)
        if col > 0:
            down = grid[col-1][row]
            if not(down.visited):
                self.neighbors.append(down)
    

    def get_next(self):
        return random.choice(self.neighbors) if self.neighbors else None


    def paint(self):
        x, y = self.col*SPACING, self.row*SPACING
        pygame.draw.rect(self.window,WHITE,(x,y,SPACING,SPACING))