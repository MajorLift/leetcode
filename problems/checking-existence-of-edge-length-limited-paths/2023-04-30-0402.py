# Checking Existence of Edge Length Limited Paths
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
# Accepted 2023-04-30 04:02 UTC · Python · 2418 ms · 62.9 MB

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        queries = sorted(
            [[*e, i] for i,e in enumerate(queries)], 
            key=lambda x: x[2])
        uf = UnionFind(n)
        answer = [False] * len(queries)
        for p, q, limit, idx in queries:
            while edgeList and edgeList[0][2] < limit:
                u, v, _ = edgeList.pop(0)
                uf.union(u, v)
            answer[idx] = uf.isConnected(p, q)
        return answer

class UnionFind:
    def __init__(self, size):
        self.roots = list(range(size))

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

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
