# House Robber IV
# https://leetcode.com/problems/house-robber-iv/
# Accepted 2023-02-06 04:00 UTC · Python · 1398 ms · 26.2 MB

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def robs_K_or_more(capability):
            cnt, skips = 0, set()
            for i, num in enumerate(nums):
                if i in skips: continue
                if num <= capability:
                    cnt += 1
                    skips.add(i + 1)
            return cnt >= k

        return bisect_left(
            a=range(max(nums) + 1), 
            x=True, 
            lo=min(nums), 
            key=lambda x: robs_K_or_more(x)
        )
