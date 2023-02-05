# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Accepted 2023-02-05 17:36 UTC · Python · 134 ms · 16 MB

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = max_right = -math.inf
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] > max_left:
                    max_left = height[l]
                else:
                    ans += max_left - height[l]
                l += 1
            else:
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    ans += max_right - height[r]
                r -= 1
        return ans
