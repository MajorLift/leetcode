# Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
# Accepted 2022-10-13 13:34 UTC · Python · 3275 ms · 52.7 MB

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        count = 0
        curr_start = +math.inf
        for start, end in intervals[::-1]:
            if end > curr_start:
                count += 1
            else:
                curr_start = start
        return count
