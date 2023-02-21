# Unique Paths
# https://leetcode.com/problems/unique-paths/
# Accepted 2023-02-21 23:24 UTC · Python · 31 ms · 13.8 MB

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n
        for i in range(1, m):
            curr = [1] + [0] * (n - 1)
            for j in range(1, n):
                curr[j] = curr[j - 1] + prev[j]
            prev = curr
        return prev[-1]
