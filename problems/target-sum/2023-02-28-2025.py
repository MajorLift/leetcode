# Target Sum
# https://leetcode.com/problems/target-sum/
# Accepted 2023-02-28 20:25 UTC · Python · 301 ms · 14 MB

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        prev = [0] * (2 * total + 1)
        prev[total + nums[0]] = 1
        prev[total - nums[0]] += 1
        for i in range(1, n):
            curr = [0] * (2 * total + 1)
            for acc in range(-total, total + 1):
                if prev[acc + total] > 0:
                    curr[acc + total + nums[i]] += prev[acc + total]
                    curr[acc + total - nums[i]] += prev[acc + total]
            prev = curr
        return prev[target + total] if abs(target) <= total else 0
