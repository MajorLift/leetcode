# Maximum Number of Events That Can Be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
# Accepted 2023-01-24 08:05 UTC · Python · 3292 ms · 61.5 MB

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        ans = 0
        i = 0
        d = 1
        pq = []
        while pq or i < len(events):
            if not pq:
                d = events[i][0]
            while i < len(events) and events[i][0] <= d:
                heappush(pq, events[i][1])
                i += 1
            heappop(pq)
            ans += 1
            d += 1
            while pq and pq[0] < d:
                heappop(pq)
        return ans
