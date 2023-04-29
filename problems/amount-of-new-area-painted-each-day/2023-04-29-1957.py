# Amount of New Area Painted Each Day
# https://leetcode.com/problems/amount-of-new-area-painted-each-day/
# Accepted 2023-04-29 19:57 UTC · Python · 3677 ms · 69.6 MB

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        n = len(paint)
        maxEnd = -inf
        intervals = []
        for idx, [start, end] in enumerate(paint):
            heappush(intervals, (start, idx, 'START'))
            heappush(intervals, (end, idx, 'END'))
            maxEnd = max(maxEnd, end)

        worklog, pq, visited = [0] * n, [], set()
        for pos in range(maxEnd + 1):
            while intervals and intervals[0][0] == pos:
                _, idx, _type = heappop(intervals)
                if _type == 'START':
                    heappush(pq, idx)
                elif _type == 'END':
                    visited.add(idx)
            
            while pq and pq[0] in visited:
                heappop(pq)
            if pq:
                worklog[pq[0]] += 1

        return worklog
