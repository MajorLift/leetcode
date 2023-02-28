# Target Sum
# https://leetcode.com/problems/target-sum/
# Accepted 2023-02-28 20:19 UTC · Python · 393 ms · 14.3 MB

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        memo = [([0] * (2 * total + 1)) for _ in range(n)]
        memo[0][total + nums[0]] = 1
        memo[0][total - nums[0]] += 1
        for i in range(1, n):
            for acc in range(-total, total + 1):
                if memo[i - 1][acc + total] > 0:
                    memo[i][acc + total + nums[i]] += memo[i - 1][acc + total]
                    memo[i][acc + total - nums[i]] += memo[i - 1][acc + total]
        return memo[n - 1][target + total] if abs(target) <= total else 0
