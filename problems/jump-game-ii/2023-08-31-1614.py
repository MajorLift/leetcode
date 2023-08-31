# Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted 2023-08-31 16:14 UTC · Python · 110 ms · 17.4 MB

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = cnt = 0
        while r < n - 1:
            reach = max(i + nums[i] for i in range(l, r + 1))
            l, r = r + 1, reach
            cnt += 1
        return cnt
