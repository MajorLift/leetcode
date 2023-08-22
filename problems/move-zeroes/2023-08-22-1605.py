# Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Accepted 2023-08-22 16:05 UTC · Python · 7769 ms · 18 MB

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                j = i
                while j < len(nums) - 1 and nums[j + 1] != 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    j += 1
