# Walking Robot Simulation
# https://leetcode.com/problems/walking-robot-simulation/
# Accepted 2023-08-25 03:24 UTC · Python · 403 ms · 23 MB

class Solution:
    DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        self.coord = (0, 0)
        self.dir_idx = 0
        self.max_dist = 0
        self.obstacles_x, self.obstacles_y = defaultdict(list), defaultdict(list)
        for x, y in sorted(obstacles):
            self.obstacles_x[x].append(y)
            self.obstacles_y[y].append(x)
        
        for command in commands:
            if command == -2:
                self.dir_idx = (self.dir_idx - 1) % 4
            elif command == -1:
                self.dir_idx = (self.dir_idx + 1) % 4
            else:
                offset = map(lambda e: command * e, self.DIRECTIONS[self.dir_idx])
                nxt_coord = tuple(map(sum, zip(offset, self.coord)))
                self.coord = self.check_obstacles(nxt_coord)
                print(nxt_coord, self.coord)
                self.max_dist = max(self.max_dist, self.euclid_dist())
            # print(command, self.coord, self.dir_idx, self.max_dist)
        return self.max_dist

    def check_obstacles(self, dst: tuple[int, int]) -> tuple[int, int]:
        (x0, y0), (x1, y1) = self.coord, dst
        if x0 == x1:
            if y0 <= y1:
                for yt in self.obstacles_x[x0]:
                    if y0 <= yt <= y1 and not (x0 == y0 == yt == 0):
                        return (x0, yt - 1)
            else:
                for yt in self.obstacles_x[x0][::-1]:
                    if y1 <= yt <= y0 and not (x0 == y0 == yt == 0):
                        return (x0, yt + 1)
        if y0 == y1:
            if x0 <= x1:
                for xt in self.obstacles_y[y0]:
                    if x0 <= xt <= x1 and not (x0 == y0 == xt == 0):
                        return (xt - 1, y0)
            else:
                for xt in self.obstacles_y[y0][::-1]:
                    if x1 <= xt <= x0 and not (x0 == y0 == xt == 0):
                        return (xt + 1, y0)
        return dst

    def euclid_dist(self) -> int:
        return sum(map(lambda x: x ** 2, self.coord))
