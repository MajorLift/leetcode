# Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
# Accepted 2022-10-05 05:41 UTC · Python · 283 ms · 14 MB

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        nums = sorted(candidates)
        output = []
        def backtrack(tmp = [], start = 0, remainder = target):
            if remainder < 0:
                return
            if remainder == 0:
                output.append(tmp)
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(tmp + [nums[i]], i + 1, remainder - nums[i])
        backtrack()
        return output
