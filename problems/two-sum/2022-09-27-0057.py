# Two Sum
# https://leetcode.com/problems/two-sum/
# Accepted 2022-09-27 00:57 UTC · Python · 121 ms · 15.1 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
