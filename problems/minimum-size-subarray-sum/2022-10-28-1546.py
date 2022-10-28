# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Accepted 2022-10-28 15:46 UTC · Python · 624 ms · 27.1 MB

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        l = curr_sum = 0
        for r in range(n):
            curr_sum += nums[r]         
            while curr_sum >= target:
                ans = min(ans, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        return ans if ans <= n else 0
