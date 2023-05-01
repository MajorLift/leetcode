# Path With Maximum Minimum Value
# https://leetcode.com/problems/path-with-maximum-minimum-value/
# Accepted 2023-05-01 23:27 UTC · Python · 2967 ms · 21.5 MB

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = map(len, (grid, grid[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        coords = defaultdict(list)
        for i, j in product(range(m), range(n)):
            coords[grid[i][j]].append((i, j))
        uf = UnionFind(m, n)
        marked = set()
        for val in sorted(coords.keys(), reverse=True):
            for r, c in coords[val]:
                marked.add((r, c))
                for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                    if not (0 <= i < m and 0 <= j < n) \
                        or (i, j) not in marked:
                        continue
                    uf.union((r, c), (i, j))
            if uf.isConnected((0, 0), (m - 1, n - 1)):
                return val
        return min(grid[0][0], grid[-1][-1])
        
class UnionFind:
    def __init__(self, m, n):
        self.roots = {(i, j): (i, j) for i, j in product(range(m), range(n))}
    
    def find(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        rootX, rootY = map(self.find, (x, y))
        if rootX != rootY:
            self.roots[rootY] = rootX

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
