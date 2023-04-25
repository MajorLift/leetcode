# Maximum Number of Visible Points
# https://leetcode.com/problems/maximum-number-of-visible-points/
# Accepted 2023-04-25 22:22 UTC · Python · 2163 ms · 50.3 MB

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        arr = [degrees(atan2(y - y0, x - x0))
            for x, y in points 
            if (x, y) != (x0, y0)]
        arr.sort()
        arr += [e + 360 for e in arr]
         
        l = ans = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
        return ans + len(points) - len(arr) // 2
