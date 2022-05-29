# K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Accepted 2022-05-29 06:47 UTC · Python · 851 ms · 20.5 MB

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(-math.sqrt(point[0] ** 2 + point[1] ** 2), i) for i, point in enumerate(points)]
        heap = [dist[j] for j in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            if dist[i][0] > heap[0][0]:
                heapq.heappushpop(heap, (dist[i][0], i))
        return [points[i] for (_, i) in heap]
