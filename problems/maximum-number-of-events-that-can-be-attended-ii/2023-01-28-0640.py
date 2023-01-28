# Maximum Number of Events That Can Be Attended II
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
# Accepted 2023-01-28 06:40 UTC · Python · 1011 ms · 200.1 MB

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])

        @cache
        def dp(idx = 0, quota = k):
            if quota == 0 or idx >= n: 
                return 0
            start, end, val = events[idx]
            next_idx = bisect_right(events, end, lo=idx, key=lambda x: x[0])
            return max(dp(idx + 1, quota), val + dp(next_idx, quota - 1))

        return dp(0, k)
