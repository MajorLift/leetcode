# Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted 2023-03-15 22:28 UTC · Python · 507 ms · 15.2 MB

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = -1
        for i in range(n):
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
            if i >= max_reach and nums[i] == 0:
                return False
        return False
