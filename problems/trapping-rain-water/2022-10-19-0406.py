# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Accepted 2022-10-19 04:06 UTC · Python · 150 ms · 16.1 MB

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        ldp, rdp = [height[0]] + [0] * (n - 1), [0] * (n - 1) + [height[-1]]
        for i in range(1, n):
            ldp[i] = max(ldp[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            rdp[i] = max(rdp[i + 1], height[i])
        for i in range(n):
            ans += min(ldp[i], rdp[i]) - height[i]
        return ans
