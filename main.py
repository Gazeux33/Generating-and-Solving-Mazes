import sys
import pygame
import random

from Astar import Astar

sys.setrecursionlimit(1000000)

COLORS = {
    "-2": "#6A26E1",
    "-1": "#000000",
    "0": "#FFFFFF",
    "1": "#4749FC",
    "2": "#BC47FC",
    "3": "#F747FC",
    "4": "#5CFC47",
    "5": "#F4FC47",
    "6": "#F4FC47",
    "7": "#FF0F01",
    "8": "#396E1F",
    "9": "#141075",
}

WIN_SIZE = 800
VISITED_NUMBER = -2
WALL_NUMBER = -1
WHITE_NUMBER = 0


class Game:
    def __init__(self):
        self.NB_CASE = 99
        self.SIZE = WIN_SIZE, WIN_SIZE
        self.step = WIN_SIZE / self.NB_CASE

        pygame.init()
        self.display_screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Labyrinth")
        self.clock = pygame.time.Clock()

        self.matrix = None
        self.walls = None
        self.solver = None
        self.finish = None
        self.reset()

    def play(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e and self.finish:
                        path = self.solver.astar()
                        if path is None:
                            print("Pas de chemin trouvé")
                        else:
                            for coord in path:
                                y, x = coord
                                self.matrix[y][x] = VISITED_NUMBER
                    if event.key == pygame.K_r and self.finish:
                        self.reset()
            if not self.finish:
                for i in range(200):
                    self.transform_matrix()

            if len(self.walls) == 0:
                self.finish = True
            self.draw_matrix()

            self.clock.tick(20)
            pygame.display.flip()

    def draw_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                rect = pygame.Rect(j * self.step, i * self.step, self.step + 1, self.step + 1)
                color = self.matrix[i][j]
                if self.finish:
                    if color != WALL_NUMBER and color != VISITED_NUMBER:
                        color = WHITE_NUMBER
                pygame.draw.rect(self.display_screen, COLORS[str(color)], rect)

    def add_colors(self):
        for i in range(1, len(self.matrix) - 1, 2):
            for j in range(1, len(self.matrix) - 1, 2):
                self.matrix[i][j] = random.randint(1, 9)
        self.matrix[1][0] = WHITE_NUMBER
        self.matrix[len(self.matrix) - 2][len(self.matrix) - 1] = WHITE_NUMBER

    def get_walls(self):
        wall = []
        for i in range(1, len(self.matrix) - 1, 1):
            for j in range(1, len(self.matrix) - 1, 1):
                if self.matrix[i][j] == WALL_NUMBER:
                    wall.append((j, i))  # add wall coordinates
        return wall

    def transform_matrix(self):
        if len(self.walls) > 0:
            wall = random.choice(self.walls)
            self.walls.remove(wall)
            y, x = wall

            if self.matrix[y][x - 1] != WALL_NUMBER and self.matrix[y][x + 1] != WALL_NUMBER:
                if self.matrix[y][x - 1] != self.matrix[y][x + 1]:
                    self.spread_color(wall, random.choice([self.matrix[y][x - 1], self.matrix[y][x + 1]]))

            if self.matrix[y - 1][x] != WALL_NUMBER and self.matrix[y + 1][x] != WALL_NUMBER:
                if self.matrix[y - 1][x] != self.matrix[y + 1][x]:
                    self.spread_color(wall, random.choice([self.matrix[y - 1][x], self.matrix[y + 1][x]]))

    def spread_color(self, wall, color):
        y, x = wall
        self.matrix[y][x] = color
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (abs(i) + abs(j) == 1
                        and self.is_wall_in_range(y + i, x + j)
                        and self.matrix[y + i][x + j] != color
                        and self.matrix[y + i][x + j] != WALL_NUMBER):
                    self.spread_color((y + i, x + j), color)

    def is_wall_in_range(self, x, y):
        return not (x > len(self.matrix) - 1 or y > len(self.matrix) - 1 or x < 0 or y < 0)

    def is_possible(self):
        start = 1, 0
        end = len(self.matrix) - 2, len(self.matrix) - 1
        visited = []
        return self.search_end(start, end, visited)

    def search_end(self, current, end, visited):
        y, x = current
        if current == end:
            return True
        if current in visited or not self.is_wall_in_range(y, x):
            return False

        (visited.append(current))

        for i in range(-1, 2):
            for j in range(-1, 2):
                if abs(i) + abs(j) == 1:
                    next_cell = (y + i, x + j)
                    if self.is_wall_in_range(*next_cell) and self.matrix[y + i][x + j] != WALL_NUMBER:
                        result = self.search_end(next_cell, end, visited)
                        if result:
                            return True

        return False

    def reset(self):
        self.matrix = [[WALL_NUMBER for _ in range(self.NB_CASE)] for _ in range(self.NB_CASE)]
        self.add_colors()
        self.walls = self.get_walls() + self.get_walls()
        self.finish = False
        self.solver = Astar(self, (1, 0), (len(self.matrix) - 2, len(self.matrix) - 1))

    def print_matrix(self):
        for row in self.matrix:
            print(row)


game = Game()
game.play()
