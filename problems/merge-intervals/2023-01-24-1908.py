# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Accepted 2023-01-24 19:08 UTC · Python · 140 ms · 18.9 MB

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        for start, end in intervals:
            if not output or start > output[-1][1]:
                output.append([start, end])
            elif start <= output[-1][1] < end:
                prev_start, _ = output.pop()
                output.append([prev_start, end])
        return output
