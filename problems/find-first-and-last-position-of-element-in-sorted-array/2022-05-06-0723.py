# Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Accepted 2022-05-06 07:23 UTC · Python · 106 ms · 15.5 MB

class Solution:
    def __init__(self):
        self.min = +math.inf
        self.max = -math.inf
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        
        self.recurse(0, len(nums))
        return [self.min, self.max] if self.min != +math.inf or self.max != -math.inf else [-1, -1]
        
    def recurse(self, lo: int, hi: int) -> None:
        mid = lo + (hi - lo) // 2
        
        if hi - lo == 0 or (hi - lo == 1 and self.nums[mid] != self.target):
            return
        
        if self.nums[mid] == self.target:
            if mid < self.min:
                self.min = mid
                while (self.min > lo and self.nums[self.min - 1] == self.target):
                    self.min -= 1
            if mid > self.max:
                self.max = mid
                while (self.max < hi - 1 and self.nums[self.max + 1] == self.target):
                    self.max += 1
            return
        
        if self.nums[mid] < self.target: 
            self.recurse(mid + 1, hi)
        else:
            self.recurse(lo, mid)
