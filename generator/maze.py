from settings import *
import pygame, sys
from node import Node


class Maze: 
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Maze")

        self.is_running = True
        self.grid = [[Node(i,j,self.window) for i in range(N)] for j in range(N)]


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    
    def draw_grid(self):
        for i in range(N):
            for j in range(N):
                self.grid[i][j].draw()


    def remove_wall(self, node_a, node_b):
        delta_row = node_a.row-node_b.row
        delta_col = node_a.col-node_b.col

        if delta_row == 1:
            node_a.wall["top"], node_b.wall["bottom"] = False, False
        if delta_row == -1:
            node_a.wall["bottom"], node_b.wall["top"] = False, False
        if delta_col == 1:
            node_a.wall["left"], node_b.wall["right"] = False, False
        if delta_col == -1:
            node_a.wall["right"], node_b.wall["left"] = False, False


    def draw_maze(self):
        stack = []
        first_node = self.grid[0][0]
        first_node.visited = True
        stack.append(first_node)

        while stack:
            self.draw_grid()
            current_node = stack.pop()
            current_node.paint()
            current_node.get_neighbors(self.grid)
            next_node = current_node.get_next()  

            if next_node is not None:
                stack.append(current_node)
                self.remove_wall(current_node, next_node)
                next_node.visited = True
                stack.append(next_node)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.window.fill((0,0,0))
            self.clock.tick(FPS)


    def main(self):
        self.draw_maze()
        while self.is_running:
            self.check_events()
            self.draw_grid()
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()
