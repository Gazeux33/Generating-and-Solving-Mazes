import sys
import pygame

COLORS = {"-1": "#000000",
          "0": "#FFFFFF",
          "1": "#4749FC",
          "2": "#BC47FC",
          "3": "#F747FC",
          "4": "#5CFC47",
          "5": "#F4FC47",
          "6": "#F4FC47",
          "7": "#FF0F01",
          "8": "#396E1F",
          "9": "#141075", }


class Game:
    def __init__(self):
        self.NB_CASE = 19
        self.TILE_SIZE = 10
        self.SIZE = self.NB_CASE * self.TILE_SIZE, self.NB_CASE * self.TILE_SIZE

        pygame.init()
        self.display_screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Labyrinth")

        self.clock = pygame.time.Clock()

        self.matrix = [[-1 for y in range(self.NB_CASE)] for i in range(self.NB_CASE)]

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
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                rect = pygame.Rect(j * self.TILE_SIZE, i * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                color = self.matrix[i][j]
                pygame.draw.rect(self.display_screen, COLORS[str(color)], rect)


game = Game()
game.play()