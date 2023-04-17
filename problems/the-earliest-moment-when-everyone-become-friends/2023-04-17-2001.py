# The Earliest Moment When Everyone Become Friends
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
# Accepted 2023-04-17 20:01 UTC · Python · 99 ms · 14.2 MB

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        for timestamp, x, y in sorted(logs, key=lambda x: x[0]):
            uf.union(x, y)
            if uf.groups == 1:
                return timestamp
        return -1

class UnionFind:
    def __init__(self, size = 0):
        self.root = list(range(size))
        self.groups = size
        self.edges = 0

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
            self.groups -= 1
            self.edges += 1
