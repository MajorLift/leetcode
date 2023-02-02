# 3Sum
# https://leetcode.com/problems/3sum/
# Accepted 2023-02-02 04:26 UTC · Python · 7881 ms · 18.6 MB

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = set()
        for k in range(n - 1, 1, -1):
            res = self.twoSum(nums[:k], -nums[k])
            for i, j in res:
                output.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return output
    
    def twoSum(self, nums, target):
        hashmap = {e: i for i,e in enumerate(nums)}
        output = set()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                output.add(tuple(sorted([i, hashmap[complement]])))
        return output
