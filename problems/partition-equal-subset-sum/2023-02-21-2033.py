# Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
# Accepted 2023-02-21 20:33 UTC · Python · 1133 ms · 13.9 MB

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if total % 2 > 0:
            return False
        target = total // 2
        memo = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                if memo[i - num]:
                    memo[i] = True
        return memo[-1]
