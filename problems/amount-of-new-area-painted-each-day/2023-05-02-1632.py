# Amount of New Area Painted Each Day
# https://leetcode.com/problems/amount-of-new-area-painted-each-day/
# Accepted 2023-05-02 16:32 UTC · Python · 3295 ms · 68.1 MB

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        intervals = []
        maxEnd = -inf
        for day, (start, end) in enumerate(paint):
            heappush(intervals, (start, day, 'START'))
            heappush(intervals, (end, day, 'END'))
            maxEnd = max(maxEnd, end)
        
        worklog, pq, visited = [0] * len(paint), [], set()
        for pos in range(maxEnd + 1):
            while intervals and intervals[0][0] == pos:
                _, day, _type = heappop(intervals)
                if _type == 'START':
                    heappush(pq, day)
                if _type == 'END':
                    visited.add(day)

            while pq and pq[0] in visited:
                heappop(pq)
            if pq:
                worklog[pq[0]] += 1

        return worklog
