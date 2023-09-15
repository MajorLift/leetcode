# Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/
# Accepted 2023-09-15 03:41 UTC · Python · 1063 ms (81.23%) · 16.8 MB (98.13%)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = set()
        dist = [(0, 0)] + [(+inf, i) for i in range(1, len(points))]
        cost = 0
        while dist:
            u_key, u_idx = heappop(dist)
            mst.add(u_idx)
            cost += u_key
            next_dist = []
            while dist:
                v_key, v_idx = heappop(dist)
                if v_idx in mst: continue
                w = Solution.manhattan(points[u_idx], points[v_idx])
                heappush(next_dist, (min(w, v_key), v_idx))
            dist = next_dist
        return cost

    @staticmethod
    def manhattan(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
