# Amount of New Area Painted Each Day
# https://leetcode.com/problems/amount-of-new-area-painted-each-day/
# Accepted 2023-04-29 20:15 UTC · Python · 2074 ms · 64.4 MB

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        worklog, line = [0] * len(paint), defaultdict(int)
        for i, (start, end) in enumerate(paint):
            while start < end:
                jump = max(start + 1, line[start])
                worklog[i] += 1 if line[start] == 0 else 0
                line[start] = max(line[start], end)
                start = jump
        return worklog
