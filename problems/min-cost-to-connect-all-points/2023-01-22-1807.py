# Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Accepted 2023-01-22 18:07 UTC · Python · 1602 ms · 14.6 MB

class Node:
    def __init__(self, idx, key):
        self.idx = idx
        self.key = key

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return "(idx: %s, dist: %s)" % (self.idx, self.key)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        numVertices = len(points)
        mst = set()
        dist = [Node(0, 0)] + [Node(i, +math.inf) for i in range(1, numVertices)]
        
        cost = 0
        while dist:
            heapify(dist)
            u = heappop(dist)
            mst.add(u.idx)
            cost += u.key
            for v in dist:
                if v.idx not in mst:
                    w = self.manhattan(points[u.idx], points[v.idx])
                    if w < v.key:
                        v.key = w
        return cost
    
    def manhattan(self, a, b):
        (x1, y1), (x2, y2) = a, b
        return abs(x1 - x2) + abs(y1 - y2)
