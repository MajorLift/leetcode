# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2022-10-18 05:17 UTC · Python · 1858 ms · 27.4 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        maxArea = 0
        while left < right:
            maxArea = max(maxArea, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
