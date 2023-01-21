# Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Accepted 2023-01-21 04:14 UTC · Python · 859 ms · 67.6 MB

from typing import TypeVar, Generic

Coordinates = tuple[int, int]
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        numVertices = len(points)
        edges = [(self.manhattan(a, b), a, b) \
            for a, b in itertools.combinations([tuple(point) for point in points], 2)]
        heapq.heapify(edges)

        cost = 0
        MST = UnionFind[Coordinates]()
        while MST.numEdges < numVertices - 1:
            dist, a, b = heapq.heappop(edges)
            if MST.connected(a, b):
                continue
            MST.union(a, b)
            cost += dist
        return cost
    
    def manhattan(self, a: Coordinates, b: Coordinates) -> int:
        (x1, y1), (x2, y2) = a, b
        return abs(x1 - x2) + abs(y1 - y2)

T = TypeVar('T')
class UnionFind(Generic[T]):
    def __init__(self):
        self.roots: dict[T, T] = dict()
        self.numEdges = 0

    def find(self, x: T) -> T:
        if x not in self.roots or x == self.roots[x]:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x: T, y: T) -> None:
        if x not in self.roots:
            self.roots[x] = x
        if y not in self.roots:
            self.roots[y] = y
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.roots[rootY] = rootX
            self.numEdges += 1
        
    def connected(self, x: T, y: T) -> bool:
        rootX, rootY = self.find(x), self.find(y)
        return rootX == rootY
