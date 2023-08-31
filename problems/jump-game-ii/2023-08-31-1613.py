# Jump Game II
# https://leetcode.com/problems/jump-game-ii/
# Accepted 2023-08-31 16:13 UTC · Python · 111 ms · 17.4 MB

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = reach = cnt = 0
        while r < n - 1:
            reach = max(reach, *(i + nums[i] for i in range(l, r + 1)))
            l, r = r + 1, reach
            cnt += 1
        return cnt
