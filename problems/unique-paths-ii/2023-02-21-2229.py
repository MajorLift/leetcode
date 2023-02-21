# Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/
# Accepted 2023-02-21 22:29 UTC · Python · 55 ms · 14 MB

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        grid = [[not bool(grid[i][j]) for j in range(n)] for i in range(m)]
        memo = [[int(i * j == 0) for j in range(n)] for i in range(m)]
        flag = False
        for i in range(m):
            if not grid[i][0]:
                flag = True
            if flag:
                memo[i][0] = int(not flag)
        flag = False
        for j in range(n):
            if not grid[0][j]:
                flag = True
            if flag:
                memo[0][j] = int(not flag)
                
        for i, j in product(range(1, m), range(1, n)):
            memo[i][j] = ((memo[i - 1][j] if grid[i - 1][j] else 0) 
                + (memo[i][j - 1] if grid[i][j - 1] else 0))
        return memo[-1][-1] if grid[-1][-1] else 0
