# Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Accepted 2023-03-02 20:30 UTC · Python · 464 ms · 18.7 MB

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(r, c):
            return max(dfs(i, j) + 1 
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[r][c] 
                else 1 
                for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)))
        return max(dfs(i, j) for i, j in product(range(m), range(n)))
