# Unique Paths
# https://leetcode.com/problems/unique-paths/
# Accepted 2023-02-22 11:56 UTC · Python · 27 ms · 13.8 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(m + n - 2, n - 1)
