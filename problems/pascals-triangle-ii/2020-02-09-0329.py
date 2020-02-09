# Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii/
# Accepted 2020-02-09 03:29 UTC · Python · 28 ms · 12.6 MB

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
