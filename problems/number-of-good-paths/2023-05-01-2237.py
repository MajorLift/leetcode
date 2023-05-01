# Number of Good Paths
# https://leetcode.com/problems/number-of-good-paths/
# Accepted 2023-05-01 22:37 UTC · Python · 2202 ms · 43.2 MB

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        count = [{vals[i]: 1} for i in range(n)]
        edges = sorted([(max(vals[u], vals[v]), u, v) for u,v in edges])

        ans = n
        uf = UnionFind(n)
        for w, u, v in edges:
            root_u, root_v = map(uf.find, (u, v))
            if root_u == root_v: continue
            # connects subtrees root_u, root_v, each guaranteed to be
            # comprised only of nodes s.t. vals[node] <= w
            # (edge uv is a cut for bipartite subtree root_u | root_v)
            uf.union(u, v)
            # combinations: cross product
            # 0 if vals[u] < val or vals[v] < val
            ans += count[root_u].get(w, 0) \
                    * count[root_v].get(w, 0)
            # update number of nodes s.t. vals[node] == w 
            # contained in subtree root_u | root_v
            count[root_u][w] = count[root_u].get(w, 0) \
                                + count[root_v].get(w, 0)
            count[root_v][w] = 0
        
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
        if rootX == rootY: return
        self.roots[rootY] = rootX
