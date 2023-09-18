# The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Accepted 2023-09-18 17:39 UTC · Python · 114 ms (22.14%) · 16.7 MB (70.98%)

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for _, i in nsmallest(k, [(sum(row), i) for i, row in enumerate(mat)])]
