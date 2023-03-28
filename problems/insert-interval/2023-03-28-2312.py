# Insert Interval
# https://leetcode.com/problems/insert-interval/
# Accepted 2023-03-28 23:12 UTC · Python · 80 ms · 17.5 MB

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = sorted([*intervals, newInterval], key=lambda x: x[0])
        output = [inserted[0]]
        i, j = 0, 1
        while j < len(inserted):
            [start_a, end_a], [start_b, end_b] = output[-1], inserted[j]
            if end_a >= start_b:
                output[-1] = (start_a, max(end_a, end_b))
            else:
                output.append((start_b, end_b))
                i += 1
            j += 1
        return output
