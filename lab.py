import random

import pygame
import sys


class Game:
    def __init__(self):
        self.NB_CASE = 9
        self.TILE_SIZE = 10
        self.SIZE = self.WIDTH, self.HEIGHT = self.NB_CASE * self.TILE_SIZE, self.NB_CASE * self.TILE_SIZE

        # screen
        self.display_screen = pygame.display.set_mode(self.SIZE)
        self.display_screen.fill((255, 255, 255))
        pygame.display.set_caption("Labyrinth")

        # clock
        self.clock = pygame.time.Clock()

        # matrix
        self.matrix = [[0 for y in range(self.NB_CASE)] for i in range(self.NB_CASE)]
        self.init_matrix()
        self.apply_color()
        self.print_matrix()
        self.transform_matrix()

    def init_matrix(self):
        # lines
        for i in range(len(self.matrix)):
            for j in range(0, len(self.matrix), 2):
                self.matrix[i][j] = -1

        # columns
        for i in range(0, len(self.matrix), 2):
            for j in range(len(self.matrix) - 1):
                self.matrix[i][j] = -1

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.draw_matrix()

            self.clock.tick(15)
            pygame.display.flip()

    def draw_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                rect = pygame.Rect(j * self.TILE_SIZE, i * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                pygame.draw.rect(self.display_screen, self.get_color(self.matrix[i][j]), rect)

    def apply_color(self):
        for i in range(1, len(self.matrix) - 1, 2):
            for j in range(1, len(self.matrix) - 1, 2):
                self.matrix[i][j] = random.randint(1, 9)

    def print_matrix(self):
        for tab in self.matrix:
            print(tab)

    def is_finished(self):
        color = self.matrix[1][1]
        for i in range(len(self.matrix)-1):
            for j in range(len(self.matrix)-1):
                if self.matrix[i][j] != color and self.matrix[i][j] != -1:
                    return False
        return True

    def transform_matrix(self):
        while not self.is_finished():
            x = random.randint(1, len(self.matrix) - 2)
            y = random.randint(1, len(self.matrix) - 2)
            if self.matrix[y][x] == -1:
                axe = random.randint(1, 2)
                if axe == 1:  # lines
                    if self.matrix[y][x-1] != -1 and self.matrix[y][x+1] != -1:
                        if self.matrix[y][x-1] != self.matrix[y][x+1]:
                            case = random.randint(1, 2)
                            if case == 1:
                                color = self.matrix[y][x-1]
                            else:
                                color = self.matrix[y][x+1]
                            self.matrix[y][x - 1] = color
                            self.matrix[y][x] = color
                            self.matrix[y][x + 1] = color
                if axe == 2:  # columns
                    if self.matrix[y-1][x] != -1 and self.matrix[y+1][x] != -1:
                        if self.matrix[y-1][x] != self.matrix[y+1][x]:
                            case = random.randint(1, 2)
                            if case == 1:
                                color = self.matrix[y-1][x]
                            else:
                                color = self.matrix[y+1][x]
                            self.matrix[y-1][x] = color
                            self.matrix[y][x] = color
                            self.matrix[y+1][x] = color

    @staticmethod
    def get_color(color):
        if color == -1:
            return 0, 0, 0  # black
        elif color == 0:
            return 255, 255, 255  # white
        elif color == 1:
            return "#4749FC"  # light blue
        elif color == 2:
            return "#BC47FC"  # purple
        elif color == 3:
            return "#F747FC"  # pink
        elif color == 4:
            return "#5CFC47"  # light green
        elif color == 5:
            return "#F4FC47"  # yellow
        elif color == 6:
            return "#FFB530"  # orange
        elif color == 7:
            return "#FF0F01"  # red
        elif color == 8:
            return "#396E1F"  # dark green
        elif color == 9:
            return "#141075"  # dark blue


if __name__ == "__main__":
    game = Game()
    game.game_loop()
