import random

import pygame
import sys


class Tile:
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.rect = pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Labyrinth:
    def __init__(self):
        self.NBCASE = 59
        self.TILE_SIZE = 10
        self.SIZE = self.WIDTH, self.HEIGHT = self.NBCASE * self.TILE_SIZE, self.NBCASE * self.TILE_SIZE

        self.color = [  # white
                        # black
                      (229, 232, 39),  # yellow
                      (68, 232, 39),  # green
                      (187, 39, 232),  # purple
                      (234, 63, 206),  # pink
                      (0, 0, 255),  # blue
                      (255, 0, 0),  # red
                      ]

        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode(self.SIZE)
        self.display_surface.fill((255, 255, 255))

        self.matrice = [[0 for i in range(self.NBCASE)] for y in range(self.NBCASE)]


        self.walls = []
        self.tiles = []
        self.init_matrice()

    def init_matrice(self):

        # lines
        for i in range(len(self.matrice)):
            for j in range(0, len(self.matrice), 2):
                self.walls.append(Tile(j, i, (0, 0, 0), self.TILE_SIZE))

        # columns
        for i in range(0, len(self.matrice), 2):
            for j in range(len(self.matrice) - 1):
                self.walls.append(Tile(j, i, (0, 0, 0), self.TILE_SIZE))

        # colors
        for i in range(1, len(self.matrice) - 1, 2):
            for j in range(1, len(self.matrice) - 1, 2):
                self.tiles.append(Tile(j, i, random.choice(self.color), self.TILE_SIZE))

    def draw_matrice(self):
        for wall in self.walls:
            wall.draw(self.display_surface)
        for tile in self.tiles:
            tile.draw(self.display_surface)

    def get_wall(self):
        wall = []
        for i in range(1, len(self.matrice) - 2, 1):
            for j in range(1, len(self.matrice) - 2, 1):
                if self.matrice[i][j] == 1:
                    wall.append([j, i])
        return wall

    def get_tile(self):
        tile = []
        for i in range(1, len(self.matrice) - 2, 1):
            for j in range(1, len(self.matrice) - 2, 1):
                if self.matrice[i][j] != 1:
                    tile.append([j, i])
        return tile

    def transform_matrice(self):
        wall = self.get_wall()
        for i in range(len(wall) - 1):
            axis = random

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.draw_matrice()

            self.clock.tick(15)
            pygame.display.flip()


if __name__ == "__main__":
    lab = Labyrinth()
    lab.game_loop()
