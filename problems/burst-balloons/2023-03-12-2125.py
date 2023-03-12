# Burst Balloons
# https://leetcode.com/problems/burst-balloons/
# Accepted 2023-03-12 21:25 UTC · Python · 7795 ms · 16.9 MB

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[0] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                for i in range(l, r + 1):
                    memo[l][r] = max(memo[l][r], 
                        (memo[l][i - 1] if i > 0 else 0)
                        + (nums[l - 1] if l > 0 else 1) 
                            * nums[i] 
                            * (nums[r + 1] if r < n - 1 else 1)
                        + (memo[i + 1][r] if i < n - 1 else 0))
        return memo[0][-1]
