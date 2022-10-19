# Binary Search
# https://leetcode.com/problems/binary-search/
# Accepted 2022-10-19 22:15 UTC · Python · 315 ms · 15.5 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1
