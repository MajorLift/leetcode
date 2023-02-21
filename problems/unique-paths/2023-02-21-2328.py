# Unique Paths
# https://leetcode.com/problems/unique-paths/
# Accepted 2023-02-21 23:28 UTC · Python · 26 ms · 13.9 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))
