# Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
# Accepted 2022-12-30 00:58 UTC · Python · 132 ms · 16.4 MB

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n and grid[r][c] == 1):
                return 0
            grid[r][c] = 0
            return 1 + dfs(r - 1 , c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area
