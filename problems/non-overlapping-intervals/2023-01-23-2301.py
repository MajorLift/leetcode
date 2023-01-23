# Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
# Accepted 2023-01-23 23:01 UTC · Python · 1514 ms · 52.1 MB

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        prev_end = -math.inf
        for start, end in intervals:
            if start < prev_end:
                ans += 1
            else:
                prev_end = end
        return ans
