# Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Accepted 2022-12-28 02:37 UTC · Python · 284 ms · 16.6 MB

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(row, col):
            grid[row][col] = "0"
            for i, j in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                    dfs(i, j)
                    
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        return ans
