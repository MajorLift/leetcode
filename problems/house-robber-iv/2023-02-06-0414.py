# House Robber IV
# https://leetcode.com/problems/house-robber-iv/
# Accepted 2023-02-06 04:14 UTC · Python · 812 ms · 26.1 MB

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_valid(capability):
            cnt, skip = 0, False
            for num in nums:
                if skip:
                    skip = False
                    continue
                if num <= capability:
                    cnt += 1
                    skip = True
            return cnt >= k

        return bisect_left(
            a=range(max(nums) + 1), 
            lo=min(nums),
            key=lambda val: is_valid(val),
            x=True)
