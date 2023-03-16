# Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted 2023-03-16 22:13 UTC · Python · 122 ms · 15 MB

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = l = r = 0
        while (r < len(nums) - 1):
            reach = 0
            for i in range(l, r + 1):
                reach = max(reach, i + nums[i])
            l, r = r + 1, reach
            ans += 1
        return ans
