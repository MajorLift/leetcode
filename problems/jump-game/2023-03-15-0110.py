# Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted 2023-03-15 01:10 UTC · Python · 5850 ms · 42.1 MB

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dp(i):
            if i == n - 1:
                return True
            return any(dp(j) for j in range(min(i + nums[i], n - 1), i, -1))
        return dp(0)
