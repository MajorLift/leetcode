# Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# Accepted 2023-04-12 06:08 UTC · Python · 73 ms · 13.9 MB

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
        minutes = 0
        while fresh:    # break if no fresh oranges are left
            # mark cells adjacent to rotten oranges
            marked = []
            for i, j in fresh:
                for direction in DIRECTIONS:
                    x, y = map(sum, zip((i, j), direction))
                    if 0 <= x < m and 0 <= y < n:
                        grid[i][j] |= grid[x][y] >> 1
                if grid[i][j] & 1:
                    marked.append((i, j))
            # update marked cells to rotten
            for i, j in marked:
                grid[i][j] <<= grid[i][j] & 1
                # grid[i][j] &= 0b11    # and mask unnecessary
                fresh.remove((i, j))
            # break if state is unchanged from previous minute
            if not marked:
                return -1
            minutes += 1
        return minutes
