# Two Sum
# https://leetcode.com/problems/two-sum/
# Accepted 2022-09-27 00:56 UTC · Python · 63 ms · 15.5 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {e: i for i,e in enumerate(nums)}
        # print(nums_dict)
        complements = [target - num for num in nums]
        for i, comp in enumerate(complements):
            if comp in nums_dict and nums_dict[comp] != i:
                return [i, nums_dict[comp]]
