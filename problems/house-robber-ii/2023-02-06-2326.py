# House Robber II
# https://leetcode.com/problems/house-robber-ii/
# Accepted 2023-02-06 23:26 UTC · Python · 27 ms · 13.8 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3: return max(nums)
        memo = [[0 for _ in range(n + 1)] for _ in range(2)]
        for c in range(2):
            for i in range(n - 2, -1, -1):
                memo[c][i] = max(nums[(i + c) % n] + memo[c][i + 2], memo[c][i + 1])
        return max(memo[0][0], memo[1][0])
