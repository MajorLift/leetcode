# Race Car
# https://leetcode.com/problems/race-car/
# Accepted 2023-05-02 15:44 UTC · Python · 806 ms · 30.3 MB

class Solution:
    def racecar(self, target: int) -> int:
        @cache
        def dp(target):
            if target == 0: return -1
            local_min = +inf
            cnt1 = dst1 = 1
            while dst1 < target:
                cnt2 = dst2 = 0
                while dst2 < dst1:
                    local_min = min(
                        local_min, 
                        cnt1 + 1 + cnt2 + 1 
                            + dp(target - (dst1 - dst2)))
                    cnt2 += 1
                    dst2 = (1 << cnt2) - 1
                cnt1 += 1
                dst1 = (1 << cnt1) - 1
            local_min = min(
                local_min, 
                cnt1 + 1 + dp(dst1 - target))
            return local_min
        return dp(target)
