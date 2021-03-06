from mazeplayer import MazePlayer
import random


class MazeGameEngine:
    def __init__(self, maze):
        self.player = MazePlayer(0, maze.length - 1)
        self.target = (random.randrange(maze.width), random.randrange(maze.length))
        self.maze = maze
        self.record = {"o": [(self.player.x, self.player.y)], "a": []}

    def get_number_of_steps(self):
        return len(self.record["a"])

    def get_observation(self):
        return self.player.x, self.player.y, self.target[0], self.target[1]

    def move_player(self, direction):
        assert self.player is not None
        assert self.target is not None
        self.player.x, self.player.y = self._move(self.player.x, self.player.y, direction)
        self.record["o"].append((self.player.x, self.player.y))
        self.record["a"] += [direction]

        return self.player.x == self.target[0] and self.player.y == self.target[1]

    def move_target(self, direction):
        next_position = self._move(self.target[0], self.target[1], direction)
        if next_position[0] == self.player.x and next_position[1] == self.player.y:
            return
        self.target = next_position

    def _move(self, position_x, position_y, direction):
        if direction == 0:
            if position_y > 0 and self.maze.grid[position_y, position_x] & 1 << direction:
                return position_x, position_y-1
        elif direction == 1:
            if position_x < self.maze.width and self.maze.grid[position_y, position_x] & 1 << direction:
                return position_x+1, position_y
        elif direction == 2:
            if position_y < self.maze.length and self.maze.grid[position_y, position_x] & 1 << direction:
                return position_x, position_y+1
        elif direction == 3:
            if position_x > 0 and self.maze.grid[position_y, position_x] & 1 << direction:
                return position_x-1, position_y
        return position_x, position_y
