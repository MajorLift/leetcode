# Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Accepted 2022-09-25 02:34 UTC · Python · 244 ms · 15.4 MB

class UnionFind:
    def __init__(self, size):
        self.count = size
        self.root = [i for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for [a, b] in edges:
            uf.union(a, b)
        return uf.count
