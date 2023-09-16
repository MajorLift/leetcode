# Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/
# Accepted 2023-09-16 01:02 UTC · Python · 1814 ms (24.48%) · 26 MB (5.05%)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = map(len, (heights, heights[0]))
        if m == n == 1: 
            return 0
        SRC, DST = (0, 0), (m - 1, n - 1)
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        pq = []   # (w, u, v)
        for r, c in product(range(m), range(n)):
            for i, j in (map(sum, zip((r, c), d)) for d in DIRS):
                if not (0 <= i < m and 0 <= j < n): continue
                heappush(pq, (abs(heights[r][c] - heights[i][j]), (r, c), (i, j)))

        uf = UnionFind(m, n)
        while pq:
            effort, u, v = heappop(pq)
            uf.union(u, v)
            if uf.is_connected(SRC, DST):
                return effort
        return -1

class UnionFind:
    def __init__(self, m: int, n: int):
        self.roots = [[(i, j) for j in range(n)] 
                        for i in range(m)]
    
    def find(self, x: tuple[int, int]) -> tuple[int, int]:
        i, j = x
        if self.roots[i][j] == (i, j):
            return (i, j)
        self.roots[i][j] = self.find(self.roots[i][j])
        return self.roots[i][j]

    def union(self, x: tuple[int, int], y: tuple[int, int]):
        rootX, rootY = map(self.find, (x, y))
        i, j = rootY
        self.roots[i][j] = rootX
    
    def is_connected(self, x: tuple[int, int], y: tuple[int, int]) -> bool:
        return self.find(x) == self.find(y)
