# Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# Accepted 2023-01-07 04:29 UTC · Python · 51 ms · 13.8 MB

from itertools import product
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = [(i, j) for i, j in product(range(m), range(n)) if grid[i][j] == 1]
        if not fresh:
            return 0
        rotten = [(i, j) for i, j in product(range(m), range(n)) if grid[i][j] == 2]
        if not rotten:
            return -1

        count, time = len(fresh), 0
        queue = deque([*rotten])
        while queue:
            nextQueue = []
            while queue:
                r, c = queue.popleft()
                for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        grid[i][j] = 2
                        count -= 1
                        nextQueue.append((i, j))
            queue += nextQueue
            if queue:
                time += 1

        return time if count == 0 else -1
