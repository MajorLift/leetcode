# Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
# Accepted 2023-04-03 21:58 UTC · Python · 1316 ms · 51.9 MB

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        curr_end, erased = intervals[0][1], 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < curr_end:
                erased += 1
            else:
                curr_end = intervals[i][1]
        return erased
