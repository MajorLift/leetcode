# Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/
# Accepted 2023-05-01 21:05 UTC · Python · 3595 ms · 44.7 MB

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        count = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([(max(vals[u], vals[v]), u, v) for u,v in edges])
        ans = n
        uf = UnionFind(n)
        for val, u, v in edges:
            root_u, root_v = map(uf.find, (u, v))
            if root_u == root_v: continue
            ans += count[root_u][val] * count[root_v][val]
            uf.union(u, v)
            count[root_u] = Counter({val: count[root_u][val] + count[root_v][val]})
            count[root_v] = Counter({val: 0})
        return ans

class UnionFind:
    def __init__(self, size):
        self.roots = list(range(size + 1))

    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        rootX, rootY = map(self.find, (x, y))
        if rootX == rootY:
            return
        self.roots[rootY] = rootX
