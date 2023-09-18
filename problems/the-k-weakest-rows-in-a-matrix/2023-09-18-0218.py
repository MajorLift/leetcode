# The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Accepted 2023-09-18 02:18 UTC · Python · 94 ms (97.49%) · 16.6 MB (94.25%)

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = [(sum(row), i) for i, row in enumerate(mat)]
        heapify(pq)
        return [i for cnt, i in nsmallest(k, pq)]
