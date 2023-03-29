# Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted 2023-03-29 20:11 UTC · Python · 81 ms · 17.2 MB

class Solution:    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = [], []
        start_new, end_new = newInterval
        for i, (start, end) in enumerate(intervals):
            if start > end_new:
                r = intervals[i:]
                break
            elif end < start_new:
                l.append(intervals[i])
            else:
                start_new, end_new = min(start, start_new), max(end, end_new)
        return l + [[start_new, end_new]] + r
