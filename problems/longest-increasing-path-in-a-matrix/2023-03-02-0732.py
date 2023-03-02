# Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Accepted 2023-03-02 07:32 UTC · Python · 448 ms · 19.1 MB

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(r, c):
            return max(dfs(i, j) + 1 
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[r][c] 
                else 1 
                for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)))
        return max(dfs(i, j) for i in range(m) for j in range(n))
