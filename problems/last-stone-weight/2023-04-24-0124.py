# Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/
# Accepted 2023-04-24 01:24 UTC · Python · 19 ms · 13.8 MB

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while stones:
            if len(stones) == 1:
                return -heappop(stones)
            x, y = -heappop(stones), -heappop(stones)
            if x > y:
                heappush(stones, -(x - y))
        return 0
