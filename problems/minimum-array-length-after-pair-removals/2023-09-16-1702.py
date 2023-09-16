# Minimum Array Length After Pair Removals
# https://leetcode.com/problems/minimum-array-length-after-pair-removals/
# Accepted 2023-09-16 17:02 UTC · Python · 1200 ms (25%) · 31.8 MB (25%)

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        pq = [-v for v in cnt.values()]
        heapify(pq)
        while len(pq) > 1:
            a, b = -heappop(pq), -heappop(pq)
            if a > 1: heappush(pq, -a + 1)
            if b > 1: heappush(pq, -b + 1)
        return -(pq or [0])[0]
