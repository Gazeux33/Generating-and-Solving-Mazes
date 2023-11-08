import pygame


class Tile:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = 0
        self.rect = pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.get_color(self.color), self.rect)

    def __repr__(self):
        return f"tuile({self.x},{self.y},{self.color})"

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
