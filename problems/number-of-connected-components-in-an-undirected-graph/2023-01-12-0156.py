# Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Accepted 2023-01-12 01:56 UTC · Python · 106 ms · 15.3 MB

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return len([x for i, x in enumerate(uf.root) if x == i])
