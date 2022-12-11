# Combination Sum
# https://leetcode.com/problems/combination-sum/
# Accepted 2022-12-11 08:06 UTC · Python · 99 ms · 14.1 MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(tmp = [], start = 0, remainder = target):
            if remainder == 0:
                output.append(tmp)
            if remainder > 0:
                [backtrack(tmp + [candidates[i]], i, remainder - candidates[i]) for i in range(start, len(candidates))]
        backtrack()
        return output
