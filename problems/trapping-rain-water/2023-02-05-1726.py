# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Accepted 2023-02-05 17:26 UTC · Python · 155 ms · 16.3 MB

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = list(accumulate(height, max)), list(accumulate(height[::-1], max))[::-1]
        return sum([min(max_left[i], max_right[i]) - height[i] for i in range(len(height))])
