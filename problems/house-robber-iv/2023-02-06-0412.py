# House Robber IV
# https://leetcode.com/problems/house-robber-iv/
# Accepted 2023-02-06 04:12 UTC · Python · 1536 ms · 26.2 MB

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_valid(capability):
            cnt, skips = 0, set()
            for i in (idx for idx in range(len(nums)) if idx not in skips):
                if nums[i] <= capability:
                    cnt += 1
                    skips.add(i + 1)
            return cnt >= k

        return bisect_left(
            range(max(nums) + 1), 
            lo=min(nums),
            key=lambda x: is_valid(x),
            x=True)
