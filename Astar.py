from dataclasses import dataclass


import pygame
import heapq


@dataclass
class Node:
    coord: (int, int)
    loss: int
    heuristic: int
    parent: 'Node' = None

    def __lt__(self, other):
        return (self.loss + self.heuristic) < (other.loss + other.heuristic)


@dataclass
class Astar:
    game: object
    start: (int, int)
    end: (int, int)
    screen: pygame.Surface

    def __init__(self, game, start, end):
        self.game = game
        self.matrix = self.game.matrix
        self.start_node = Node(start, 0, self.heuristic(start, end))
        self.end_node = Node(end, 0, 0)  # The end node has no heuristic as it's the goal
        self.open_set = [self.start_node]
        self.closed_set = set()

    @staticmethod
    def heuristic(node, end):
        return abs(end[0] - node[0]) + abs(end[1] - node[1])

    def astar(self):
        while self.open_set:
            current_node = heapq.heappop(self.open_set)  # Get the node with the lowest total cost
            if current_node.coord == self.end_node.coord:
                # Path found
                return self.reconstruct_path(current_node)

            self.closed_set.add(current_node.coord)

            for neighbor_coord in self.get_neighbors(current_node):
                neighbor = Node(neighbor_coord, 0, 0, current_node)
                if neighbor.coord in self.closed_set:
                    continue  # Ignore already visited nodes

                tentative_loss = current_node.loss + 1  # Assuming each step has a cost of 1

                if neighbor not in self.open_set or tentative_loss < neighbor.loss:
                    neighbor.loss = tentative_loss
                    neighbor.heuristic = tentative_loss + self.heuristic(neighbor.coord, self.end_node.coord)
                    if neighbor not in self.open_set:
                        heapq.heappush(self.open_set, neighbor)

        return None  # No path found

    def get_neighbors(self, node):
        neighbors = []
        y, x = node.coord
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (abs(i) + abs(j) == 1
                        and self.game.is_wall_in_range(y + i, x + j)
                        and self.matrix[y + i][x + j] != -1):
                    neighbors.append((y + i, x + j))
        return neighbors

    def reconstruct_path(self, node):
        path = []
        while node:
            path.insert(0, node.coord)  # Insert at the beginning to reverse the path
            node = node.parent
        return path
