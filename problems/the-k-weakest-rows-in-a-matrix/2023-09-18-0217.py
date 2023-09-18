# The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Accepted 2023-09-18 02:17 UTC · Python · 110 ms (38.27%) · 16.7 MB (70.98%)

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = [(sum(row), i) for i, row in enumerate(mat)]
        heapify(pq)
        return [heappop(pq)[1] for _ in range(k)]
