# Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/
# Accepted 2023-01-26 01:29 UTC · Python · 181 ms · 14.6 MB

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([(0, 0)])
        pq = [(grid[0][0], 0, 0)]
        time = 0
        while pq:
            w, i, j = heappop(pq)
            time = w
            if i == j == n - 1:
                break
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    heappush(pq, (max(grid[x][y], time), x, y))
                    visited.add((x, y))
        return time
