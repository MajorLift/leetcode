# Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/
# Accepted 2022-10-19 22:24 UTC · Python · 62 ms · 13.8 MB

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while maxheap:
            if len(maxheap) > 1:
                y, x = -heapq.heappop(maxheap), -heapq.heappop(maxheap)
                if y > x:
                    heapq.heappush(maxheap, -(y - x))
            else:
                return -maxheap[0]
        return 0
