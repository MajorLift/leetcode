# Redundant Connection
# https://leetcode.com/problems/redundant-connection/
# Accepted 2023-01-11 15:42 UTC · Python · 58 ms · 14.4 MB

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for u, v in edges:
            if uf.connected(u - 1, v - 1):
                return [u, v]
            uf.union(u - 1, v - 1)
