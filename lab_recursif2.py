import pygame
import sys
import random

from tile import Tile

"""
le but de ce code est de creer un labyrinthe
Pour cela on creer une matrice avec les murs ayant la valeur -1
les murs formes un maillage( fonction init_matrice())
le principe est que le programme choisi un mur aleatoirement 
sur un axe aleatoire
puis va comparer les couleurs qu'il a des deux cote
si les deux couleurs sont differentes alors le mur se brise et tout l'espace est
rempli avec une des deux couleurs tirée aleatoirement
ce processus est fait avec une fonction recusrive ( spread_color())
"""


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
            self.clock.tick(5)
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
            print(wall)
            axis = random.randint(1, 2)
            print(axis)
            if axis == 1:
                self.transform_lines(wall)
            else:
                self.transform_columns(wall)

    def get_wall(self):
        wall = []
        for i in range(1, len(self.matrix) - 2, 1):
            for j in range(1, len(self.matrix) - 2, 1):
                if self.matrix[i][j].color == -1:
                    wall.append(self.matrix[i][j])
        return wall

    def transform_lines(self, wall):
        if self.matrix[wall.y][wall.x - 1] != -1 and self.matrix[wall.y][wall.x + 1] != -1:
            if self.matrix[wall.y][wall.x - 1].color != self.matrix[wall.y][wall.x + 1].color:
                color = random.choice([self.matrix[wall.y][wall.x - 1].color, self.matrix[wall.y][wall.x + 1].color])
                self.spread_color(wall.x, wall.y, color)

    def transform_columns(self, wall):
        if self.matrix[wall.y - 1][wall.x] != -1 and self.matrix[wall.y + 1][wall.x] != -1:
            if self.matrix[wall.y - 1][wall.x].color != self.matrix[wall.y + 1][wall.x].color:
                color = random.choice([self.matrix[wall.y - 1][wall.x].color, self.matrix[wall.y + 1][wall.x].color])
                self.spread_color(wall.x, wall.y, color)

    # up = 1
    # right = 2
    # down = 3
    # left = 4
    def spread_color(self, x, y, color):
        if self.matrix[y][x].color == -1:
            self.matrix[y][x].color = color
            print(f"case {x} {y} reussi")

            # Vérification des indices avant de lancer les appels récursifs
            if y > 0 and self.matrix[y - 1][x].color != -1:
                self.spread_color(x, y - 1, color)

            if y < len(self.matrix) - 1 and self.matrix[y + 1][x].color != -1:
                self.spread_color(x, y + 1, color)

            if x > 0 and self.matrix[y][x - 1].color != -1:
                self.spread_color(x - 1, y, color)

            if x < len(self.matrix[y]) - 1 and self.matrix[y][x + 1].color != -1:
                self.spread_color(x + 1, y, color)



if __name__ == "__main__":
    game = Game()
    game.play()
import pygame
import sys
import random

from tile import Tile

"""
le but de ce code est de creer un labyrinthe
Pour cela on creer une matrice avec les murs ayant la valeur -1
les murs formes un maillage( fonction init_matrice())
le principe est que le programme choisi un mur aleatoirement 
sur un axe aleatoire
puis va comparer les couleurs qu'il a des deux cote
si les deux couleurs sont differentes alors le mur se brise et tout l'espace est
rempli avec une des deux couleurs tirée aleatoirement
ce processus est fait avec une fonction recusrive ( spread_color())
"""


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
            print(wall)
            axis = random.randint(1, 2)
            print(axis)
            if axis == 1:
                self.transform_lines(wall)
            else:
                self.transform_columns(wall)

    def get_wall(self):
        wall = []
        for i in range(1, len(self.matrix) - 2, 1):
            for j in range(1, len(self.matrix) - 2, 1):
                if self.matrix[i][j].color == -1:
                    wall.append(self.matrix[i][j])
        return wall

    def transform_lines(self, wall):
        if self.matrix[wall.y][wall.x - 1].color != -1 and self.matrix[wall.y][wall.x + 1].color != -1:
            if self.matrix[wall.y][wall.x - 1].color != self.matrix[wall.y][wall.x + 1].color:
                color = random.choice([self.matrix[wall.y][wall.x - 1].color, self.matrix[wall.y][wall.x + 1].color])
                self.spread_color(wall.x, wall.y, color)

    def transform_columns(self, wall):
        if self.matrix[wall.y - 1][wall.x].color != -1 and self.matrix[wall.y + 1][wall.x].color != -1:
            if self.matrix[wall.y - 1][wall.x].color != self.matrix[wall.y + 1][wall.x].color:
                color = random.choice([self.matrix[wall.y - 1][wall.x].color, self.matrix[wall.y + 1][wall.x].color])
                self.spread_color(wall.x, wall.y, color)

    # up = 1
    # right = 2
    # down = 3
    # left = 4
    def spread_color(self, x, y, color):
        self.matrix[y][x].color = color
        print(f"case {x} {y} reussi")

        # Vérification des indices avant de lancer les appels récursifs
        if x - 1 >= 0 and self.matrix[y][x - 1].color != color and self.matrix[y][x - 1].color != -1:
            self.spread_color(x - 1, y, color)

        if x + 1 < len(self.matrix[0]) and self.matrix[y][x + 1].color != color and self.matrix[y][x + 1].color != -1:
            self.spread_color(x + 1, y, color)

        if y - 1 >= 0 and self.matrix[y - 1][x].color != color and self.matrix[y - 1][x].color != -1:
            self.spread_color(x, y - 1, color)

        if y + 1 < len(self.matrix) and self.matrix[y + 1][x].color != color and self.matrix[y + 1][x].color != -1:
            self.spread_color(x, y + 1, color)


if __name__ == "__main__":
    game = Game()
    game.play()
