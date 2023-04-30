# Remove Max Number of Edges to Keep Graph Fully Traversable
# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
# Accepted 2023-04-30 03:24 UTC · Python · 2408 ms · 75.2 MB

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_a, uf_b = UnionFind(n), UnionFind(n)
        cnt = 0
        for _type, u, v in edges:
            if _type == 3:
                cnt += uf_a.union(u, v) | uf_b.union(u, v)
        for _type, u, v in edges:
            if _type == 1:
                cnt += uf_a.union(u, v)
            if _type == 2:
                cnt += uf_b.union(u, v)
        if uf_a.numGroups == 1 and uf_b.numGroups == 1:
            return len(edges) - cnt
        return -1

class UnionFind:
    def __init__(self, size):
        self.roots = list(range(size + 1))
        self.numGroups = size
        
    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        rootX, rootY = map(self.find, (x, y))
        if rootX == rootY:
            return 0
        self.roots[rootY] = rootX
        self.numGroups -= 1
        return 1
