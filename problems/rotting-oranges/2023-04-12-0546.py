# Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# Accepted 2023-04-12 05:46 UTC · Python · 69 ms · 14 MB

class Solution:
    def orangesRotting(self, grid: List[List[int]]):
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(grid), len(grid[0])
        # 0b00: unmarked fresh, 0b01: marked fresh, 0b10: rotten
        fresh = set()
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                fresh.add((i, j))
                grid[i][j] = 0
        prev = len(fresh)
        minutes = 0
        while fresh:    # break if no fresh oranges are left
            # mark fresh cells that are adjacent to a rotten orange
            for i, j in fresh:
                for direction in DIRECTIONS:
                    x, y = map(sum, zip((i, j), direction))
                    if 0 <= x < m and 0 <= y < n:
                        grid[i][j] |= grid[x][y] >> 1
            # update marked cells to rotten
            for i, j in list(fresh):
                if grid[i][j] & 1:
                    grid[i][j] <<= 1
                    fresh.remove((i, j))
            # break if number of fresh oranges is unchanged from previous minute
            if len(fresh) == prev:
                return -1
            prev = len(fresh)
            minutes += 1
        return minutes
