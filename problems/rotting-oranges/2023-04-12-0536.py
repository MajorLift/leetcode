# Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# Accepted 2023-04-12 05:36 UTC · Python · 62 ms · 13.9 MB

class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(grid), len(grid[0])
        fresh = set()
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                fresh.add((i, j))
                grid[i][j] = 0
        prev = len(fresh)
        time = 0
        while fresh:
            for i, j in fresh:
                for direction in DIRECTIONS:
                    x, y = map(sum, zip((i, j), direction))
                    if 0 <= x < m and 0 <= y < n:
                        grid[i][j] |= grid[x][y] >> 1
            for i, j in list(fresh):
                grid[i][j] &= 1
                if grid[i][j] & 1:
                    grid[i][j] <<= 1
                    fresh.remove((i, j))
            if len(fresh) == prev:
                return -1
            prev = len(fresh)
            time += 1
        return time
