# Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water/
# Accepted 2023-01-25 07:10 UTC · Python · 98 ms · 14.7 MB

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([(0, 0)])
        pq = [(grid[0][0], 0, 0)]
        history = []
        while pq:
            level, i, j = heappop(pq)
            history.append(level)
            if i == j == n - 1:
                break
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    heappush(pq, (grid[x][y], x, y))
                    visited.add((x, y))
        return max(history)
