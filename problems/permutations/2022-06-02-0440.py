# Permutations
# https://leetcode.com/problems/permutations/
# Accepted 2022-06-02 04:40 UTC · Python · 45 ms · 14.1 MB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        def backtrack(first):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        backtrack(0)
        return output
