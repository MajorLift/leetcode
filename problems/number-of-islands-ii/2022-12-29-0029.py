# Number of Islands II
# https://leetcode.com/problems/number-of-islands-ii/
# Accepted 2022-12-29 00:29 UTC · Python · 590 ms · 19.7 MB

class UnionFind:
    def __init__(self, size):
        self.count = 0
        self.root = dict()

    def add(self, x):
        if x not in self.root:
            self.root[x] = x
            self.count += 1
        
    def find(self, x):
        if x not in self.root:
            return None
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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        uf = UnionFind(m * n)
        output = [0 for _ in range(len(positions))]
        for idx, [r, c] in enumerate(positions):
            grid[r][c] = 1
            uf.add((r, c))
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    uf.union((r, c), (i, j))
            output[idx] = uf.count
        return output
