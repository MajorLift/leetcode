# Maximum Number of Events That Can Be Attended
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
# Accepted 2023-01-24 08:08 UTC · Python · 1219 ms · 48.8 MB

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: -x[0])
        ans = 0
        d = 1
        pq = []
        while pq or events:
            if not pq:
                d = events[-1][0]
            while events and events[-1][0] <= d:
                heappush(pq, events.pop()[1])
            heappop(pq)
            ans += 1
            d += 1
            while pq and pq[0] < d:
                heappop(pq)
        return ans
