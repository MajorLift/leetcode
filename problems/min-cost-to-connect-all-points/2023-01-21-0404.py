# Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Accepted 2023-01-21 04:04 UTC · Python · 1716 ms · 129.1 MB

Coordinates = tuple[int, int]

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        numVertices = len(points)
        edges = [(self.manhattan(a, b), tuple(a), tuple(b)) \
            for a, b in combinations(points, 2)]
        heapify(edges)

        cost = 0
        MST = UnionFind()
        while MST.numEdges < numVertices - 1:
            dist, a, b = heappop(edges)
            if MST.connected(a, b):
                continue
            MST.union(a, b)
            cost += dist
        return cost
    
    def manhattan(self, a: Coordinates, b: Coordinates) -> int:
        (x1, y1), (x2, y2) = a, b
        return abs(x1 - x2) + abs(y1 - y2)

class UnionFind:
    def __init__(self):
        self.roots: dict[Coordinates, Coordinates] = dict()
        self.numEdges = 0

    def find(self, x: Coordinates) -> Coordinates:
        if x not in self.roots or x == self.roots[x]:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x: Coordinates, y: Coordinates) -> None:
        if x not in self.roots:
            self.roots[x] = x
        if y not in self.roots:
            self.roots[y] = y
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.roots[rootY] = rootX
            self.numEdges += 1
        
    def connected(self, x: Coordinates, y: Coordinates) -> bool:
        rootX, rootY = self.find(x), self.find(y)
        return rootX == rootY
