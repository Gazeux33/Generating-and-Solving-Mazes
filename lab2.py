import pygame
import sys
import random

class Game:
    def __init__(self):
        self.NB_CASE = 30
        self.TILE_SIZE = 20
        self.SIZE = self.WIDTH, self.HEIGHT = self.NB_CASE * self.TILE_SIZE, self.NB_CASE * self.TILE_SIZE

        pygame.init()
        self.display_screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Labyrinth")

        self.clock = pygame.time.Clock()

        self.grid = [[1 for _ in range(self.NB_CASE)] for _ in range(self.NB_CASE)]
        self.generate_maze(1, 1)
        self.grid[0][1] = 0
        self.grid[self.NB_CASE - 1][self.NB_CASE - 2] = 0

    def generate_maze(self, x, y):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < self.NB_CASE and 0 <= ny < self.NB_CASE and self.grid[ny][nx] == 1:
                self.grid[ny][nx] = 0
                self.grid[y + dy][x + dx] = 0
                self.generate_maze(nx, ny)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_grid()

            self.clock.tick(15)
            pygame.display.flip()

    def draw_grid(self):
        for y in range(self.NB_CASE):
            for x in range(self.NB_CASE):
                if self.grid[y][x] == 1:
                    color = (0, 0, 0)  # Black (wall)
                else:
                    color = (255, 255, 255)  # White (path)

                rect = pygame.Rect(x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                pygame.draw.rect(self.display_screen, color, rect)

if __name__ == "__main__":
    game = Game()
    game.game_loop()
