# Race Car
# https://leetcode.com/problems/race-car/
# Accepted 2023-05-02 16:00 UTC · Python · 844 ms · 31.6 MB

class Solution:
    def racecar(self, target: int) -> int:
        @cache
        def dp(target):
            if target == 0: 
                return -1
            ans = +inf
            for cnt1 in range(15):
                dist1 = (1 << cnt1) - 1
                if dist1 >= target: break
                for cnt2 in range(15):
                    dist2 = (1 << cnt2) - 1
                    if dist2 >= dist1: break
                    ans = min(
                        ans, 
                        cnt1 + 1 + cnt2 + 1
                            + dp(target - (dist1 - dist2)))
            ans = min(
                ans, 
                cnt1 + 1 + dp(dist1 - target))
            return ans

        return dp(target)
