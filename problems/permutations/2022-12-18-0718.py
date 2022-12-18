# Permutations
# https://leetcode.com/problems/permutations/
# Accepted 2022-12-18 07:18 UTC · Python · 70 ms · 14 MB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output: List[List[int]] = []
        def backtrack(tmp: List[int] = [], used: List[bool] = [False] * n):
            if len(tmp) == len(nums):
                output.append(tmp)
            for i in range(n):
                if not used[i]:
                    backtrack(tmp + [nums[i]], used[:i] + [True] + used[i+1:])
        backtrack()
        return output
