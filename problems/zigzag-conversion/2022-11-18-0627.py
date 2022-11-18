# Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/
# Accepted 2022-11-18 06:27 UTC · Python · 145 ms · 14.1 MB

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        mat = [[] for _ in range(numRows)]
        unit = numRows + numRows - 2
        for i, char in enumerate(s):
            idx = i % unit
            if idx < numRows:
                mat[idx].append(char)
            else:
                mat[-(2 + idx % numRows)].append(char)

        return "".join(["".join(row) for row in mat])
