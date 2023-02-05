# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2023-02-05 04:43 UTC · Python · 748 ms · 27.4 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = -math.inf
        while l < r:
            width = r - l
            if height[l] <= height[r]:
                maxArea = max(maxArea, height[l] * width)
                l += 1
            else:
                maxArea = max(maxArea, height[r] * width)
                r -= 1
        return maxArea
