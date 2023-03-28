# Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted 2023-03-28 23:33 UTC · Python · 83 ms · 17.5 MB

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = intervals[:]
        bisect.insort_right(inserted, newInterval, key=lambda x: x[0])
        output = [inserted[0]]
        for start_r, end_r in inserted[1:]:
            start_l, end_l = output[-1]
            if end_l >= start_r:
                output[-1] = start_l, max(end_l, end_r)
            else:
                output.append((start_r, end_r))
        return output
