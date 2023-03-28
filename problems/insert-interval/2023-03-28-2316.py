# Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted 2023-03-28 23:16 UTC · Python · 79 ms · 17.6 MB

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = sorted([*intervals, newInterval], key=lambda x: x[0])
        output = [inserted[0]]
        for start_b, end_b in inserted[1:]:
            start_a, end_a = output[-1]
            if end_a >= start_b:
                output[-1] = start_a, max(end_a, end_b)
            else:
                output.append((start_b, end_b))
        return output
