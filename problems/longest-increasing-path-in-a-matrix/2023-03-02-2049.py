# Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Accepted 2023-03-02 20:49 UTC · Python · 460 ms · 14.8 MB

class Solution:
    """
    Reversed Kahn's Algorithm TopSort
    source: (r, c)
    target: (i, j)
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        outdegree = [[0 for _ in range(n)] for _ in range(m)]
        for r, c in product(range(m), range(n)):
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[r][c]:
                    outdegree[r][c] += 1

        leaves = [(i, j) 
            for i, j in product(range(m), range(n)) 
            if outdegree[i][j] == 0]
        dist = 0
        while leaves:
            dist += 1
            leaves_next = []
            for i, j in leaves:
                for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= r < m and 0 <= c < n and matrix[i][j] > matrix[r][c]:
                        outdegree[r][c] -= 1
                        if outdegree[r][c] == 0:
                            leaves_next.append((r, c))
            leaves = leaves_next
        return dist
