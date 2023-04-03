# Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/
# Accepted 2023-04-03 22:00 UTC · Python · 1348 ms · 52.2 MB

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end, ans = -math.inf, 0
        for start, end in intervals:
            if start < prev_end:
                ans += 1
            else:
                prev_end = end
        return ans
