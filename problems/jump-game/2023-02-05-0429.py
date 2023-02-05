# Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted 2023-02-05 04:29 UTC · Python · 5835 ms · 42.1 MB

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dp(i):
            if i == len(nums) - 1: return True
            return any(dp(j) for j in range(min(i + nums[i], len(nums) - 1), i, -1))
        return dp(0)
