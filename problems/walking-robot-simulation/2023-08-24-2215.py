# Walking Robot Simulation
# https://leetcode.com/problems/walking-robot-simulation/
# Accepted 2023-08-24 22:15 UTC · Python · 502 ms · 22.7 MB

class Solution:
    DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.coord = (0, 0)
        self.dir_idx = 0
        self.max_dist = 0
        self.obstacles = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -2:
                self.dir_idx = (self.dir_idx - 1) % 4
            elif command == -1:
                self.dir_idx = (self.dir_idx + 1) % 4
            else:
                for k in range(command):
                    nxt_coord = tuple(map(sum, zip(self.DIRECTIONS[self.dir_idx], self.coord)))
                    if nxt_coord in self.obstacles:
                        break
                    self.coord = nxt_coord
                    self.max_dist = max(self.max_dist, self.euclid_dist())

        return self.max_dist

    def euclid_dist(self):
        return sum(map(lambda x: x ** 2, self.coord))
