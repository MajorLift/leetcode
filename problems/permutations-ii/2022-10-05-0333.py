# Permutations II
# https://leetcode.com/problems/permutations-ii/
# Accepted 2022-10-05 03:33 UTC · Python · 191 ms · 14.3 MB

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output: List[List[int]] = []
        nums = sorted(nums)
        def backtrack(tmp: List[int] = [], used: List[bool] = [False] * n) -> None:
            nonlocal output, nums
            if len(tmp) == len(nums):
                output.append(tmp)
                return
            for i in range(n):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and used[i - 1]):
                    continue
                backtrack(tmp + [nums[i]], used[:i] + [True] + used[i+1:])
        backtrack()
        return output
