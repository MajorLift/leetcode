# Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# Accepted 2023-02-28 08:26 UTC · Python · 79 ms · 14.3 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = local_max = local_min = nums[0]
        for num in nums[1:]:
            local_max, local_min = max(num, local_max * num, local_min * num), \
                min(num, local_max * num, local_min * num)
            global_max = max(global_max, local_max)
        return global_max
