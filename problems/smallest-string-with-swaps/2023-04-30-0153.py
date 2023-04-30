# Smallest String With Swaps
# https://leetcode.com/problems/smallest-string-with-swaps/
# Accepted 2023-04-30 01:53 UTC · Python · 1283 ms · 53.3 MB

class Solution:
    def smallestStringWithSwaps(self, s, pairs: List[List[int]]) -> str:
        n, s = len(s), list(s)
        uf = UnionFind(n)
        for x, y in pairs:
            uf.union(x, y)
            
        groups = uf.groups()
        for k,v in groups.items():
            chars = sorted([s[idx] for idx in v])
            for idx in v:
                s[idx] = chars.pop(0)
        return ''.join(s)

class UnionFind:
    def __init__(self, size):
        self.roots = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        rootX, rootY = map(self.find, (x, y))
        if rootX == rootY: 
            return
        if self.rank[rootX] == self.rank[rootY]:
            self.roots[rootY] = rootX
            self.rank[rootX] += 1
        else:
            lesser, greater = sorted((rootX, rootY), key=lambda x: self.rank[x])
            self.roots[greater] = lesser

    def groups(self):
        output = defaultdict(list)
        for node, root in enumerate(self.roots):
            self.roots[node] = self.find(root)
            output[self.roots[node]].append(node)
        return output
