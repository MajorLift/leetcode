# Smallest String With Swaps
# https://leetcode.com/problems/smallest-string-with-swaps/
# Accepted 2023-04-30 01:51 UTC · Python · 1202 ms · 53 MB

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

    def groups(self):
        output = defaultdict(list)
        for node, root in enumerate(self.roots):
            self.roots[node] = self.find(root)
            output[self.roots[node]].append(node)
        return output
