# 3Sum
# https://leetcode.com/problems/3sum/
# Accepted 2023-02-02 08:42 UTC · Python · 7644 ms · 18.3 MB

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        hashmap = {num: i for i, num in enumerate(nums)}
        for k in range(len(nums) - 2):
            for i, j in self.twoSum(nums, -nums[k], k + 1):
                output.add(tuple(sorted([nums[k], nums[i], nums[j]])))
        return output
        
    def twoSum(self, nums, target, start):
        hashmap = {num: i for i, num in enumerate(nums)}
        output = []
        for i in range(start, len(nums)):
            if target - nums[i] in hashmap and hashmap[target - nums[i]] > i:
                output.append((i, hashmap[target - nums[i]]))
        return output
