# Subsets
# https://leetcode.com/problems/subsets/
# Accepted 2022-10-01 06:13 UTC · Python · 34 ms · 14.1 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output: List[List[int]] = []
        def backtrack(tmp: List[int], start: int) -> None:
            nonlocal output
            output.append(tmp)
            for i in range(start, n):
                backtrack(tmp + [nums[i]], i + 1)
        backtrack([], 0)
        return output
