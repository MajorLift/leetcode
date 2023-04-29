# Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/
# Accepted 2023-04-29 22:04 UTC · Python · 2052 ms · 26 MB

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = map(len, (heights, heights[0]))
        if m == n == 1:
            return 0
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        edges = []
        for r, c in product(range(m), range(n)):
            for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                edges.append((abs(heights[r][c] - heights[i][j]), (r, c), (i, j)))
        edges.sort()

        uf = UnionFind(m, n)
        for effort, x, y in edges:
            uf.union(x, y)
            if uf.isConnected((0, 0), (m - 1, n - 1)):
                return effort
        return -1
        

class UnionFind:
    def __init__(self, m, n):
        self.roots = [[(i, j) for j in range(n)] for i in range(m)]
        
    def find(self, x):
        i, j = x
        if self.roots[i][j] == (i, j):
            return (i, j)
        self.roots[i][j] = self.find(self.roots[i][j])
        return self.roots[i][j]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        i, j = rootY
        self.roots[i][j] = rootX

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
