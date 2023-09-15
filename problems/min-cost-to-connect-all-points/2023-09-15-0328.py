# Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Accepted 2023-09-15 03:28 UTC · Python · 1034 ms (81.99%) · 17.1 MB (95.36%)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = set()
        dist = [(0, 0)] + [(+inf, i) for i in range(1, len(points))]
        heapify(dist)
        cost = 0
        while dist:
            u_key, u_idx = heappop(dist)
            mst.add(u_idx)
            cost += u_key
            next_dist = []
            while dist:
                v_key, v_idx = heappop(dist)
                if v_idx not in mst:
                    w = Solution.manhattan(points[u_idx], points[v_idx])
                    heappush(next_dist, (min(w, v_key), v_idx))
            dist = next_dist
        return cost

    @staticmethod
    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
