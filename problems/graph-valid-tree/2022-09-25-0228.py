# Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree/
# Accepted 2022-09-25 02:28 UTC · Python · 244 ms · 15.5 MB

class UnionFind:
    def __init__(self, size):
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
        
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)
        for [x, y] in edges:
            if uf.isConnected(x, y):
                return False
            else:
                uf.union(x, y)
        return True
