# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2022-10-18 05:17 UTC · Python · 1521 ms · 26.1 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        maxArea = 0
        while left < right:
            if height[left] <= height[right]:
                maxArea = max(maxArea, (right - left) * height[left])
                left += 1
            else:
                maxArea = max(maxArea, (right - left) * height[right])
                right -= 1
        return maxArea
