# The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Accepted 2023-09-18 17:27 UTC · Python · 109 ms (44.08%) · 16.7 MB (38.2%)

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for i, _ in sorted(enumerate(mat), key=lambda x: (sum(x[1]), x[0]))[:k]]
