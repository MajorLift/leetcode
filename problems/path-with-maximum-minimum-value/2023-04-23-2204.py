# Path With Maximum Minimum Value
# https://leetcode.com/problems/path-with-maximum-minimum-value/
# Accepted 2023-04-23 22:04 UTC · Python · 3390 ms · 20.4 MB

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIRECTIONS = ((1, 0), (0, -1), (-1, 0), (0, 1))
        
        hashmap = defaultdict(set)
        for i, j in product(range(m), range(n)):
            hashmap[grid[i][j]].add((i, j))
        uf, visited = UnionFind(m, n), set()
        for k in sorted(hashmap.keys(), reverse=True):
            for x, y in hashmap[k]:
                visited.add((x, y))
                for i, j in (map(sum, zip((x, y), d)) for d in DIRECTIONS):
                    if not (0 <= i < m and 0 <= j < n) \
                        or (i, j) not in visited:
                        continue
                    uf.union((x, y), (i, j))
                if uf.connected((0, 0), (m - 1, n - 1)):
                    return k     

class UnionFind:

    def __init__(self, m, n):
        self.root = {(i, j): (i, j) for i, j in product(range(m), range(n))}

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        self.root[rootY] = rootX
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
