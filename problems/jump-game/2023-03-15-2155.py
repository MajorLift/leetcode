# Jump Game
# https://leetcode.com/problems/jump-game/
# Accepted 2023-03-15 21:55 UTC · Python · 450 ms · 15.4 MB

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= curr:
                curr = i
        return curr == 0
