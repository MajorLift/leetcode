# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Accepted 2022-12-06 00:30 UTC · Python · 2079 ms · 20.7 MB

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kclosest, candidates = [], []
        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            if len(kclosest) < k:
                heapq.heappush(kclosest, (-dist, [x, y]))
            else:
                max_curr, [max_x, max_y] = kclosest[0]
                max_curr *= -1
                if max_curr <= dist:
                    heapq.heappush(candidates, (dist, [x, y]))
                else:
                    min_curr, [min_x, min_y] = heapq.heappushpop(candidates, (dist, [x, y]))
                    heapq.heappushpop(kclosest, (-min_curr, [min_x, min_y]))
        return [x[1] for x in kclosest]
