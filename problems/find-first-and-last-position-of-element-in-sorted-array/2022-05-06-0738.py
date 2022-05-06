# Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Accepted 2022-05-06 07:38 UTC · Python · 144 ms · 15.4 MB

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        
        foundRange = self.binarySearch(0, len(nums))
        if foundRange is None:
            return [-1, -1]
        lo, mid, hi = foundRange
        min = max = mid
        
        while min > lo and nums[min - 1] == target:
            min -= 1
        while max < hi - 1 and nums[max + 1] == target:
            max += 1
        return [min, max]
        
    def binarySearch(self, lo: int, hi: int) -> int or None:        
        if hi - lo <= 0:
            return
        
        mid = lo + (hi - lo) // 2
        
        if self.nums[mid] < self.target: 
            return self.binarySearch(mid + 1, hi)
        elif self.nums[mid] > self.target:
            return self.binarySearch(lo, mid)
        else:
            return lo, mid, hi
