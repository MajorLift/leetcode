# Student Attendance Record II
# https://leetcode.com/problems/student-attendance-record-ii/
# Accepted 2023-04-30 19:24 UTC · Python · 3947 ms · 741.8 MB

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(k, absent):
            if k < 3:
                if absent == 1:
                    return [1, 2, 4][k]
                if absent == 0:
                    return [1, 3, 8][k]
            if absent == 1:
                return sum([
                    dp(k - 1, 1),
                    dp(k - 2, 1),
                    dp(k - 3, 1),
                ]) % MOD
            if absent == 0:
                return (sum([
                    dp(k - 1, 0),
                    dp(k - 2, 0),
                    dp(k - 3, 0),
                ]) + dp(k, 1)) % MOD
        
        return dp(n, 0) % MOD
