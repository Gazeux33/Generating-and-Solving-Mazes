import pygame


class GroupTile:
    def __init__(self, *args):
        self.group = []
        [self.group.append(tile) for tile in args]

    def __add__(self, other):
        new_group = GroupTile()
        new_group.group += self.group
        new_group.group += other.group
        return new_group

    def __repr__(self):
        return f"Group:{len(self.group)}"
