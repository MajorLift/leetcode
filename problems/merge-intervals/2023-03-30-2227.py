# Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Accepted 2023-03-30 22:27 UTC · Python · 155 ms · 18.6 MB

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[1])
        output = deque([intervals[-1]])
        for i in range(len(intervals) - 2, -1, -1):
            (start_l, end_l), (start_r, end_r) = intervals[i], output[0]
            if start_r <= end_l:
                output[0] = min(start_l, start_r), end_r
            else:
                output.appendleft((start_l, end_l))
        return output
