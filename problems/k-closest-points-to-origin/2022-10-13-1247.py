# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Accepted 2022-10-13 12:47 UTC · Python · 1949 ms · 20.6 MB

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxpq, minpq = [], []
        for x, y in points:
            dist = math.sqrt(x ** 2 + y ** 2)
            if len(maxpq) < k:
                heapq.heappush(maxpq, (-dist, [x, y]))
            else:
                max_curr, [max_x, max_y] = maxpq[0]
                max_curr *= -1
                if max_curr <= dist:
                    heapq.heappush(minpq, (dist, [x, y]))
                else:
                    heapq.heappop(maxpq)
                    heapq.heappush(minpq, (dist, [x, y]))
                    min_curr, [min_x, min_y] = heapq.heappop(minpq)
                    heapq.heappush(maxpq, (-min_curr, [min_x, min_y]))
        return [x[1] for x in maxpq]
