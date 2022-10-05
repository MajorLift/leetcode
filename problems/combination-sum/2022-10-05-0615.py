# Combination Sum
# https://leetcode.com/problems/combination-sum/
# Accepted 2022-10-05 06:15 UTC · Python · 49 ms · 13.9 MB

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        output = []
        def backtrack(tmp = [], start = 0, remainder = target):
            if remainder == 0:
                output.append(tmp)
            if remainder > 0:
                for i in range(start, n):
                    backtrack(tmp + [candidates[i]], i, remainder - candidates[i])
        backtrack()
        return output
