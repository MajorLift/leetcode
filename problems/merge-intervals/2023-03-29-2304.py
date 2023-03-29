# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Accepted 2023-03-29 23:04 UTC · Python · 150 ms · 18.8 MB

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [tuple(intervals[0])]
        for start, end in intervals[1:]:
            start_prev, end_prev = output[-1]
            if start <= end_prev:
                output[-1] = min(start_prev, start), max(end_prev, end)
            else:
                output.append((start, end))
        return output
