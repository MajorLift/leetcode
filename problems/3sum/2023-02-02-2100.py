# 3Sum
# https://leetcode.com/problems/3sum/
# Accepted 2023-02-02 21:00 UTC · Python · 7068 ms · 18.4 MB

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.nums.sort()
        output = set()
        for k in range(len(nums) - 1, 1, -1):
            for i, j in self.twoSumSorted(0, k - 1, -nums[k]):
                output.add((nums[i], nums[j], nums[k]))
        return output
        
    def twoSumSorted(self, left, right, target):
        output = []
        while left < right:
            if self.nums[left] + self.nums[right] == target:
                output.append((left, right))
                left, right = left + 1, right - 1
            while left < len(self.nums) - 1 and self.nums[left] + self.nums[right] < target:
                left = max(left + 1, 
                    bisect_left(self.nums, target - self.nums[right], 
                        lo=left + 1, hi=right - 1))
            while right > 0 and self.nums[left] + self.nums[right] > target:
                right = min(right - 1, 
                    bisect_right(self.nums, target - self.nums[left], 
                        lo=left + 1, hi=right - 1))
        return output
