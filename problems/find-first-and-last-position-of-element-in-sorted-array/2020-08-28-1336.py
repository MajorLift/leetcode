# Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Accepted 2020-08-28 13:36 UTC · Python · 92 ms · 15.3 MB

class Solution:
    nums = []
    target = 0
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        
        mid = self.binarySearch(0, len(nums)-1)
        if mid == -1:
            return [-1,-1]
        lo = mid - 1
        while lo >= 0 and nums[lo] == target:
            lo -= 1
        lo += 1
        hi = mid + 1
        while hi < len(nums) and nums[hi] == target:
            hi += 1
        hi -= 1
        
        return [lo, hi]
        
    def binarySearch(self, lo, hi):
        if lo <= hi:        
            mid = lo + (hi - lo) // 2
            if self.nums[mid] > self.target:
                return self.binarySearch(lo, mid - 1)
            if self.nums[mid] < self.target:
                return self.binarySearch(mid + 1, hi)
            if self.nums[mid] == self.target:
                return mid
        return -1
