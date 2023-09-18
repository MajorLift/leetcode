# The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Accepted 2023-09-18 17:38 UTC · Python · 115 ms (19.03%) · 16.4 MB (99.87%)

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = [(sum(row), i) for i, row in enumerate(mat)]
        return [i for cnt, i in nsmallest(k, pq)]
