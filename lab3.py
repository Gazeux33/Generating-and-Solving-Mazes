import pygame
import sys
import random

from tile import Tile
from group_tile import GroupTile


class Game:
    def __init__(self):
        self.NB_CASE = 59
        self.TILE_SIZE = 10
        self.SIZE = self.WIDTH, self.HEIGHT = self.NB_CASE * self.TILE_SIZE, self.NB_CASE * self.TILE_SIZE

        pygame.init()
        self.display_screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Labyrinth")

        self.clock = pygame.time.Clock()

        self.matrix = [[Tile(j, i, self.TILE_SIZE) for j in range(self.NB_CASE)] for i in range(self.NB_CASE)]
        self.init_matrix()
        self.apply_color()

        self.print_matrix()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.transform_matrix()
            self.draw_matrix()

            self.transform_matrix()
            self.clock.tick(120)
            pygame.display.flip()

    def draw_matrix(self):
        for tab in self.matrix:
            for tile in tab:
                tile.draw(self.display_screen)

    def init_matrix(self):
        # lines
        for i in range(len(self.matrix)):
            for j in range(0, len(self.matrix), 2):
                self.matrix[i][j].color = -1

        # columns
        for i in range(0, len(self.matrix), 2):
            for j in range(len(self.matrix) - 1):
                self.matrix[i][j].color = -1

    def apply_color(self):
        for i in range(1, len(self.matrix) - 1, 2):
            for j in range(1, len(self.matrix) - 1, 2):
                self.matrix[i][j].color = random.randint(1, 9)

    def print_matrix(self):
        for tab in self.matrix:
            print(tab)

    def transform_matrix(self):
        walls = self.get_wall()
        if walls:
            wall = random.choice(walls)

            axis = random.randint(1, 2)
            if axis == 1:
                if self.matrix[wall.y][wall.x - 1] != -1 and self.matrix[wall.y][wall.x + 1] != -1:
                    print("pas de noir validé")
                    if self.matrix[wall.y][wall.x - 1].color != self.matrix[wall.y][wall.x + 1].color:
                        print("couleur differente")
                        color = random.choice(
                            [self.matrix[wall.y][wall.x - 1].color, self.matrix[wall.y][wall.x + 1].color])
                        self.matrix[wall.y][wall.x - 1].color = color
                        self.matrix[wall.y][wall.x].color = color
                        self.matrix[wall.y][wall.x + 1].color = color
            elif axis == 2:
                if self.matrix[wall.y - 1][wall.x] != -1 and self.matrix[wall.y + 1][wall.x] != -1:
                    if self.matrix[wall.y - 1][wall.x].color != self.matrix[wall.y + 1][wall.x].color:
                        color = random.choice(
                            [self.matrix[wall.y - 1][wall.x].color, self.matrix[wall.y + 1][wall.x].color])
                        self.matrix[wall.y - 1][wall.x].color = color
                        self.matrix[wall.y][wall.x].color = color
                        self.matrix[wall.y + 1][wall.x].color = color

    def get_wall(self):
        wall = []
        for i in range(1, len(self.matrix) - 1, 1):
            for j in range(1, len(self.matrix) - 1, 1):
                if self.matrix[i][j].color == -1:
                    wall.append(self.matrix[i][j])
        return wall


if __name__ == "__main__":
    game = Game()
    game.play()
