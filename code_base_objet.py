import pygame
import sys
import random

from tile import Tile


class Game:
    def __init__(self):
        self.NB_CASE = 19
        self.TILE_SIZE = 10
        self.SIZE = self.WIDTH, self.HEIGHT = self.NB_CASE * self.TILE_SIZE, self.NB_CASE * self.TILE_SIZE

        pygame.init()
        self.display_screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Labyrinth")

        self.clock = pygame.time.Clock()

        self.matrix = [[Tile(j, i, self.TILE_SIZE) for j in range(self.NB_CASE)] for i in range(self.NB_CASE)]

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pass

            self.draw_matrix()

            self.clock.tick(120)
            pygame.display.flip()

    def draw_matrix(self):
        for tab in self.matrix:
            for tile in tab:
                tile.draw(self.display_screen)


game = Game()
game.play()
