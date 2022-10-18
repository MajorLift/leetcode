# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2022-10-18 05:20 UTC · Python · 1846 ms · 27.4 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        maxArea, width = 0, n - 1
        while left < right:
            if height[left] <= height[right]:
                maxArea = max(maxArea, width * height[left])
                left += 1
            else:
                maxArea = max(maxArea, width * height[right])
                right -= 1
            width -= 1
        return maxArea
