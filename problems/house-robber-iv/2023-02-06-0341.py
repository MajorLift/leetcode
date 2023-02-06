# House Robber IV
# https://leetcode.com/problems/house-robber-iv/
# Accepted 2023-02-06 03:41 UTC · Python · 1422 ms · 26 MB

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def condition(cap):
            i = takes = 0
            while i < len(nums):
                if nums[i] <= cap:
                    i += 1
                    takes += 1
                i += 1
            return takes >= k

        return bisect_left(range(max(nums) + 1), True, lo=min(nums), key=lambda cap: condition(cap))
