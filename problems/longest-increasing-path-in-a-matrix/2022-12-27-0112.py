# Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Accepted 2022-12-27 01:12 UTC · Python · 467 ms · 18.7 MB

from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        @cache
        def dfs(r, c):
            return max(1 + dfs(i, j) if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[r][c] else 0 \
                for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)))
        
        return 1 + max(dfs(i, j) for i in range(m) for j in range(n))
